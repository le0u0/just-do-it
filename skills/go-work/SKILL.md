---
name: go-work
description: 'Implement production code from a request, spec, ticket or approved plan, following the project''s own rules and skills, with the work driven test-first through dev-tdd. Use for "implement step 2", "build this feature", "fix this failure" or "diagnose this bug". For unit specs alone use go-ut.'
---

# Work

Report as the caller specifies; default `Done` / `Open` / `Changed`. A test run reports `Result` and `Commands`. Write no plan docs (`plan.md`, `checklist.md`, `review.md`, diagnosis files): return everything in the reply and the caller saves it. Input is text or a path the caller names; search no storage.

## Modes

- **Direct request:** implement what the user asked and report the changed files. No plan, checklist, or branch check.
- **Failure to fix:** the caller sends a failed spec or a bug report. Diagnose per [diagnose.md](references/diagnose.md), then fix.
- **Approved plan:** a plan from `go-plan`, passed as text or path. Follow [step-execution.md](references/step-execution.md); after the last step, [validation.md](references/validation.md). Done when the `Goal` is met.
- **Specs only or a test run:** call `go-ut`. This skill changes no spec itself.

## Rules

- Work on the current branch; never create or push branches. Commit only per the plan's per-step delivery, or when the user approves the work and the exact one-line message. Otherwise leave work uncommitted.
- A follow-up request outside the plan's steps, such as a tweak or fix after the `Goal` holds, still ends in a commit, but never a new commit for a small change to work already committed. Before committing, list the unpushed commits (`git log @{u}..HEAD`, or `origin/HEAD..HEAD` with no upstream). When the change is related to the unpushed `HEAD` commit, such as the same file or purpose, fold it in with `git commit --amend --no-edit`. Otherwise make one new commit for the related changes. Never amend or rewrite a pushed commit.
- Keep working until the plan's `Goal` holds, step by step. Delete only files the plan's `Deletions` lists; ask for any other deletion.
- Run specs only when the request or approved plan authorizes it; a later no-tests instruction wins. Without authorization, write the specs and hand back unrun.
- Leave protected test files and unrelated specs unchanged.
- No self-review: review is only `go-review`'s job. Report `Open: ready for review`; never review your own diff.
- End-to-end coverage goes to `go-e2e`, only when the user or plan asks.

## Workflow

1. Read the [project references](references/project-references.md) for the feature type, and follow their conventions for mocking, setup, and file placement.
2. When the request leaves out a choice a project skill asks for, such as a variant or target folder, ask once. Skip what the request already says.
3. Build with TDD, one behavior at a time, batched per step (a direct request is one step). Call `dev-tdd` at the seams, once per step: it confirms the seam, drives the red-green loop with `go-ut` and `go-e2e`, and leaves the step's specs passing.
4. Throughout: run typecheck and single spec files regularly. Run the full suite once, at the end of the work, and only when authorized. Skip the loop for changes with no testable behavior, such as pure styling, and say so.
5. Self-check by reading: each requested behavior maps to a changed file and a spec; the diff has nothing unrelated. Format only changed files. Do not review.
