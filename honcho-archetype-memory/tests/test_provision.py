from harness.provision import run, Summary
from harness.archetype_source import Archetype

ARCHS = [
    Archetype("u1", "the_tower", "The Tower", "the-tower"),
    Archetype("u2", "the_fool", "The Fool", "the-fool"),
]

class FakeAdmin:
    def __init__(self): self.created = []
    def ensure_peer(self, peer_id): self.created.append(peer_id)

def test_mints_for_each_and_skips_existing():
    admin = FakeAdmin()
    store = {"the-fool": {"token": "existing"}}     # already has a token
    minted = []
    def mint(peer_id):
        minted.append(peer_id); return f"tok-{peer_id}"
    summary = run(None, "admin", ARCHS, [], admin, mint, store, "2026-06-16T00:00:00Z")
    assert admin.created == ["the-tower", "the-fool"]   # both peers ensured
    assert minted == ["the-tower"]                       # the-fool skipped
    assert summary.minted == 1 and summary.skipped == 1
    assert summary.created == 2                           # both peers ensured
    assert store["the-tower"]["token"] == "tok-the-tower"

def test_rotate_remints_existing():
    admin = FakeAdmin()
    store = {"the-fool": {"token": "old"}}
    def mint(peer_id): return f"new-{peer_id}"
    summary = run(None, "admin", [ARCHS[1]], [], admin, mint, store, "t", rotate=True)
    assert store["the-fool"]["token"] == "new-the-fool"
    assert summary.minted == 1 and summary.skipped == 0

def test_per_archetype_failure_is_collected_not_fatal():
    admin = FakeAdmin()
    def mint(peer_id):
        raise RuntimeError("mint blew up")
    summary = run(None, "admin", [ARCHS[0]], [], admin, mint, {}, "t")
    assert summary.failed and "the-tower" in summary.failed[0]
    assert summary.created == 1   # peer IS ensured before mint() raises
    assert summary.minted == 0

def test_dry_run_writes_nothing():
    admin = FakeAdmin()
    store = {}
    def mint(peer_id): return "tok"
    summary = run(None, "admin", ARCHS, [], admin, mint, store, "t", dry_run=True)
    assert store == {}                  # untouched
    assert admin.created == []          # no peers created
