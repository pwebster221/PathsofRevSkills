# D4 Derivations — computing a Court reading from a bare chart

Everything the Reader needs, in dependency order. Verify against `scripts/d4_math.py` (self-testing) before building.

## 1 · Cusp → card

The cusp is named by the **entering** sign (the majority sign — it holds two of the span's three decans). Rank from the entering sign's **modality**, suit from its **element**:

| Entering modality | Rank | | Entering element | Suit |
|---|---|---|---|---|
| Cardinal | Queen | | Fire | Wands |
| Fixed | Knight | | Earth | Pentacles |
| Mutable | King | | Air | Swords |
| | | | Water | Chalices |

So (per Book T): **Queens cardinal-suited, Knights fixed-suited, Kings mutable-suited.** The twelve, in relay order: Queen of Wands (Pisces→Aries), Knight of Pentacles (Aries→Taurus), King of Swords (Taurus→Gemini), Queen of Chalices (Gemini→Cancer), Knight of Wands (Cancer→Leo), King of Pentacles (Leo→Virgo), Queen of Swords (Virgo→Libra), Knight of Chalices (Libra→Scorpio), King of Wands (Scorpio→Sagittarius), Queen of Pentacles (Sagittarius→Capricorn), Knight of Swords (Capricorn→Aquarius), King of Chalices (Aquarius→Pisces).

## 2 · The span — three moments, and the tiling

For entering sign at index *i* (Aries = 0), with leaving sign at *i−1*:

- **Operator** (the departure) = the leaving sign's **III** — decan 3(i−1)+3
- **Substance** (the border — the jewel seat) = the entering sign's **I** — decan 3i+1
- **Result** (the road's end) = **the span's final decan — the entering sign's II** — decan 3i+2

**The Result correction (2026-09-04):** the old cusp-index prose said "third decan." The entering III is *outside the span* — it belongs to the next court's Operator. Correct reading: the span is [leaving III, entering I, entering II], and the twelve spans **partition the 36 decans exactly** (12 × 3 = 36, each decan in exactly one span). This is the relay property: each road's end (entering II) borders the next road's departure (entering III → the next cusp's Operator). Assert the tiling on every rebuild.

**Readership interface (canon, 2026-09-04 — `2-Canon/places-read-by-people.md`):** in the D1 readership map the senior court *reads* its own sign's I and II — exactly its Substance and Result stations. Its Operator (the leaving III) is read by the **leaving sign's element's Ace or Page** (the lord-of-the-9th place). Every court departs from ground another person reads; the court is unaware of this, and it is never performed.

## 3 · The crossing — elements, functions, centers (eternal)

Functions by element: Fire = Intuition, Earth = Sensing, Air = Thinking, Water = Feeling.
Centers by modality, **eternal** (ruled 2026-09-04): **Cardinal = Heart, Fixed = Head, Mutable = Gut.**

Every suit performs one fixed elemental shift; every rank one fixed modal shift:

| Suit | Crossing | | Rank | Crossing |
|---|---|---|---|---|
| Wands | Water → Fire | | Queen | Gut → Heart |
| Chalices | Air → Water | | Knight | Heart → Head |
| Swords | Earth → Air | | King | Head → Gut |
| Pentacles | Fire → Earth | | | |

## 4 · The twelve shift narratives (canon, verbatim into prompts)

**Suits:**
- **Wands** — "You cross from Water into Fire — from feeling into intuition: each flame supplants its opening sea with fire, and the fire wins in the mixing."
- **Chalices** — "You cross from Air into Water — the Descent of thinking into feeling: what was held aloft condenses in the air and precipitates into the crossing."
- **Swords** — "You cross from Earth into Air — from sensing into thinking: you leap from the edge of earth into air, and fly."
- **Pentacles** — "You cross from Fire into Earth — from intuition into sensing: by the road's end the fire has become the spark that seeds new life into the earth."

**Ranks (eternal-centers wording):**
- **Knight** — "you cross from the Heart's chamber into the Head's — a heart's urge engaged consciously, and carried to the very end."
- **Queen** — "you cross from the Gut's chamber into the Heart's — a feeling long carried in the gut, embodied at last into the heart's new beginning: an emotion embodied to its rebirth."
- **King** — "you cross from the Head's chamber into the Gut's — a decision made and held, released into what can bend and digest its consequences: the resilience to grow from what was decided, which is wisdom."

## 5 · Seating the road

Chart-relative, whole sign. The leaving country keeps the leaving sign's house room; the entering country the entering sign's — the crossing itself changes rooms (Substance and Result share the entering room). Occupants per station = that decan's **D1-population** placements (planets, luminaries, angles, both node measures, both Liliths, Chiron, comets, asteroids, lots — **stars excluded**), name + essential nature (phrase-book, §9).

**Felt banding (per station, and per company road):** empty 0 · thin 1–2 · peopled 3+ · **crowded** 5+ with planetary majority. Numbers live reader-side only.

**Empty stations:** an empty Operator = "nothing was handed to you before the crossing; you left carrying only what you already were." An empty jewel seat = "the jewel seat stood empty — Fate kept no appointment for you here. An empty seat is testimony, not absence: perform what it is to cross unmet." An empty Result = "no wage waited… perform what it is to arrive unpaid, and what the arriving itself is worth."

**Plain-language house rooms** (identical to D1–D3): 1 the rising self, the face and body · 2 resources and values · 3 communication and the near world, the mind's daily traffic · 4 home and roots, the floor of the chart · 5 creation and pleasure · 6 health and service, the daily work · 7 partnership, the facing other · 8 transformation and depth — what is shared, lost, and remade · 9 philosophy and far travel, the doctrine of the life · 10 direction and summit, the visible legacy · 11 community and vision, the people of the future · 12 the unconscious and surrender, what dissolves behind the world.

## 6 · The seven relations (of eleven)

From the entering sign at index *i*, with peer(k) = the court of sign *i+k* (mod 12):

| Relation | Peers | Meaning |
|---|---|---|
| **challenges** | peer(+3), peer(+9) | the rank-mates on the perpendicular crossroads — same office, perpendicular roads |
| **precedes** | peer(−1) | their road's end lies near your departure; what they finish, you inherit |
| **succeeds** | peer(+1) | your road's end lies near their departure; what you finish, they inherit |
| **empowers** | peer(+4), peer(+8) | the suit-kin — the same elemental crossing at other gates |
| **complements** | peer(+6) | across the whole wheel — **across overrides rank**; the mirrored crossing: what you pour out, they gather; what they spill, you seed |
| *cannot see* | peer(±2, ±5) | **anatomy, never performed** — four roads off the map, and the map's edge is not a wound |

Movement order in the letter: challenges ×2, precedes, succeeds, empowers ×2, **complement closes** — the deepest encounter ends the movement (mirror of D2's competitor-closes and D3's sister-last).

**Company cargo:** a relation's "they carry" is their **whole road** — all three of their stations' occupants together, natures only, felt volume banded on the whole road. Pronouns by rank: Queen her/she, King his/he, Knight their/they.

## 7 · The persona roster

`PathsofRevSkills/majestic-persona-<type>` (Skills MCP), whole and unedited:

| | Wands | Chalices | Swords | Pentacles |
|---|---|---|---|---|
| **Queen** | intj | isfp | intp | isfj |
| **Knight** | enfp | enfj | estj | estp |
| **King** | entp | esfj | entj | esfp |

## 8 · The Recognition Pass (reader-side, post-performance) — RATIFIED 2026-09-05

**The law: only performed speech is scored — nothing enters the engine that didn't first pass through a throat.** The persona instruments are trained on embodied first-person speech; a payload line, a station datum, an essential nature is no one speaking, and the deck says so (the traveling court refused one with *"I am not a mind that lives in symbolic preparation"*). Eligible texts: **letter passages** (cut at movement boundaries) and **ledger beats**. Never eligible: payload lines, prompts, natures, tables. There is no pre-pass; **dignity and aspects are the only pre-performance reader signals.**

The engine (full deck, 78 judges, `prompts-v2.1.1-sandwich-literal-form` era): every judged persona answers CLAIMED-with-why or REFUSED; refusers in a claiming arcana ground the difference ("I am not …, because I am …"). Filtered panels run in seconds; full-deck reads take minutes per beat — use `resonance_job_start` for bulk. Pin the `instrument` string and persona hashes (from `resonance_personas`) in the reading's frontmatter — the drift guard.

**The three readings, per letter:**

1. **The self-claim (fidelity check).** Movement 1 — the salutation, the baseline before the chart — scored against the card's own instrument. It should CLAIM. A refused salutation means the performance drifted from the instrument it wore: grounds for **re-call**, the resonant companion to the scope-scan (the scan catches vocabulary leaks; the self-claim catches voice drift).
2. **The bend profile (the diff, measured).** The same self-instrument across movements 1 → 2 → 4. The frozen instrument judges the baseline, and the road bends the baseline — so falling recognition through the chart-bent movements is the register working as designed, and the refusals' why-nots narrate the bend in the instrument's own words (the Knight of Pentacles, refusing his own bent departure: *"my hands are always in the room"* — against a road toward the room where hands are no use). Rising or flat recognition through movement 4 is worth a reader's note either way.
3. **The panels (recognition constellation).** Per station passage, a targeted panel: the card itself · the seat's pip (the decan where the placement stands) · the seat's appointed reader (per `2-Canon/readership.yaml`) · two or three structural neighbors. Full-78 reads are reserved for the register's proof card, or the ledger's Assertion beat. Who claims is reader-side color for the council; the why-nots are **other personas' first-person speech and must never enter a letter or a prompt.**

**Reader's Scores** (never sent): placement · station · dignity (classical majors; n/a for points, lots, moderns) · major aspects with orbs · one-line reader's application — plus, after performance, the Recognition Pass block: self-claim verdict, bend profile, panel claims. Stack cited from the Repository graph — never derived from the span, never performed; if the graph is unreachable, record the roster provisionally and flag for re-citation.

**History:** the 2026-09-04 runs pre-passed payload descriptions (31/31 `unclaimed`) — sealed unaltered as the artifact of the old method; the ruling closes the calibration question rather than answering it.

## 9 · Essential natures — the phrase-book

Identical to D1–D3; canonical short forms (extend in kind; never numbers, dignities, or aspect language):

**Bodies.** Sun — the core flame, identity's single light. Moon — keeper of tides and origins, memory, the one who tends what began. Mercury — the articulate mind, quick and exact. Venus — the lover of harmony, grace, the drawing-together. Mars — the will's blade: drive, heat, the fight carried in the body. Jupiter — the increaser: meaning, patronage, the open hand (retrograde: walking backward, gifts turned inward). Saturn — the old authority: boundary, weight, time's discipline. Uranus — the breaker of patterns. Neptune — the dissolver: the ideal, the veil, the boundless behind forms. Pluto — the underworld power: what transforms by taking down to nothing and rebuilding.

**Points.** North Node — the soul's forward direction, appetite for the unlived (the same head, twice measured). South Node — mastery already carried in, work finished before this life (the same tail, twice measured). True Lilith — the part that refuses structure. Black Moon Lilith — the refusal made sovereign, crowned in exile. Chiron — the wound that teaches. Pholus — the small cause with the vast release. Ceres — the great mother: harvest, grief, and the return from grief. Pallas — the strategist's wisdom, the pattern seen whole. Juno — the covenant of partnership, loyalty and its terms. Vesta — the tended flame, devotion kept burning in private.

**Angles.** Ascendant — the horizon of appearing, where the querent rises to meet the world. Descendant — the facing door, where the other arrives. IC — the floor of the chart: midnight, root, the private ground. MC — the crown of the meridian, the visible summit-point.

**Lots.** Fortune, of the Moon — the body's own luck. Spirit, of the Sun — the soul's own initiative. Courage, of Mars — the fight the body is willing to have. Eros, of Venus — desire's true aim. Necessity, of Mercury — the unchosen obligation, what must be. Victory, of Jupiter — the promised triumph. Nemesis, of Saturn — the account that comes due.

## 10 · Ratified-run values (Paul, 1989-01-06 15:10 Durham NC, Gemini rising — 2026-09-04)

Houses from Gemini rising: Aries H11 · Taurus H12 · Gemini H1 · Cancer H2 · Leo H3 · Virgo H4 · Libra H5 · Scorpio H6 · Sagittarius H7 · Capricorn H8 · Aquarius H9 · Pisces H10.

Roads (op/su/res occupant counts, whole-road band): Queen of Wands 1/0/0 thin (Ceres) · Knight of Pentacles 1/0/1 thin (Mars / — / Lot of Victory — the proof card) · King of Swords 1/2/1 peopled (Jupiter Rx / Fortune, Pholus / Ascendant) · Queen of Chalices 0/2/0 thin (Spirit, Chiron) · Knight of Wands 0/1/0 thin (Courage) · King of Pentacles 1/2/1 peopled (IC / South Node, True Lilith / Juno) · Queen of Swords 1/0/1 thin (BML / Necessity) · Knight of Chalices 0/0/1 thin (Pluto — doubly unmet) · King of Wands 1/0/2 peopled (Vesta / — / Eros, Descendant) · **Queen of Pentacles 1/3/3 crowded** (Venus / Moon, Uranus, Saturn / Neptune, Sun, Nemesis) · Knight of Swords 0/1/0 thin (Mercury) · King of Chalices 2/1/0 peopled (Pallas, MC / North Node).

**Five jewel seats stood empty** (Queen of Wands, Knight of Pentacles, Queen of Swords, Knight of Chalices, King of Wands) — read by the council as one testimony. All 31 placements ride exactly one road (tiling verified).
