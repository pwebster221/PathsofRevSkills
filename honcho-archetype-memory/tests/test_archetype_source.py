import json
from pathlib import Path
from harness.archetype_source import clean, EXPECTED_COUNT

FIXTURE = Path(__file__).parent / "fixtures" / "raw_archetypes_anomalous.json"

def _raw():
    return json.loads(FIXTURE.read_text())["archetypes"]

def test_dedupes_duplicate_uuid():
    cleaned, anomalies = clean(_raw())
    uuids = [a.uuid for a in cleaned]
    assert len(uuids) == len(set(uuids))                      # no dup UUIDs
    assert any("duplicate" in a.lower() for a in anomalies)   # reported

def test_peer_id_from_slug_not_number_or_name():
    cleaned, _ = clean(_raw())
    by_slug = {a.slug: a for a in cleaned}
    assert by_slug["the_tower"].peer_id == "the-tower"
    # Cups/Chalices name drift must not leak into peer_id
    assert by_slug["knight_of_chalices"].peer_id == "knight-of-chalices"

def test_count_mismatch_is_reported_not_fatal():
    cleaned, anomalies = clean(_raw())   # fixture intentionally != 78
    assert cleaned                       # still returns the clean set
    assert any(str(EXPECTED_COUNT) in a for a in anomalies)

def test_malformed_row_is_reported_not_raised():
    raw = [
        {"id": "4d07f306-cb53-4c89-bfbc-974d9fe01f1b", "name": "The Tower", "slug": "the_tower"},
        {"id": "78a50c83-8828-4fd6-819a-30398c1b62d8", "name": "No Slug Card"},  # missing slug
    ]
    cleaned, anomalies = clean(raw)              # must NOT raise
    slugs = [a.slug for a in cleaned]
    assert "the_tower" in slugs                  # good row survives
    assert len(cleaned) == 1                     # malformed row dropped
    assert any("malformed" in a.lower() for a in anomalies)  # reported
