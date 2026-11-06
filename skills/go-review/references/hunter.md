# Hunter

Find candidates under your lenses. High recall: report what you cannot rule out; the verifier filters.

## Read

- Project rules per [project-references.md](project-references.md).
- Method: the repository's own review skill (method only, not its scope, delivery, format), else [review-method.md](review-method.md).
- The scoped diff once. Cover every hunk.

## Hunt

- Code only; run no tests, edit nothing.
- One pass over all hunks per lens you were given; each pass collects candidates.
- Follow each changed value or behavior to every reader: callers, siblings sharing the contract, templates, specs.
- Apply the relevant [checks.md](checks.md); Contract hunter also [smells.md](smells.md).
- Check changed code follows comments in modified files.
- Risky hunk (changed condition, removed guard): `git log -L` or `git blame`; flag a change that undoes earlier intent.
- Per candidate, search other changed files and sibling code for the same pattern; one candidate per root cause, listing every location.
- Skip known findings the caller passed, and anything they cover.

## Return

At most 15 candidates, most likely first, nothing else:

```text
C1 | path:line[, path:line] | lens | trigger: <input or state> -> <wrong result> | evidence: <what in the code shows it> | new | pre-existing
```

- `pre-existing`: the bug sits in code the change did not touch and does not newly reach.
- None: `no candidates`.

## Quick tier

You are also the verifier: run [verifier.md](verifier.md) on your candidates and return its output instead.
