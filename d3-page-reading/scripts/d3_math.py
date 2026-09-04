"""D3 (I.3 Throne Pages) reference math — PAT-[d3], SPEC RATIFIED.

Pure functions, no I/O. Verifies the canon entailment (the throne names the
suit) and the 2026-08-18 proof run (Paul, Gemini rising, whole sign).

D3 consumes D2's reader-side output: Option B vault routing takes a D2
treasury dict; Option A relations take the D2 pole totals. See the sibling
skill d2-ace-reading/scripts/d2_math.py for how those are produced.
"""

SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
         "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
ELEMENT = {s: ["Fire", "Earth", "Air", "Water"][i % 4] for i, s in enumerate(SIGNS)}
OPPOSITION = {"Fire": "Air", "Air": "Fire", "Water": "Earth", "Earth": "Water"}
CONFLICT = {"Fire": "Water", "Water": "Fire", "Earth": "Air", "Air": "Earth"}
FUNCTION = {"Fire": "Intuition", "Earth": "Sensing", "Air": "Thinking", "Water": "Feeling"}

# Seasons in wheel order: (name, cardinal gate, fixed throne, mutable passing door)
SEASONS = [("Spring", "Aries", "Taurus", "Gemini"),
           ("Summer", "Cancer", "Leo", "Virgo"),
           ("Autumn", "Libra", "Scorpio", "Sagittarius"),
           ("Winter", "Capricorn", "Aquarius", "Pisces")]

SUIT_OF_ELEMENT = {"Fire": "Page of Wands", "Water": "Page of Chalices",
                   "Air": "Page of Swords", "Earth": "Page of Pentacles"}
PERSONA = {"Page of Pentacles": "istj", "Page of Wands": "infj",
           "Page of Chalices": "infp", "Page of Swords": "istp"}
# Nocturnal Pages walk WITH the year (auxiliary at the mutable passing door);
# diurnal walk AGAINST it (auxiliary at the cardinal gate). Moon's and Sun's
# Pages fix the sects: Chalices/Pentacles nocturnal, Wands/Swords diurnal.
NOCTURNAL = {"Page of Chalices", "Page of Pentacles"}


def page_of_season(season_name):
    """The throne names the suit: the fixed sign's element is the Page's."""
    for name, gate, throne, door in SEASONS:
        if name == season_name:
            return SUIT_OF_ELEMENT[ELEMENT[throne]]
    raise KeyError(season_name)


def arc(page):
    """-> dict(season, gate, throne, door, sect, walk_sign, far_sign)."""
    for name, gate, throne, door in SEASONS:
        if SUIT_OF_ELEMENT[ELEMENT[throne]] == page:
            noct = page in NOCTURNAL
            return dict(season=name, gate=gate, throne=throne, door=door,
                        sect="nocturnal" if noct else "diurnal",
                        walk_sign=door if noct else gate,
                        far_sign=gate if noct else door)
    raise KeyError(page)


def stack(page):
    """-> (dominant, auxiliary, inferior, tertiary) as elements.
    Dominant = throne element; auxiliary = walked-toward door's element;
    inferior = far door's element; tertiary = the one element the season does
    not contain (the Tertiary Gap Lemma) — always the dominant's zodiacal
    opposite, which is why the home vault can never hold its coin."""
    a = arc(page)
    present = {ELEMENT[a["throne"]], ELEMENT[a["walk_sign"]], ELEMENT[a["far_sign"]]}
    tert = next(e for e in ("Fire", "Earth", "Air", "Water") if e not in present)
    return ELEMENT[a["throne"]], ELEMENT[a["walk_sign"]], ELEMENT[a["far_sign"]], tert


def sister(page):
    """The Page whose sovereign is this Page's tertiary — the opposite season."""
    tert = stack(page)[3]
    return SUIT_OF_ELEMENT[tert]


def rivals(page):
    """The two adjacent seasons' Pages (competition, always crossing sect)."""
    names = [SUIT_OF_ELEMENT[ELEMENT[t]] for _, _, t, _ in SEASONS]
    i = names.index(page)
    return names[(i - 1) % 4], names[(i + 1) % 4]


def whole_sign_house(sign, asc_sign):
    return (SIGNS.index(sign) - SIGNS.index(asc_sign)) % 12 + 1


def gap_house(page, asc_sign):
    """Where the dark part points: the sister's throne-sign's house."""
    return whole_sign_house(arc(sister(page))["throne"], asc_sign)


def vault_routes(page):
    """-> {currency_element: part} for the home vault. The dark currency is
    forbidden: the home vault constitutionally cannot hold it (the sister
    axis is the opposition axis)."""
    dom, aux, inf, tert = stack(page)
    assert OPPOSITION[dom] == tert  # the forbidden-coin theorem
    return {dom: "sovereign", aux: "walking", inf: "far", tert: "FORBIDDEN"}


