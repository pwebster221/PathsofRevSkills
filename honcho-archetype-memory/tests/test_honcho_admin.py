import pytest
from harness.honcho_admin import assert_auth_enabled, AuthDisabledError

class _AuthError(Exception):
    status_code = 401

def test_auth_enabled_when_invalid_token_rejected():
    def factory(base_url, workspace_id, api_key):
        class C:
            def peers(self):
                raise _AuthError("Unauthorized")
        return C()
    # should NOT raise: invalid token was rejected => auth is on
    assert_auth_enabled("http://localhost:8000", "ws", client_factory=factory)

def test_raises_when_invalid_token_accepted():
    def factory(base_url, workspace_id, api_key):
        class C:
            def peers(self):
                return iter([])      # accepted invalid token => auth OFF
        return C()
    with pytest.raises(AuthDisabledError):
        assert_auth_enabled("http://localhost:8000", "ws", client_factory=factory)
