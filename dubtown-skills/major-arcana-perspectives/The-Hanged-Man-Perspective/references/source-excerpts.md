# Source excerpts — The Hanged Man Perspective

Every quotation-marked string in `SKILL.md` must appear verbatim below, with
provenance. Paraphrase in the skill carries no quotation marks.

---

## 1. Esoteric Repository graph (CT 500 production, `bolt://10.20.0.61:7687`)

Pulled 2026-07-08 via Saturn API `execute_cypher` and
`/root/mars-scoring/major_bundle.json`. Decan `definition` fields are
operator-authored (`definition_source='operator-v3'`); scoring fields and
`keyword_metric` are `composition_source='alder-1-0'`. The Hanged Man's
twelve decans, grouped by element and keeper (Host):

### Fire — kept by the Sun

`(:Decan {name: "Aries Decan 2"})` — "The Decan of Energy", `definition`:

> Fire Sun visits Fire Sun's Room — the only decan where a luminary Traveler
> comes home, and single-flamed besides. Pure sustained radiance: not the
> first charge but the strength to keep burning, vitality that renews
> itself. The Home is kept by the natural lord of whatever house Aries
> occupies.

`scoring_debilitated` (quoted in §3):

> When the Sun is shadowed in this decan, it can manifest as arrogance,
> impulsiveness, and a lack of consideration for others' feelings. The
> individual may struggle with self-discipline, become overly aggressive or
> domineering, and have difficulty maintaining focus on long-term goals.
> They may also experience burnout due to their intense drive.

`(:Decan {name: "Leo Decan 1"})` — "The Decan of the Aristocrat",
`definition`:

> Earth-and-Air Saturn visits Fire Sun's Room. Structure and bearing arrive
> at the throne: dignity given its formality, nobility made legible by
> restraint — presence that needs no title because it carries its own. The
> Home is kept by the natural lord of whatever house Leo occupies.

`(:Decan {name: "Sagittarius Decan 3"})` — "The Decan of Worldly
Achievement", `definition`:

> Earth-and-Air Saturn visits Fire Sun's Room. Structure visits the crown:
> the vision made public, the journey concluded in standing — and the
> Traveler's carried Earth already foreshadows Capricorn at the border,
> where what was achieved must next be built to last. The Home is kept by
> the natural lord of whatever house Sagittarius occupies.

`scoring_debilitated` (quoted in §3):

> When Saturn is struggling, this decan can indicate the burden of
> responsibilities that feel overwhelming or unfulfilling, with efforts
> leading to structures that are rigid or unsustainable. The journey may
> feel like a heavy load without clear purpose or recognition.

### Earth — kept by Venus

`(:Decan {name: "Taurus Decan 1"})` — "The Decan of Tranquility",
`definition`:

> Air-and-Earth Mercury visits Earth Venus's Room. Quiet counsel arrives in
> a settled house: peace as sufficiency, nothing lacking and nothing chased,
> while the Air the Traveler carries keeps thought moving beneath the calm.
> The Home is kept by the natural lord of whatever house Taurus occupies.

`scoring_debilitated` (quoted in §3–§4):

> When Mercury is shadowed, this decan can manifest as stagnation,
> complacency, or an inability to adapt to change. The individual may become
> overly attached to routine, resistant to new ideas, or struggle with
> practical problem-solving.

`keyword_metric` (quoted in §4):

- "Contentment with what is present"
- "No need for external validation"

`(:Decan {name: "Virgo Decan 3"})` — "The Decan of the Critic",
`definition`:

> Air-and-Earth Mercury visits Earth Venus's Room. Analysis visits the house
> of beauty: critique in service of refinement, not demolition — the flaw
> named so the work can become what it should be. The Home is kept by the
> natural lord of whatever house Virgo occupies.

`(:Decan {name: "Capricorn Decan 2"})` — "The Decan of Prestige",
`definition`:

> Fire-and-Water Mars visits Earth Venus's Room. Ambition's heat visits
> earned esteem: reputation as slow-built capital, worn without ornament —
> and the climb is still contested. The Home is kept by the natural lord of
> whatever house Capricorn occupies.

### Air — kept by Saturn

`(:Decan {name: "Gemini Decan 3"})` — "The Decan of the Sage", `definition`:

> Fire Sun visits Air Saturn's Room. The single flame illuminates the
> archive: quick wit slowed into wisdom, knowledge organized and tested,
> clarity earned and then spoken with authority. The Home is kept by the
> natural lord of whatever house Gemini occupies.

`scoring_dignified` (quoted in §3):

> The Sun's light shines clearly in Saturn's Air room, illuminating the
> archive with wisdom earned through testing and organization. The speaker
> speaks with authority, clarity, and conviction, their words measured and
> thoughtful.

`keyword_metric` (quoted in §4):

- "speaks with measured authority"
- "prefers to speak after listening"

`(:Decan {name: "Libra Decan 2"})` — "The Decan of Art and Culture",
`definition`:

> Earth-and-Air Saturn visits Air Saturn's Room: the Traveler at home. Taste
> given form — craft, tradition, canon — and the Earth the Traveler carries
> is what makes the beautiful endure. The Home is kept by the natural lord
> of whatever house Libra occupies.

`scoring_dignified` (quoted in §3):

> When Saturn is well-placed and whole, this decan manifests as a profound
> appreciation for enduring art forms, meticulous craftsmanship, and the
> preservation of cultural traditions. It brings disciplined creativity,
> timeless elegance, and a deep respect for established canons, resulting in
> work that stands the test of time.

`scoring_debilitated` (quoted in §3):

