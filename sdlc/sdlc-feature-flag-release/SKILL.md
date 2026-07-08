---
name: sdlc-feature-flag-release
description: >-
  Use during ship when you need to deploy code to production continuously but
  control when and to whom a feature becomes visible. Activates when someone says
  "we want to merge this now but not turn it on yet", "roll it out to 5% first",
  "we need a kill switch", or when deployment must be decoupled from release for
  trunk-based teams, dark launches, or progressive exposure.
stage: ship
posture: feature-flag-release
tier: 2
role: skill
license: MIT
---

# Skill: Feature-Flag Release

## Lineage

Feature flagging (feature toggling) was codified by Martin Fowler and Pete Hodgson
in *Feature Toggles* (martinfowler.com, 2017) and is the runtime complement to the
*Continuous Delivery* pipeline discipline of Humble and Farley (2010). It is the
operational backbone of trunk-based development and "progressive delivery": every
commit reaches production, but a flag — not a deploy — decides who sees the change.
The practice matured into a tooling category (feature management) and an open
standard, OpenFeature (CNCF).

## Core Principle

**Decouple deployment from release.** Shipping code and exposing behavior become two
independent decisions. Code is deployed *dark*, then exposure is widened at runtime
under direct control, and reversed instantly without a redeploy. Risk moves from the
irreversible moment of deploy to a dial you can turn both ways.

## Key Concepts

- **Flag types.** Release toggles (short-lived, gate unfinished work), experiment
  toggles (A/B), ops toggles (circuit breakers / kill switches), and permission
  toggles (entitlements). They have very different lifespans — conflating them is the
  root of most flag debt.
- **Targeting.** Exposure by cohort: internal users → percentage ramp → segment →
  all. Evaluation is per-request against user/context attributes.
- **Kill switch.** Any release flag is also an abort control: flip off to mitigate
  without rolling back the deploy.
- **Flag debt.** Stale flags are dead conditional branches that multiply test paths
  and hide behavior. Retirement is part of the workflow, not an afterthought.

## Execution Steps

### 1. Wrap the change
Put the new path behind a named flag, default **off**. Keep the old path intact so
the flag genuinely chooses between two live behaviors.

### 2. Deploy dark
Merge to trunk and deploy to production with the flag off. The change is now in prod,
exposed to no one.

### 3. Ramp by cohort
Enable for internal/dogfood users, then a small percentage, widening as signals stay
green. Hold each step long enough to read real telemetry.

### 4. Observe per-cohort
Compare error rate, latency, and business metrics for flagged-on vs flagged-off
populations. The off cohort is your built-in control group.

### 5. Decide: widen or kill
Continue the ramp to 100%, or flip the kill switch on any regression — mitigation in
seconds, no redeploy.

### 6. Retire the flag
Once fully rolled out and stable, remove the flag and the dead branch. Close the loop
so the codebase doesn't accumulate toggle debt.

## Tooling Reference

| Layer | Options |
|---|---|
| Managed platforms | LaunchDarkly, Split, Statsig |
| Open source | Unleash, Flagsmith, GrowthBook |
| Standard / SDK | OpenFeature (CNCF) — vendor-neutral evaluation API |
| Homegrown | Config-service + cached evaluation (viable at small scale; grows costly) |

## Failure Modes and Mitigations

| Failure mode | Mitigation |
|---|---|
| Zombie flags / flag debt | Expiry dates + owner per flag; a "retire" task in the same PR that ships to 100% |
| Combinatorial test explosion | Test the default-on and default-off paths; limit concurrent long-lived release flags |
| Release flags used as permanent config | Separate flag types by lifespan; promote durable toggles to real configuration |
| Inconsistent state across coupled flags | Model dependencies explicitly; avoid flags that must move together |
| Targeting on sensitive attributes | Treat flag-evaluation context as PII-bearing; audit who can change targeting |
