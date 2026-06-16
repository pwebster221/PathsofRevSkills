# Honcho Archetype Provisioning Harness Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Python CLI harness that provisions one Honcho peer per Tarot archetype in a single workspace and mints a peer-scoped JWT for each, so a runtime agent authenticating as one archetype is cryptographically confined to that archetype's memory.

**Architecture:** Six focused modules — `config`, `archetype_source`, `honcho_admin`, `key_minter`, `keystore`, `provision` (CLI). The archetype list is pulled live from solar-mcp's HTTP API with a cached snapshot fallback, cleaned (dedupe-by-UUID, slug-derived peer IDs, anomaly reporting), then each archetype gets a get-or-create peer and a non-expiring peer-scoped token minted by shelling out to Honcho's canonical `scripts/generate_jwt.py`.

**Tech Stack:** Python 3.11+, `honcho` (Python SDK), `httpx`, `python-dotenv`, `pytest`. Self-hosted Honcho via Docker (`http://localhost:8000`).

## Global Constraints

- Target Honcho server MUST run with `AUTH_USE_AUTH=true` and `AUTH_JWT_SECRET` set; the harness refuses to run otherwise. (Verbatim env names.)
- Workspace ID: `paths-of-reverence`.
- Peer IDs derive ONLY from the immutable `slug` (normalize `_`→`-`). Never from `number` (scrambled in source) or display `name` (Cups/Chalices drift).
- Keys are non-expiring: never pass `--expires` to `generate_jwt.py`.
- Key minting shells out to `{HONCHO_REPO_PATH}/scripts/generate_jwt.py`; no JWT signing in our code.
- Anomalies (duplicate UUIDs, post-dedupe count ≠ 78): dedupe, warn loudly, continue.
- Keystore file `archetype_keys.json` is gitignored and written with `0600` perms.
- All new code lives under `honcho-archetype-memory/`.

---

### Task 1: Project scaffold + config loader

**Files:**
- Create: `honcho-archetype-memory/pyproject.toml`
- Create: `honcho-archetype-memory/.env.example`
- Create: `honcho-archetype-memory/.gitignore`
- Create: `honcho-archetype-memory/harness/__init__.py`
- Create: `honcho-archetype-memory/harness/config.py`
- Test: `honcho-archetype-memory/tests/test_config.py`

**Interfaces:**
- Produces: `load_config(env: Mapping[str,str]) -> Config` where `Config` is a frozen dataclass with fields `honcho_base_url: str`, `honcho_repo_path: str`, `workspace_id: str`, `solar_mcp_url: str`, `solar_mcp_token: str | None`, `keystore_path: str`, `snapshot_path: str`. Raises `ConfigError(msg)` naming the first missing required key.

- [ ] **Step 1: Write the failing test**

```python
# honcho-archetype-memory/tests/test_config.py
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd honcho-archetype-memory && python -m pytest tests/test_config.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'harness.config'`

- [ ] **Step 3: Write the scaffold files**

```toml
# honcho-archetype-memory/pyproject.toml
[project]
name = "honcho-archetype-memory"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = ["honcho-ai", "httpx>=0.27", "python-dotenv>=1.0"]

[project.optional-dependencies]
dev = ["pytest>=8.0"]

[tool.pytest.ini_options]
pythonpath = ["."]
```

```gitignore
# honcho-archetype-memory/.gitignore
archetype_keys.json
.env
__pycache__/
*.pyc
.venv/
```

```bash
# honcho-archetype-memory/.env.example
HONCHO_BASE_URL=http://localhost:8000
HONCHO_REPO_PATH=/absolute/path/to/cloned/honcho
WORKSPACE_ID=paths-of-reverence
SOLAR_MCP_URL=https://solar.dubtown-server.us
# SOLAR_MCP_TOKEN=          # set if solar-mcp requires auth
# KEYSTORE_PATH=archetype_keys.json
# SNAPSHOT_PATH=harness/data/archetypes_snapshot.json
```

```python
# honcho-archetype-memory/harness/__init__.py
```

```python
# honcho-archetype-memory/harness/config.py
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd honcho-archetype-memory && python -m pytest tests/test_config.py -v`
Expected: 3 passed

- [ ] **Step 5: Commit**

