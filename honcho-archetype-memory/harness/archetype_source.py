from __future__ import annotations
from dataclasses import dataclass
import json
import logging
from pathlib import Path

logger = logging.getLogger("harness.archetype_source")

EXPECTED_COUNT = 78
RAW_KEY = "archetypes"


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
        uuid = row.get("id")
        slug = row.get("slug")
        if not uuid or not slug:
            anomalies.append(f"Skipped malformed row (missing id/slug): {row}")
            continue
        if uuid in seen:
            anomalies.append(f"Dropped duplicate UUID {uuid} ({row.get('name', slug)})")
            continue
        seen.add(uuid)
        out.append(Archetype(uuid=uuid, slug=slug, name=row.get("name", slug), peer_id=_peer_id(slug)))
    if len(out) != EXPECTED_COUNT:
        anomalies.append(f"Expected {EXPECTED_COUNT} archetypes after dedupe, got {len(out)}")
    return out, anomalies


def _http_get(url: str, token: str | None) -> dict:
    import httpx
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    resp = httpx.get(url.rstrip("/") + "/archetypes", headers=headers, timeout=30.0)
    resp.raise_for_status()
    return resp.json()


def fetch(cfg, http_get=_http_get) -> tuple[list[Archetype], list[str]]:
    """Fetch archetypes from live HTTP backend with snapshot fallback.

    Tries live HTTP pull from solar-mcp. On any exception, logs a warning,
    reads the snapshot file, and cleans it. On HTTP success, also writes
    the raw payload to the snapshot file (cache-on-success).

    The seed snapshot is intentionally minimal and is replaced wholesale on
    the first successful live pull. Full 78 will populate automatically once
    SOLAR_MCP_URL is correct.
    """
    try:
        payload = http_get(cfg.solar_mcp_url, cfg.solar_mcp_token)
        raw = payload[RAW_KEY]
        Path(cfg.snapshot_path).parent.mkdir(parents=True, exist_ok=True)
        Path(cfg.snapshot_path).write_text(json.dumps(payload, indent=2))
        cleaned, anomalies = clean(raw)
        return cleaned, anomalies
    except Exception as exc:  # noqa: BLE001 - any live failure -> snapshot
        logger.warning("solar-mcp live fetch failed (%s); using snapshot fallback", exc)
        raw = json.loads(Path(cfg.snapshot_path).read_text())[RAW_KEY]
        cleaned, anomalies = clean(raw)
        anomalies.insert(0, f"Used snapshot fallback ({cfg.snapshot_path}) due to: {exc}")
        return cleaned, anomalies
