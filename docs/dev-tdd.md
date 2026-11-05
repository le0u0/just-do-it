# dev-tdd

Drives one step or behavior test-first. Called by `go-work` at its seams, or by you directly.

## DO IT

- Per behavior: confirm the seam, write a failing spec, make the smallest production change, watch it pass.
- Calls `go-ut` for unit specs and `go-e2e` for e2e specs, only when the user or plan asks for e2e.
- Reports `Done` (at most 20 words) naming the spec that failed before and the run that passed after.
- Never edits a spec to match wrong code. Changes an existing assertion only when the expected behavior changed, and says why in `Open`.
- Never writes plan docs. Skips the loop for untestable changes, such as pure styling, and says so.

## USE IT

| Situation | Use |
| --- | --- |
| "Do this test-first", "red-green this fix" | `dev-tdd` |
| Build a whole plan | `go-work` (calls it) |
| One spec, no loop | `go-ut` |

The manager does not call it directly.

## WORK IT

- A seam is confirmed before the first spec.
- The red run happens once, before any production change.
- When red cannot be seen, `Open` says `red not observed`.
- Production code changes only enough to pass the spec.
- Each step ends with its specs passing.

## FIT IT

```text
go-work -> dev-tdd -> go-ut / go-e2e
```

- `go-work` calls it once per step.
- `go-ut` and `go-e2e` do the spec work and runs.
