# Run Unit Tests

Run unit tests with the setup found per [test-setup.md](test-setup.md), when the request or approved plan authorizes them; a later no-tests instruction wins. Run focused specs only: the step's specs, and on a rerun the failed specs plus the specs the fix changed. The full suite runs only when the user asks.

1. Read the `package.json` scripts (or the project's build files), the test runner config, and the runtime version. Check wrapper scripts first; run the project's own script or local binary, never a globally installed CLI, and pick a command that selects tests without rewriting source or configuration. Never install or upgrade a runner to gain a selector.
2. Select the spec with command arguments, such as a file path or name filter, using the project's documented command. Quote globs for zsh. Keep the configured project, browser, and watch options.
3. Record the worktree and index state first, including existing user edits to test setup and configuration. Run only the target, without a pipe, and report its real exit code; when it can't be captured, report it as unknown. Keep zero tests, compilation failures, and environment failures apart from assertion failures.
4. Check status and diff afterward, even on failure. Tracked source, configuration, and user files must be unchanged. When a helper rewrote files, stop using it, undo only this run's changes from the captured content, keep earlier edits, and report it. Never use a broad checkout or reset.
5. Report each command, exit code, and outcome in the reply.

## On failure

Report each failed spec file and test name, and the symptom. `go-work` fixes the code; change a spec only when it contradicts the plan, and say so. The cause and the fix are not this skill's job.

On `failed`, list each failed spec file and test name in `Result`, and put only the failed tests' output (name, error, top stack lines) in the reply. List other specs that use the changed code, helpers, or selectors, not run, as `Affected`.

## Protected files

Test bootstrap and runner configuration, compiler configuration, and package scripts stay unedited. Add no focused or disabled tests. Repairing test infrastructure is separate explicit scope. Writing specs leaves them unedited too.

## Blocked selection

When the runner cannot select the tests or the command is blocked, report it as `blocked` with the exact limit and the next step. Ask before running the full suite; leave the harness and unrelated tests alone. Report unrelated compilation failures without editing those specs.
