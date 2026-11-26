# Diagnose Format (`agent-view/diagnose.md`)

For a bug ticket whose diagnosis would clutter `agent-view/plan.md`, write it to `~/.just-do-it/{project}/{branch}/agent-view/diagnose.md` per the [writing rules](writing-rules.md).

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

- `Conclusions` first: at most five bullets, only what affects scope, design, risk, or validation.
- `Rejected`: one short reason each.
- Label evidence fact, inference, or unverified.
- Evidence, not authorization: copy conclusions into `agent-view/plan.md` `Decisions` for approval; never keep competing scopes.
