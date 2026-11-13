---
name: go-work
description: 'Implement one step of work (a request, a plan step, or a failure to fix), following the project''s own rules and skills, with the work driven test-first through dev-tdd. Use for "implement step 2", "build this feature", "fix this failure" or "diagnose this bug". For unit specs alone use go-ut.'
---

# Work

Report as the caller specifies; default `Done` / `Open` / `Changed`. A test run reports `Result` and `Commands`.

## Modes

- **Direct request:** implement it, report changed files. No start gate.
- **Failure to fix:** diagnose per [diagnose.md](references/diagnose.md), then fix.
- **Plan step:** the caller passes the plan text and names one step. Do only that step, per [step-execution.md](references/step-execution.md). Never start the next step; the caller sequences steps.
- **Specs only or test run:** call `go-ut`. Change no spec here.

## Rules

- Stay on the current branch.
- Commit only per the plan's per-step delivery, or when the user approves the work and the exact one-line message.
- A small follow-up to committed work amends instead of adding a commit:
  1. List unpushed commits (`git log @{u}..HEAD`, or `origin/HEAD..HEAD` with no upstream).
  2. Related to the unpushed `HEAD` commit (same file or purpose): `git commit --amend --no-edit`.
  3. Otherwise one new commit.
  4. Never amend a pushed commit.
- Claim only what you read or ran. Say "seen in a listing" for the rest.
- Review is `go-review`'s job; the caller sends finished work there.

## Workflow

1. Read the [project references](references/project-references.md); follow their conventions for mocking, setup, and file placement.
2. Ask once when the request omits a choice a project skill asks for, such as a variant or target folder.
3. Call `dev-tdd` once per step (a direct request is one step). It leaves the step's specs passing.
4. Run typecheck regularly; spec runs happen inside `dev-tdd` and `go-ut`.
   - Passing specs and lint prove no typing. Typecheck every config the project defines, strictest included, plus editor diagnostics when a tool offers them; cover spec files too.
   - Errors in files you touched are yours to fix, or report in `Open` when pre-existing and out of scope.
5. Self-check by reading: each behavior maps to a changed file and a spec; the diff has nothing unrelated.
