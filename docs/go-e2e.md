# go-e2e

Authors, explores, runs and debugs Playwright e2e tests. The manager runs it in a subagent; you can call it directly.

## DO IT

- Authors specs and test data, finds locators by exploring the live UI, runs specs, and debugs failures, using `playwright-cli`.
- Writes only specs and test data in the repo.
- Writing a spec never runs it. It runs only when authorized, and never resets environments or test data unless asked.
- Production changes, such as a missing test selector, go to `go-work`. Formal review goes to `go-review`.

## USE IT

| Situation | Use |
| --- | --- |
| Add, find a locator, run or fix an e2e test | `go-e2e` |
| Add a missing selector in production code | `go-work` |

The manager calls it once, after the last step, for the specs the plan's `E2E` line names.

## WORK IT

- It finds the e2e setup first, and writes nothing when there is none.
- Specs come from explored locators, not from reading source alone.
- A run names exact spec files, never a folder or the full suite, and reports the real exit code.
- A failure comes with a log path and the symptom, not a guessed cause.

## FIT IT

```text
go-work -> go-e2e -> go-review
```

- Before it: `go-work` reports `Open: run e2e`.
- `dev-tdd` calls it when e2e specs are asked for.
- After it: `go-review`; a failure goes back to `go-work`.
