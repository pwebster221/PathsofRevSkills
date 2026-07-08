---
name: sdlc-controlled-release-gate
description: "Use during ship in regulated, audited, or extreme-risk environments where fully automated promotion is insufficient without governance. Activates when someone says \"who approves this release\", \"we need an audit trail or change board\", \"this is compliance-sensitive\", or when a bad release carries regulatory, legal, or safety cost. A deliberate, auditable risk-evaluation gate where authorized stakeholders accept responsibility — automating all that can be automated while reserving human judgment for what genuinely needs it."
stage: ship
posture: controlled-release-gate
tier: 2
role: skill
license: MIT
---
# Skill: Controlled Release Gate

## Lineage

The Controlled Release Gate posture draws from the ITIL Change Management framework (specifically the Change Advisory Board process), the formal gate reviews of the Rational Unified Process (RUP), and the risk management philosophy of the Spiral Model. It is the appropriate posture for environments where regulatory compliance, audit requirements, or extreme risk profiles make fully automated release pipelines insufficient without additional governance.

This posture does not mean "slow" or "manual for its own sake." It means deliberate, auditable, and accountable change management - and the goal is always to automate everything that can be automated, while reserving human judgment for decisions that genuinely require it.

---

## Core Principle

In regulated industries - finance, healthcare, government, aerospace - the cost of a bad release extends beyond user impact to regulatory fines, legal liability, and in some contexts, public safety. The release gate is a structured risk evaluation point where authorized stakeholders explicitly accept responsibility for the change entering production.

---

## Change Classification

Not all changes require the same ceremony. Classify before applying gates.

| Change Type | Description | Gate Process |
| --- | --- | --- |
| **Standard Change** | Pre-approved, low-risk, frequently repeated (config update, library patch, known procedure) | Automated gate only; no CAB required |
| **Normal Change** | Moderate risk; specific scope; requires review and explicit approval | Full release gate process |
| **Emergency Change** | Critical fix under time pressure; risk of waiting exceeds risk of change | Expedited gate with mandatory post-implementation review |

Expanding the Standard Change catalog over time reduces overhead without reducing governance.

---

## Execution Steps: Normal Change

### 1. Change Request Documentation

Create a formal Change Request (CR) containing:

- **What**: Precise description of what is changing (diff-level specificity, not vague summaries)
- **Why**: Business or technical justification
- **When**: Planned deployment window; maintenance window if user impact is expected
- **Risk Assessment**: Impact if the change fails; affected systems and user populations
- **Rollback Plan**: Specific, tested steps to revert. "We'll redeploy the previous version" is not a rollback plan.
- **Test Evidence**: Links to CI results, staging validation, security scan output, performance data

Store this in your change management system (ServiceNow, Jira, Linear).

### 2. Pre-Deployment Review

The Change Advisory Board (or equivalent governance body) reviews the CR. Required inputs:

- Completed CR with all fields populated
- Sign-off from team lead or technical lead
- Security review (if authentication, authorization, or data handling is affected)
- Performance impact assessment (if the change is traffic-sensitive)

Possible outputs: **Approved**, **Approved with conditions**, or **Rejected with feedback**.

### 3. Deployment Window Execution

During the approved window:

1. Notify stakeholders that the deployment window has opened.
2. Execute the deployment using the documented procedure. The procedure must be scripted - ad-hoc execution in production is not acceptable.
3. Run post-deploy verification checklist:
   - Smoke tests pass
   - Health check endpoints return expected responses
   - Key business metrics are within normal range
   - Monitoring dashboards show no anomalies

### 4. Go / No-Go Decision

The deployment lead makes an explicit decision after verification:

- **Go**: Close the change window. Mark CR as Implemented. Notify stakeholders.
- **No-Go**: Execute the rollback plan. Document precisely what failed and why. Open a new CR for the remediated change.

### 5. Post-Implementation Review

Within 48 hours, conduct a brief PIR:

- Did the deployment proceed as documented?
- Were there unexpected impacts?
- What should be improved in the process for next time?

Update the CR with PIR notes. This forms the audit trail.

---

## Acceleration Strategies

The Controlled Release Gate posture does not preclude automation. It defines the governance layer around it.

- **Auto-populate CR fields** from CI pipeline data: test results, diff summary, artifact hash, security scan output.
- **Pre-approve standard changes** in the change management system when defined pipeline gates pass.
- **Automate deployment execution** so the human approval is the gate, not the mechanism. A human approves; a machine deploys.
- **Integrate observability** into the Go/No-Go decision window with dashboards that populate automatically post-deploy.

The North Star: human judgment is applied only to decisions that genuinely require human judgment. Everything else is automated. Every gate that can be eliminated through confidence-building should eventually be eliminated.

---

## Failure Modes and Mitigations

| Failure Mode | Mitigation |
| --- | --- |
| CAB becomes a rubber-stamp ritual | Ensure reviewers have real authority and accountability; rotate membership; challenge under-reviewed approvals |
| Process overhead degrades team velocity | Expand Standard Change catalog aggressively; invest in automation; track and reduce DORA change failure rate as evidence of safety |
| Rollback plan is theoretical and untested | Require rollback procedure to be rehearsed in staging before CR approval is granted |
| Emergency change bypasses all gates and causes incident | Make post-implementation review mandatory; use findings to close the process gap that created the emergency |
