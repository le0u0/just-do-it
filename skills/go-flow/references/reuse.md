# Scheduling

## Parallel steps

1. Fill available worker slots with compatible ready steps from `agent-view/plan.md`. A step is ready after its `Blocked by` steps have been verified and delivered. Use one worker per step and launch the compatible workers before waiting for any result. A conflict delays only the conflicting step. Continue dispatching other ready work.
   - Check owned paths, test inputs, focused runner commands and mutable state. Concurrent steps need disjoint writes and tests independent of sibling edits. Use existing runner isolation for shared databases, fixtures, ports, build output, or caches when it makes tests independent. A file filter alone does not prove independence.
   - Run conflicting or uncertain steps in sequence with each other.
2. Give each worker the resolved branch storage directory (`~/.just-do-it/{project}/{branch}/`), step number, owned paths, current checkout and branch, starting checkout state, and authorized tests. Each worker runs `dev-tdd` through `go-work` (which calls `go-ut` / `go-e2e`). If it finds a sibling dependency or shared-state conflict, pause the affected work and resume it in sequence. Keep existing edits intact.
3. Verify each step's actual diff and red and green evidence. A test failure caused by sibling work is invalid as red evidence. Rerun affected checks after overlapping work stops and report any red result that could not be verified. Preserve pre-existing changes.
4. With per-step commits, wait for the active wave to finish editing, then commit verified steps one at a time in plan order. Use each approved one-line message. Scope the commit to the verified step's paths, adding only new files for those paths as needed. Check staged and unstaged diffs first, preserve unrelated staging, and verify the commit's SHA and paths. Follow the [commit gate](../../go-work/references/step-execution.md#commit-gate). When fixing a mistake in the unpushed `HEAD` step commit, amend it (`git commit --amend --no-edit`) instead of piling on extra fix commits, and ensure `agent-view/CHANGELOG.md` is updated with every commit or amendment. In leave-uncommitted mode, relay step approval when required; leave index and HEAD untouched.
5. Mark each delivered step in `agent-view/checklist.md` and schedule the next ready steps. A failed step blocks its dependents. Keep independent work moving when safe.

## Worker reuse

- Reuse the planner across grill rounds. If replaced, supply `agent-view/research.md`, confirmed decisions, and current frontier.
- Use one E2E worker for the task. Reuse the research worker only for requirement research.
- Resume a step's worker for that step's fixes and missing evidence. Release it after verification and delivery.
- Review starts and cleans up its own workers. It reads any existing `agent-view/review.md` for re-review.
