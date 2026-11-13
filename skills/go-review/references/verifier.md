# Verifier

Precision: keep only candidates that hold end to end. You get candidates, not the hunters' reasoning; read the code yourself.

## Verify

- Project rules per [project-references.md](project-references.md); evidence bar per [review-method.md](review-method.md) `Evidence`.
- Per candidate: restate the trigger, trace it through the code, try to disprove it (upstream guard, type, caller contract). Drop what does not hold.
  - Drop for a guard only when the guard covers the trigger's exact case: read what it checks, not that it exists.
  - A candidate that holds in the code but whose reachability you cannot settle (for example, depends on backend data) is kept, marked `unconfirmed`, never dropped.
- Keep findings introduced or exposed by the change, including untouched code the change newly breaks.
- `pre-existing` candidates that hold: keep, marked pre-existing.
- Omit: intentional-looking changes, lint-ignored issues, unreachable cases, style preferences, pure renames, tooling-enforced issues.
- A missing contract limits one finding, never the review.
- Deduplicate by root cause across hunters.

## Return

Findings as [report-format.md](report-format.md) blocks, unnumbered, most severe first; pre-existing ones last under `Pre-existing`. Then one line per dropped candidate: `<candidate ID>: dropped — <at most 10 words>`; a guard drop names the guard as `file:line` and the case it covers.
