# Review Agents

## Tier

Count changed lines and files from the fetched diff facts, excluding paths in [scope-baseline.md](scope-baseline.md) `Exclude`.

- **Deep:** a risky path is touched (auth, permissions, payment, billing, schema or migration, data deletion, secrets, CI or release, installers, or a path `REVIEW.md` marks), or more than 1000 changed lines.
- **Quick:** at most 150 changed lines in at most 3 files, no risky path.
- **Standard:** everything else.

## Roles

Each call sets `model` and `effort` from this table, whatever model runs the main thread.

| Role | Model | Effort | Quick | Standard | Deep |
| --- | --- | --- | --- | --- | --- |
| Fetch: `go-triage` Fetch job | haiku | low | 1 | 1 | 1 |
| Hunter: Correctness | sonnet | medium | 1, all lenses, verifies its own | 1 | 1 |
| Hunter: Contract | sonnet | medium | — | 1 | 1 |
| Hunter: Security | sonnet | medium | — | — | 1 |
| Verifier | opus | medium | — | 1 | 1 |
| Recheck (re-review only) | haiku | low | 1 | 1 | 1 |

Lenses from [review-method.md](review-method.md):

- **Correctness:** Logic, State and data, Async and lifecycle, Failure paths.
- **Contract:** Contract, Regression, Requirements, and the Standards axis.
- **Security:** Security, and Regression on access or data paths.

## Start

- `general-purpose` subagent; never a fork. Fresh for every review; never resume an earlier review's agent.
- Fetch prompt names `just-do-it:go-triage`, the Fetch job, and each ask with its refs, paths or URLs.
- Prompt, at most twelve lines: role, repository path, baseline and range, absolute path of the role's reference in this skill, requirement text or path, project rule paths, known findings. Never paste the diff or the conversation.
- Hunters of one review get the same prompt, except role and lenses, in that order.

## Recheck

Input: each open finding's number, heading, `Issue`, `Fix`, and the delta command for its file.

Per finding, one line: `<number>: fixed | open | unclear — <at most 12 words>`. `fixed` only when the delta removes the cited trigger; otherwise `open`, or `unclear` when the delta changes the code but not plainly.
