---
name: tarot-interpretation
description: >-
  Interpret one or more tarot cards through Paul's own correspondence stack for
  The 78 — not generic Rider-Waite meanings. Reads each card's attributions from
  bundled correspondence tables (self-contained; no live lookup needed) and reads it
  through the per-arcana grammar:
  Major Arcana by the Generative Principle + Kabbalah; Majestic Arcana
  by the MBTI generator (Thrones / Court / Aces); Minor Arcana by triplicity-ascent
  decan ruler + sign + Enneagram (planet = subject, sign = environment, type =
  situation). Optionally places a reading inside a decomposition lens (4×19
  elemental, 7×11 planetary lords, 11×7 Tree stations) and scores resonance with
  the Mars Scoring Engine. Use this skill whenever the user supplies a card, a
  spread (cards in named positions), or a derived reading and wants it interpreted
  in their system — phrasings like "interpret this card", "read these cards",
  "what does X of Chalices mean in my system", "read this spread", "interpret by
  lot / by element", "what's the generative read on the Tower", or "score this
  reading's resonance". INTERPRET ONLY — never draw, deal, or randomly select a
  card. Cards are user-supplied or deterministically derived elsewhere.
---

# Tarot Interpretation (The 78)

## What this does

Takes a card, a positional spread, or a full derived reading and interprets it
through Paul's correspondence stack — the three-arcana architecture of The 78,
not stock card meanings. Every correspondence is listed in the bundled `references/`
tables, so interpretation needs **no live database lookup** — read the tables
directly. Flow: **resolve from references → read each card → synthesize → (lens
placement) → (resonance score) → persist.**

The user may ask for a single card or a whole spread, with or without a lens, with
or without scoring. Run only what is asked.

## Sources

- **`references/` (bundled, authoritative).** All correspondences live here and are
  the source of truth for interpretation: `majors.md` (Major attributions),
  `generative-principle.md` (the 1–21 number layer), `mbti-majestic.md` (the Majestic
  generator), `decans.md` (the 36 Minors), `lenses.md` (4×19 / 7×11 / 11×7). Read
  these directly — no query needed to interpret.
- **repository** (Neo4j) — used only for **persistence** of a reading and optional
  **verification/refresh** of the tables. Not consulted during ordinary
  interpretation. Reading edges: `THROUGH_LENS`, `DREW_CARD`, `DOMAIN_CARD`,
  `PLANETARY_CARD`.
- **Mars Scoring Engine** — optional. Scores a card or reading's resonance against
  supplied text. It scores on **triplicity-ascent** decan lords.
- **kairos-mcp** — required for the **11×7 derived laying** (almuten figuris + lord
  positions) and any reading read against a natal chart; otherwise optional.

## Standing rules

1. **Interpret only — never draw.** This skill never randomizes, deals, shuffles,
   or selects a card. Cards arrive either user-supplied or **deterministically
   derived** by another system (a chart cast, a releasing period, Sacred Journey).
   Derived single cards are valid but rare. If asked to "draw" or "pull" a random
   card, decline and ask for the card(s) or the derivation source.
2. **The bundled tables are authoritative.** Interpret from `references/`; do not
   query the Repository to look up a correspondence. The Repository is consulted only
   to persist a reading or to verify/refresh the tables on request.
3. **Verify before writing.** Before any Cypher *write* (persistence), run read
   queries to confirm exact node names, labels, and edge types. No exceptions. And
   never invent a correspondence that isn't in the tables — if something's missing,
   say so rather than guess.
4. **Water suit is Chalices** — everywhere, including any historical/derived input
   that arrives as "Cups." Normalize silently.
5. **Decan ruler = triplicity-ascent** (canonical; what the Mars engine scores on).
   **Chaldean** order is a selectable alternate ruler set, **off by default** —
   use it only when the user explicitly asks for the Chaldean reading.
6. **Majestic is a generator, not a lookup.** Derive a court/throne card's MBTI
   from the two binaries (§Majestic). Do not read the type off a stored table as
   the primary act; the stored value is a cache to cross-check against, not the
   source of truth.
7. **Time is Unix epoch seconds as a node property** — never an edge property; no
   `TimeFrame` nodes; no Neo4j Aura for writes (Python + driver).

**All correspondences are listed in `references/`. Read them directly to interpret —
no live query is needed.**

---

## Resolving a card

Normalize the name (Cups → Chalices), then classify the tier from the name and read
that card's row from the matching table — no query:

- **Major** (The Fool … The World) → `references/majors.md` + `generative-principle.md`
- **Majestic** (any Page/Knight/Queen/King/Ace) → `references/mbti-majestic.md`
- **Minor** (pips Two–Ten of a suit) → `references/decans.md`

Then route to the matching module below.

---

## Major module — 22 (0 + 21)

