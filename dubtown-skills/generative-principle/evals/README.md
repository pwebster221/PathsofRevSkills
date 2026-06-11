# Trigger evals — generative-principle

A skill loads almost entirely off its `SKILL.md` `description`. These evals pin down
*when it should fire* so a future edit to the description can't silently break it.

- **`evals.json`** — two prompt sets. `should_trigger` must load the skill;
  `should_not_trigger` must not (each names the skill that should win instead). The
  close call is `tarot-interpretation`: *deriving the 1–21 structure* fires this skill,
  *reading actual cards* fires that one.

## Running

```bash
# structural checks only — no network, CI-friendly
python3 ../scripts/run_evals.py

# also run the live LLM triggering judge (needs an API key)
ANTHROPIC_API_KEY=sk-... python3 ../scripts/run_evals.py --judge
```

The runner always validates structure (well-formed, lists disjoint, skill + description
exist). With `--judge` and a key set, it shows each prompt to a model alongside the
description, asks whether the skill would fire, and scores the verdict against the
expectation. Without a key, the live step is skipped (not a failure). Exit code is
non-zero if an enabled check fails.

When you edit the SKILL.md description, re-run with `--judge` and confirm every
should-trigger still fires and no should-not-trigger starts firing. Add new prompts here
whenever a real-world phrasing surprises you in either direction.
