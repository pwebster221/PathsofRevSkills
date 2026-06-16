#!/usr/bin/env python3
"""Trigger eval runner for a dubtown skill.

A skill is loaded almost entirely off its SKILL.md `description` field. This runner
checks that the description still triggers correctly:

  * STRUCTURAL checks (always run, no network): the eval file is well-formed, the
    two prompt sets are disjoint, the named skill exists and has a description.
  * LIVE judge (optional): if ANTHROPIC_API_KEY is set and --judge is passed, each
    prompt is shown to a model alongside the description, the model decides whether
    the skill would fire, and the verdict is scored against the eval's expectation.
    Without a key the live check is skipped (and that is not a failure).

Usage:
    python3 run_evals.py                  # structural checks for this skill
    python3 run_evals.py --judge          # also run the live triggering judge
    python3 run_evals.py --evals PATH     # point at a different evals.json
    python3 run_evals.py --skill-dir DIR  # eval a different skill folder

Exit code is non-zero if any enabled check fails (CI-friendly). Stdlib only.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

# Resolve paths relative to this script: scripts/ -> skill root -> evals/evals.json
SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_ROOT = SCRIPT_DIR.parent

API_URL = "https://api.anthropic.com/v1/messages"
MODEL = os.environ.get("EVAL_MODEL", "claude-sonnet-4-6")


# --- loading -----------------------------------------------------------------

def read_description(skill_dir: Path) -> str:
    """Pull the `description:` value out of a SKILL.md YAML frontmatter block."""
    skill_md = skill_dir / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        raise ValueError(f"{skill_md}: no YAML frontmatter found")
    front = m.group(1)
    # description may be a folded block scalar (`description: >-`) or inline.
    dm = re.search(r"^description:\s*(>[-+]?|\|[-+]?)?[ \t]*\n?(.*?)(?=^\w[\w-]*:|\Z)",
                   front + "\n", re.DOTALL | re.MULTILINE)
    if not dm:
        raise ValueError(f"{skill_md}: no description field")
    body = dm.group(2) if dm.group(1) else dm.group(2).splitlines()[0] if dm.group(2) else ""
    return " ".join(line.strip() for line in body.strip().splitlines()).strip()


def normalize_cases(raw: list) -> list[dict]:
    """Accept either bare strings or {prompt, winner} objects."""
    out = []
    for item in raw:
        if isinstance(item, str):
            out.append({"prompt": item, "winner": None})
        elif isinstance(item, dict) and "prompt" in item:
            out.append({"prompt": item["prompt"], "winner": item.get("winner")})
        else:
            raise ValueError(f"bad eval case: {item!r}")
    return out


# --- structural checks -------------------------------------------------------

def structural_checks(evals: dict, skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill = evals.get("skill")
    if not skill:
        errors.append("evals.json: missing 'skill'")
    if skill and skill_dir.name != skill:
        errors.append(f"skill name '{skill}' != folder '{skill_dir.name}'")
    if not (skill_dir / "SKILL.md").exists():
        errors.append(f"{skill_dir}/SKILL.md does not exist")
    else:
        try:
            desc = read_description(skill_dir)
            if len(desc) < 40:
                errors.append("SKILL.md description looks too short to trigger reliably")
        except ValueError as e:
            errors.append(str(e))

    pos = normalize_cases(evals.get("should_trigger", []))
    neg = normalize_cases(evals.get("should_not_trigger", []))
    if not pos:
        errors.append("no should_trigger prompts")
    if not neg:
        errors.append("no should_not_trigger prompts")

    pos_set = {c["prompt"].strip().lower() for c in pos}
    neg_set = {c["prompt"].strip().lower() for c in neg}
    overlap = pos_set & neg_set
    if overlap:
        errors.append(f"prompts in BOTH lists: {sorted(overlap)}")
    for label, cases in (("should_trigger", pos), ("should_not_trigger", neg)):
        seen = set()
        for c in cases:
            key = c["prompt"].strip().lower()
            if key in seen:
                errors.append(f"{label}: duplicate prompt {c['prompt']!r}")
            seen.add(key)
            if not c["prompt"].strip():
                errors.append(f"{label}: empty prompt")
    return errors


# --- live judge (optional) ---------------------------------------------------

def judge_prompt(description: str, skill: str, prompt: str, api_key: str) -> bool:
    """Ask the model whether this skill's description would fire on the prompt."""
    system = (
        "You decide whether a Claude 'skill' should activate for a user prompt. "
        "You are given the skill's description (its trigger spec) and one user prompt. "
        "Answer with exactly one token: YES if the skill should load, NO if it should not."
    )
    user = (
        f"SKILL: {skill}\n"
        f"DESCRIPTION:\n{description}\n\n"
        f"USER PROMPT:\n{prompt}\n\n"
        "Should this skill load? Answer YES or NO."
    )
    payload = json.dumps({
        "model": MODEL,
        "max_tokens": 5,
        "system": system,
        "messages": [{"role": "user", "content": user}],
    }).encode("utf-8")
    req = urllib.request.Request(API_URL, data=payload, method="POST", headers={
        "content-type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
    })
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read())
    text = "".join(b.get("text", "") for b in data.get("content", [])).strip().upper()
    return text.startswith("Y")


