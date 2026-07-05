---
name: sdlc-design
description: >-
  Use when transitioning from understanding what to build toward deciding how to structure it. Activates when the team needs to make architectural decisions, define system boundaries, plan component relationships, or establish interface contracts before or during implementation. Also activates when someone asks how to structure code, what pattern to use, how to split responsibilities across services, or how to document a design decision. Presents posture options based on context signals and routes to the appropriate methodology skill.
stage: design
tier: 1
role: navigator
license: MIT
---
# SDLC Navigator: Design

Design is the stage where structure is decided. Not all of it - the right amount for what is known right now. The goal is to make load-bearing decisions deliberately while leaving room for what will only be understood through building.

## Read the Room First

| Signal | Questions to ask |
| --- | --- |
| **Coupling risk** | How expensive is a wrong structural decision? Can it be changed cheaply later, or will it propagate everywhere? |
| **Architecture complexity** | Is this a single module, a service, or a distributed system spanning multiple teams? |
| **Interface criticality** | Do other systems or teams depend on the contracts being defined here? |
| **Team topology** | Is one team building the whole thing, or do boundaries need to match organizational seams? |
| **Design fluidity** | Is the right structure likely to emerge from building, or does it need to be established before building can proceed? |

## Posture Options

### 1. Emergent Design

**When:** Coupling risk is low or recoverable, the system is small enough for one team, and the right structure is more likely to emerge from working code than from upfront planning. Favors reversible decisions. **What it enables:** Organic architecture that reflects actual requirements rather than predicted ones; continuous refactoring as the real shape becomes clear. **Load skill:** `sdlc-emergent-design`

---

### 2. Architecture-First

**When:** Multiple teams need to align on boundaries, structural decisions will be expensive to reverse, or the system spans services with independent deployment and ownership. **What it enables:** Documented architectural decisions with explicit rationale; team boundaries that match system seams; a shared map that prevents independent teams from making conflicting structural choices. **Load skill:** `sdlc-architecture-first`

---

### 3. Schema-First

**When:** Data model correctness is the primary design concern, API contracts need to be provably consistent, or the system is data-intensive with complex relationships and invariants. **What it enables:** A precise, agreed data model and interface contract before any implementation begins; implementations in different languages or services that are guaranteed to be compatible. **Load skill:** `sdlc-schema-first`

---

### 4. Outside-In Design

**When:** The user-facing boundary (UI, API, CLI) should drive internal structure; behavior is better understood than architecture; and the team wants to avoid building infrastructure that the product does not actually need. **What it enables:** Internal design shaped by real use cases rather than theoretical structure; API surfaces and UIs that are designed before the implementation that serves them. **Load skill:** `sdlc-outside-in-design`

---

### 5. AI-Assisted Design Exploration

**When:** The design space is large, multiple structural approaches are viable, trade-off analysis would benefit from rapid option generation, or the team needs to evaluate patterns faster than manual research allows. **What it enables:** A wide set of design options generated quickly for human evaluation; pattern matching against known solutions; structured trade-off analysis before committing to an approach. **Load skill:** `sdlc-ai-design`

---

## Postures Can Combine

The most common combination: use **Outside-In Design** to establish the behavioral boundary, then **Architecture-First** to make the structural decisions that boundary implies, and **Emergent Design** for all internals that do not cross team or service seams.

## Connects to

- **Upstream:** `sdlc-discovery` - design decisions are grounded in what discovery produced
- **Downstream:** `sdlc-build` - the chosen structure is what the Build stage implements against
- **Parallel:** `sdlc-formal-specification` (if critical interfaces need mathematical contracts, this runs alongside Design, not before it)
