from __future__ import annotations
from dataclasses import dataclass

EXPECTED_COUNT = 78


@dataclass(frozen=True)
class Archetype:
    uuid: str
    slug: str
    name: str
    peer_id: str


def _peer_id(slug: str) -> str:
    return slug.strip().replace("_", "-")


def clean(raw: list[dict]) -> tuple[list[Archetype], list[str]]:
    """Dedupe by UUID (first wins), derive peer_id from slug, collect anomalies."""
    seen: set[str] = set()
    out: list[Archetype] = []
    anomalies: list[str] = []
    for row in raw:
        uuid = row["id"]
        slug = row["slug"]
        if uuid in seen:
            anomalies.append(f"Dropped duplicate UUID {uuid} ({row.get('name', slug)})")
            continue
        seen.add(uuid)
        out.append(Archetype(uuid=uuid, slug=slug, name=row.get("name", slug), peer_id=_peer_id(slug)))
    if len(out) != EXPECTED_COUNT:
        anomalies.append(f"Expected {EXPECTED_COUNT} archetypes after dedupe, got {len(out)}")
    return out, anomalies
