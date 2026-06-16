import json
from pathlib import Path

import pytest

from harness.archetype_source import fetch
from harness.config import load_config


def _cfg(tmp_path):
    snap = tmp_path / "snap.json"
    snap.write_text(json.dumps({"archetypes": [
        {"id": "u1", "name": "The Tower", "slug": "the_tower", "cardType": "major", "number": 7}
    ]}))
    return load_config({
        "HONCHO_BASE_URL": "http://localhost:8000",
        "HONCHO_REPO_PATH": "/repos/honcho",
        "SOLAR_MCP_URL": "https://example.invalid",
        "SNAPSHOT_PATH": str(snap),
    })


def test_http_success_caches_snapshot(tmp_path):
    cfg = _cfg(tmp_path)
    payload = {"archetypes": [
        {"id": "u1", "name": "The Tower", "slug": "the_tower", "cardType": "major", "number": 7},
        {"id": "u2", "name": "The Fool", "slug": "the_fool", "cardType": "major", "number": 0},
    ]}
    def fake_get(url, token):  # injected
        return payload
    arch, _ = fetch(cfg, http_get=fake_get)
    assert {a.slug for a in arch} == {"the_tower", "the_fool"}
    # cached to snapshot
    assert len(json.loads(Path(cfg.snapshot_path).read_text())["archetypes"]) == 2


def test_falls_back_to_snapshot_on_http_error(tmp_path):
    cfg = _cfg(tmp_path)
    def boom(url, token):
        raise ConnectionError("solar-mcp down")
    arch, anomalies = fetch(cfg, http_get=boom)
    assert [a.slug for a in arch] == ["the_tower"]            # from seed snapshot
    assert any("fallback" in a.lower() for a in anomalies)


def test_raises_clear_error_when_both_http_and_snapshot_fail(tmp_path):
    cfg = _cfg(tmp_path)
    # Point the snapshot path at a file that does not exist.
    missing = tmp_path / "does_not_exist.json"
    cfg = load_config({
        "HONCHO_BASE_URL": "http://localhost:8000",
        "HONCHO_REPO_PATH": "/repos/honcho",
        "SOLAR_MCP_URL": "https://example.invalid",
        "SNAPSHOT_PATH": str(missing),
    })

    def boom(url, token):
        raise ConnectionError("solar-mcp down")

    with pytest.raises(RuntimeError) as excinfo:
        fetch(cfg, http_get=boom)
    msg = str(excinfo.value)
    assert "solar-mcp down" in msg           # mentions the live failure
    assert str(missing) in msg               # mentions the snapshot path
