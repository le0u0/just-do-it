# go-fix

Fix the review findings you select and return a numbered disposition for each. The manager runs it in the main thread; you can also call it directly.

## DO IT

- Takes a review (text or path) and your choice per finding: accepted, deferred, disputed or ignored.
- Rechecks each selected finding against the current code, and asks when the code has drifted.
- Fixes production code through `go-work` and unit specs through `go-ut`.
- Hands e2e findings back as `Open` for `go-e2e`.
- Returns, per finding, a disposition, a `Done` line of at most 20 words and a `Status`, plus the open count by severity.
- Writes no `review.md` or checklist, and leaves changes uncommitted unless you approve an exact commit message.
- "Set status to approved" changes nothing and replies `Status: approved`.

## USE IT

| Situation | Use |
| --- | --- |
| "Fix review findings 1 and 3" | `go-fix` |
| You want the fixes checked again | `go-review` |
| No review exists yet | `go-review` first |
| The manager has selected findings | It runs `go-fix` itself, before anything else, and records the dispositions |

## WORK IT

- Finding IDs are kept exactly as in the review.
- Every selected finding has an evidenced outcome.
- Findings you didn't select are untouched.
- Deferred and disputed findings stay open.
- It reports validation limits, such as tests it was not allowed to run.

## FIT IT

```text
go-review -> go-fix -> go-review
```

- It fixes only what `go-review` found and you chose.
- It calls `go-work` and `go-ut` for the code and specs, and `go-e2e` for e2e findings.
- `start-manager` records the dispositions in `review.md` and `checklist.md`.
