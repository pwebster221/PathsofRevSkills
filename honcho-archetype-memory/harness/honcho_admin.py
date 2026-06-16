from __future__ import annotations
import logging

logger = logging.getLogger("harness.honcho_admin")


class AuthDisabledError(RuntimeError):
    """Raised when the Honcho server accepts an invalid token (auth not enforced)."""


def _default_factory(base_url: str, workspace_id: str, api_key: str):
    from honcho import Honcho
    return Honcho(base_url=base_url, workspace_id=workspace_id, api_key=api_key, environment="local")


def _looks_like_auth_error(exc: Exception) -> bool:
    status = getattr(exc, "status_code", None)
    if status in (401, 403):
        return True
    return any(w in str(exc).lower() for w in ("unauth", "forbidden", "invalid token"))


def assert_auth_enabled(base_url: str, workspace_id: str, client_factory=_default_factory) -> None:
    client = client_factory(base_url, workspace_id, "invalid.token.deliberately")
    try:
        list(client.peers())
    except Exception as exc:  # noqa: BLE001
        if _looks_like_auth_error(exc):
            logger.info("Auth is enforced (invalid token rejected).")
            return
        raise RuntimeError(f"Could not verify auth (server reachable?): {exc}") from exc
    raise AuthDisabledError(
        "Honcho accepted an INVALID token: auth is disabled. "
        "Set AUTH_USE_AUTH=true and AUTH_JWT_SECRET on the server before provisioning."
    )


class HonchoAdmin:
    def __init__(self, base_url: str, workspace_id: str, admin_token: str, client_factory=_default_factory):
        self.client = client_factory(base_url, workspace_id, admin_token)

    def ensure_peer(self, peer_id: str) -> None:
        self.client.peer(peer_id)   # get-or-create; idempotent
