# Run Unit Tests

## Scope

- Use the setup from [test-setup.md](test-setup.md).
- Focused specs only: the step's specs; on a rerun, the failed specs plus those the fix changed.

## Steps

1. Read the `package.json` scripts (or build files), runner config, and runtime version.
   - Check wrapper scripts first. Run the project's own script or local binary, never a global CLI.
   - Pick a command that selects tests without rewriting source or configuration.
   - Never install or upgrade a runner to gain a selector.
2. Select the spec with the project's documented command and arguments, such as a file path or name filter. Quote globs for zsh. Keep the configured project, browser, and watch options.
3. Record worktree and index state first, including existing user edits to test setup and configuration.
   - Run only the target, without a pipe.
   - Report the real exit code; unknown if it can't be captured.
   - Keep zero tests, compilation failures, and environment failures apart from assertion failures.
4. Check status and diff afterward, even on failure. Tracked source, configuration, and user files must be unchanged.
   - A helper rewrote files: stop using it, undo only this run's changes from captured content, keep earlier edits, report it.
   - Never use a broad checkout or reset.
5. Report each command, exit code, and outcome.
6. Slow runs (selection impossible, full suite only): before each rerun, list every known cause and fix them all in one run; read the failure for the real cause before changing the spec or mock again.

## On failure

- Report each failed spec file and test name, and the symptom, in `Result`.
- Put only the failed tests' output (name, error, top stack lines) in the reply.
- List other specs using the changed code, helpers, or selectors, not run, as `Affected`.
- `go-work` fixes the code. Change a spec only when it contradicts the plan, and say so. Cause and fix are not this skill's job.

## Protected files

- Never edit test bootstrap, runner configuration, compiler configuration, or package scripts, including while writing specs.
- Add no focused or disabled tests.
- Repairing test infrastructure is separate explicit scope.

## Blocked selection

- Runner can't select the tests or the command is blocked: report `blocked` with the exact limit and next step.
- Report unrelated compilation failures without editing those specs.
