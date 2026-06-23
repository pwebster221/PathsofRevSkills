---
name: sdlc-sustain
stage: sustain
tier: 1
role: navigator
license: MIT
---
# Stage 6 - Sustain: Navigator

## Purpose

Sustain is where software lives. Ship was a moment. Sustain is the indefinite ongoing relationship between a system and the world it operates in. It encompasses reliability engineering, operational health, architectural evolution, and the continuous reduction of toil and entropy.

Most SDLC models treat sustain as an afterthought - a maintenance mode entered when "real development" is done. This is wrong. For long-lived systems, sustain consumes the majority of engineering effort over the system's lifetime. The goal of this Navigator is to match your current operational context to the posture that most effectively keeps the system healthy, trustworthy, and evolvable.

Sustain postures are not mutually exclusive. Unlike earlier stages, a team may operate multiple postures simultaneously - running an SRE/SLO posture as the baseline operational mode while also running a Chaos Engineering posture to proactively discover failure modes.

---

## Signal Definitions

| Signal | What It Measures | Values |
| --- | --- | --- |
| **operational_maturity** | Quality of observability, alerting, runbooks, and on-call practices | low / medium / high |
| **system_criticality** | Impact of outage: user harm, revenue, safety, or regulatory exposure | low / medium / high |
| **toil_level** | Volume of repetitive, automatable manual operational work | low / medium / high |
| **change_velocity** | How frequently the system is modified in production | low / medium / high |
| **failure_mode** | The most pressing operational problem right now | unreliable / slow / brittle / cluttered / unclear |

---

## Routing Table

| operational_maturity | system_criticality | Primary Concern | Recommended Posture |
| --- | --- | --- | --- |
| medium-high | high | Reliability and uptime | SRE / SLO-Driven Operations |
| any | any | Active incident or recurring failures | Incident Response |
| any | any | Technical debt accumulating; architecture degrading | Evolutionary Architecture |
| low-medium | any | Too much manual work; unclear priorities; reactive firefighting | Kanban Operations |
| high | high | System is stable; proactively finding hidden failure modes | Chaos Engineering |

> **Concurrence rule:** SRE/SLO-Driven Operations is the recommended *baseline* for any system with high criticality. Other postures are activated on top of it when a specific concern demands focused attention.

---

## Signal Elicitation Prompts

- *"Do you have defined SLOs, and do you know right now if you're meeting them?"* -> operational_maturity, system_criticality
- *"What percentage of your operational work is repetitive tasks a script could do?"* -> toil_level
- *"How often do you get paged for the same type of failure?"* -> failure_mode
- *"Is your system getting harder to change over time? Are you slowing down?"* -> change_velocity, failure_mode
- *"How confident are you that your system will recover correctly from a dependency failure you've never seen before?"* -> chaos_engineering readiness

---

## Stage Boundaries

**Entry condition:** Ship stage complete. System is live in production with active traffic and observability enabled.

**Exit condition:** Sustain is open-ended. It concludes when the system is intentionally decommissioned or replaced. At decommission, a structured wind-down (data migration, dependency notification, traffic rerouting) is required before closure.
