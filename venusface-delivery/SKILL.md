---
name: venusface-delivery
description: The proven VenusFace feature-delivery loop — branch, build, test, live visual smoke via the loopback bridge, PR, bot-review fixes, merge verification, and the two deploy paths (web-only fast vs migration-hardened). Use for any VenusFace (CT 525) change, and as a template for other CT-hosted FastAPI+SPA services.
---

# VenusFace delivery loop

Proven across PRs #29–#37 (R4 pins → R6 gallery, PoR polish, genesis retention).
Working clone: `/root/venusface-build` (host, gh write). Box: CT 525 `/opt/venusface`
(SSH read-only deploy key). Full deploy runbook lives in memory
`project_venusface_deploy.md` — this skill is the loop around it.

## 1. Branch + build

- `git checkout main && git pull --ff-only origin main && git checkout -b feat/<name>`
  — ALWAYS from fresh main. Never commit follow-up work onto an already-merged
  PR branch (did it once; the PR diff survives but the branch history confuses).
- Schema changes: **any new `deck_card`/`assets`/`deck_canon` column must be added to
  EVERY explicit column list** — `branch_from_checkpoint` inserts, `reset_deck`
  blanks, asset-clone loops. Snapshots are `SELECT *`; only the writers drift.
  Codex caught this class on BOTH schema PRs. Grep `INSERT INTO <table>` +
  `UPDATE <table> SET` before calling a migration done.
- Arity/validation tables exist at TWO layers (engine `_TRACK_REF_ARITY` pre-spend
  + db `_TRACK_SOURCE_ARITY` post-render). Relax them TOGETHER or a run fails
  after billing.
- Test-harness trap: majors 1–21 aren't in the fresh-DB card_template skeleton —
  `upsert_card` BEFORE `create_deck` or the new deck seeds no deck_card row and
  writes silently no-op.

## 2. Gates (host)

- py: `.venv/bin/python -m pytest -q` (uv-synced venv in the clone).
- web: `cd web && npx vitest run && npm run build`.
- Schema-validated endpoints: yaml doc updates race a running suite — rerun after
  editing `docs/schema/*.yaml`.

## 3. Live visual smoke (pre-merge, real data)

The box API is loopback-bound. Bridge it temporarily:

1. Background `pct exec 525 -- python3` TCP forwarder: bind `10.20.0.156:18300`
   → `127.0.0.1:8300` (threading pipe loop — script in memory
   `reference_loopback_smoke_bridge.md`).
2. Host: `VENUSFACE_API=http://10.20.0.156:18300 npx vite --port 5199 --strictPort`
   (vite proxy target is env-overridable; NEVER pipe vite through `head` — the
   pipe closing on config reload SIGPIPE-kills the server).
3. Screenshot: `/opt/google/chrome/chrome --headless=new --no-sandbox --disable-gpu
   --window-size=1440,1200 --virtual-time-budget=9000 --screenshot=out.png <url>`.
   (Playwright MCP loses its sandbox config on reconnect; headless chrome is the
   reliable fallback. One flag set per invocation — extra `--evaluate-on-new-document`
   style flags trip "multiple targets".)
4. TEARDOWN: TaskStop both; then verify the forwarder inside the CT with
   `pct exec 525 -- pgrep -f 'socket.create_connection'` — pattern must NOT appear
   in your own checker command line (pgrep/pkill self-match: the checking bash
   matches itself, and pkill can kill its own shell, exit 137).

## 4. PR + bot review loop

- `gh pr create` with verification evidence in the body. `gh pr merge` is
  classifier-blocked — the operator merges.
- Bots (Codex, blocks.team) find real bugs nearly every PR. For each inline
  comment: fix, add a regression test, push, REPLY on the thread naming the
  commit, THEN resolve. **Never bulk-resolve threads you haven't read** — sweep
  `isResolved==false` only AFTER addressing every comment (resolved one unread
  once; had to confess).
- A finding can be wrong in the details but right in substance (e.g. the design's
  feeds-tags); reply with the correction, don't blindly comply.

## 5. Merge verification (remote-control operators race you)

When the operator says "merged":
- `gh pr view N --json state,mergedAt` AND `git fetch && git merge-base
  --is-ancestor <your-last-sha> origin/main`.
- A merge can land BEFORE your final push (PR #29 raced the letterbox commit —
  orphaned on the branch, needed a follow-up PR) or the operator's click can
  silently fail (#30, #33 "merged" while state=OPEN). Never deploy on the word
  alone; never announce a fix deployed that ancestry doesn't confirm.

## 6. Deploy (two paths)

- **Web-only** (`git diff --name-only <box-sha> origin/main | grep -v '^web/'`
  empty): pull + `npm ci && npm run build` — NO restart (FastAPI serves web/dist
  live), no jobs risk, no gate needed. Probe: served bundle hash matches dist.
- **Python/migration**: full hardened runbook — `pct pull` DB backup FIRST,
  jobs-running check, single pct-exec pipeline (pull → build → pytest gate →
  RE-CHECK jobs → restart), probe NEW behavior on the RUNNING process (a served
  field, a migrated column via the venv's sqlite3 — no sqlite3 CLI on the box).
- After deploy: update `project_venusface_decks.md` memory with the arc state.
