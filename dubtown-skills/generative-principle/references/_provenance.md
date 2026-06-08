# Provenance — generative-principle

## Source of truth

The canonical, live source is the **Linear project "Generative Principle"** (team PAT, Paths of
Reverence):

```
https://linear.app/paths-of-reverence/project/generative-principle-9c95ff0c599b
```

Owner: paul.webster@dubtowndesigns.com

The per-number issues **PAT-212 → PAT-232** (1 → 21, id = 211 + N) and the cross-cutting
discovery issues (PAT-449, 450, 470–479) are authoritative. This skill is a **pointer**, not a
mirror: the bundled `references/` files are an *offline snapshot for orientation*. Pull the live
issue (`get_issue PAT-2NN`) whenever a working session needs full prose — depth accrues in Linear
and these snapshots lag.

## What is bundled, and from where

| Reference file | Source | Last synced |
|---|---|---|
| `number-index.md` | Linear `list_issues` (project) + `MajorArcana` nodes | 2026-06-08 |
| `operational-grammars.md` | PAT-214 (multiplicative), PAT-473 (sequential), PAT-213 (Generate-prime) | 2026-06-08 |
| `unc-structure.md` | Project description + PAT-470 (septenaries), PAT-471 (pillars), PAT-478 (prime taxonomy) | 2026-06-08 |

The grammar content in `operational-grammars.md` is a near-verbatim distillation of the deep
issues; the `unc-structure.md` master table overlaps with
`tarot-interpretation/references/generative-principle.md` (that file is the *interpretation*
downstream of this research — keep the two in sync when the structure shifts).

## Sync ritual

When the Linear project changes materially:

1. `get_project` + `list_issues` (project "Generative Principle") to see what moved.
2. Update `number-index.md` depth column and any new discovery-issue rows.
3. When a deep issue's grammar/structure changes, update `operational-grammars.md` /
   `unc-structure.md` to match; bump the "Last synced" date here.
4. If the structural model shifts (new pillar model, grammar reconciliation, etc.), also update
   `tarot-interpretation/references/generative-principle.md` — it consumes this structure.
5. Bump the SKILL.md description only if the change alters the triggering surface.

## Why pointer, not mirror

Unlike the brand/coding sources, this material is **actively under research** — issues are living
documents that change as exploration deepens. Mirroring would guarantee drift on the very content
most likely to move. The snapshot exists only to orient quickly and to work offline; the live
issues remain the one home for current depth.