The Major is the **cosmological / archetypal** layer. The Fool is **0**, the
generative precondition standing outside the count; the structure proper is the
21 = 3 × 7.

**Resolve** from `references/majors.md` (element, sign/planet, Hebrew letter, Tree
path, stage of the path) and `references/generative-principle.md` (the number's
prime/composite status, factorization, pillar(s), septenary role).
- **Prime vs composite.** 9 emergent primes (the Enneagram-shaped set) read as
  *irreducible generative acts*. 12 composites (the Zodiac-shaped set) read as
  **trinity-operations**: smaller factor = **Operator**, larger = **Substance**,
  product = **Result**, mapped to Cardinal · Fixed · Mutable. Squares are
  self-action.
- **Generate / Produce rhythm.** Odd→Even = Generate, Even→Odd = Produce.
- **Pillar membership** (four pillars by base prime, per `references/generative-principle.md`):
  Mind (×2, the evens), Soul (×3), Man (×5), Divine (×7). Dual members (e.g. 6/12/18
  = Mind∧Soul, 21 = Soul∧Divine) read as reinforcement.
- **Septenary role.** Operator (1–7), Substance (8–14), Result (15–21).

**Then layer:** Hebrew letter, Tree path, stage of the path, and astrology (sign
card → 1 sign; planetary card → its domicile sign(s); elemental card —
Fool/Hanged Man/Judgement — → all 3 signs of its element).

**Grammar:** read the card as *a structural operation in the deck's self-generation*
— what it produces and how — located on its pillar(s) and septenary, then deepened by
its Kabbalah and astrology. The Fool, when present, is read as the precondition, not
a step.

---

## Majestic module — 20 (4 Thrones + 12 Court + 4 Aces)

The **mental-structures** layer. Internal split:

- **Thrones** — the 4 **Pages**, the *seasonal thrones*: each is seated at the
  cross-quarter festival at its season's **height** (Wands = Lammas, Chalices =
  Samhain, Pentacles = Beltane, Swords = Candlemas).
- **Court** — **Knights, Queens, Kings** (12), the working psyches. **Queens and
  Kings hold the solstices and equinoxes.**
- **Aces** — the 4 pure cognitive-function pairs (Ni+Ne, Fi+Fe, Ti+Te, Si+Se),
  standing as the **culmination above their throne** — the function whole, before
  it stacks.

Three independent layers sit on each Majestic card and must not be conflated: the
**cognitive** layer (the MBTI generator below), the **seasonal** layer (Sabbats,
above), and the **elemental** layer (inner = suit element, outer = rank element).
All three are true at once.

**Suit → function:** Wands/Intuition · Chalices/Feeling · Swords/Thinking ·
Pentacles/Sensing.

**MBTI generator (derive, do not look up).** For a Throne or Court card, the type
is fixed by two orthogonal binaries:
1. **Dominant attitude** — extraverted (♂) or introverted (♀). ♂ → Knight/King;
   ♀ → Page/Queen.
2. **Auxiliary element vs suit element** — *opposing* pair (Fire/Water, Air/Earth)
   → the youth/conflict ranks **Page/Knight**; *complementary* pair (Fire/Air,
   Water/Earth) → the experienced/harmony ranks **Queen/King**.

The 2×2 over those binaries yields the four courts of a suit uniquely. Worked
example (Wands = Fire = Intuition dominant): Page = INFJ (Ni; aux Fe→Water,
opposing), Knight = ENFP (Ne; aux Fi→Water, opposing), Queen = INTJ (Ni; aux
Te→Air, complementary), King = ENTP (Ne; aux Ti→Air, complementary).

**Resolve** the full type, cognitive stack, seasonal seat, and elemental pair from
`references/mbti-majestic.md` (which lists all 16 courts + 4 Aces). The table is the
generator's cached output — if a derivation ever disagrees with it, trust the
derivation and flag the row.

**Grammar:** read as *a mind shaped around the suit's function* — the cognitive
stack in motion. A **Throne/Page** adds its seasonal seat; an **Ace** is read as
the function in its undivided culmination, not as a person.

---

## Minor module — 36 (pips 2–10)

The **patterns-of-behavior** layer. Nine pips per suit.

**Resolve** from `references/decans.md` (sign, triplicity-ascent ruler, Chaldean
alternate, Enneagram type — all 36 listed).

- **Decan ruler** = the triplicity-ascent column (default). If the user asks for
  Chaldean, use the Chaldean column instead and say so.
- **Enneagram** = the pip number: 2→Type 2 … 9→Type 9, **10→Type 1** (return to
  source). Secondary lens — center → modality: Heart (2,3,4) = Cardinal, Head
  (5,6,7) = Fixed, Body (8,9,1) = Mutable.

