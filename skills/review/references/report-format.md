# Saved Review

Follow the [written docs](../../manager/references/written-docs.md) rules. Issue, Fix and Done are the main points: one line each, at most 20 words, no file location. The report never mentions a ticket, its requirements, or its progress; that belongs in `checklist.md`.

```markdown
# Code review

Status: reviewed

## Issue Count

TODO: 2 (Critical: 0, Warning: 2, Minor: 0)

## Manual review

1. `export-util.ts:120`
   -> When the box is full, it throws everything out. Should it say "full"?
2. `layout.ts:1149`
   -> Two screens share one notebook. Does a bad save keep the old page?

## TODO

### 1. Warning — ProfileFormComponent

- **Issue:** Failed update leaves Save disabled. No retry.
- **Fix:** Clear pending state on error.

---

### 2. Warning — ExportService

- **Issue:** Overflow drops the export silently.
- **Fix:** Throw and show the error.

## RESOLVED

### 3. Warning — SidebarComponent

- **Done:** Removed host binding. Sidebar found by its own ID.
- **Status:** fixed (e4f5g6h)

## IGNORED

None.

## Tests

<sub>Unit: 2 specs passed<br>E2E: not run</sub>

## Reference

<sub>Repository: /absolute/path/to/repo<br>Branch: feature-branch<br>Reviewed from: a1b2c3d<br>Reviewed to: e4f5g6h<br>Diff fingerprint: hash when work is uncommitted</sub>
```

## Fields

- **Issue Count:** open `TODO` findings only, with their severity split. Count nothing resolved or ignored.
- **Heading:** number, severity, and the owning class or file.
- **Issue:** trigger and impact, one line.
- **Fix:** the corrective action, one line; one alternative at most.
- **Done / Status:** only in `RESOLVED`. Added by `resolve-review`, or alone when a re-review finds an author's fix. `Done` is the final change. `Status` is such as `fixed (e4f5g6h)`, `fixed, tested`, `fixed, not tested`, `deferred`, `disputed`, or `ignored by user`.
- **Manual review:** sits above `TODO`, so the reader knows where to look first. Pick by risk, not size: logic, state, data flow, permissions. Skip renames, templates, styles, generated code, and specs. At most seven, riskiest first. Each is `file:line`, then `-> ` one sentence of at most 20 words in the plain words a five-year-old follows: what the code does and what could go wrong, with an everyday picture and no jargon or code names. Pick them from the diff even when `TODO` is empty. `None.` only when the diff is a few low-risk lines.
- **Tests:** written by the manager from the testers' reports, never by the reviewer. Starts as `Unit: not run` and `E2E: not run`.

## Severity

- Critical: data loss, security breach, corruption, or blocking runtime failure.
- Warning: incorrect behavior, regression, or missing requirement.
- Minor: low-risk maintainability or convention issue.

## Sections

Wrap `Tests` and `Reference` in `<sub>`; the reviewer needs them, the reader does not. Order findings by severity. Numbers stay stable across sections; put `---` between findings. Keep `TODO`, `RESOLVED` and `IGNORED`, writing `None.` when empty. `TODO` holds open, deferred, and disputed findings; `RESOLVED` holds applied fixes; `IGNORED` needs the user's explicit choice. `Status: approved` records user approval only.

Write `review.md` only after the review completes; a re-review updates it. A re-review adds no history: it moves fixed findings to `RESOLVED` as one `Done` line, and keeps every point short. For uncommitted work, `Diff fingerprint` identifies the snapshot.

## Review-only ticket

When the review has a ticket but no plan, save `checklist.md` beside `review.md`, per [checklist-format.md](../../plan/references/checklist-format.md): one item per open finding, the requirement source and review range under `Reference`. Update it on each re-review. Keep all ticket text out of `review.md`.
