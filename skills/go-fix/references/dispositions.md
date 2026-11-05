# Dispositions

One entry per selected finding, keeping its ID. The caller records them.

```markdown
### 3. Warning — SidebarComponent

- **Disposition:** accepted | deferred | disputed | ignored
- **Done:** Removed host binding. Sidebar found by its own ID.
- **Status:** fixed (e4f5g6h)
```

## Fields

- **Done:** final change, one line, at most 20 words, fragments; code, identifiers, paths, errors exact.
- **Status:** `fixed (e4f5g6h)`, `fixed, tested`, `fixed, not tested`, `deferred`, `disputed`, `ignored by user`. An uncommitted fix has no SHA.
- Deferred or disputed stays `TODO`; applied fixes go to `RESOLVED`; `IGNORED` needs the user's explicit choice.

## Approval

- "Set status to approved": change nothing (no review, edits, tests, finding changes). Reply `Status: approved`.

## Count

- End with open count by severity (Critical, Warning, Minor). A fix is not a new review; keep the original range.