**Grammar (the three slots):**
- **Planet = subject** — who or what is acting.
- **Sign = environment** — the field it acts in.
- **Enneagram type = situation** — the dynamic at play.

Read as: *this subject, in this environment, facing this situation.* The pip's
position in its suit's 2→10 ascent (the suit's function climbing its territory)
gives the developmental register.

---

## Decomposition lenses (optional)

A reading can be placed inside one of three orthogonal partitions of the 78. These
are reading **boards**, not card meanings. Full membership is in
`references/lenses.md`. Use only when asked ("read by element / by lot / on the
Tree").

- **4×19 — Elemental** (complete). Four elements × 19 (suit of 14 + 5 Majors: 3
  zodiacal, 1 elemental, 1 planetary). Sun (19) and High Priestess/Moon (2) held out
  as the frame. Read a card by its **elemental home**.
- **7×11 — Planetary Lords** (complete). Seven planets × 11, Fool apart; weighted by
  natal dignity → the **scored / fixed-self** board. Full membership in `lenses.md`:
  Majors by own + domicile-sign trumps (luminaries' third Major by sect), Minors by
  triplicity-ascent decan ruler, Courts by each court's dominant-sign domicile ruler,
  Pages/Aces by sect.
- **11×7 — Tree Stations** (the derived laying). 10 Sephiroth + Da'ath × 7, Fool
  apart → the **derived / between** board. Chart-derived: compute the almuten figuris
  (Kairos) as anchor, process the 7 lordship-blocks by each lord's distance from it,
  deal 7 per station down the lightning flash, Da'ath taking the remainder. Full
  method in `lenses.md`. This is the one lens that needs a computed chart.

**Three-board reading method.** Scored (fixed self) / dealt (the moment) / derived
(between) = Cardinal / Fixed / Mutable. The reading is the **displacement** between
boards, not any single board read alone.

---

## Interpretation modes

- **Single card** — resolve → module grammar → one tight reading.
- **Spread** — interpret each card in its named position, then a synthesis that
  reads the cards as one dialogue (not isolated blurbs). Note cross-arcana
  resonances (e.g. a Minor's planet echoing a Major in the spread).
- **Resonance score** (optional) — if the user gives text (a question, a journal
  entry, a situation), call `Mars Scoring Engine: classify_text` and report how the
  card(s) score against it. Never narrate engine internals.
- **Lens placement** (optional) — locate the reading on a chosen board.

---

## Persistence

Persist only when the user wants the reading kept.

1. **Verify schema first** — inspect `:Interpretation` / `:Reading` shape and edge
   types before writing:
   ```cypher
   MATCH (r:Reading)-[e]->(x) RETURN type(e), labels(x) LIMIT 15
   ```
2. Create the reading node with Unix-time node props; attach each card with
   `DREW_CARD` (per position) and the lens with `THROUGH_LENS` if one was used.
   All people are `:User` nodes; role is set by edge type (`FOR_USER` = submitter;
   `READER`/`QUERENT` only when someone else fills that role).
3. Python + Neo4j driver, not Aura.

---

## Output Format

```
# Reading — <card / spread name>

## Cards
<per card: name · tier · resolved correspondences>

## Reading
<per-card interpretation via the module grammar>

## Synthesis
<the spread read as one, cross-resonances noted>     # spreads only

## Lens — <4×19 | 7×11 | 11×7>                        # if requested
<placement + what the board adds>

## Resonance                                          # if scored
<Mars scores vs the supplied text>

## Persistence
<:Reading node id, lens edge, card edges>             # if persisted
```

Lead with the resolved correspondences, keep interpretation specific to the cards
in front of you, and let the per-arcana grammar — not generic meanings — carry the
read.

---

## references/

The bundled tables, authoritative and self-contained:

- **`majors.md`** — Major attribution sheet (element, sign/planet, Hebrew letter,
  Tree path, stage). No Hermetic-principle layer (retired; the Generative Principle
  replaces it).
- **`generative-principle.md`** — numbers 1–21: prime/composite, factorization,
  pillars, septenary roles (from Linear PAT-212–232).
- **`mbti-majestic.md`** — the Majestic generator + the 16 courts and 4 Aces, with
  the seasonal and inner/outer-element layers.
- **`decans.md`** — the 36 Minors: sign, triplicity-ascent ruler, Chaldean alternate,
  Enneagram type.
- **`lenses.md`** — 4×19 (complete), 7×11 (complete), 11×7 (complete — the
  chart-derived laying).

All three lenses are now defined. The only chart-dependent piece is the 11×7, which
calls Kairos for the almuten and lord positions; everything else reads from the static
tables. (The 7×11 luminaries' third Major is derived by sect — Judgement→Sun, Hanged
Man→Moon; flag if you ever want it hard-set.)
