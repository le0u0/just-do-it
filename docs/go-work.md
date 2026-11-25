# go-work

Implements one step of work, test-first: a request, one step of `agent-view/plan.md`, or a failure to fix. `go-flow` assigns one standard worker per step and runs independent steps concurrently. You can also call `go-work` directly.

## DO IT

```mermaid
flowchart LR
    IN([request, failure,<br/>or plan step]) --> M{mode}
    M --> D[dev-tdd<br/>-> go-ut / go-e2e]
    M --> S[verify shared setup]
    D --> O([updates checklist.md<br/>& CHANGELOG.md])
    S --> O
```

| Mode | Does |
| --- | --- |
| Direct request | Implements the request, updates `agent-view/CHANGELOG.md` on commit |
| Failure to fix | Diagnoses first (`agent-view/diagnose.md`), then fixes |
| Plan step | Owns the test, fix, and local setup for one behavior, updates `agent-view/checklist.md` and `agent-view/CHANGELOG.md` |
| Specs only | Calls `go-ut` |

| Does | Detail |
| --- | --- |
| Reads | `agent-view/plan.md`, `agent-view/checklist.md`, `agent-view/spec.md`, `agent-view/attachments/`, `public/glossary.md`, `public/adr/` |
| Calls | `dev-tdd` once per behavior step (`go-ut` writes `agent-view/ut.md`; `go-e2e` writes `agent-view/e2e.md`) |
| Writes | Source and specs in the repo; updates `agent-view/checklist.md`, `agent-view/CHANGELOG.md`, `agent-view/diagnose.md`, and on-demand `public/glossary.md` / `public/adr/` |

[Skill](../skills/go-work/SKILL.md) · [Storage](../skills/go-setup/references/storage.md)
