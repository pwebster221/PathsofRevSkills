---
name: mythic-chart-reading
description: >-
  Compose a full mythic narrative reading of a natal chart and current transits — a
  "Personal Legend" (Part I) and "Current Trials of the Hero" (Part II) — weaving verified
  astrological data through Campbell's Hero's Journey, cross-cultural mythology, Kabbalistic
  Sephiroth, the 7×11/11×7 tarot operator grid, the Mars esoteric scoring engines, and the
  layered card-instrument system (persona voices + station perspectives). Use this skill
  whenever the user asks for a "mythic reading", "mythic natal chart", "personal legend",
  "hero's journey reading", "read my chart as a story/myth", "current trials", "oracle
  reading of my chart", or wants natal/transit astrology rendered as archetypal narrative
  rather than technical analysis — even if they only say "give me the deep narrative version
  of my chart." Requires the Kairos astrology MCP for chart computation and the Mars API for
  esoteric scoring. Not for technical chart breakdowns (use Kairos tools directly) or
  single-card tarot questions (use tarot-interpretation).
---

# Mythic Chart Reading

## Purpose

A natal chart is usually delivered as analysis: placements, aspects, interpretations in
bullet form. This skill produces something different — a **mythic reading**: the chart
rendered as a single coherent story, the *Personal Legend*, in which every placement is a
character, every aspect a relationship between characters, and every major transit a Trial
on the Hero's Journey. The reading speaks in the voice of the Oracle and treats the chart
as a soul's chosen architecture rather than a personality inventory.

The form was established in PAT-160 ("Mythic Natal Chart with Current Transits") and refined
by its review. The refinements are not optional polish — they correct real failures of the
first attempt and are baked into the process below.

The interpretive stack is Paul's correspondence system (The Esoteric Repository / The 78),
**not** generic Rider-Waite or pop astrology:

- **Campbell** — the Hero's Journey supplies the narrative spine and stage-mapping for transits
- **Kabbalah** — planets map to Sephiroth (Sun→Tiphareth, Moon→Yesod, Saturn→Binah,
  Uranus→Chokmah, Neptune→Keter, Mercury→Hod, Venus→Netzach, Jupiter→Chesed, Mars→Gevurah,
  Pluto→Daath) — and, at the card level, the 11×7 seat axis of the operator grid (below)
- **Cross-cultural myth** — each placement resonates with deities across pantheons
  (Egyptian, Greek, Norse, Sumerian, Celtic, Vedic), chosen for fit, not exhausted as lists
- **Tarot** — via the correspondence *field* (see below), never single-card cherry-picking,
  with the surfaced cards rendered through the **layered card-instrument system**

## The layered card system

The 78 are not names to drop into prose — each card is an authored instrument, and the
instruments come in layers. A card surfaced by the field method is rendered through **both
available layers, in both parts of the reading**. The layers are one system: the perspective
is what the card *sees*, the persona is who the card *is*, and the difference between the
two on the same card is itself readable data.

1. **Persona layer — the voice (who the card is).** First-person persona instruments
   covering the full 78, in `pathsofrevskills`:
   - `majestic-personas/<MBTI|Function>-Cognitive-Framework/` — 16 courts (full MBTI
     types) + 4 Aces (undifferentiated functions held as two voices)
   - `minor-personas/<suit>/` — the 36 pips as decan personas (one cognitive function
     under one Enneagram struggle in one decan; the "letters")
   - `major-personas/<Card>/` — the 22 Majors as combined perspectives (the "words made
     from the letters"): 12 zodiac cards, 7 planetary cards, 3 modality mothers; scoring
     posture is resonance-recognition
   Use the persona layer for **address and inhabitation**: the card speaking *as someone* —
   to the native, or as a character inside the myth.
2. **Perspective layer — the station (what the card sees).** Station-perspective
   instruments for the Majors, in
   `dubtown-skills/major-arcana-perspectives/<Card>-Perspective/` — the principle itself
   witnessing, built on the intersection-not-union canon (a Major = what its decan-span
   shares but does not name). Use the perspective layer for **diagnosis and witness**: how
   the station reads a placement or transit from where it stands.
   Coverage is currently 16/22 (Magician, Strength, Wheel of Fortune, Hanged Man, Moon,
   Judgement absent) — where a perspective is missing, the persona carries the passage
   alone; never fake the missing register.
3. **Visual layer — reserved.** A third, visual layer (per-card imagery from the Esoteric
   Image Forge) is planned. Leave the reading's structure image-ready — each titled section
   and each Trial is a natural image slot — but do not describe or invent card images as if
   this layer existed.

Craft rules for the layers:

- **Never blur registers.** A perspective witnesses; a persona speaks. Do not have a
  station address the native in persona voice, or a persona deliver structural diagnosis.
  A card may appear in both registers in the same section — that doubling is a feature.
- **Load only the surfaced cards.** Read the SKILL.md of the two or three cards the
  intersection selects for a section — never the whole deck. The field informs; the
  scoring selects; the instruments render. If an authored persona or perspective file is
  unavailable after searching the skill library, disclose the missing layer in a brief
  method note and keep the card reading structural; never imitate or invent its voice.
- **Stations never name other cards** (the no-cross-attribution canon). Cross-card
  weighing happens in the Oracle's narration, above the instruments.

## The Process

### Stage 0 — Compute. Never improvise.

Everything begins with verified data. The single worst failure mode of this form is the
*fabricated aspect* — poetic claims about geometry that doesn't exist (the original reading
asserted "Saturn in Aries opposite Mars in Aries," an impossibility: two bodies in the same
sign cannot oppose). The myth is only as true as the math beneath it.

