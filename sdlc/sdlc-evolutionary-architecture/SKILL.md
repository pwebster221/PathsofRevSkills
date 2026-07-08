---
name: sdlc-evolutionary-architecture
description: "Use during sustain to keep a long-lived architecture able to change safely, via small continuous improvements guided by fitness functions rather than a big redesign. Activates when someone says \"the architecture is drifting or decaying\", \"should we do a big rewrite\", \"how do we evolve this safely\", or when architectural qualities must be protected over time. Treats architecture as a continuous series of decisions, not a one-time one — fitness functions objectively detect drift from intended qualities."
stage: sustain
posture: evolutionary-architecture
tier: 2
role: skill
license: MIT
---
# Skill: Evolutionary Architecture

## Lineage

Evolutionary Architecture was systematized by Neal Ford, Rebecca Parsons, and Patrick Kua in *Building Evolutionary Architectures* (O'Reilly, 2017), building on the continuous refactoring philosophy of Extreme Programming and the architectural fitness function concept from the evolutionary computation field. The central argument: in a world of continuous change, designing an architecture that is "finished" is less valuable than designing an architecture that can *evolve* safely.

This posture is the architectural expression of the Sustain stage. Systems don't degrade because people are careless - they degrade because architecture is treated as a one-time decision rather than a continuous practice.

---

## Core Principle

> "Architecture is not a single decision made at the start. It is a continuous series of decisions made across the lifetime of a system."

The antidote to architectural decay is not a "big redesign" - those projects fail at a high rate, taking years and delivering systems that are already outdated on arrival. The antidote is making small, continuous architectural improvements guided by fitness functions that objectively detect when the architecture is drifting from its intended qualities.

---

## Key Concepts

| Concept | Definition |
| --- | --- |
| **Fitness Function** | An automated check that evaluates a specific architectural characteristic. Like a test for the architecture itself. |
| **Architectural Characteristic** | A quality attribute the architecture must maintain: performance, scalability, security, modularity, deployability, etc. |
| **Incremental Change** | Architectural evolution applied in small, safe steps rather than big-bang rewrites |
| **Coupling** | The degree to which components depend on each other. Low coupling enables independent evolution. |
| **Guided Evolution** | Using fitness functions to ensure architectural changes move toward, not away from, desired qualities |

---

## Fitness Function Examples

Fitness functions make architectural constraints executable and automatically verifiable:

| Architectural Concern | Fitness Function |
| --- | --- |
| Layered architecture: UI must not import infrastructure | Linting rule / ArchUnit test that fails CI if the violation exists |
| Performance: API latency must remain under 200ms p99 | Load test in CI that fails if threshold is exceeded |
| Security: no new critical CVEs in dependencies | Security scan in CI pipeline |
| Modularity: service A must not directly query service B's database | Integration test / schema access policy that detects cross-boundary data access |
| Deployability: build must complete in under 10 minutes | CI build time tracked and alerted on threshold breach |

---

## Execution Steps

### 1. Identify the Current Architectural Concerns

Conduct a structured architectural review (not a blame session) to identify:

- Where is the system most painful to change?
- Where do bugs cluster? (Bug distribution often maps to poorly bounded modules)
- What constraints are currently violated that were originally intended?
- What quality attributes are degrading over time?

Document findings as architectural debts with estimated impact.

### 2. Define Fitness Functions for Critical Characteristics

For each identified concern, define a fitness function:

- What is the measurable quality attribute?
- What is the threshold that must not be crossed?
- How will it be checked? (CI step, runtime monitor, scheduled audit)
- Who owns it?

Start with 2-3 high-value fitness functions. Add incrementally.

### 3. Integrate Fitness Functions into the Build Pipeline

Fitness functions must run automatically. A fitness function that requires manual execution will be skipped under pressure. Integrate into CI/CD so that architectural violations fail the build.

### 4. Incremental Architectural Improvement

Apply the Strangler Fig pattern for significant architectural changes:

1. Route a subset of traffic or functionality to the new implementation while the old one remains.
2. Gradually migrate more functionality to the new implementation.
3. When migration is complete, delete the old implementation.

Never attempt to rewrite and migrate simultaneously under time pressure. Incremental migration with a working system at every step is the safe path.

### 5. Technical Debt Prioritization

Maintain a technical debt register. Prioritize debt items by:

- **Pain multiplier**: How much does this debt slow down current development?
- **Risk**: What's the failure mode if this debt is left unaddressed?
- **Coupling**: Does this debt prevent architectural evolution in other areas?

Treat high-priority debt items as first-class work items in sprint planning, not as "we'll get to it" afterthoughts.

---

## Anti-Patterns to Avoid

| Anti-Pattern | Symptom | Corrective Action |
| --- | --- | --- |
| Big Rewrite | "We need to start over" | Apply Strangler Fig instead; rewrites rarely succeed |
| Architecture by Astronaut | Theoretical purity over practical evolution | Fitness functions ground architecture in measurable outcomes |
| Debt Ignored Until Crisis | "We don't have time to refactor" | Schedule debt work as a first-class team metric (20% capacity) |
| Premature Abstraction | Over-engineering for a future that doesn't arrive | Defer architectural decisions until the point of maximum information |

---

## Failure Modes and Mitigations

| Failure Mode | Mitigation |
| --- | --- |
| Fitness functions become stale and are ignored | Review fitness functions quarterly; delete ones that no longer map to real architectural concerns |
| Refactoring breaks existing behavior | Maintain comprehensive automated test coverage as the safety net for all refactoring |
| Architectural improvements stall because "there's no time" | Make the cost of NOT evolving visible: track how long changes take in high-debt areas vs. low-debt areas |
