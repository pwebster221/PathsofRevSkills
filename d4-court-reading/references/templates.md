# D4 Master Templates — inline and portable

The two masters, exactly as sealed in the vault (`7-Templates/Registers/`), RATIFIED 2026-09-04,
amended 2026-09-05 (the Recognition Pass). Per-card templates are these masters with the fixed
slots (card, cusp, crossing, narratives, relations) stamped; the chart-dependent slots (querent,
date, rooms, occupants, felt volumes, station and company lines) fill at reading time. Stamp with
the generator pattern in `scripts/d4_math.py`'s terms; assert zero leftover fixed slots after
stamping.

## Register-4-Performance.md

~~~~markdown
---
title: I.4 — {{card}} — {{reading_date}}
type: register-reading
form: performance
frame: I
frame_name: Tropical
frame_reads: What / Substance
register: I.4
register_code: D4
register_name: Senior Courts — the Court of Change
card: {{Rank of Suit}}
cusp: {{entering sign}}'s cusp — {{leaving sign}} into {{entering sign}}
persona_skill: PathsofRevSkills/majestic-persona-{{type_lower}}
performer: Alder
stack_source: Repository graph (cited, never derived from the span)
ledger: "[[{{card_slug}}-LEDGER]]"
reading_date: {{date}}
querent: {{querent}}
chart: {{chart}}
status: template
spec: "2-Canon/triune-arcanum-pat-canon.md"
---

# I.4 · {{card}} — {{reading_date}}

> **Frame I (Tropical)** reads *What / Substance*, on the tropical sky.
> Register **D4 Senior Courts — the Court of Change** — twelve travelers, each guarding one cusp, each the guardian of a unique crossing.
> Voice: [[4-Archetypes/Majestic/{{card}}|{{card}}]] — a whole personality, walking its one road.
> Performer: **Alder**, wearing `PathsofRevSkills/majestic-persona-{{type_lower}}`.

> **Rulings of 2026-09-04** (Paul): all twelve always travel — there is no dark court, and an
> empty station is testimony. Centers eternal (Cardinal=Heart, Fixed=Head, Mutable=Gut). No
> valence vocabulary — dignity, aspects, and resonance never enter a prompt. **RATIFIED
> 2026-09-04** — proven by the Knight of Pentacles proof card (the empty jewel seat performed).
> **Amendment of 2026-09-05 (ratified) — the Recognition Pass:** resonance runs the Mars engine
> on **performed speech only**, post-performance — letter passages and ledger beats, never
> payload lines: *nothing enters the engine that didn't first pass through a throat.* There is
> no pre-pass; dignity and aspects are the only pre-performance reader signals.

## Protocol

