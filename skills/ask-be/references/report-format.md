# Backend report format

Use the Slack format by default. Use plain format when requested. Preserve exact technical evidence; mark material unknowns without inventing details.

## Slack format

Return the formatted report directly for one-step copying. Use a bold opening, visible dividers, bold section labels and one paragraph per request detail. Keep request details as plain text. Put response before payload in JSON code blocks. Omit sections that do not apply; include the actual evidence, not placeholders. Avoid Markdown soft line breaks and extra leading spaces.

For an API issue:

````markdown
**[What happened]. Could you please help take a look? Thanks!**

━━━━━━━━━━━━━━━━━━━━

**REQUEST**

API: [method and path]

Backend: [verified address or environment]

Time: [timestamp and timezone]

Request ID: [if captured]

━━━━━━━━━━━━━━━━━━━━

**RESPONSE**

```json
[response]
```

━━━━━━━━━━━━━━━━━━━━

**PAYLOAD**

```json
[payload]
```
````

For a backend requirement, use the same opening and divider style. Replace API sections with **REQUIREMENT** and, when helpful, **EXAMPLE** or **OPEN QUESTIONS**. Include the relevant contract and supporting changes; do not invent permission values or defaults.

## Plain format

Use concise prose and ordinary Markdown headings and code blocks, without dividers or decorative styling. For an API issue, state the problem and request details, then response and payload. For a backend requirement, state the requested behavior, relevant contract, and material open questions. Adapt sections to the evidence; omit unavailable optional details.

## Evidence

Include the complete response body when available and concise. Include relevant payload fields as JSON; for a long payload, label it as an excerpt and do not claim it reproduces the issue. Mark sensitive-value redactions. Identify a localhost frontend proxy separately from the backend address. Do not prescribe investigation steps unless requested or supported by evidence.
