# Dispositions

One entry per selected finding. Update `agent-view/review.md` (plus `dev-view/review.html` and `agent-view/checklist.md` when present) in place.

```markdown
### Warning — SidebarComponent

- **Disposition:** accepted | deferred | disputed | ignored
- **Done:** Removed host binding. Sidebar found by its own ID.
- **Status:** fixed (e4f5g6h)
```

## Fields

- **Done:** final change, one line, at most 20 words, fragments; code, identifiers, paths, errors exact.
- **Status:** `fixed (e4f5g6h)`, `fixed, tested`, `fixed, not tested`, `deferred`, `disputed`, `ignored by user`. An uncommitted fix has no SHA.
- Deferred or disputed stays `TODO`; applied fixes move to `RESOLVED` in `agent-view/review.md`; `IGNORED` needs the user's explicit choice.
- Keep the number while a finding stays in `TODO`. Remove it from the heading and HTML card when the finding moves out. Preserve `Last TODO number` per the [report format](../../go-review/references/report-format.md#fields).
- Keep the finding's verification steps and expected result when moving it. Record the actual scoped check and outcome if run.
- When a fix is committed or amended, also update `agent-view/CHANGELOG.md` per [storage.md](../../go-setup/references/storage.md).

## Approval

- "Set status to approved": change nothing in code or tests; set `Status: approved` in `agent-view/review.md` (and `dev-view/review.html` when present) and reply `Status: approved`.

## Count

- Update `Issue Count` in `agent-view/review.md` (and `dev-view/review.html` when present) and end with the open count by severity. Keep the recorded coverage, comparison range, snapshot, round, and acceptance evidence. If the checkout changed, mark its evidence stale for the current checkout.
