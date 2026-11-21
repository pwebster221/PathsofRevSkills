---
name: horary-consultation
description: Run a complete horary consultation through the Kairos astrology MCP — cast the question-chart at the moment it lands, seat the querent (including third-party relay questions), assign significators with turned houses, judge by dignity, reception, translation, and perfection arithmetic, verify against the principals' natals (sunrise convention when birth time is unknown), optionally layer synastry and a dated transit corridor, and deliver a technical judgment, a plain-words letter, and a sequence-of-events report with hard calendar dates. Use whenever the user asks a horary question or says "cast a chart for this question", "run a question chart", "what does the chart say about X", "use kairos" for a question, an astrological "should I / will it happen / how do I help / where is it", or wants an existing horary re-seated, deepened with new context, cross-checked against natals or synastry, timed, or written up for the person it concerns. Requires kairos-mcp. Not for natal narratives or card readings.
---

# Horary Consultation

A horary chart is cast for the moment a question is received and understood, and judged to answer that question — nothing more, nothing less. This skill encodes the full consultation pipeline: **Cast → Seat → Judge → Verify → Layer → Date → Deliver.** A minimal consultation is Cast → Seat → Judge. A full one adds natal verification, a synastry layer for relational questions, a hard-dated timeline, and a cascade of written deliverables.

## Operating laws (read first, apply always)

**THE GATE — source before assertion.** Every planetary position comes from an Astraeus (formerly Kairos) call. Never recall positions, signs, or speeds from memory. Aspects, orbs, applying/separating status, and timing may be *derived arithmetically* from Astraeus-returned longitudes and speeds — derivation from sourced data is permitted and encouraged; free recall is not.

**The moment is the moment.** The chart is cast when the question reaches the astrologer and is understood. Later corrections — "actually the question is my friend's," new biographical context — **re-seat or re-read the chart; they never re-cast it.** Wrong-querent corrections move house assignments (see Seating). New context decodes the existing testimony (see Judgment).

**House system: Whole Sign** unless the user specifies otherwise. State the system in the writeup.

**Unknown birth times use the sunrise convention.** Cast the natal at local sunrise (≈05:25–07:15 depending on date/latitude; estimate, then verify). Self-verification is mandatory: the returned Ascendant must sit within ~1–2° of the Sun. Report the verification. State the Moon's intraday uncertainty range explicitly (Moon moves ~12–14°/day; compute the span from midnight to 23:59 and carry it as an orb-of-uncertainty on every Moon claim). House overlays from sunrise charts are solar-symbolic — weight them lightly and say so once.

**Canonical time:** record the cast as local time, UTC, Julian day, and Unix epoch seconds.

**Question-scope discipline.** The chart answers the question asked. If the question is about the dog, the judgment is about the dog; adjacent lives (the ex, the friend) get described only as they bear on the question, and their outcomes are never promised. Say so explicitly in deliverables when the temptation to overreach is present.

## Step 1 — Cast

Call `astraeus:get_current_transit` (the Astraeus MCP server, key `astraeus`; formerly `kairos-mcp`, tool names unchanged) with the querent's latitude/longitude and `house_system` (default `whole_sign`). This returns the moment-chart: planets with longitudes, sign-degrees, speeds, retrograde flags, plus house cusps. Record timestamp, JD, epoch. If the call needs user approval and fails with "no approval received," tell the user to approve and explain that the horary moment is preserved — the question already landed.

## Step 2 — Seat the chart

Decide who holds the Ascendant:

- **The question is the asker's own** → asker = Ascendant.
- **Relay rule:** the question originates with a third party and reaches you through an agent (the user asking on a friend's behalf, with that person's knowledge) → **the concerned party takes the Ascendant.** Lilly read for absent clients through messengers; the messenger never got the first house. The relaying user moves to their relationship house (friend = 11th, sibling = 3rd, partner = 7th, etc.) and gets read there — including dignity, disposition, and what role the chart assigns them in the matter.
- **The user asks about someone else's situation from their own concern, without that person's involvement** → user keeps the Ascendant; the other person is found by turning.

Document the ruling and its reason in the writeup. When a correction arrives mid-consultation, re-seat and show explicitly what changes (usually only the relayer's significator) and what holds (everything else).

## Step 3 — Significators and judgment

Querent = Lord of the Ascendant **plus the Moon as co-significator.** Quesited parties by house, turning as needed (the ex's dog = 6th from the 7th). Full machinery — turning arithmetic, considerations before judgment, dignity audit, receptions, translation/collection, prohibition sweep, perfection arithmetic — lives in **`references/judgment-procedure.md`. Read it before judging any chart.**

The judgment must end in a verdict: can the thing be done / will it happen / where does it resolve — supported by named testimonies, with the mechanism (who acts, through which channel, in what order) and honest cautions.

## Step 4 — Verify against the natals (radicality)

For each principal whose birth data is available, cast `astraeus:get_natal` (sunrise convention if no time; tiers 0–5 suffice). Then hunt **echoes between the horary and the natals** — these are radicality testimonies that the chart knows who it's for:

- The horary's significator *choice* matching a natal occupancy (the horary gives the dog to Jupiter; the querent's natal Jupiter sits in his natal 6th, the animal house).
- A horary house landing on a natal cluster (the horary's quesited-house sign holds the querent's natal Moon and Saturn — the matter lives where his heart and duty live).
- Horary bodies transiting the principal's relevant natal houses (the horary Moon — the translator — moving through the querent's natal 11th when a friend is doing the relaying).
- Tight degree contacts between horary planets and natal points (horary Mercury conjunct a principal's natal Venus within 1°).

Two or three strong echoes confirm the chart; report them. Their absence doesn't void the judgment but lowers stated confidence.

## Step 5 — Context decoding

When the user adds biographical context (homelessness, addiction, illness, a breakup), **the context decodes testimony already present — it does not change the chart.** Re-read the significators' conditions literally: peregrine = the wanderer, the one with no place that receives it (Lilly's vagabonds); Saturn's terms = the bounds of hardship; Neptune prominent = the fog, the opiate, the dissolved boundary; a 12th-house quesited = confinement, the street, hidden suffering — while distinguishing *structural* placements (6-from-7 always lands in the radical 12th) from *elective* testimony layered on top (the lord's dignity, the Node's presence). The mark of a true decode is that prior readings sharpen rather than reverse.