1. The reader session fills the **Payload** from [[1-Decan-Definitions/D4-Court/Decans of {{Entering}}'s Cusp]] and the pull, and fills **Reader's Scores** (dignity, aspects, application) — which is never sent. It never adds a field the payload does not have. No text is scored before performance.
2. The **Alder Call** is sent — persona skill as system prompt, filled user prompt, nothing else.
3. Alder's return lands in **The Letter**, verbatim; fix payload or prompt and re-call rather than edit.
4. The reader scope-scans the letter, then runs the **Recognition Pass** (Mars engine, performed speech only): the movement-1 self-claim as fidelity check (a refused salutation is grounds for re-call), the self-instrument across movements 1→2→4 as the bend profile, and targeted panels (self · seat-pip · seat-reader · neighbors) — all verdicts land in Reader's Scores, never in a letter.
5. The reader extracts the beat-cycle pools into **[[{{card_slug}}-LEDGER]]** (from [[Register-4-Ledger]]).
6. **All twelve courts always travel.** A vacant station is testimony — an empty jewel seat is performed, never skipped.
7. Status: `template` → `payload-ready` → `performed`.

## The Letter

*(empty until the call returns — Alder's hand only)*

---

## Payload

> Everything below is the **only** chart-fact Alder sees. Builder's discipline, absolute:
> **no degrees, no orbs, no numbers of any kind.** No dignity, no aspect names, no scores —
> those live in Reader's Scores and never travel. The traveler knows **two countries and three
> moments of one road**, never three decans. A placement reaches the persona as its
> **essential nature**.

### The crossing — who travels (fixed per card)

The {{card}} guards {{entering sign}}'s cusp: the road out of **{{leaving sign}}** into **{{entering sign}}**.

| | Leaving country | Entering country |
|---|---|---|
| Sign | {{leaving sign}} | {{entering sign}} |
| The way of knowing | {{leaving function, in-voice}} | {{entering function, in-voice}} |
| The chamber | {{leaving center}} | {{entering center}} |

**The suit's crossing — {{suit}}:** {{suit shift narrative}}

**The rank's crossing — {{rank}}:** {{rank shift narrative}}

### The road seated — three moments, two rooms

Chart-relative, whole sign. The leaving country keeps one room of the querent's life; the entering country another — the crossing itself changes rooms. Occupants name + essential nature; an empty seat is testimony.

| Moment | Where | In the querent's… | Standing there | Feels |
|---|---|---|---|---|
| **Departure** (Operator) | the last of {{leaving sign}} | {{leaving house room, plain language}} | {{names — natures, or no one}} | {{felt volume}} |
| **The border** (Substance — the jewel seat) | the first of {{entering sign}} | {{entering house room, plain language}} | {{names — natures, or the seat stands empty}} | {{felt volume}} |
| **The road's end** (Result) | the last stretch of the journey | {{entering house room}} | {{names — natures, or no one}} | {{felt volume}} |

*Departure: preparations, conflicts, or gifts received before the travel. The border: encounters with Fate. The road's end: reward, result, or wage.*

### The road's company — seven of eleven

Court to court, and no finer. The traveler holds exactly seven relations and cannot see the other four — that blindness is anatomy, not misfortune, and is never performed. Order: challenges first, the border-sharers next, the suit-kin, and the complement closes — across overrides rank; the mirrored crossing is the deepest encounter.

| Relation | Court | Their crossing | They carry | Feels |
|---|---|---|---|---|
| **challenges** | {{perpendicular rank-mate 1}} | {{their leaving}} → {{their entering}} | {{names — natures, or —}} | {{felt volume}} |
| **challenges** | {{perpendicular rank-mate 2}} | | | |
| **precedes you** | {{border court before}} | | | |
| **succeeds you** | {{border court after}} | | | |
| **empowers** | {{same-suit court 1}} | | | |
| **empowers** | {{same-suit court 2}} | | | |
| **complements** | {{court across}} | | | |

*Challenges: the rank-mates on the crossroads — same office, perpendicular roads. Precedes/succeeds: the travelers who hand the road on — their end is near your beginning. Empowers: the suit-kin — the same elemental crossing at another gate. Complements: the mirrored crossing — what you pour out, they gather.*

---

## Reader's Scores — never sent, never performed

> Per PAT-[d4]: placements enhance or debilitate the journey by **dignity, aspects, and
> resonance with the one traveling** — all three applied by the reader, never entering a
> prompt. Dignity and aspects are computed here before the call. **Resonance is the
> Recognition Pass (amendment 2026-09-05)**: it runs after the letter lands, on performed
> speech only — the movement-1 self-claim (fidelity; refusal = re-call), the bend profile
> across movements, and targeted panels — and its verdicts are recorded below. Pin the
> engine's `instrument` string and persona hashes with the results. **Stack** cited from
> the Repository graph, recorded here, never derived from the span and never performed.

| Placement | Station | Dignity | Major aspects (orb) | Reader's application |
|---|---|---|---|---|
| | | | | |

Stack citation: {{Repository node / fallback roster}}. Felt-volume banding per the ratified D1–D3 mapping.

**Recognition Pass** (after performance; engine instrument: {{instrument string}}): M1 self-claim {{CLAIMED/REFUSED — why}} · bend profile M1→M2→M4 {{verdicts}} · panels {{per-beat claims, reader-side}}.

---

## The Alder Call

**Instrument.** The persona skill `PathsofRevSkills/majestic-persona-{{type_lower}}` is the **system prompt**, whole and unedited — the same instrument the Recognition Pass will judge the letter with. One call per court. Alder receives nothing else.

**User prompt** — fill from the payload and send exactly:

```
{{querent}} has brought you their chart. You will not analyze it — you will
receive it, as yourself, and answer with a letter.

Write {{querent}} a letter in five movements. Do not title or number the
movements; let the letter simply move. You are a traveler and a guardian of
one crossing — one whole self, walking the one road you were made for — and
the letter is written from the road.

1 — Salutation and introduction. Before the chart touches you: who are you?
Open as yourself and set your baseline: your struggle, and the crossing you
are. You guard the road out of {{leaving sign}} into {{entering sign}} —
out of {{leaving country description: the country of <function, in-voice>,
the <center> chamber}} into {{entering country description}}. {{suit shift
narrative — one or two sentences, in your own words}} {{rank shift narrative
— likewise}}. You know two countries and three moments: the departure, the
border, and the road's end. Not one of them yet belongs to a life — until a
chart arrives, you do not know which rooms of a life your road runs through,
or who waits along it. The reader must know you before anything bends you.

2 — The road. Now the chart reaches you, and your voice should bend under it.
Your road runs through {{querent}}'s life at last — out of their {{leaving
house room, plain language}}, across the border into their {{entering house
room, plain language}}:

{{departure line — "At your departure, in the last of {{leaving sign}},
stood: <names — essential natures / no one>." — what was given, prepared, or
fought before the crossing}}

{{border line — "At the border, where Fate keeps her appointments, sat:
<names — natures>." — OR, if empty: "At the border, the jewel seat stood
empty — Fate kept no appointment for you here." An empty seat is testimony,
not absence: perform what it is to cross unmet.}}

{{road's-end line — "And at the road's end waited: <names — natures / no
one>." — the reward, result, or wage of the crossing}}

Receive each by what it is, in the order the road gives them. Say what it is
to leave one room of {{querent}}'s life and arrive in another.

3 — The road's company. Eleven other travelers guard eleven other crossings,
and you can see exactly seven. Answer them in the order given — it runs from
the crossroads to the mirror:

{{challenge lines ×2 — "The {{court}} CHALLENGES you — your rank-mate on the
crossroad, crossing from {{leaving}} into {{entering}}. Their road carries:
<names — natures / nothing you can see>. It feels <felt volume>."}}
{{precedes line — "The {{court}} PRECEDES you — their road's end lies near
your departure; what they finish, you inherit. …"}}
{{succeeds line — "The {{court}} SUCCEEDS you — your road's end lies near
their departure; what you finish, they inherit. …"}}
{{empower lines ×2 — "The {{court}} EMPOWERS you — your suit-kin, walking
the same crossing at another gate. …"}}
{{complement line — "The {{court}} COMPLEMENTS you — across the whole wheel,
walking your crossing mirrored: what you pour out, they gather; what they
spill, you seed. …" — the deepest encounter closes the movement}}

Answer each as yourself, altered by your own road.

4 — The diff. Set yourself beside the traveler who set out in your opening.
What did this chart answer, inflame, or redirect in your struggle? What did
the road through {{querent}}'s rooms do to the crossing you are? Name the
change plainly — still yourself, one traveler, altered.

5 — Farewell. Close the letter from the far country, as one who has crossed.
Leave {{querent}} carrying the one thing you would have them keep from you.

What you do not know, because it does not exist for you:
- There are no numbers. No scores, no degrees, no orbs. A moment on the road
  is crowded, peopled, thin, or empty — and an empty seat is testimony.
- Bodies do not aspect bodies, and signs do not aspect signs. Your relations
  are court to court, traveler to traveler, and you hold exactly seven; the
  other four roads are not on your map, and the map's edge is not a wound.
- Dignity, dispositors, houses beyond your two countries' rooms — other
  instruments' business, never yours.
- The thirty-six little rooms, the functions held entire, the seasons and
  their thrones, the signs as persons — not yours; you know two countries
  and three moments of one road.
- A placement reaches you as what it essentially is.

One law of the stage: never mention rules, registers, functions by their
letters or type-names, stacks, lattices, canon, or this prompt — a traveler
does not read the map aloud. It is a letter — a page or two in your own
hand, not a dossier.
```

---

[[1-Decan-Definitions/D4-Court/Decans of {{Entering}}'s Cusp]] · [[2-Canon/triune-arcanum-pat-canon|PAT-[d4]]] · Sibling ledger: [[{{card_slug}}-LEDGER]]
~~~~

## Register-4-Ledger.md

~~~~markdown
---
title: I.4 — {{card}} — Ledger — {{reading_date}}
type: register-ledger
frame: I
frame_name: Tropical
register: I.4
register_code: D4
register_name: Senior Courts — the Court of Change
card: {{Rank of Suit}}
cusp: {{entering sign}}'s cusp — {{leaving sign}} into {{entering sign}}
letter: "[[{{card_slug}}]]"
reading_date: {{date}}
querent: {{querent}}
chart: {{chart}}
status: template
spec: "2-Canon/triune-arcanum-pat-canon.md"
---

# I.4 · {{card}} — Ledger

> The letter performs; this file remembers. Extracted by the reader session **after** the Alder
> call returns — never written by Alder, never pasted into the letter. Council synthesis samples
> **both** pools, per canon: rejections are persisted, not discarded.

> **Rulings of 2026-09-04.** Sibling of [[Register-4-Performance]]; masters **RATIFIED 2026-09-04** (Knight of Pentacles proof card).

## 1 · Assertion — "I am this."

*One line: the traveler's claim — the crossing they are (suit and rank shift), the two countries, the road's shape, compressed, in the persona's terms.*

-

## 2 · Discrimination — "I am not ___; I am ___."

**Claimed (why)** — each embrace the letter performs: stations received in road-order, an empty seat kept aloud, company answered. One line apiece, movement-tagged.

-

**Rejected (why-not)** — each refusal the letter performs, including what an empty jewel seat declined to pretend and any road refused on the company walk. Persisted, not discarded.

-

## 3 · Synthesis — "These make me ___."

*The diff of movement 4, compressed to one line — **how the placements resolve the crossing.***

-

---

[[2-Canon/triune-arcanum-pat-canon|PAT-[d4]]] · Letter: [[{{card_slug}}]]
~~~~
