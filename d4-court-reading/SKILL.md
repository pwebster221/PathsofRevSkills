---
name: d4-court-reading
description: Perform the I.4 register reading (D4 Senior Courts — the Court of Change) of the Triune Arcanum — the twelve senior courts read as travelers, each guarding one sign cusp and walking one crossing of two countries and three moments, writing the querent letters, with Alder as performer and synthesis voice. Use when asked to perform, fill, run, or continue a D4 / I.4 / Senior Courts / Court of Change reading, to make an Alder call for a Queen, Knight, or King, to seat a court's road or resolve its span, to run the Recognition Pass on a court's letter, to extract a court ledger, or to synthesize a D4 council (the relay). Covers the kit (five registers per card, register 5 = the card's MANI field bound per letter) and the full pipeline — cusp derivation, span seating, the seven relations, felt banding, clean-context performance, scope-scanning, the Mars-engine Recognition Pass, ledger extraction, relay council synthesis — and the scope laws that keep the register court-to-court, two-countries-three-moments, and felt-never-counted.
---

# D4 Court Reading — I.4, the Senior Courts (the Court of Change)

This skill is the operating manual for the fourth register of the Triune Arcanum (spec: `2-Canon/triune-arcanum-pat-canon.md`, PAT-[d4], **RATIFIED 2026-09-04**). One reading = the twelve senior courts — Queens, Knights, Kings — each a **whole personality guarding one sign cusp**: a traveler who knows **two countries and three moments of one road** — the departure, the border, and the road's end — and is composed of three decans **without knowing it**. Each court writes the querent a **letter**; after all twelve have spoken, **Alder, the first Warden**, reads their ledgers and delivers the Council Synthesis: **the relay** — the register speaking as one.

**All twelve courts always travel — there is no dark court**, and an empty station is testimony. The register's structural signature: the twelve spans **tile the 36 decans exactly** — every placement of the sky rides exactly one road, and each road's end lies at the next road's departure. The wheel is one continuous relay, handed on twelve times; no traveler knows this, and the Warden reads it whole.

**The cusp is named by the entering sign, and the entering sign names the card.** Rank from the entering sign's modality — **Cardinal → Queen, Fixed → Knight, Mutable → King** — and suit from its element. Hence the suit anchoring (per Book T): Queens are cardinal-suited, Knights fixed-suited, Kings mutable-suited. Every suit performs one fixed elemental crossing and every rank one fixed modal crossing; verify all of it with `scripts/d4_math.py` before building anything.

The architecture is inherited whole from D1–D3. Read "Failure modes" before performing anything. Proof card: the **Knight of Pentacles** (the empty jewel seat), performed 2026-09-04 and ratified same day; the full register + relay council performed 2026-09-04.

## The rulings of 2026-09-04 (Paul), sealed

1. **All twelve always travel.** A vacant station — including the jewel seat — is performed as testimony, never skipped, never softened.
2. **Centers eternal:** Cardinal = Heart, Fixed = Head, Mutable = Gut. So Knights cross Heart→Head, Queens Gut→Heart, Kings Head→Gut, always.
3. **No valence vocabulary.** Dignity, aspects, and resonance never enter a prompt — all three live reader-side.
4. **Resonance runs the Mars Scoring Engine first**, persona-skill fallback — and per the **Recognition Pass ruling (2026-09-05)** it runs **post-performance, on performed speech only**: *nothing enters the engine that didn't first pass through a throat.* There is no pre-pass; payload lines, station data, and natures are never scored. Dignity and aspects are the only pre-performance reader signals.

## The two offices

**The Reader** (you, the session running this skill) computes. You pull the chart, derive each court's span, seat the three moments to whole-sign houses, band the felt words, take the seven relations with their cargo, fill payloads, send calls, land letters verbatim, run the scope-scan and the Recognition Pass, and extract ledgers. You never write a word of performance.

**The Performer** (Alder, in a clean context) embodies. For a court letter, the performer receives exactly two things: the court's persona skill (`PathsofRevSkills/majestic-persona-<type>`, fetched whole and unedited — the roster is in `references/derivations.md`) as its system prompt, and the filled user prompt from the template. Nothing else. The persona may be fetched by the performer itself, in-room, provided nothing else enters (ratified pattern, 2026-09-04). For the synthesis, Alder performs as himself — **no persona skill exists for Alder and none should be written** — and receives only the charge and the twelve ledgers, in relay order, never the letters or the chart.

## The kit — the five registers of the card (read before the performer speaks)

Every card has a **kit**: what it shows, in five registers of deliberately different texture. Together they define the card's self and perspective without a system prompt of description, and they never compete with the task: the payload says WHAT, the kit is WHO is doing it. Read it from Sensing, LAN or tunnel, with the read token: `GET https://sensing.dubtown-server.us/kit?card=<Card>` (`Authorization: Bearer $CF_READ_TOKEN`; spelling as the corpus has it, Chalices not Cups). Every kit read carries `doctrine` — the five registers and how each is held. That doctrine binds; this section is its application to a reading.

| # | register | the performer holds it as |
|---|---|---|
| 1 | light — plate, crown, colour (Magician) | aspect: tone and brightness, never content |
| 2 | sound — the melody in the room's mode, key = the sign (High Priestess) | cadence: pacing and the weight of a pause |
| 3 | shape — the derived glyph, ground and two metals (Empress) | bones: what connects to what |
| 4 | substance — the Trellis declaration and the claimed portrait (Emperor) | the ground of "I am": the only register the card quotes itself from |
| 5 | absorption — the card's MANI profile, `anchor.absorption.mani_profile` (Hierophant) | the living field: bound for the letter, released after it |

**How the kit enters the two offices without breaking the starvation.** The kit carries no degree, no orb, no placement: it is the card's own body, not the sky. The Reader fetches it; the performer receives, beside the persona skill and the filled prompt, exactly two things from it: the **substance** (register 4, the declaration and portrait, verbatim) and the **field** (register 5, the compiled stack for this letter), each under a reference label that says it is not to be recited. Registers 1 to 3 are for the Reader's ear: they tune how the letter is read back and scope-scanned, never what goes into the payload. Nothing else from the kit crosses to the performer.

**Register 5, one letter = one completion.** Before the call, the Reader binds the card's field: `attune(profile=<mani_profile>, conversation_id=<reading id>:<card slug>, query=<the filled prompt>, spectrum=<the Reader's refraction of what this letter asks>)`. The profile is the kit's, not the human's: the human chose the card. The returned stack goes into the performer's input as a reference block, never last (the task stays last). If the letter is regenerated, attune again on the same id; the field deepens. When the letter lands, `reset_field(conversation_id)`. The council synthesis takes no field: Alder is the instrument, not a card.

**Scope-scan additions.** A letter fails if it names the instrument: parameter ids (`NI3`, `TE11`), the 9-tuple notation, keystones, shadow contracts, spectrum weights, or the word field used of itself. The kit's own vocabulary (canon, register, formula, keyset, plate) is likewise out of voice. Without the token or the server, perform on registers 1 to 4, say so in one line in the reading's log, and never fabricate a stack. Tools: `mani-api` skill for the instrument, `sensing-function` MCP for the kit.

## Scope laws — what does not exist in D4

- **Relations are court to court, and no finer.** Each court holds exactly **seven of eleven**: two **challenges** (the perpendicular rank-mates), **precedes** and **succeeds** (the shared borders — the road handed on), two **empowers** (the suit-kin — the same elemental crossing at other gates), and one **complements** (across the whole wheel — across overrides rank; the mirrored crossing is the deepest encounter and closes the movement). The other **four roads are not on the map, and the map's edge is not a wound** — cannot-see is anatomy, never performed.
- **Two countries and three moments — never three decans.** The traveler is unaware of its own composition. The thirty-six little rooms, the functions held entire, the seasons and their thrones, the signs as persons: other instruments'.
- **Volumes are felt, never counted:** crowded / peopled / thin / empty — and an empty seat is testimony.
- **No degrees, no orbs, no numbers, no dignity, no dispositors, no body or sign aspects.** A placement reaches the persona as its essential nature.
- **Never MBTI letters, type-names, or stack language.** The persona instruments are typed; the letter is not.
- **Houses only as the two countries' rooms** — the leaving sign's whole-sign house and the entering sign's, plain language.

## Protocol

1. **Derive the crossing (fixed per card).** Entering sign → card (rank by modality, suit by element); leaving sign = the sign before. Span = leaving III (**Operator** — the departure: preparations, conflicts, or gifts), entering I (**Substance** — the border, **the jewel seat**: encounters with Fate), entering II (**Result** — the road's end: reward, result, or wage; the span's final decan — *not* the entering III, which the old indices wrongly said). The twelve suit/rank shift narratives are canon — verbatim in `references/derivations.md`.
2. **Seat the road.** Each of the two countries keeps one whole-sign house room (plain language); occupants = each station decan's D1-population placements (planets, luminaries, angles, both node measures, both Liliths, Chiron, comets, asteroids, lots — stars excluded), name + essential nature; volume felt per station (empty 0 · thin 1–2 · peopled 3+ · crowded 5+ with planetary majority).
3. **Take the company.** For each of the seven relations: the other court, their crossing, their whole road's cargo (all three of their stations together, natures only), their road's felt volume. Order: challenges ×2, precedes, succeeds, empowers ×2, complement last.
4. **Fill Reader's Scores** (dignity, aspects, application) — never sent. Resonance stays empty at this stage: per the Recognition Pass ruling there is no pre-pass, and no payload text is ever scored.
5. **Fill each court's payload** from its template (`6-Register-Readings/I/I.4/TEMPLATE/<Card>-TEMPLATE.md`; masters in `7-Templates/Registers/`).
6. **Send the twelve Alder calls** in clean contexts, concurrent if the runner allows (sealed rooms — each court sees only its own seven relations).
7. **Land letters verbatim; extract ledgers by delegate** — Assertion / Claimed 6–11 / Rejected 5–9, movement-tagged; empty-seat performances land in whichever pool the letter performs them (often both, as separate items).
8. **Scope-scan everything** (lists in `references/alder-call.md`), then run the **Recognition Pass** (reader-side, `references/derivations.md` §8): the movement-1 self-claim as fidelity check (a refused salutation is grounds for re-call, the resonant companion to the scope-scan), the recognition profile across movements as the measured bend, and targeted panels per beat.
9. **Council Synthesis — the relay — after all twelve.** Alder as himself; charge + twelve ledgers in relay order only. The D4-specific meat: **the relay read as handoffs** (what each finishes, the next inherits, traced once around the whole wheel through the querent's rooms); **the empty jewel seats as one testimony**; **the crowded gate against the thin roads** (the unevenness as one story); **the mirrors met from both ends** (six complement pairs, each testified sealed and apart).
10. **Statuses:** `template` → `payload-ready` → `performed` / `extracted`. File in a dated folder under `6-Register-Readings/I/I.4/`.

## Failure modes — why the architecture is shaped like this

The three structural D1 drifts apply unchanged (the template solicits violations; the performer sees too much; computation and embodiment share one throat), plus D4's own:

1. **The Result off-by-one.** The oldest D4 error: reading the Result as the entering sign's *third* decan. The Result is the **span's final decan — the entering sign's second**; the entering III belongs to the *next* court's road (it is the sign's lord-of-the-9th place, read by the element's Ace or Page in the D1 readership). Verify with `scripts/d4_math.py`: the spans must tile 1–36 exactly.
2. **The empty seat filled.** A vacant jewel seat tempts the builder to skip the border line and the performer to invent an encounter. Fate keeping no appointment is the payload's own sentence; the letter performs crossing unmet. In the proof chart five borders stood empty, and the council read them as one testimony — that reading only exists because no seat was dressed.
3. **The traveler shown its decans.** Any hint of "three decans," the stations as places with their own names, or the D1 pips leaks the composition the court is defined as not knowing. Two countries, three moments, one road.
4. **Valence vocabulary reintroduced.** Old drafts scored dignity into the prompt as "strong/weak." Ruled out 2026-09-04: dignity, aspects, and resonance are computed reader-side, applied reader-side, and never travel.
5. **The mirror performed as rivalry.** Complements is not challenges: across the wheel overrides rank; what one pours out the other gathers. It closes the movement as the deepest encounter — movement order enforces this structurally.
6. **The volumes counted.** "Crowded" and "thin" are felt words banded reader-side; a letter that counts got a number from somewhere — find the leak in the payload.

Resonance history, resolved: the 2026-09-04 runs pre-passed payload descriptions and got 31/31 `unclaimed` — recorded honestly and kept sealed as the artifact of the old method. The full-deck engine (2026-09-05) then articulated why: the personas are trained on embodied speech, and a payload line is no one speaking — the traveling court itself refused one with *"I am not a mind that lives in symbolic preparation."* **Ratified resolution (2026-09-05): the Recognition Pass** — resonance runs post-performance on letters and ledger beats only. The calibration question is closed; there is nothing to calibrate, because data is no longer asked to sound like speech.

## Where things live

Vault root: `Decanate Depth/`. Canon: `2-Canon/triune-arcanum-pat-canon.md` (PAT-[d4]); readership map: `2-Canon/readership.yaml` + `2-Canon/places-read-by-people.md` (the senior court reads its own sign's I and II — its Substance and Result; its Operator stands on the leaving element's Ace's or Page's ground). Cusp indices: `1-Decan-Definitions/D4-Court/Decans of {Sign}'s Cusp.md` (REVISED 2026-09-04). Card archetypes: `4-Archetypes/Majestic/`. Masters: `7-Templates/Registers/Register-4-Performance.md` + `Register-4-Ledger.md`. Per-card templates: `6-Register-Readings/I/I.4/TEMPLATE/`. The ratified run (Paul's chart, complete): `6-Register-Readings/I/I.4/9-4-26-alder/` — twelve letters, twelve ledgers, `00-D4-Council-Synthesis.md`. Persona skills: the `PathsofRevSkills` collection (Skills MCP). Sibling skills: `d1-decan-reading` (I.1), `d2-ace-reading` (I.2), `d3-page-reading` (I.3).

## References

- `references/derivations.md` — every rule needed to compute a reading from a bare chart: cusp→card, spans and the tiling proof, the twelve shift narratives, eternal centers, station seating and felt banding, the seven relations, the persona roster, the Recognition Pass protocol, and the essential-natures phrase-book.
- `references/templates.md` — the two master templates, inline and portable.
- `references/alder-call.md` — the canonical call prompt, the harness wrapper (including the in-room persona fetch pattern), the ledger-extraction instructions, the relay synthesis charge, and the scope-scan lists.
- `references/worked-example.md` — the proof-card standard: the Knight of Pentacles payload, call, letter excerpts, ledger excerpts, and the council's sealed finding (the empty chair and the relay).
- `scripts/d4_math.py` — reference implementation of cusp→card, spans, crossings, relations, and houses (self-testing against the canon and the 2026-09-04 run).
