---
name: go-work
description: 'Implement one step of work (a request, a plan step, or a failure to fix), following the project''s own rules and skills, with the work driven test-first through dev-tdd. Use for "implement step 2", "build this feature", "fix this failure" or "diagnose this bug". For unit specs alone use go-ut.'
---

# Work

Report as the caller specifies. Default to `Done` / `Open` / `Changed`. Pass test-run evidence to the caller per [Test report](../justaway/references/reports.md#test-report), including the excerpt for any unresolved failure.

## Modes

- **Direct request:** implement it, report changed files. No start gate.
- **Failure to fix:** diagnose per [diagnose.md](references/diagnose.md), then fix.
- **Plan step:** the caller passes the plan and names one step. Follow [step-execution.md](references/step-execution.md). In `justaway`, edit owned paths, run authorized scoped tests, and return evidence to the coordinator.
- **Specs only or test run:** call `go-ut`. Change no spec here.

## Rules

- Stay on the current branch.
- In a manager-assigned job, leave HEAD and the index untouched and report questions to the coordinator. For standalone work, commit only per the plan's per-step delivery, or when the user approves the work and the exact one-line message.
- A small follow-up to committed work amends instead of adding a commit:
  1. List unpushed commits (`git log @{u}..HEAD`, or `origin/HEAD..HEAD` with no upstream).
  2. Related to the unpushed `HEAD` commit (same file or purpose) and the plan does not use per-step commits: `git commit --amend --no-edit`. Per-step commits: never amend; one new commit with the plan's message.
  3. Otherwise one new commit.
  4. Never amend a pushed commit.
- Claim only what you read or ran. Say "seen in a listing" for the rest.
- Review is `go-review`'s job; the caller sends finished work there.

## Workflow

1. Read the [project references](references/project-references.md); follow their conventions for reusable components, mocking, setup, and file placement.
2. Inspect any supplied triage brief and attached images before implementing visual or UI behavior, and match their details.
3. Ask once when the request omits a choice a project skill asks for, such as a variant or target folder.
4. Own the whole behavior step, including its specs, implementation, and step-specific setup. Complete any approved setup needed to run the focused spec, then call `dev-tdd` once for the step. For a setup-only step, run its named verification when authorized and return the outcome.
5. Run typecheck regularly; spec runs happen inside `dev-tdd` and `go-ut`.
   - Passing specs and lint prove no typing. Typecheck every config the project defines, strictest included, plus editor diagnostics when a tool offers them; cover spec files too.
   - Errors in files you touched are yours to fix, or report in `Open` when pre-existing and out of scope.
6. Self-check by reading: each behavior maps to a changed file and a spec; the diff has nothing unrelated. Report any failed or blocked tool/check instead of claiming `Done`.