```bash
git add honcho-archetype-memory/
git commit -m "feat(honcho): project scaffold + config loader"
```

---

### Task 2: Archetype cleaning (dedupe, normalize, anomaly report)

This is the core data-integrity layer. It must turn the messy live payload (79 rows incl. a duplicate Magician UUID, scrambled `number`s) into a clean, deduped list of 78 with stable slug-derived peer IDs, and surface anomalies.

**Files:**
- Create: `honcho-archetype-memory/harness/archetype_source.py` (cleaning portion)
- Create: `honcho-archetype-memory/tests/fixtures/raw_archetypes_anomalous.json`
- Test: `honcho-archetype-memory/tests/test_archetype_source.py`

**Interfaces:**
- Produces: `@dataclass(frozen=True) Archetype(uuid: str, slug: str, name: str, peer_id: str)`.
- Produces: `clean(raw: list[dict]) -> tuple[list[Archetype], list[str]]` returning `(archetypes, anomalies)`. Dedupes by `uuid` (first wins), derives `peer_id = slug.replace("_","-")`, and appends a human-readable anomaly string for each dropped duplicate and when `len(archetypes) != 78`.
- Produces: `EXPECTED_COUNT = 78`.

- [ ] **Step 1: Write the failing test**

```python
# honcho-archetype-memory/tests/test_archetype_source.py
import json
from pathlib import Path
from harness.archetype_source import clean, Archetype, EXPECTED_COUNT

FIXTURE = Path(__file__).parent / "fixtures" / "raw_archetypes_anomalous.json"

def _raw():
    return json.loads(FIXTURE.read_text())["archetypes"]

def test_dedupes_duplicate_uuid():
    cleaned, anomalies = clean(_raw())
    uuids = [a.uuid for a in cleaned]
    assert len(uuids) == len(set(uuids))                      # no dup UUIDs
    assert any("duplicate" in a.lower() for a in anomalies)   # reported

def test_peer_id_from_slug_not_number_or_name():
    cleaned, _ = clean(_raw())
    by_slug = {a.slug: a for a in cleaned}
    assert by_slug["the_tower"].peer_id == "the-tower"
    # Cups/Chalices name drift must not leak into peer_id
    assert by_slug["knight_of_chalices"].peer_id == "knight-of-chalices"

def test_count_mismatch_is_reported_not_fatal():
    cleaned, anomalies = clean(_raw())   # fixture intentionally != 78
    assert cleaned                       # still returns the clean set
    assert any(str(EXPECTED_COUNT) in a for a in anomalies)
```

- [ ] **Step 2: Create the fixture (real anomalies, trimmed)**

```json
// honcho-archetype-memory/tests/fixtures/raw_archetypes_anomalous.json
{
  "archetypes": [
    {"id": "9387696b-c7c0-4926-ba55-6e599743601d", "name": "The Magician", "slug": "the_magician", "cardType": "major", "number": 1},
    {"id": "9387696b-c7c0-4926-ba55-6e599743601d", "name": "The Magician", "slug": "the_magician", "cardType": "major", "number": 1},
    {"id": "4d07f306-cb53-4c89-bfbc-974d9fe01f1b", "name": "The Tower", "slug": "the_tower", "cardType": "major", "number": 7},
    {"id": "74d15cab-b538-430d-940a-2d0af0918632", "name": "The Sun", "slug": "the_sun", "cardType": "major", "number": 2},
    {"id": "78a50c83-8828-4fd6-819a-30398c1b62d8", "name": "Knight of Cups", "slug": "knight_of_chalices", "cardType": "court", "number": null}
  ],
  "total": 5
}
```

- [ ] **Step 3: Run test to verify it fails**

Run: `cd honcho-archetype-memory && python -m pytest tests/test_archetype_source.py -v`
Expected: FAIL — `ImportError: cannot import name 'clean'`

- [ ] **Step 4: Implement the cleaning layer**

