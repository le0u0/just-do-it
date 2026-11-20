# Dispositions

One entry per selected finding, keeping its ID. Update `agent-view/review.md` (plus `dev-view/review.html` and `agent-view/checklist.md` when present) in place.

```markdown
### 3. Warning — SidebarComponent

- **Disposition:** accepted | deferred | disputed | ignored
- **Done:** Removed host binding. Sidebar found by its own ID.
- **Status:** fixed (e4f5g6h)
```

## Fields

- **Done:** final change, one line, at most 20 words, fragments; code, identifiers, paths, errors exact.
- **Status:** `fixed (e4f5g6h)`, `fixed, tested`, `fixed, not tested`, `deferred`, `disputed`, `ignored by user`. An uncommitted fix has no SHA.
- Deferred or disputed stays `TODO`; applied fixes move to `RESOLVED` in `agent-view/review.md`; `IGNORED` needs the user's explicit choice.
- When a fix is committed or amended, also update `agent-view/CHANGELOG.md` per [storage.md](../../go-setup/references/storage.md).

## Approval

- "Set status to approved": change nothing in code or tests; set `Status: approved` in `agent-view/review.md` (and `dev-view/review.html` when present) and reply `Status: approved`.

## Count

- Update `Issue Count` in `agent-view/review.md` (and `dev-view/review.html` when present) and end the reply with open count by severity (Critical, Warning, Minor). A fix is not a new review; keep the original range until `go-review` runs again.
