---
name: sdlc-sre-slo-driven
description: "Use during sustain to treat reliability as a measurable product feature — defining SLOs and using error budgets to balance velocity against stability without politics. Activates when someone says \"how reliable should this be\", \"how do we choose between features and stability\", \"how do we measure and operate reliability\", or when \"keeping it up\" needs a quantified contract. Within the error budget, move fast; budget burned, stop shipping and invest in reliability — an explicit, agreed, measurable tradeoff."
stage: sustain
posture: sre-slo-driven
tier: 2
role: skill
license: MIT
---
# Skill: SRE / SLO-Driven Operations

## Lineage

Site Reliability Engineering was formalized at Google and published in the *SRE Book* (Beyer et al., 2016) and *The SRE Workbook* (2018). It is an engineering discipline applied to operations: using software to manage systems at scale, defining reliability as a measurable product requirement, and using error budgets to balance velocity against stability in a quantified, non-political way.

The core contribution of SRE to software engineering is the insight that "reliability" is not an aspiration - it is a *feature*, with a target, an owner, and a budget for violating it.

---

## Core Principle

> "Hope is not a strategy." - SRE Book

SRE replaces vague commitments to "keeping the system up" with a mathematical contract between the engineering team and its users: the Service Level Objective (SLO). When you're within your error budget, you can move fast. When you've burned your error budget, you stop shipping new features and invest in reliability. The tradeoff is explicit, agreed-upon, and measurable.

---

## Key Concepts

| Concept | Definition |
| --- | --- |
| **SLI (Service Level Indicator)** | A quantitative measure of service behavior. Examples: request success rate, latency p99, data freshness. |
| **SLO (Service Level Objective)** | A target value for an SLI over a defined time window. Example: 99.9% of requests succeed over a 28-day rolling window. |
| **Error Budget** | The allowed amount of unreliability: 100% minus the SLO. At 99.9% SLO, you have 0.1% of requests (or 43.8 minutes/month) to spend. |
| **Toil** | Manual, repetitive, automatable operational work that scales with traffic. Toil is the enemy of engineering capacity. |
| **SLA (Service Level Agreement)** | A contractual commitment with external consequences. SLOs are internal targets; SLAs are external contracts. Always set SLOs more ambitious than your SLAs. |

---

## Execution Steps

### 1. Define SLIs

Identify what "good" looks like for your users. Good SLIs are:

- User-centric (measuring what users actually experience, not what's convenient to instrument)
- Measurable from existing telemetry
- Few in number (2-4 per service is typical)

Common SLI categories:

- **Availability**: fraction of valid requests that succeed
- **Latency**: fraction of requests faster than a defined threshold
- **Throughput**: rate of valid requests processed
- **Freshness**: how recent the data served to users is

### 2. Set SLOs

For each SLI, define a target and window:

- "99.9% of requests will return HTTP 200 over a 28-day rolling window"
- "95% of requests will complete in under 200ms over a 28-day rolling window"

SLO targets should be set based on user need and historical performance - not at 100% (unachievable) or arbitrarily tight (budget burns too fast on normal variation).

### 3. Implement Error Budget Tracking

Build or adopt a dashboard that shows:

- Current SLO performance vs. target
- Error budget remaining (and burn rate)
- Historical SLO performance trends

Alert on *error budget burn rate*, not raw SLI values. A brief spike that doesn't burn budget is noise. A slow degradation that burns budget steadily is a crisis.

### 4. Error Budget Policy

Define in writing what happens when error budget is depleted:

- Feature development is paused
- On-call team is authorized to reject new production changes
- Reliability work takes scheduling priority
- Policy reactivates when budget is replenished

This policy removes the politics from reliability conversations. Budget depleted = stop shipping. Budget healthy = move fast. The math decides, not the manager.

### 5. Toil Reduction

Track toil as a metric. SRE teams should spend no more than 50% of time on toil (the original Google heuristic). For each recurring manual task:

1. Document it as a runbook entry.
2. Identify whether it can be automated.
3. Prioritize automation proportional to toil cost.

### 6. Blameless Post-Mortems

After any SLO breach or significant incident, conduct a post-mortem:

- Document the timeline of events (what happened and when)
- Identify contributing factors (plural - failures are systemic, not individual)
- Define action items with owners and deadlines
- Share the post-mortem openly within the organization

Post-mortems are learning events, not accountability rituals.

---

## Failure Modes and Mitigations

| Failure Mode | Mitigation |
| --- | --- |
| SLOs set so tight that budget burns constantly | Recalibrate SLOs to reflect real user expectations, not engineering vanity |
| SLOs set so loose that they never catch real problems | Tighten gradually based on user complaint data and historical incidents |
| Error budget policy ignored under feature pressure | Escalate to engineering leadership; policy only works if it has teeth |
| Alert fatigue from too many low-priority pages | Alert on budget burn rate, not individual SLI violations; eliminate non-actionable alerts |
| Toil never decreases because automation is always "next quarter" | Track toil percentage as a reported team metric; make reduction a quarterly OKR |
