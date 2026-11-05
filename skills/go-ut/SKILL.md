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

Write no plan docs; return everything in the reply. Input is text or a path the caller names.

## Modes

- **Write or fix specs:** for changed code, with no production change. Report production defects found; fixing them is `go-work`'s job.
- **Test run:** run the named specs per [running.md](references/running.md) and report. Change no files.

## Rules

- Run specs only when the request or approved plan authorizes it; a later no-tests instruction wins. Without authorization, write the specs and hand back unrun.
- Run focused specs only. The full suite runs only when the user asks.
- Leave the protected files listed in `running.md` and unrelated specs unchanged.
- End-to-end specs go to `go-e2e`.

## Workflow

1. Read the [project references](references/project-references.md) for the feature type: rules, project-local skills such as a testing skill, the test framework's config, and the nearest comparable spec. Follow their conventions for mocking, setup, and file placement.
2. Find the setup per [test-setup.md](references/test-setup.md). With none, write and run no specs and say `no unit test setup`.
3. Read [test-quality.md](references/test-quality.md) and [examples.md](references/examples.md), and [mocking.md](references/mocking.md) when a spec needs a mock.
4. Write one spec for one behavior in the spec file the project places beside the code, with the coverage comment from `test-quality.md`.
5. Run the focused spec per `running.md`, and report the result.
6. Self-check by reading: spec setup reaches the intended state; assertions would fail on the regression; no spec mocks the code's own modules; no expected value is recomputed from the code's formula. Format only changed files.
