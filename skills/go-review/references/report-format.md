# Review Report

## Style

- Fragments; code, identifiers, paths, error strings exact. Present state only.
- Reference detail goes in `<sub>`.
- Issue, Fix, Done: one line each, at most 20 words, no file location.
- Never mention a ticket, its requirements, or progress.

## Template

```markdown
# Code review

Status: reviewed

## Issue Count

TODO: 2 (Critical: 0, Warning: 2, Minor: 0)

## Tests

- Unit: pass, 2 specs
- E2E: not run: no e2e spec in the diff

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

## PRE-EXISTING

None.

## Reference

<sub>Repository: /absolute/path/to/repo<br>Branch: feature-branch<br>Reviewed from: a1b2c3d<br>Reviewed to: e4f5g6h<br>Diff fingerprint: hash when work is uncommitted<br>Tier: Standard<br>Round: 1</sub>
```

## Fields

- **Issue Count:** open `TODO` only, with severity split.
- **Heading:** number, severity, owning class or file.
- **Issue:** trigger and impact. **Fix:** corrective action; one alternative at most.
- **Done / Status:** only in `RESOLVED`; added by the caller from `go-fix` results, or by a re-review that finds an author's fix.
  - `Status`: `fixed (e4f5g6h)`, `fixed, tested`, `fixed, not tested`, `deferred`, `disputed`, `ignored by user`.
- **Tests:** written by the caller, never `go-review`. Starts `Unit: not run`, `E2E: not run`.

## Severity

- Critical: data loss, security breach, corruption, blocking runtime failure.
- Warning: incorrect behavior, regression, missing requirement.
- Minor: low-risk maintainability or convention issue.

## Sections

- `Reference` in `<sub>`. `Tests` plain, under `Issue Count`: `Unit` and `E2E` lines, each `pass`, `fail` with spec names, or `not run: <reason>`.
- Findings by severity; numbers stable across sections; `---` between findings.
- Keep `TODO`, `RESOLVED`, `IGNORED`, `PRE-EXISTING`; `None.` when empty.
  - `TODO`: open, deferred, disputed. `RESOLVED`: applied fixes. `IGNORED`: needs the user's explicit choice. `PRE-EXISTING`: real bugs the change did not introduce or expose; not counted, not sent to `go-fix` unless the user asks.
- `Round`: 1 on a first review, plus 1 per re-review. `Tier`: the tier this round ran.
- `Status: approved` records user approval only.
- Uncommitted work: `Diff fingerprint` identifies the snapshot.
