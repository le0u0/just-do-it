---
name: go-work
description: 'Implement production code from a request, spec, ticket or approved plan, following the project''s own rules and skills, with the work driven test-first through dev-tdd. Use for "implement step 2", "build this feature", "fix this failure" or "diagnose this bug". For unit specs alone use go-ut.'
---

# Work

## Contract

- Report as the caller specifies; default `Done` / `Open` / `Changed`. A test run reports `Result` and `Commands`.
- Write no plan docs (`plan.md`, `checklist.md`, `review.md`, diagnosis). Return all in the reply; the caller saves it.
- Input is text or a path the caller names. Search no storage.

## Modes

- **Direct request:** implement it, report changed files. No plan, checklist, or branch check.
- **Failure to fix:** diagnose per [diagnose.md](references/diagnose.md), then fix.
- **Approved plan:** text or path from `go-plan`. Follow [step-execution.md](references/step-execution.md), then [validation.md](references/validation.md). Done when the `Goal` is met.
- **Specs only or test run:** call `go-ut`. Change no spec here.

## Rules

- Stay on the current branch. Never create or push branches.
- Commit only per the plan's per-step delivery, or when the user approves the work and the exact one-line message.
- A follow-up after the `Goal` holds still ends in a commit, but never a new one for a small change to committed work:
  1. List unpushed commits (`git log @{u}..HEAD`, or `origin/HEAD..HEAD` with no upstream).
  2. Related to the unpushed `HEAD` commit (same file or purpose): `git commit --amend --no-edit`.
  3. Otherwise one new commit.
  4. Never amend a pushed commit.
- Delete only files the plan's `Deletions` lists; ask for any other.
- Run specs only when the request or plan authorizes it; a later no-tests instruction wins. Otherwise write specs and hand back unrun.
- Leave protected test files and unrelated specs unchanged.
- No self-review: report `Open: ready for review`; `go-review` reviews.
- e2e coverage goes to `go-e2e`, only when the user or plan asks.

## Workflow

1. Read the [project references](references/project-references.md); follow their conventions for mocking, setup, and file placement.
2. Ask once when the request omits a choice a project skill asks for, such as a variant or target folder.
3. Call `dev-tdd` once per step (a direct request is one step). It confirms the seam, drives red-green with `go-ut` and `go-e2e`, and leaves the step's specs passing.
4. Run typecheck and single spec files regularly. Run the full suite once at the end, only when authorized. Skip the loop for untestable changes, such as pure styling, and say so.
5. Self-check by reading: each behavior maps to a changed file and a spec; the diff has nothing unrelated. Format only changed files.
