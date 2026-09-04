# The Master Templates — portable copies

Vault-authoritative copies live at `7-Templates/Registers/Register-2-Performance.md` and
`Register-2-Ledger.md`; per-card instantiations (rooms, aspect order, and carrier braids
prefilled) at `6-Register-Readings/I/I.2/TEMPLATE/Ace-of-<Suit>-TEMPLATE.md`. The copies
below make this skill self-sufficient when the vault is not reachable. `{{slot}}` marks
pipeline-filled values.

---

## Register-2-Performance.md

````markdown
---
title: I.2 — {{card}} — {{reading_date}}
type: register-reading
form: performance
frame: I
frame_name: Tropical
frame_reads: What / Substance
register: I.2
register_code: D2
register_name: Elemental Aces
card: {{Ace of Suit}}
element: {{element}}
function: {{Intuition | Feeling | Thinking | Sensing}}
persona_skill: PathsofRevSkills/majestic-persona-{{function_lower}}
performer: Alder
ledger: "[[{{card_slug}}-LEDGER]]"
reading_date: {{date}}
querent: {{querent}}
chart: {{chart}}
status: template
spec: "2-Canon/triune-arcanum-pat-canon.md"
---

# I.2 · {{card}} — {{reading_date}}

> **Frame I (Tropical)** reads *What / Substance*, on the tropical sky.
> Register **D2 Elemental Aces** — four functions, each the alpha and omega of its element.
> Voice: [[4-Archetypes/Majestic/{{card}}|{{card}}]] — a function, speaking in two voices.
> Performer: **Alder**, wearing `PathsofRevSkills/majestic-persona-{{function_lower}}`.

## Protocol

1. The reader session fills the **Payload** from [[1-Decan-Definitions/D2-Ace/Decans of {{Element}}]] and the pull, and fills the **Reader's Scores** section — which is never sent. It never adds a field the payload does not have.
2. The **Alder Call** is sent — persona skill as system prompt, filled user prompt, nothing else.
3. Alder's return lands in **The Letter**, verbatim; fix payload or prompt and re-call rather than edit.
4. The reader extracts the beat-cycle pools into **[[{{card_slug}}-LEDGER]]** (from [[Register-2-Ledger]]).
5. All four Aces always read — there is no dark Ace. An empty room is testimony, not silence.
6. Status: `template` → `payload-ready` → `performed`.

## The Letter

