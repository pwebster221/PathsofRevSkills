---
name: sdlc-discovery
description: >-
  Use at the start of any software work when the team needs to understand what to build before building it. Activates whenever requirements are being gathered, a problem needs defining, stakeholders need aligning, or scope needs bounding. Also activates when someone says "we need to figure out what X should do", "what are the requirements for", or "where do we even start with". Presents posture options based on context signals and routes to the appropriate methodology skill.
stage: discovery
tier: 1
role: navigator
license: MIT
---
# SDLC Navigator: Discovery

Discovery is the stage where understanding is built before implementation begins. The goal is not to produce a perfect specification - it is to reach sufficient shared understanding to move forward without avoidable rework.

## Read the Room First

Before choosing a posture, assess these signals:

| Signal | Questions to ask |
| --- | --- |
| **Clarity** | How well-understood is the problem? Does anyone know what "done" looks like? |
| **Criticality** | What is the cost of a wrong assumption surviving into production? |
| **Stakeholder availability** | Can the people who know what they want be in the room? |
| **Formality needed** | Do contracts, APIs, or safety guarantees need to be provable? |
| **Scale** | One team on one feature, or many teams aligning across a program? |

## Posture Options

### 1. Conversational Elicitation

**When:** Stakeholders are available, requirements are fuzzy or emergent, the domain is business/UX-facing, and iteration is expected. **What it enables:** Shared language between technical and non-technical contributors; requirements expressed as concrete examples rather than abstract statements. **Load skill:** `sdlc-conversational-elicitation`

---

### 2. Incremental Backlog

**When:** Requirements will evolve across delivery cycles, the team works iteratively, and "good enough to start" beats "complete before starting". **What it enables:** A living prioritized list that captures intent without over-specifying implementation; planning that adjusts as learning accumulates. **Load skill:** `sdlc-incremental-backlog`

---

### 3. Formal Specification

**When:** High criticality, low tolerance for ambiguity, formal contracts or safety guarantees are required, or downstream systems depend on precise interface definitions. **What it enables:** Mathematical precision in requirements; a specification that can be used to verify implementation correctness, not just check functionality. **Load skill:** `sdlc-formal-specification`

---

### 4. AI-Assisted Exploration

**When:** The problem space is large or poorly understood, there are many hidden stakeholder needs to surface, or the team needs to rapidly map a complex domain before committing to an approach. **What it enables:** Accelerated elicitation using multi-agent simulation of stakeholder roles; surfacing edge cases and conflicts early at scale. **Load skill:** `sdlc-ai-requirements`

---

## Postures Can Combine

These are not mutually exclusive. A common pattern: start with **Conversational Elicitation** to develop shared language, harden the most critical interfaces with **Formal Specification**, and maintain an **Incremental Backlog** for everything else.

## Connects to

- **Upstream:** None - this is the entry point
- **Downstream:** `sdlc-design` - take discovery outputs into structural decisions
- **Parallel:** `sdlc-build` can begin on well-understood areas while discovery continues elsewhere
