import pytest
from harness.config import load_config, ConfigError

BASE_ENV = {
    "HONCHO_BASE_URL": "http://localhost:8000",
    "HONCHO_REPO_PATH": "/repos/honcho",
    "SOLAR_MCP_URL": "https://solar.dubtown-server.us",
}

def test_loads_with_defaults():
    cfg = load_config(BASE_ENV)
    assert cfg.workspace_id == "paths-of-reverence"          # default
    assert cfg.keystore_path.endswith("archetype_keys.json")  # default
    assert cfg.honcho_base_url == "http://localhost:8000"
    assert cfg.solar_mcp_token is None                        # optional

def test_missing_required_key_names_it():
    env = {k: v for k, v in BASE_ENV.items() if k != "HONCHO_REPO_PATH"}
    with pytest.raises(ConfigError) as exc:
        load_config(env)
    assert "HONCHO_REPO_PATH" in str(exc.value)

def test_overrides_workspace():
    cfg = load_config({**BASE_ENV, "WORKSPACE_ID": "custom-ws"})
    assert cfg.workspace_id == "custom-ws"
