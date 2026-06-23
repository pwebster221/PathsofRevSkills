---
name: sdlc-continuous-deployment
stage: ship
posture: continuous-deployment
tier: 2
role: skill
license: MIT
---
# Skill: Continuous Deployment

## Lineage

Continuous Deployment is the logical endpoint of the Continuous Delivery philosophy articulated by Jez Humble and Dave Farley in *Continuous Delivery* (2010) and quantified by the DORA research program in *Accelerate* (Forsgren, Humble, Kim, 2018). It is the practice of automatically promoting every commit that passes all automated quality gates directly to production - no human approval required.

This is not recklessness. It is the discipline of building enough confidence in your pipeline that human approval gates become the risk, not the mitigation.

---

## Core Principle

> "If it hurts, do it more often." - Jez Humble

The pain of infrequent releases comes from batch size. Large batches accumulate more change, amplify risk, and make root-cause analysis exponentially harder. Continuous Deployment eliminates batch size as a variable by making the batch size one: a single commit.

---

## Prerequisites

Before adopting this posture, the following must be true:

1. **Automated test suite with high confidence coverage** - Unit, integration, and contract tests that the team genuinely trusts.
2. **Fast pipeline** - Total build + test time ideally under 10 minutes. Longer pipelines create queue pressure that defeats the purpose.
3. **Trunk-based development** - All work integrates to main frequently (at minimum daily). Long-lived branches are incompatible with CD.
4. **Observability in production** - Metrics, logs, and traces that allow rapid detection of regressions post-deploy.
5. **Fast rollback mechanism** - Either automated rollback on SLO breach or a one-command manual rollback with MTTR under 5 minutes.
6. **Feature flags** - The escape valve that makes CD safe. Deploy code that isn't yet user-visible.

---

## Execution Steps

### 1. Gate Definition
Define the quality gates that must pass before auto-promotion:
- Unit tests: 100% pass
- Integration tests: 100% pass
- Static analysis: no new critical violations
- Security scan: no new high/critical CVEs introduced
- Performance budget: p95 latency within defined threshold

### 2. Pipeline Construction
Organize stages in strict order:

```
Commit -> Build -> Unit Test -> Integration Test
-> Static Analysis -> Security Scan
-> Deploy to Staging -> Smoke Test
-> Deploy to Production -> SLO Verification
```

Every stage is automated. There are no manual steps.

### 3. Deployment Execution
- Build immutable artifacts once; deploy the artifact, not the source.
- Use zero-downtime deployment strategy (rolling update, or blue-green under the hood).
- Emit a deployment event to your observability platform with commit SHA, author, and timestamp.

### 4. Post-Deploy Verification
- Run a smoke test suite against production immediately after deploy.
- Monitor SLOs for a defined burn window (typically 5-15 minutes post-deploy).
- If SLO breach is detected: automated rollback or immediate on-call alert.

### 5. Feedback Loop
- Surface deploy status to the team in real time (Slack, dashboard).
- Track DORA metrics: Deployment Frequency, Lead Time for Changes, MTTR, Change Failure Rate.
- Treat every failed deployment as a process improvement signal, not just an incident.

---

## Failure Modes and Mitigations

| Failure Mode | Mitigation |
|---|---|
| Pipeline becomes slow, creating backlog pressure | Parallelize test stages; split test suite; invest in test infrastructure |
| Flaky tests generate false-positive failures | Quarantine flaky tests; fix before re-adding to gate |
| Production incident from an auto-deployed change | Improve coverage for the gap; add to smoke suite; implement automatic rollback |
| Team loses confidence in the pipeline and starts overriding it | Never override the pipeline manually - fix the pipeline instead. Manual overrides are a smell, not a solution. |

---

## Key Metrics

| Metric | Elite Level (DORA) |
|---|---|
| Deployment Frequency | Multiple deploys per day |
| Lead Time for Changes | Less than 1 hour from commit to production |
| Change Failure Rate | Under 5% |
| MTTR | Under 1 hour |
