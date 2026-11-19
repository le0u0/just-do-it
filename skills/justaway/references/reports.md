# Handoff and Reports

## Handoff

- Send the paths or text needed for the job: current plan step, owned files, review, and relevant decisions. A worker reads only the task documents it was given and performs its own local discovery.
- State job, acceptance criteria, test authorization, commit rules in at most twelve lines. The agent has none of the conversation.

## Report

For routine implementation and test jobs, at most eight lines of status and evidence. Research returns its full brief. Planning returns a question round or the full plan and checklist.

```text
Status: done | failed | blocked
Changed: <files, or none>
Commands: <command → exit code, or none>
Artifacts: <paths, or none>
Open: <what remains or needs the user, or none>
```

## Test report

After a unit or E2E run, return this to the coordinator, or to the user for a direct run. Keep the status fields within eight lines. Include the failure excerpt in the same response.

```text
Status: done | failed | blocked
Result: <counts>; failed: <spec file and test name each, or none>
Commands: <command → real exit code>
Changed: <files, or none>
Affected: <other specs that use the changed code, helpers, or selectors, not run, or none>
Open: <or none>
Failure: <runner excerpt, or none>
```

- **done:** `Result` has counts (`12 specs, 0 failed`), `Commands` exit 0. No log.
- **failed:** put each failed spec and test name in `Result`. Include the exact error and top relevant stack lines under `Failure`. For a runner or compile failure, include its decisive error. The coordinator can record the result in its checklist or review. Create a separate log file only when the user requests one.
- **blocked:** `Open` has the reason and the needed action (`approve a full-suite run`, `start the backend`). No log.

## Scope of a run

- Only specs the task changed, unless the user asks for more.
- Rerun after a fix: previously failed specs plus specs the fix changed.
- Other possibly affected specs go under `Affected`, unrun.
