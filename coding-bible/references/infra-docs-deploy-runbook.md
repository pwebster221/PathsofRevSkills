# Registry-Driven Infra-Docs Deploy Runbook (CT 850)

Operational detail for the canon's "Registry-driven infra docs" rule. Session-discovered
homelab specifics — NOT a mirror of upstream canon. Safe to edit directly.

The site lives on CT 850 (`infra-docs`, SPI Forum), served by `mkdocs serve` at
`http://10.20.0.160:8000`. Source of truth: `ansible/dubtown-infra/registry/containers.yml`.

## The workflow (canonical order)

1. Edit `registry/containers.yml` — never hand-edit generated docs (they're regenerable).
2. Regenerate: `ansible-playbook playbooks/maintenance/generate_docs.yml`
   (renders VM inventory incl. the per-VM services dropdown, container inventory,
   per-service pages, services index, and `.services_nav.yml`).
   - `generate_docs.yml` is the comprehensive generator. `generate_service_docs.yml`
     is the older/narrower one (service pages + index only). Prefer `generate_docs.yml`.
3. Deploy to CT 850: append `-e deploy=true`. This runs the `mkdocs` role: copies
   docs → recursive ownership pass → restarts the service.

## ▲ Deploy is pathologically slow (~28 min) — do NOT kill it on timeout

The `deploy=true` path runs `file: recurse=true` ownership over the **pct_remote**
connection. Each file is a separate perl→python→MOTD round-trip into CT 850, so it's
O(files) and grinds for ~25-30 min on a ~440-file docs tree. **It is not hung** — it
advances task-by-task (watch `ps aux | grep AnsiballZ`).

- The canon's older note ("pip step hangs; kill + manual pct push") is **misleading
  for this playbook** — the real bottleneck is the ownership recurse, not pip, and
  killing it mid-run leaves the deploy half-done (content copied but `mkdocs` not yet
  restarted → site still serves 404 on the new pages).
- **Correct pattern:** run `deploy=true` as a `terminal(background=true,
  notify_on_complete=true)` job and let it finish. A foreground call will hit the
  600s ceiling and kill the playbook, wasting ~10 min and leaving an inconsistent state.
- The `mkdocs serve` restart at play end briefly returns HTTP `000` while it rebuilds
  the site — wait ~5-15s and poll `/` for `200` before checking new pages.

## Verifying the result (do this, don't assume)

Files deploy to the **real docs root**: `/opt/mkdocs/site/docs/` on CT 850 (the serve
process cwd is `/opt/mkdocs/site`; `docs_dir` defaults to `docs/`). NOT
`/opt/mkdocs/docs/` — that path is empty and will fool you into thinking deploy failed.

Three live-site checks after restart:
- `curl -s -o /dev/null -w '%{http_code}' http://10.20.0.160:8000/services/<hostname>-<port>/` → 200
- `curl -s http://10.20.0.160:8000/services/ | grep -i <ServiceName>` (services index)
- `curl -s http://10.20.0.160:8000/vms/ | grep -i <ServiceName>` (per-VM dropdown)

## Registry `services:` schema (per worked example CT 520)

```yaml
services:
  - name: Ollama
    port: 11434              # omit for portless workers
    type: ollama             # fastapi | neo4j | postgres | redis | minio | proxy | worker | ...
    classification: utility  # production | utility | staging | development | internal
    description: >
      One-paragraph operational summary.
    # optional: api_spec_path: /openapi.json  → triggers OpenAPI fetch + API doc page
    # optional: domain / tunnel_url, neo4j_target, mongo_target, repo, active: false
```
The per-VM services dropdown in `vms/index.md` renders four columns: name, port, type,
classification. Only services with `api_spec_path` get their spec fetched + an API page.

## Probe what actually runs before writing service entries

Don't transcribe assumptions — verify against the live VM/CT:
- `qm status <vmid>` / `qm config <vmid>` (VMs) or `pct status` (LXC); get IP via
  `qm agent <vmid> network-get-interfaces`.
- Listening ports: `qm guest exec <vmid> -- /bin/bash -lc "ss -tlnp"` (guest-exec output
  is JSON with an `out-data` field — parse it).
- For an Ollama host specifically: `curl http://<ip>:11434/api/version` and `/api/tags`
  (the `ollama` CLI panics with `$HOME is not defined` under guest-exec; hit the API).
- Distinguish **services** (real app surfaces → registry `services:`) from **substrate**
  (Docker/containerd daemons, nvidia-persistenced → mention in `notes`, don't pad the
  list). Idle Docker with zero resident containers is substrate, not a service.

## Committing cleanly when the working tree is already dirty

`registry/containers.yml` is often dirty with someone else's uncommitted entry (e.g. a
half-finished container block) plus stale untracked regenerated docs. To commit ONLY
your logical change without entangling theirs:

1. `git diff registry/containers.yml` → find the `@@` hunk headers; identify which hunk
   is yours by line number.
2. `git diff registry/containers.yml > /tmp/full.diff`
3. Build a patch with just the diff header (first ~4 lines) + your hunk:
   `{ sed -n '1,4p' /tmp/full.diff; sed -n '<start>,<end>p' /tmp/full.diff; } > /tmp/mine.diff`
4. `git apply --cached /tmp/mine.diff` — stages only your hunk to the index.
5. Verify isolation: `git diff --cached registry/containers.yml | grep -iE '<theirOtherEntry>'`
   should be empty; `git diff --cached --name-only` should list only your file.
6. Commit. Leave regenerated/derived docs uncommitted — they regenerate from the registry,
   so not committing them loses nothing and avoids sweeping in unrelated churn.