```python
# honcho-archetype-memory/harness/archetype_source.py
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
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `cd honcho-archetype-memory && python -m pytest tests/test_archetype_source.py -v`
Expected: 3 passed

- [ ] **Step 6: Commit**

```bash
git add honcho-archetype-memory/harness/archetype_source.py honcho-archetype-memory/tests/
git commit -m "feat(honcho): archetype cleaning with dedupe + anomaly reporting"
```

---

### Task 3: Archetype source backends (HTTP live + snapshot fallback)

**Files:**
- Modify: `honcho-archetype-memory/harness/archetype_source.py` (add backends + `fetch`)
- Create: `honcho-archetype-memory/harness/data/archetypes_snapshot.json` (seed)
- Test: `honcho-archetype-memory/tests/test_archetype_backends.py`

**Interfaces:**
- Consumes: `clean()`, `Archetype` from Task 2; `Config` from Task 1.
- Produces: `fetch(cfg: Config, http_get=...) -> tuple[list[Archetype], list[str]]`. Tries the HTTP backend at `cfg.solar_mcp_url`; on any exception logs a warning, reads `cfg.snapshot_path`, and cleans that. On HTTP success it also writes the raw payload to `cfg.snapshot_path` (cache-on-success). `http_get` is injectable for testing (defaults to an httpx call).
- Produces: `RAW_KEY = "archetypes"` (the list key in solar-mcp's JSON).

- [ ] **Step 1: Write the failing test**

```python
# honcho-archetype-memory/tests/test_archetype_backends.py
import json
from pathlib import Path
from harness.archetype_source import fetch
from harness.config import load_config

def _cfg(tmp_path):
    snap = tmp_path / "snap.json"
    snap.write_text(json.dumps({"archetypes": [
        {"id": "u1", "name": "The Tower", "slug": "the_tower", "cardType": "major", "number": 7}
    ]}))
    return load_config({
        "HONCHO_BASE_URL": "http://localhost:8000",
        "HONCHO_REPO_PATH": "/repos/honcho",
        "SOLAR_MCP_URL": "https://example.invalid",
        "SNAPSHOT_PATH": str(snap),
    })

def test_http_success_caches_snapshot(tmp_path):
    cfg = _cfg(tmp_path)
    payload = {"archetypes": [
        {"id": "u1", "name": "The Tower", "slug": "the_tower", "cardType": "major", "number": 7},
        {"id": "u2", "name": "The Fool", "slug": "the_fool", "cardType": "major", "number": 0},
    ]}
    def fake_get(url, token):  # injected
        return payload
    arch, _ = fetch(cfg, http_get=fake_get)
    assert {a.slug for a in arch} == {"the_tower", "the_fool"}
    # cached to snapshot
    assert len(json.loads(Path(cfg.snapshot_path).read_text())["archetypes"]) == 2

def test_falls_back_to_snapshot_on_http_error(tmp_path):
    cfg = _cfg(tmp_path)
    def boom(url, token):
        raise ConnectionError("solar-mcp down")
    arch, anomalies = fetch(cfg, http_get=boom)
    assert [a.slug for a in arch] == ["the_tower"]            # from seed snapshot
    assert any("fallback" in a.lower() for a in anomalies)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd honcho-archetype-memory && python -m pytest tests/test_archetype_backends.py -v`
Expected: FAIL — `ImportError: cannot import name 'fetch'`

- [ ] **Step 3: Implement backends**

```python
# append to honcho-archetype-memory/harness/archetype_source.py
import json
import logging
from pathlib import Path

logger = logging.getLogger("harness.archetype_source")
RAW_KEY = "archetypes"


def _http_get(url: str, token: str | None) -> dict:
    import httpx
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    resp = httpx.get(url.rstrip("/") + "/archetypes", headers=headers, timeout=30.0)
    resp.raise_for_status()
    return resp.json()