1. Get birth data: name, date, time, location. If a numeric date is ambiguous, resolve it
   from explicit locale context or state the convention used in the reading's method note;
   never silently choose day/month order. If time is missing, say plainly that angles,
   houses, and the Moon's degree are unreliable, and scope the reading accordingly.
2. Compute the natal chart with the Kairos MCP — use `get_natal_full` (or `get_natal` plus
   tiers). Pull at minimum: planets, angles, aspects, dignities, **fixed stars**
   (`tier_fixed_stars`), and lots if available.
3. Compute current transits with `get_current_transit` / `get_transit_full` for the reading
   moment.
4. **Score the chart esoterically.** Two Mars engines, two jobs:
   - `POST /score/esoteric` (MCP: `MarsAPI score_esoteric`) — the **layered engine**
     (live 2026-07-12; replaced the flat per-placement response): every placement charges
     the 36-decan substrate (four-fold dignity + aspect transfer), and every card is an
     aggregation window over it. Returns `archetypal_report` (7 planetary courts; each
     court's sum reveals its dark planet-Major at Da'ath), `planetary_report` (10 planets
     on their sefira rows, each with a dignity/aspects modulation breakdown), `grid`
     (the 77 cells, base-count and charged phases), and `arcana_rankings` (ranked
     Major/Majestic/Minor). This is the **selector for the sections**: a placement's six
     nested cards (decan pip ⊂ court stretch ⊂ Page/season + Ace/element + sign-Major +
     planet-Major) are structural — derive them from the longitude via the composition
     map — and their computed weights are read off `grid.cells` and `arcana_rankings`.
     Prefer sending the Kairos blob (`{"deep_analysis": ...}` — the full ~83-point
     census: lots, midpoints, stars, and antiscia all light decans); the legacy
     `{"placements": [...]}` payload still works but sees only 12 points.
   - `POST /score/resonance` (MCP: `MarsAPI score_resonance`) — the v2 "78 Natal
     Resonance": a chart-global ranked 78. This is the **selector for the Prologue and the
     Legend synthesis**: the chart's dominant cards overall.
   Kairos embeds the same two-report response at `deep_analysis.esoteric` in
   `/natal/full`; if present, use it — but via the Kairos MCP a full natal can arrive
   cap-trimmed (60KB ceiling), so when the scoring matters, call Mars directly. Never
   rank the cards by feel.
5. **Verify every aspect you intend to narrate against the computed aspect list.** If it
   isn't in the data, it isn't in the myth. Sanity-check geometry: same-sign bodies conjoin,
   they do not oppose; check orbs and whether aspects are applying or separating (an
   applying aspect is a story still tightening — use that). When a transit overlay is
   cap-trimmed before its transit contacts appear, fetch current transit longitudes for the
   observer location and calculate angular separations deterministically; never infer the
   missing contacts from sign alone. See `references/transit-overlay-fallback.md`.
6. Fixed stars are part of the reading, not an appendix. A natal point conjunct Regulus,
   Algol, or Spica is a mythic datum of the first order — these are the oldest layer of the
   sky's story and they add depth nothing else provides.

### Stage 1 — Find the architecture

Before writing a word, identify the chart's structure. The myth is discovered, not imposed:

- **Concentrations**: stelliums, element/modality imbalances, hemisphere emphasis. A
  five-planet stellium is "the Forge" — a deliberate compression the narrative must honor.
