"""D2 (I.2 Elemental Aces) reference math — PAT-[d2], rulings of 2026-08-12.

Pure functions, no I/O. Verified against the ratified 2026-08-18 performance
(Paul, 1989-01-06 15:10 Durham NC, Gemini rising, whole sign).

Reader-side only: everything here feeds Reader's Scores and felt-volume
banding. None of it is ever sent to a performer.
"""

SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
         "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
ELEMENT = {s: ["Fire", "Earth", "Air", "Water"][i % 4] for i, s in enumerate(SIGNS)}
MODALITY = {s: ["Cardinal", "Fixed", "Mutable"][i % 3] for i, s in enumerate(SIGNS)}
CENTER = {"Cardinal": "Heart", "Fixed": "Head", "Mutable": "Gut"}

# Households: element -> (Heart, Head, Gut) signs.
ROOMS = {"Fire": ("Aries", "Leo", "Sagittarius"),
         "Water": ("Cancer", "Scorpio", "Pisces"),
         "Air": ("Libra", "Aquarius", "Gemini"),
         "Earth": ("Capricorn", "Taurus", "Virgo")}
ACE = {"Fire": "Ace of Wands", "Water": "Ace of Chalices",
       "Air": "Ace of Swords", "Earth": "Ace of Pentacles"}
FUNCTION = {"Fire": "Intuition", "Water": "Feeling",
            "Air": "Thinking", "Earth": "Sensing"}

# Relations. Competitive = zodiacal opposition; twin = conflict axis (never
# an outward aspect); the two obliques are the remaining elements, performed
# non-twin first, twin's company second, competitor last.
OPPOSITION = {"Fire": "Air", "Air": "Fire", "Water": "Earth", "Earth": "Water"}
TWIN = {"Fire": "Water", "Water": "Fire", "Earth": "Air", "Air": "Earth"}

# Carrier streams (canon elemental-dominance table). Dominant first.
STREAMS = {"Mars": ("Fire", "Water"), "Jupiter": ("Fire", "Water"),
           "Venus": ("Air", "Earth"), "Mercury": ("Air", "Earth"),
           "Saturn": ("Earth", "Air"),
           "Sun": ("Fire",), "Moon": ("Water",),
           "Uranus": ("Air",), "Neptune": ("Water",), "Pluto": ("Fire",)}
PLANETS = {"Mercury", "Venus", "Mars", "Jupiter", "Saturn"}
LUMINARIES = {"Sun", "Moon"}
OUTER_LORDS = {"Uranus", "Neptune", "Pluto"}


