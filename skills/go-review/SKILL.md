---
name: go-review
description: 'Review a branch, diff or work-in-progress change against the project''s standards and the supplied objective or bug, and return the review report in the reply. Use for "review my branch" or "review this diff".'
---

# Review

Report as the caller specifies. The report is the reply; write no file.

Run in the main thread as coordinator: pick the tier, start the review agents, assemble the report. Never read hunks yourself; agents read the code.

## 1. Fetch

One `go-triage` Fetch call (per [agents.md](references/agents.md)) gathers everything at once. Ask only what is missing:

- Ticket text, when the requirement is a ticket URL or key, including linked tickets.
- Baseline evidence, unless the user supplied the baseline.
- Diff facts for the range.
- File text of `REVIEW.md`, for the risky paths it marks.
- Re-review: delta files from `Reviewed to`, checked against the files of open `TODO` findings.

Decide from its facts yourself: the baseline per [scope-baseline.md](references/scope-baseline.md), then the tier.

## 2. Inputs and tier

- **Requirements:** caller-supplied text, path, fetched ticket text, or plan. None or unreachable: review at once with what you have; agents still apply **Correctness** in [checks.md](references/checks.md).
- **Previous review:** earlier report from the caller, if any.
- **Tier:** from the diff facts, per [agents.md](references/agents.md). The caller or user may name a tier; it wins.

## 3. First review

1. Start every hunter of the tier in parallel, per [agents.md](references/agents.md) and [hunter.md](references/hunter.md).
2. Collect their candidates. Quick: the single hunter returns findings; skip step 3.
3. Start one verifier with all candidates, per [verifier.md](references/verifier.md).
4. Number the verifier's findings by severity; place them per [report-format.md](references/report-format.md). Relay the verifier's dropped lines in the reply above the report.

## 4. Re-review

Given a previous review, return it updated in full. Delta: `git diff <Reviewed to>` through the working tree.

1. **Round cap:** previous `Round` is 3 or more: run 4.2 and 4.4 only; hunt nothing new. Say in `Open`: `round cap: reconsider the approach`.
2. **Open findings:** a `TODO` whose file the delta files leave untouched stays as written. The rest go to one recheck agent per [agents.md](references/agents.md).
   - `fixed`: move to `RESOLVED` as one `Done` line (at most 20 words) plus `Status: fixed (<short SHA>)`.
   - `open`: keep its two lines.
3. **New code:** hunt the delta only, at the tier the delta's own diff facts give. Pass every earlier finding (all sections) as known.
4. New findings numbered after the last. Update `Issue Count` (open `TODO` only), `Reviewed to`, `Round`. Leave `Tests` as written.

- A reported test failure the fix does not address is a finding; send it to the hunters as a lead.

## 5. Reply

End the reply with the report per [report-format.md](references/report-format.md). A caller's handoff lines go above it: `Changed: none`; `Open:` open issue count by severity.

- Report only and end the reply with the report. `go-fix` applies fixes when the caller or user asks for them.
- No subagents in this host: run each role's reference yourself, in order (hunters, then verifier).
