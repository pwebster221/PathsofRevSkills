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
    a_admin.peer("the-tower")
    a_admin.peer("the-hierophant")

    tower_tok = mint_peer_token(REPO, WS, "the-tower")
    tower_client = _client(tower_tok)

    # The Tower's own peer is reachable with its scoped token.
    tower_client.peer("the-tower").chat("test")     # should not raise auth error

    # The Tower's token must be REJECTED reading The Hierophant.
    with pytest.raises(Exception) as exc:
        tower_client.peer("the-hierophant").chat("test")
    assert any(w in str(exc.value).lower() for w in ("unauth", "forbidden", "401", "403"))
