# Code review

Status: reviewed

Mock example. Findings and test results are fictional.

## Issue Count

TODO: 2 (Critical: 0, Warning: 2, Minor: 0)

## Manual review

1. `profile-form.component.ts:123`
   -> The button waits for a reply that never comes. Does it wake up again?
2. `profile-form.component.ts:145`
   -> The helper may hide the "sorry" note. Is it still shown?

## TODO

### 1. Warning — ProfileFormComponent

- **Issue:** A failed update leaves Save disabled. No retry.
- **Fix:** Clear pending state on error. Add retry spec.

---

### 2. Warning — ProfileFormComponent

- **Issue:** Changed error path hides the server's error message.
- **Fix:** Keep the existing error display on failure.

## RESOLVED

None.

## IGNORED

None.

## Tests

<sub>Unit: mock pass, not run<br>E2E: not run</sub>

## Reference

<sub>Repository: /example/repo<br>Branch: PROJ-9999-prevent-duplicate-save<br>Reviewed from: a1b2c3d<br>Reviewed to: a1b2c3d</sub>
