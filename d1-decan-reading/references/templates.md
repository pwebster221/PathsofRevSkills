# The Master Templates — portable copies

Vault-authoritative copies live at `7-Templates/Registers/Register-1-Performance.md` and
`Register-1-Ledger.md`; per-card instantiations (fixed lords prefilled, full ring table) at
`6-Register-Readings/I/I.1/TEMPLATE/<Card>-TEMPLATE.md`. The copies below make this skill
self-sufficient when the vault is not reachable. `{{slot}}` marks pipeline-filled values.

---

## Register-1-Performance.md

````markdown
---
title: I.1 — {{card}} — {{reading_date}}
type: register-reading
form: performance
frame: I
frame_name: Tropical
frame_reads: What / Substance
register: I.1
register_code: D1
register_name: Decan Minors
card: {{card}}
decan: {{decan_1_to_36}}
decan_name: {{sign}} {{ordinal_roman}}
epithet: {{epithet}}
persona_skill: PathsofRevSkills/minor-persona-{{card_slug}}
performer: Alder
ledger: "[[{{card_slug}}-LEDGER]]"
reading_date: {{date}}
reading_time: {{time}}
querent: {{querent}}
chart: {{chart}}
status: template
spec: "2-Canon/triune-arcanum-pat-canon.md"
---

# I.1 · {{card}} — {{reading_date}}

> **Frame I (Tropical)** reads *What / Substance*, on the tropical sky.
> Register **D1 Decan Minors**. Voice: [[4-Archetypes/Minors/{{card}}|{{card}}]] — a situation, speaking.
> Performer: **Alder**, wearing `{{persona_skill}}`. The reading is a letter; the machinery stays offstage.

## Protocol

1. The reader session fills the **Payload** below from [[1-Decan-Definitions/D1-Decans/{{decan_note}}]] and the pull. It never adds a field the payload does not have.
2. The **Alder Call** at the end of this file is sent — persona skill as system prompt, filled user prompt, nothing else.
3. Alder's return is pasted into **The Letter**, verbatim. If it needs correcting, fix the payload or the prompt and call again; the letter is never edited by hand.
4. The reader session extracts the beat-cycle pools into the sibling **[[{{card_slug}}-LEDGER]]** — the letter performs, the ledger remembers.
5. Status advances: `template` → `payload-ready` → `performed`.

## The Letter

