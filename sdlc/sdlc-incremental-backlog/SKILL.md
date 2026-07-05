---
name: sdlc-incremental-backlog
description: >-
  Use during discovery and throughout delivery when requirements will evolve, scope needs to be managed iteratively, or the team needs to start building before everything is known. Activates when someone asks how to prioritize work, what to build next, how to break down a feature, or when a project needs ongoing planning that adjusts as learning accumulates. Draws on Scrum, Kanban, SAFe, and Lean to offer a flexible living backlog practice that avoids both over-planning and under-planning.
stage: discovery
posture: incremental-backlog
tier: 2
role: skill
license: MIT
---
# Skill: Incremental Backlog

## What this enables

A living, prioritized list of work that reflects current understanding - not a frozen requirements document. The backlog grows and shrinks as the team learns. It enables delivery to start before everything is known and planning to improve as feedback arrives from real users and real code.

## Fit signals

- Requirements will evolve across delivery cycles
- The team works iteratively - delivery happens in time-boxed or flow-based increments
- "Good enough to start" beats "complete before starting"
- The cost of delay outweighs the risk of building something slightly wrong
- Multiple stakeholders need visibility into what is being worked on and why

## Anti-signals

- The problem requires a complete, provable specification before any implementation (use `sdlc-formal-specification` instead)
- The work is a single well-understood task that does not benefit from iterative planning
- All requirements are stable and contractually fixed at the outset

## Core practice

A backlog item is a **promise to have a conversation**, not a specification. The detail captured at any point should match how soon the work will be done - items near the top are refined and understood; items further down are sketches.

Two primary rhythms exist: **time-boxed** (Scrum-style sprints with a defined planning cadence) and **flow-based** (Kanban-style continuous pull with WIP limits). The choice depends on team preference and delivery context, not doctrine.

## Key moves

1. **Express items as user stories, not tasks.** Format: "As \[who\], I want \[what\], so that \[why\]." The "so that" is the most important part - it connects the item to value and prevents gold-plating.

2. **Apply INVEST criteria before pulling an item into active work.**

   - *Independent:* can be built without depending on another unfinished item
   - *Negotiable:* the how is open; only the what and why are fixed
   - *Valuable:* delivers something a stakeholder actually cares about
   - *Estimable:* the team can roughly size it
   - *Small:* completable within one cycle or a few days
   - *Testable:* there exists a clear way to know it is done

3. **Refine just-in-time, not just-in-case.** Spend no more than 10% of team capacity on backlog refinement. Detail stories only when they are 2-3 items from the top of the queue. Over-refinement wastes effort on items whose requirements will change before they are built.

4. **Limit work in progress.** Whether using sprints or continuous flow, finishing one thing before starting another improves throughput and reduces context-switching cost. Kanban: set explicit WIP limits per stage. Scrum: commit to fewer items per sprint than feels comfortable.

5. **Review and re-prioritize regularly.** The backlog is wrong the moment you stop touching it. Product owners, stakeholders, and the team should inspect and adapt the order at each planning cycle based on what was learned in the previous one.

6. **Use a Definition of Done consistently.** Every item has the same exit condition: tested, reviewed, integrated, releasable. Partial "done" is not done. This is where backlog practice connects to delivery quality.

## Example

A team is building a notification system. Initial backlog items arrive as: "Users need to get notified about things." Through refinement this becomes:

- "As a registered user, I want an email when my order ships, so that I know when to expect delivery." \[High priority - INVEST-ready\]
- "As a user, I want to manage my notification preferences, so that I only receive messages I care about." \[Medium - needs further conversation\]
- "As an admin, I want a notification audit log." \[Low - rough sketch only\]

The team pulls only the first item into the current sprint. The second is discussed in refinement. The third stays a sketch until business need drives it higher. Three months later, the third item is dropped - it was never actually needed.

## AI leverage points

- **Story decomposition:** give an LLM a large feature description and ask it to split it into INVEST-compliant stories. Review the output for missed dependencies and misaligned value statements.
- **Acceptance criteria generation:** provide a story and ask for 3-5 Given/ When/Then scenarios. Use as conversation starters with stakeholders, not as finished specifications.
- **Priority framing:** describe two items and ask the LLM to argue the case for prioritizing each, then use that framing to sharpen your own reasoning.

## Connects to

- **Upstream:** `sdlc-discovery` - backlog items emerge from elicitation
- **Downstream:** `sdlc-build` - items pulled from the top feed directly into whichever Build posture fits the work
- **Lateral:** `sdlc-conversational-elicitation` (produces items), `sdlc-bdd` (refines acceptance criteria into executable tests)