def fetch(cfg, http_get=_http_get) -> tuple[list[Archetype], list[str]]:
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
```

- [ ] **Step 4: Create the seed snapshot**

Seed with the 2026-06-16 pull. Minimal viable seed (the harness will overwrite it on first successful live pull via cache-on-success):

```json
// honcho-archetype-memory/harness/data/archetypes_snapshot.json
{
  "archetypes": [
    {"id": "4d07f306-cb53-4c89-bfbc-974d9fe01f1b", "name": "The Tower", "slug": "the_tower", "cardType": "major", "number": 7}
  ],
  "total": 1
}
```

Note in a code comment that this seed is intentionally minimal and is replaced wholesale on the first successful live pull. (Full 78 will populate automatically once `SOLAR_MCP_URL` is correct.)

- [ ] **Step 5: Run tests to verify they pass**

Run: `cd honcho-archetype-memory && python -m pytest tests/test_archetype_backends.py -v`
Expected: 2 passed

- [ ] **Step 6: Commit**

```bash
git add honcho-archetype-memory/harness/archetype_source.py honcho-archetype-memory/harness/data/ honcho-archetype-memory/tests/test_archetype_backends.py
git commit -m "feat(honcho): live HTTP backend with snapshot fallback + cache-on-success"
```

---

### Task 4: Key minter (shell out to generate_jwt.py)

**Files:**
- Create: `honcho-archetype-memory/harness/key_minter.py`
- Test: `honcho-archetype-memory/tests/test_key_minter.py`

**Interfaces:**
- Consumes: `Config.honcho_repo_path`, `Config.workspace_id`.
- Produces: `mint_peer_token(honcho_repo_path: str, workspace_id: str, peer_id: str, runner=subprocess.run) -> str`. Builds `["python", "scripts/generate_jwt.py", "--workspace", ws, "--peer", peer_id, "--print-only"]`, runs with `cwd=honcho_repo_path`, returns stripped stdout. Raises `MintError` on non-zero exit (message includes stderr). No `--expires` (non-expiring per global constraints).

- [ ] **Step 1: Write the failing test**

```python
# honcho-archetype-memory/tests/test_key_minter.py
import subprocess
import pytest
from harness.key_minter import mint_peer_token, MintError

class _Result:
    def __init__(self, rc, out="", err=""):
        self.returncode, self.stdout, self.stderr = rc, out, err

def test_builds_correct_command_and_returns_token():
    captured = {}
    def fake_run(cmd, cwd, capture_output, text):
        captured["cmd"], captured["cwd"] = cmd, cwd
        return _Result(0, out="  the.jwt.token  \n")
    token = mint_peer_token("/repos/honcho", "paths-of-reverence", "the-tower", runner=fake_run)
    assert token == "the.jwt.token"
    assert captured["cwd"] == "/repos/honcho"
    assert captured["cmd"][1].endswith("generate_jwt.py")
    assert "--peer" in captured["cmd"] and "the-tower" in captured["cmd"]
    assert "--workspace" in captured["cmd"] and "paths-of-reverence" in captured["cmd"]
    assert "--expires" not in captured["cmd"]   # non-expiring

def test_raises_on_nonzero_exit():
    def fake_run(cmd, cwd, capture_output, text):
        return _Result(1, err="bad secret")
    with pytest.raises(MintError) as exc:
        mint_peer_token("/repos/honcho", "ws", "p", runner=fake_run)
    assert "bad secret" in str(exc.value)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd honcho-archetype-memory && python -m pytest tests/test_key_minter.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'harness.key_minter'`

- [ ] **Step 3: Implement the minter**

```python
# honcho-archetype-memory/harness/key_minter.py
from __future__ import annotations
import os
import subprocess


class MintError(RuntimeError):
    """Raised when generate_jwt.py fails to mint a token."""


def mint_peer_token(honcho_repo_path: str, workspace_id: str, peer_id: str, runner=subprocess.run) -> str:
    script = os.path.join("scripts", "generate_jwt.py")
    cmd = ["python", script, "--workspace", workspace_id, "--peer", peer_id, "--print-only"]
    result = runner(cmd, cwd=honcho_repo_path, capture_output=True, text=True)
    if result.returncode != 0:
        raise MintError(f"generate_jwt.py failed for peer '{peer_id}': {result.stderr.strip()}")
    return result.stdout.strip()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd honcho-archetype-memory && python -m pytest tests/test_key_minter.py -v`
Expected: 2 passed

- [ ] **Step 5: Commit**

```bash
git add honcho-archetype-memory/harness/key_minter.py honcho-archetype-memory/tests/test_key_minter.py
git commit -m "feat(honcho): peer-scoped key minter via generate_jwt.py"
```

---

### Task 5: Keystore (read/write/skip/rotate, 0600 perms)

**Files:**
- Create: `honcho-archetype-memory/harness/keystore.py`
- Test: `honcho-archetype-memory/tests/test_keystore.py`

**Interfaces:**
- Produces: `load(path: str) -> dict[str, dict]` (empty dict if file absent).
- Produces: `has_token(store: dict, slug: str) -> bool`.
- Produces: `put(store: dict, slug: str, peer_id: str, archetype_uuid: str, token: str, minted_at: str) -> None` (mutates `store`).
- Produces: `save(path: str, store: dict) -> None` — writes JSON and `chmod 0600`.

- [ ] **Step 1: Write the failing test**

```python
# honcho-archetype-memory/tests/test_keystore.py
import os
import stat
from harness import keystore

