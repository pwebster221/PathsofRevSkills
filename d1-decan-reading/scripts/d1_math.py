"""D1 (I.1 Decan Minors) reference math — PAT-[d1].

Pure functions, no I/O. Decans are 1-based (1 = Aries I ... 36 = Pisces III).
Verified against the vault's 36 decan definition files, 2026-08-07.
"""

SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
         "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
ORDINALS = ["I", "II", "III"]

# Golden Dawn pip mapping: sign -> its three pips in ordinal order.
CARDS = {
    1: "Two of Wands", 2: "Three of Wands", 3: "Four of Wands",
    4: "Five of Pentacles", 5: "Six of Pentacles", 6: "Seven of Pentacles",
    7: "Eight of Swords", 8: "Nine of Swords", 9: "Ten of Swords",
    10: "Two of Chalices", 11: "Three of Chalices", 12: "Four of Chalices",
    13: "Five of Wands", 14: "Six of Wands", 15: "Seven of Wands",
    16: "Eight of Pentacles", 17: "Nine of Pentacles", 18: "Ten of Pentacles",
    19: "Two of Swords", 20: "Three of Swords", 21: "Four of Swords",
    22: "Five of Chalices", 23: "Six of Chalices", 24: "Seven of Chalices",
    25: "Eight of Wands", 26: "Nine of Wands", 27: "Ten of Wands",
    28: "Two of Pentacles", 29: "Three of Pentacles", 30: "Four of Pentacles",
    31: "Five of Swords", 32: "Six of Swords", 33: "Seven of Swords",
    34: "Eight of Chalices", 35: "Nine of Chalices", 36: "Ten of Chalices",
}

CHALDEAN = ["Mars", "Sun", "Venus", "Mercury", "Moon", "Saturn", "Jupiter"]
DOMICILE_ELEMENTS = {"Mars": ["Fire", "Water"], "Venus": ["Earth", "Air"],
                     "Mercury": ["Air", "Earth"], "Jupiter": ["Fire", "Water"],
                     "Saturn": ["Earth", "Air"], "Sun": ["Fire"], "Moon": ["Water"]}
SIGN_RULER = {"Aries": "Mars", "Taurus": "Venus", "Gemini": "Mercury", "Cancer": "Moon",
              "Leo": "Sun", "Virgo": "Mercury", "Libra": "Venus", "Scorpio": "Mars",
              "Sagittarius": "Jupiter", "Capricorn": "Saturn", "Aquarius": "Saturn",
              "Pisces": "Jupiter"}
SIGN_ELEMENT = {s: ["Fire", "Earth", "Air", "Water"][i % 4] for i, s in enumerate(SIGNS)}

# Home office: natural lord + element of each whole-sign house.
# The ONLY office admitting modern rulers, and only these three: H8/H11/H12.
NATURAL_LORD = {1: ("Mars", "Fire"), 2: ("Venus", "Earth"), 3: ("Mercury", "Air"),
                4: ("Moon", "Water"), 5: ("Sun", "Fire"), 6: ("Mercury", "Earth"),
                7: ("Venus", "Air"), 8: ("Pluto", "Water"), 9: ("Jupiter", "Fire"),
                10: ("Saturn", "Earth"), 11: ("Uranus", "Air"), 12: ("Neptune", "Water")}

VERB = {3: "recognizes", 6: "supports", 9: "competes",
        12: "reinforces", 15: "aggravates", 18: "challenges"}
HARSH_TO_KIND = [18, 15, 9, 3, 6, 12]  # performance order for movement 3


def decan_of(longitude: float) -> int:
    """Ecliptic longitude (0-360) -> 1-based decan."""
    return int(longitude % 360.0 // 10) + 1


def decan_name(n: int) -> str:
    return f"{SIGNS[(n - 1) // 3]} {ORDINALS[(n - 1) % 3]}"


def sign_of(n: int) -> str:
    return SIGNS[(n - 1) // 3]


def temporal_lord(n: int):
    """Chaldean traveler, clothed in BOTH domicile elements."""
    lord = CHALDEAN[(n - 1) % 7]
    return lord, DOMICILE_ELEMENTS[lord]


def eternal_lord(n: int):
    """Triplicity ascent: I = sign ruler, II = next same-element sign's ruler,
    III = previous. Clothed in the sign's element."""
    sign, ordinal = sign_of(n), (n - 1) % 3
    element = SIGN_ELEMENT[sign]
    ring = [s for s in SIGNS if SIGN_ELEMENT[s] == element]  # zodiac order
    i = ring.index(sign)
    target = [ring[i], ring[(i + 1) % 3], ring[(i - 1) % 3]][ordinal]
    return SIGN_RULER[target], element


def presiding_lord(n: int):
    sign = sign_of(n)
    return SIGN_RULER[sign], SIGN_ELEMENT[sign]


def home_lord(n: int, rising_sign: str):
    """Chart-relative: natural lord of the whole-sign house the decan's sign
    occupies for the given rising sign."""
    house = (SIGNS.index(sign_of(n)) - SIGNS.index(rising_sign)) % 12 + 1
    lord, element = NATURAL_LORD[house]
    return house, lord, element


def ring_relations(n: int, lit: set):
    """(lit_rows harsh->kind as (distance, mate, verb), dark as (mate, card)).
    Ordinal-preserving only; across ordinals, silence. Dark decans are dark."""
    mates = [m for m in range(1, 37) if m != n and (m - 1) % 3 == (n - 1) % 3]
    rows, dark = [], []
    for m in mates:
        d = min(abs(n - m), 36 - abs(n - m))
        (rows if m in lit else dark).append((d, m))
    rows.sort(key=lambda t: HARSH_TO_KIND.index(t[0]))
    return ([(d, m, VERB[d]) for d, m in rows],
            [(m, CARDS[m]) for _, m in sorted(dark, key=lambda t: t[1])])


if __name__ == "__main__":
    # Self-test against ratified facts from the 2026-08-07 performance.
    assert decan_of(150.0) == 16 and CARDS[16] == "Eight of Pentacles"
    assert temporal_lord(34) == ("Saturn", ["Earth", "Air"])
    assert eternal_lord(34) == ("Jupiter", "Water")
    assert home_lord(34, "Gemini") == (10, "Saturn", "Earth")
    assert home_lord(28, "Gemini") == (8, "Pluto", "Water")
    lit = {3, 5, 6, 7, 8, 10, 13, 15, 16, 17, 18, 20, 23, 24,
           26, 27, 28, 29, 31, 33, 34, 36}
    rows, dark = ring_relations(34, lit)
    assert rows[0] == (18, 16, "challenges") and rows[-1] == (12, 10, "reinforces")
    assert len(dark) == 5
    print("all checks pass")