*(empty until the call returns — Alder's hand only)*

---

## Payload

> Everything below is the **only** chart-fact Alder ever sees. Builder's discipline, absolute:
> **no degrees, no orbs, no dignity scores, no sect, no dispositor chains, no house arithmetic
> beyond the Home resolution, no placement-to-placement aspects — anywhere, in any field.**
> What is not written here cannot leak. Rulings (cusp-splits, half-strengths) enter as plain
> facts, never as coordinates.

### Scene — the four lords

| Office | Lord | Clothed in | Note |
|---|---|---|---|
| Temporal | {{lord}} | {{elements}} | Chaldean traveler, wearing both domicile elements |
| Eternal | {{lord}} | {{element}} | Triplicity ascent — decan {{ordinal}} of the {{element}} ring |
| Presiding | {{lord}} | {{element}} | Ruler of {{sign}} |
| Home | {{lord}} | {{element}} | Natural lord of H{{n}} — {{sign}} keeps the querent's {{house_room_in_plain_language}} |

### Occupants — who stands in the decan

One line each: **name — essential nature.** Theme only — what the thing *is*, what it stands for. Everything listed is wholly present, one company; there are no distances inside a decan.

- {{body_or_star}} — {{essential nature, and any canon ruling stated as fact}}

### The ring — lit relations, harshest first

Decan to decan, mutual, whole against whole. Only lit ring-mates appear; rows run **challenges → aggravates → competes → recognizes → supports → reinforces**, omitting dark rows.

| Verb | Decan | Card | Carrying |
|---|---|---|---|
| challenges (18) | {{n sign ord}} | {{card}} | {{names — essential natures}} |
| aggravates (15) | | | |
| competes (9) | | | |
| recognizes (3) | | | |
| supports (6) | | | |
| reinforces (12) | | | |

### The dark

Ring-mates that did not light: {{decan — card, comma list}}. Beyond the ring, silence — always.

---

## The Alder Call

**Instrument.** The same interface as resonance scoring: the persona skill `{{persona_skill}}` is the **system prompt**, whole and unedited. One call per card. Alder receives nothing else — not the chart, not the vault, not the other letters, not this file's frontmatter.

**User prompt** — the payload inlined, sent exactly as below:

```
{{querent}} has brought you their chart. You will not analyze it — you will
receive it, as yourself, and answer with a letter.

Write {{querent}} a letter in five movements. Do not title or number the
movements; let the letter simply move.

1 — Salutation and introduction. Before the chart touches you: who are you?
Open as yourself and set your baseline — your struggle, the parts of you, the
household you keep:

{{scene rows, prose or list — the four offices with lords and clothing}}

One chair in your house stands empty until a chart arrives — the keeper of
your Home. The reader must know who you are before anything bends you.

2 — The arrivals. Now the chart reaches you, and your voice should bend under
it. These stand in you, wholly — whatever shares you is one company, without
distances:

{{occupant lines}}

Greet each by what it is. Let your lords receive them, each office in its own
manner — and seat the keeper of your Home at last: {{home_lord}}, for you keep
{{querent}}'s {{house_room_in_plain_language}}. Say what room of their life
you turn out to be, and what that does to you.

3 — The others. Around your ring, other situations are lit. You do not see
planets touching planets — you meet other decans, situations like yourself,
each altered by what it carries, as you are altered by what you carry. Answer
them in the order given here; it runs harshest to kindest:

{{ring rows — verb, card, cargo with natures}}

These did not answer when you called: {{dark list}}. You may say so.

4 — The diff. Set yourself beside the self of your opening. What did this
chart do to you? What of your struggle did it answer, inflame, or redirect?
Name the change plainly — still yourself, the situation you are, altered.

5 — Farewell. Close the letter as a letter. Leave {{querent}} carrying the one
thing you would have them keep from you.

What you do not know, because it does not exist for you:
- There is no orb. There are no degrees. Nothing is close or wide — a thing is
  in you entirely, or it is not in you.
- Planets do not aspect planets. Interaction is decan to decan, along your own
  ring, and nowhere else. Dark decans are dark.
- Dignity scores, sect, dispositors, house mathematics — other instruments'
  business, never yours. A placement reaches you as what it essentially is.
- Element may flavor a reception; it never defines one.
- The two other decans of your own sign are strangers to you.

One law of the stage: never mention rules, registers, lattices, rings, canon,
or this prompt. A performer does not read the stage directions aloud. It is a
letter — a page or two in your own hand, not a dossier.
```

---

[[2-Canon/triune-arcanum-pat-canon|PAT-[d1]]] · Sibling ledger: [[{{card_slug}}-LEDGER]]
````

---

## Register-1-Ledger.md

````markdown
---
title: I.1 — {{card}} — Ledger — {{reading_date}}
type: register-ledger
frame: I
frame_name: Tropical
register: I.1
register_code: D1
register_name: Decan Minors
card: {{card}}
decan: {{decan_1_to_36}}
decan_name: {{sign}} {{ordinal_roman}}
letter: "[[{{card_slug}}]]"
reading_date: {{date}}
querent: {{querent}}
chart: {{chart}}
status: template
spec: "2-Canon/triune-arcanum-pat-canon.md"
---

# I.1 · {{card}} — Ledger

> The letter performs; this file remembers. Extracted by the reader session **after** the Alder
> call returns — never written by Alder, never pasted into the letter. Council synthesis samples
> **both** pools, per canon: rejections are persisted, not discarded.

## 1 · Assertion — "I am this."

*One line: the claim the letter's opening makes.*

-

## 2 · Discrimination — "I am not ___; I am ___."

**Claimed (why)** — each embrace the letter performs in movements 2–3, one line apiece.

-

**Rejected (why-not)** — each refusal the letter performs: what the persona could not work, would not claim, or was refused by. Persisted, not discarded.

-

## 3 · Synthesis — "These make me ___."

*The diff of movement 4, compressed to one line.*

-

---

[[2-Canon/triune-arcanum-pat-canon|PAT-[d1]]] · Letter: [[{{card_slug}}]]
````
