# Diagnose Doc

Return a diagnosis in the reply in this shape; write no file, the caller saves it. Every point is one line, at most 15 words, in fragments; code, identifiers, paths, and error strings stay exact:

```markdown
# Diagnose: PROJ-123 question

## Conclusions

- Root cause: `x` skips guard when flag off.
- Affected path: `a.ts:12` to `b.ts:40`.
- Unverified: prod flag default.

## Rejected

- Cache stale: value fresh in trace.

## Evidence

- <sub>fact: `a.ts:12` reads flag once.</sub>
- <sub>inference: `b.ts:40` never reruns.</sub>

## Reference

<sub>Repository: /absolute/path/to/repo<br>Branch: PROJ-123-do-something<br>HEAD: a1b2c3d</sub>
```

`Conclusions` come first, at most five bullets, only what affects scope, design, risk, or validation. `Rejected` is one short reason each. Label each evidence line fact, inference, or unverified.

The diagnosis is evidence, not authorization.

