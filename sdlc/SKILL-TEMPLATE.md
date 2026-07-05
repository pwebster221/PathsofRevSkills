---
name: sdlc-<skill-id>
description: >-
  One paragraph an agent can match against. State WHEN to use this skill and what
  it activates on — the phrases, situations, and signals that should trigger it.
stage: <discovery|design|build|verify|ship|sustain>
posture: <posture-id>        # Tier 2 only; omit for navigators
tier: <1|2>
role: <navigator|skill>
license: MIT
---

# Skill: <Human Name>

> Stage: <primary> · also useful in: <secondary, if any>

## What it enables

The capability or outcome this posture produces — not the procedure. What becomes
possible that wasn't before.

## Fit signals

- <2–3 context conditions that point here>
- These should echo the `signals_favored` registered in MANIFEST.yaml.

## Anti-signals

- <when this posture will fight you — the conditions under which to route elsewhere>

## Core practice

The methodology in plain language, kept brief. The mental model, not a tutorial.

## Key moves

1. <concrete action>
2. <concrete action>
3. <concrete action>

## Example

One real case, drawn from source material in `references/SOURCES.md`.

## AI leverage points

Where GenAI specifically amplifies this skill.

## Connects to

- **upstream:** <skill that feeds this>
- **downstream:** <skill this feeds into>
- **lateral:** <complementary skills at the same stage>

---

<!--
Authoring notes
- Tier 1 navigators carry `signals:` (the axes to score); their body is a routing
  table of posture options, each ending in **Skill doc:** `sdlc-<id>`.
- Tier 2 postures carry `signals_favored:` and follow the section structure above.
- Always add references/SOURCES.md and register the skill in MANIFEST.yaml.
-->
