# dubtown-skills

Canonical skill repository for the DubTown / Journeyman ecosystem. This repo is the
**single source of truth** for agent skills. SkillServer syncs from it (read-only) and
serves the skills to every consumer — LocalAGI, Claude Code, Alder, and any other MCP/REST client.

## Rules of the road

- **One origin.** Skills are authored here and nowhere else. Other machines clone to
  contribute; SkillServer only ever pulls. Nothing authors locally against a synced copy.
- **One folder per skill.** Each top-level directory is a skill and must contain a `SKILL.md`.
- **The directory name must match the `name:` field** in that skill's frontmatter.

## Skill layout

```
skill-name/
├── SKILL.md          # required: YAML frontmatter (name, description) + instructions
├── references/       # optional: docs loaded on demand (palettes, schemas, rule sheets)
├── scripts/          # optional: executable helpers
└── assets/           # optional: templates, icons, static files
```

## Writing the SKILL.md

Two fields are required: `name` and `description`.

The **`description` is the trigger** — the agent decides whether to load the skill almost
entirely from this field. Write it as *when to use this and what it does*, and lean slightly
assertive: state the contexts that should fire it, including ones where the user won't say the
skill's name outright. Under-triggering is the common failure, not over-triggering.

Keep the body focused (ideally under ~500 lines). Push deep material into `references/` and
point to it from the body, so it loads only when needed.

## Current skills

| Skill | Domain | Status |
|-------|--------|--------|
| `path-of-reverence-brand` | Brand / design system | slot — paste existing brand book |
| `coding-bible` | Engineering standards | slot — paste existing bible |
| `esoteric-exploration` | Symbolic synthesis | new — flesh out |
| `metaphysical-conversation` | Contemplative dialogue | new — flesh out |
| `tarot-interpretation` | Card interpretation (The 78) | active |
| `generative-principle` | UNC research / number 1–21 exploration | active |
| `d1-decan-reading` | Register performance — Triune Arcanum I.1 Decan Minors | active |
| `d2-ace-reading` | Register performance — Triune Arcanum I.2 Elemental Aces | active |
| `d3-page-reading` | Register performance — Triune Arcanum I.3 Throne Pages | active |
