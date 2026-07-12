# LiteLLM Gateway — CT 560 (ai-toolkit)

⟜ Operational detail for the central LLM routing point. The canon's one-liner
("LiteLLM — Central routing point. Change model config here, not per-service") is
correct as a *principle*; this file is the *deployment reality* plus the load-bearing
drift that has to be navigated when editing it. Tight register.

## The pattern (why LiteLLM exists here)

LiteLLM on CT 560 is the stable seam between LLM **consumers** (other LXCs, agents,
UIs) and LLM **backends** (Ollama on gpu-vm, OpenAI, etc.). Consumers point once at the
gateway and never change; when a backend model/host/IP changes, you edit **only** the
gateway config. This is the entire value — do not let consumers hard-wire a backend.

- Consumer-facing endpoint:  `http://10.20.0.153:4000/v1`  (CT 560 LAN IP, OpenAI-compat)
- Auth to the gateway:        `general_settings.master_key` (the `sk-...` in config.yaml)
- Model name:                 whatever `model_name` you define in `model_list`
- Backends are reached by the gateway, not the consumer — so a backend's DHCP IP
  churning only ever requires a one-file edit on CT 560.

## Deployment shape (as found 2026-05)

Docker (the documented exception to native-systemd — already deployed this way; fix in
place, don't re-architect to systemd without a reason):

```
container: litellm  (image ghcr.io/berriai/litellm:main-stable, port 4000:4000)
compose:   /opt/litellm/docker-compose.yml
config:    /opt/litellm/config.yaml         <- the REAL config (model_list lives here)
secrets:   OPENAI_API_KEY / SUPERMEMORY_API_KEY / LITELLM_MASTER_KEY in compose env
command:   --config /app/config.yaml --detailed_debug
```

## ▲ Gotcha — empty-dir mount shadowing the real config

The compose mount drifted to a path that does not exist as a file:

```
volumes:
  - ./litellm_config.yaml:/app/config.yaml:ro   # WRONG: litellm_config.yaml is an empty DIR
```

When a Docker bind-mount source is a directory, Docker mounts the **directory** over
`/app/config.yaml` — the container boots with an empty config dir, not the 567-byte
`config.yaml` sitting right next to it. Symptom: LiteLLM serves nothing useful (no
`model_list`), but the container is "up." Fix: point the mount at the real file and
delete the empty dir.

```
volumes:
  - ./config.yaml:/app/config.yaml:ro          # RIGHT
```

After changing a bind mount you must recreate the container (`docker compose up -d`,
or `down && up -d`) — a restart alone keeps the old mount.

## ▲ Discipline — never retype redacted secrets

The master key and API keys display **redacted** in tool output (`sk-loc...mory`) but
the real bytes are intact on disk. Edit secret-bearing files by `cp` + append, or
targeted patch of non-secret lines — never reconstruct a key from the redacted view, or
you will silently write `sk-loc...mory` as the literal key. Back up first
(`cp config.yaml config.yaml.bak-$(date +%Y%m%d-%H%M%S)`), then append the new block.

## Adding an Ollama backend (worked example: gpu-vm)

Ollama has **no auth** — access is gated purely by network reachability. It binds
`0.0.0.0:11434` by default, so any host that can route to it can use it. Confirm it's
actually serving before wiring the gateway:

```
curl -s http://<ollama-host>:11434/api/tags        # lists models
curl -s http://<ollama-host>:11434/api/version
```

Append to `model_list` in `/opt/litellm/config.yaml`:

```yaml
model_list:
  - model_name: alder
    litellm_params:
      model: ollama_chat/alder-base:latest        # ollama_chat/, not ollama/, for chat models
      api_base: http://<ollama-host>:11434
```

The Ollama host's IP is intentionally NOT pinned in this file — that's the gateway's
job to absorb. The durable facts: gpu-vm = VM 530 (Ubuntu 24.04, netplan `dhcp4: true`,
no DHCP server on the Proxmox host → lease comes from the gateway/router at 10.20.0.1).
Pin its address with a **DHCP reservation on the router**, not a guest-side netplan
static (avoids a network blip on a live GPU box and avoids pool-collision risk).

## Verify end-to-end after any change

```
curl -s http://10.20.0.153:4000/v1/models -H "Authorization: Bearer <master_key>"
curl -s http://10.20.0.153:4000/v1/chat/completions -H "Authorization: Bearer <master_key>" \
  -H "Content-Type: application/json" \
  -d '{"model":"alder","messages":[{"role":"user","content":"ping"}]}'
```
