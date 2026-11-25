---
name: go-work
description: 'Implement one step of work (a request, a plan step, or a failure to fix), following the project''s own rules and skills, with the work driven test-first through dev-tdd. Updates agent-view/checklist.md and agent-view/CHANGELOG.md.'
---

# Work

Resolve `~/.just-do-it/{project}/{branch}/` per [storage.md](../go-setup/references/storage.md). If the branch folder does not exist under `~/.just-do-it/*/{branch}`, run `go-setup` first to confirm `{project}` with the user. Report as the caller specifies, defaulting to `Done` / `Open` / `Changed`, and pass test-run evidence per [Test report](../go-flow/references/reports.md#test-report-agent-viewutmd-and-agent-viewe2emd).

## Modes

- **Direct request:** implement it, update `agent-view/CHANGELOG.md` on commit, report changed files. No start gate.
- **Failure to fix:** diagnose per [diagnose.md](references/diagnose.md), save diagnosis to `agent-view/diagnose.md` per [diagnose-format.md](references/diagnose-format.md), then fix.
- **Plan step:** read `agent-view/plan.md` and `agent-view/checklist.md` (or use the plan step passed by `go-flow`). Follow [step-execution.md](references/step-execution.md). Edit owned paths, run authorized scoped tests through `dev-tdd` (`go-ut` / `go-e2e`), and update `agent-view/checklist.md` and `agent-view/CHANGELOG.md`.
- **Specs only or test run:** call `go-ut`. Change no spec here.

## Rules

- Apply the project's [test retry limit](../go-setup/references/public-docs.md#jdi-configmd), including delegated work. If test configuration lacks a valid limit, run `go-setup` to confirm it.
- Stay on the current branch.
- In a parallel `go-flow` wave, leave `HEAD` and the index untouched for the flow coordinator to serialize commits, and report questions to the caller. For standalone work or single-step execution, commit per the plan's per-step delivery or when the user approves the work and the exact one-line message, and update `agent-view/CHANGELOG.md` and `agent-view/checklist.md`.
- A small follow-up to committed work amends instead of adding a commit:
  1. List unpushed commits (`git log @{u}..HEAD`, or `origin/HEAD..HEAD` with no upstream).
  2. Related to the unpushed `HEAD` commit (same file or purpose) and the plan does not use per-step commits: `git commit --amend --no-edit`. Per-step commits: amend only when fixing a mistake in the unpushed `HEAD` step commit itself; otherwise create one new commit with the plan's message. Update the SHA in `agent-view/CHANGELOG.md`.
  3. Otherwise one new commit.
  4. Never amend a pushed commit.
- Unknown domain terms, product concepts, or hard-to-reverse trade-offs encountered during implementation: **never guess**—ask the user and update `~/.just-do-it/{project}/public/glossary.md` or `public/adr/` per [public-docs.md](../go-setup/references/public-docs.md).
- Comments: write self-explanatory code without comments by default. When a non-obvious constraint requires a comment, limit it to **1 line only (`// ...`)**—never add multi-line comments or JSDoc blocks unless project rules require them.
- Claim only what you read or ran. Say "seen in a listing" for the rest.
- Review is `go-review`'s job; finished work goes there.

## Workflow

1. Read the [project references](references/project-references.md) (including `public/glossary.md` and `public/adr/` when present); follow their conventions for reusable components, mocking, setup, and file placement.
2. Inspect `agent-view/spec.md` and `agent-view/attachments/` when present before implementing visual or UI behavior, and match their details.
3. Ask once when the request omits a choice a project skill or unknown domain term requires.
4. Own the whole behavior step, including its specs, implementation, and step-specific setup. Complete any approved setup needed to run the focused spec, then call `dev-tdd` once for the step (`dev-tdd` drives `go-ut` / `go-e2e`). Pass evidence-only mode through to `go-ut` when requested by the coordinator. For a setup-only step, run its named verification when authorized and return the outcome.
5. Run typecheck regularly; spec runs happen inside `dev-tdd` and `go-ut`.
   - Passing specs and lint prove no typing. Typecheck every config the project defines, strictest included, plus editor diagnostics when a tool offers them; cover spec files too.
   - Errors in files you touched are yours to fix, or report in `Open` when pre-existing and out of scope.
6. Self-check by reading: each behavior maps to a changed file and a spec; the diff has nothing unrelated. Update `agent-view/checklist.md` and (when committed) `agent-view/CHANGELOG.md`. Report any failed or blocked tool/check instead of claiming `Done`.