def constitution(page, treasury):
    """Route a D2 treasury (e.g. {"Earth": 6, "Air": 6, "Fire": 6}) into the
    Page's parts. Star bonuses (key "star") ride along unrouted."""
    routes = vault_routes(page)
    feed = {"sovereign": 0, "walking": 0, "far": 0}
    for cur, pts in treasury.items():
        if cur == "star":
            continue
        part = routes.get(cur)
        assert part != "FORBIDDEN", f"{cur} coin cannot be in {page}'s vault"
        if part:
            feed[part] += pts
    return feed


def feed_band(points):
    """Recorded banding of the proof run. The dark part is always 'forbidden'
    regardless of points — call this only for the three grounded parts."""
    if points >= 6:
        return "well-fed"
    if points >= 3:
        return "fed"
    if points >= 1:
        return "lean"
    return "unfed"


if __name__ == "__main__":
    # The entailment: the throne names the suit.
    assert page_of_season("Spring") == "Page of Pentacles"
    assert page_of_season("Summer") == "Page of Wands"
    assert page_of_season("Autumn") == "Page of Chalices"
    assert page_of_season("Winter") == "Page of Swords"
    # Tertiary Gap Lemma: quadrant holds dom+aux+inf only; tertiary absent.
    assert stack("Page of Chalices") == ("Water", "Fire", "Air", "Earth")   # canon example
    assert stack("Page of Pentacles") == ("Earth", "Air", "Fire", "Water")
    assert stack("Page of Wands") == ("Fire", "Water", "Earth", "Air")
    assert stack("Page of Swords") == ("Air", "Earth", "Water", "Fire")
    # Sister pairs exchange dominant <-> tertiary, opposite seasons.
    assert sister("Page of Pentacles") == "Page of Chalices"
    assert sister("Page of Chalices") == "Page of Pentacles"
    assert sister("Page of Wands") == "Page of Swords"
    assert sister("Page of Swords") == "Page of Wands"
    # Competition always crosses sect; the sister challenge runs within it.
    for _, _, throne, _ in SEASONS:
        p = SUIT_OF_ELEMENT[ELEMENT[throne]]
        for r in rivals(p):
            assert (p in NOCTURNAL) != (r in NOCTURNAL)
        assert (p in NOCTURNAL) == (sister(p) in NOCTURNAL)
    # Walk seating: nocturnal aux at mutable door, diurnal aux at cardinal gate.
    assert arc("Page of Chalices")["walk_sign"] == "Sagittarius"
    assert arc("Page of Pentacles")["walk_sign"] == "Gemini"
    assert arc("Page of Wands")["walk_sign"] == "Cancer"
    assert arc("Page of Swords")["walk_sign"] == "Capricorn"
    # Proof-run houses (Gemini rising): stations and gaps.
    assert whole_sign_house(arc("Page of Pentacles")["throne"], "Gemini") == 12
    assert whole_sign_house(arc("Page of Swords")["walk_sign"], "Gemini") == 8
    assert gap_house("Page of Pentacles", "Gemini") == 6
    assert gap_house("Page of Wands", "Gemini") == 9
    assert gap_house("Page of Chalices", "Gemini") == 12
    assert gap_house("Page of Swords", "Gemini") == 3
    # Double-booking: each gap house IS the sister's throne house.
    for _, _, throne, _ in SEASONS:
        p = SUIT_OF_ELEMENT[ELEMENT[throne]]
        assert gap_house(p, "Gemini") == whole_sign_house(arc(sister(p))["throne"], "Gemini")
    # Vault routing + proof-run feeds.
    assert vault_routes("Page of Chalices") == {"Water": "sovereign", "Fire": "walking",
                                                "Air": "far", "Earth": "FORBIDDEN"}
    pent = constitution("Page of Pentacles", {"Earth": 6, "Air": 6, "Fire": 6, "star": 2})
    assert {k: feed_band(v) for k, v in pent.items()} == {
        "sovereign": "well-fed", "walking": "well-fed", "far": "well-fed"}
    chal = constitution("Page of Chalices", {"Fire": 3})
    assert {k: feed_band(v) for k, v in chal.items()} == {
        "sovereign": "unfed", "walking": "fed", "far": "unfed"}
    swords = constitution("Page of Swords", {"Air": 6, "Earth": 3, "star": 2})
    assert {k: feed_band(v) for k, v in swords.items()} == {
        "sovereign": "well-fed", "walking": "fed", "far": "unfed"}
    wands = constitution("Page of Wands", {"Fire": 6, "Water": 3, "Earth": 3})
    assert {k: feed_band(v) for k, v in wands.items()} == {
        "sovereign": "well-fed", "walking": "fed", "far": "fed"}
    print("all checks pass")
