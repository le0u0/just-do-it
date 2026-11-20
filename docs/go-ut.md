# go-ut

Writes, fixes or runs unit specs for changed code, and writes the test run report to `agent-view/ut.md`. Called by `dev-tdd` and `go-work`, or by you directly.

## DO IT

```mermaid
flowchart LR
    IN([change or specs<br/>to cover]) --> S[read or confirm<br/>public/jdi-config.md]
    S --> W[write one spec<br/>per behavior]
    W --> R[focused run,<br/>when authorized]
    R --> O([write agent-view/ut.md])
```

| Does | Detail |
| --- | --- |
| Setup | Reads `~/.just-do-it/{project}/public/jdi-config.md`. If missing, triggers `go-setup` configuration confirmation with the user |
| Writes in repo | Specs covering all observable behaviors of the touched component/unit beside the code (any comment max 1 line) |
| Runs | Only focused specs, and only when authorized |
| Writes to storage | `~/.just-do-it/{project}/{branch}/agent-view/ut.md` |

[Skill](../skills/go-ut/SKILL.md) · [Storage](../skills/go-setup/references/storage.md)
