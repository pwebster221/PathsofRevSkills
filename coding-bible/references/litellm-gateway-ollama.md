# LiteLLM gateway → Ollama routing (CT 560)

The fleet's LLM aggregation layer. One stable endpoint everything points at; you
re-point the gateway when a backend changes, not every consumer. This is the
intended architecture and it is the right call for fan-in to local models.

## Live facts (verify against /root/CLAUDE.md, which is the infra SOT)

- **CT 560** (`ai-toolkit`, 10.20.0.153) runs LiteLLM in **Docker** (compose),
  image `ghcr.io/berriai/litellm:main-stable`, port **4000**.
- Config + compose live in `/opt/litellm/`:
  - `config.yaml` — the real config (`general_settings.master_key`, `model_list`,
    pass-through endpoints).
  - `docker-compose.yml` — mounts `./config.yaml:/app/config.yaml:ro`, injects
    `OPENAI_API_KEY` / `SUPERMEMORY_API_KEY` / `LITELLM_MASTER_KEY` as env.
- **Stable endpoint for any LXC:** `http://10.20.0.153:4000/v1`, bearer =
  master_key, OpenAI-compatible. Ask for a `model_name` from `model_list`.
- A served model: `alder-1-0` → `ollama_chat/alder-base:latest` on **gpu-vm**
  (VM 530, 10.20.0.121:11434, DHCP-reserved). GPU box also serves `hermes-pat`
  and a `steelpuddles/hermes-4.3-36B` tag — not exposed unless asked.

## ▲ Gotchas (paid for at least once)

- **Empty-dir mount crash-loop.** If `docker-compose.yml` mounts a path that is a
  *directory* into `/app/config.yaml`, LiteLLM dies on boot with
  `IsADirectoryError: Is a directory: '/app/config.yaml'` and Docker shows it as
  "Up N seconds" while it restarts forever. Root cause here was a mount pointing at
  an empty `litellm_config.yaml/` dir instead of the real `config.yaml`. Fix the
  mount to the file, `rmdir` the stray dir, recreate.
- **Boot race on verify.** After `compose up -d`/`--force-recreate`, LiteLLM takes
  ~10–25s to be ready. Curling too early returns empty body → a JSON parse
  traceback that looks like a real failure but is just timing. Check
  `docker logs` for `Set models:` and `/health/readiness` returning
  `{"status":"healthy"}` before trusting a failed completion.
- **`"db":"Not connected"` is normal** for a master-key-only install. It means no
  Postgres → no virtual keys, no spend tracking, no admin UI key management. The
  single `master_key` is the only credential. Fine for trusted private-subnet
  fan-in; not a bug.

## ✦ Secret-preserving edit technique

The master_key and provider keys display **redacted** in tool output
(`sk-loc...mory`) but the real bytes are intact on disk. NEVER retype a key from
the redacted view. Edit by append / path-change only:
- Append `model_list` blocks with a heredoc; the existing file is untouched.
- Rewrite the mount line with a python read/replace asserting the exact old string
  exists (`assert old in s`) — surgical, never regenerates secrets.
- Mask in any echo/log: `sed "s/sk-[A-Za-z0-9._-]*/sk-REDACTED/g"`.
- Back up both files first: `cp -av config.yaml config.yaml.bak-$(date +%Y%m%d-%H%M%S)`.

## Add / rename a model (the routine task)

```yaml
model_list:
  - model_name: alder-1-0          # the string LXCs request
    litellm_params:
      model: ollama_chat/alder-base:latest   # ollama_chat/ for /v1/chat/completions
      api_base: http://10.20.0.121:11434
```
Then `cd /opt/litellm && docker compose up -d --force-recreate`, wait for boot,
verify `/v1/models` lists it and a completion returns. Rename = change `model_name`
only; recreate. Use `assert s.count(old)==1` so a rename can't accidentally hit
`alder-base`.

## When to add the Postgres DB (deferred, by Paul's call)

Co-locating Postgres on CT 560 (a second compose service, same Docker network,
named volume) is the right way to get virtual keys / spend tracking *without* a
cross-LXC runtime dependency — DB and proxy share a lifecycle. But it is a
genuine scope expansion: it needs a real home for the rotated admin master_key
(Vaultwarden, CT 570 — currently unconfigured). Paul deferred this as its own
deliberate task rather than bolt it onto a "serve one model" request. Do not
volunteer the DB unless he asks for per-LXC keys, usage attribution, or a
public surface. Authentik (website SSO) is an IdP, NOT a secret store — it can
gate the admin UI later but the raw key still lives in a secret store.

## ◐ DubTown standards note

This install predates the coding-bible "native systemd over Docker" preference.
It is a working Docker deployment — extend the existing compose pattern, do not
re-architect to systemd mid-task. Flag the drift on record; don't fix unasked.
