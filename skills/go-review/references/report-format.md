# Review Report

## Style

- Fragments: drop articles, filler, hedging.
- Code, identifiers, paths, error strings stay exact.
- Present state only: no history, dates, how a decision was reached.
- Reference detail goes in `<sub>`.
- Issue, Fix, Done: main points. One line each, at most 20 words, no file location.
- Never mention a ticket, its requirements, or its progress.

## Template

```markdown
# Code review

Status: reviewed

## Issue Count

TODO: 2 (Critical: 0, Warning: 2, Minor: 0)

## Tests

- Unit: pass, 2 specs
- E2E: not run: no e2e spec in the diff

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

## Reference

<sub>Repository: /absolute/path/to/repo<br>Branch: feature-branch<br>Reviewed from: a1b2c3d<br>Reviewed to: e4f5g6h<br>Diff fingerprint: hash when work is uncommitted</sub>
```

## Fields

- **Issue Count:** open `TODO` findings only, with severity split. Count nothing resolved or ignored.
- **Heading:** number, severity, owning class or file.
- **Issue:** trigger and impact, one line.
- **Fix:** corrective action, one line; one alternative at most.
- **Done / Status:** only in `RESOLVED`.
  - Added by the caller from `go-fix` results, or alone when a re-review finds an author's fix.
  - `Done`: the final change.
  - `Status`: `fixed (e4f5g6h)`, `fixed, tested`, `fixed, not tested`, `deferred`, `disputed`, or `ignored by user`.
- **Manual review:** above `TODO`, so the reader knows where to look first.
  - Pick by risk, not size: logic, state, data flow, permissions.
  - Skip renames, templates, styles, generated code, specs.
  - At most seven, riskiest first.
  - Each: `file:line`, then `-> ` one sentence of at most 20 words, in plain words a five-year-old follows: what the code does and what could go wrong, with an everyday picture, no jargon or code names.
  - Pick from the diff even when `TODO` is empty. `None.` only when the diff is a few low-risk lines.
- **Tests:** written by the caller from the unit and e2e reports, never by `go-review`. Starts as `Unit: not run` and `E2E: not run`.

## Severity

- Critical: data loss, security breach, corruption, blocking runtime failure.
- Warning: incorrect behavior, regression, missing requirement.
- Minor: low-risk maintainability or convention issue.

## Sections

- Wrap `Reference` in `<sub>`.
- Keep `Tests` plain, right under `Issue Count`: the reader checks it for pass or fail.
  - One line each for `Unit` and `E2E`: `pass`, `fail` with failed spec names, or `not run: <reason>`.
- Order findings by severity. Numbers stay stable across sections; `---` between findings.
- Keep `TODO`, `RESOLVED`, `IGNORED`; write `None.` when empty.
  - `TODO`: open, deferred, disputed findings.
  - `RESOLVED`: applied fixes.
  - `IGNORED`: needs the user's explicit choice.
- `Status: approved` records user approval only.

## Reply

- Reply with the report only after the review completes.
- Re-review: return the supplied report updated in full, with no history. Fixed findings move to `RESOLVED` as one `Done` line; every point stays short.
- Uncommitted work: `Diff fingerprint` identifies the snapshot.
