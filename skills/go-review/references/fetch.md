# Review Fetch Worker

Gather the requested facts for the review coordinator. Use read-only commands. Return sources, paths, SHAs, and any command errors. Review findings belong to the hunters.

| Input needed | Evidence |
| --- | --- |
| Baseline evidence | For each candidate ref, report SHA, ancestry to `HEAD`, and reflog evidence of branch start when available. |
| Diff facts | Report stats and paths for the requested range plus working tree and untracked paths. Include counts for tier selection. |
| Checkout snapshot | Compute the SHA-256 snapshot using the [test snapshot method](../../go-flow/references/reports.md#test-report-agent-viewutmd-and-agent-viewe2emd), including HEAD, index, tracked worktree diffs, and untracked files. Return the hash and whether `git --no-optional-locks status --porcelain=v1 --untracked-files=all` is empty. Report any collection error. |
| Project rules | Return `REVIEW.md` contents or `missing`, and paths of any applicable project-local review skills. |

Report missing inputs and failed commands with the error and missing evidence. Remote Git fetches require authorization.