def test_round_trip_and_perms(tmp_path):
    path = str(tmp_path / "keys.json")
    store = keystore.load(path)                       # absent -> {}
    assert store == {}
    keystore.put(store, "the-tower", "the-tower", "uuid-1", "tok", "2026-06-16T00:00:00Z")
    keystore.save(path, store)
    reloaded = keystore.load(path)
    assert reloaded["the-tower"]["token"] == "tok"
    assert reloaded["the-tower"]["peer_id"] == "the-tower"
    mode = stat.S_IMODE(os.stat(path).st_mode)
    assert mode == 0o600

def test_has_token(tmp_path):
    store = {}
    assert not keystore.has_token(store, "the-fool")
    keystore.put(store, "the-fool", "the-fool", "u", "t", "2026-06-16T00:00:00Z")
    assert keystore.has_token(store, "the-fool")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd honcho-archetype-memory && python -m pytest tests/test_keystore.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'harness.keystore'`

- [ ] **Step 3: Implement the keystore**

```python
# honcho-archetype-memory/harness/keystore.py
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd honcho-archetype-memory && python -m pytest tests/test_keystore.py -v`
Expected: 2 passed

- [ ] **Step 5: Commit**

```bash
git add honcho-archetype-memory/harness/keystore.py honcho-archetype-memory/tests/test_keystore.py
git commit -m "feat(honcho): keystore with skip/rotate and 0600 perms"
```

---

### Task 6: Honcho admin wrapper (auth-enabled assertion + peer get-or-create)

**Files:**
- Create: `honcho-archetype-memory/harness/honcho_admin.py`
- Test: `honcho-archetype-memory/tests/test_honcho_admin.py`

**Interfaces:**
- Consumes: `Config`.
- Produces: `assert_auth_enabled(base_url: str, workspace_id: str, client_factory=...) -> None`. Builds a client with a deliberately invalid token and makes one authenticated call (`list(client.peers())`); if it does NOT raise, raises `AuthDisabledError`. Connection failures (server unreachable) re-raise as `RuntimeError`.
- Produces: `class HonchoAdmin` wrapping a real `Honcho` client (admin token); method `ensure_peer(peer_id: str) -> None` (get-or-create via `self.client.peer(peer_id)`).

**Note for implementer:** the exact exception class the SDK raises on 401 is confirmed at runtime. The probe treats *any* exception whose string/status indicates auth (401/403/"unauth") as "auth enabled," and re-raises connection errors. Keep the predicate in one helper `_looks_like_auth_error(exc)` so it's easy to tighten once the class is known.

- [ ] **Step 1: Write the failing test**

```python
# honcho-archetype-memory/tests/test_honcho_admin.py
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd honcho-archetype-memory && python -m pytest tests/test_honcho_admin.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'harness.honcho_admin'`

- [ ] **Step 3: Implement the admin wrapper**

```python
# honcho-archetype-memory/harness/honcho_admin.py
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
    return any(w in str(exc).lower() for w in ("unauth", "forbidden", "invalid token", "401", "403"))


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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd honcho-archetype-memory && python -m pytest tests/test_honcho_admin.py -v`
Expected: 2 passed

- [ ] **Step 5: Commit**

```bash
git add honcho-archetype-memory/harness/honcho_admin.py honcho-archetype-memory/tests/test_honcho_admin.py
git commit -m "feat(honcho): admin wrapper with auth-enabled assertion + ensure_peer"
```

---

### Task 7: Provision CLI orchestrator

**Files:**
- Create: `honcho-archetype-memory/harness/provision.py`
- Test: `honcho-archetype-memory/tests/test_provision.py`

**Interfaces:**
- Consumes: everything above.
- Produces: `run(cfg, admin_token, archetypes, anomalies, admin, mint, store, now, *, dry_run=False, rotate=False) -> Summary` where `Summary` is a dataclass `(created: int, skipped: int, minted: int, failed: list[str], anomalies: list[str])`. Pure orchestration over injected collaborators (`admin.ensure_peer`, `mint(peer_id)`, `store` dict, `now` string) so it is fully unit-testable. Per-archetype exceptions are caught and appended to `failed`.
- Produces: `main(argv=None) -> int` — wires real collaborators from env/config, calls `run`, prints the summary, returns non-zero if `failed` is non-empty.

- [ ] **Step 1: Write the failing test**

```python
# honcho-archetype-memory/tests/test_provision.py
from harness.provision import run, Summary
from harness.archetype_source import Archetype

