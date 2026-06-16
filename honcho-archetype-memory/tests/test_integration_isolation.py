import os
import pytest

honcho = pytest.importorskip("honcho")
Honcho = honcho.Honcho

from harness.key_minter import mint_peer_token

pytestmark = pytest.mark.integration

BASE = os.environ.get("HONCHO_BASE_URL", "http://localhost:8000")
REPO = os.environ.get("HONCHO_REPO_PATH", "")
WS = "paths-of-reverence-itest"


def _client(token):
    return Honcho(base_url=BASE, workspace_id=WS, api_key=token, environment="local")


@pytest.mark.skipif(not REPO, reason="HONCHO_REPO_PATH not set")
def test_peer_key_cannot_read_other_peer():
    admin = os.environ["HONCHO_ADMIN_TOKEN"]
    a_admin = _client(admin)
    # peer() is get-or-create: these calls ensure both peers exist server-side
    # before the scoped token is minted, so leg B's rejection below must be an
    # AUTH error (not a missing-peer error) — enforced by the predicate.
    a_admin.peer("the-tower")
    a_admin.peer("the-hierophant")

    tower_tok = mint_peer_token(REPO, WS, "the-tower")
    tower_client = _client(tower_tok)

    # Leg A: The Tower's own peer is reachable with its scoped token.
    # Only fail if Tower's token is wrongly REJECTED on its OWN peer (a real
    # isolation regression); unrelated infra errors (bad LLM key, timeout) skip.
    try:
        tower_client.peer("the-tower").chat("test")
    except Exception as e:
        msg = str(e).lower()
        if any(w in msg for w in ("unauth", "forbidden", "401", "403")):
            pytest.fail(f"Tower's own scoped token was rejected on its OWN peer: {e}")
        pytest.skip(f"Leg A raised a non-auth error (isolation not exercised): {e}")

    # Leg B: The Tower's token must be REJECTED reading The Hierophant.
    with pytest.raises(Exception) as exc:
        tower_client.peer("the-hierophant").chat("test")
    assert any(w in str(exc.value).lower() for w in ("unauth", "forbidden", "401", "403"))
