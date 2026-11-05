# go-ut

Writes, fixes or runs unit specs for changed code. Called by `dev-tdd` and `go-work`, or by you directly.

## DO IT

- Input: the change or specs to cover, as text or a path you name.
- Writes one spec per behavior beside the code, with a coverage comment, following the project's test setup and mocking rules.
- Runs only focused specs, and only when authorized. Reports `Status` / `Result` / `Commands` / `Changed` / `Open`.
- Never changes production code (it reports defects for `go-work`), never runs the full suite unless asked, never touches e2e specs.

## USE IT

| Situation | Use |
| --- | --- |
| Add or fix unit specs, run a spec | `go-ut` |
| Build a feature test-first | `go-work` (calls `dev-tdd`) |
| e2e specs | `go-e2e` |

The manager calls it for unit runs before review.

## WORK IT

- It reads the project's test setup first, and says `no unit test setup` when there is none.
- Each spec covers one behavior and carries a `Covered` comment.
- A run uses one exact command, on the named spec only, with a real exit code.
- A production bug is reported, not fixed.

## FIT IT

```text
go-work -> dev-tdd -> go-ut (red) -> production change -> go-ut (green)
```

- `dev-tdd` calls it for the red and green runs.
- A failing run goes back to `go-work`; e2e goes to `go-e2e`.
