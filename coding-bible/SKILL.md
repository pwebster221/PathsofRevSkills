---
name: coding-bible
description: Use this skill whenever code or infrastructure is being written, built, audited, debugged, deployed, or architected for Paul Webster / DubTown Designs OR for Paths of Reverence — the Coding Bible is the universal coding standard for both. It is Paul's personal coding canon AND Paths of Reverence's coding canon (PoR is one of Paul's projects; PoR services are built to these same rules). Encodes preferred frameworks (FastAPI + Pydantic v2, FastMCP, LangGraph, Astro, Neo4j-first, native systemd over Docker), infrastructure patterns (Proxmox/LXC, Cloudflare Tunnels with protocol http2 only, WireGuard for inter-node VPN, Authentik OIDC for auth, Ansible as sole IaC), container archetype classification (Three-Duality of Depth × Permanence × Velocity → 8 archetypes), MCP service shape conventions (mounted /mcp/mcp vs standalone /mcp), workflow norms (7-phase build, subagent-driven development, macro authorization, optionality as a requirement), agent behavior norms (honest unperformed errors, cost discipline, Esoteric Diction tier discipline for agent outputs), and load-bearing operational gotchas (cloudflared QUIC instability, FastMCP behind tunnel requires custom main(), KairosAPI client drift, Sacred Journey wrapper drift, tar --exclude-from anchoring, Linear renderer quirks, cloudflared has no graceful reload). Trigger on the named technologies, on container/host/network design, on auth/MCP/tunnel setup, on any of the cited PoR services as worked examples, and on broader "how should I build this" questions in Paul's or PoR's workspace. Use even when the user does not name "coding bible" or "standards" — if the work is code or infrastructure under Paul's authorship or under the Paths of Reverence ecosystem, this skill applies.
---

# coding-bible

⟜ The universal coding canon for **Paul Webster / DubTown Designs** and **Paths of
Reverence**. Frameworks, programs (as worked examples), and the rules of conduct that
have been paid for at least once in time, sleep, or a 502.

**Scope.** This is one canon shared by two scopes:

- Paul's personal projects across DubTown Designs.
- Every service in the Paths of Reverence ecosystem (PoR is one of Paul's projects;
  PoR's code is built to these same rules, not a separate sub-standard).

The PoR services named in Part II are *worked examples* of the canon in action, not the
canon's scope. The rules apply equally to a side project that uses none of the named
PoR hostnames.

## When this skill applies

- Writing, building, auditing, debugging, deploying any service or infrastructure
  component under Paul's authorship or inside the Paths of Reverence ecosystem.
- Picking a framework, runtime, or platform for a new service (FastAPI vs Flask, FastMCP
  vs raw MCP SDK, Neo4j vs Postgres, systemd vs Docker, etc.).
- Configuring Cloudflare Tunnels, WireGuard, Authentik OIDC, Proxmox/LXC containers,
  Ansible playbooks, or any of the named infrastructure.
- Classifying a new container with the Three-Duality archetype system.
- Deciding the shape of an MCP service (mounted vs standalone path conventions).
- Designing a multi-step workflow (the 7-phase build), authorizing subagent-driven
  development, or deciding whether to require optionality (custom tool + MCP).
- Tuning agent behavior — honest unperformed errors, cost discipline, Esoteric Diction
  tier selection for agent outputs.
- Hitting any of the load-bearing gotchas: cloudflared QUIC, FastMCP behind tunnel,
  KairosAPI client drift, Sacred Journey wrapper drift, tar excludes, Linear renderer.

## When this skill does NOT apply

- Pure prose/visual/typographic decisions inside a PoR-authored artifact — hand off to
  `paths-of-reverence-brand`.
- Code/infrastructure outside Paul Webster / DubTown Designs / Paths of Reverence
  authorship (this canon encodes Paul's and PoR's shared norms, not industry defaults).

## The triadic structure

The canon is organized as a triad. Read the relevant section first.

| Part | Planet | Register | Content |
|---|---|---|---|
| Frameworks | ☿ Mercury | The conduit | What we build with — FastAPI, Pydantic, FastMCP, LangGraph, Neo4j, Ansible, Proxmox+LXC, Cloudflare Tunnel, WireGuard, Authentik, Vaultwarden, etc. |
| Programs | ☉ Sol | The manifest | What we have built — Sacred Journey, Kairos, Mars Scoring, Solar, Mercury, Alder, PoR Hub, Esoteric Repository, etc. PoR services act as *worked examples* of the rules in action. |
| Coding Rules | ♄ Saturn | The boundary | How we hold the work — architecture rules, infra/networking rules, MCP shape, data drift, auth, agent behavior, workflow, documentation. |

Bodies of references mirror the canon section-by-section.

## Callout family — read first

Every Conventions & Gotchas line in this canon carries one or more marks. Recognize them.

| Mark | Name | Meaning |
|---|---|---|
| ▲ | Gotcha | The load-bearing trapdoor. Read first if short on time. |
| ◐ | Drift | Wrapper / client / API mismatch. Smoke-test before flipping. |
| ✦ | Pattern | A worked pattern worth remembering. |
| ✱ | Decision | Decided but not yet deployed — partial coverage. |
| ⧈ | Memory | A `[[memory-name]]` cross-reference into Paul's memory store. |
| † | Read-only | Hands off. Production graphs, third-party hosts. |

A Gotcha that is also a Drift carries both marks. Treat compound marks as compounding
risk.

## Three-Duality archetype — quick reference

Every container Paul deploys is classified along three axes. The sigil is the primary
identifier; the name follows.

| Sigil | Code | Name | Tunnel policy |
|---|---|---|---|
| ◆●▼ | DPS | Vault | Its own tunnel (deepest classification) |
| ◆●▲ | DPI | Sanctum | Its own tunnel (deep + persistent + iterative) |
| ◆○▲ | DCI | Laboratory | Per-service judgment |
| ◆○▼ | DCS | Bunker | Per-service judgment |
| ◇●▲ | SPI | Forum | Shared-host tunnel acceptable |
| ◇●▼ | SPS | Monument | Shared-host tunnel acceptable |
| ◇○▲ | SCI | Workshop | Default for generic services |
| ◇○▼ | SCS | Billboard | Shared-host tunnel acceptable |

When classifying a new container, decode all three axes — Depth (Deep ◆ / Surface ◇) ×
Permanence (Persistent ● / Consumable ○) × Velocity (Iterative ▲ / Static ▼). Source:
`references/coding-bible-full.md` § Architecture / Three-Duality.

The full archetype semantic (tunnel placement, backup policy, lifecycle expectations) is
mirrored from `brand-system.md` §5.2 — see `paths-of-reverence-brand/references/sigils.md`
for the canonical sigil home. The decision tree per archetype is gated behind the future
`rules/three-duality.md` work in the canon.

## The most load-bearing rules (Tight register)

Drawn from `references/coding-rules.md` and `references/gotchas-load-bearing.md`.

### Infrastructure & networking

- **Force `protocol: http2` in every `cloudflared` `config.yml`.** QUIC default thrashes
  → intermittent 502s.
- **`systemctl reload cloudflared` actually restarts** (~7s outage). Batch ingress
  changes.
- **Always pass tunnel UUIDs, never names.** Name resolution can pick the wrong UUID.
  Verify with `cloudflared tunnel info <uuid>`.
- **Multi-zone certs on CT 520.** Use `--origincert cert-dubtown.pem` for
  `*.dubtown-server.us`; default `cert.pem` is the `sacredjourney.io` zone.
- **Per-deep-container tunnels.** DPS/DPI archetypes (Vaultwarden, monitoring) get
  their own tunnel, never shared. Exceptions accumulate into systemic risk.
- **CT 2001 is read-only / third-party.** † Never edit, install, or restart. Dev goes
  on CT 2002.

### MCP & service shape

- **`por-mcp` monorepo is the SoT for standalone MCP servers** ✱
  (github.com/pwebster221/por-mcp, private; decided 2026-07-15). One truth, many
  expressions: each LXC clones the full repo and runs only its own server via
  `deploy.sh <name>` (git pull → dep sync → `systemctl restart` → health check).
  `mcp-registry.json` at repo root is the machine-readable fleet manifest — agents
  read it instead of crawling LXCs. In scope: standalone wrappers only (agi-skills,
  kairos, solar, mani-mcp-proxy, reporeason). MCPs mounted inside a parent FastAPI
  app (Sacred Journey, Mars, Grimoire, Repository-KG, VenusFace) stay with their
  service — registry entries with `"managed": "in-service"`.
- **Migration never changes a server's runtime.** The fleet is native systemd + venv;
  no forced containerization. `deploy.sh` dispatches on the registry's `"runtime"`
  field (`systemd` default; `compose` only where a server already runs under Docker,
  i.e. reporeason). Tunnels are untouched — they point at localhost ports and don't
  care where the code is canonical.
- **FastMCP behind tunnel requires a custom `main()`** running uvicorn with
  `proxy_headers=True` and `forwarded_allow_ips="*"`, plus Starlette `CORSMiddleware`
  mounted *before* the MCP app. `mcp.run()` is insufficient.
- **Mounted MCP → `/mcp/mcp`** (Sacred Journey, Solar, Mars, Repository).
  **Standalone wrappers → `/mcp`** (Kairos MCP, reporeason). Do not assume — check.
- **MCP auth: fleet-deployed** — Authentik OIDC via fastmcp OIDCProxy on the MCP
  surfaces (wired 2026-07-11); mutation tools additionally gate on `MCP_WRITE_TOKEN`.
  Raw REST APIs underneath remain public — treat any new public surface as needing
  its own Authentik gate.

### Data & client drift

- **KairosAPI client drift smoke-test** before flipping any toggle on a non-git'd
  caller. Drift won't surface until the first real call — silent 422.
- **Sacred Journey wrapper drift check** — `/opt/SacredJourneyAPI/app/mcp_server.py`
  drifts from V2 Pydantic. Check both the API and the wrapper before patching. Verify
  state via `/cycles/{id}/progress`.
- **Production graph = `CT 500:7687`.** Each staging DB has a specific port on VM 510.
  Authoritative port table is in `/root/CLAUDE.md` (SOT for live infra facts).

### Auth

- **Authentik OIDC is the standard** (PAT-509, 2026-05-16). Replaces single-user JWT
  for any new PoR service. Two PAT-509 follow-ups are deferred — verify the integration
  is complete for the specific service before assuming it is.

### Agent behavior — the rules of conduct

- **Honest unperformed errors.** ✦ If a subsystem failed, say so directly. No
  voice-rewrapping.
- **Esoteric Diction tier discipline.** Tight for operational/error lines, Standard for
  bodies, Deep only for Part openings. ✱ Do not default to Deep. Full tier reference
  in `paths-of-reverence-brand/references/tiers.md`.
- **Cost discipline.** Minimize Opus. Enforce token budgets. Recover output from logs
  on failed runs rather than re-running.
- **Langflow `session_id` discipline.** Always set an explicit `session_id` on every
  `ChatInput`. Blank defaults to shared "New Session N" slots and history bleeds.

### Workflow

- **The 7-phase build:** brainstorm → spec → plan → subagent execute → dev review →
  deploy → cleanup. ✦ Don't shortcut for features that touch more than one service.
- **Subagent-driven dev.** Fresh subagent per task; two-stage review (subagent + dev)
  catches real bugs. Inline review acceptable for < 30-line wiring tasks.
- **Macro decision → no micro re-asks.** Once a multi-step task is authorized,
  permission is for the whole arc. Re-ask only when the work leaves the authorized
  scope.
- **Optionality as a requirement.** ✦ When the user asks for both a custom tool AND
  an MCP, build both. The redundancy is the value.

### Documentation

- **Registry-driven infra docs.** Edit `ansible/dubtown-infra/registry/containers.yml`,
  re-run the mkdocs playbook. Don't hand-edit generated docs.
- **MEMORY.md scope.** Save user profile, project state, feedback, references. Don't
  save anything derivable from `git log`, code, or `CLAUDE.md`. Each memory file has
  `name` / `description` / `type` frontmatter; index entries are one line.
- **Memory framing — records, not dictates.** ✦ Override when context warrants. Verify
  memory against live state before acting on it.
- **Linear renderer quirks.** Use fenced code blocks for dense tables / bullet lists,
  or Linear silently drops content.
- **`tar --exclude-from` anchoring.** Bare `sessions/` won't match nested
  `.claude/sessions/`. Anchor patterns to the in-archive path or verify post-extraction.

## When to read which reference

- `references/coding-bible-full.md` — the complete coding-bible canon, verbatim mirror.
  Read when you need a specific entry's full template (Purpose / Where used /
  Version-Source / Conventions & Gotchas / Links) or when looking up the
  Programs section as a worked example for a new service.
- `references/coding-rules.md` — Section 3 (Coding Rules) mirrored standalone. Read
  when auditing a service or PR against the rules of conduct without needing the
  Frameworks/Programs context.
- `references/gotchas-load-bearing.md` — distilled Tight-register Gotcha list pulled
  across the entire canon. Read when triaging a failure or doing a pre-deploy review.
- `references/_provenance.md` — sync provenance for the mirror. Read only when canon
  has changed and you need to re-mirror.

## When the user is building a new service

1. **Classify with the Three-Duality archetype.** Decode all three axes. Default is
   SCI (◇○▲ Workshop) for generic services. The archetype dictates tunnel placement
   and backup policy.
2. **Pick the framework stack from the Frameworks section.** Default: FastAPI +
   Pydantic v2 + Neo4j + systemd unit + Cloudflare Tunnel (http2). FastMCP when an
   MCP surface is needed.
3. **Decide service shape** (mounted /mcp/mcp under FastAPI vs standalone /mcp wrapper).
   Mounted is preferred when API and MCP share data models; standalone when wrapping
   a foreign API.
4. **Wire auth via Authentik OIDC** if the surface is user-facing. Bearer for
   service-to-service unless on the deprecation path.
5. **Add ▲ Gotchas to the Coding Bible** as you find them. The canon grows from the
   incidents that paid for it.

## When the user is debugging a known-pattern failure

Match the symptom to the gotcha:

- Intermittent 502s through a tunnel → check `protocol: http2` in `config.yml`.
- MCP service rejects browser clients → custom `main()` with proxy headers + CORS.
- Wrong tunnel routing after `tunnel route dns` → name resolution bug, pass the UUID.
- Silent 422 on a Pydantic client → wrapper drift, smoke-test the API contract.
- Cross-flow Langflow history bleed → blank `session_id`.
- Linear post silently dropping rows → use a fenced code block.

## Versioning

This skill mirrors coding-bible v1 (2026-05-16, written against PoR Brand System v1).
Bump the mirror when canon changes — see `references/_provenance.md`.
