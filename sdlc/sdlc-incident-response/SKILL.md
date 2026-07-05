---
name: sdlc-incident-response
description: >-
  Use during sustain when production is degraded or down and the team needs to
  coordinate a fast, calm recovery and learn from it. Activates when someone says
  "we have an incident", "the system is down", "who's running this", "we're getting
  paged repeatedly", or when failures are recurring and unreliable and you need a
  repeatable command structure and blameless review rather than ad-hoc heroics.
stage: sustain
posture: incident-response
tier: 2
role: skill
license: MIT
---

# Skill: Incident Response

## Lineage

Modern incident response for software was codified in Google's *Site Reliability
Engineering* (Beyer et al., 2016), particularly its chapters on managing incidents
and postmortem culture, and operationalized by practitioner playbooks such as
PagerDuty's Incident Response documentation (response.pagerduty.com). It adapts the
Incident Command System (ICS) from emergency services — defined roles and a single
chain of command — and pairs it with the blameless postmortem tradition (John
Allspaw / Etsy). The discipline links directly to SRE error budgets: incidents are
how reliability debt comes due.

## Core Principle

**Restore service first, learn second — under clear command, without blame.** During
an incident the goal is mitigation, not root-cause elegance. Coordination beats
heroics: one person directs, others execute defined roles, communication is steady
and external. Afterward, a blameless review converts the event into systemic
improvement rather than individual fault.

## Key Concepts

- **Severity levels.** A pre-agreed scale (e.g. SEV1–SEV3) that sets urgency,
  who is paged, and comms cadence — decided by impact, not by guesswork mid-incident.
- **Roles.** *Incident Commander* (decides and directs, does not fix), *Ops/Tech
  Lead* (drives mitigation), *Communications Lead* (status to stakeholders/customers),
  *Scribe* (timeline). Small incidents collapse roles onto one person; large ones
  separate them strictly.
- **Lifecycle.** Detect → declare/classify → mitigate → resolve → review.
- **Blameless postmortem.** A written, systems-focused account with concrete,
  owned, tracked action items. Blamelessness exists to surface truth, not to excuse.

## Execution Steps

### 1. Declare and classify
Anyone can declare. Assign a severity and open a single coordination channel. Naming
the incident is what turns chaos into a managed response.

### 2. Assign command
Name an Incident Commander immediately. For larger incidents, split out Comms and
Scribe. The IC coordinates; they do not disappear into the keyboard.

### 3. Stabilize
Prioritize the fastest safe mitigation — roll back, fail over, disable a feature
flag, shed load — over diagnosing the underlying cause.

### 4. Communicate on a cadence
Post regular status updates internally and to affected users on a fixed interval,
even when the update is "still investigating." Silence costs more than bad news.

### 5. Resolve and verify
Confirm recovery against the signals that defined the incident — not just that the
alert cleared. Declare resolution explicitly and hand off any monitoring.

### 6. Blameless postmortem
Within a few days, write the timeline, contributing factors, and what made detection
or recovery slow. Produce specific, owned action items and track them to done.

## Tooling Reference

| Layer | Options |
|---|---|
| Alerting / on-call | PagerDuty, Opsgenie, Grafana OnCall |
| Incident coordination | incident.io, FireHydrant, Rootly, Slack war-room + bot |
| Status communication | Statuspage, Better Stack, hosted status pages |
| Observability | Grafana, Datadog, Honeycomb, Prometheus — for detection and verification |
| Knowledge | Runbooks linked from alerts; postmortem repository |

## Failure Modes and Mitigations

| Failure mode | Mitigation |
|---|---|
| No clear commander; everyone debugging | Mandate an IC on every SEV1/2; IC directs and does not fix |
| Heroics over coordination | Define roles up front; rotate the IC role so it isn't one person's burden |
| Blame culture suppresses facts | Strictly blameless postmortems; focus on systems and signals, never individuals |
| Postmortems with no follow-through | Action items are owned, dated, and tracked like any other work |
| Alert fatigue masks real incidents | Tune alerts to symptoms users feel; delete noisy alarms; link every alert to a runbook |
| Comms gaps during outage | Communications Lead posts on a fixed cadence, including "no change yet" |
