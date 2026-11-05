# Handoff and Reports

## Handoff

- Send paths or the text the job needs: plan step, files, review text or path, `state/context.md`.
- A skill reads nothing from storage; hand it what it needs.
- Send only the current step.
- State job, acceptance criteria, test authorization, commit rules in at most twelve lines.
- The agent has none of the conversation. Never paste it, a plan, a diff, or a log.

## Report

An agent ends with at most eight lines:

```text
Status: done | failed | blocked
Changed: <files, or none>
Commands: <command → exit code, or none>
Artifacts: <paths, or none>
Open: <what remains or needs the user, or none>
```

- Facts only: no narrative, restated plan, code excerpts.

## Test report

`go-e2e` after a run, and a unit run, end with this report instead, at most eight lines:

```text
Status: done | failed | blocked
Result: <counts>; failed: <spec file and test name each, or none>
Commands: <command → real exit code>
Changed: <files, or none>
Artifacts: <failure log path, or none>
Affected: <other specs that use the changed code, helpers, or selectors, not run, or none>
Open: <or none>
```

- **done:** `Result` has the counts (such as `12 specs, 0 failed`); `Commands` has exit 0. Send no log or output.
- **failed:**
  - List each failed spec file and test name in `Result`.
  - `Artifacts` is a log of only the failed tests' output (name, error, top stack lines), saved in the branch folder's `state/`, else the system temp directory.
  - State the symptom; leave the cause to the manager.
- **blocked:** `Open` has the reason and what the manager or user should do, such as `approve a full-suite run` or `start the backend`. Send no log.

## Scope of a run

- Run only the specs the task changed, unless the user asks for more.
- Rerun after a fix: the previously failed specs plus the specs the fix changed.
- List other specs that may be affected under `Affected`, unrun.
