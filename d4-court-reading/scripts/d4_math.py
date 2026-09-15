"""D4 (I.4 Senior Courts — the Court of Change) reference math — PAT-[d4],
rulings of 2026-09-04. Pure functions; self-testing against the canon and the
2026-08-18/09-04 chart data (Paul, Gemini rising)."""

SIGNS = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo",
         "Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]
ELEMENT = {s: ["Fire","Earth","Air","Water"][i%4] for i,s in enumerate(SIGNS)}
MODALITY = {s: ["Cardinal","Fixed","Mutable"][i%3] for i,s in enumerate(SIGNS)}
CENTER = {"Cardinal":"Heart","Fixed":"Head","Mutable":"Gut"}   # eternal
FUNCTION = {"Fire":"Intuition","Earth":"Sensing","Air":"Thinking","Water":"Feeling"}
SUIT_OF = {"Fire":"Wands","Water":"Chalices","Air":"Swords","Earth":"Pentacles"}
RANK_OF_MOD = {"Cardinal":"Queen","Fixed":"Knight","Mutable":"King"}  # entering sign's modality
PERSONA = {"Knight of Wands":"enfp","Knight of Chalices":"enfj","Knight of Swords":"estj","Knight of Pentacles":"estp",
 "Queen of Wands":"intj","Queen of Chalices":"isfp","Queen of Swords":"intp","Queen of Pentacles":"isfj",
 "King of Wands":"entp","King of Chalices":"esfj","King of Swords":"entj","King of Pentacles":"esfp"}

def court_of_cusp(entering_sign):
    """The cusp is named by the entering (majority, two-decan) sign."""
    rank = RANK_OF_MOD[MODALITY[entering_sign]]
    return f"{rank} of {SUIT_OF[ELEMENT[entering_sign]]}"

def span(entering_sign):
    """(operator_decan, substance_decan, result_decan), 1-based D1 decans."""
    i = SIGNS.index(entering_sign)
    leaving = SIGNS[(i-1) % 12]
    op = SIGNS.index(leaving)*3 + 3      # leaving sign's III
    return op, i*3 + 1, i*3 + 2          # entering I, entering II (final decan)

def crossing(entering_sign):
    i = SIGNS.index(entering_sign); leaving = SIGNS[(i-1)%12]
    return dict(leaving=leaving, entering=entering_sign,
        elements=(ELEMENT[leaving], ELEMENT[entering_sign]),
        functions=(FUNCTION[ELEMENT[leaving]], FUNCTION[ELEMENT[entering_sign]]),
        centers=(CENTER[MODALITY[leaving]], CENTER[MODALITY[entering_sign]]),
        modalities=(MODALITY[leaving], MODALITY[entering_sign]))

def relations(entering_sign):
    """7 of 11: challenges(2 perpendicular rank-mates), precedes/succeeds(2),
    empowers(2 same suit), complement(1 across — overrides rank)."""
    i = SIGNS.index(entering_sign)
    peer = lambda k: court_of_cusp(SIGNS[(i+k) % 12])
    return dict(
        challenges=[peer(3), peer(9)],
        precedes=peer(-1), succeeds=peer(1),
        empowers=[peer(4), peer(8)],
        complement=peer(6),
        cannot_see=[peer(2), peer(5), peer(7), peer(10)])

def whole_sign_house(sign, asc):
    return (SIGNS.index(sign)-SIGNS.index(asc)) % 12 + 1

if __name__ == "__main__":
    # Suit anchoring per Book T: Queens cardinal-suited, Knights fixed, Kings mutable.
    assert court_of_cusp("Taurus") == "Knight of Pentacles"
    assert court_of_cusp("Aries") == "Queen of Wands"
    assert court_of_cusp("Gemini") == "King of Swords"
    assert court_of_cusp("Scorpio") == "Knight of Chalices"
    # Every suit performs one elemental shift; every rank one modal shift.
    for s in SIGNS:
        c = crossing(s); court = court_of_cusp(s)
        suit = court.split(" of ")[1]; rank = court.split(" ")[0]
        assert {"Wands":("Water","Fire"),"Chalices":("Air","Water"),
                "Swords":("Earth","Air"),"Pentacles":("Fire","Earth")}[suit] == c["elements"]
        assert {"Knight":("Heart","Head"),"Queen":("Gut","Heart"),
                "King":("Head","Gut")}[rank] == c["centers"]      # eternal centers
    # Spans tile the 36 decans exactly once.
    seen = [d for s in SIGNS for d in span(s)]
    assert sorted(seen) == list(range(1,37)) and span("Taurus") == (3,4,5)
    # Relations: each court sees exactly 7 of 11, and the sets are consistent.
    r = relations("Taurus")
    assert r["challenges"] == ["Knight of Wands","Knight of Swords"]
    assert r["precedes"] == "Queen of Wands" and r["succeeds"] == "King of Swords"
    assert set(r["empowers"]) == {"King of Pentacles","Queen of Pentacles"}
    assert r["complement"] == "Knight of Chalices"
    assert len(r["cannot_see"]) == 4
    # Proof-card stations (Gemini rising): H11 -> H12 crossing.
    assert whole_sign_house("Aries","Gemini") == 11 and whole_sign_house("Taurus","Gemini") == 12
    print("all checks pass")
