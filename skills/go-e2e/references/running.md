# Running and Debugging

## Run

- Take command, project, arguments, and auth state from `package.json` and the runner config.
- Pass the documented base URL. Unresolvable: ask.
- Run exactly the spec files the handoff names (the plan's `E2E` line), by file argument and name filter. Prefix `PLAYWRIGHT_HTML_OPEN=never`.
- Folder, tag, full suite, or e2e UI only when asked.
- Runner cannot select by file: report `blocked`.

## Report

- Run without a pipe. Report the real exit code, or unknown, for this run only.
- `Result`: counts, such as `12 specs, 0 failed`, plus each failed spec file and test name.
- Failed-only log in the system temp directory (name, error, top stack lines). Report its path.
- State the symptom; leave the cause to the caller.
- `Affected`: other specs using the changed code, helpers, or selectors, unrun.
- Check wrapper scripts for file writes first. Compare the worktree before and after.
- Rerun only failed tests, only when verification was requested.

## Debug

Only when asked, and only when `npx playwright test --help` lists `--debug=cli`. Else report from the log.

1. Run the one failing test with `--debug=cli` in the background.
2. `playwright-cli attach <session>`.
3. Inspect `snapshot`, `console`, `requests` at the failing step.
4. Stop the background run.
5. Report cause and proposed fix, usually a locator or expectation. Change no file unless asked.
