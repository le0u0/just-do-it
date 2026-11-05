# Dispositions

Return one entry per selected finding, keeping its ID. The caller records them in the review and checklist.

```markdown
### 3. Warning — SidebarComponent

- **Disposition:** accepted | deferred | disputed | ignored
- **Done:** Removed host binding. Sidebar found by its own ID.
- **Status:** fixed (e4f5g6h)
```

## Fields

- **Done:** the final change, one line, at most 20 words. Fragments; code, identifiers, paths and error strings stay exact.
- **Status:** such as `fixed (e4f5g6h)`, `fixed, tested`, `fixed, not tested`, `deferred`, `disputed`, or `ignored by user`. A fix left uncommitted has no SHA.
- A finding stays open (`TODO`) when deferred or disputed; applied fixes move to `RESOLVED`; `IGNORED` needs the user's explicit choice.

## Approval

For "set review status to approved", change nothing: no new review, source edits, tests, or finding changes. Reply `Status: approved` for the caller to record.

## Count

End with the open finding count by severity (Critical, Warning, Minor) after the fixes. A fix is not a new review; keep the original reviewed range.
