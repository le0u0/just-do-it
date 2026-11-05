# Diagnose Format

For a bug ticket whose diagnosis would clutter the plan, return it after the plan in this shape, per the [writing rules](writing-rules.md). The caller saves it.

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

## Rules

- `Conclusions` come first: at most five bullets, only what affects scope, design, risk, or validation.
- `Rejected`: one short reason each.
- Label each evidence line fact, inference, or unverified.
- The diagnosis is evidence, not authorization. Copy its conclusions into the plan's `Decisions` for approval. Never keep competing scopes across both.
