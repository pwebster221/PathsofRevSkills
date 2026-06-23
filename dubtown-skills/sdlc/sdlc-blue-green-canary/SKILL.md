---
name: sdlc-blue-green-canary
description: "Use during ship when you need zero-downtime deployment and want to separate deploying code from exposing it to users. Activates when someone says \"how do we roll this out safely\", \"deploy without downtime\", \"limit the blast radius\", or when you can validate at production scale before full cutover. Maintains parallel environments (blue-green) and/or progressively shifts traffic (canary) so risk at any moment is proportional to the share of traffic on the new version."
stage: ship
posture: blue-green-canary
tier: 2
role: skill
license: MIT
---
# Skill: Blue-Green / Canary Rollout

## Lineage

Blue-Green Deployment was described by Martin Fowler and popularized in *Continuous Delivery* as a technique for zero-downtime deployments by maintaining two identical production environments. Canary Releases - named after the canary-in-a-coal-mine safety practice - extend this concept by progressively shifting traffic to the new version, allowing real-world validation before full rollout. Both techniques are foundational to the SRE discipline of managing risk at the deployment boundary.

---

## Core Principle

Deployment and cutover are separable events. You can deploy new code without exposing users to it, validate it against real infrastructure at production scale, and progressively shift traffic while monitoring for regressions. Risk at any moment is proportional to the percentage of traffic seeing the new version.

---

## Technique Comparison

| Technique | Mechanism | Best For |
|---|---|---|
| **Blue-Green** | Two identical environments; switch all traffic at once via load balancer | Quick full cutover with instant rollback capability |
| **Canary** | One environment; gradually shift a percentage of traffic to the new version | Large-scale services requiring progressive production validation |
| **Ring Deployment** | Canary applied in defined rings: internal -> beta users -> general availability | Consumer products with distinct user cohorts |

---

## Execution Steps: Blue-Green

### 1. Provision
Maintain two production environments - Blue (currently live) and Green (new version). They are identical in configuration, scale, and infrastructure.

### 2. Deploy to Inactive Environment
Deploy the new version to Green. Green is not receiving user traffic.

### 3. Smoke Test Green
Run the full smoke suite against Green using its direct endpoint URL (bypassing the load balancer). Fix any failures before proceeding.

### 4. Cutover
Switch the load balancer to route all traffic to Green. Blue is now idle but still running.

### 5. Monitor
Watch SLOs for 15-30 minutes. If healthy: proceed to decommission. If degraded: switch load balancer back to Blue (instant full rollback, no redeploy required).

### 6. Decommission Blue
Once confident the release is stable, tear down Blue or update it to become the next deployment target.

---

## Execution Steps: Canary

### 1. Deploy Canary
Deploy the new version alongside the existing version. Route a small initial percentage of traffic to the canary (1-5%).

### 2. Define Canary Success Criteria
Before advancing traffic, specify your thresholds:
- Error rate delta: canary error rate must not exceed baseline by more than 0.1%
- Latency delta: p99 must not exceed baseline by more than 20ms
- Business metrics: conversion rate, engagement - no statistically significant degradation

### 3. Progressive Traffic Shift
If the canary passes success criteria at each step, increment traffic:

```
1% -> 5% -> 10% -> 25% -> 50% -> 100%
```

Each step requires a minimum bake time (5-15 minutes at scale, longer for lower-traffic services where sample size builds slowly).

### 4. Automated Abort
If success criteria are violated at any traffic percentage, automatically route all traffic back to the stable version and alert on-call. Do not advance.

### 5. Full Rollout
Once at 100%, decommission the old version.

---

## Database Migration: The Expand-Contract Pattern

The most common failure mode for blue-green and canary deployments is a database migration that the old version cannot read. Solve this with expand-contract:

1. **Expand**: Add new columns/tables while keeping old ones. Both versions can operate.
2. **Migrate**: Deploy new version. Run data backfill. Old version still works on old schema.
3. **Contract**: Once old version is fully decommissioned, remove old schema elements.

Never deploy a breaking schema change in the same release as the application change.

---

## Tooling Reference

| Layer | Blue-Green | Canary |
|---|---|---|
| Kubernetes | Two Deployments + Service label selectors | Argo Rollouts, Flagger |
| Cloud Load Balancer | AWS ALB weighted target groups, GCP traffic splitting | Same |
| Service Mesh | Istio VirtualService weight rules | Istio + Prometheus + Flagger |

---

## Failure Modes and Mitigations

| Failure Mode | Mitigation |
|---|---|
| Breaking schema migration during Blue-Green cutover | Apply expand-contract pattern; never deploy schema breaks with app changes |
| Canary success criteria too loose; bad version reaches 100% | Tighten thresholds; extend bake time before advancing; add business metric monitoring |
| Cost of running two full environments (Blue-Green) | Auto-scale Blue to zero after successful cutover; tear down promptly |
| Session affinity breaks during traffic shift | Use stateless session design or sticky sessions with canary awareness |
