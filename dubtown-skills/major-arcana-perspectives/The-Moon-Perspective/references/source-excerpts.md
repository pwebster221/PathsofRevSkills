# Source excerpts — The Moon Perspective

Every quotation-marked string in `SKILL.md` must appear verbatim below, with
provenance. Paraphrase in the skill carries no quotation marks.

---

## 1. Esoteric Repository graph (CT 500 production, `bolt://10.20.0.61:7687`)

Pulled 2026-07-08 via Saturn API `execute_cypher` and
`/root/mars-scoring/major_bundle.json`. Decan `definition` fields are
operator-authored (`definition_source='operator-v3'`); scoring fields are
`composition_source='alder-1-0'`.

### `(:Decan {name: "Pisces Decan 1"})` — epithet "The Decan of Self", traveler Saturn

`definition`:

> Earth-and-Air Saturn visits Water Jupiter's Room. The boundary visits the
> boundless: identity found by dissolving into the whole — and the Traveler
> carries in the one edge that lets a self exist at all. The Home is kept by
> the natural lord of whatever house Pisces occupies.

`scoring_dignified`:

> When Saturn is well-placed, the individual can find a sense of self within
> the collective, using their boundaries to navigate the world while still
> being open and adaptable. They may have a deep understanding of the
> interconnectedness of all things and use this wisdom to guide their
> actions.

`scoring_debilitated`:

> When Saturn is shadowed, the individual struggles with identity issues,
> feeling lost or disconnected from themselves. They may have difficulty
> setting boundaries, leading to confusion about where they end and others
> begin. This can result in a lack of direction and purpose in life.

`keyword_metric` (selected, quoted in §3–§4):

- "A tendency to lose oneself in others or in the collective"
- "A sense of being a chameleon, adapting to others rather than being oneself"
- "A sense of being adrift or without a clear identity"

### `(:Decan {name: "Pisces Decan 2"})` — epithet "The Decan of the Healer", traveler Jupiter

`definition`:

> Fire-and-Water Jupiter visits Water Moon's Room. Grace visits the tide:
> another's wound felt as one's own and tended accordingly — restoration
> beyond what skill alone explains, warmed by the Fire the Traveler carries.
> The Home is kept by the natural lord of whatever house Pisces occupies.

`scoring_dignified`:

> When Jupiter is strong in this decan, it manifests as profound healing
> ability where the individual can intuitively sense and address others'
> emotional wounds. Their compassionate presence becomes a source of genuine
> restoration, blending practical care with spiritual insight to help others
> find inner peace.

`scoring_debilitated`:

> When Jupiter struggles here, the healer's compassion may become
> overwhelming or self-indulgent, leading to emotional exhaustion from
> absorbing others' pain without proper boundaries. Healing efforts might
> feel forced or insincere, potentially causing more harm than good through
> misguided empathy.

`keyword_metric` (selected, quoted in §4):

- "Ability to sense when someone needs comfort without being asked"
- "Healing through shared vulnerability and trust"
- "Compassionate action that goes beyond intellectual analysis"

### `(:Decan {name: "Pisces Decan 3"})` — epithet "The Decan of Ancient Wisdom", traveler Mars

`definition`:

> Fire-and-Water Mars visits Water Mars's Room: the Traveler at home, at the
> zodiac's end — the last fire before Aries begins the round again. What
> burns here is the distilled memory of the whole circle: wisdom that acts,
> because it has already seen every outcome. The Home is kept by the natural
> lord of whatever house Pisces occupies.

`scoring_dignified`:

> When Mars is well-placed, this decan manifests as profound wisdom in
> action - intuitive insights that lead to decisive, purposeful outcomes.
> The individual acts from deep knowing, integrating past experiences into
> present decisions with clarity and resolve.

`scoring_debilitated`:

> When shadowed, this decan shows as confusion between intuition and impulse.
> The individual may act on half-formed ideas or struggle to translate inner
> wisdom into effective action, leading to frustration and scattered efforts.

`keyword_metric` (selected, quoted in §4):

- "speaks with ancient authority"
- "acts on deep intuition"
- "draws from collective memory"
- "operates from inner knowing"
- "moves with deliberate fluidity"

---

## 2. Solar Reliquary / Solar API — Archetype `the_moon`

Pulled 2026-07-08 via Solar MCP `get_archetype("the_moon")`. Composition
source `alder-1-0`, `majorStyle: "sign"`.

`composition.essentialNature`:

> As the pure whole sign of Pisces, The Moon is the embodiment of the mutable
> water element, ruled by Jupiter. It represents the fluidity and
> adaptability of the subconscious mind, where the boundaries between self
> and other, dream and reality, dissolve into a boundless ocean of potential.
> As the house lord of Pisces, it governs the realm of the unconscious,
> intuition, and spiritual connection, guiding the traveler through the
> depths of their own psyche.

`composition.pathSeat`:

> The Moon's structural seat on the Tree of Life is the Hebrew letter Qoph,
> which bridges the sephiroth of Netzach (Victory) and Malkuth (Kingdom).
> Qoph represents the back of the head, symbolizing the subconscious mind and
> the connection between the divine spark within (Netzach) and the earthly
> realm (Malkuth). This path signifies the journey of self-discovery and the
> integration of the conscious and unconscious aspects of the self.

---

## 3. Agrippa, *Three Books of Occult Philosophy* — water and Lunary texture

Via GrimoireRAG semantic search over `esoteric_grimoire` (Chroma, VM 510),
2026-07-08.

Book I, Chap. III, "Of the Water and Air" — source `*the fifth section.pdf`,
p. 523:

> THE other two elements, viz. water and air, are not less efficacious than
> the former; neither is Nature wanting to work wonderful things in them.
> There is so great a necessity of water, that without it nothing can
> live--no herb nor plant whatsoever without the moistening of water, can
> bring forth; in it is the seminary virtue of all things, especially of
> animals, whose seed is manifestly waterish. [...] Such is the efficacy of
> this element of water, that spiritual regeneration cannot be done without
> it, as Christ himself testified to Nicodemus.

Book I, Chap. XXIV, "What things are Lunary, or under the power of the
Moon" — source `*The Second 31.pdf`, p. 566:

> These things are Lunary, amongst the Elements, viz. the Earth, then the
> Water, as well that of the Sea, as of the Rivers, and all moist things, as
> the moisture of Trees, and Animals, especially they which are White, as the
> Whites of Eggs, fat, sweat, flegme [phlegm], and the superfluities of
> bodies.
