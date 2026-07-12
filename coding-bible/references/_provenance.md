# Provenance — coding-bible mirror

## Sources & propagation (3-tier)

The coding bible exists in three locations with one directional propagation flow.

| Tier | Location | Role |
|---|---|---|
| **Authoring (upstream)** | `/Users/dubtownraces/Development/ProgrammingStandards/ProgrammingStandards-Rules/UPDATED-Code-Brand-Truth/coding-bible.md` | Where Paul writes the canon. v1 (2026-05-16). Owner: paul.webster@dubtowndesigns.com. |
| **Runtime SOT (THIS TREE)** | `/root/.hermes/skills/dubtown/coding-bible/` | **Primary SOT for the Hermes agent runtime.** The canon read when the skill auto-loads. Subagents spawned via `delegate_task` pull from here via `skill_view('coding-bible')`. This is the file the agent actually reads. |
| **Redistribution mirror** | `/root/.hermes/plugins/dubtown-standards/skills/coding-bible/` | Claude Code plugin artifact for sharing the canon out to other Claude Code environments. **Derived from the runtime SOT — do not edit directly.** |

**Propagation flow:** authoring → runtime SOT → redistribution mirror.

When the upstream canon changes:

1. Re-mirror into the runtime SOT (this tree) first — the Hermes agent reads from here, including any spawned subagents.
2. Then propagate to the plugin tree via `/canon-mirror-sync --apply` from a Claude Code session, or a plain `cp -r`. The plugin tree is for redistribution to other Claude Code environments, not for the Hermes agent.

**Never edit the redistribution mirror directly** — drift from the runtime SOT silently breaks subagent canon access without surfacing anywhere visible.

Version mirrored: **v1 (2026-05-16)**, built to **PoR Brand System v1**.
Owner: paul.webster@dubtowndesigns.com

## What is mirrored, and where

| Reference file | Source location | Last mirrored |
|---|---|---|
| `coding-bible-full.md` | `coding-bible.md` (entire file) | 2026-05-18 |
| `coding-rules.md` | `coding-bible.md` § Part III (Coding Rules) | 2026-05-18 |
| `gotchas-load-bearing.md` | Distilled from every ▲ line across the canon | 2026-05-18 |

`frameworks.md` (§ Part I), `programs.md` (§ Part II), and `cross-reference-appendix.md`
(§ Appendix) are deferred — `coding-bible-full.md` covers them, and the SKILL.md surfaces
the most-used rules. Add a sectional mirror when a section starts being read frequently
in isolation.

## Sync ritual

When `coding-bible.md` changes:

1. Read the diff. Identify which entries changed.
2. Overwrite `coding-bible-full.md` with the new full source. Bump "Last mirrored."
3. If the change touches a rule in Part III, update `coding-rules.md` and re-derive
   the relevant Gotcha lines in `gotchas-load-bearing.md`.
4. If the change adds a new Framework or Program, no derived file needs updating yet —
   the full mirror covers it.
5. Bump the version note in the parent SKILL.md frontmatter description if the change
   alters triggering surface (new framework, new container ID range, new hostname zone).
   Pure content updates inside an existing entry do not require a description bump.
6. Re-run the trigger benchmark in `.claude/skills/evals/evals.json` if any change
   touches triggering.

## What is NOT mirrored

- **Three-Duality archetype sigils** are defined in `brand-system.md` §5.2 and live in
  the `paths-of-reverence-brand` skill. This skill *references* them for service
  classification but does not duplicate the canonical home. One home per fact.
- **Esoteric Diction tier definitions** likewise live in `brand-system.md` §6. This
  skill cites them in agent behavior rules (`don't default to Deep`) and points readers
  at `paths-of-reverence-brand/references/tiers.md`.
- **Live infrastructure facts** (current ports, IPs, container IDs in flux) are sourced
  from `/root/CLAUDE.md` per the canon's preamble. This skill mirrors the *conventions
  about* infrastructure, not the live state.

## Why Mirror, not Pointer

The decision (made 2026-05-18) was that agent latency on the rule-of-conduct lookups is
high-frequency enough that one extra file read across the `UPDATED-Code-Brand-Truth/`
boundary materially slows agent loops. Mirror trades a small drift risk (mitigated by
this ritual) for predictable in-context access.
