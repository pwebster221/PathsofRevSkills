# Honcho Archetype Memory Provisioning Harness — Design

**Date:** 2026-06-16
**Author:** Paul Webster (Dub Town / Paths of Reverence)
**Status:** Approved for planning

## Purpose

Bootstrap a single Honcho memory store for the Paths of Reverence archetype
system. One agent today hot-swaps between 78 Tarot archetypes (weights,
knowledge, tools, prompts); eventually 78 independent models. Honcho is the
shared memory layer, partitioned so each archetype can read and write only its
own accumulated memory.

This harness provisions that layer: it creates one Honcho peer per archetype and
mints a peer-scoped credential for each, so the runtime agent can authenticate
as a single archetype and be cryptographically confined to that archetype's
memory.

## Verified Foundations

These were confirmed against current Honcho source and docs before designing:

- **Scoped JWTs exist.** Honcho authentication uses JWTs that can be scoped to
  the workspace, peer, or session level. A peer-scoped token grants access only
  to that peer.
- **Minting tool.** `scripts/generate_jwt.py` in the honcho repo mints scoped
  tokens. Relevant flags: `--admin`, `--workspace/-w`, `--peer/-p`,
  `--session/-s`, `--expires/-e`, `--print-only`. Peer scoping requires a
  workspace. Omitting `--expires` produces a non-expiring token.
- **Enforcement is a separate switch.** Scoped keys are only enforced when the
  server runs with `AUTH_USE_AUTH=true` and `AUTH_JWT_SECRET` set. With auth
  disabled (the local-dev default), every token can read everything. The harness
  must treat auth-enabled as a hard precondition.
- **Self-host.** `docker compose up` against the cloned honcho repo; SDK points
  at `http://localhost:8000` (or `HONCHO_URL`).
- **Idempotent peers.** `client.peer(id)` is get-or-create; re-runs do not
  duplicate.
- **Memory model (for later milestones, not this harness).** Knowledge enters a
  peer either as conclusions/observations written directly about the peer, or as
  session messages processed by the background deriver into representations.
  Queried back via the peer chat/dialectic endpoint. The deriver requires LLM API
  keys in the honcho `.env`.
  - **Decided:** the next milestone uses **session messages** (deriver-formed
    representations), not direct conclusions — archetype memory should *emerge*
    from reasoning over interaction, not be hand-asserted. Implication for the
    harness: the self-hosted honcho `.env` must have an LLM API key configured
    (`LLM_ANTHROPIC_API_KEY` / `LLM_OPENAI_API_KEY` / `LLM_GEMINI_API_KEY`) so the
    deriver is functional when that milestone arrives. The harness should warn (not
    fail) if no LLM key is detected, since it's not needed for provisioning itself.

## Decisions

| Decision | Choice | Rationale |
|---|---|---|
| Deployment | Self-host via Docker | Data sovereignty over querent data; full control. |
| Language / SDK | Python (`honcho`) | Matches the ML/MCP stack. |
| Isolation model | One workspace, 78 peers, 78 peer-scoped JWTs | Single store to query; per-archetype confinement via key scope. |
| Key minting | Shell out to `scripts/generate_jwt.py` | Canonical signer; no crypto/secret handling in our code; repo is already present for self-host. |
| Archetype source | solar-mcp HTTP API (configurable URL) + baked snapshot fallback | "Pull live" against the source of truth, but unblocked today and resilient if the service is down. |
| Anomaly policy | Dedupe by UUID + loud warning, continue | Keeps provisioning moving while surfacing solar-mcp data bugs. |
| Key expiry | Non-expiring (omit `--expires`) | Simplest for self-hosted dev; revisit before broad prod. |
| Querent peer | Out of scope | Created at runtime when a real person appears, not at provisioning. |

## Architecture

```
solar-mcp (HTTP)            honcho repo (self-host)
   │  list archetypes          │  scripts/generate_jwt.py
   ▼                           ▼
archetype_source ──► provision.py ──► honcho_admin ──► Honcho server (auth ON)
   (clean/dedupe)      (orchestrate)   (peers)            workspace: paths-of-reverence
                            │                                 ├─ peer: the-fool
                            ▼                                 ├─ peer: the-tower
                       key_minter ──► generate_jwt.py         └─ … 78 peers
                            │
                            ▼
                       keystore ──► archetype_keys.json (gitignored)
```

