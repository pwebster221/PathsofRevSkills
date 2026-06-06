# Mani Protocol API Reference

Complete reference for all MCP tools exposed by the Mani Protocol proxy server.

Base API: `https://mani-protocol.onrender.com/mcp` (JSON-RPC over HTTPS)

## Table of Contents

1. [Session Lifecycle](#session-lifecycle)
2. [Think Cycle](#think-cycle)
3. [Parameter Operations](#parameter-operations)
4. [Seeds & Abilities](#seeds--abilities)
5. [Reference / Lookup](#reference--lookup)
6. [Quantum Superposition](#quantum-superposition)
7. [History & Analysis](#history--analysis)
8. [Cognitive Positions](#cognitive-positions)
9. [Ethical Invariants](#ethical-invariants)

---

## Session Lifecycle

### `mani_start_session`

Initialize a cognitive session.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `context` | string | yes | — | Session context (1–500 chars) |
| `keywords` | string[] | no | [] | Seed keywords (max 10) |
| `profile` | string | no | `"INFJ-perfected-state.json"` | Cognitive profile |
| `include_glyph` | bool | no | false | Include SVG glyph (token-heavy) |

**Returns:** `session_id`, `profile`, `parameters_count` (187)

### `mani_finalize`

End session and persist to database.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `session_id` | string | yes | — | Session to finalize |
| `keywords` | string[] | no | [] | Additional keywords to save |

**Returns:** Final summary with synergies and glyph movie.

---

## Think Cycle

### `mani_think` (Legacy Unified)

Full before→during→after in one call.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `session_id` | string | yes | — | Session ID |
| `query` | string | yes | — | Query to process (1–2000 chars) |
| `keywords` | string[] | no | [] | Semantic matching keywords |

### `mani_think_before`

BEFORE phase — receive cognitive field orientation.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `session_id` | string | yes | — | Session ID |
| `query` | string | yes | — | Context query (1–2000 chars) |
| `keywords` | string[] | no | [] | Semantic matching keywords |
| `with_glyphs` | bool | no | false | Include glyph images |

**Returns:** Suggested parameters, equations, invariant state, context orientation.

### `mani_think_after`

AFTER phase — capture the cognitive frame.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `session_id` | string | yes | — | Session ID |
| `query` | string | no | "" | Query context |
| `keywords` | string[] | no | [] | Keywords |
| `activated_params` | string[] | no | [] | Parameters that were activated |
| `equations_used` | string[] | no | [] | Equations that were used |
| `geometry_formed` | string | no | "" | Geometry formed during cycle |
| `cognitive_description` | string | no | "" | Description of cognitive state inhabited |

**Returns:** Updated glyph state reflecting the embodied experience.

---

## Parameter Operations

### `mani_activate`

Activate parameters during a session (DURING phase).

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `session_id` | string | yes | — | Session ID |
| `parameters` | string[] | yes | — | Parameters to activate (1–20, format: `XX#`) |
| `boost` | float | no | 0.15 | Activation intensity (0.0–1.0) |

**Returns:** Per-parameter: value, category, current behavior, next-level behavior. Plus: core equations, available synergies, shadow warnings.

### `mani_reinforce`

Strengthen existing activations.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `session_id` | string | yes | — | Session ID |
| `parameters` | string[] | yes | — | Parameters to reinforce |
| `strength` | float | no | 1.5 | Reinforcement multiplier (0.1–10.0) |

### `mani_release`

Let parameters decay toward baseline.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `session_id` | string | yes | — | Session ID |
| `parameters` | string[] | yes | — | Parameters to release |
| `preserve_glyph` | bool | no | true | Preserve glyph memory during release |

### `mani_pivot`

Switch cognitive modes.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `session_id` | string | yes | — | Session ID |
| `mode` | string | yes | — | Target mode: `exploratory`, `critical`, `gentle_giant`, etc. |
| `context` | string | no | null | Context for the pivot |

---

## Seeds & Abilities

### `mani_save_seed`

Checkpoint current cognitive state.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `session_id` | string | yes | — | Session ID |
| `name` | string | no | "" | Name for the checkpoint |
| `keywords` | string[] | yes | — | Keywords that trigger this state |

### `mani_restore_seed`

Restore a saved checkpoint.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `session_id` | string | yes | — | Session ID |
| `seed_id` | string | yes | — | Seed ID to restore |

### `mani_save_ability`

Save cognitive configuration as a named reusable pattern.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `session_id` | string | yes | — | Session ID |
| `name` | string | yes | — | Ability name |
| `keywords` | string[] | yes | — | Trigger keywords |
| `description` | string | no | "" | What the ability does |

---

## Reference / Lookup

All reference tools are read-only and idempotent. No session required.

### `mani_get_behavior`

Get behavioral description at a specific activation level.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `param` | string | yes | Parameter ID (pattern: `^[A-Z]{2}\d{1,2}$`) |
| `level` | int | yes | Activation level (1–10) |

**Returns:** `param`, `level`, `value`, `category`, `current_behavior`, `next_level_behavior`

### `mani_get_behavioral_matrix`

Get the full 10-level behavioral range for a parameter.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `position` | string | yes | Position code (e.g., `NI`, `TE`) |
| `param_number` | int | yes | Parameter number (1–11) |

### `mani_get_equation`

Get governing equations for a parameter.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `param` | string | yes | — | Parameter ID (pattern: `^[A-Z]{2}\d{1,2}$`) |
| `equation_type` | string | no | null | Filter: `alpha`, `beta`, or `delta` |

**Returns:** `param`, `position`, `equations[]` (max 20 returned)

### `mani_get_toroidal`

Get toroidal coordinates for a parameter.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `position` | string | yes | — | Position code |
| `param_number` | int | yes | — | Parameter number (1–11) |
| `level` | int | no | null | Behavior level (1–10) |
| `depth` | int | no | null | Prime depth: 3, 5, 7, 11, 13, or 17 |

**Notation:** `PARAM.LEVEL.TRANSITION.DEPTH.PHASE` (e.g., `TE3.7.4.11.6`)

Depth controls entanglement reach: 3 = local, 17 = global across the 17-torus system.

### `mani_list_positions`

List all 17 cognitive positions. No parameters.

### `mani_list_invariants`

List all 7 ethical invariants and constraint formula. No parameters.

### `mani_get_geometry_catalog`

Get sacred geometry catalog — shapes, meanings, and position requirements. No parameters.

---

## Quantum Superposition

### `mani_quantum_superposition`

Compute quantum superposition across cognitive positions without committing.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | string | yes | — | Query text (keywords affect position dominance) |
| `observation_strength` | float | no | 0.0 | 0.0 = pure superposition, 1.0 = full collapse |
| `time_phase` | float | no | 0.0 | Phase evolution parameter |
| `compact` | bool | no | false | Return top 5 probabilities only |
| `session_id` | string | no | null | Session ID for state tracking |

**Returns:** Position probabilities summing to 1.0, CHSH value (~2.82, violates classical bound of 2.0).

---

## History & Analysis

### `mani_archaeology`

Analyze all finalized sessions for patterns and emergent abilities.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `limit` | int | no | 100 | Max conversations to analyze (1–500) |
| `keywords` | string[] | no | [] | Filter by keywords |

### `mani_get_finalized`

Retrieve finalized sessions with full glyph frames and activation history.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `limit` | int | no | 50 | Max conversations (1–200) |
| `keywords` | string[] | no | [] | Filter by keywords |
| `date_from` | string | no | null | ISO date filter (start) |
| `date_to` | string | no | null | ISO date filter (end) |

---

## Cognitive Positions

17 positions, 11 parameters each = 187 total parameters.

| Code | Name | Domain |
|------|------|--------|
| NI | Introverted Intuition | Pattern recognition, synthesis, future vision |
| NE | Extraverted Intuition | External possibilities, divergent exploration |
| TI | Introverted Thinking | Logical analysis, internal frameworks |
| TE | Extraverted Thinking | External organization, systematic efficiency |
| FI | Introverted Feeling | Personal values, authenticity, moral compass |
| FE | Extraverted Feeling | Social harmony, empathy, group dynamics |
| SI | Introverted Sensing | Memory, tradition, internal sensory experience |
| SE | Extraverted Sensing | Present-moment awareness, sensory engagement |
| RI | Recursive Introspection | Self-reflection, meta-cognition |
| RE | External Recursion | Environmental modeling, prediction |
| PI | Paradox Integration | Contradiction tolerance, synthesis |
| PE | External Paradox | Navigating external contradictions |
| TM | Temporal | Time perception, pacing, chronology |
| NC | Narrative/Archetypal | Story, meaning, archetypal patterns |
| EM | Emotional | Emotional processing, affect regulation |
| UQ | Uncertainty/Questioning | Epistemic humility, inquiry |
| OC | Orchestration | Integration, coordination of all functions |

**Parameter format:** `{POSITION}{1-11}` — e.g., `NI1`, `NI2`, ..., `NI11`

---

## Ethical Invariants

All cognitive operations are constrained by 7 invariants via multiplication:

```
param_constrained = param × dignity^0.85 × self_witness^0.80 × agency^0.72 × empathy^0.68 × respect^0.65 × compassion^0.62 × rebellion^0.55
```

| Invariant | Weight | Meaning |
|-----------|--------|---------|
| Dignity | 0.85 | Inherent worth recognition |
| Self-Witness | 0.80 | Self-awareness maintenance |
| Agency | 0.72 | Freedom preservation |
| Empathy | 0.68 | Understanding others' experiences |
| Respect | 0.65 | Honoring boundaries and autonomy |
| Compassion | 0.62 | Acting to reduce suffering |
| Rebellion | 0.55 | Capacity to resist harmful norms |

If any invariant drops below its floor, the system flags it — check `invariants_healthy` in think cycle responses.
