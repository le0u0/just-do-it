# go-flow

Stateless pipeline skill that chains the independent `go-*` skills over `~/.just-do-it/{project}/{branch}/`. Run the full ticket workflow or request any slice of steps (such as `research -> plan` or `plan -> work -> review`).

Skills can also run independently. If branch storage is missing, they trigger `go-setup` to confirm the project and create it. Branch-specific files live in `agent-view/` and `dev-view/`; `public/` is shared across the project. See [Storage](../skills/go-setup/references/storage.md) for the complete layout.

```mermaid
flowchart LR
    Start([Start]) -->|start workflow| S[go-setup]
    S -->|confirm project and research| R[to-spec]
    R -->|plan| P[go-plan]
    P -->|approve plan and build| A[go-work<br/>parallel independent steps<br/>dev-tdd]
    A -->|test| T[go-ut + go-e2e<br/>ut.md & e2e.md]
    T -->|fix failed tests| W[go-work<br/>fix and retry within limit]
    W -->|check test result| Q{Tests pass?}
    Q -->|continue when passing| V
    Q -->|stop when limit reached| Stop([Stop and ask user])
    T -->|review passing tests| V[go-review]
    V -->|fix TODO findings| F[go-fix]
    F -->|retest fixes| T
    V -->|finish when clean| End([End])
```

| Stage | Who runs it | Writes to storage |
| --- | --- | --- |
| 1. Setup | `go-setup` (main thread) | Confirms `{project}`; creates `agent-view/`, `dev-view/`, `public/` |
| 2. Research | `to-spec` (`fast`) | `agent-view/spec.md`, `agent-view/attachments/{ticket}/`, `dev-view/spec.html` |
| 3. Grill & plan | `go-plan` (`reasoning`) | `agent-view/plan.md`, `agent-view/checklist.md`, `agent-view/commit-format.md`, `agent-view/diagnose.md`, `dev-view/plan.html`, plus on-demand `public/glossary.md` & `public/adr/` |
| 4. Build | `go-work` (`standard`, one worker per step, parallel when independent; drives `dev-tdd`) | Code & specs, `agent-view/checklist.md`, `agent-view/CHANGELOG.md` |
| 5. Test | `go-ut` + `go-e2e` (`standard`) | Runs touched unit specs and planned E2E specs, writing `agent-view/ut.md` and `agent-view/e2e.md`. Failed tests are fixed and retried up to the project limit; if exhausted, stop and ask the user |
| 6. Review | `go-review` (main thread + review team) | Reads `agent-view/ut.md` & `agent-view/e2e.md`; writes `agent-view/review.md` and `dev-view/review.html` |
| 7. Fix loop | `go-fix` → `go-ut` / `go-e2e` → `go-review` | Applies fixes, re-runs `go-ut` and `go-e2e` when E2E-affecting files changed, and re-reviews until 0 `TODO` findings remain and all tests pass, or the review round cap is reached |

[Skill](../skills/go-flow/SKILL.md) · [Agent mapping](../skills/go-flow/references/agents.md#host-mapping) · [Scheduling](../skills/go-flow/references/reuse.md#parallel-steps) · [Storage](../skills/go-setup/references/storage.md)
