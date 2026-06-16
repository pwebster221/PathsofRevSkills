from __future__ import annotations
import json
import os
from pathlib import Path


def load(path: str) -> dict[str, dict]:
    p = Path(path)
    if not p.exists():
        return {}
    return json.loads(p.read_text())


def has_token(store: dict[str, dict], slug: str) -> bool:
    return bool(store.get(slug, {}).get("token"))


def put(store: dict[str, dict], slug: str, peer_id: str, archetype_uuid: str, token: str, minted_at: str) -> None:
    store[slug] = {
        "peer_id": peer_id,
        "archetype_uuid": archetype_uuid,
        "token": token,
        "minted_at": minted_at,
    }


def save(path: str, store: dict[str, dict]) -> None:
    p = Path(path)
    p.write_text(json.dumps(store, indent=2))
    os.chmod(p, 0o600)
