# Judgment Procedure

The full machinery for Step 3 of a horary consultation. Work through it in order; skip nothing silently — if a check is waived (e.g., judging despite an early Ascendant), say so and why.

## 1. Significator assignment

- **Querent:** Lord of the Ascendant sign (traditional rulerships: Aries/Scorpio→Mars, Taurus/Libra→Venus, Gemini/Virgo→Mercury, Cancer→Moon, Leo→Sun, Sagittarius/Pisces→Jupiter, Capricorn/Aquarius→Saturn), **plus the Moon as co-significator** unless the Moon is the quesited's lord.
- **Quesited:** by house. Core map — 2nd money/movables, 3rd siblings/messages/short trips, 4th father/home/land/end-of-the-matter, 5th children/pleasure, 6th illness/servants/small animals (**dogs are 6th regardless of breed or size**; 12th is for horses and great cattle), 7th partner/ex-partner/open enemy/the-other, 8th death/the partner's money, 9th journeys/faith/law, 10th career/mother/authority, 11th friends/hopes, 12th confinement/hidden things/self-undoing.
- **Turning:** count the quesited's house as a new 1st and count onward, signs inclusive. *The ex's dog* = 6th from the 7th: Libra 7th → Pisces is the 6th sign from Libra counting Libra as 1 → radical 12th. Always show the arithmetic once in the technical writeup. **Structural caution:** 6-from-7 lands in the radical 12th for every chart; do not read 12th-house affliction into the placement itself — read the *lord's* condition and what is elective (occupying bodies, the Node, aspects).
- **Natural significators** (Sun for the dignified, Moon for mothers/the public, Venus for young women, Saturn for the old, Mercury for messengers) are overlay testimony only — never let them displace the house lords.

## 2. Considerations before judgment

Check and record; judge anyway with stated cautions (Lilly's own practice):

- Ascendant under 3° (question premature) or over 27° (matter already decided). Whole-sign output gives sign-level cusps only — if the exact ASC degree matters, derive it from the MC or request a quadrant system alongside.
- Moon void of course (perfects no further major aspect before leaving its sign).
- Moon in the via combusta (15° Libra – 15° Scorpio).
- Saturn in the 7th (the astrologer errs) or in the 1st (the querent burdened; the matter weighs).
- Sect: Sun above horizon = day chart. Note the out-of-sect malefic — it marks the harshest pressure in the figure and *who it lands on* is itself a finding.

## 3. Dignity audit

For each significator, from Kairos data plus the standard tables:

- **Essential:** domicile, exaltation, triplicity (state which scheme; sect-assign if Dorothean), terms (Egyptian and Ptolemaic differ — if a claim depends on the term, verify it holds in both or name the system), face. **Peregrine** = none of the above: the wanderer. Read peregrination literally when the question's context supports it (homelessness, drift, the unplaced). Detriment and fall are debilities, not moral verdicts: detriment = acting outside one's strength; fall = helping in a jurisdiction not one's own.
- **Accidental:** house strength (angular > succedent > cadent), speed, retrogradation, combustion (within ~8.5° of the Sun, same sign — the burned/silenced voice; cazimi within 17' exalts instead), besiegement, station.

## 4. Receptions and disposition

- A planet in another's domicile (or exaltation) is **received** — it leans on, is welcomed by, is in the territory of that lord. Mutual reception = a working exchange.
- **Trace the dispositor chains of all significators.** Closed loops (A in B's sign, B in C's, C in A's) mean the matter is internally entangled — no outside authority resolves it; the parties hold each other. A significator *outside* the loop but disposed *into* it (the friend's Saturn disposed by the querent's Mars) shows whose initiative activates whom.
- Both quesited lords disposed by the querent's co-significator = the matter rests, dispositionally, on the querent. Say it when it's there; it often *is* the answer to "how can I help."

## 5. Perfection — the mechanism of the answer

The question resolves through one or more of:

- **Direct perfection:** the significators apply to a major aspect and complete it in-sign.
- **Translation of light:** a faster body separates from one significator and applies to the other, carrying the matter between them. The translator's identity is a finding (the Moon = the querent himself; Mercury = a message, an arranged service, the go-between who relayed the question). Translation by squares perfects with friction — say "do it anyway" when receptions support it.
- **Collection:** both significators apply to a slower third body that gathers them.
- **Reception-only perfection** (strong mutual reception without aspect) — weak; flag as such.

**Prohibition sweep — mandatory before declaring any perfection.** For each pending perfection, check every body that perfects an aspect with either significator *earlier*: does it abscise the light (a swifter body cutting in) or assist (a benefic or relevant lord whose earlier contact is itself a translation/collection serving the matter)? A Mercury that sextiles the querent's lord and then conjoins the quesited's lord before the main aspect completes is reinforcement, not prohibition — the delivery channel. Name each intervening contact either way.

## 6. Timing arithmetic (real-ephemeris method)

Use returned longitudes and daily speeds; show the work once per writeup.

```
t_days = Δ / (speed_faster − speed_slower)
```

where Δ is the degrees the faster body must close on the (moving) aspect point. For an applying aspect between A (faster) and B: solve `lonA + speedA·t + aspect_angle = lonB + speedB·t` (mind direction and 360° wraps). Verify **in-sign completion**: compute both bodies' positions at t; if either ingresses first, the perfection is denied by that ingress unless the aspect re-forms.

- Convert every t to a **calendar date and approximate local hour** from the cast timestamp.
- **Sign-exit times** (`(30 − sign_degree)/speed`) bound the windows: a reception ends when the received planet leaves the receiving sign — that boundary is usually THE WINDOW's closing time.
- **29th-degree perfections** complete at the eleventh hour, immediately before ingress: read as last-moment success followed by changed conditions. List the post-perfection ingresses of all significators with dates — that cluster is the chapter turn.
- Classical symbolic units (cardinal/angular = days, mutable/succedent = weeks, fixed/cadent = months) are a fallback for charts without usable speeds; prefer real arithmetic and say which was used.
- The Moon's **recent separations** (work backward: Δ/Moon-speed) reconstruct the question's prehistory — what the querent just came through (the Neptune fog, the Saturn weight, the Sun's clarity) and roughly when. Report it; it builds trust and tests radicality.

## 7. The verdict

End the judgment with, in order: the answer to the question as asked; the mechanism (who acts, through which channel, in what sequence); the timing skeleton (window / delivery / catalyst / completion / turn — finalized in Step 7 of SKILL.md); the cautions (debilities of the actors, the out-of-sect malefic's target, Neptune-style fog); and the outcome testimony for the quesited (the end-of-the-matter 4th, the quesited lord's final condition, the Node's placement). Lead every deliverable with the verdict.
