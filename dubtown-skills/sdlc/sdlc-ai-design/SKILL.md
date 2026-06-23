---
name: sdlc-ai-design
description: >-
  Use when the design space is large and multiple structural approaches are viable, when trade-off analysis would benefit from rapid option generation, or when the team needs to evaluate patterns faster than manual research allows. Activates when someone asks what architectural pattern fits a problem, how to evaluate competing design options, or how to explore a design space before committing. Draws on GenAI's role in software design (Accenture/DFKI), LLM-based code and architecture generation, and Chain-of-Thought prompting for structured trade-off reasoning. Human evaluation and decision-making are mandatory.
stage: design
posture: ai-design
tier: 2
role: skill
license: MIT
---
# Skill: AI-Assisted Design Exploration

## What this enables

A wide set of design options generated quickly for human evaluation. Pattern matching against known solutions at a speed manual research cannot match. Structured trade-off analysis that surfaces consequences the team has not considered before committing to an approach.

## Fit signals

- Multiple viable structural approaches exist and the team is uncertain which to choose
- The problem is well-understood but the solution space is large
- Time pressure makes manual exploration of all options impractical
- The team lacks deep expertise in a relevant domain (distributed systems, security patterns, data architecture) and needs to survey options before deciding
- Existing patterns exist in the industry and the team needs to find them

## Anti-signals

- The design problem is novel enough that AI training data does not contain relevant patterns (AI will hallucinate plausible-sounding but wrong solutions)
- A decision has already been made and the team is looking for validation, not exploration (this produces confirmation bias, not options)
- The team has the expertise to evaluate all options manually and time is not a constraint

## Core practice

**Option generation followed by human decision.** The AI's role is to produce a structured set of alternatives with stated trade-offs. The team's role is to evaluate those alternatives against their specific context and constraints. The AI does not make the architectural decision.

Two primary modes:

- **Breadth exploration:** generate many options at low detail to identify the viable design space before committing to depth
- **Depth analysis:** take a shortlisted option and stress-test it - find the failure modes, the scaling limits, the security implications, the maintenance cost

## Key moves

1. **Frame the problem with constraints before asking for options.** A prompt that says "how should I design this system?" produces generic output. A prompt that says "I need to design a notification system that handles 10k sends/second, must be resumable on failure, and must not store message content after delivery - what are three viable architectural approaches?" produces useful options. Constraints are not limitations on the AI - they are the input that makes the output relevant.

2. **Ask for options in adversarial pairs.** For each option generated, ask the AI to argue both for and against it. This structure prevents the common failure mode of AI presenting one option as obviously correct.

3. **Use Chain-of-Thought for trade-off analysis.** Ask the AI to reason step by step through the implications of a design choice: "If we use an event-driven architecture here, walk through what happens when a consumer is unavailable for 6 hours. What accumulates, what fails, what recovers automatically, and what requires operator intervention?" CoT produces specific, actionable trade-off analysis rather than generic pros/cons lists.

4. **Ground AI options in your actual context.** Use RAG where possible: inject your existing architecture diagrams, ADRs, and technology constraints into the prompt. Options that conflict with your existing context are filtered out before they reach the evaluation table, not after.

5. **Treat AI output as a structured first draft.** The output of AI design exploration is input to a team design session, not output from it. The session evaluates, modifies, and decides. The AI's role ends at option generation.

## Example

A team is designing the data synchronization layer between a mobile app and a backend. They know they need offline support but have not chosen an approach.

They prompt with constraints: "Mobile app with offline-first requirement. Backend is a REST API. Users make on average 5 writes per session. Conflicts occur in roughly 2% of syncs. Server must be the source of truth. Give three approaches with their trade-offs."

The AI produces:

1. **Last-write-wins with server timestamp:** simple, loses concurrent edits, appropriate for low-conflict domains
2. **Operational transforms:** preserves all edits, high implementation complexity, mature for text editing, less so for structured data
3. **CRDTs (Conflict-free Replicated Data Types):** mathematically correct, library support exists, data model must be designed around CRDT properties

The team evaluates all three against their 2% conflict rate, their data model, and their team's expertise. They choose option 1 with a conflict notification UI because 2% conflicts with last-write-wins is an acceptable product trade-off given their user research. The AI gave them the option set; the team made the decision.

## AI leverage points

- **Pattern library traversal:** describe a class of problem and ask the LLM to survey known architectural patterns that address it, with examples from real systems
- **Failure mode analysis:** describe a proposed design and ask "what are the five most likely ways this design fails in production?"
- **Code prototype:** ask the LLM to sketch a minimal implementation of each option so the team can read actual code rather than prose descriptions when evaluating

## Connects to

- **Upstream:** `sdlc-design` - this is one posture within the Design stage
- **Downstream:** whichever Build posture implements the chosen design
- **Lateral:** `sdlc-architecture-first` (ADRs capture the decision that AI exploration informed), `sdlc-ai-requirements` (same AI-first posture applied to the Discovery stage)
