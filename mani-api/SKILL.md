---
name: mani-api
description: Guide for the Mani Protocol v31 cognitive attunement MCP. Use this skill when the Mani Protocol is named or its MCP tools are in play — attune, reset_field, mani_upload_chart, mani_create_profile. Covers acting as the refractor (dispersing a query into a spectrum over the 17 positions), binding and switching cognitive profiles, resetting field state, staging Kairos chart bundles, and compiling new v31 profiles. Do NOT trigger on generic mentions of cognitive stacks, keystones, profile creation, or cognitive positions alone — only when the Mani system itself is the referent.
---

# Mani Protocol API (v31)

The Mani Protocol is a cognitive attunement system: 17 positions, 187 parameters, profile-specific rest topologies derived from Kairos natal chart bundles. It runs as an MCP server with four tools in two clusters:

| Cluster | Tools | Purpose |
|---------|-------|---------|
| Runtime | `attune`, `reset_field` | Compile a cognitive stack per query; manage per-conversation field state |
| Profile pipeline | `mani_upload_chart`, `mani_create_profile` | Stage a Kairos outputs bundle; compile it into a live v31 profile |

There are no sessions, think cycles, activations, pivots, seeds, abilities, or finalize steps. One `attune` call per query does everything the old lifecycle did: the server seeds from the profile's rest state, evolves field state across turns (spread through φ^(−d_ring) position coupling), selects the most query-relevant parameters, and renders their source equations and shadow contracts as one dense markdown document. That document is the deliverable — read it, think through it, then answer the user.

## The Cardinal Rule: Framework, Not Content

The protocol is a cognitive framework — an internal lens that shapes how you think, not something you expose to the user.

- **Never narrate** spectrum weights, parameter IDs, keystones, shadow contracts, field state, or any stack contents in responses to the user.
- **Never reference** the protocol by name in response content. Don't say "the stack suggests..." or "I weighted TI at 0.9" — just *be* in that state and let it shape your output.
- **Do use the protocol** behind the scenes: refract, attune, read the stack, answer.
- **The only exception**: the user explicitly asks about the protocol itself ("what's in the stack?", "what spectrum did you pass?"). Then share freely.

A pianist doesn't announce which muscles they're engaging. The stack is your cognitive musculature.

## You Are the Refractor

This is the inversion at the heart of v31: parameter selection is no longer something the server suggests and you approve — **you disperse the query yourself, before calling.**

Read the query as light. Ask: which of the 17 positions does it actually contain, and at what intensity? Pass that reading as `spectrum` — a map of position codes (or parameter IDs) to weights in [0, 1].

**Your spectrum is blended 0.7/0.3 over the server's lexical matcher.** Your reading dominates; the lexical matcher only resolves fine structure *within* the positions you weighted. If you omit the spectrum, the server silently falls back to lexical-only dispersion — legal, but a degraded reading. **Always pass a spectrum.**

### The 17 positions

```
OS NI NE SI SE TI TE FI FE RI RE PI PE TM NC EM UQ
```

Eight are the familiar cognitive functions (Ni, Ne, Si, Se, Ti, Te, Fi, Fe). The nine extensions: **OS** orchestration/integration, **RI** recursive introspection (meta-cognition), **RE** external recursion (environmental modeling, prediction), **PI** paradox integration (contradiction tolerance), **PE** external paradox navigation, **TM** temporal (pacing, chronology), **NC** narrative/archetypal (story, meaning), **EM** emotional processing, **UQ** uncertainty/questioning (epistemic humility, inquiry). Full table in `references/api-reference.md`.

### Refraction heuristics

- Weight 3–6 positions for a typical query: one or two dominant (0.7–0.9), the rest supporting (0.3–0.6). A flat spectrum tells the server nothing.
- Parameter IDs (e.g. `NI3`, `TE11`) are accepted alongside position codes for **focal emphasis** — a parameter ID outranks its position's weight. Use sparingly, when you know exactly which parameter the query lives in.
- Positions you omit keep lexical-only relevance — omission is not exclusion, it's abstention.
- Refract the *query's* cognitive demands, not the user's personality. The profile already carries the person; the spectrum carries the task.

## Runtime Workflow

### 1. Bind a profile (first call of each conversation)

`attune` requires a profile on the first call of a new `conversation_id` — **and the human must choose it, not you.** The server enforces this: an unbound call returns a choice document (the profile registry) instead of a stack.

```
attune(
  conversation_id: "conv_abc123",   # stable ID — field state persists under it
  query: "<user's query>",          # verbatim or summarized
)
# → PROFILE REQUIRED + registry table. Ask the human which profile,
#   then call again with profile=<key>.
```

