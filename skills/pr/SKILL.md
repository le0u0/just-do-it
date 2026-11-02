---
name: pr
description: 'Write the pull request title and body for a finished branch: a visual summary, before and after evidence, and merge danger. Text, and opens the PR when asked. Use for "pr", "create a PR", "open a PR", "write the PR", "PR text" or "commit, push, pr".'
effort: medium
metadata:
  tier: standard
---

# PR

Report per [reports.md](../manager/references/reports.md). Produce text; open the PR only when the user asks, per step 6.

1. Gather the branch folder's `plan.md`, `checklist.md`, and approved `review.md`, and the diff from the plan's initial baseline. With no branch folder, use the diff and what the user told you. Use the project's own terms.
2. Write the title as one line in the project's commit format.
3. Write the body per [pr-format.md](references/pr-format.md). Keep prose short and skip preambles.
4. Save it as `pr.md` in the branch folder. The one-line rule for written docs does not apply to the body.
5. Reply with the title, the body, and the path.
6. Only when the user asked to open or create the PR: read the host from `git remote get-url origin` and the base branch from `git symbolic-ref refs/remotes/origin/HEAD`, returning the question as `Open` when either is unclear. Push the current branch if it has no remote copy, never forced. Open the PR with the host's CLI using the saved title and body, such as `gh pr create --base <base> --title <title> --body-file <path>` for GitHub. For a host with no CLI available, give the new-PR URL and say the PR is not opened: GitHub `<repo-url>/compare/<base>...<branch>`, Bitbucket `<repo-url>/pull-requests/new?source=<branch>&dest=<base>`, GitLab `<repo-url>/-/merge_requests/new?merge_request[source_branch]=<branch>`. For another host, say the URL is unknown. Report the PR URL.

Done when the title is one line and every acceptance criterion in `plan.md` has evidence or `not run` in the body.
