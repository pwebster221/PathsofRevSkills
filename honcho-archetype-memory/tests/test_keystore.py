import os
import stat
from harness import keystore

def test_round_trip_and_perms(tmp_path):
    path = str(tmp_path / "keys.json")
    store = keystore.load(path)                       # absent -> {}
    assert store == {}
    keystore.put(store, "the-tower", "the-tower", "uuid-1", "tok", "2026-06-16T00:00:00Z")
    keystore.save(path, store)
    reloaded = keystore.load(path)
    assert reloaded["the-tower"]["token"] == "tok"
    assert reloaded["the-tower"]["peer_id"] == "the-tower"
    assert reloaded["the-tower"]["archetype_uuid"] == "uuid-1"
    assert reloaded["the-tower"]["minted_at"] == "2026-06-16T00:00:00Z"
    mode = stat.S_IMODE(os.stat(path).st_mode)
    assert mode == 0o600

def test_has_token(tmp_path):
    store = {}
    assert not keystore.has_token(store, "the-fool")
    keystore.put(store, "the-fool", "the-fool", "u", "t", "2026-06-16T00:00:00Z")
    assert keystore.has_token(store, "the-fool")
