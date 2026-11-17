---
name: ask-be
description: 'Prepare a concise backend handoff for an API issue or backend requirement.'
---

# Ask Backend

Prepare a short, readable report that a backend engineer can act on. Match the user's language and use only supplied or verified evidence.

## Steps

1. Identify the backend action. For an API issue, capture the known method, endpoint, environment, status, decisive response, relevant request fields, observed behavior and expected behavior. For a requirement, capture the goal, required behavior, relevant API or data contract, acceptance criteria and open questions as applicable.
   For a requirement involving existing code, inspect the named repository and nearby models, usages and comparable behavior before drafting. Trace relevant types and dependencies so the handoff includes the contract and supporting changes needed. Cite evidence in the reply when useful; distinguish confirmed conventions from proposed behavior. If the repository or decisive evidence is unavailable, say so and ask for only the missing decisions.
2. Separate observations, expectations and hypotheses. Never invent reproduction steps, backend causes, contracts or validation results. Mark material unknowns briefly; ask only when missing information blocks a useful report.
3. Follow [report-format.md](references/report-format.md) for the requested report type. Use impeccable's restrained Read-mode principles: clear hierarchy, legibility and purposeful spacing.
4. Include the captured request payload and response in API issue reports when available. For long payloads, use a clearly labelled excerpt of relevant fields. Redact personal, clinical, credential and other sensitive values by default, marking redactions. Never claim a redacted or abbreviated payload reproduces the issue without verification.
5. Deliver per Output. Do not send the report to anyone unless explicitly requested.

## Output

- Default: return the complete Markdown report in the reply. Do not create a file.
- In `justaway` manager mode: save `backend-{short-description}.md` in the branch folder, updating it in place. A user-supplied task directory wins. Resolve the branch folder and apply the shared [storage rules](../justaway/references/storage.md); on a blocked save, return the report and blocked path.
- If the user explicitly requests a Markdown file, follow their requested location. If no location is provided, ask where to save it outside manager mode; in manager mode use the branch folder.

## HAR input

Accept pasted HAR JSON or a user-supplied `.har` path. Select the request matching the issue and extract its method, URL, status, timestamp, request body, response body and any request, correlation or trace ID when present. A localhost proxy address does not establish the backend address; inspect available proxy configuration when relevant, and mark the backend environment unknown if it cannot be established. If several requests could match, ask which one. Identify missing bodies rather than assuming they were captured. Do not replay requests. HAR files can contain sensitive data even when sanitized; apply the redaction rule above.

## Done when

The backend request, relevant evidence and unknowns are clear; the requested output is returned or its blocked save is reported.