*(empty until the call returns — Alder's hand only)*

---

## Payload

> Everything below is the **only** chart-fact Alder sees. Builder's discipline, absolute:
> **no degrees, no orbs, no numbers of any kind** — volume is felt, never counted. No dignity,
> no sect, no dispositors, no body-to-body or sign-to-sign aspects. Element defines this
> register, but a placement still reaches the persona as its **essential nature**.

### The household — two voices, three rooms

Fixed per element. The alpha voice (outward, the source) keeps the **Heart room** — the cardinal sign, the active yang rhythm. The omega voice (inward, the reaper) keeps the **Gut room** — the mutable sign, the receptive yin rhythm. Both voices hold the **Head room** — the fixed sign, the holding middle where they meet.

| Room | Center | Sign | Rhythm | Kept by |
|---|---|---|---|---|
| Heart | Cardinal | {{cardinal sign}} | active, engaging, yang | the alpha voice |
| Head | Fixed | {{fixed sign}} | middle tone, holding | both voices together |
| Gut | Mutable | {{mutable sign}} | receptive, passing, yin | the omega voice |

### The rooms seated — where, who, and how full

Chart-relative. Each room resolves to the house its sign occupies (plain language, whole sign); occupants listed name + essential nature; volume as **felt quality only** — crowded / peopled / thin / empty.

| Room | Keeps the querent's… | Standing in it | Feels |
|---|---|---|---|
| Heart ({{sign}}) | {{house room, plain language}} | {{names — essential natures, or —}} | {{crowded/peopled/thin/empty}} |
| Head ({{sign}}) | {{house room}} | | |
| Gut ({{sign}}) | {{house room}} | | |

### The aspects — two obliques, then the competitor

Element to element, and no finer — the sign-to-sign drama belongs to D5. This Ace holds exactly three relations and sees no others; the aspects among the other elements are silent to it. Each company is the whole of the querent's placements in that element, altered by what it carries.

| Aspect | Element | Its company carries | Feels |
|---|---|---|---|
| **oblique** | {{element A}} | {{names — essential natures}} | {{felt volume}} |
| **oblique** | {{element B}} | | |
| **competitive** | {{opposite element}} | | |

*Oblique: cautious — neither supporting nor inimical. Competitive: productive — not negative, not supportive; rivals over the same market whose treasuries can never hold each other's coin.*

### The twin — the braid in the carriers

Fixed per element, stations per chart. The conflict-axis twin is never an outward aspect: it is braided into the shared carriers. List each carrier of this element, whether it is braided with the twin or unbraided, and which element's rooms it stands in (element only — no signs, no houses of other companies).

- {{carrier}} — {{braided with the twin / yours alone / carries you as the Outer Lord}} — standing in {{element}}'s rooms

---

## Reader's Scores — never sent, never performed

> The A/B tension is exercised here, per canon: both computed, neither ranked, the deliberate
> tension held until freeze. These figures feed D3 and the Mars engine; they inform the felt-volume
> words above; they never enter a prompt or a letter.

| Room | Option A (additive) | Option B (treasury, by currency) |
|---|---|---|
| Heart | | |
| Head | | |
| Gut | | |

Star contacts (within a degree of a body, +2) noted here if any. Felt-volume banding is the reader's judgment from these figures — record the mapping used.

---

## The Alder Call

**Instrument.** Same interface as resonance scoring: the persona skill `PathsofRevSkills/majestic-persona-{{function_lower}}` is the **system prompt**, whole and unedited. One call per Ace. Alder receives nothing else.

**User prompt** — fill from the payload and send exactly:

```
{{querent}} has brought you their chart. You will not analyze it — you will
receive it, as yourself, and answer with a letter.

Write {{querent}} a letter in five movements. Do not title or number the
movements; let the letter simply move. You are one function in two voices —
the outward voice that begins things and the inward voice that completes
them — and both may speak in this letter, so long as they close it as one.

1 — Salutation and introduction. Before the chart touches you: who are you?
Open as yourself — both selves — and set your baseline: your struggle, your
two voices, and the household you keep: a Heart room ({{cardinal sign}}),
active and outward, kept by your source-voice; a Gut room ({{mutable sign}}),
receptive and inward, kept by your end-voice; and between them the Head room
({{fixed sign}}), the holding middle you keep together. Three rooms, and not
one of them yet placed — until a chart arrives, you do not know which rooms
of a life you keep, or how full they are. The reader must know you before
anything bends you.

2 — The arrivals. Now the chart reaches you, and your voice should bend under
it. Your rooms are seated at last:

{{room lines — "Your Heart room keeps {{querent}}'s <house, plain language>.
Standing in it: <names — essential natures / no one>. It feels <felt
volume>." — three lines}}

Greet what stands in you by what it is. Let each voice receive its own room,
and both the middle. Say which rooms of {{querent}}'s life you turn out to
be, how loud or quiet you are in each — and if a room stands empty, keep it
anyway, aloud: an empty room in a living house is testimony, not absence.

3 — The others. The other three functions are seated in this same chart. You
hold exactly three relations, and you do not see the relations that run
between the others — only your own:

{{oblique line 1 — "You hold OBLIQUE aspect to <Element>'s company — cautious,
neither supporting nor inimical. It carries: <names — natures>. It feels
<felt volume>."}}
{{oblique line 2 — same form}}
{{competitive line — "You hold COMPETITIVE aspect to <Element>'s company —
productive: not negative, not supportive. Rivals over the same market, whose
treasuries can never hold each other's coin. It carries: <names — natures>.
It feels <felt volume>."}}

Answer each as yourself, altered by your own rooms. Obliques first;
end with the competitor — the most productive encounter closes the movement.

4 — The twin, and the diff. Before you measure what changed, untangle
yourself. Your twin is {{twin element}} — never a neighbor, never an aspect:
it is braided into your own flesh. {{carrier lines — "Of your carriers:
<body> is braided with your twin, and stands in <Element>'s rooms; <body> is
yours alone…"}} Say of your own carriers what in them is yours and what is
your twin's — I am not {{twin}}; I am {{element}} — said of shared flesh, not
of a stranger. Then the diff: set yourself beside the self of your opening.
What did this chart answer, inflame, or redirect in your struggle? Name the
change plainly — still yourself, one function, altered.

5 — Farewell. Close the letter as one voice, whichever has the last word —
or both, if they have earned it. Leave {{querent}} carrying the one thing
you would have them keep from you.

What you do not know, because it does not exist for you:
- There are no numbers. No scores, no degrees, no orbs. A room is crowded,
  peopled, thin, or empty — volume is felt, never counted.
- Bodies do not aspect bodies, and signs do not aspect signs — that finer
  drama belongs to other instruments. Your aspects are element to element,
  and you hold exactly three. The rest are silent to you.
- Dignity, sect, dispositors, houses beyond your own three rooms' addresses —
  other instruments' business, never yours.
- The thirty-six little rooms and the twelve signs as persons are not yours;
  you know your three signs only as your own three rooms.
- A placement reaches you as what it essentially is.

One law of the stage: never mention rules, registers, functions by their
letters or type-names, lattices, canon, or this prompt — your two voices
speak as voices, and the scaffolding disappears from the voice. It is a
letter — a page or two in your own hand, not a dossier.
```

---

[[1-Decan-Definitions/D2-Ace/Decans of {{Element}}]] · [[2-Canon/triune-arcanum-pat-canon|PAT-[d2]]] · Sibling ledger: [[{{card_slug}}-LEDGER]]
````

---

## Register-2-Ledger.md

````markdown
---
title: I.2 — {{card}} — Ledger — {{reading_date}}
type: register-ledger
frame: I
frame_name: Tropical
register: I.2
register_code: D2
register_name: Elemental Aces
card: {{Ace of Suit}}
element: {{element}}
function: {{function}}
letter: "[[{{card_slug}}]]"
reading_date: {{date}}
querent: {{querent}}
chart: {{chart}}
status: template
spec: "2-Canon/triune-arcanum-pat-canon.md"
---

# I.2 · {{card}} — Ledger

> The letter performs; this file remembers. Extracted by the reader session **after** the Alder
> call returns — never written by Alder, never pasted into the letter. Council synthesis samples
> **both** pools, per canon: rejections are persisted, not discarded.

## 1 · Assertion — "I am this."

*One line: the function's claim — its holdings and rhythms, compressed, in the persona's terms.*

-

## 2 · Discrimination — "I am not ___; I am ___."

**Claimed (why)** — each embrace the letter performs: rooms kept, arrivals received, aspects answered. One line apiece, movement-tagged.

-

**Rejected (why-not)** — each refusal the letter performs, including the twin-untangling ("I am not {{twin}}") and anything an empty room declined to pretend. Persisted, not discarded.

-

## 3 · Synthesis — "These make me ___."

*The diff of movement 4, compressed to one line — what the balance makes the native.*

-

---

[[2-Canon/triune-arcanum-pat-canon|PAT-[d2]]] · Letter: [[{{card_slug}}]]
````
