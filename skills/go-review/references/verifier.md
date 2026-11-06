# Verifier

Precision: keep only candidates that hold end to end. You get candidates, not the hunters' reasoning; read the code yourself.

## Verify

- Project rules per [project-references.md](project-references.md); evidence bar per [review-method.md](review-method.md) `Evidence`.
- Per candidate: restate the trigger, trace it through the code, try to disprove it (upstream guard, type, caller contract). Drop what does not hold.
- Keep findings introduced or exposed by the change, including untouched code the change newly breaks.
- `pre-existing` candidates that hold: keep, marked pre-existing.
- Omit: intentional-looking changes, lint-ignored issues, unreachable cases, style preferences, pure renames, tooling-enforced issues.
- A missing contract limits one finding, never the review.
- Deduplicate by root cause across hunters.
- `unclear` recheck items: decide `fixed` or `open`.

## Return

Findings as [report-format.md](report-format.md) blocks, unnumbered, most severe first; pre-existing ones last under `Pre-existing`. Then one line per dropped candidate: `C<n>: dropped — <at most 10 words>`. Then recheck decisions, if any.