- **Workspace:** `paths-of-reverence` (single store).
- **Peers:** one per archetype, ID derived from the immutable `slug`
  (`the_tower` → `the-tower`). Never derived from `number` (demonstrably
  scrambled in source) or display `name` (Cups/Chalices drift).
- **Admin token:** used only by the harness for create/mint operations.
- **Peer-scoped tokens:** the runtime credentials, one per archetype.
- **Keystore:** `archetype_keys.json`, gitignored, maps
  `slug → {peer_id, archetype_uuid, scoped_token, minted_at}`.

## Components

Each has one job and is testable in isolation.

1. **`config.py`** — loads and validates env: `HONCHO_BASE_URL`,
   `HONCHO_REPO_PATH`, `WORKSPACE_ID`, `SOLAR_MCP_URL` (+ auth), `KEYSTORE_PATH`.
   Fails fast with a clear message on anything missing.

2. **`archetype_source.py`** — returns clean archetype records. Pluggable
   backend: `HttpBackend` (calls `SOLAR_MCP_URL`) and `SnapshotBackend` (reads a
   versioned `archetypes_snapshot.json` baked from the 2026-06-16 pull). Owns:
   dedupe by UUID, slug→peer-id normalization, post-dedupe count assertion,
   anomaly collection. HTTP backend falls back to snapshot on failure (logged).

3. **`honcho_admin.py`** — thin wrapper over the Honcho Python SDK using the
   admin token: assert workspace, get-or-create peer. Asserts the target server
   has auth enabled before doing anything (probe an authenticated endpoint with
   and without a token).

4. **`key_minter.py`** — subprocess call to
   `{HONCHO_REPO_PATH}/scripts/generate_jwt.py --workspace <ws> --peer <peer_id>
   --print-only` (no `--expires`). Captures stdout token; raises on non-zero exit.

5. **`keystore.py`** — read/write `archetype_keys.json` (0600 perms). Skip-if-present
   unless `--rotate`. Records `minted_at` (timestamp passed in, not generated
   inside any pure function, to keep functions testable).

6. **`provision.py`** — CLI orchestrator. Flags: `--dry-run` (no writes),
   `--rotate` (re-mint existing), `--limit N` (subset for testing). Flow below.

## Data Flow

1. Load + validate config.
2. `honcho_admin.assert_auth_enabled()` — refuse to run if auth is off.
3. `archetype_source.fetch()` → clean records + anomaly list. Warn on anomalies.
4. Assert/confirm workspace `paths-of-reverence`.
5. For each archetype: get-or-create peer → (skip if keystore has token and not
   `--rotate`, else mint scoped token) → record in keystore. Per-archetype
   failures are collected, not fatal.
6. Print summary: created / skipped / rotated / failed / anomalies.

## Error Handling

- **Auth off** → hard stop before any provisioning. This is the precondition
  that makes isolation real.
- **Missing config** → fail fast with the specific missing key named.
- **solar-mcp unreachable** → fall back to snapshot, log loudly, continue.
- **Anomalies (dup UUID, count ≠ 78)** → dedupe, warn, continue.
- **Per-archetype create/mint failure** → collect, continue, report at end with
  non-zero exit if any failed.

## Testing

- **Unit — `archetype_source`:** fixture containing the real anomalies (duplicate
  Magician UUID, scrambled `number`s, Cups/Chalices drift). Assert: dedupe to 78,
  peer IDs derived from slug, anomalies reported.
- **Unit — `key_minter`:** mock subprocess; assert correct flags, token capture,
  error on non-zero exit.
- **Unit — `keystore`:** round-trip, skip-if-present, rotate, file perms.
- **Integration:** local auth-enabled Honcho + `--limit 3`. Provision 3 peers,
  then assert isolation directly — archetype A's scoped token can read A's peer
  and is **rejected** reading archetype B's peer. This is the test that proves
  the entire premise.

## Out of Scope (Future Milestones)

- Querent peer creation and the querent's shared/representation model.
- Writing/seeding archetype knowledge (decided: via **session messages** →
  deriver representations; built in the next milestone).
- The runtime agent that loads a key and "wears" an archetype.
- Cross-archetype synthesis at the admin level.
- Migration from self-host to managed.

## Open Items to Confirm at Implementation

- Exact solar-mcp HTTP base URL (`solar.dubtown-server.us` vs `sacredjourney.io`)
  and its auth scheme. Snapshot fallback covers the gap until confirmed.
- Whether Honcho peer IDs accept underscores (would let us use slugs verbatim);
  default plan normalizes `_`→`-`.
