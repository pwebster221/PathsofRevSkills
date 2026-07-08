---
name: sdlc-outside-in-design
description: >-
  Use when the user-facing boundary should drive internal structure - when behavior is better understood than architecture, or when the team wants to avoid building infrastructure that the product does not actually need. Activates when someone asks how to design from the user's perspective, how to use acceptance criteria to guide design, or how to prevent internal complexity from growing beyond what external behavior requires. Draws on BDD's outside-in development philosophy, XP's customer-collaboration principle, and the practice of designing APIs and UIs before their implementations.
stage: design
posture: outside-in-design
tier: 2
role: skill
license: MIT
---
# Skill: Outside-In Design

## What this enables

Internal structure shaped by real use cases rather than theoretical elegance. An API or UI surface that is designed - and validated with stakeholders - before the implementation that serves it. Avoidance of infrastructure built for requirements that never materialized.

## Fit signals

- The user experience or API surface is the primary value delivered - the internals exist to serve it, not the other way around
- Behavior is better understood than architecture at the start of design
- Stakeholders can validate a UI prototype or API contract before implementation begins
- The team has previously built infrastructure "for the future" that was never used
- BDD-style scenarios already exist from Discovery and need to drive design

## Anti-signals

- The system is infrastructure-first (a database engine, a network protocol, a compiler) - the "outside" is a technical interface, not a user experience
- Multiple teams need structural alignment before any boundary can be defined (use `sdlc-architecture-first` first, then outside-in within each boundary)
- Data model correctness is the dominant design concern (use `sdlc-schema-first`)

## Core practice

Work from the **outside boundary inward**. The sequence:

1. Define observable behavior at the boundary (what a user or caller can do and what they see in response)
2. Design the boundary surface (UI wireframe, API contract, CLI interface)
3. Validate the boundary design with stakeholders before writing implementation
4. Let the internals emerge to satisfy the boundary - no more, no less

The BDD insight applied to design: the acceptance scenario is the spec. Design that cannot be connected to an acceptance scenario is speculative. Structure that cannot be exercised through the boundary is overhead.

## Key moves

1. **Write the acceptance test before designing the internals.** The acceptance test describes what a user accomplishes, expressed at the boundary level:

   - *Given* a user has items in their shopping cart
   - *When* they complete checkout
   - *Then* they receive an order confirmation with a reference number

   This scenario is now the design constraint. The internal design question becomes: what is the minimum structure needed to make this scenario pass?

2. **Prototype the boundary, not the internals.** A UI wireframe or a mock API (returning hard-coded data) lets stakeholders validate the design in hours rather than weeks. Real feedback on a prototype is worth more than any amount of upfront internal design.

3. **Drive the API from the calling code, not the serving code.** Write the client code that uses the API before writing the API that serves it. Code that is awkward to call is telling you the API design is wrong. Adjust the API, not the client.

4. **Implement only what acceptance tests require.** Once the boundary is defined, internal structure is grown exactly as far as the acceptance tests demand. Each layer added must be traceable to a scenario. Layers that cannot be traced are premature generalization.

5. **Keep the boundary stable while the internals evolve.** The observable interface is the contract with the outside world. Refactor internals freely; treat boundary changes as breaking changes requiring deliberate versioning.

## Example

A team is building a document search feature. Rather than designing a search engine internally and then exposing it, they start outside-in:

**Step 1 - acceptance scenario:**

- Given a user enters "invoice Q3 2025" in the search box
- When results appear
- Then the top result is the most recently modified document containing those terms and each result shows title, modified date, and a content excerpt

**Step 2 - boundary design:**

- A search input component with debounced queries
- `GET /search?q={query}` returning `[{id, title, modified_at, excerpt}]`
- A results list component that renders the response

**Step 3 - stakeholder validation:**

- A Figma mockup of the UI and a mock API returning dummy data are reviewed in a 30-minute session. Stakeholders ask for a "filter by date range" option not in the original scenario. A new scenario is added.

**Step 4 - internal design:**

- Only now does the team ask: what search index, ranking algorithm, and excerpt extraction is needed to satisfy both scenarios? The answer is constrained and specific, not speculative.

## AI leverage points

- **Scenario-to-API translation:** take a set of BDD scenarios and ask the LLM to derive the minimum API surface that would support them. Use as a draft for team review.
- **Client code simulation:** describe the API design and ask the LLM to write client code for the primary use case. Awkward client code is a design signal.
- **Prototype acceleration:** use GenAI to generate UI component stubs or mock API responses rapidly for stakeholder validation sessions.

## Connects to

- **Upstream:** `sdlc-design` - this is one posture within the Design stage; `sdlc-conversational-elicitation` (scenarios produced in Discovery drive this stage)
- **Downstream:** `sdlc-bdd` (Build posture that operationalizes this at the implementation level), `sdlc-tdd` (internal implementation driven by tests at the unit level)
- **Lateral:** `sdlc-schema-first` (the API surface defined here becomes a schema contract), `sdlc-emergent-design` (internals emerge from the outside-in constraint)
