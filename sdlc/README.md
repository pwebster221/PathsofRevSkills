# dubtown-skills / sdlc

A two-tier agentic skill library for selecting and applying SDLC methodology
**postures** — the discipline of choosing *how* to build based on the context
signals in front of you, not habit.

## The two tiers

| Tier | Role | What it does |
|---|---|---|
| **1 — Navigator** | `role: navigator` | One per SDLC stage (discovery, design, build, verify, ship, sustain). Reads context signals and routes to a posture. |
| **2 — Posture skill** | `role: skill` | A specific methodology (TDD, BDD, Cleanroom, GitOps, SRE…). Self-contained and directly loadable. |

The stages form the lifecycle spine:

```
discovery → design → build → verify → ship → sustain
```

## How an agent uses this repo

1. **Load `MANIFEST.yaml` first.** It is the complete routing index — every skill,
   its tier, stage, path, routing signals, and backing PDFs. An agent never has to
   scan folders to decide what to load.
2. **Pick the stage navigator** for the work at hand (e.g. `sdlc-build`).
3. **Read its signals**, score the context, and route to the posture whose
   `signals_favored` best matches (e.g. `sdlc-tdd`).
4. **Load that posture's `SKILL.md`** and apply it. Open `references/SOURCES.md`
   when provenance or deeper reading is needed.

## Layout

```
sdlc/
├── MANIFEST.yaml        ← routing index — load this first
├── README.md            ← this file
├── SKILL-TEMPLATE.md    ← canonical template for new skills
│
├── sdlc-<id>/
│   ├── SKILL.md         ← frontmatter (name, stage, tier, role…) + the skill body
│   └── references/
│       └── SOURCES.md   ← PDF-library pointers + external canonical sources
│
├── Software_Development_Methodologies_PDFs/   ← shared evidence library (00_INDEX.md)
└── _original_txt/       ← pre-reorg source files, kept for reference; safe to delete
```

6 navigators + 27 postures = **33 skills**.

## Adding a new skill

1. Copy `SKILL-TEMPLATE.md` to `sdlc-<your-id>/SKILL.md` and fill the frontmatter
   and body.
2. Add a `references/SOURCES.md` pointing at the relevant PDFs in the shared library
   (`../../Software_Development_Methodologies_PDFs/NN_Name.pdf`) and any external
   canonical sources.
3. Register the skill in `MANIFEST.yaml` under its stage, with `signals_favored`
   (Tier 2) or `signals` (Tier 1) and its `references`.

## Provenance note

`references/SOURCES.md` files point into the shared PDF library catalogued in
`Software_Development_Methodologies_PDFs/00_INDEX.md`. Entries 24–27 are 2024–2025
preprints/whitepapers on the agentic-AI frontier — treat as emerging evidence, not
settled practice.
