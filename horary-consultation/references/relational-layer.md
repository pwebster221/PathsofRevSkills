# Relational Layer — Synastry in Service of the Question

Run this layer only when the question is entangled with a relationship between principals (an ex, a family member, a partner). The synastry is read **for the question's sake** — what binds these two, which channels are clean for the contact the judgment requires, which are live wires — never as freestanding compatibility analysis, and never as reunion validation when the question was about help.

## 1. Inputs and casting

- Reuse persisted natals by `chart_id` where possible; cast missing principals with the sunrise convention (verify ASC≈Sun; state the Moon's intraday range).
- Call `kairos-mcp:get_synastry` with `chart_a` / `chart_b` as `{"chart_id": ...}` or `{"birth_data": {...}, "anonymous": true}`, `house_system: "whole_sign"`.
- Output keys: `natal_a`, `natal_b`, `cross_aspects`, `perspectives` (a_in_b / b_in_a overlays), `pair_synthesis` (`contacts`, `chemistry`, `houses`, `dignity_exchange`), `metadata` (overlay_id, canonical chart ids).

## 2. Attribution verification — do this before reading anything

**Do not trust the A/B labels in `cross_aspects`.** The engine's `planet1`/`planet2` assignment has been observed flipped relative to the chart_a/chart_b call order. Verify by degree: match each row's `sign`/`degree` against the known natal positions from `natal_a`/`natal_b` and relabel by *position*, which is unambiguous. One mismatch means re-derive the whole table's ownership before drawing a single conclusion. This is THE GATE applied to synastry: the positions are sourced; the labels are checked.

## 3. Reading order

**a. Chemistry blocks first** (`pair_synthesis.chemistry`):
- `venus_mars` — the erotic axis. A literal zero score is a finding: the bond was never held by chemistry.
- `saturn_glue` — Saturn contacts to the other's luminaries and Venus. One person's Saturn aspecting the other's Sun *and* Moon *and* Venus is the signature of the load-bearing bond: conjunction to the Moon = the weight on the heart; trine to Venus = the velvet side of the chain (tenderness stays organized around them); square to the Sun = the cost to selfhood. **Mutual Moon–Saturn interlocks** (each one's Saturn on the other's Moon) are the can't-stay-can't-leave architecture — name it kindly and precisely.
- `sun_moon` — the classic rapport axis; note applying/separating.

**b. Dignity exchange** (`pair_synthesis.dignity_exchange`):
- `rulership_exchanges` / `exaltation_exchanges` — bonds that *feed*. Their complete absence alongside heavy saturn_glue yields the kindest true sentence available: *it binds without nourishing.*
- `detriment_traps` / `fall_traps` — shared debilities (both Marses in detriment in the same sign = conflict goes stubborn, material, immovable between them). Traps prescribe what channel to avoid.

**c. Tightest cross-aspects** (orb ≤ ~3.5°, classical bodies + Nodes, Vesta, Juno, Chiron):
- Sort by orb. Sub-degree contacts are structural; sub-10' contacts are the headline (a South Node exactly on the other's Vesta at 0°04' = devotion soldered to their point of release).
- Classify each as **clean channel** (harmonious aspects from one's luminaries/benefics to the other's action or speech planets — these are the approach routes the judgment should use: "his words are the master key" from Mercury–Mercury plus Mercury–Sun plus Jupiter–Mercury) or **live wire** (Mars–Pluto oppositions, Mars on the other's South Node/12th — the channels crisis exploits; the judgment's boundary rules derive from these: *nothing through Mars*).
- Same-cohort outer conjunctions (both born weeks apart: Jupiter–Jupiter, Saturn–Saturn, outer planets, Nodes) are generational — but when a cohort conjunction lands inside a personal knot (both Saturns fused into a mutual Moon–Saturn stack), it stops being background.

**d. House overlays** (`perspectives`): with sunrise charts these are solar-symbolic — use only the strongest and say so once. A Sun in the other's 12th = the unseen helper, never the rescuer on stage. Benefics landing in the other's 6th when the question concerns an animal = the shared good has the animal's address.

**e. Stacks.** Look for degree-zone pile-ups across both charts (four bodies — two Moons, two Saturns — within a few degrees of one sign). When the stack's sign matches the horary's quesited house sign, the quesited stands at the bond's center of mass. That convergence between question-chart and natal pair is the strongest cross-system finding this method produces; lead with it.

## 4. The transit corridor

Walk the relevant moving body (usually the faster malefic implicated in the horary's perfection) across the shared degree-zones, dating every crossing with real-speed arithmetic from the horary's ephemeris:

1. List target degrees in transit order: the querent's sensitive points (Vesta, South Node), shared nodal degrees, the other principal's natal Mars/personal planets, opposition points to either Pluto, and the horary perfection degree.
2. Date each crossing. Where a crossing on one principal's natal Mars coincides with an opposition to the other's Pluto, you have found **THE HARD DATE** — the catalyst. Attach conduct rules (nothing scheduled, nothing negotiated, no cash, hold the prepared line) when the question's stakes warrant.
3. Sequence the corridor against the horary timeline: deliveries complete *before* the hard date; completion and the ingress turn follow it. Frame causally where the chart supports it: *whatever breaks on the catalyst is what the perfection resolves.*

## 5. Composite (optional)

`get_composite` (midpoint or davison) only if the user asks for the relationship-as-entity. It rarely serves a help-question; default to skipping.
