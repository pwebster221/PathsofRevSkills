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
