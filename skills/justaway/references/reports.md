# Handoff and Reports

## Handoff

- Send paths or the text the job needs: current plan step, files, review text or path, and the glossary and ADR text the job needs. Skills read nothing from storage.
- State job, acceptance criteria, test authorization, commit rules in at most twelve lines. The agent has none of the conversation.

## Report

At most eight lines, facts only:

```text
Status: done | failed | blocked
Changed: <files, or none>
Commands: <command → exit code, or none>
Artifacts: <paths, or none>
Open: <what remains or needs the user, or none>
```

## Test report

`go-e2e` after a run, and a unit run, end with this instead, at most eight lines:

```text
Status: done | failed | blocked
Result: <counts>; failed: <spec file and test name each, or none>
Commands: <command → real exit code>
Changed: <files, or none>
Artifacts: <failure log path, or none>
Affected: <other specs that use the changed code, helpers, or selectors, not run, or none>
Open: <or none>
```

- **done:** `Result` has counts (`12 specs, 0 failed`), `Commands` exit 0. No log.
- **failed:** failed spec file and test name in `Result`; `Artifacts` is a log of only failed tests' output (name, error, top stack lines) in the branch folder's `state/`, else system temp. State the symptom, not the cause.
- **blocked:** `Open` has the reason and the needed action (`approve a full-suite run`, `start the backend`). No log.

## Scope of a run

- Only specs the task changed, unless the user asks for more.
- Rerun after a fix: previously failed specs plus specs the fix changed.
- Other possibly affected specs go under `Affected`, unrun.
