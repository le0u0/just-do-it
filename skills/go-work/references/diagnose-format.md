# Diagnose Doc

## Output

- One line per point, at most 15 words, fragments. Code, identifiers, paths, error strings exact.

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

## Sections

- `Conclusions`: first, at most five bullets, only what affects scope, design, risk, or validation.
- `Rejected`: one short reason each.
- `Evidence`: label each fact, inference, or unverified.
- The diagnosis is evidence, not authorization.
