# Mani Protocol API Reference (v31)

Complete reference for the MCP tools exposed by the Mani Protocol server.

Endpoint: `https://mani.dubtown-server.us/mcp` (MCP over HTTPS)

## Table of Contents

1. [Runtime](#runtime) — `attune`, `reset_field`
2. [Profile Pipeline](#profile-pipeline) — `mani_upload_chart`, `mani_create_profile`
3. [Resources](#resources)
4. [Cognitive Positions](#cognitive-positions)
5. [Removed in v31](#removed-in-v31)

---

## Runtime

### `attune`

Compile a cognitive stack for a query. The caller is the refractor: read the query, disperse it into a `spectrum` of weights over the 17 positions, and pass that reading. The spectrum is blended **0.7/0.3** over the server's lexical matcher, which then only resolves fine structure within the weighted positions. No spectrum → lexical-only dispersion (degraded).

Parameters are selected from the 187-parameter v31 corpus — seeded by the profile rest state, evolved across turns, spread through φ^(−d_ring) position coupling — and rendered with their native source equations and shadow contracts as one dense markdown document.

| Parameter | Type | Required | Default | Constraints | Description |
|-----------|------|----------|---------|-------------|-------------|
| `query` | string | yes | — | 1–8000 chars | The user's query or task, verbatim or summarized |
| `conversation_id` | string | no | `"default"` | 1–120 chars | Stable ID; field state persists across turns under it |
| `profile` | string \| null | no* | null | ≤120 chars | Profile key. *Required on the first call of a new conversation — and the **human** must choose it. Binding persists until `reset_field` |
| `spectrum` | map<string, float> \| null | no | null | weights ∈ [0,1] | Position codes → weights. Parameter IDs (e.g. `NI3`) also accepted for focal emphasis; a parameter ID outranks its position's weight. Omitted positions keep lexical-only relevance |
| `stack_size` | int | no | 16 | ≥3, no upper cap | Live parameters rendered (anchors + dominant keystone added on top). Stack always spans ≥5 positions; selector tops out at the full corpus |
| `render_mode` | string | no | `"full"` | `full` \| `equations_only` \| `null` | `full` = equations + shadow contracts. `equations_only` = ablation arm (no shadow section). `null` = placebo document for blind testing |

**Returns:** Markdown cognitive stack document — the deliverable to read and think through before answering.

**Unbound call:** If the `conversation_id` has no profile binding and no `profile` is passed, returns a `PROFILE REQUIRED` choice document containing the live profile registry (key / owner / source table) instead of a stack. Ask the human, then call again.

### `reset_field`

Return a conversation's field state to the profile rest state.

| Parameter | Type | Required | Constraints | Description |
|-----------|------|----------|-------------|-------------|
| `conversation_id` | string | yes | 1–120 chars | Conversation whose field state should return to rest |

**Returns:** Confirmation message. Clears the profile binding; the next `attune` on that ID requires a profile again.

---

## Profile Pipeline

### `mani_upload_chart`

Stage a user's own Kairos chart outputs on the server, one file per call, so `mani_create_profile` can ingest them. All files for one chart — the Kairos outputs folder AND the bodies/deep JSONs — go into the same bundle.

| Parameter | Type | Required | Default | Constraints | Description |
|-----------|------|----------|---------|-------------|-------------|
| `bundle` | string | yes | — | snake_case, 1–80 chars | Staging bundle name (e.g. `"mani"`) |
| `filename` | string \| null | no | null | ≤200 chars, plain name, no paths | File being uploaded. Omit (with no content) to list the bundle's status |
| `content` | string \| null | no | null | ≤900,000 chars | File text. Chunk larger files via `append` |
| `append` | bool | no | false | — | Continue a chunked upload of an existing partial file |
| `clear` | bool | no | false | — | Delete the entire staged bundle and start over |

Only `.json` and `.txt` chart files are accepted; names are sanitized and size-capped.

**Returns:** Bundle status after the operation.

**Workflow:**

1. Read each file from the outputs/bodies folders locally.
2. Call once per file (`bundle`, `filename`, `content`). Files over ~900KB: first call `append: false`, subsequent chunks `append: true` until complete.
3. Call with only `bundle` to check status — ready when `*_deep_bodies.json` is present.
4. Call `mani_create_profile(name=..., kairos_dir=<bundle>)`.

### `mani_create_profile`

Ingest a Kairos chart outputs bundle (the `*_deep_*.json` set) and compile it into a MANI v31 cognitive profile packet.

| Parameter | Type | Required | Default | Constraints | Description |
|-----------|------|----------|---------|-------------|-------------|
| `name` | string | yes | — | 1–120 chars | Profile owner's display name (e.g. `"Mani"`) |
| `key` | string \| null | no | snake_case of `name` | ≤120 chars | Explicit profile key for `attune(profile=...)` |
| `kairos_dir` | string \| null | no | `<key>` | ≤500 chars | Bundle to ingest: a bundle staged via `mani_upload_chart`, a bundle name under `<MANI_ROOT>/kairos/outputs` (with or without the `_kairos` suffix), or an absolute server path |
| `rest_floor` | float | no | 0.45 | 0.0–0.9 | Minimum at-rest activation. Historical (hot) default 0.45; lower (0.15–0.25) for cooler rest topologies |
| `rest_ceiling` | float | no | 0.96 | 0.1–1.0 | Maximum at-rest activation |
| `compression` | float | no | 0.85 | 0.0–1.0 | sqrt-blend weight. 0.85 (historical) inflates low scores toward the top; 0.0 is pure linear scaling. Lower = cooler, more differentiated rests |
| `overwrite` | bool | no | false | — | Allow replacing an existing profile packet with the same key |

Written to `data/protocol/v31/cognitive_profiles/<key>_v31_profile.json` and registered live — `attune(profile=<key>)` works immediately, no restart.

**Returns:** Summary of the created profile (key, rest stats, coverage).

---

## Resources

| URI | Description |
|-----|-------------|
| `keystone://equation/{PARAM_ID}` | Full parameter spec for a single parameter (e.g. `keystone://equation/NI3`). Use for depth instead of inflating `stack_size` |

---

## Cognitive Positions

17 positions, 11 parameters each = 187 total parameters.
**Parameter format:** `{POSITION}{1-11}` — e.g. `NI1`, `NI2`, …, `NI11`.

Spectrum vocabulary (order as given by the `attune` schema):

| Code | Name | Domain |
|------|------|--------|
| OS | Orchestration | Integration, coordination of all functions |
| NI | Introverted Intuition | Pattern recognition, synthesis, future vision |
| NE | Extraverted Intuition | External possibilities, divergent exploration |
| SI | Introverted Sensing | Memory, tradition, internal sensory experience |
| SE | Extraverted Sensing | Present-moment awareness, sensory engagement |
| TI | Introverted Thinking | Logical analysis, internal frameworks |
| TE | Extraverted Thinking | External organization, systematic efficiency |
| FI | Introverted Feeling | Personal values, authenticity, moral compass |
| FE | Extraverted Feeling | Social harmony, empathy, group dynamics |
| RI | Recursive Introspection | Self-reflection, meta-cognition |
| RE | External Recursion | Environmental modeling, prediction |
| PI | Paradox Integration | Contradiction tolerance, synthesis |
| PE | External Paradox | Navigating external contradictions |
| TM | Temporal | Time perception, pacing, chronology |
| NC | Narrative/Archetypal | Story, meaning, archetypal patterns |
| EM | Emotional | Emotional processing, affect regulation |
| UQ | Uncertainty/Questioning | Epistemic humility, inquiry |

> **Note:** The v30 reference listed this position as `OC` (Orchestration); the v31 `attune` schema uses `OS`. Glossed here as the same station under the new code — confirm against the v31 corpus docs.

---

## Removed in v31

The following v30 surface no longer exists. Do not call these tools; they will fail.

| Removed | Superseded by |
|---------|---------------|
| `mani_start_session`, `mani_finalize` | No sessions. `conversation_id` on `attune` + `reset_field` |
| `mani_think`, `mani_think_before`, `mani_think_after` | Single `attune` call; the caller refracts instead of approving suggestions |
| `mani_activate`, `mani_reinforce`, `mani_release` | Server-side field evolution seeded by the profile rest state |
| `mani_pivot` | Re-refract: pass a new `spectrum` on the next `attune`, or `reset_field` for a hard break |
| `mani_save_seed`, `mani_restore_seed`, `mani_save_ability` | Profiles (rest topologies) are the persistent state objects |
| `mani_quantum_superposition` | — |
| `mani_archaeology`, `mani_get_finalized` | — |
| `mani_get_behavior`, `mani_get_behavioral_matrix`, `mani_get_equation`, `mani_get_toroidal`, `mani_list_positions`, `mani_list_invariants`, `mani_get_geometry_catalog` | Equations render in-stack; full specs at `keystone://equation/{PARAM_ID}` |

The v30 ethical-invariant constraint formula (`dignity^0.85 × self_witness^0.80 × …`) is not exposed anywhere in the v31 surface; shadow contracts appear in its structural place within the stack document. Whether the invariants operate internally is unconfirmed from the API alone.