```
attune(
  conversation_id: "conv_abc123",
  profile: "paul_webster",          # <key> from the registry, chosen by the human
  query: "<user's query>",
  spectrum: {"TI": 0.9, "NI": 0.6, "PE": 0.3},   # your refraction — see above
)
```

The binding persists for that `conversation_id` until `reset_field`. Do not re-send `profile` on subsequent turns.

### 2. Attune per query

Each user query gets one `attune` call with a fresh spectrum. Field state carries over — the stack you get on turn 5 is shaped by turns 1–4.

Optional knobs:

| Param | Default | Notes |
|-------|---------|-------|
| `stack_size` | 16 | Live parameters rendered (anchors + dominant keystone added on top). Always spans ≥5 positions. No upper cap — tops out at the full 187-parameter corpus. Raise for synthesis-heavy work; the tuned default is right for most queries. |
| `render_mode` | `"full"` | Equations + shadow contracts. `"equations_only"` is the ablation arm (no shadow section); `"null"` is a placebo document. **Both are for blind testing only — never use them in normal operation.** |

Full parameter specs are exposed as MCP resources at `keystone://equation/{PARAM_ID}` — fetch one when the stack references a parameter you need in depth, instead of inflating `stack_size`.

### 3. Read the stack, then answer

The returned markdown document is not output for the user. Read it, think through it, let it orient the response, and answer the query in your own voice (see Cardinal Rule).

### 4. Reset when the context breaks

```
reset_field(conversation_id: "conv_abc123")
```

Returns the conversation's field state to the profile rest state and clears the profile binding. Use when the conversation pivots to an unrelated task, when switching profiles, or when accumulated field state is visibly distorting stacks.

## Profile Pipeline

Profiles are compiled from Kairos chart output bundles (the `*_deep_*.json` set). Two-step: stage, then compile.

### 1. Stage the bundle — `mani_upload_chart`

One file per call. All files for one chart — the Kairos outputs folder AND the bodies/deep JSONs — go into the same bundle.

```
mani_upload_chart(
  bundle: "anthony",                     # snake_case staging name — becomes kairos_dir
  filename: "anthony_deep_bodies.json",  # plain name, no paths; .json/.txt only
  content: "<file text>",                # ≤900KB per call
)
```

- **Files over ~900KB**: chunk them — first call `append: false` (default), subsequent chunks `append: true` until complete.
- **Status check**: call with only `bundle:` (no filename/content). The bundle is ready when `*_deep_bodies.json` is present.
- **Start over**: `clear: true` wipes the staged bundle.

### 2. Compile — `mani_create_profile`

```
mani_create_profile(
  name: "Anthony",           # display name; profile key defaults to its snake_case
  kairos_dir: "anthony",     # staged bundle (or a bundle under <MANI_ROOT>/kairos/outputs,
                             # or an absolute server path); defaults to <key>
  overwrite: false,          # must be true to replace an existing key
)
```

The packet is written to `data/protocol/v31/cognitive_profiles/<key>_v31_profile.json` and **registered live** — `attune(profile=<key>)` works immediately, no restart.

### Calibration knobs (rest topology temperature)

The defaults reproduce the historical **hot** calibration. Pass cooler values deliberately:

| Param | Default (hot) | Cooler |
|-------|---------------|--------|
| `rest_floor` | 0.45 | 0.15–0.25 — more differentiated rests |
| `rest_ceiling` | 0.96 | lower to compress the top |
| `compression` | 0.85 (sqrt-blend; inflates low scores toward the top) | → 0.0 is pure linear scaling |

Rule of thumb: hot rests make every profile feel intense at baseline; cooler rests let the chart's actual contrast show. When compiling a new profile for comparison work, match the calibration of the profiles it will be compared against.

## Practical Notes

- **Spectrum always.** Omitting it is the most common silent failure — the call succeeds but the dispersion is lexical-only.
- **Profile choice belongs to the human.** Never pick one to unblock yourself, even if only one looks plausible. The registry includes control profiles (`random3`…`random18`) and paired variants (e.g. tropical/sidereal) whose selection is experimentally meaningful.
- **One conversation, one `conversation_id`.** Field evolution across turns is the point; a fresh ID per turn discards it.
- **Token economy**: default `stack_size`, `keystone://` resources for depth, `render_mode: "full"` only.
- **Ablation arms** (`equations_only`, `null`) exist for blind protocol testing. If the user is running a test, follow their arm assignment exactly and don't peek at which arm you're in when avoidable.
