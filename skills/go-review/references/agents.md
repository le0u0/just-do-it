# Review Agents

## Tier

Count changed lines and files from the fetched diff facts, excluding paths in [scope-baseline.md](scope-baseline.md) `Exclude`.

- **Deep:** a risky path is touched (auth, permissions, payment, billing, schema or migration, data deletion, secrets, CI or release, installers, or a path `REVIEW.md` marks), or more than 1000 changed lines.
- **Quick:** at most 150 changed lines in at most 3 files, no risky path.
- **Standard:** everything else.

## Roles

Each call maps the role's tier per [host mapping](../../justaway/references/agents.md#host-mapping), whatever model runs the main thread.

| Role | Tier | Quick | Standard | Deep |
| --- | --- | --- | --- | --- |
| Fetch: `to-triage` Fetch job | `fast` | 1 | 1 | 1 |
| Hunter: Correctness | `standard` | 1, all lenses, verifies its own | 1 | 1 |
| Hunter: Contract | `standard` | — | 1 | 1 |
| Hunter: Security | `standard` | — | — | 1 |
| Verifier | `reasoning` | — | 1 | 1 |
| Recheck (re-review only) | `fast` | 1 | 1 | 1 |

Lenses from [review-method.md](review-method.md):

| Hunter | ID prefix | Lenses |
| --- | --- | --- |
| Correctness | `R` | Logic, State and data, Async and lifecycle, Failure paths |
| Contract | `K` | Contract, Regression, Requirements, and the Standards axis |
| Security | `S` | Security, and Regression on access or data paths |

## Start

- Announce each worker launch before starting per [Announce](../../justaway/references/agents.md#announce).
- Start each hunter, verifier, and recheck worker fresh per [host mapping](../../justaway/references/agents.md#host-mapping) (avoid forks and avoid resuming earlier review workers), and clean them up when done. Reuse the session's `to-triage` worker for `Fetch` when available.
- Fetch prompt names `to-triage` and its absolute `SKILL.md` path, the Fetch job, and each ask with its refs, paths or URLs.
- Prompt: role, repository path, baseline and range, absolute path of the role's reference in this skill, requirement text or path, project rule paths, and any project-local review skill paths from Fetch. Agents read the diff themselves.
- Payloads (candidates for the verifier, known findings for hunters, open findings for recheck) go in one file in system temp; the prompt names its path.
- Hunters of one review get the same prompt, except role, ID prefix and lenses, in that order.
- Release finished one-shot `recheck` or standalone `Fetch` workers before hunting; keep a reusable `to-triage` worker alive. With too few slots, batch hunters, collect all candidates, then run the verifier.

## Recheck

Input: each open finding's number, heading, `Issue`, `Fix`, and the delta command for its file.

Per finding, one line: `<number>: fixed | open — <at most 12 words>`. `fixed` only when the delta plainly removes the cited trigger; anything less is `open`.
