## Summary

Lock profile form submission while a save request is in flight and restore the Save button on failure.

```diff
 onSubmit()
+  if (this.isSaving) return
+  this.isSaving = true
   this.profileService.save(payload)
+    .pipe(finalize(() => this.isSaving = false))
     .subscribe(...)
```

## Evidence

- **Before:** Rapid double-click on Save fired two `PUT /api/v1/profile` requests; failed save left `isSaving = true`.
  **After:** `npx vitest run src/app/profile/profile-form.component.spec.ts` (3 specs, 0 failed) and `npx playwright test playwright/tests/profile-save.spec.ts` (1 spec, 0 failed).

## Merge Danger

**Door:** two-way

Client-only guard in `ProfileFormComponent`; revert restores previous submit handler with no schema or API change.

**Blast Radius:** component

Scoped to the profile form (`src/app/profile/`).
