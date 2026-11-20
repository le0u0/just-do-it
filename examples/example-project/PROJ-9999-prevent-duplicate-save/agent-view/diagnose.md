# Diagnose: PROJ-9999 Duplicate profile save requests

## Conclusions

- Root cause: `onSubmit()` sets `isSaving = true` only inside `subscribe()` next callback instead of before `profileService.save()`.
- Affected path: `src/app/profile/profile-form.component.ts:42` to `src/app/profile/profile-form.component.html:18`.

## Rejected

- Double binding on `(click)` and `(ngSubmit)`: template binds `(ngSubmit)` only.

## Evidence

- <sub>fact: `profile-form.component.ts:42` calls `this.profileService.save()` before updating `this.isSaving`.</sub>
- <sub>fact: error callback logs error without resetting `this.isSaving = false`.</sub>

## Reference

<sub>Repository: /example/repo<br>Branch: PROJ-9999-prevent-duplicate-save<br>HEAD: a1b2c3d</sub>
