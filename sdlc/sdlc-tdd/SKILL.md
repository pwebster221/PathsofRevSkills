---
name: sdlc-tdd
description: >-
  Use during build when the design is not yet clear and you want tests to drive the architecture into existence. Activates when someone says "I'm not sure how to structure this", "where do I start with this feature", or when refactoring risk is high and a safety net is needed. Also activates for any greenfield code where the interface is not yet defined. Implements Kent Beck's Red-Green- Refactor cycle as a design practice, not just a testing practice.
stage: build
posture: tdd
tier: 2
role: skill
license: MIT
---
# Skill: Test-Driven Development

## What this enables

Design that emerges from use rather than speculation. When you write the test first, you are forced to think about what the code should do before thinking about how it should do it. The result is code that is testable by construction, interfaces that are shaped by their callers, and a permanent safety net that makes every subsequent refactor safe.

TDD does not produce more tests. It produces better-designed code that happens to be thoroughly tested.

## Fit signals

- The design is not yet clear - you are unsure how to structure the solution
- Refactoring is expected - the code will need to change as understanding grows
- Working solo or in a pair on a focused unit of functionality
- The cost of discovering design mistakes late (in QA or production) is high
- You want the tests to serve as living documentation of intended behaviour

## Anti-signals

- The specification is completely defined upfront and must be proven correct before any code is written (use `sdlc-cleanroom` instead)
- The work is exploratory / prototype-quality and will be thrown away (use `sdlc-genai-assisted` for fast spikes instead)
- Stakeholders need to read and validate the test scenarios (use `sdlc-bdd` so scenarios are expressed in plain language)

## Core practice

Three rules, in strict order:

1. **Red** - Write a failing test that describes the next small behaviour you want. The test must fail for the right reason - not because of a syntax error, but because the behaviour does not yet exist.

2. **Green** - Write the minimum code necessary to make the test pass. This means the simplest thing that could possibly work - no more. Resist the urge to generalize. Ugly code that passes is correct at this step.

3. **Refactor** - Clean up the code. Remove duplication. Clarify names. Improve structure. The tests stay green throughout. Refactoring is not optional - it is the step where design quality actually improves.

Repeat. Each cycle should take minutes, not hours.

## Key moves

1. **Write one test at a time.** Do not write a list of tests and then implement them. One failing test, then make it pass, then clean up. The discipline of the small cycle is the whole practice.

2. **Test behaviour, not implementation.** The test should describe what the code does from the outside - what goes in, what comes out, what changes in state. Never test private methods or internal structure. If the test breaks when you refactor without changing behaviour, the test is wrong.

3. **Use the test to design the interface.** Before writing the test, ask: "If this code were perfect, how would I call it?" Write the call first. The test forces you to design the API before implementing it.

4. **Keep the cycle short.** If a single Red-Green-Refactor cycle takes more than 15 minutes, the step is too large. Break it down. The power of TDD comes from the rapid feedback loop - the smaller the cycle, the faster you learn whether your design is working.

5. **Treat the refactor step as mandatory, not optional.** Technical debt accumulates exactly when teams skip the third step. Green-and-clean is the only acceptable stopping point.

## Example

**Kent Beck, TDD by Example:** Beck demonstrates TDD with a multi-currency money system. Rather than designing the class hierarchy upfront, he writes a test: `assertEquals(Money.dollar(5), Money.dollar(5))`. The test fails because `equals()` is not defined. He implements the minimum. Then he writes the next test. The `Dollar`, `Franc`, and `Money` classes emerge from the pressure of the tests - not from a design document.

The lesson: the architecture that emerges from TDD is shaped by how the code will actually be used. Speculative design produces code shaped by how the designer imagined it might be used. These are different things.

## AI leverage points

- **Test generation:** given a function signature and a description, an LLM can draft an initial set of test cases - useful for seeding the Red step quickly, especially for edge cases the developer might not consider
- **Refactoring suggestions:** after Green, prompt the LLM with the passing code and ask "what duplication or naming issues do you see?" as a Refactor accelerator
- **Cycle coaching:** an agent can monitor cycle length and flag when a single TDD step is taking too long, prompting a step decomposition

## Connects to

- **Upstream:** `sdlc-design` (architecture decisions shape what gets tested first)
- **Downstream:** `sdlc-verify` (TDD tests form the base of the verification suite)
- **Lateral:** `sdlc-bdd` (BDD scenarios become the acceptance-level tests; TDD operates at the unit level below them), `sdlc-mob-programming` (TDD pairs naturally with mob - the Navigator writes the test, the Driver implements)
