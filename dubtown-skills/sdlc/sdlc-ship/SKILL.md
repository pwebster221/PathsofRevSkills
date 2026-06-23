---
name: sdlc-ship
stage: ship
tier: 1
role: navigator
license: MIT
---
# Stage 5 - Ship: Navigator

## Purpose

The Ship stage answers a deceptively simple question: how does working software become running software? The answer varies enormously. A consumer SaaS startup and a financial institution both "ship" - but what that word means differs by an order of magnitude in ceremony, risk posture, and tooling.

This Navigator reads five contextual signals and routes to the posture that fits your current situation. It does not prescribe a permanent shipping strategy. Postures can and should evolve as team maturity grows.

---

## Signal Definitions

| Signal | What It Measures | Values |
|---|---|---|
| **automation_maturity** | How much of your pipeline is automated end-to-end | low / medium / high |
| **risk_tolerance** | Blast radius and recovery time if a bad deploy hits production | low / medium / high |
| **compliance_burden** | Regulatory or audit requirements on change management | low / medium / high |
| **traffic_scale** | Volume and distribution of production traffic | small / medium / large |
| **release_frequency** | How often the team ships to production | occasional / regular / continuous |

---

## Routing Table

| automation_maturity | risk_tolerance | compliance_burden | release_frequency | Recommended Posture |
|---|---|---|---|---|
| high | high | low | continuous | Continuous Deployment |
| high | medium | low | continuous | Continuous Deployment |
| medium-high | medium | low | regular | Blue-Green / Canary Rollout |
| high | medium | low | regular | Blue-Green / Canary Rollout |
| any | any | low | any | Feature Flag Release (when decoupling deploy from release is the primary concern) |
| high | any | low | regular-continuous | GitOps Release (when declarative state and drift prevention are the primary concern) |
| any | low | high | occasional-regular | Controlled Release Gate |
| low | low | high | occasional | Controlled Release Gate |

> **Tie-breaking rule:** When multiple postures match, prefer the one that most directly addresses your *current* bottleneck. Scared of rollback? Blue-Green/Canary. Losing track of infrastructure state? GitOps. Business not ready to expose the feature yet? Feature Flags. Auditors breathing down your neck? Controlled Release Gate.

---

## Signal Elicitation Prompts

Use these when signal values are unclear:

- *"How much of your deploy process requires manual steps or human approvals before reaching production?"* -> automation_maturity
- *"If the next deploy has a critical bug, how quickly can you detect it and how many users are affected before you recover?"* -> risk_tolerance
- *"Does your organization require a change ticket, CAB approval, or audit trail before production changes?"* -> compliance_burden
- *"How many times per day/week/month does your team currently push to production?"* -> release_frequency
- *"How large and geographically distributed is your production user base?"* -> traffic_scale

---

## Stage Boundaries

**Entry condition:** Verify stage is complete. All acceptance criteria and quality gates have passed. The artifact is promotion-ready.

**Exit condition:** The artifact is running in production with observability active. The team has confirmed via a defined success signal: SLO met, smoke tests green, key metrics stable.

**Handoff to Sustain:** Ship ends when the software is alive in production. Sustain begins the moment you are responsible for keeping it alive.
