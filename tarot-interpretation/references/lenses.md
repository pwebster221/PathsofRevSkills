# Decomposition Lenses — Membership

Optional reading boards over the 78. The 4×19 and 7×11 are fixed; the 11×7 is
chart-derived. All three are complete.

---

## 4×19 — Elemental (complete)

Four elemental groups of nineteen: each = full suit (Ace + pips 2–10 + 4 courts = 14)
+ **5 Majors** (3 zodiacal of the element's signs, 1 elemental Major, 1 planetary
Major). **Sun (19)** and **High Priestess / Moon (2)** are held out as the two lights
framing the deck. 4×19 = 76, + Sun + Moon = 78.

Planetary-Major seats follow the planet→element rule (Mars/Fire, Jupiter/Water,
Mercury/Air, Venus/Earth) — this can differ from a card's intrinsic element (e.g.
Wheel of Fortune's node reads Earth, but it seats as Water's planetary Major under
Jupiter, per your "Fortune for Jupiter").

| Element | Suit | 3 Zodiacal Majors | Elemental Major | Planetary Major |
|---|---|---|---|---|
| **Fire** | Wands (14) | Emperor (Aries), Strength (Leo), Temperance (Sagittarius) | Judgement | Tower (Mars) |
| **Water** | Chalices (14) | Chariot (Cancer), Death (Scorpio), The Moon (Pisces) | The Hanged Man | Wheel of Fortune (Jupiter) |
| **Air** | Swords (14) | Lovers (Gemini), Justice (Libra), The Star (Aquarius) | The Fool | The Magician (Mercury) |
| **Earth** | Pentacles (14) | Hierophant (Taurus), Hermit (Virgo), The Devil (Capricorn) | The World | The Empress (Venus) |

Held out: **The Sun (19)**, **The High Priestess / Moon (2)** — first division and
final prime, the frame rather than the contents.

---

## 7×11 — Planetary Lords (complete)

Seven classical planets, 11 cards each; **the Fool held apart**. Membership weighted
by natal dignity against the subject's chart → the **scored / fixed-self** board.

**Closing arithmetic** (verified): five non-luminaries = 3 Majors + 6 Minors + 2
Courts = 11; luminaries = 3 Majors + 3 Minors + 1 Court + 4 Pages/Aces = 11.

### Majors — 3 per planet (own trump + domicile-sign trumps)

| Planet | Majors |
|---|---|
| Mars | Tower (own), Emperor (Aries), Death (Scorpio) |
| Venus | Empress (own), Hierophant (Taurus), Justice (Libra) |
| Mercury | Magician (own), Lovers (Gemini), Hermit (Virgo) |
| Jupiter | Wheel of Fortune (own), Temperance (Sagittarius), The Moon (Pisces) |
| Saturn | World (own), Devil (Capricorn), Star (Aquarius) |
| Sun | Sun (own), Strength (Leo), Judgement (Fire — by sect) |
| Moon | High Priestess (own), Chariot (Cancer), The Hanged Man (Water — by sect) |

Sun and Moon rule only one sign each, so own-trump + domicile yields 2 Majors; the
third is the elemental Major of the luminary's **sect** — Judgement (Fire, diurnal) →
Sun, Hanged Man (Water, nocturnal) → Moon. (The Fool is held apart.) Same sect rule
the Pages/Aces layer uses.

### Minors — by triplicity-ascent decan ruler (complete, from `decans.md`)

| Planet | Count | Cards |
|---|---|---|
| Mars | 6 | 2·7·9 Wands, 3·5·10 Chalices |
| Jupiter | 6 | 4·6·8 Wands, 4·6·8 Chalices |
| Saturn | 6 | 2·7·9 Pentacles, 3·5·10 Swords |
| Venus | 6 | 3·5·10 Pentacles, 2·7·9 Swords |
| Mercury | 6 | 4·6·8 Pentacles, 4·6·8 Swords |
| Sun | 3 | 3·5·10 Wands |
| Moon | 3 | 2·7·9 Chalices |

### Courts — by domicile ruler of the court's dominant sign (complete)

The 12 Knight/Queen/King courts (Pages are thrones — see Pages/Aces below). Each
court's **dominant sign** is the in-element sign anchoring its suit's element (the
0–20° majority of its span; Queen = cardinal, Knight = fixed, King = mutable — see
`mbti-majestic.md`), mapped to that sign's domicile ruler:

| Planet | Courts (dominant sign) |
|---|---|
| Mars | Queen of Wands (Aries), Knight of Chalices (Scorpio) |
| Venus | Queen of Swords (Libra), Knight of Pentacles (Taurus) |
| Mercury | King of Swords (Gemini), King of Pentacles (Virgo) |
| Jupiter | King of Wands (Sagittarius), King of Chalices (Pisces) |
| Saturn | Knight of Swords (Aquarius), Queen of Pentacles (Capricorn) |
| Sun | Knight of Wands (Leo) |
| Moon | Queen of Chalices (Cancer) |

2 each to the five non-luminaries, 1 each to the luminaries = 12.


### Pages + Aces — by sect (complete)

Fire + Air (diurnal) → **Sun**; Water + Earth (nocturnal) → **Moon**. Each luminary
takes 2 Pages + 2 Aces = 4.

- **Sun:** Page & Ace of Wands (Fire), Page & Ace of Swords (Air).
- **Moon:** Page & Ace of Chalices (Water), Page & Ace of Pentacles (Earth).

---

## 11×7 — Tree Stations (the derived laying)

Eleven Tree stations (10 Sephiroth + Da'ath), 7 cards each = 77, **+ the Fool apart**.
11 = the fixed state of man (2×5) — the board to place energy upon. Unlike the other
lenses, membership is **chart-derived**: the deck is ordered from the individual natal
chart, then dealt. This is the **derived / "between"** board.

It is the only lens that needs a computed chart (Kairos). It reuses the 7×11 lordship
as the card→lord map.

### Method — the Procession of the Lords

1. **Anchor.** Compute the **almuten figuris** (lord of the chart) — Ibn Ezra weighted
   essential dignity over the Ascendant, Sun, Moon, Lot of Fortune, and prenatal
   syzygy (Kairos `tier_almuten`). The almuten is the head of the procession.
2. **Procession.** The anchor's lordship-block (its 11 cards) leads. The remaining six
   lords' blocks follow, ordered by each lord's **zodiacal distance forward from the
   anchor's degree** (ascending). Ties (equal distance): higher essential dignity,
   then descending Tree order.
3. **Within a block.** The lord's 11 cards in fixed wheel-address order.
4. **Concatenate** → a 77-card order. The **Fool is held apart** — the climber,
   occupying every coordinate, dealt to none.
5. **Deal** 7 per station down the lightning flash: Kether → Chokmah → Binah → Chesed
   → Geburah → Tiphareth → Netzach → Hod → Yesod → Malkuth (70 cards).
6. **Da'ath = the remainder.** The final 7 are not dealt position-by-position; they
   **arrive** at Da'ath once the ten are complete — knowledge revealed as gained.

Result: a unique 11×7 board per chart. Because the lordship blocks are 11 and the
deal is 7 (coprime), the lords smear across the stations in a way no two charts share.
This is the **derived location**; read against the 7×11 fixed-self board, the
displacement between them is the reading.

Deterministic for a given natal chart — a derived laying, never a draw.
