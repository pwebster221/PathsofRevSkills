---
name: sdlc-build
description: >-
  Use when the team is writing working software - translating understood requirements into running code. Activates when someone says "how should we write this", "what's the best approach for building X", "how do we structure this code", or when implementation is about to begin. Reads context signals and routes to the methodology posture that fits the specific work, team, and risk profile. Not all code is the same; not all code should be built the same way.
stage: build
tier: 1
role: navigator
license: MIT
---
# SDLC Navigator: Build

Build is where intent becomes software. The challenge is not just writing code that works - it is writing code that can be understood, changed, and relied upon by the people who come after. The right posture depends on what you know, who is in the room, and what the cost of being wrong looks like.

## Read the Room First

| Signal | Questions to ask |
| --- | --- |
| **Spec clarity** | Do we know what "correct" looks like before we start writing? |
| **Criticality** | What is the cost if this code is wrong in production? |
| **Novelty** | Is this well-understood territory or are we learning as we go? |
| **Collaboration mode** | Who is available, and how are they working together? |
| **Iteration speed** | Do we need to explore quickly, or prove correctness carefully? |

## Posture Options

### 1. Test-Driven Development (TDD)

**When:** The design is not yet clear, refactoring risk is real, and you need the tests to drive the architecture into existence. Works solo or in pairs. **What it enables:** Design that emerges from use rather than speculation; a permanent safety net that makes refactoring safe; code that is testable by construction. **Skill doc:** `sdlc-tdd`

---

### 2. Behavior-Driven Development (BDD)

**When:** Stakeholders and developers need shared language about what the software should do. Stories exist or can be elicited. The team needs executable specifications that non-technical contributors can read and verify. **What it enables:** Living documentation that stays in sync with the code; acceptance criteria expressed as scenarios that both product and engineering can own; test coverage that maps directly to stakeholder value. **Skill doc:** `sdlc-bdd`

---

### 3. Mob Programming

**When:** Knowledge is siloed, onboarding is a bottleneck, shared ownership matters more than individual velocity, or the problem is complex enough that no single person should solve it alone. **What it enables:** Continuous code review as the code is written; elimination of knowledge silos; dramatically accelerated onboarding; collective ownership of every line. **Skill doc:** `sdlc-mob-programming`

---

### 4. GenAI-Assisted Development

**When:** Exploration speed matters, the domain is large or poorly mapped, a single contributor needs to move fast, or the team wants to leverage LLMs for code generation, gap analysis, or patch validation. **What it enables:** Faster first-pass code generation; LLM-driven localization and repair for known defect classes; CoT prompting to surface edge cases before they reach production; RAG-grounded suggestions that stay anchored to the actual codebase. **Skill doc:** `sdlc-genai-assisted`

---

### 5. Cleanroom

**When:** Criticality is high, the cost of a defect in production is unacceptable, the specification is already well-defined, and the team has the discipline to verify correctness before compiling rather than discover it through debugging. **What it enables:** Software correct by construction; defect rates measurable in fractions of a percent; quality certified through statistical usage testing rather than assumed through manual QA. **Skill doc:** `sdlc-cleanroom`

---

## Signal Quick-Reference

| If you see this... | Try this posture |
| --- | --- |
| Design unclear, refactoring risk high | TDD |
| Stakeholders need to read the spec | BDD |
| Knowledge silos, onboarding bottleneck | Mob Programming |
| Need speed, large domain, solo contributor | GenAI-Assisted |
| High criticality, correctness must be proven | Cleanroom |
| Mixed: exploratory + quality-critical | GenAI-Assisted for localization, Cleanroom for implementation |
| Mixed: team alignment + design clarity | Mob Programming + TDD in rotation |

## Stage Connections

- **Feeds from:** `sdlc-design` (architecture and contracts become the build input)
- **Feeds into:** `sdlc-verify` (what build produces, verify tests)
- **Runs alongside:** `sdlc-verify` in TDD and BDD postures (test and build are inseparable)
