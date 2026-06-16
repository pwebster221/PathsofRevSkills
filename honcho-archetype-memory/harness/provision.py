from __future__ import annotations
import argparse
import logging
import os
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone

from . import keystore
from .config import load_config
from .archetype_source import fetch
from .honcho_admin import assert_auth_enabled, HonchoAdmin
from .key_minter import mint_peer_token

logger = logging.getLogger("harness.provision")


@dataclass
class Summary:
    created: int = 0
    skipped: int = 0
    minted: int = 0
    failed: list[str] = field(default_factory=list)
    anomalies: list[str] = field(default_factory=list)


def run(cfg, admin_token, archetypes, anomalies, admin, mint, store, now, *, dry_run=False, rotate=False) -> Summary:
    s = Summary(anomalies=list(anomalies))
    for a in archetypes:
        try:
            if dry_run:
                continue
            admin.ensure_peer(a.peer_id)
            s.created += 1
            if keystore.has_token(store, a.peer_id) and not rotate:
                s.skipped += 1
                continue
            token = mint(a.peer_id)
            keystore.put(store, a.peer_id, a.peer_id, a.uuid, token, now)
            s.minted += 1
        except Exception as exc:  # noqa: BLE001
            s.failed.append(f"{a.peer_id}: {exc}")
    return s


def main(argv=None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description="Provision Honcho peers + scoped keys for all archetypes.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--rotate", action="store_true")
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args(argv)

    cfg = load_config(os.environ)
    admin_token = os.environ.get("HONCHO_ADMIN_TOKEN")
    if not admin_token:
        logger.error("HONCHO_ADMIN_TOKEN is required (mint with generate_jwt.py --admin).")
        return 2

    assert_auth_enabled(cfg.honcho_base_url, cfg.workspace_id)

    archetypes, anomalies = fetch(cfg)
    if args.limit:
        archetypes = archetypes[: args.limit]
    for a in anomalies:
        logger.warning("ANOMALY: %s", a)

    admin = HonchoAdmin(cfg.honcho_base_url, cfg.workspace_id, admin_token)
    store = keystore.load(cfg.keystore_path)
    now = datetime.now(timezone.utc).isoformat()

    def mint(peer_id):
        return mint_peer_token(cfg.honcho_repo_path, cfg.workspace_id, peer_id)

    summary = run(cfg, admin_token, archetypes, anomalies, admin, mint, store, now,
                  dry_run=args.dry_run, rotate=args.rotate)

    if not args.dry_run:
        keystore.save(cfg.keystore_path, store)

    logger.info("Done: created=%d minted=%d skipped=%d failed=%d anomalies=%d",
                summary.created, summary.minted, summary.skipped, len(summary.failed), len(summary.anomalies))
    for f in summary.failed:
        logger.error("FAILED %s", f)
    return 1 if summary.failed else 0


if __name__ == "__main__":
    sys.exit(main())
