# Evals

Behavioral cases for the skills: file changes and executed commands, not just frontmatter and links.

## Run

```mermaid
flowchart LR
    P[prepare<br/>fixtures] --> A[fresh agent<br/>per case] --> C[check files<br/>and commands] --> R[read traces<br/>vs checks] --> B[baseline<br/>without skill]
```

| Step | Do |
| --- | --- |
| 1. Prepare | Disposable fixtures outside any real checkout (git repos, synthetic test runner, nothing installed): `python3 evals/fixture.py prepare /private/tmp/just-do-it-evals-UNIQUE` |
| 2. Run | Per case in `cases.json`, give a fresh agent only the skill path (from `skills/`, not an installed cache), the generated `request.txt` and the `repo` directory. It saves its final answer as `response.md` beside `repo`. Withhold `checks`, `before.json` and the fixture script |
| 3. Check | `python3 evals/fixture.py check /private/tmp/just-do-it-evals-UNIQUE` |
| 4. Read | Traces and responses against each case's `checks`. Manager cases: confirm each handoff, and that only `go-triage`, `go-e2e` and `go-review`'s own review agents run as subagents |
| 5. Baseline | Repeat without the skill. A case passing both ways may be redundant: shorten it unless it guards safety, approval or scope |

Run a subset with `--case CASE_ID` (repeatable) on `prepare` and `check`.

## Limits

| Limit | Detail |
| --- | --- |
| Synthetic runner | Logs arguments and file hashes per call, so it catches config or spec edits that narrow a run |
| Not covered | Real tests, browsers, ticket tools |
| Failing focused command | Stays a reported failure |