ARCHS = [
    Archetype("u1", "the_tower", "The Tower", "the-tower"),
    Archetype("u2", "the_fool", "The Fool", "the-fool"),
]

class FakeAdmin:
    def __init__(self): self.created = []
    def ensure_peer(self, peer_id): self.created.append(peer_id)

def test_mints_for_each_and_skips_existing():
    admin = FakeAdmin()
    store = {"the-fool": {"token": "existing"}}     # already has a token
    minted = []
    def mint(peer_id):
        minted.append(peer_id); return f"tok-{peer_id}"
    summary = run(None, "admin", ARCHS, [], admin, mint, store, "2026-06-16T00:00:00Z")
    assert admin.created == ["the-tower", "the-fool"]   # both peers ensured
    assert minted == ["the-tower"]                       # the-fool skipped
    assert summary.minted == 1 and summary.skipped == 1
    assert store["the-tower"]["token"] == "tok-the-tower"

def test_rotate_remints_existing():
    admin = FakeAdmin()
    store = {"the-fool": {"token": "old"}}
    def mint(peer_id): return f"new-{peer_id}"
    summary = run(None, "admin", [ARCHS[1]], [], admin, mint, store, "t", rotate=True)
    assert store["the-fool"]["token"] == "new-the-fool"
    assert summary.minted == 1 and summary.skipped == 0

def test_per_archetype_failure_is_collected_not_fatal():
    admin = FakeAdmin()
    def mint(peer_id):
        raise RuntimeError("mint blew up")
    summary = run(None, "admin", [ARCHS[0]], [], admin, mint, {}, "t")
    assert summary.failed and "the-tower" in summary.failed[0]

def test_dry_run_writes_nothing():
    admin = FakeAdmin()
    store = {}
    def mint(peer_id): return "tok"
    summary = run(None, "admin", ARCHS, [], admin, mint, store, "t", dry_run=True)
    assert store == {}                  # untouched
    assert admin.created == []          # no peers created
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd honcho-archetype-memory && python -m pytest tests/test_provision.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'harness.provision'`

- [ ] **Step 3: Implement the orchestrator**

```python
# honcho-archetype-memory/harness/provision.py
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd honcho-archetype-memory && python -m pytest tests/test_provision.py -v`
Expected: 4 passed

- [ ] **Step 5: Run the full unit suite**

Run: `cd honcho-archetype-memory && python -m pytest -v`
Expected: all tests from Tasks 1–7 pass.

- [ ] **Step 6: Commit**

```bash
git add honcho-archetype-memory/harness/provision.py honcho-archetype-memory/tests/test_provision.py
git commit -m "feat(honcho): provision CLI orchestrator with dry-run/rotate/limit"
```

---

### Task 8: Live isolation integration test (proves the premise)

This task requires a locally running, **auth-enabled** Honcho. It is the test that proves archetype keys are actually confined. Marked `@pytest.mark.integration` so it is skipped by default.

**Files:**
- Create: `honcho-archetype-memory/tests/test_integration_isolation.py`
- Create: `honcho-archetype-memory/docs/RUNBOOK.md`
- Modify: `honcho-archetype-memory/pyproject.toml` (register the `integration` marker)

**Interfaces:**
- Consumes: `mint_peer_token`, real `Honcho` client.

- [ ] **Step 1: Register the marker**

Add to `pyproject.toml` under `[tool.pytest.ini_options]`:

```toml
markers = ["integration: requires a running auth-enabled Honcho (deselect with -m 'not integration')"]
```

- [ ] **Step 2: Write the runbook**

```markdown
# honcho-archetype-memory/docs/RUNBOOK.md
## Bring up auth-enabled Honcho
1. git clone https://github.com/plastic-labs/honcho.git && cd honcho
2. cp docker-compose.yml.example docker-compose.yml && cp .env.template .env
3. In .env set: AUTH_USE_AUTH=true ; AUTH_JWT_SECRET=$(python scripts/generate_jwt_secret.py) ;
   and one LLM key (LLM_ANTHROPIC_API_KEY=...) for the deriver (needed later, not for provisioning).
