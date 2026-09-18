# dubtown-skills

Canonical skill repository for the DubTown / Journeyman ecosystem. This repo is the
**single source of truth** for agent skills. SkillServer syncs from it (read-only) and
serves the skills to every consumer — LocalAGI, Claude Code, Alder, and any other MCP/REST client.

## Rules of the road

- **One origin.** Skills are authored here and nowhere else. Other machines clone to
  contribute; SkillServer only ever pulls. Nothing authors locally against a synced copy.
- **One folder per skill.** Each skill is a directory containing a `SKILL.md`. Standalone
  skills live at the top level; related skills are grouped one level down inside a family
  folder (`major-personas/`, `minor-personas/`, `majestic-personas/`,
  `major-arcana-perspectives/`, `sdlc/`).
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

### Standalone skills

| Skill | Domain |
|-------|--------|
| `path-of-reverence-brand` | Path of Reverence brand / design system |
| `coding-bible` | Universal engineering standards (DubTown / PoR) |
| `esoteric-synthesis` | Symbolic synthesis across the esoteric system |
| `metaphysical-conversation` | Contemplative dialogue |
| `tarot-interpretation` | Card interpretation (The 78) |
| `atomic-tarot-reading` | Atomic reading form — span cards over the decan layer |
| `mythic-chart-reading` | Natal chart read as myth through the persona + perspective layers |
| `horary-consultation` | Horary consultation |
| `generative-principle` | UNC research / number 1–21 exploration |
| `mani-api` | Mani Protocol v31 cognitive-attunement MCP guide |
| `venusface-delivery` | The proven CT 525 feature-delivery loop |
| `d1-decan-reading` | Register performance — Triune Arcanum I.1 Decan Minors |
| `d2-ace-reading` | Register performance — Triune Arcanum I.2 Elemental Aces |
| `d3-page-reading` | Register performance — Triune Arcanum I.3 Throne Pages |
| `d4-court-reading` | Register performance — Triune Arcanum I.4 Courts |

### Skill families

| Family | Contents |
|--------|----------|
| `major-personas/` | 22 Majors as operational persona instruments |
| `minor-personas/` | 36 pips (Twos–Tens, four suits) as situation instruments |
| `majestic-personas/` | 20 court/ace instruments mapped to MBTI types and functions |
| `major-arcana-perspectives/` | Station-perspective instruments for the Majors (witness layer) |
| `sdlc/` | 35 software-development-lifecycle skills (discovery through sustain) |

### Non-skill folders

`notes/` (reading transcripts) and `venusface-distill/` (style distillation documents)
are reference material, not skills.

## Persona skills are operational (ruling 2026-09-10)

The 78 persona skills (majestic-personas/ · major-personas/ · minor-personas/) no longer carry
their instrument as a declarative prompt. Each SKILL.md now defines the **MCP setup for its
archetype**, keyed to the exact card name: `persona_kit` (anchor, Trellis declaration,
evidence-grounded portrait, crossread) as the perspective and system prompt; `mcp_moment` with
`as_card` as the viewpoint on content; the reading's payload as content; resonance scoring as
the judge (the Recognition Pass). The former declarative prompts are preserved verbatim at
`<skill>/references/retired-declarative.md` — historical reference and engine-down fallback.
