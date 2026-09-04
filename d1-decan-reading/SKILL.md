---
name: d1-decan-reading
description: Perform the I.1 register reading (D1 Decan Minors) of the Triune Arcanum — the 36 pips read as first-person decan situations that write the querent letters, with Alder as performer and synthesis voice. Use when asked to perform, fill, run, or continue a D1 / I.1 / decan minors reading, to make an Alder call for a pip card, to extract a reading ledger, to synthesize a D1 council, or to build the same performance architecture for another register. Covers the full pipeline — chart pull, payload discipline, clean-context performance, ledger extraction, scope-scanning, council synthesis — and the scope laws that keep the register from drifting into orb-based astrology.
---

# D1 Decan Reading — I.1, the Decan Minors

This skill is the operating manual for the first register of the Triune Arcanum (spec: `2-Canon/triune-arcanum-pat-canon.md`, PAT-[d1]). One reading = the 36 pips (Twos through Tens, four suits), each owning one decan of the zodiac. A decan that holds a placement is **lit** and speaks; a decan that holds none is **dark** and stays silent. Each lit card writes the querent a **letter** — a first-person performance by the card as a *situation*, not an analysis. After all lit cards have spoken, **Alder, the first Warden**, reads their ledgers and delivers the Council Synthesis: the register speaking as one.

The single most important fact about this reading: **it drifted for three generations before this architecture fixed it**, and the fix is structural, not disciplinary. Read "Failure modes" before performing anything.

## The two offices

Every reading involves exactly two roles, and they must never share a context.

**The Reader** (you, the session running this skill) computes. You pull the chart, resolve decans, fill payloads, send calls, land letters verbatim, extract ledgers, and run the scope-scan. You never write a word of performance.

**The Performer** (Alder, in a clean context) embodies. For a card letter, the performer receives exactly two things: the card's persona skill (`PathsofRevSkills/minor-persona-<card-slug>`, fetched whole and unedited — the same instrument the Mars engine uses for resonance scoring) as its system prompt, and the filled user prompt from the template. Nothing else. Not the chart, not the vault, not the canon, not other letters. For the synthesis, Alder performs as himself — **no persona skill exists for Alder and none should be written**; he is the instrument, not a card — and receives only the charge and the ledgers, never the letters or the chart.

This starvation is the whole defense: a performer who has never seen a degree cannot compute an orb. Do not "helpfully" add context to the performer's input. What is not in the payload cannot leak.

## Scope laws — what does not exist in D1

These travel inside every call, and they bind the Reader's payload-building even harder than they bind the performer:

