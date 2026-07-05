---
name: sdlc-acceptance-walkthrough
description: >-
  Use during verify when stakeholders need to see and validate what was built before it progresses. Activates when someone asks "how do we get sign-off", "do product need to review this", "how do we confirm the stakeholder actually wanted this", or when a sprint review, demo, or formal acceptance event is scheduled. Draws on BDD scenario execution, Scrum Sprint Review, and stakeholder alignment practices to produce human-validated confirmation that the software meets its intended purpose.
stage: verify
posture: acceptance-walkthrough
tier: 2
role: skill
license: MIT
---
# Skill: Acceptance Walkthrough

## What this enables

Human confirmation that the software does what stakeholders actually wanted -
not just what was specified. The gap between a correct implementation and a
correctly interpreted requirement is one of the most common sources of
production disappointment. An acceptance walkthrough closes that gap before
the code ships, not after.

## Fit signals

- Stakeholders are available and their sign-off carries decision-making authority
- BDD scenarios or acceptance criteria exist and can structure the walkthrough
- The team has experienced "we built it right, but it wasn't what they wanted"
- The work is business-facing, UX-facing, or has regulatory significance
- A sprint review, milestone demo, or formal acceptance event is the delivery mechanism

## Anti-signals

- No accessible stakeholder - the team is working on infrastructure with no
  user-visible behaviour (use `sdlc-ci-pipeline` as the sole gate)
- The required validation is formal correctness against a specification, not
  stakeholder opinion (use `sdlc-structured-inspection` instead)

## Core practice

The acceptance walkthrough is a **structured conversation**, not a presentation.
The team demonstrates the software against its acceptance criteria and the
stakeholders respond with confirmation, correction, or clarification.

Two modes:

**Scenario-driven (preferred when BDD exists):** Walk through each acceptance
scenario in sequence. For each scenario: state the Given/When/Then, demonstrate
the system behaviour, and ask the stakeholder to confirm the Then matches their
intent. A passing test is not sufficient - the stakeholder must agree the test
describes what they actually wanted.

**Demo-driven (when BDD does not exist):** Demonstrate the working software
against the stated acceptance criteria. Use concrete examples rather than
feature tours. "Here is a customer placing an order with an expired credit card"
is better than "here is the payment error handling."

In both modes: record what was accepted, what was rejected, and what generated
new questions. These outputs feed directly back into the backlog.

## Key moves

1. **Let the software speak, not the presenter.** The walkthrough is not a
   sales pitch. Resist the urge to narrate intent ("this will eventually...").
   Show what the system does now, against the criteria that were agreed.

2. **Invite rejection explicitly.** Ask: "Is there anything here that is not
   what you expected?" Most stakeholders will not volunteer disagreement unless
   asked. The walkthrough's value is in surfacing disagreement early, not in
   confirming agreement.

3. **Do not demo the happy path only.** Walk through error states, edge cases,
   and the scenarios most likely to have been misunderstood. The happy path
   rarely surfaces interpretive gaps.

4. **Record outcomes in the backlog, not in meeting notes.** Accepted criteria
   are closed. Rejected criteria become new backlog items with the stakeholder's
   correction as the acceptance criteria. Questions become spikes or refinement
   items. Nothing lives only in a document.

5. **Time-box ruthlessly.** A walkthrough that runs long is usually covering
   too much scope. Limit each session to work completable in one delivery
   cycle. Depth over breadth.

## Example

**Scrum Sprint Review:** The sprint review is the canonical acceptance walkthrough
in Agile delivery. Schwaber and Sutherland's Scrum Guide frames it explicitly
as an inspection of the increment - not a status report, but a working session
in which the team and stakeholders determine what to do next based on what has
been built and what has changed in the environment.

Teams that run sprint reviews as demo presentations and skip the conversation
miss the point. The review's value is in the dialogue - the stakeholder who
sees the feature and says "actually, I need it to do X differently" is giving
information that could not have been obtained earlier. That is the moment the
process is designed to create.

## AI leverage points

- **Scenario summary generation:** before the walkthrough, an agent can produce
  a human-readable summary of all acceptance scenarios being reviewed - useful
  for stakeholders who did not write the Gherkin
- **Outcome capture:** during or after the walkthrough, an agent can transcribe
  accepted/rejected/questioned items and format them as backlog-ready items
- **Gap analysis:** given the accepted scenarios and the current backlog, an
  agent can identify which user journeys have no corresponding acceptance
  criteria - surfaces missing coverage before the next cycle

## Connects to

- **Upstream:** `sdlc-bdd` (BDD scenarios are the structured input to the walkthrough),
  `sdlc-incremental-backlog` (the stories being reviewed were pulled from the backlog)
- **Downstream:** `sdlc-ship` (accepted work is authorized for release),
  `sdlc-incremental-backlog` (rejected and questioned items return to the backlog)
- **Lateral:** `sdlc-ci-pipeline` (the pipeline confirms technical correctness;
  the walkthrough confirms stakeholder intent - both gates, different questions)