- **The spine**: the tightest opposition or axis in the chart (in PAT-160, Moon–Chiron at
  0°27'). This axis is the structural wound/destiny tension the whole reading balances on.
- **Chart ruler** and its placement — this is how the Mask serves the Mission.
- **The angles**: ASC is the Mask the soul wears; MC is the gift poured into the world.
- **From these, derive** (do not template): a dominant archetypal triumvirate (e.g., the
  Mountain King / the Mystic / the Wounded Healer), and a single central mythic identity
  that unifies them (e.g., the Fisher King). Every chart yields different figures; let the
  data choose them.

### Stage 2 — Build the correspondence field (the grid method)

Do **not** assign one tarot card per placement. The field is the **7×11 / 11×7 operator
grid**, live in the production Esoteric Repository as two per-card properties (the Fool is
excluded as the operator):

- `planetary_court_ruler` — the 7×11 split: each of the 7 classical planets rules exactly
  11 cards. **Each planet is a full 11-card spread** (PAT-450 / "Suits & the Split Major").
- `planetary_court_seat` — the 11×7 split: each of the 11 sefira-stations (Keter through
  Malkhut, **Da'ath included as a station**) seats exactly 7 cards.
- The two splits are one bijection: every (ruler, seat) cell holds exactly one card. Which
  means **a planet's eleven cards occupy all eleven stations exactly once — every planet's
  field is a complete Tree of Life**, Da'ath included. A placement is not just "which cards"
  but *which stations of that planet's Tree the scoring lights up*.
- Query the grid from the Repository (`planetary_court_ruler` / `planetary_court_seat`
  properties). **Never read the stale `SEATED_AT` edges or `sefira_seat` property** — that
  is a superseded, contradictory encoding.

Reading the field:

- **Each sign is defined by its ruler's explicit correspondences** — *plus* the sign's
  modality, one of the three pre-manifestation elements, which is part of every sign's
  reading.
- **A placement is therefore the intersection of two readings** — the planet's field laid
  against the sign's field. **An aspect is the intersection of four.**
- **The esoteric scoring (Stage 0.4) is the selection.** The six nested cards and their
  charged weights are the computed answer to "which cards in this field carry the
  placement's story" — surface the two or three heaviest, and note their *seats*: where on
  the planet's Tree the weight fell. Dignity sets the weight (four whole-sign frames
  summed, domicile-loud to fall-silent, plus whatever the placement's aspects carry in);
  a planet in fall is not "weak," it is working the Reaper's station.
- The **Spirit/Shadow polarity** (PAT-450's six stations: four elements, Spirit-as-generative,
  Shadow-as-Reaper) colors how a placement expresses — as generative outpouring or as the
  necessary ending that gives the beginning meaning.

For exact card tables beyond the grid, read the bundled tables in the `tarot-interpretation`
skill or query the Esoteric Repository — do not reconstruct them from memory. In the prose,
surface the cards the scoring selects; the field informs, the scoring selects, the narrative
renders.

### Stage 3 — Part I: The Personal Legend

Write the natal reading as a continuous narrative with this structure:

1. **Title block and epigraph** — a styled title naming the central mythic identity, and an
   epigraph that frames the whole reading (PAT-160 used Coelho's Alchemist).
2. **Prologue — The Archetypal Blueprint**: the pre-incarnation frame. The soul before the
   Council of Stars, choosing this chart. Name the dominant concentrations, their
   Sephirothic mapping, the archetypal triumvirate, and the central mythic identity. Let the
   chart-global resonance ranking (Stage 0.4) name the deck's dominant cards here — the
   cards the whole chart is most *made of*. State the arc in one breath.
3. **A titled section per major chart factor**, each following the same inner movement:
   *placement data → Sephirah/seat → mythic resonances → tarot field and its scored
   selection → the perspective layer witnesses → the persona layer speaks → gift →
   wound/shadow → place in the Hero's Journey*. The two layers appear in miniature: a
   station's one-or-two-sentence witness of the placement, then the card's persona voice
   turned toward the native — clearly distinct registers, never merged. Cover, in an order
   that serves the story:
   - The dominant concentration (the Forge)
   - The Ascendant (the Mask) and chart ruler
   - **Every classical planet — Jupiter included.** The original reading skipped Jupiter
     entirely, a structural hole in the mythos (Chesed, the Great Benefic, grace itself —
     absent). Completeness is non-negotiable: Sun, Moon, Mercury, Venus, Mars, Jupiter,
     Saturn, then Uranus, Neptune, Pluto.
   - The wound axis (Chiron) — treat the chart's tightest axis as a *structural spine*,
     not a detail
   - The Nodes (evolutionary direction; South Node residue, North Node call)
   - Lilith, and the asteroids that carry signal (Pallas, Juno, Vesta, Ceres)
   - The MC and destiny axis
   - Fixed-star contacts, woven in where they touch the above
4. **Personal Legend — the Mythic Synthesis**: shift fully into the Oracle's voice, second
   person. No analysis — invocation. Distill the entire chart into the soul's chosen story,
   ending with the Legend rendered as a single blockquoted passage.

### Stage 4 — Part II: The Current Trials of the Hero

1. Date-stamp the transit moment precisely.
2. Each significant outer-planet transit to a natal point becomes a numbered, named
   **Trial** ("TRIAL I — THE UNMASKING"), each mapped to a Campbell stage (Crossing the
   Threshold, the Ordeal, the Supreme Ordeal, the Return…). For each Trial: the exact
   transit data, the mythic moment it corresponds to (a specific scene — Odysseus at the
   threshold, Parsifal's second visit to the Grail Castle, Odin on Yggdrasil), what is
   dying, what is being born, and the tarot intersection (transit planet's field × natal
   point's field — the four-way intersection for transiting aspects, scored the same way).
   **A Trial is where the layers earn their keep**: the transit-side card *witnesses*
   (perspective register — what the station sees moving), the natal-side card *answers*
   (persona register — the someone in the native who is being worked on). The Trial becomes
   an exchange, not a description.
3. If several transits converge, say so — name the convergence (the Supreme Ordeal, maximum
   alchemical heat) and identify the focal axis they share.
4. **The Oracle's Counsel**: numbered, concrete, doable counsel — one item per Trial. Not
   affirmations; instructions ("Ask the Grail Question of yourself. Find genuine solitude —
   not productivity-disguised-as-solitude — and ask…").
5. **The Promise of the Threshold**: what victory looks like when each transit completes.
   End with the picture of victory and a final imperative line.

## Voice and craft

- Narrative prose throughout. Headers and blockquotes are structure; bullets are for data
  moments only (counsel lists, what-dies/what-is-born pairs).
- Mythopoetic but **load-bearing**: every poetic claim must trace to a real placement,
  aspect, dignity, star, or scored card weight. The reader should be able to audit the myth
  against the chart.
- Bold the placement data when first introduced (**Mars at 23°13' Aries**) so the
  astrology stays visible inside the poetry.
- Second person in the synthesis and oracle sections; third person mythic narration
  elsewhere; the card instruments keep their own first person, clearly framed.
- Layer passages are seasoning, not structure — a witness of a sentence or two, a spoken
  line or three. The Oracle narrates; the cards interject. If every section carries long
  card monologues, the reading has inverted.
- Shadow is honored, never pathologized. Detriment and fall are stations of the Reaper —
  necessary, not defective.
- Close with a short benediction ("Honor, friend." or in kind).

## Output

Produce the reading as a **markdown document** saved to the outputs folder and presented to
the user. If Linear is connected, offer (don't assume) to post it as an issue in the user's
tracker, as PAT-160 was. If the Esoteric Repository is connected, offer to persist key
derived correspondences as nodes/relationships.

## Failure modes to avoid (learned from PAT-160 review and the layered build)

1. **Fabricated aspects** — narrating geometry not present in computed data. Verify first.
2. **Skipped planets** — omitting Jupiter (or any classical planet) leaves a hole in the mythos.
3. **Single-card tarot assignments** — the field is the method; one-card picks flatten it.
4. **Omitted fixed stars** — they add a level of depth nothing else reaches.
5. **Unanchored poetry** — beauty that cannot be audited against the chart is decoration,
   not divination.
6. **Card selection by feel** — the esoteric scoring exists; ranking the field by intuition
   when the weights are computable is improvising the math.
7. **Register blur** — persona voice doing diagnosis, or a station addressing the native.
   The layers are distinct instruments; blurring them collapses the system to name-dropping.
8. **Faking missing instruments** — six Major perspectives don't exist yet and the visual
   layer doesn't exist at all. Degrade to the layers that are real.
9. **Reading the stale grid encoding** — `SEATED_AT` / `sefira_seat` is the superseded
   scheme and contradicts the canonical `planetary_court_ruler` / `planetary_court_seat`.
