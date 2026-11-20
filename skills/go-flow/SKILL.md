---
name: go-flow
description: 'Run the end-to-end ticket workflow or a requested sequence of steps: go-setup -> go-research -> go-plan -> parallel go-work (with go-ut / go-e2e) -> go-review -> go-fix.'
---

# Flow

Stateless pipeline orchestrator that chains the independent `go-*` skills over the shared branch directory `~/.just-do-it/{project}/{branch}/`. Every skill reads and writes its own files under `agent-view/`, `dev-view/`, and `public/`.

## Pipeline

```mermaid
flowchart LR
    S[go-setup<br/>storage] --> R[go-research<br/>agent-view/research.md]
    R --> P[go-plan<br/>grill goal + plan.md]
    U([User]) <-->|decisions & approval| P
    P --> W1[go-work step 1<br/>dev-tdd: go-ut / go-e2e]
    P --> W2[go-work step N<br/>parallel independent step]
    W1 --> V[go-review<br/>dev-view/review.md]
    W2 --> V
    V -->|findings| F[go-fix<br/>dispositions & fixes]
```

By default, run the full flow in order. When the user requests a partial chain (for example, `research -> plan` or `plan -> work -> review`) or when earlier artifacts already exist in `agent-view/` and the user asks to continue, start at the requested stage.

## Stage routing

| Stage | Skill | Execution | Storage output |
| --- | --- | --- | --- |
| 1. Setup | `go-setup` | Main thread | Confirms `{project}`; ensures `~/.just-do-it/{project}/{branch}/{agent-view,dev-view}` and `public/` |
| 2. Research | `go-research` | Fast worker | `agent-view/research.md`, `agent-view/attachments/{ticket}/` |
| 3. Grill & plan | `go-plan` | Reasoning worker | `agent-view/plan.md`, `agent-view/checklist.md`, `agent-view/commit-format.md`, `agent-view/diagnose.md`, `public/glossary.md`, `public/adr/` |
| 4. Build & test | `go-work` | Standard worker per step (parallel when independent; calls `dev-tdd` -> `go-ut` / `go-e2e`) | Code & specs, `agent-view/checklist.md`, `agent-view/CHANGELOG.md`, `dev-view/ut.md`, `dev-view/e2e.md` |
| 5. Review | `go-review` | Main thread with review team | `dev-view/review.md` (references `dev-view/ut.md` & `dev-view/e2e.md`) |
| 6. Fix | `go-fix` | Main thread | Fixes, updates `dev-view/review.md`, `agent-view/checklist.md`, `agent-view/CHANGELOG.md` |

## Flow execution

1. **Setup (`go-setup`).** Resolve `~/.just-do-it/*/{branch}`. If missing, run `go-setup` to confirm `{project}` with the user and create `agent-view/`, `dev-view/`, and `public/`.
2. **Research (`go-research`).** For a ticket key or requirements link, dispatch one `fast` worker per [agents.md](references/agents.md) with the resolved `{task}` path (`~/.just-do-it/{project}/{branch}/`). It fetches live requirements, comments, related tickets, and attachments, saving `agent-view/research.md` and `agent-view/attachments/{ticket}/`. Report any fetch/MCP failure immediately—never fall back to local git guesses. Skip if the user supplied full requirements inline with no lookup needed.
3. **Grill and plan (`go-plan`).** Dispatch one `reasoning` worker with `{task}`. Relay its numbered frontier questions (including goal confirmation and any unknown domain terms for `public/glossary.md` or decisions for `public/adr/`) to the user and resume the worker with confirmed answers. Once `agent-view/plan.md` and `agent-view/checklist.md` are written, present a short summary of the `Goal`, numbered steps, unit/E2E test scope, and deletions, and ask for plan approval.
4. **Build (`go-work`).** After user approval, mark `agent-view/plan.md` `Status: approved`. If any step or the plan includes unit or E2E tests and `public/test-config.md` does not exist yet, run `go-setup`'s test-config confirmation first. Schedule ready steps per [reuse.md](references/reuse.md#parallel-steps):
   - Dispatch one `standard` `go-work` worker per ready step. Independent steps with disjoint writes and isolated tests run concurrently.
   - Each worker runs `dev-tdd` (calling `go-ut` / `go-e2e`, which write `dev-view/ut.md` / `dev-view/e2e.md`).
   - Verify each step's diff and test evidence per [reports.md](references/reports.md), serialize approved per-step commits, and ensure `agent-view/checklist.md` and `agent-view/CHANGELOG.md` are updated before unlocking dependent steps.
   - When the plan has a final E2E scenario not yet run inside a step, run `go-e2e` per [tests.md](references/tests.md) and [validation.md](references/validation.md) so `dev-view/e2e.md` is current.
5. **Review (`go-review`).** Run `go-review` on the branch diff against the plan's baseline and `agent-view/plan.md`. `go-review` writes `dev-view/review.md` with references to `dev-view/ut.md` and `dev-view/e2e.md`.
6. **Fix (`go-fix`).** When `dev-view/review.md` has in-scope `TODO` findings under the approved plan (or selected by the user), run `go-fix` to apply fixes, update `dev-view/review.md` and `agent-view/CHANGELOG.md`, refresh affected tests in `dev-view/ut.md` / `dev-view/e2e.md`, and re-review delta changes through `go-review`.
7. **Finish.** Report the final status, saved file paths in `agent-view/` and `dev-view/`, and any open items. The user can run `to-pr`, `to-test-doc`, or `to-handoff` anytime.

## Authorization

- Follow the latest user instruction. Test runs, resets, commits, pushes, external writes, and scope expansion require authorization from the user or approved plan.
- Plan approval covers its listed steps, deletions, scoped test runs, per-step commit messages, and `go-fix` for in-scope findings.
