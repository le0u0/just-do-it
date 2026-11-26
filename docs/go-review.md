# go-review

Use `go-review plan` for a fresh Deep review of the draft, spec and checklist. See `agent-view/plan-review.md` and `dev-view/plan-review.html`. Findings are advisory pending your disposition.

Use `go-review code` with a PR URL, branch, SHA or diff. It writes `agent-view/review.md` (linking `agent-view/ut.md` and `agent-view/e2e.md`), and render `dev-view/review.html`. Runs in the main thread, called by `go-flow` or directly, and starts its own review agents.

Subagents are required; an unavailable agent blocks the review.

Direct runs stop after reporting. The automatic fix loop belongs to `go-flow` when included in the requested flow.

## DO IT

```mermaid
flowchart LR
    IN([confirm goal and ticket spec]) --> G[review Fetch<br/>standard: target, diff, paths]
    G -->|new snapshot or inputs| H[2-3 hunters<br/>standard, by lens]
    G -->|matching coverage| R
    H --> V[verifier<br/>deep: verify candidates]
    V --> R([write agent-view/review.md<br/>& dev-view/review.html])
```

| Feature | Detail |
| --- | --- |
| Goal & review plan | Uses the explicit goal and target when supplied, or the matching plan/spec. Asks only when the review scope remains unclear |
| Tests and acceptance | Flags stale test evidence and maps each ticket outcome to its current evidence or gap |
| Findings | Show how to verify, expected result, actual result, and fix. File labels reveal their paths on hover |
| Output | Writes `agent-view/review.md` (for agents) and interactive `dev-view/review.html` (for you) |

| Tier | When | Agents |
| --- | --- | --- |
| Standard | everything else | Correctness + Contract hunters (`standard`), 1 verifier (`deep`) |
| Deep | auth, billing, schema, secrets, CI, release, installers, `REVIEW.md` paths, or >1000 lines | + Security hunter |

PR and single-commit reviews pin all reads and evidence to the selected refs. A local branch review uses a verified baseline and applicable worktree changes. An SSH repository URL needs a review target.

The initial and delivery reviews cover the full diff from the original baseline. A direct re-review starts at the prior reviewed commit if it represented a clean checkout and still anchors the same review scope. Otherwise use the original baseline. Reuse a matching snapshot if its recorded coverage meets the request. Ticket review requires a ready spec or complete supplied requirements.

[Skill](../skills/go-review/SKILL.md) · [Report format](../skills/go-review/references/report-format.md) · [Storage](../skills/go-setup/references/storage.md)
