---
name: sdlc-ci-pipeline
description: >-
  Use during verify when an automated test suite exists and the team needs an objective, repeatable gate that determines whether a change is safe to progress. Activates when someone asks "what enforces our quality standard", "how do we prevent bad code from reaching production", or "what does our integration process look like". Draws on Continuous Delivery (Humble and Farley) and DevOps principles to establish the deployment pipeline as the authoritative verification mechanism.
stage: verify
posture: ci-pipeline-gate
tier: 2
role: skill
license: MIT
---
# Skill: CI Pipeline Gate

## What this enables

An objective, automated gate that confirms every change meets a defined quality
standard before it progresses toward production. The pipeline replaces manual
verification steps that are inconsistent, slow, and dependent on whoever is
available. When the pipeline is the authority, "done" has a definition that
does not shift based on schedule pressure or team mood.

## Fit signals

- An automated test suite exists and is maintained
- The team integrates changes frequently - at least daily
- Manual verification is a bottleneck or inconsistency source
- The team's definition of "done" needs to be enforceable, not advisory
- Multiple contributors are working on the same codebase simultaneously

## Anti-signals

- No automated test suite exists yet (build one via `sdlc-tdd` or `sdlc-bdd` first)
- The verification required is human judgment - stakeholder approval, formal inspection
  (use `sdlc-acceptance-walkthrough` or `sdlc-structured-inspection` instead)
- The codebase is pre-MVP with no stability expectation

## Core practice

The deployment pipeline is a **sequence of automated stages**, each of which
must pass before the next runs. A stage that fails stops the pipeline; the
change is not promoted until the pipeline is green.

**Canonical stage sequence (Humble & Farley):**

1. **Commit stage** (~5 minutes): compile, unit tests, static analysis. Fast
   enough that a developer waits for it. If this fails, no one else is affected.

2. **Acceptance stage** (~30-60 minutes): automated acceptance tests (BDD
   scenarios, integration tests, contract tests). Broader coverage; longer runtime.

3. **Capacity stage** (performance, load testing): run against a production-like
   environment. Not every pipeline runs this on every commit - it can be
   nightly or release-gated.

4. **Manual approval gate** (if required): a human reviews the pipeline summary
   and authorizes progression to production. This is a checkpoint, not a
   verification step - verification was the pipeline's job.

**The pipeline is the source of truth.** If it passes, the change is verified.
If it fails, the change is not verified - regardless of how confident the
developer feels.

## Key moves

1. **Keep the commit stage under 5 minutes.** A slow commit stage is one
   developers route around. If it takes 20 minutes, people stop running it
   locally and start batch-submitting work. Speed is a correctness property
   of the pipeline.

2. **Treat a failing pipeline as a production incident.** A broken build blocks
   every team member downstream. The rule: fix it or revert within 10 minutes.
   Do not leave a broken pipeline for "after lunch."

3. **Never commit directly to main without a passing pipeline.** Every change
   goes through the pipeline before merging. No exceptions for "small fixes" -
   those are the changes most likely to break integration.

4. **Run the full suite against every integration, not just new code.** Regression
   failures caused by interactions between changes are the class of defect the
   pipeline exists to catch. A pipeline that only tests the changed code is not
   a pipeline - it is a unit test runner.

5. **Make pipeline failures immediately visible.** Large monitors, Slack alerts,
   broken build indicators - the team should never have to check whether the
   pipeline is green. Green/red should be ambient information in the team's
   environment.

## Example

**Humble & Farley, Continuous Delivery (2010):** The deployment pipeline concept
formalizes the observation that every team already has a sequence of steps between
"code is written" and "code is in production." The question is whether that sequence
is automated, repeatable, and fast - or manual, inconsistent, and slow.

At Thoughtworks, the move from manual integration testing to a fully automated
pipeline consistently reduced integration failures and eliminated the "integration
hell" pattern - the compounding of defects that occurs when teams integrate
infrequently and discover problems weeks after they were introduced.

## AI leverage points

- **Pipeline configuration generation:** given a project structure and tech stack,
  an LLM can draft an initial CI configuration (GitHub Actions, GitLab CI, etc.)
  for team review - a strong starting point for teams without pipeline experience
- **Failure analysis:** when the pipeline fails, an agent can parse the failure
  log and identify the likely root cause, reducing the time between red and fix
- **Flaky test detection:** over time, an agent can track test pass/fail rates
  and flag tests that fail intermittently - the signal that separates real
  failures from noise

## Connects to

- **Upstream:** `sdlc-build` (the test suite produced in build is the pipeline's
  primary input), `sdlc-tdd`, `sdlc-bdd` (tests and scenarios become pipeline stages)
- **Downstream:** `sdlc-ship` (a passing pipeline is the authorization to ship)
- **Lateral:** `sdlc-acceptance-walkthrough` (human sign-off may follow a passing pipeline
  for stakeholder-facing features)