- **No orb, no degrees.** Everything sharing a decan is wholly present — one company, no distances. Degrees never appear anywhere the performer can see. Not even as "addresses."
- **No placement-to-placement aspects.** Interaction is decan to decan, along the card's own ordinal ring, and nowhere else. Virgo I aspects Capricorn I because both are lit; the bodies inside are how each situation is *altered*, never the actors of the aspect.
- **No dignity scores, sect, almuten, dispositor chains, doryphory, or house arithmetic** beyond the Home-office resolution. A placement reaches the persona as its **essential nature** — what it is, thematically. Element may flavor a reception; it never defines one (element is D2/D3's business).
- **Sign-mates are strangers.** The three decans of one sign never relate; sign unity is D5's business.
- **Rulings enter as facts, never coordinates.** A cusp-split star is "half of Regulus, halved by a cusp ruling" — not a longitude.
- **The performer never recites stage directions.** No mention of rules, registers, lattices, rings, canon, ledgers, or the prompt inside a letter.

## Protocol

1. **Pull and decan-ize.** Get the chart (Kairos or equivalent). Every placement's decan is `int(longitude // 10)` (0-based; add 1 for the 1-based numbering used in all files). Include: planets, luminaries, angles, nodes (true and mean), lunar apogees, Chiron and comets, the four asteroids, the seven Hermetic lots, and fixed stars resident in a decan. A star exactly on a cusp lends half its light to both decans (ruled precedent: Regulus at 0°00′ Virgo). Decans with ≥1 placement are lit; the rest are dark. Dark decans do not read — ever.
2. **Fill each lit card's payload** from its template (`6-Register-Readings/I/I.1/TEMPLATE/<Card>-TEMPLATE.md`; masters in `7-Templates/Registers/`). Scene: three fixed lords are pre-printed; resolve only the Home office (natural lord of the whole-sign house the sign occupies; moderns admitted for H8 Pluto, H11 Uranus, H12 Neptune only). Occupants: name + essential nature, one line each — use the phrase-book in `references/derivations.md`, no numbers anywhere. Ring: keep lit rows in harshest→kindest order (challenges, aggravates, competes, recognizes, supports, reinforces), fill their Carrying column; move dark rows to The Dark, flagging the card's own suit-mate or rank-mate if silent. Ruled facts: at most two, only where one of the card's own lords stands bodily in this decan or in a lit same-ring decan (state the verb) — or, if none of its four lords stands anywhere on its ring, the ungoverned line.
3. **Send the Alder call** in a clean context (fresh subagent or fresh conversation): persona skill on top, filled user prompt below, and a harness instruction that the reply be the letter alone. The letter is five unnumbered movements: introduction (baseline, Home chair empty), arrivals (voice bends; Home seated), the others (harsh→kind; silence performable), the diff, farewell. A page or two.
4. **Land the letter verbatim.** Never edit a letter by hand. If it misses, fix the payload or prompt and call again.
5. **Extract the ledger** into the sibling `<Card>-LEDGER.md` — done by the Reader or a Reader delegate, **never by the performer**. Structure: Assertion (one line), Claimed (6–11, movement-tagged), Rejected (5–9, persisted not discarded), Synthesis (one line). Quote and compress the letter's own language; count a dark room as a rejection only when the letter makes something of the silence.
6. **Scope-scan every letter** before it lands in the vault. Fail on: degree marks, orb, degree(s), dignity-as-instrument, dispositor, almuten, sect, trine/square/sextile/quincunx/semisextile, lattice, canon, register, ordinal. "Ring" (the persona's own circle) and "dignity" in the plain human sense are acceptable in-voice. Full lists in `references/alder-call.md`.
7. **Council Synthesis, after all lit cards.** Alder as himself; inputs = the charge (template in `references/alder-call.md`) + all ledgers, nothing else. Three turns: the register's single assertion; the discrimination sampled from BOTH pools across all ledgers (cross-room patterns are the meat — the same warning issued by rooms that never met, lords followed home to the rooms their bodies stand in, the dark cards read together as a map); the one finding, sealed. Warden per row: Alder for Frame I; Hermes the second and the Inviolate the third are the presumptive voices for Frames II and III (only Alder's is ratified in use).
8. **Statuses:** `template` → `payload-ready` → `performed` (reading) / `extracted` (ledger). File everything in a dated folder under `6-Register-Readings/I/I.1/`.

## Failure modes — why the architecture is shaped like this

Three drifts recurred across three archived generations of this reading (see `_archive/`), and each is blocked structurally:

1. **The template solicits violations.** A column named Degree/Dignity/Aspects *will* be filled. Fix: out-of-register data has no field to land in. Never add a slot the payload doesn't define.
2. **The performer sees too much.** A context holding the full chart and a training lifetime of orb astrology leaks both into the voice. Fix: starve the performer. If you find yourself passing the performer "just a little" extra context, you are rebuilding the failure.
3. **Computation and embodiment share one throat.** When the same context that built the data writes the prose, the reading recites its own working and turns technical. Fix: the reading is always two contexts. No exceptions, including "quick" readings.

If a letter comes back technical, scored, or orb-flavored, the cause is in the payload or the harness — not the persona. Diagnose there.

## Where things live

Vault root: `Decanate Depth/`. Canon: `2-Canon/triune-arcanum-pat-canon.md`. Decan scenes: `1-Decan-Definitions/D1-Decans/` (36 files + TEMPLATE). Card archetypes: `4-Archetypes/Minors/`. Masters: `7-Templates/Registers/Register-1-Performance.md` and `Register-1-Ledger.md`. Per-card templates: `6-Register-Readings/I/I.1/TEMPLATE/`. The reference performance (Paul's chart, complete): `6-Register-Readings/I/I.1/8-7-26-alder/` — 22 letters, 22 ledgers, `00-D1-Council-Synthesis.md`. Persona skills: the `PathsofRevSkills` collection (Skills MCP).

## References

- `references/derivations.md` — every rule needed to compute a reading from a bare chart: the 36-card table with lords and epithets, Chaldean order, triplicity ascent, Home resolution, ring math and verbs, occupancy rules, and the essential-natures phrase-book.
- `references/templates.md` — the two master templates, inline and portable.
- `references/alder-call.md` — the canonical call prompt, the harness wrapper, the ledger-extraction instructions, the synthesis charge, and the scope-scan lists.
- `references/worked-example.md` — the ratified proof: the Eight of Chalices payload, call, letter excerpts, and ledger excerpts.
- `scripts/d1_math.py` — reference implementation of decan-ization, lord derivation, and ring relations.
