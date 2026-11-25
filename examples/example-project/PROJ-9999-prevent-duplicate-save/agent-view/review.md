# Code review

Status: reviewed

## Issue Count

TODO: 2 (Critical: 0, Warning: 2, Minor: 0)

## Tests

- Unit: [ut.md](ut.md)
- E2E: [e2e.md](e2e.md)

## Acceptance

- Expected 1 · Save starts one request and shows Saving… · unverified · sample result unavailable
- Expected 2 · Repeated clicks send one request · unverified · sample result unavailable
- Expected 3 · Successful save closes Edit Profile · unverified · sample result unavailable
- Expected 4 · Save accepts a retry after an error · unverified · retry action untested

## TODO

### 1. Warning — <span title="src/app/profile/profile-form.component.ts">ProfileFormComponent</span>

- **How to verify:**
  1. In <span title="src/app/profile/profile-form.component.spec.ts">ProfileForm Unit Test</span>, make validation throw before the save request starts.
  2. Submit the form and check the Save button after the error.
- **Expected:** Save is enabled so the user can retry.
- **Actual:** Unverified: Thrown synchronous validation error in `onSubmit()` leaves `isSaving` true and Save disabled.
- **Fix:** Move `isSaving = true` after synchronous form validation or wrap in `try / finally`.

---

### 2. Warning — <span title="src/app/profile/profile-form.component.ts">ProfileFormComponent</span>

- **How to verify:**
  1. Open Edit Profile. Mock the save request to return HTTP 500 with the message “Profile update rejected.”
  2. Click Save and read the error banner.
- **Expected:** The banner shows “Profile update rejected.”
- **Actual:** Unverified: Changed error handler overwrites server `err.error.message` with generic fallback text.
- **Fix:** Preserve `err.error?.message ?? defaultError` display on failure.

## RESOLVED

None.

## IGNORED

None.

## PRE-EXISTING

None.

## Reference

<sub>Repository: /example/repo<br>Branch: PROJ-9999-prevent-duplicate-save<br>Reviewed from: a1b2c3d<br>Reviewed to: e4f5g6h<br>Coverage: full<br>Tier: Standard<br>Round: 1<br>Last TODO number: 2</sub>
