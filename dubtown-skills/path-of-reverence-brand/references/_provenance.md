# Provenance — paths-of-reverence-brand mirror

## Source of truth

The canonical brand specification lives at:

```
/Users/dubtownraces/Development/ProgrammingStandards/ProgrammingStandards-Rules/UPDATED-Code-Brand-Truth/brand-system.md
```

Version mirrored: **v1 (2026-05-17)**
Owner: paul.webster@dubtowndesigns.com

## What is mirrored, and where

| Reference file | Source location | Last mirrored |
|---|---|---|
| `brand-system-full.md` | `brand-system.md` (entire file) | 2026-05-18 |
| `tiers.md` | `brand-system.md` §6 (Esoteric Diction) | 2026-05-18 |

Additional sectional mirrors (`palette.md`, `typography.md`, `sigils.md`,
`iconography.md`, `do-dont.md`, `cross-link-conventions.md`, `examples.md`) are
deferred — the SKILL.md surfaces the most-used rules, and
`brand-system-full.md` is the fallback for everything else. Add a sectional mirror
when a section starts being read frequently in isolation.

## Sync ritual

When `brand-system.md` changes:

1. Read the diff. Identify which sections changed.
2. For each changed section that has a sectional mirror file, copy the new section
   verbatim into the reference file. Preserve the `## Mirrored from` header on top.
3. Always overwrite `brand-system-full.md` with the new full source. Bump the
   "Last mirrored" date in this file and in the affected mirror headers.
4. Bump the version note in the parent SKILL.md frontmatter description if the change
   alters triggering surface (new glyph families, new tiers, etc.). Pure content
   updates do not require a description bump.
5. Re-run the trigger benchmark in `.claude/skills/evals/evals.json` if any change
   touches triggering — verify the skill still fires on the should-trigger prompts and
   does not fire on the should-not-trigger prompts.

## Why Mirror, not Pointer

The decision (made 2026-05-18) was that agent latency on tier discipline / sigil rules /
palette lookups is high-frequency enough that one extra file read across the
`UPDATED-Code-Brand-Truth/` boundary materially slows agent loops. Mirror trades the
small drift risk (mitigated by this ritual) for predictable in-context access.

## Cross-skill home for shared content

Three-Duality archetype sigils are *defined* in `brand-system.md` §5.2. The
`coding-bible` skill references them but does not mirror them — the canonical
home is here (`paths-of-reverence-brand/references/sigils.md` once written, or
`brand-system-full.md` §5.2 today). One home per fact.
