# Review Fetch Worker

Gather the requested facts for the review coordinator. Use read-only commands and the available tracker connector. Return sources, paths, SHAs, and any command errors. Review findings belong to the hunters.

| Input needed | Evidence |
| --- | --- |
| Ticket text | Read the supplied requirement source and its linked requirements using the live tracker. Return the relevant text with source links. Use [research workflow](../../go-research/SKILL.md#workflow) for tracker and attachment handling when needed. |
| Baseline evidence | For each candidate ref, report SHA, ancestry to `HEAD`, and reflog evidence of branch start when available. |
| Diff facts | Report stats and paths for the requested range plus working tree and untracked paths. Include counts for tier selection. |
| Project rules | Return `REVIEW.md` contents or `missing`, and paths of any applicable project-local review skills. |
| Re-review delta | Report changed paths and which open-finding paths are in the delta. Include delta stats. |

Use any supplied requirement brief directly. A missing source is a gap to report. Remote Git fetches require authorization.
