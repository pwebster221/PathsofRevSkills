---
name: sdlc-cleanroom
description: >-
  Use during build when criticality is high, the cost of a production defect is unacceptable, and the team has a well-defined specification to work from. Activates when someone says "this cannot fail in production", "we need to prove this is correct, not just test it", or when working on safety-critical, regulatory, or high-reliability systems. Implements the Cleanroom philosophy: verify correctness before compiling, eliminate debugging as a practice, and certify quality through statistical usage testing.
stage: build
posture: cleanroom
tier: 2
role: skill
license: MIT
---
# Skill: Cleanroom

## What this enables

Software correct by construction. The Cleanroom approach eliminates the debug cycle by preventing the defects that require it. Code is not written and then tested - it is reasoned about until it is provably correct, and then written. Defect rates measurable in fractions of a percent. Quality certified through statistical usage testing rather than assumed through manual QA.

The name comes from semiconductor manufacturing: a cleanroom does not detect contamination after the fact - it prevents contamination from entering in the first place.

## Fit signals

- Production defects carry unacceptable costs (safety-critical, financial, regulatory, or high-availability systems)
- The specification is complete and formally defined before implementation begins
- The team has the discipline and mathematical background to reason about correctness at each step
- Quality certification is required - stakeholders need a quantifiable reliability statement, not just "it passed QA"
- The code will not be significantly refactored - the verify-before-compile approach assumes the specification is stable

## Anti-signals

- Requirements are expected to change frequently during implementation (use `sdlc-tdd` or `sdlc-incremental-backlog` instead)
- The team needs to explore the design as they build (Cleanroom requires a complete spec before the first line is written)
- Speed of exploration is the primary constraint (use `sdlc-genai-assisted` for fast iteration)
- The team does not have access to formal correctness verification training

## Core practice

Cleanroom operates on a single foundational principle: **prove it correct before you run it.** This is not metaphorical. Before code is submitted for compilation, it is verified by correctness review - a structured walkthrough in which the team reasons through the code's logic against the specification using mathematical argument, not intuition.

**Three phases:**

**1. Specification**The system is fully specified using formal or semi-formal notation before implementation begins. Z schemas, state machines, or precisely written functional specifications define the intended behaviour. The specification is the contract; the code is the proof.

**2. Implementation and Correctness Verification**Code is written in small increments. After each increment, the team conducts a **correctness verification review** - not a code review for style or structure, but a line-by-line proof that the code satisfies the specification. If the verification cannot be completed, the code is rewritten until it can. The increment is not compiled until verification passes.

**3. Statistical Usage Testing (Certification**)Once the verified code is integrated, it is tested using a **statistical usage model** - a probability distribution over the ways real users will use the system, derived from operational profiles. Test cases are sampled from this distribution. Reliability is then estimated using statistical inference rather than pass/fail counting.

This is not regression testing. It is **certification**: a quantifiable statement of the form "this system will fail, on average, once per N operational hours under the specified usage profile."

## Key moves

1. **Never compile code you have not verified.** This is the discipline that defines the practice. If you have to run the code to find out whether it is correct, you have not finished verification. The compiler is a confirmation, not a discovery tool.

2. **Conduct correctness verification as a team activity.** The verification review is not a solo checklist. It is a structured walkthrough in which team members challenge each other's reasoning. One reviewer cannot catch all the logical gaps in their own argument.

3. **Write the operational profile before writing any code.** The operational profile defines what "usage" means for this system: which functions are called, how often, in what sequences, with what inputs. It is the foundation of the statistical test model. Without it, the certification is meaningless.

4. **Track defects from verification, not from testing.** In Cleanroom, defects discovered in testing represent failures of the verification process. They are analysed to understand why the correctness argument was wrong - not just fixed and moved on from.

5. **Measure Mean Time to Failure, not defect counts.** Cleanroom quality is expressed as reliability (MTTF under the operational profile), not as a defect list. This is a fundamentally different quality model than conventional testing and requires a different mindset from the entire team.

## Example

**IBM Cleanroom, Federal Systems Division (Mills, Dyer, Linger):** The original Cleanroom projects at IBM produced software with defect densities orders of magnitude lower than industry averages. One project - a 1.6 million line security kernel - achieved zero defects in system testing. The approach was later applied commercially and in NASA systems where the cost of a production defect was mission-critical.

The key insight from these projects: most defects are not caught by testing; they are prevented by the discipline of not moving forward until the current increment is understood. Testing finds the defects that slip through. Cleanroom removes the category of "slip through."

## AI leverage points

- **Specification review:** an LLM can review a formal specification for internal consistency, missing cases, and ambiguities before implementation begins - acting as a first-pass specification checker
- **Correctness argument drafting:** during verification review, an agent can draft the initial correctness argument for a code increment, which the team then challenges and refines - faster than writing from scratch
- **Operational profile generation:** given a system description and usage context, an LLM can draft an initial operational profile for team review - seeding the statistical test model
- **Defect analysis:** when a defect is found in statistical testing, an agent can help trace it back to the verification step that should have caught it, accelerating process improvement

## Connects to

- **Upstream:** `sdlc-formal-specification` (Cleanroom requires a formal or semi-formal specification; formal-spec is the natural upstream skill)
- **Downstream:** `sdlc-verify` (Cleanroom's statistical usage testing is a specialized verify posture in its own right)
- **Lateral:** `sdlc-tdd` (TDD and Cleanroom occupy opposite ends of the design clarity spectrum - TDD discovers design through tests; Cleanroom proves a known design; know which situation you are in before choosing)
