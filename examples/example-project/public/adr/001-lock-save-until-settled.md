# ADR 001: Lock Save button in client state until request settles

- **Context:** Rapid double-clicks on the profile form Save button trigger duplicate `PUT /api/v1/profile` calls before the first response returns.
- **Decision:** Gate `onSubmit()` and button `disabled` state on `isSaving`, resetting `isSaving = false` in `finalize()` across both success and error paths.
- **Why:** Immediate UI feedback prevents duplicate network writes without waiting for backend idempotency changes.
