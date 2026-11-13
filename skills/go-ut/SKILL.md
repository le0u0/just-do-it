---
name: go-ut
description: 'Write, fix or run unit specs for changed code, following the project''s own test setup and conventions. Use for "add unit tests", "fix this spec", "run the unit tests for X" or "write specs for this change".'
---

# Unit Tests

Report as the caller specifies; default `Done` / `Open` / `Changed`. A run reports:

```text
Status: done | failed | blocked
Result: <counts>; failed: <spec file and test name each, or none>
Commands: <command → real exit code>
Changed: <files, or none>
Open: <or none>
```

## Modes

- **Write or fix specs:** no production change. Report production defects; `go-work` fixes them.
- **Test run:** run the named specs per [running.md](references/running.md) and report. Change no files.

## Rules

- Run specs only when the request or plan authorizes it; the newest instruction wins, so a request to run named specs authorizes exactly those runs, even when an earlier plan says not to run tests. Otherwise write specs and hand back unrun.
- Focused specs only; the full suite only when the user asks.
- Leave the protected files in `running.md` and unrelated specs unchanged.
- e2e specs go to `go-e2e`.

## Workflow

1. Read the [project references](references/project-references.md) for the feature type; follow their conventions for mocking, setup, and file placement.
2. Find the setup per [test-setup.md](references/test-setup.md). None: write and run no specs, say `no unit test setup`.
3. Read [test-quality.md](references/test-quality.md) and [examples.md](references/examples.md), plus [mocking.md](references/mocking.md) when a spec needs a mock.
4. Write one spec for one behavior in the spec file the project places beside the code, with the coverage comment from `test-quality.md`.
5. Run the focused spec per `running.md`; report the result.
6. Self-check by reading: setup reaches the intended state; assertions would fail on the regression; no mock of the code's own modules; no expected value recomputed from the code's formula. Rewrite a spec that fails this check, and rerun it when running is authorized, before reporting. Format only changed files.
