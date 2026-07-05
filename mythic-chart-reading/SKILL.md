---
name: mythic-chart-reading
description: >-
  Compose a full mythic narrative reading of a natal chart and current transits — a
  "Personal Legend" (Part I) and "Current Trials of the Hero" (Part II) — weaving verified
  astrological data through Campbell's Hero's Journey, cross-cultural mythology, Kabbalistic
  Sephiroth, and the 7×11 tarot correspondence field. Use this skill whenever the user asks
  for a "mythic reading", "mythic natal chart", "personal legend", "hero's journey reading",
  "read my chart as a story/myth", "current trials", "oracle reading of my chart", or wants
  natal/transit astrology rendered as archetypal narrative rather than technical analysis —
  even if they only say "give me the deep narrative version of my chart." Requires the Kairos
  astrology MCP for chart computation. Not for technical chart breakdowns (use Kairos tools
  directly) or single-card tarot questions (use tarot-interpretation).
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
  Pluto→Daath)
- **Cross-cultural myth** — each placement resonates with deities across pantheons
  (Egyptian, Greek, Norse, Sumerian, Celtic, Vedic), chosen for fit, not exhausted as lists
- **Tarot** — via the correspondence *field* (see below), never single-card cherry-picking

## The Process

### Stage 0 — Compute. Never improvise.

Everything begins with verified data. The single worst failure mode of this form is the
*fabricated aspect* — poetic claims about geometry that doesn't exist (the original reading
asserted "Saturn in Aries opposite Mars in Aries," an impossibility: two bodies in the same
sign cannot oppose). The myth is only as true as the math beneath it.

1. Get birth data: name, date, time, location. If time is missing, say plainly that angles,
   houses, and the Moon's degree are unreliable, and scope the reading accordingly.
2. Compute the natal chart with the Kairos MCP — use `get_natal_full` (or `get_natal` plus
   tiers). Pull at minimum: planets, angles, aspects, dignities, **fixed stars**
   (`tier_fixed_stars`), and lots if available.
3. Compute current transits with `get_current_transit` / `get_transit_full` for the reading
   moment.
4. **Verify every aspect you intend to narrate against the computed aspect list.** If it
   isn't in the data, it isn't in the myth. Sanity-check geometry: same-sign bodies conjoin,
   they do not oppose; check orbs and whether aspects are applying or separating (an
   applying aspect is a story still tightening — use that).
5. Fixed stars are part of the reading, not an appendix. A natal point conjunct Regulus,
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

### Stage 2 — Build the correspondence field (the corrected tarot method)

Do **not** assign one tarot card per placement. Each sign and planet has one *primary* card,
one or two by rulership (which implies one or two in fall), one exalted, one in detriment —
but the corrected method (final verdict, PAT-160 comments) considers the **entire field**:

- **Each planet is a full 11-card spread** (the 7×11 of PAT-450 / "Suits & the Split
  Major"): its major arcana (3), its minors (6 or 3), its Majestic cards (2 or 5), or a
  combination.
- **Each sign is defined by its ruler's explicit correspondences**: one major, four
  Majestic (overlap between signs is expected and fine), and three minors — *plus* the
  sign's modality, one of the three pre-manifestation elements, which is part of every
  sign's reading.
- **A placement is therefore the intersection of two readings** — the planet's field laid
  against the sign's field. **An aspect is the intersection of four.**
- The **Spirit/Shadow polarity** (PAT-450's six stations: four elements, Spirit-as-generative,
  Shadow-as-Reaper) colors how a placement expresses — as generative outpouring or as the
  necessary ending that gives the beginning meaning. Use it to read dignity and debility
  mythically: a planet in fall is not "weak," it is working the Reaper's station.

For the exact card tables, read the bundled tables in the `tarot-interpretation` skill or
query the Esoteric Repository — do not reconstruct them from memory. In the prose, surface
the two or three cards from the intersection that carry the placement's story; the field
informs, the narrative selects.

### Stage 3 — Part I: The Personal Legend

Write the natal reading as a continuous narrative with this structure:

1. **Title block and epigraph** — a styled title naming the central mythic identity, and an
   epigraph that frames the whole reading (PAT-160 used Coelho's Alchemist).
2. **Prologue — The Archetypal Blueprint**: the pre-incarnation frame. The soul before the
   Council of Stars, choosing this chart. Name the dominant concentrations, their
   Sephirothic mapping, the archetypal triumvirate, and the central mythic identity. State
   the arc in one breath.
3. **A titled section per major chart factor**, each following the same inner movement:
   *placement data → Sephirah → mythic resonances → tarot field → gift → wound/shadow →
   place in the Hero's Journey*. Cover, in an order that serves the story:
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
   point's field — the four-way intersection for transiting aspects).
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
  aspect, dignity, or star. The reader should be able to audit the myth against the chart.
- Bold the placement data when first introduced (**Mars at 23°13' Aries**) so the
  astrology stays visible inside the poetry.
- Second person in the synthesis and oracle sections; third person mythic narration
  elsewhere.
- Shadow is honored, never pathologized. Detriment and fall are stations of the Reaper —
  necessary, not defective.
- Close with a short benediction ("Honor, friend." or in kind).

## Output

Produce the reading as a **markdown document** saved to the outputs folder and presented to
the user. If Linear is connected, offer (don't assume) to post it as an issue in the user's
tracker, as PAT-160 was. If the Esoteric Repository is connected, offer to persist key
derived correspondences as nodes/relationships.

## Failure modes to avoid (learned from PAT-160 review)

1. **Fabricated aspects** — narrating geometry not present in computed data. Verify first.
2. **Skipped planets** — omitting Jupiter (or any classical planet) leaves a hole in the mythos.
3. **Single-card tarot assignments** — the field is the method; one-card picks flatten it.
4. **Omitted fixed stars** — they add a level of depth nothing else reaches.
5. **Unanchored poetry** — beauty that cannot be audited against the chart is decoration,
   not divination.
