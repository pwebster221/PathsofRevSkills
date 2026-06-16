from __future__ import annotations
from dataclasses import dataclass
from collections.abc import Mapping


class ConfigError(RuntimeError):
    """Raised when required configuration is missing or invalid."""


@dataclass(frozen=True)
class Config:
    honcho_base_url: str
    honcho_repo_path: str
    workspace_id: str
    solar_mcp_url: str
    solar_mcp_token: str | None
    keystore_path: str
    snapshot_path: str


_REQUIRED = ("HONCHO_BASE_URL", "HONCHO_REPO_PATH", "SOLAR_MCP_URL")


def load_config(env: Mapping[str, str]) -> Config:
    for key in _REQUIRED:
        if not env.get(key):
            raise ConfigError(f"Missing required config: {key}")
    return Config(
        honcho_base_url=env["HONCHO_BASE_URL"],
        honcho_repo_path=env["HONCHO_REPO_PATH"],
        workspace_id=env.get("WORKSPACE_ID", "paths-of-reverence"),
        solar_mcp_url=env["SOLAR_MCP_URL"],
        solar_mcp_token=env.get("SOLAR_MCP_TOKEN") or None,
        keystore_path=env.get("KEYSTORE_PATH", "archetype_keys.json"),
        snapshot_path=env.get("SNAPSHOT_PATH", "harness/data/archetypes_snapshot.json"),
    )