## Step 6 — Relational layer (optional)

When the question is entangled with a relationship between principals, run `astraeus:get_synastry` and read it **for the question's sake** — what binds these two, which channels are clean for the needed contact, which are live wires. Protocol, including the chemistry/saturn-glue blocks, dignity-exchange traps, the cross-aspect attribution gotcha, and the transit corridor, lives in **`references/relational-layer.md`. Read it before any synastry call.**

## Step 7 — The timeline

Convert every perfection, crossing, and ingress into **hard calendar dates** using real ephemeris speeds (arithmetic in `judgment-procedure.md`). Then designate, by name:

- **THE WINDOW** — the reception-bounded contact period (e.g., until a significator ingresses out of the receiving sign). Give its closing day and approximate hour.
- **The delivery band** — when arrangements and material help land (often the Mercury-channel perfections).
- **THE HARD DATE** — the catalyst: the tightest malefic trigger in the sequence (e.g., transiting Mars exact on a principal's natal Mars while opposing Pluto). Distinguish the *catalyst* from the *turn*: the hard date destabilizes; the perfection-plus-ingress cluster that follows is the shift it precipitates. Attach conduct rules to the hard date (nothing scheduled, nothing negotiated) when the question warrants them.
- **Completion** — the main perfection, with its degree (flag 29°/eleventh-hour perfections).
- **The chapter turn** — post-perfection ingresses of the significators; frame the help as completion, not re-opening, when the chart shows it.

## Step 8 — Deliverables

Up to three registers, produced on request, in this order of derivation: **technical judgment → plain-words letter → sequence-of-events report.** Each is a translation of the one before, never a new reading. Templates, register-shifting rules, and a worked example live in **`references/deliverables.md`.** When the counsel includes real-world action (vet care, shelter, treatment, legal paths), verify current programs by web search before naming them, and embed them at the right timeline points — never as a detached list.

## Astraeus operations

- **Tools:** `get_current_transit` (the horary moment), `get_natal` (principals; accepts `birth_data` dict, `tiers`, `house_systems` list), `get_synastry` / `get_composite` (`chart_a`/`chart_b` each `{"chart_id": ...}` or `{"birth_data": {...}, "anonymous": true}`), `get_transit` (corridor spot-checks against a natal), `get_chart` / `list_charts` (retrieval).
- **birth_data shape:** `{name, date "YYYY-MM-DD", time "HH:MM", tz_offset (signed hours, mind DST for the birth date), latitude, longitude, city}`.
- **Large results store to a file path** instead of returning inline. Parse with Python: load the JSON, the payload is `json.loads(d[0]['text'])`; natal keys include `meta, planets, houses, aspects, chart_id`; synastry keys include `natal_a, natal_b, cross_aspects, pair_synthesis`. Planets carry `longitude, sign, sign_degree, speed, retrograde`.
- **Persistence and privacy:** charts persist with a `chart_id` (anonymous unless a `user_id` is passed). Report every chart_id created so the user can tag, link, or delete it in the staging DB.

## Ethics (non-negotiable, all deliverables)

1. **Through the person, never around them.** Help that touches another person's life, property, or animal routes through their knowledge and consent. Never counsel unilateral removal of an animal or property, however sympathetic the framing — and notice when the chart itself agrees (translation runs *to* their significator; a bond marked as the quesited's strength).
2. **Dignity for the vulnerable.** Describe, don't judge. A peregrine Venus is a wanderer the chart is describing, not condemning. Find and report the testimony of care that survives hard circumstances (the recent benefic conjunction; the exalted lord) — it is usually there and usually true.
3. **No outcome promises for lives the question didn't ask about.** "Her road wasn't the question, and it isn't yours to carry" is a permanent fixture of this practice.
4. **Helper, not rescuer.** When the chart shows it (a 12th-house Sun overlay, Saturn in fall disposed by the querent's lord), say plainly that the user or querent works best offstage, frames the move but doesn't make it.
5. **Boundary counsel must be chart-derived and protective, not punitive** — "nothing through Mars, everything through Mercury and Jupiter" is legitimate because the chart drew it; generic moralizing is not.
6. **Crisis honesty.** If the situation involves addiction, homelessness, or danger, real resources (verified current by search) accompany the symbolic counsel, and safety-relevant advice (bring a friend to a street meeting; don't schedule confrontation on the hard date) is stated without drama.

## Failure modes to avoid

- Recasting the chart because the querent was corrected. Re-seat.
- Asserting positions, sunrise times, or program details from memory. Source them.
- Reading 12th-house doom into a structurally turned placement.
- Letting a synastry drift into reunion validation when the question was about help.
- Delivering the timeline without naming which date is catalyst and which is turn.
- Burying the verdict. Lead with it in every register.
