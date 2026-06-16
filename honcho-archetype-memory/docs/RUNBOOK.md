# Archetype Memory Provisioning — Runbook

## Bring up auth-enabled Honcho
1. git clone https://github.com/plastic-labs/honcho.git && cd honcho
2. cp docker-compose.yml.example docker-compose.yml && cp .env.template .env
3. In .env set: AUTH_USE_AUTH=true ; AUTH_JWT_SECRET=$(python scripts/generate_jwt_secret.py) ;
   and one LLM key (LLM_ANTHROPIC_API_KEY=...) for the deriver. The LLM key is NOT needed for
   provisioning or for the isolation test itself; it IS needed for the later
   session-message / deriver milestone.
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

## First-live-run validation checklist
These items depend on the real honcho-ai SDK + a live server and could not be
verified in CI. Confirm them the first time you run against live Honcho — they
are the highest-risk assumptions in the harness:

1. SDK method surface for the auth probe. `honcho_admin.assert_auth_enabled`
   probes with `client.peers()` (a list call chosen because it forces a server
   round-trip), while provisioning uses `client.peer(id)` (get-or-create).
   Confirm against honcho-ai that: (a) `peers()` exists and returns 401/403 with
   an invalid token, and (b) `peer(id)` enforces the same auth. If `peers()` is
   absent or doesn't round-trip, switch the probe to whatever call provisioning
   actually uses. If the probe ever raises a non-auth error (e.g. AttributeError),
   it surfaces as "Could not verify auth (server reachable?)" — investigate before
   trusting isolation.

2. Isolation proof strength (test_integration_isolation). Leg A currently does
   `chat("test")` on the archetype's own (possibly empty) peer and only fails on
   an auth-shaped error. On first live run, strengthen leg A to assert a concrete
   successful read of the archetype's OWN seeded data, so leg B's rejection of
   another archetype's peer can't pass for an unrelated reason. If leg B's
   rejection is a not-found (404) rather than an auth error (401/403), the
   assertion correctly fails — investigate, because that means the peer wasn't
   created, not that isolation held.

3. solar-mcp endpoint. Confirm the real base URL (SOLAR_MCP_URL) and that
   `GET {base}/archetypes` returns `{"archetypes": [...]}`. Until confirmed, the
   harness uses the committed seed snapshot via the fallback path (logged loudly).
   `python -m harness.provision --limit 0` validates the auth + fetch path without
   creating any peers.
