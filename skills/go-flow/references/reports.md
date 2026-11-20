# Handoff and Reports

## Handoff

- Pass the resolved branch storage directory (`~/.just-do-it/{project}/{branch}/`), current plan step, owned files, and relevant decisions. A worker reads its inputs from `agent-view/`, `dev-view/`, and `public/`, and performs its own local discovery.
- State job, acceptance criteria, test authorization, commit rules in at most twelve lines. The agent has none of the conversation.

## Report

For routine implementation and test jobs, at most eight lines of status and evidence.

```text
Status: done | partial | failed | blocked
Changed: <files, or none>
Commands: <command → exit code, or none>
Artifacts: <saved paths under agent-view/ or dev-view/, or none>
Open: <what failed/timed out/denied or remains, or none>
```

On `partial`, `failed`, or `blocked`, `Open` states the failed step/tool, reason, and missing work. Never report `done` when a required step failed.

## Test report (`agent-view/ut.md` and `agent-view/e2e.md`)

After a unit (`go-ut`) or E2E (`go-e2e`) run, write or update `agent-view/ut.md` or `agent-view/e2e.md` in the resolved branch directory and return the summary to the caller. In `go-ut` evidence-only mode, return the same fields directly to the coordinator without writing the shared report. Record a reproducible snapshot of HEAD, index, tracked working-tree contents, and untracked non-ignored files immediately before and after the run. If the snapshots differ, report the result as stale for the full checkout. Keep status fields within eight lines and include any failure excerpt.

Compute the snapshot from the full `git rev-parse HEAD`, the NUL-delimited index entries from `git ls-files --stage -z`, binary `git diff --no-ext-diff --binary HEAD`, and sorted NUL-delimited names and content hashes of untracked non-ignored files from `git ls-files --others --exclude-standard -z`. Include file modes and symlink targets in those hashes. Use `git --no-optional-locks` for these queries so evidence collection does not refresh the shared index. Hash the length-delimited components together with SHA-256. Record the hash and method; do not rely on timestamps. If a component cannot be read or the repository changes while collecting it, mark the result stale.

```markdown
# Unit Test Results

- **Status:** done | failed | blocked
- **Result:** <counts>; failed: <spec file and test name each, or none>
- **Commands:** `<command>` → <real exit code>
- **Changed:** <files, or none>
- **Affected:** <other specs that use the changed code, helpers, or selectors, not run, or none>
- **Open:** <or none>

## Failure

<runner excerpt, or None.>

## Reference

<sub>Repository: /absolute/path/to/repo<br>Branch: feature-branch<br>HEAD: a1b2c3d<br>Snapshot: reproducible snapshot and method</sub>
```

(`agent-view/e2e.md` uses `# E2E Test Results` with the same fields.)

- **done:** `Result` has counts (`12 specs, 0 failed`), `Commands` exit 0. `Failure` is `None.`.
- **failed:** put each failed spec and test name in `Result`. Include the exact error and top relevant stack lines under `Failure`. For a runner or compile failure, include its decisive error.
- **blocked:** `Open` has the reason and the needed action (`approve a full-suite run`, `start the backend`).

## Scope of a run

- Only specs the task changed, unless the user asks for more.
- Rerun after a fix: previously failed specs plus specs the fix changed.
- Other possibly affected specs go under `Affected`, unrun.
