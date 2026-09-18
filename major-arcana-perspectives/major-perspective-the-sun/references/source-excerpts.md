# Source excerpts — The Sun Perspective

Every quotation-marked string in `SKILL.md` must appear verbatim below, with
provenance. Paraphrase in the skill carries no quotation marks.

---

## 1. Esoteric Repository graph (CT 500 production, `bolt://10.20.0.61:7687`)

Pulled 2026-07-05 via Saturn API `execute_cypher`. Decan `definition` fields
are operator-authored (`definition_source='operator-v3'`); scoring fields are
`composition_source='alder-1-0'`.

### `(:Decan {name: "Aries Decan 2"})` — epithet "The Decan of Energy", traveler Sun

`definition`:

> Fire Sun visits Fire Sun's Room — the only decan where a luminary Traveler
> comes home, and single-flamed besides. Pure sustained radiance: not the
> first charge but the strength to keep burning, vitality that renews itself.
> The Home is kept by the natural lord of whatever house Aries occupies.

`scoring_dignified`:

> When the Sun is well-placed in this decan, it radiates confidence,
> leadership, and a strong sense of purpose. The individual exudes vitality,
> takes initiative, and inspires others with their passion and determination.
> They are self-reliant, courageous, and able to overcome obstacles with ease.

`scoring_debilitated`:

> When the Sun is shadowed in this decan, it can manifest as arrogance,
> impulsiveness, and a lack of consideration for others' feelings. The
> individual may struggle with self-discipline, become overly aggressive or
> domineering, and have difficulty maintaining focus on long-term goals. They
> may also experience burnout due to their intense drive.

`keyword_metric` (selected, quoted in §4):

- "Unwavering focus on goals"
- "Radiates warmth and vitality"

### `(:Decan {name: "Leo Decan 1"})` — epithet "The Decan of the Aristocrat", traveler Saturn

`definition`:

> Earth-and-Air Saturn visits Fire Sun's Room. Structure and bearing arrive at
> the throne: dignity given its formality, nobility made legible by restraint
> — presence that needs no title because it carries its own. The Home is kept
> by the natural lord of whatever house Leo occupies.

`scoring_dignified`:

> When Saturn is well-placed in this decan, the individual embodies
> disciplined nobility. They command respect through their composed presence
> and methodical approach to life's challenges. Their formal bearing and
> attention to detail create a sense of authority that inspires confidence
> and stability.

`scoring_debilitated`:

> When Saturn is shadowed in this decan, the individual may struggle with
> self-doubt and rigidity. Their formal demeanor can become cold and aloof,
> making it difficult to connect authentically with others. They may feel
> burdened by expectations and find it challenging to express their true
> feelings or embrace spontaneity.

`keyword_metric` (selected, quoted in §4):

- "Uses formal language and precise diction"
- "Projects an aura of quiet authority and self-assurance"

### `(:Decan {name: "Sagittarius Decan 3"})` — epithet "The Decan of Worldly Achievement", traveler Saturn

`definition`:

> Earth-and-Air Saturn visits Fire Sun's Room. Structure visits the crown: the
> vision made public, the journey concluded in standing — and the Traveler's
> carried Earth already foreshadows Capricorn at the border, where what was
> achieved must next be built to last. The Home is kept by the natural lord of
> whatever house Sagittarius occupies.

`scoring_dignified`:

> When Saturn is well-placed, this decan represents the successful culmination
> of a long journey, where disciplined effort and practical application lead
> to tangible achievements that stand the test of time. The vision is realized
> in a structured, lasting form.

`scoring_debilitated`:

> When Saturn is struggling, this decan can indicate the burden of
> responsibilities that feel overwhelming or unfulfilling, with efforts
> leading to structures that are rigid or unsustainable. The journey may feel
> like a heavy load without clear purpose or recognition.

`keyword_metric` (selected, quoted in §4):

- "Establishing a legacy through perseverance"

---

## 2. Solar Reliquary / Solar API — Archetype `the_sun`

Pulled 2026-07-05 via Solar MCP `get_archetype("the_sun")`. Composition source
`alder-1-0`, `majorStyle: "planetary"`.

`composition.essentialNature`:

> As a luminary, the Sun is the source of all life and vitality on Earth. It
> radiates pure, sustained energy that renews itself, providing the strength
> to keep burning brightly. This celestial body embodies the essence of
> leadership, authority, and the beginning of new cycles. The Sun's influence
> permeates the decans under its rulership, infusing them with its fiery
> nature and transformative power.

`composition.pathSeat`:

> The Hebrew letter Resh represents the head or beginning, symbolizing
> leadership, authority, and the Sun's role as a guiding force. This path
> bridges the sephiroth of Hod (Splendor) and Yesod (Foundation), signifying
> the Sun's ability to illuminate the way and provide a solid foundation for
> growth and transformation.

`composition.portrait` (final clause quoted in §2):

> …guiding beings towards their true potential and purpose.

---

## 3. Agrippa, *Three Books of Occult Philosophy* — Book II ch. XXXII

Via GrimoireRAG semantic search over `esoteric_grimoire` (Chroma, VM 510),
2026-07-05. Two OCR variants of the same chapter were retrieved; quotes below
are from the cleaner variant (source `*the fifth section.pdf`, p. 591):

> The Sun giveth light to all things of itself, and gives it plentifully, not
> only to all things in heaven and air, but earth and deep. Whatever good we
> have, Jamblicus says, we have it from the Sun alone; or from it through
> other things. Heraclitus calls the Sun, the fountain of celestial light; and
> many of the Platonists placed the soul of the world chiefly in the Sun […]
> Hence the antient naturalists called the Sun the very heart of Heaven […]

Short forms used in SKILL.md §2: "the fountain of celestial light", "the very
heart of Heaven", "The Sun giveth light to all things of itself, and gives it
plentifully", "Whatever good we have, Jamblicus says, we have it from the Sun
alone; or from it through other things."

Also retrieved (not quoted in the skill, kept for reference — source `*The
Second 31.pdf`, p. 623, alternate OCR):

> …which therefore Orpheus cals the enlivening eyes of the heaven.

Note the skill's header paraphrases "the enlivening eyes of Heaven" — if
quoted directly in a future revision, prefer this variant's spelling with
provenance.
