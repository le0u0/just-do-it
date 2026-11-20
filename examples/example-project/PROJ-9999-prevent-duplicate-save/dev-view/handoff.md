# Handoff: Backend idempotency for `PUT /api/v1/profile`

- **Target team:** Backend (`profile-service`)
- **Context:** Frontend added a client-side `isSaving` lock in `ProfileFormComponent` (`PROJ-9999`), but concurrent requests from multi-tab sessions can still race on `PUT /api/v1/profile`.

## Observed vs Expected

- **Endpoint:** `PUT /api/v1/profile`
- **Observed:** Two concurrent `PUT` payloads with identical display name updates create duplicate audit rows (`HTTP 200` on both).
- **Expected:** Accept an `If-Match` / `version` field or deduplicate identical concurrent updates within the same profile version (`HTTP 409 Conflict` on stale version).

## Proposed Contract

```json
{
  "accountId": "REDACTED_ID",
  "version": 4,
  "profile": {
    "displayName": "Example User"
  }
}
```

## Open Questions

- Should stale-version conflicts return the latest `profile` snapshot in the `409` body?
