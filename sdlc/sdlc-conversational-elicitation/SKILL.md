---
name: sdlc-conversational-elicitation
description: >-
  Use during discovery when requirements are unclear, stakeholders are available, or the team needs to convert vague intent into concrete testable examples. Activates when someone says "what should this actually do", "can we talk through the requirements", or when a feature needs to be understood before design begins. Draws on BDD scenario thinking and XP customer collaboration to build shared language between technical and non-technical contributors without over-formalizing too early.
stage: discovery
posture: conversational-elicitation
tier: 2
role: skill
license: MIT
---
# Skill: Conversational Elicitation

## What this enables

The ability to turn ambiguous intent into concrete understanding through structured conversation - without requiring formal documentation, UML, or complete specifications before work can begin. The output is shared language and concrete examples, not a requirements document.

## Fit signals

- Stakeholders can participate in discovery, not just hand over a spec
- Requirements are likely to shift as understanding grows
- The domain is business- or user-facing, not safety-critical
- The team is small enough for conversation to be the primary coordination mechanism

## Anti-signals

- Requirements must be provably complete before implementation begins (use `sdlc-formal-specification` instead)
- Stakeholders are unavailable or cannot articulate what they need
- The feature touches a formally-specified interface requiring mathematical consistency

## Core practice

Elicitation through **concrete examples** rather than abstract rules. The BDD insight is that stakeholders understand examples far better than specifications - and that examples, once written, become executable tests. The XP principle underneath is "customer on-site": the people who know what is needed are part of the team, not a separate constituency to be managed.

## Key moves

1. **Start with a story, not a requirement.** Ask "tell me about a time when a user would need this" rather than "what should the system do." Narrative generates examples; direct questioning generates wish lists.

2. **Use Given/When/Then to make examples concrete.** Once a scenario emerges, structure it:

   - *Given* \[the context that must be true\]
   - *When* \[the action the user or system takes\]
   - *Then* \[the observable outcome that signals success\] This is not about any specific tool - it is a thinking format that forces precision without requiring formalism.

3. **Explore the edges before committing to the center.** Ask "what happens if..." and "what would make this wrong?" Edge cases reveal assumptions the center hides. A scenario that breaks a Given/When/Then is often more informative than one that passes cleanly.

4. **Keep examples visible, not buried in a document.** Physical or shared visual space keeps conversation alive. Documents close conversation; visible examples invite challenge and refinement.

5. **Stop when examples start repeating.** Discovery is done when new scenarios stop teaching the team anything new. That is the signal to move to design - not a word count or a page count.

## Example

A feature request: "users should be able to reset their password." As stated, this is underspecified. Conversational elicitation turns it into:

- *Given* a registered user who has forgotten their password *When* they request a password reset *Then* they receive an email with a reset link valid for 24 hours

- *Given* a user who clicks a reset link after 24 hours have passed *When* they try to set a new password *Then* they see an error and are prompted to request a new link

- *Given* a user who has already used a reset link *When* they try to use the same link again *Then* the link is rejected regardless of expiry time

Three examples. Two edge cases surfaced. The conversation that produced these took 15 minutes and prevented at least two engineering assumptions from reaching production unchallenged.

## AI leverage points

- **Generate edge cases:** prompt an LLM with the core scenario and ask "what are five ways this could go wrong or be misunderstood?" Use the output as conversation starters, not accepted truth.
- **Multi-persona simulation:** use `sdlc-ai-requirements` to role-play different user personas simultaneously, generating scenarios from multiple viewpoints at speed.
- **Translate prose to scenarios:** use an LLM to convert existing requirements documents into Given/When/Then format as a starting point for human review - never as a final output.

## Connects to

- **Upstream:** `sdlc-discovery` (this is one posture within that stage)
- **Downstream:** `sdlc-bdd` (scenarios produced here become the test specification in the Build stage)
- **Lateral:** `sdlc-incremental-backlog` (examples map naturally to backlog items), `sdlc-ai-requirements` (AI accelerates example generation at scale)