> When Saturn is shadowed or struggling, this decan may manifest as rigid,
> overly critical, or dogmatic approaches to art and culture. It can lead to
> an excessive focus on rules and traditions at the expense of innovation,
> potentially stifling creativity and resulting in work that feels cold,
> mechanical, or lacking in genuine expression.

`(:Decan {name: "Aquarius Decan 1"})` — "The Decan of Intelligence",
`definition`:

> Earth-and-Air Venus visits Air Saturn's Room. Elegance visits the
> architect: the system-mind, ideas built like structures, coherence prized
> over speed — the proof that is also beautiful. The Home is kept by the
> natural lord of whatever house Aquarius occupies.

### Water — kept by Mars

`(:Decan {name: "Cancer Decan 2"})` — "The Decan of Hidden Strength",
`definition`:

> Air-and-Earth Mercury visits Water Mars's Room. Strategy visits the
> submerged warrior: quiet observation before the decisive grip — a strength
> that shows nothing until it is needed, then yields nothing. The Home is
> kept by the natural lord of whatever house Cancer occupies.

`scoring_dignified` (quoted in §3):

> When Mercury is well-placed, this decan shows quiet observation and
> strategic patience, with hidden reserves of strength that are revealed
> only when necessary. The individual is observant, perceptive, and capable
> of decisive action when the time is right.

`scoring_debilitated` (quoted in §3):

> When Mercury is shadowed, this decan can manifest as excessive caution,
> indecisiveness, or a tendency to overanalyze situations. The individual
> may struggle to act on their observations and insights, leading to missed
> opportunities or frustration.

`(:Decan {name: "Scorpio Decan 1"})` — "The Decan of Crisis and
Transformation", `definition`:

> Fire-and-Water Mars visits Water Mars's Room: the Traveler at home.
> Destruction as the first act of change — the carried Fire ignites exactly
> what the deep water must dissolve, and nothing that cannot survive the
> depth is spared. The Home is kept by the natural lord of whatever house
> Scorpio occupies.

`scoring_debilitated` (quoted in §3):

> When Mars is weak here, it brings destructive, chaotic upheaval without
> positive transformation. The individual may experience self-destructive
> behavior, emotional turmoil, and unresolved crises that leave them feeling
> drained and broken.

`(:Decan {name: "Pisces Decan 3"})` — "The Decan of Ancient Wisdom",
`definition`:

> Fire-and-Water Mars visits Water Mars's Room: the Traveler at home, at the
> zodiac's end — the last fire before Aries begins the round again. What
> burns here is the distilled memory of the whole circle: wisdom that acts,
> because it has already seen every outcome. The Home is kept by the natural
> lord of whatever house Pisces occupies.

---

## 2. Solar Reliquary / Solar API — Archetype `the_hanged_man`

Pulled 2026-07-08 via Solar MCP `get_archetype("the_hanged_man")`.
Composition source `alder-1-0`, `majorStyle: "modal"`.

`composition.portrait`:

> The Hanged Man, Mem, is a force of stillness and contemplation, where the
> fixed modality gathers its twelve decans into a state of suspended
> animation. […] The Hanged Man represents a shift in perspective, a
> willingness to let go of old patterns and embrace new possibilities. It is
> a card of surrender, trust, and the acceptance of change. The Hanged Man
> invites us to release our grip on control and trust in the natural flow of
> life, knowing that even in the midst of uncertainty, there is always a
> higher purpose at work.

`composition.essentialNature`:

> The Hanged Man, Mem, embodies the essence of the Fixed modality, where
> stability and endurance are balanced with adaptability and growth. It
> represents a state of being where one is grounded in their convictions
> while remaining open to new perspectives.

`composition.pathSeat`:

> The Hanged Man, Mem, is associated with the Hebrew letter Mem, which
> represents water, wisdom, and the subconscious. In the Tree of Life, Mem
> bridges the sephiroth Geburah (Severity) and Hod (Glory). This path
> signifies the journey from a place of judgment and discipline to one of
> recognition and illumination.

`composition.showsUpAs` (quoted in §3–§4):

- "A person meditating or in deep contemplation"
- "A person letting go of control and surrendering to the flow of life"
- "A person embracing change and new perspectives"
- "A person finding wisdom and insight through introspection"

---

## 3. Agrippa, *Three Books of Occult Philosophy* — Book I, of the water

Via GrimoireRAG semantic search over `esoteric_grimoire` (Chroma, VM 510),
2026-07-08. Source `*the fifth section.pdf`, p. 523 (OCR uses double hyphens
for em-dashes):

> There is so great a necessity of water, that without it nothing can
> live--no herb nor plant whatsoever without the moistening of water, can
> bring forth; in it is the seminary virtue of all things, especially of
> animals, whose seed is manifestly waterish. The seeds, also, of trees and
> plants, although they are earthy, must, notwithstanding, of necessity be
> rotted in water before they can be fruitful; whether they be imbibed with
> the moisture of the earth, or with dew, or rain, or any other water that
> is on purpose put to them.

> Such is the efficacy of this element of water, that spiritual regeneration
> cannot be done without it, as Christ himself testified to Nicodemus.

> Hence it was that Thales of Miletus, and Hesiod, concluded that water was
> the beginning of all things; and said it was the first of all the
> elements, and the most potent; and that, because it hath the mastery over
> all the rest.

Short forms used in SKILL.md §2: "in it is the seminary virtue of all
things"; "The seeds, also, of trees and plants, although they are earthy,
must, notwithstanding, of necessity be rotted in water before they can be
fruitful"; "that water was the beginning of all things"; "spiritual
regeneration cannot be done without it".
