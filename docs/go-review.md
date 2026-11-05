# go-review

Review a branch, diff or work-in-progress change and return the review report. The manager runs it as a subagent; you can also call it directly. It is the only skill that reviews.

## DO IT

- Takes requirements (text, path, ticket URL or plan), an optional previous review, and an optional baseline.
- Reads the scoped diff, every hunk, then changed functions and their callers.
- Keeps only findings the change introduced or exposed, judged against the project's standards.
- Returns the whole report in the reply: issue count, a `Manual review` list, `TODO`, `RESOLVED`, `IGNORED` and a reference line.
- On a re-review, returns the previous report updated in full.
- Runs no tests, edits no source, and writes no files. `Tests` stays "not run" for the manager to fill.

## USE IT

| Situation | Use |
| --- | --- |
| "Review my branch", "review this diff" | `go-review` |
| Findings are chosen for fixing | `go-fix` |
| The manager has finished a step or the e2e run passed | It sends the baseline and scope to `go-review` |

## WORK IT

- The baseline is stated, and the diff is not empty.
- Every hunk is read before it says "no actionable findings".
- Findings cite the changed lines and say what breaks.
- A re-review moves fixed items to `RESOLVED` and numbers new findings after the last.

## FIT IT

```text
go-review -> go-fix -> go-review
```

- `go-fix` fixes the findings you select. A review approves no fixes by itself.
- `go-work` finishes with `Open: ready for review`, which leads to this skill.
- `start-manager` saves the report as `review.md` and writes the test results into `Tests`.