def live_checks(evals: dict, skill_dir: Path, api_key: str) -> tuple[int, int, list[str]]:
    skill = evals["skill"]
    desc = read_description(skill_dir)
    pos = normalize_cases(evals.get("should_trigger", []))
    neg = normalize_cases(evals.get("should_not_trigger", []))
    passed = failed = 0
    failures: list[str] = []
    for expected, cases in ((True, pos), (False, neg)):
        for c in cases:
            try:
                got = judge_prompt(desc, skill, c["prompt"], api_key)
            except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
                failures.append(f"  API error on {c['prompt']!r}: {e}")
                failed += 1
                continue
            ok = got == expected
            mark = "PASS" if ok else "FAIL"
            arrow = "fire" if got else "skip"
            want = "fire" if expected else "skip"
            print(f"  [{mark}] want={want:4} got={arrow:4}  {c['prompt']}")
            if ok:
                passed += 1
            else:
                failed += 1
                extra = f" (expected {c['winner']} to win)" if c.get("winner") and not expected else ""
                failures.append(f"  {c['prompt']!r}: wanted {want}, got {arrow}{extra}")
    return passed, failed, failures


# --- main --------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="Trigger eval runner for a dubtown skill.")
    ap.add_argument("--skill-dir", type=Path, default=SKILL_ROOT,
                    help="skill folder (default: this script's skill)")
    ap.add_argument("--evals", type=Path, default=None,
                    help="path to evals.json (default: <skill-dir>/evals/evals.json)")
    ap.add_argument("--judge", action="store_true",
                    help="run the live LLM triggering judge (needs ANTHROPIC_API_KEY)")
    args = ap.parse_args()

    skill_dir = args.skill_dir.resolve()
    evals_path = (args.evals or skill_dir / "evals" / "evals.json").resolve()

    if not evals_path.exists():
        print(f"ERROR: evals file not found: {evals_path}", file=sys.stderr)
        return 2
    evals = json.loads(evals_path.read_text(encoding="utf-8"))

    print(f"== structural checks: {evals.get('skill', '?')} ==")
    errors = structural_checks(evals, skill_dir)
    if errors:
        for e in errors:
            print(f"  [FAIL] {e}")
        print(f"\n{len(errors)} structural error(s).")
        return 1
    pos_n = len(evals.get("should_trigger", []))
    neg_n = len(evals.get("should_not_trigger", []))
    print(f"  [PASS] well-formed; {pos_n} should-trigger / {neg_n} should-not-trigger; lists disjoint.")

    if not args.judge:
        print("\nLive triggering judge not run (pass --judge to enable). Structural checks passed.")
        return 0

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("\n--judge requested but ANTHROPIC_API_KEY is not set; skipping live check.")
        print("Structural checks passed.")
        return 0

    print(f"\n== live triggering judge (model={MODEL}) ==")
    passed, failed, failures = live_checks(evals, skill_dir, api_key)
    print(f"\nlive: {passed} passed, {failed} failed")
    if failures:
        print("failures:")
        for f in failures:
            print(f)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