def sign_of(lon):
    return SIGNS[int(lon % 360.0 // 30)]


def whole_sign_house(sign, asc_sign):
    return (SIGNS.index(sign) - SIGNS.index(asc_sign)) % 12 + 1


def relations(element):
    """-> (oblique_nontwin, oblique_twin_company, competitive) — performance order."""
    comp, twin = OPPOSITION[element], TWIN[element]
    nontwin = [e for e in ("Fire", "Earth", "Air", "Water")
               if e not in (element, comp, twin)][0]
    return nontwin, twin, comp


def option_a(body, terrain):
    """Additive score of one body funding the pole of its occupied sign."""
    if body in PLANETS:
        d = STREAMS[body]
        return 1 + 2 + (2 if d[0] == terrain else (1 if len(d) > 1 and d[1] == terrain else 0))
    if body in LUMINARIES or body in OUTER_LORDS:
        e = STREAMS[body][0]
        return 1 + 2 + (2 if e == terrain else (-1 if OPPOSITION[e] == terrain else 0))
    return 1 + 1  # other bodies: angles, nodes, Liliths, Chiron, comets, asteroids, lots


def option_b(body, terrain):
    """Treasury deposit: {currency: points}. Stream-less bodies deposit
    nothing (open ruling, exercised 2026-08-18, unratified)."""
    out = {}
    for stream in STREAMS.get(body, ()):
        mult = 2 if stream == terrain else (0 if OPPOSITION[stream] == terrain else 1)
        if mult:
            out[stream] = out.get(stream, 0) + 3 * mult
    return out


def star_contact(orb_degrees):
    """+2 within a degree of a body, either option; otherwise absent.
    Ruled precedent: 1.124 deg (Vega-Sun, 2026-08-18) is OUTSIDE."""
    return 2 if orb_degrees <= 1.0 else 0


def braid(body, element):
    """How a carrier of `element` carries it: 'leading edge' | 'depth' |
    'pure' | 'outer lord' | None (not a carrier)."""
    s = STREAMS.get(body, ())
    if element not in s:
        return None
    if body in OUTER_LORDS:
        return "outer lord"
    if len(s) == 1:
        return "pure"
    return "leading edge" if s[0] == element else "depth"


def felt_volume(occupants, planetary):
    """Recorded banding of the ratified run. `occupants` counts every listed
    presence (both node measures count); `planetary` counts planets,
    luminaries, and Outer Lords among them."""
    if occupants == 0:
        return "empty"
    if occupants <= 2:
        return "thin"
    if occupants >= 5 and planetary > occupants / 2:
        return "crowded"
    return "peopled"


def company_scores(placements, asc_sign):
    """placements: iterable of (body_name, longitude). Returns per-element
    dicts: A totals by center, B treasuries by center/currency."""
    A, B = {}, {}
    for name, lon in placements:
        sign = sign_of(lon)
        e, c = ELEMENT[sign], CENTER[MODALITY[sign]]
        A.setdefault(e, {}).setdefault(c, 0)
        A[e][c] += option_a(name, e)
        for cur, pts in option_b(name, e).items():
            B.setdefault(e, {}).setdefault(c, {}).setdefault(cur, 0)
            B[e][c][cur] += pts
    return A, B


if __name__ == "__main__":
    # Self-test against the ratified 2026-08-18 run (Gemini rising).
    assert ROOMS["Earth"] == ("Capricorn", "Taurus", "Virgo")
    assert whole_sign_house("Capricorn", "Gemini") == 8
    assert whole_sign_house("Taurus", "Gemini") == 12
    assert whole_sign_house("Virgo", "Gemini") == 4
    assert relations("Earth") == ("Fire", "Air", "Water")
    assert relations("Fire") == ("Earth", "Water", "Air")
    assert relations("Water") == ("Air", "Fire", "Earth")
    assert relations("Air") == ("Water", "Earth", "Fire")
    # A worked values
    assert option_a("Saturn", "Earth") == 5
    assert option_a("Sun", "Earth") == 3
    assert option_a("Moon", "Earth") == 2      # water opposed by earth terrain
    assert option_a("Mars", "Fire") == 5
    assert option_a("Mercury", "Air") == 5
    assert option_a("Jupiter", "Earth") == 3   # neither stream matches
    assert option_a("Pluto", "Water") == 3     # fire neutral in water
    assert option_a("Ascendant", "Air") == 2   # other body
    # B worked values (canon examples)
    assert option_b("Sun", "Earth") == {"Fire": 3}
    assert option_b("Mars", "Fire") == {"Fire": 6, "Water": 3}
    assert option_b("Moon", "Earth") == {}     # water inadmissible in earth
    assert option_b("Saturn", "Earth") == {"Earth": 6, "Air": 3}
    assert option_b("Mercury", "Air") == {"Air": 6, "Earth": 3}
    assert option_b("Lot of Fortune", "Air") == {}  # stream-less (open ruling)
    # Star rule
    assert star_contact(0.232) == 2 and star_contact(0.032) == 2
    assert star_contact(1.124) == 0            # Vega-Sun exclusion precedent
    # Braids
    assert braid("Saturn", "Earth") == "leading edge"
    assert braid("Saturn", "Air") == "depth"
    assert braid("Sun", "Fire") == "pure"
    assert braid("Pluto", "Fire") == "outer lord"
    assert braid("Sun", "Earth") is None
    assert all(braid(b, "Earth") != "pure" for b in STREAMS)  # Earth: no pure carrier
    # Felt banding: the ratified Gut-room judgment call
    assert felt_volume(5, 0) == "peopled"
    assert felt_volume(6, 5) == "crowded"
    assert felt_volume(2, 1) == "thin"
    assert felt_volume(0, 0) == "empty"
    # Full-chart regression: the ratified pull's element A totals (stars added
    # separately: Algol->Earth +2, Deneb->Air +2 => 34 / 19 / 16 / 15).
    P = [("Sun", 286.5040), ("Moon", 273.9814), ("Mercury", 305.3622),
         ("Venus", 265.1002), ("Mars", 23.2261), ("Jupiter", 56.4017),
         ("Saturn", 276.2806), ("Uranus", 272.1014), ("Neptune", 280.1428),
         ("Pluto", 224.7017), ("True North Node", 335.9610),
         ("True South Node", 155.9610), ("Mean North Node", 337.4790),
         ("Mean South Node", 157.4790), ("True Lilith", 158.3075),
         ("Black Moon Lilith", 176.3712), ("Chiron", 93.4837),
         ("Pholus", 68.5494), ("Ceres", 357.0637), ("Pallas", 321.0213),
         ("Juno", 160.5258), ("Vesta", 238.9148), ("Ascendant", 78.8923),
         ("Descendant", 258.8923), ("MC", 327.7993), ("IC", 147.7993),
         ("Lot of Fortune", 66.3697), ("Lot of Spirit", 91.4149),
         ("Lot of Eros", 252.5776), ("Lot of Necessity", 199.8998),
         ("Lot of Courage", 122.0360), ("Lot of Victory", 43.8791),
         ("Lot of Nemesis", 288.8032)]
    A, B = company_scores(P, "Gemini")
    assert sum(A["Earth"].values()) + 2 == 34
    assert sum(A["Air"].values()) + 2 == 19
    assert sum(A["Fire"].values()) == 16
    assert sum(A["Water"].values()) == 15
    assert sum(v for c in B["Earth"].values() for v in c.values()) + 2 == 20
    assert sum(v for c in B["Fire"].values() for v in c.values()) == 12
    assert sum(v for c in B["Air"].values() for v in c.values()) + 2 == 11
    assert sum(v for c in B["Water"].values() for v in c.values()) == 3
    assert B["Earth"]["Gut"] if "Gut" in B["Earth"] else True  # Virgo mints no currency
    assert "Gut" not in B["Earth"]
    print("all checks pass")
