# Majestic Arcana — MBTI Generator

Source: generator logic (Paul's canonical mechanic) **validated against** the live
`MajesticArcana` nodes. All 16 courts re-derived from the two binaries match the
stored `EMBODIES_TYPE` / `psych_mbti_type` exactly. This file documents the
generator; the stored type is a cache to cross-check, never the primary source.

## The generator (derive, do not look up)

A court/throne card's type is fixed by two orthogonal binaries:

1. **Dominant function = suit.** Wands → Intuition, Chalices → Feeling, Swords →
   Thinking, Pentacles → Sensing.
2. **Dominant attitude.** Extraverted (♂) → **Knight / King**; introverted (♀) →
   **Page / Queen**.
3. **Auxiliary function's element vs the suit element.** *Opposing* pair
   (Fire/Water, Air/Earth) → the youth/conflict ranks **Page / Knight**;
   *complementary* pair (Fire/Air, Water/Earth) → the experienced/harmony ranks
   **Queen / King**.

The 2×2 of (attitude) × (aux opposing/complementary) yields the four courts of a
suit uniquely.

> Note: this auxiliary-element relationship is **not** the same as the deck's
> `HAS_INNER_ELEMENT`/`HAS_OUTER_ELEMENT` (= suit element × rank element: Page=Earth,
> Knight=Air, Queen=Water, King=Fire — the traditional "X of Y" dignity). The
> generator runs on the *cognitive* aux-element; the inner/outer pair is a separate
> descriptive layer.

## Internal split

- **Thrones** — the 4 **Pages** (seasonal seat). See Sabbat caveat below.
- **Court** — **Knights, Queens, Kings** (12).
- **Aces** — the 4 pure cognitive-function pairs, the culmination above the throne.

## Courts (validated)

| Card | Suit | Rank | Dom function | Attitude | Aux (element) | Pair to suit | MBTI |
|---|---|---|---|---|---|---|---|
| Page of Wands | Wands | Page | Ni (Intuition) | ♀ int | Fe (Water) | opposing | INFJ |
| Knight of Wands | Wands | Knight | Ne | ♂ ext | Fi (Water) | opposing | ENFP |
| Queen of Wands | Wands | Queen | Ni | ♀ int | Te (Air) | complementary | INTJ |
| King of Wands | Wands | King | Ne | ♂ ext | Ti (Air) | complementary | ENTP |
| Page of Chalices | Chalices | Page | Fi (Feeling) | ♀ int | Ne (Fire) | opposing | INFP |
| Knight of Chalices | Chalices | Knight | Fe | ♂ ext | Ni (Fire) | opposing | ENFJ |
| Queen of Chalices | Chalices | Queen | Fi | ♀ int | Se (Earth) | complementary | ISFP |
| King of Chalices | Chalices | King | Fe | ♂ ext | Si (Earth) | complementary | ESFJ |
| Page of Swords | Swords | Page | Ti (Thinking) | ♀ int | Se (Earth) | opposing | ISTP |
| Knight of Swords | Swords | Knight | Te | ♂ ext | Si (Earth) | opposing | ESTJ |
| Queen of Swords | Swords | Queen | Ti | ♀ int | Ne (Fire) | complementary | INTP |
| King of Swords | Swords | King | Te | ♂ ext | Ni (Fire) | complementary | ENTJ |
| Page of Pentacles | Pentacles | Page | Si (Sensing) | ♀ int | Te (Air) | opposing | ISTJ |
| Knight of Pentacles | Pentacles | Knight | Se | ♂ ext | Ti (Air) | opposing | ESTP |
| Queen of Pentacles | Pentacles | Queen | Si | ♀ int | Fe (Water) | complementary | ISFJ |
| King of Pentacles | Pentacles | King | Se | ♂ ext | Fi (Water) | complementary | ESFP |

Every row's MBTI is both the generator output and the stored `EMBODIES_TYPE` value —
they agree on all 16.

## Aces (pure function pairs)

| Card | Function pair | Archetype |
|---|---|---|
| Ace of Wands | Intuition (Ni + Ne) | the Priestess |
| Ace of Chalices | Feeling (Fi + Fe) | the Healer |
| Ace of Swords | Thinking (Ti + Te) | the Seer |
| Ace of Pentacles | Sensing (Si + Se) | the Sentinel |

`Ace of X` carries `EMBODIES_TYPE → :Function`. (See data caveat 1.)

## Court signs (astrological layer)

Each K/Q/K court's **dominant sign** is the sign that anchors its **suit's element** —
the 0–20° majority of its two-sign (20°–20°) span. Modality by rank: **Queen =
cardinal, Knight = fixed, King = mutable**. (The out-of-element 20–30° minority sign,
the prior sign of the span, is the non-dominant half of the pair.)

| Suit (element) | Queen (cardinal) | Knight (fixed) | King (mutable) |
|---|---|---|---|
| Wands (Fire) | Aries | Leo | Sagittarius |
| Chalices (Water) | Cancer | Scorpio | Pisces |
| Swords (Air) | Libra | Aquarius | Gemini |
| Pentacles (Earth) | Capricorn | Taurus | Virgo |

Pages are the seasonal thrones — they anchor the element as a whole, not a single
sign. These dominant signs feed the 7×11 court layer (each court → its dominant
sign's domicile ruler).

## Data caveats (verify / reconcile before relying on these)

1. **28 nodes, not 20.** Each suit has three Ace-type nodes: `Ace of X`, `Source of
   X`, `Mastery of X`. Only `Ace of X` has the `EMBODIES_TYPE` edge; the other two
   carry the type only as a string. Resolve Aces by the `Ace of X` node. Confirm
   whether Source/Mastery are the throne-culmination poles or legacy.
2. **Court sign data is mispointed in the repo (real bug — PAT-590).** The correct
   dominant sign is the in-element sign of the table above. The court nodes'
   `RULES_SIGN` correctly store both signs of each span, but
   `DOMINANT_ASTROLOGICAL_ASSOCIATION` and `astro_zodiac_sign` point to the wrong
   member — the 20–30° minority sign in the *prior, out-of-element* sign. Use the
   Court-signs table above, not those fields, until PAT-590 is fixed.
3. **Seasonal layer (confirmed correct, not a discrepancy).** The Sabbats on the
   Majestic cards are a real, intentional layer, distinct from both the cognitive
   generator and the inner/outer elements. The **Page is the seasonal throne**,
   seated at the cross-quarter festival at its season's *height* (Wands = Lammas,
   Chalices = Samhain, Pentacles = Beltane, Swords = Candlemas). **Queens and Kings
   hold the solstices and equinoxes.** (Knights and Aces share their suit's
   cross-quarter day in the data; the *throne* designation is the Page's.)

## Edges (for live resolution)

`EMBODIES_TYPE` → `:MBTIType` (courts) or `:Function` (aces); `PRIMARY_FUNCTION` /
`AUXILIARY` / `TERTIARY` / `INFERIOR` → `:CognitiveFunction`; `HAS_INNER_ELEMENT` /
`HAS_OUTER_ELEMENT` → `:Element`; `CELEBRATES_SABBAT` → `:Sabbat`.