4. docker compose up
5. Mint an admin token: python scripts/generate_jwt.py --admin --print-only  -> export HONCHO_ADMIN_TOKEN=...

## Provision
cd honcho-archetype-memory ; cp .env.example .env ; edit values ; set HONCHO_REPO_PATH to the honcho clone.
python -m harness.provision --dry-run        # preview
python -m harness.provision --limit 3        # provision a subset
python -m harness.provision                  # full run

## Run the isolation test
HONCHO_BASE_URL=http://localhost:8000 HONCHO_REPO_PATH=/path/to/honcho \
  python -m pytest -m integration -v
```

- [ ] **Step 3: Write the integration test**

```python
# honcho-archetype-memory/tests/test_integration_isolation.py
import os
import pytest
from honcho import Honcho
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
```

- [ ] **Step 4: Run (only when local Honcho is up)**

Run: `cd honcho-archetype-memory && HONCHO_REPO_PATH=/path/to/honcho python -m pytest -m integration -v`
Expected: PASS (Tower reads Tower; Tower rejected on Hierophant). If it FAILS by *not* raising on Hierophant, auth is misconfigured — STOP and fix `AUTH_USE_AUTH`.

- [ ] **Step 5: Verify default suite skips integration**

Run: `cd honcho-archetype-memory && python -m pytest -m "not integration" -v`
Expected: all unit tests pass, integration test deselected.

- [ ] **Step 6: Commit**

```bash
git add honcho-archetype-memory/tests/test_integration_isolation.py honcho-archetype-memory/docs/RUNBOOK.md honcho-archetype-memory/pyproject.toml
git commit -m "test(honcho): live isolation integration test + runbook"
```

---

## Self-Review

**Spec coverage:**
- Auth-enabled precondition → Task 6 (`assert_auth_enabled`) + Task 7 wiring + Task 8 runbook. ✓
- One workspace / 78 peers / peer-scoped JWTs → Tasks 6, 4, 7. ✓
- Shell out to `generate_jwt.py`, non-expiring → Task 4 (no `--expires`). ✓
- solar-mcp live + snapshot fallback + cache-on-success → Task 3. ✓
- Dedupe-by-UUID, slug-derived peer IDs, anomaly report → Task 2. ✓
- Keystore gitignored + 0600 + skip/rotate → Tasks 1 (.gitignore), 5, 7. ✓
- Idempotent peers → Task 6 (`ensure_peer`). ✓
- Isolation proof → Task 8. ✓
- LLM-key warning for deriver (next milestone) → covered in RUNBOOK (Task 8); provisioning itself does not require it, so no separate gate. ✓
- Querent peer / knowledge-seeding / runtime agent → correctly OUT of scope; no tasks. ✓

**Placeholder scan:** No TBD/TODO; every code step has complete code. The seed snapshot (Task 3) is intentionally minimal by design (cache-on-success replaces it), documented as such — not a placeholder. The runtime-exact 401 exception class is handled by a behavioral predicate `_looks_like_auth_error`, not left blank.

**Type consistency:** `Archetype(uuid, slug, name, peer_id)` used identically in Tasks 2, 3, 7. `clean() -> (list[Archetype], list[str])` and `fetch() -> (list[Archetype], list[str])` match. `mint_peer_token(repo, ws, peer_id) -> str` consumed correctly in Task 7's `mint` closure and Task 8. `keystore.put/has_token/load/save` signatures consistent across Tasks 5 and 7. `Summary` fields consistent in Task 7.

No gaps found.
