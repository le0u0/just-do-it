# Review Report (`agent-view/review.md`)

## Style

- Fragments; code, identifiers, paths, error strings exact. Present state only.
- Reference detail goes in `<sub>`.
- Actual, Fix, Done: one line each, at most 20 words, no file location.
- Keep ticket acceptance evidence in `Acceptance`.

## Template

```markdown
# Code review

Status: reviewed

## Issue Count

TODO: 2 (Critical: 0, Warning: 2, Minor: 0)

## Tests

- Unit: [ut.md](ut.md)
- E2E: [e2e.md](e2e.md)

## Acceptance

- Expected 1 · Save sends one request · pass · [E2E](e2e.md), duplicate-click scenario
- Expected 2 · Save can retry after failure · unverified · retry action untested

## TODO

### 1. Warning — <span title="src/app/profile/profile-form.component.ts">ProfileFormComponent</span>

- **How to verify:**
  1. Open Edit Profile. Make the save request return HTTP 500.
  2. Click Save. After the error banner appears, check whether Save is enabled.
- **Expected:** Save is enabled and accepts a retry.
- **Actual:** Code only: Failed update leaves Save disabled. No retry.
- **Fix:** Clear pending state on error.

---

### 2. Warning — <span title="src/app/export/export.service.ts">ExportService</span>

- **How to verify:**
  1. Fill the export queue to its limit.
  2. Request one more export and check the response.
- **Expected:** The caller receives an explicit queue-full error.
- **Actual:** Code only: Overflow drops the export silently.
- **Fix:** Throw and show the error.

## RESOLVED

### Warning — SidebarComponent

- **Done:** Removed host binding. Sidebar found by its own ID.
- **Status:** fixed (e4f5g6h)

## IGNORED

None.

## PRE-EXISTING

None.

## Reference

<sub>Repository: /absolute/path/to/repo<br>Branch: feature-branch<br>Reviewed from: a1b2c3d<br>Reviewed to: e4f5g6h<br>Coverage: full<br>Snapshot: checkout hash<br>Checkout clean: yes<br>Review inputs: input hash<br>Tier: Standard<br>Round: 1<br>Last TODO number: 2</sub>
```

## Fields

- **Issue Count:** open `TODO` only, with severity split.
- **Heading:** severity and owning class or file. Prefix with a number only in `TODO`.
- **Last TODO number:** retain the highest number assigned so later findings never reuse it. When updating an older report, initialize this value from its highest finding heading number before removing numbers from non-`TODO` sections.
- **How to verify:** name the exact screen and controls, or the test entry point. Include setup or input and up to four short steps. State any missing setup. Show file references as short labels with the exact path in their `title` attributes.
- **Expected:** the observable result if the check passes. Put it before `Actual`.
- **Actual:** the wrong result and its impact. Prefix with `Code only:` when inferred or `Unconfirmed:` when reachability is unsettled. Link an actual run when available. When reading an older report, treat its `Issue` field as `Actual`.
- **Fix:** corrective action; one alternative at most.
- **Finding reference:** put the source path and optional line in a tooltip on the owner or a short source label.
- **Done / Status:** only in `RESOLVED`; updated by `go-fix` or by a re-review that finds an author's fix.
  - `Status`: `fixed (e4f5g6h)`, `fixed, tested`, `fixed, not tested`, `deferred`, `disputed`, `ignored by user`.
- **Tests:** link existing UT/E2E reports. Mark stale reports explicitly. Leave a missing report reference empty.
- **Acceptance:** for a ticket, one line per approved `Expected` result or equivalent outcome with `pass`, `fail`, or `unverified`, and a specific current test, other verification result, or evidence gap. A review finding can substantiate a failure. Passing unrelated tests and evidence from older snapshots leave the criterion unverified.
- **Review inputs:** SHA-256 of the confirmed review scope, requirements, and applicable review rules, using a stable order and length-delimited inputs. If any of these inputs cannot be identified reliably, start a fresh review instead of reusing findings.

## Severity

- Critical: data loss, security breach, corruption, blocking runtime failure.
- Warning: incorrect behavior, regression, missing requirement.
- Minor: low-risk maintainability or convention issue.

## Sections

- `Reference` in `<sub>`. `Tests` plain, under `Issue Count`: `Unit` and `E2E` lines referencing `[ut.md](ut.md)` and `[e2e.md](e2e.md)` when present, or left empty when absent.
- Findings by severity; preserve numbers for entries that remain in `TODO`. When an entry leaves `TODO`, remove its displayed number. Separate entries with `---`.
- Keep `TODO`, `RESOLVED`, `IGNORED`, `PRE-EXISTING`; `None.` when empty.
  - `TODO`: open, deferred, disputed. `RESOLVED`: applied fixes. `IGNORED`: needs the user's explicit choice. `PRE-EXISTING`: real bugs the change did not introduce or expose; not counted, not sent to `go-fix` unless the user asks.
- `Round`: 1 on a first full review, plus 1 per subsequent full review. `Tier`: the tier used for the latest pass.
- `Status: approved` records user approval only.
- `Reviewed from`: original baseline. `Reviewed to`: HEAD of the reviewed checkout. For `Coverage: incremental`, add `Compared from` with the prior reviewed SHA. For `Coverage: full`, the comparison starts at the original baseline.
- `Snapshot` and `Checkout clean`: reviewed checkout hash and whether the SHA alone represented it. Keep these fields and the comparison range even if focused fixes change the findings list.
