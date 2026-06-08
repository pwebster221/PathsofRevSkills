# Minor Arcana — Decan Table

Source: live pull from the Esoteric Repository (`MinorArcana`, pips 2–10), verified
against the Mars Scoring Engine canon. This file is the **fallback** for the Minor
module and the 7×11 lens; query the Repository live when possible.

## Ruler systems

- **Triplicity-ascent** — canonical. Edge `RULED_BY_DECAN → :HeavenlyBody`. This is
  what the Mars Scoring Engine scores on, and the default for all interpretation.
- **Chaldean** — alternate, off by default. Edge `COUNTER_RULED_BY → :HeavenlyBody`.
  Use only on explicit request.

> ⚠️ **Data caveat.** The node property `astro_planetary_ruler` currently mirrors
> the **Chaldean** value, not the canonical triplicity-ascent ruler. Resolve the
> ruler from the `RULED_BY_DECAN` **edge**, never from that property. (Candidate
> Linear cleanup: align `astro_planetary_ruler` to the canonical edge or rename it
> `astro_chaldean_ruler`.)

## Sign progression

Each suit runs its three signs, three pips each, beginning with the suit's cardinal
sign: Wands → Aries/Leo/Sagittarius; Chalices → Cancer/Scorpio/Pisces; Swords →
Libra/Aquarius/Gemini; Pentacles → Capricorn/Taurus/Virgo.

## Table

Grammar reminder — **planet (triplicity-ascent) = subject · sign = environment ·
Enneagram type = situation.**

| Card | Suit | Pip | Sign | Triplicity-ascent (canonical) | Chaldean (alt) | Enneagram |
|---|---|---|---|---|---|---|
| Two of Wands | Wands | 2 | Aries | Mars | Mars | 2 |
| Three of Wands | Wands | 3 | Aries | Sun | Sun | 3 |
| Four of Wands | Wands | 4 | Aries | Jupiter | Venus | 4 |
| Five of Wands | Wands | 5 | Leo | Sun | Saturn | 5 |
| Six of Wands | Wands | 6 | Leo | Jupiter | Jupiter | 6 |
| Seven of Wands | Wands | 7 | Leo | Mars | Mars | 7 |
| Eight of Wands | Wands | 8 | Sagittarius | Jupiter | Mercury | 8 |
| Nine of Wands | Wands | 9 | Sagittarius | Mars | Moon | 9 |
| Ten of Wands | Wands | 10 | Sagittarius | Sun | Saturn | 1 |
| Two of Chalices | Chalices | 2 | Cancer | Moon | Venus | 2 |
| Three of Chalices | Chalices | 3 | Cancer | Mars | Mercury | 3 |
| Four of Chalices | Chalices | 4 | Cancer | Jupiter | Moon | 4 |
| Five of Chalices | Chalices | 5 | Scorpio | Mars | Mars | 5 |
| Six of Chalices | Chalices | 6 | Scorpio | Jupiter | Sun | 6 |
| Seven of Chalices | Chalices | 7 | Scorpio | Moon | Venus | 7 |
| Eight of Chalices | Chalices | 8 | Pisces | Jupiter | Saturn | 8 |
| Nine of Chalices | Chalices | 9 | Pisces | Moon | Jupiter | 9 |
| Ten of Chalices | Chalices | 10 | Pisces | Mars | Mars | 1 |
| Two of Swords | Swords | 2 | Libra | Venus | Moon | 2 |
| Three of Swords | Swords | 3 | Libra | Saturn | Saturn | 3 |
| Four of Swords | Swords | 4 | Libra | Mercury | Jupiter | 4 |
| Five of Swords | Swords | 5 | Aquarius | Saturn | Venus | 5 |
| Six of Swords | Swords | 6 | Aquarius | Mercury | Mercury | 6 |
| Seven of Swords | Swords | 7 | Aquarius | Venus | Moon | 7 |
| Eight of Swords | Swords | 8 | Gemini | Mercury | Jupiter | 8 |
| Nine of Swords | Swords | 9 | Gemini | Venus | Mars | 9 |
| Ten of Swords | Swords | 10 | Gemini | Saturn | Sun | 1 |
| Two of Pentacles | Pentacles | 2 | Capricorn | Saturn | Jupiter | 2 |
| Three of Pentacles | Pentacles | 3 | Capricorn | Venus | Mars | 3 |
| Four of Pentacles | Pentacles | 4 | Capricorn | Mercury | Sun | 4 |
| Five of Pentacles | Pentacles | 5 | Taurus | Venus | Mercury | 5 |
| Six of Pentacles | Pentacles | 6 | Taurus | Mercury | Moon | 6 |
| Seven of Pentacles | Pentacles | 7 | Taurus | Saturn | Saturn | 7 |
| Eight of Pentacles | Pentacles | 8 | Virgo | Mercury | Sun | 8 |
| Nine of Pentacles | Pentacles | 9 | Virgo | Saturn | Venus | 9 |
| Ten of Pentacles | Pentacles | 10 | Virgo | Venus | Mercury | 1 |

## Triplicity-ascent distribution (feeds the 7×11 lens)

Counting the canonical rulers across the 36 pips:

| Planet | Count | Cards |
|---|---|---|
| Mars | 6 | 2·7·9 Wands, 3·5·10 Chalices |
| Jupiter | 6 | 4·6·8 Wands, 4·6·8 Chalices |
| Saturn | 6 | 2·7·9 Pentacles, 3·5·10 Swords |
| Venus | 6 | 3·5·10 Pentacles, 2·7·9 Swords |
| Mercury | 6 | 4·6·8 Pentacles, 4·6·8 Swords |
| Sun | 3 | 3·5·10 Wands |
| Moon | 3 | 2·7·9 Chalices |

6 each to the five non-luminaries, 3 each to the luminaries = 36. This is exactly
the Minor contribution the 7×11 planetary-lords lens requires (the luminaries are
then topped up by courts, pages, and aces to reach 11).
