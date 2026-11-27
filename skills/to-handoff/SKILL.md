---
name: to-handoff
description: 'Prepare a concise team handoff for an issue, requirement, or cross-team ask (backend, frontend, DevOps, etc.) and save dev-view/handoff.md.'
---

# Handoff

Prepare a short, readable report that the target team (backend, frontend, DevOps, etc.) can act on, and save it to `~/.just-do-it/{project}/{branch}/dev-view/handoff.md`. Match the user's language and use only supplied or verified evidence.

## Storage

- Resolve `~/.just-do-it/{project}/{branch}/` per [go-setup](../go-setup/SKILL.md) and [storage.md](../go-setup/references/storage.md). If no existing project and branch artifacts explicitly identify this repository and exact branch, run `go-setup` first to confirm `{project}` with the user.
- Read `agent-view/spec.md`, `agent-view/plan.md`, and `public/glossary.md` when present.

## Steps

1. Identify the requested action. For an API or service issue, capture the known method, endpoint, environment, status, decisive response, relevant request fields, observed behavior, and expected behavior. For a requirement or infra/UI ask, capture the goal, required behavior, relevant API/data/config contract, acceptance criteria, and open questions.
   For a requirement involving existing code, inspect the named repository and nearby models, usages and comparable behavior before drafting. Trace relevant types and dependencies so the handoff includes the contract and supporting changes needed. Cite evidence in the reply when useful; distinguish confirmed conventions from proposed behavior. If the repository or decisive evidence is unavailable, say so and ask for only the missing decisions.
2. Separate observations, expectations and hypotheses. Do not invent reproduction steps, root causes, contracts or validation results. Mark material unknowns briefly; ask only when missing information blocks a useful report.
3. Follow [report-format.md](references/report-format.md) for the requested report type. Use impeccable's restrained Read-mode principles: clear hierarchy, legibility and purposeful spacing.
4. Include the captured request payload, logs, or response when available. For long payloads, use a clearly labelled excerpt of relevant fields. Redact personal, credential and other sensitive values by default, marking redactions. Do not claim a redacted or abbreviated payload reproduces the issue without verification.
5. Save the Markdown report to `~/.just-do-it/{project}/{branch}/dev-view/handoff.md` (or print in the terminal only when explicitly requested) and report the saved path. Do not send the report to anyone unless explicitly requested.

## HAR input

Accept pasted HAR JSON or a user-supplied `.har` path. Select the request matching the issue and extract its method, URL, status, timestamp, request body, response body and any request, correlation or trace ID when present. A localhost proxy address does not establish the target service address; inspect available proxy configuration when relevant, and mark the target environment unknown if it cannot be established. If several requests could match, ask which one. Identify missing bodies rather than assuming they were captured. Do not replay requests. HAR files can contain sensitive data even when sanitized; apply the redaction rule above.

## Done when

The handoff request, relevant evidence and unknowns are clear; `dev-view/handoff.md` is written and its path is reported (or printed when requested).
