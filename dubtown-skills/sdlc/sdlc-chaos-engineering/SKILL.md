---
name: sdlc-chaos-engineering
stage: sustain
posture: chaos-engineering
tier: 2
role: skill
license: MIT
---
# Skill: Chaos Engineering

## Lineage

Chaos Engineering was formalized by Netflix's Chaos Monkey project (2011) and codified as a discipline in *Chaos Engineering* (Casey Rosenthal, Nora Jones, et al., O'Reilly, 2020) and the Principles of Chaos Engineering manifesto (principlesofchaos.org). The practice emerged from a specific insight: in complex distributed systems, the failure modes that will actually hurt you in production are precisely the ones you haven't thought of and haven't tested. The only way to discover them proactively is to induce failures deliberately - in a controlled, scientific, and safe manner.

Chaos Engineering is a posture for *confident* teams, not struggling ones. It presupposes that the baseline is healthy. You are not debugging a broken system - you are proactively discovering the breaking points of a system you believe is reliable.

---

## Core Principle

> "Chaos Engineering is the discipline of experimenting on a system in order to build confidence in the system's capability to withstand turbulent conditions in production."
>
> - Principles of Chaos Engineering

The key word is *experimenting*. Chaos Engineering is not random destruction. It is the scientific method applied to system resilience: define a hypothesis, design a minimal experiment, observe results, learn from deviation.

---

## The Chaos Engineering Scientific Method

| Step | Description |
| --- | --- |
| **1. Define steady state** | Identify the metrics that define "normal" system behavior: request success rate, latency p99, queue depth, etc. |
| **2. Form a hypothesis** | "We believe that if dependency X fails, our service will degrade gracefully and steady state will be maintained within Y seconds." |
| **3. Design the experiment** | Define the minimal failure injection that tests the hypothesis, and the blast radius controls that limit impact. |
| **4. Run in the smallest safe scope** | Start in non-production. Graduate to production only when confident in blast radius controls. |
| **5. Observe and compare** | Does steady state hold? Did the system recover as expected? |
| **6. Learn from deviation** | If steady state was violated, this is a discovered failure mode. Fix it before production discovers it naturally. |

---

## Failure Injection Categories

| Category | Examples |
| --- | --- |
| **Resource exhaustion** | CPU saturation, memory pressure, disk fill, connection pool exhaustion |
| **Network failures** | Latency injection, packet loss, partition (split-brain), DNS failure |
| **Dependency failures** | Upstream service timeouts, third-party API outages, database connection failure |
| **State corruption** | Message queue backup, stale cache, clock skew |
| **Infrastructure failures** | Instance termination, AZ failure, region failure simulation |

---

## Execution Steps

### 1. Establish the Prerequisite Foundation

Do not attempt Chaos Engineering without:

- Defined and monitored SLOs
- Robust observability (metrics, traces, logs) that allows real-time observation of system behavior during experiments
- Rollback capability for experiments
- Clear blast radius controls (ability to halt an experiment instantly)
- Team awareness that experiments are running

### 2. Start with a Known Failure

Your first chaos experiment should test a failure mode you already know about and believe you've mitigated. This builds confidence in the process before you're probing unknown territory.

Example: "We believe we've handled database connection pool exhaustion. Let's verify."

### 3. Gamedays

Before running automated chaos experiments, conduct a Gameday:

- A scheduled exercise where the team runs a defined scenario manually
- Observers watch metrics and system behavior in real time
- Debrief immediately: what was expected vs. what actually happened?

Gamedays build team resilience and shared mental models alongside system resilience.

### 4. Controlled Experiments

Design each experiment with:

- **Hypothesis**: clear statement of expected behavior
- **Blast radius control**: the mechanism to halt the experiment (kill switch, time limit, traffic percentage cap)
- **Duration**: experiments run for the minimum time needed to observe steady state behavior
- **Rollback**: automatic reversion of injected faults after the experiment window

### 5. Graduate to Production

Start in staging. Graduate to production only when:

- Blast radius controls are tested and trusted
- SLO monitoring is active and alerting correctly
- Team is present and monitoring during the experiment window
- A clear rollback procedure exists

Production chaos experiments are the gold standard - staging rarely matches production traffic patterns and dependency behavior.

### 6. Automate Continuous Verification

Mature chaos engineering programs run low-blast-radius experiments continuously in production as part of the regular operational cadence. This is how Netflix operates Chaos Monkey: it runs randomly in the background, continuously verifying that services handle instance failures correctly.

Automation shifts chaos from a scheduled event to a continuous property of the system.

---

## Failure Modes and Mitigations

| Failure Mode | Mitigation |
| --- | --- |
| Experiment causes uncontrolled production outage | Never run without blast radius controls; start small; graduate slowly; kill switch must be one click |
| Team views chaos as threatening or blameworthy | Frame experiments as learning events; a discovered failure mode before the user reports it is a win |
| Chaos program started too early (system not stable enough) | Chaos Engineering is for confident teams on stable systems; fix baseline reliability first |
| Experiments become theater without learning | Require a written finding and at least one action item per experiment; track experiment-to-improvement rate |

---

## Tooling Reference

| Tool | Notes |
| --- | --- |
| **Chaos Monkey** (Netflix OSS) | Instance termination; integrates with Spinnaker; foundational tool |
| **Gremlin** | SaaS; broad failure injection library; good enterprise tooling and safety controls |
| **Chaos Mesh** | Open source; Kubernetes-native; wide failure type coverage |
| **AWS Fault Injection Simulator (FIS)** | Native AWS; integrates with CloudWatch; supports EC2, ECS, EKS, RDS |
| **Litmus** | CNCF project; Kubernetes-native; active open-source community |
