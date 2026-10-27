---
name: develop
description: 'Implement production code and its unit specs from a request or an approved plan, following the project''s own rules and skills; also write, fix or run unit specs alone. Use for "implement step 2", "build this feature", "add unit tests", "fix this spec" or "run the unit tests for X".'
effort: medium
metadata:
  tier: standard
---

# Develop

Report per [reports.md](../manager/references/reports.md); a test run reports the test report there.

## Modes

- **Direct request:** implement what the user asked and report the changed files. No plan, branch folder, checklist, or branch check.
- **Specs only:** write or fix unit specs for changed code, with no production change. Report production defects found; fixing them is another mode.
- **Test run:** run the named unit specs per [running.md](references/running.md) and report. Change no files; skip the workflow.
- **Failure to fix:** the manager sends a failed spec or a bug report. Diagnose per [diagnose.md](references/diagnose.md), then fix.
- **Approved plan:** a `plan.md` from `plan`. Follow [step-execution.md](references/step-execution.md); after the last step, [validation.md](references/validation.md). Done when the `Goal` is met.

## Rules

- Work on the current branch; never create or push branches. Commit only per the plan's per-step delivery, or when the user approves the work and the exact one-line message. Otherwise leave work uncommitted.
- Keep working until the plan's `Goal` holds, step by step. Delete only files the plan's `Deletions` lists; ask for any other deletion.
- Run specs only when the request or approved plan authorizes it; a later no-tests instruction wins. Without authorization, write the specs and hand back unrun.
- Leave the protected files listed in [running.md](references/running.md) and unrelated specs unchanged.
- End-to-end coverage goes to `e2e-tester` (`write-e2e`), only when the user or plan asks.

## Workflow

1. Read the [project references](../manager/references/project-references.md) for the feature type: rules, project-local skills such as a `create-*` or testing skill, the test framework's config, and the nearest comparable feature and spec. Follow their conventions for mocking, setup, and file placement. Read [test-quality.md](references/test-quality.md) and [examples.md](references/examples.md), and [mocking.md](references/mocking.md) when a spec needs a mock.
2. When the request leaves out a choice a project skill asks for, such as a variant or target folder, ask once. Skip what the request already says.
3. Build with TDD, one behavior at a time, per the loop in [test-quality.md](references/test-quality.md), batched per step (a direct request or specs-only job is one step), and do every part yourself:
   0. Find the unit test setup per [test-setup.md](../manager/references/test-setup.md). With none, write and run no specs, say `no unit test setup`, and continue with 2 and 4.
   1. Confirm the seam per test-quality: the step's `Test` names it. With no plan, return the seam as `Open` and proceed once the user confirms it. Write one spec for one behavior in the spec file the project places beside the code, with the coverage comment from test-quality. When running is authorized, the red run is required even for a one-line fix: write the spec and run it before touching production code, and watch it fail for the right reason. A spec for behavior the code already has may pass at once.
   2. Write the smallest production change that matches nearby code, and only what that spec requires. Skip this in specs-only mode.
   3. Run the slice's focused spec per [running.md](references/running.md) (green), and fix the code on a failure.
   4. Repeat 1 to 3 for the next behavior of the step. When the step's specs pass, commit per [step-execution.md](references/step-execution.md) and start the next step.

   Skip the loop for changes with no unit-testable behavior, such as pure styling, and say so.
4. Self-check by reading: each requested behavior maps to a changed file and a spec; spec setup reaches the intended state; assertions would fail on the regression; no spec mocks the code's own modules; no expected value is recomputed from the code's formula; the diff has nothing unrelated. Format only changed files.
