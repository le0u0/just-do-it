# Running and Debugging

## Run

- Take command, folder, arguments, base URL, and auth state from `~/.just-do-it/{project}/public/test-config.md` (and runner config).
- Pass the documented base URL. Unresolvable: ask.
- Run exactly the spec files named by the user or `agent-view/plan.md`'s `E2E` line, by file argument and name filter. Prefix `PLAYWRIGHT_HTML_OPEN=never`.
- Folder, tag, full suite, or e2e UI only when asked.
- Runner cannot select by file: record `Status: blocked` in `agent-view/e2e.md` and report.

## Report (`agent-view/e2e.md`)

- Run without a pipe. Report the real exit code, or unknown, for this run only.
- Write or update `~/.just-do-it/{project}/{branch}/agent-view/e2e.md` per [Test report](../../go-flow/references/reports.md#test-report-agent-viewutmd-and-agent-viewe2emd) and return the summary and saved path.
- `Result`: counts, such as `12 specs, 0 failed`, plus each failed spec file and test name.
- Include failure excerpts under `Failure` in `agent-view/e2e.md` and in the reply.
- State the symptom; leave the cause to `go-work`.
- `Affected`: other specs using the changed code, helpers, or selectors, unrun.
- Check wrapper scripts for file writes first. Compare the worktree before and after.
- Rerun only failed tests, only when verification was requested (updating `agent-view/e2e.md`).

## Debug

Only when asked, and only when `npx playwright test --help` lists `--debug=cli`. Otherwise report the runner output.

1. Run the one failing test with `--debug=cli` in the background.
2. `playwright-cli attach <session>`.
3. Inspect `snapshot`, `console`, `requests` at the failing step.
4. Stop the background run.
5. Report cause and proposed fix, usually a locator or expectation. Change no file unless asked.
