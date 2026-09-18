# Source excerpts — Wheel of Fortune Perspective

Every quotation-marked string in `SKILL.md` must appear verbatim below, with
provenance. Paraphrase in the skill carries no quotation marks.

---

## 1. The 78 major bundle (`/root/mars-scoring/major_bundle.json`)

Entry `major == "Wheel of Fortune"` (num 10, style planetary, planet Jupiter,
kind wanderer, letter Kaph, path Chesed→Netzach). The per-decan `essence`
fields are operator-authored canonical prose; identical essences live on the
Decan nodes in the Esoteric Repository graph.

### Aries Decan 3 — "The Decan of Idealism", traveler Venus

`essence`:

> Earth-and-Air Venus visits Fire Jupiter's Room. The Traveler brings form
> and idea to the crusader's hearth: the ideal is fought for because it is
> loved, and loved because it can be built. The Home is kept by the natural
> lord of whatever house Aries occupies.

### Cancer Decan 3 — "The Decan of Moral Courage", traveler Moon

`essence`:

> Water Moon visits Water Jupiter's Room — the Traveler among kin, though
> never at home. Private care enlarged into public principle: the defense of
> one's own becomes the defense of what is right, and the courage stays
> rooted in feeling rather than doctrine. The Home is kept by the natural
> lord of whatever house Cancer occupies.

### Leo Decan 2 — "The Decan of Morale", traveler Jupiter

`essence`:

> Fire-and-Water Jupiter visits Fire Jupiter's Room: the Traveler at home.
> Generosity as a mode of leadership — where this decan stands, the room
> believes again — and the Water the Traveler carries makes the abundance
> felt, not merely displayed. The Home is kept by the natural lord of
> whatever house Leo occupies.

### Scorpio Decan 2 — "The Decan of the Hypnotic Personality", traveler Sun

`essence`:

> Fire Sun visits Water Jupiter's Room. The single flame beneath dark water:
> magnetism at a scale others cannot look away from — light rising from the
> depths without ever fully surfacing. The Home is kept by the natural lord
> of whatever house Scorpio occupies.

### Sagittarius Decan 1 — "The Decan of the Scholar", traveler Mercury

`essence`:

> Air-and-Earth Mercury visits Fire Jupiter's Room. The student's tools
> arrive at the philosopher's hearth: language, notation, the question
> well-formed before the quest departs — wisdom pursued at full scale. The
> Home is kept by the natural lord of whatever house Sagittarius occupies.

### Pisces Decan 1 — "The Decan of Self", traveler Saturn

`essence`:

> Earth-and-Air Saturn visits Water Jupiter's Room. The boundary visits the
> boundless: identity found by dissolving into the whole — and the Traveler
> carries in the one edge that lets a self exist at all. The Home is kept by
> the natural lord of whatever house Pisces occupies.

---

## 2. Esoteric Repository graph (CT 500 production, `bolt://10.20.0.61:7687`)

Pulled 2026-07-08 via Saturn API `execute_cypher` — `keyword_metric`,
`scoring_dignified`, `scoring_debilitated`, `scoring_dignity_keys` for the
six member decans.

### `(:Decan {name: "Aries Decan 3"})`

`scoring_dignified`:

> When Venus is well-placed in this decan, the individual is a passionate and
> idealistic visionary who pursues their dreams with conviction. They are
> able to effectively combine form and idea, building tangible manifestations
> of their ideals.

`scoring_debilitated`:

> When Venus is shadowed in this decan, the individual may struggle to
> balance their idealism with practicality. Their passion for their cause may
> lead to conflicts or difficulties in achieving their goals.

`keyword_metric` (selected, quoted in §4):

- "Practical idealist"

### `(:Decan {name: "Cancer Decan 3"})`

`scoring_dignified`:

> When well-placed, this decan manifests as strong moral courage, unwavering
> integrity, and a deep sense of justice. The individual is able to stand up
> for what they believe in, defend the rights of others, and act with
> conviction based on their personal values and ethics.

`scoring_debilitated`:

> When shadowed, this decan can lead to moral confusion, indecisiveness, and
> a lack of courage. The individual may struggle to take a stand for what is
> right, feel overwhelmed by the responsibility of defending others, or
> compromise their principles in the face of adversity.

`keyword_metric` (selected, quoted in §4):

- "Defending others' rights as if they were one's own"

### `(:Decan {name: "Leo Decan 2"})`

`scoring_dignified`:

> When Jupiter is well-placed, this decan radiates confidence and optimism.
> The individual naturally inspires others through their generosity and
> leadership, creating a ripple effect of positivity and belief in their
> abilities. They have an innate talent for turning challenges into
> opportunities and making others feel valued and supported.

`scoring_debilitated`:

> When Jupiter is shadowed, this decan can manifest as overconfidence or
> arrogance. The individual may struggle to inspire others effectively, and
> their attempts at leadership through generosity may come across as
> insincere or self-serving. They might find it difficult to maintain morale
> in challenging situations, leading to a lack of belief in themselves and
> others.

`keyword_metric` (selected, quoted in §4):

- "Generous gestures that create a sense of shared success"
- "Willingness to share resources and knowledge freely"

### `(:Decan {name: "Scorpio Decan 2"})`

`scoring_dignified`:

> When the Sun is well-placed, this decan radiates a powerful, magnetic
> presence that draws others in. The individual exudes confidence and
> charisma, captivating those around them with their hypnotic intensity and
> compelling aura.

`scoring_debilitated`:

> When the Sun is struggling, this decan can manifest as manipulative or
> controlling behavior. The individual may use their magnetic charm to
> manipulate others, becoming overly intense or obsessive in their
> interactions.

### `(:Decan {name: "Sagittarius Decan 1"})`

`scoring_dignified`:

> When Mercury is well-placed, this decan shows a sharp, inquisitive mind
> that can effectively research, analyze, and communicate complex ideas. The
> student's tools are finely honed, allowing them to ask insightful
> questions, organize information logically, and articulate their thoughts
> clearly as they pursue wisdom.

`scoring_debilitated`:

> When Mercury is struggling, this decan may manifest as scattered thinking,
> difficulty focusing on research, or unclear communication. The student's
> tools may be poorly maintained, leading to confusion, misinterpretation of
> information, or an inability to effectively pursue knowledge and
> understanding.

`keyword_metric` (selected, quoted in §4):

- "Asking precise questions before embarking on a journey"
- "Breaking down big ideas into manageable parts"

### `(:Decan {name: "Pisces Decan 1"})`

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

---

## 3. Solar Reliquary / Solar API — Archetype `wheel_of_fortune`

Pulled 2026-07-08 via Solar MCP `get_archetype("wheel_of_fortune")`.
Composition source `alder-1-0`, `majorStyle: "planetary"`. The
`decanSynthesis` field is additive and was NOT used for identity.

`composition.essentialNature`:

> As the planet Jupiter, the Wheel of Fortune card represents the ultimate
> expression of growth, wisdom, and abundance. It is the source from which
> the traveler-character of Jupiter flows, carrying the essence of expansion
> and transformation wherever it goes.

`composition.portrait`:

> The Wheel of Fortune, as Jupiter, is the cosmic wanderer who brings the
> grandest visions and the most expansive wisdom to the human experience.
> […] Jupiter's influence is felt in its ability to inspire, uplift, and
> guide us towards our highest potential.

`composition.pathSeat`:

> The Wheel of Fortune card is associated with the Hebrew letter Kaph, which
> represents the power to shape and mold reality. This letter bridges the
> sephiroth Chesed (Mercy) and Netzach (Eternity), symbolizing the balance
> between compassion and endurance in the face of life's challenges. The
> path from Chesed to Netzach represents the journey of growth and
> transformation that Jupiter guides us through, as we learn to navigate the
> ever-changing landscape of life with wisdom, grace, and resilience.

---

## 4. Classical texture

GrimoireRAG queries for Jupiter material (Agrippa) returned only adjacent
noise (Thursday considerations, talismanic chapters); no classical passage
is quoted in this skill. Texture comes from the graph and Solar composition
only.
