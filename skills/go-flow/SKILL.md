---
name: go-flow
description: 'Run the end-to-end ticket workflow or a requested sequence of steps: go-setup -> to-spec -> go-plan -> parallel go-work -> go-ut & go-e2e -> go-review <-> go-fix loop until all tests pass and review is clean.'
---

# Flow

Stateless pipeline orchestrator that chains the independent `go-*` skills over the shared branch directory `~/.just-do-it/{project}/{branch}/`. Every skill reads and writes its own files under `agent-view/` (compact `.md` for agents), `dev-view/` (human-readable `.html` by default), and `public/`.

## Pipeline

```mermaid
flowchart LR
    S[go-setup<br/>storage] --> R[to-spec<br/>spec.md + spec.html]
    R --> P[go-plan<br/>grill goal + plan.md & plan.html]
    U([User]) <-->|decisions & approval| P
    P --> W1[go-work step 1<br/>dev-tdd]
    P --> W2[go-work step N<br/>parallel independent]
    W1 --> T[go-ut + go-e2e<br/>ut.md & e2e.md]
    W2 --> T
    T -->|test fails| X[go-work<br/>fix and retry within limit]
    X -->|check test result| Q{Tests pass?}
    Q -->|yes| V
    Q -->|limit exhausted| Stop([Stop and ask user])
    T -->|all pass| V[go-review<br/>review.md + review.html]
    V -->|TODO findings| F[go-fix<br/>apply fixes]
    F -->|re-test & re-review| T
    V -->|0 TODO & tests pass| D([Done])
```

By default, run the full flow in order. When the user requests a partial chain (for example, `research -> plan` or `plan -> work -> review`) or when earlier artifacts already exist in `agent-view/` and the user asks to continue, start at the requested stage.

## Stage routing

| Stage | Skill | Execution | Storage output |
| --- | --- | --- | --- |
| 1. Setup | `go-setup` | Main thread | Confirms `{project}`; ensures `~/.just-do-it/{project}/{branch}/{agent-view,dev-view}` and `public/` |
| 2. Research | `to-spec` | Fast worker | `agent-view/spec.md`, `agent-view/attachments/{ticket}/`, `dev-view/spec.html` |
| 3. Grill & plan | `go-plan` | Reasoning worker | `agent-view/plan.md`, `agent-view/checklist.md`, `agent-view/commit-format.md`, `agent-view/diagnose.md`, `dev-view/plan.html`, `public/glossary.md`, `public/adr/` |
| 4. Build | `go-work` | Standard worker per step (parallel when independent; calls `dev-tdd`) | Code & specs, `agent-view/checklist.md`, `agent-view/CHANGELOG.md` |
| 5. Test | `go-ut` + `go-e2e` | Standard worker(s) | `agent-view/ut.md`, `agent-view/e2e.md`, `public/jdi-config.md` |
| 6. Review | `go-review` | Main thread with review team | `agent-view/review.md` (references `agent-view/ut.md` & `agent-view/e2e.md`), `dev-view/review.html` |
| 7. Fix loop | `go-fix` → `go-ut`/`go-e2e` → `go-review` | Main thread + test/review workers | Fixes, updates `agent-view/review.md`, `dev-view/review.html`, `agent-view/ut.md`, `agent-view/e2e.md`, `agent-view/checklist.md`, `agent-view/CHANGELOG.md` |

## Flow execution

1. **Setup (`go-setup`).** Resolve `~/.just-do-it/*/{branch}`. If missing, run `go-setup` to confirm `{project}` with the user and create `agent-view/`, `dev-view/`, and `public/`.
2. **Spec (`to-spec`).** For a ticket key or requirements link, dispatch one `fast` worker per [agents.md](references/agents.md) with the resolved `{task}` path (`~/.just-do-it/{project}/{branch}/`). Wait for its result. Proceed only with a ready spec or complete requirements supplied inline. Follow [Blocked spec](../to-spec/SKILL.md#blocked-spec) for a failed lookup, partial spec, or missing worker result. Apply the same gate when resuming a later ticket stage whose spec is blocked.
3. **Grill and plan (`go-plan`).** Dispatch one `reasoning` worker with `{task}`. Relay its numbered frontier questions (including goal confirmation, reusable component choices, stateful transition checks, and any unknown domain terms for `public/glossary.md` or decisions for `public/adr/`) to the user and resume the worker with confirmed answers. Once `agent-view/plan.md`, `agent-view/checklist.md`, and `dev-view/plan.html` are written, share the `dev-view/plan.html` path and a short summary so the user can view `dev-view/plan.html` and approve the plan.
4. **Build (`go-work`).** After user approval, mark `agent-view/plan.md` and `dev-view/plan.html` `Status: approved`. If any step or the plan includes unit or E2E tests and `public/jdi-config.md` does not exist yet, run `go-setup`'s configuration confirmation first. Schedule ready steps per [reuse.md](references/reuse.md#parallel-steps):
   - Dispatch one `standard` `go-work` worker per ready step. Independent steps with disjoint writes and isolated tests run concurrently.
   - Each worker runs `dev-tdd` (writing complete unit specs for the touched component/unit via `go-ut`).
   - Verify each step's diff and test evidence per [reports.md](references/reports.md), serialize approved per-step commits, and ensure `agent-view/checklist.md` and `agent-view/CHANGELOG.md` are updated before unlocking dependent steps.
5. **Test (`go-ut` + `go-e2e`).** Before entering review, verify all changed unit specs through `go-ut` in evidence-only mode and publish `agent-view/ut.md` from those results and run planned E2E scenarios through `go-e2e` (writing `agent-view/e2e.md`) per [tests.md](references/tests.md) and [validation.md](references/validation.md). Route failed tests to `go-work` and apply the project's [test retry limit](../go-setup/references/public-docs.md#jdi-configmd), including failures after review fixes. Do not start or resume review while required tests fail.
6. **Review (`go-review`).** Run `go-review` on the branch diff against the plan's baseline and `agent-view/plan.md`, using the current `agent-view/ut.md` and `agent-view/e2e.md`. `go-review` writes `agent-view/review.md` and `dev-view/review.html` (showing the UT/E2E pass/fail status badge).
7. **Fix, re-test, and re-review loop (`go-fix` → `go-ut` / `go-e2e` → `go-review`).** When `agent-view/review.md` has in-scope `TODO` findings under the approved plan (or selected by the user):
   - Run `go-fix` to apply fixes and update `agent-view/review.md`, `dev-view/review.html`, `agent-view/checklist.md`, and `agent-view/CHANGELOG.md`.
   - Re-run the affected tests. Collect unit evidence through `go-ut` in evidence-only mode and have the coordinator update `agent-view/ut.md`. When E2E-affecting files changed, run `go-e2e` to update `agent-view/e2e.md`. Match the reports to the tested snapshot.
   - Re-run `go-review` on the delta after tests pass. Repeat this `go-fix` → `go-ut`/`go-e2e` → `go-review` loop until all tests pass and 0 open `TODO` findings remain, the review round cap is reached, or a test retry fails.
8. **Finish.** Report the final status, saved file paths in `dev-view/` and `agent-view/`, and any open items. The user can run `to-pr`, `to-test-doc`, or `to-handoff` anytime.

## Authorization

- Follow the latest user instruction. Test runs, resets, commits, pushes, external writes, and scope expansion require authorization from the user or approved plan.
- Plan approval covers its listed steps, deletions, scoped test runs, per-step commit messages, and the `go-fix` → re-test → re-review loop for in-scope findings.
