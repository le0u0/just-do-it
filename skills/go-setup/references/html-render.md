# HTML Render (`dev-view/*.html`)

Applies to human-readable HTML views in `~/.just-do-it/{project}/{branch}/dev-view/` (`spec.html`, `plan.html`, `review.html`, `testing-guide.html`). Agents read the compact `.md` files in `agent-view/`; the developer reads the visual `.html` pages in `dev-view/` in a browser. (`dev-view/pr.md` and `dev-view/handoff.md` remain `.md`.)

## Core principles

1. **Single self-contained HTML file**: inline CSS and minimal vanilla JS, zero build step, works directly via `file://` or local HTTP preview.
2. **Low-token partial edits via multi-line `const DATA`**:
   - Place all page content inside a pretty-printed, multi-line `const DATA = { ... };` block at the top of `<script>` (or keep content in clean, multi-line semantic sections) so that later content updates only read and `edit_file` the changed lines (`StartLine`–`EndLine`) without reading or rewriting the CSS/JS shell.
   - For JSON embedded in a script element, serialize every `<` as `\u003c` so external text cannot close the script element. Escape untrusted text and validate URLs when rendering into HTML.
3. **Figure-first & scannable**: lead with the Goal, visual statechart/flow diagram, and inline attachment images before detail cards. Use short bullets and clear status badges—never walls of text.
4. **Inline attachment images**: reference downloaded ticket images with relative paths (`../agent-view/attachments/{ticket}/{filename}`). Render each image inside a `<figure>` card with filename caption and click-to-expand `<dialog>` lightbox.
5. **Statecharts & diagrams**: render statecharts (`stateDiagram-v2`) and flowcharts either as clean inline `<svg>` state nodes/arrows or via `<pre class="mermaid">`.

## Plan and review templates

Use the matching bundled example: [plan.html](../../../examples/example-project/PROJ-9999-prevent-duplicate-save/dev-view/plan.html) or [review.html](../../../examples/example-project/PROJ-9999-prevent-duplicate-save/dev-view/review.html). Copy its shell, CSS, and script verbatim. Replace the title and report content from the corresponding Markdown. Repeat cards or rows as needed and omit inapplicable sections. When updating a report with another layout, render it from the template.

Show a short file label such as `ProfileForm Unit Test` and put the exact path and optional line in its escaped `title` attribute: `<span title="src/app/profile/profile-form.component.spec.ts">ProfileForm Unit Test</span>`. Preserve this markup from the Markdown. Both templates use it to show an immediate tooltip on hover or keyboard focus, with `cursor: help` and Escape dismissal. The `title` supplies the browser fallback when JavaScript is unavailable. If a command contains file paths, show a short command label with the full command in its tooltip.

Before saving, compare the CSS and script against the template. Verify file labels, result order and colors, and that the content matches the Markdown.

## Design tokens & base CSS

Use a consistent, restrained warm-neutral theme across all `dev-view/*.html` files:

```css
:root {
  --bg: #faf7f2;
  --surface: #ffffff;
  --surface-alt: #f6efe3;
  --text: #2b2622;
  --muted: #6b625a;
  --border: #ddd3c6;
  --accent: #faaa6c;
  --pass: #1f7a3d;
  --pass-bg: #e3f4e8;
  --warn: #b25e09;
  --warn-bg: #fef3e2;
  --fail: #b3261e;
  --fail-bg: #fbe5e3;
}
```

- **Typography**: `16px/1.55 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang TC", "Noto Sans TC", sans-serif`; headings `28px` (h1), `22px` (h2), `16px` (h3 semibold); code in `ui-monospace, SFMono-Regular, Menlo, monospace`.
- **Layout**: use the bundled shell for plan and review. Other pages use a centered container and a single column on mobile.

## Page structures

### 1. `dev-view/spec.html` (written by `to-spec`)

- **Header**: Ticket key (linked to tracker URL), title, status badge, retrieved timestamp, and linked related tickets.
- **Visual Attachments Gallery**: grid of `<figure>` cards for every image in `../agent-view/attachments/{ticket}/` (plus a file list for non-image attachments and any missing/failed downloads).
- **Attachment preview**: copy the thumbnail buttons, dialog, CSS, and script from the [bundled spec example](../../../examples/example-project/PROJ-9999-prevent-duplicate-save/dev-view/spec.html). It uses the same image-click zoom and backdrop dismissal as the plan.
- **Requirements & Acceptance Criteria**: grouped cards distinguishing confirmed requirements from comments/proposals.
- **Open Questions**: highlighted callout box for unresolved questions or unknown domain terms.
- **Code Pointers**: table or pill list of mapped entry points, source files, and test paths.

### 2. `dev-view/plan.html` (written by `go-plan`, reviewed by user for plan approval)

- **Header**: Ticket key & title, `Status: draft | approved` badge, and an ordered **Goal** list. Bold only each scenario title. Show `Expected:` in green, then `Actual:` in red, both in regular weight.
- **Statechart & Invariants** (when the ticket has state transitions per [`statechart.md`](../../go-plan/references/statechart.md)):
  - Visual statechart diagram (`stateDiagram-v2` / SVG) showing states and user/system events.
  - Invariant & edge-case table (`State | Rule | Guarded transition / edge case`).
- **Implementation Steps**: numbered step cards with `Do`, `Reuse`, `Test`, `Commit`, `Blocked by`, and `Files` as labeled tooltips. Show relevant attachment previews with short captions.
- **Attachment preview**: use the template's thumbnails with a pointer cursor and one shared dialog. Open with the image fitted to the viewport. Clicking the image switches between that expanded view and intrinsic size capped at half the viewport, with matching zoom-out and zoom-in cursors. Keep a backdrop strip around the expanded image for dismissal. Backdrop click or Escape closes the dialog and returns focus to the thumbnail.
- **Testing, Decisions, Out of Scope & Deletions**: summary card of authorized unit/E2E specs, confirmed grill decisions, excluded scope, and approved file deletions.

### 3. `dev-view/review.html` (written by `go-review`, updated by `go-fix`)

- **Header**: Branch, full or incremental coverage, comparison start SHA → reviewed SHA, tier, full review round, and open issue counts by severity. Mark when the checkout differs from the reviewed snapshot.
- **Tests Bar**: link UT/E2E reports with pass/fail for evidence matching the review snapshot, `stale` for mismatches, and `not run` when absent.
- **Acceptance**: for ticket reviews, show each approved `Expected` result with its status and supporting evidence or gap.
- **Findings (`TODO`, `RESOLVED`, `IGNORED`, `PRE-EXISTING`)**:
  - Each `TODO` card shows its ID, severity, owner, short **How to verify** steps, green **Expected**, red **Actual**, and **Fix**. Qualify inferred or unconfirmed results in **Actual**. Use the same order for other findings with verification details.
  - Show severity and owner without a finding number in `RESOLVED`, `IGNORED`, and `PRE-EXISTING`.
  - Interactive disposition selector (`Accept`, `Dispute`, `Ignore`) on each `TODO` card. Selecting `Dispute` reveals a textarea labelled `Reason` after the finding's reference, styled like the tester note in [html-page.md](../../to-test-doc/references/html-page.md). Include each disputed finding's text in the copyable `go-fix` request, preserving its ID and text. Retain entered text when switching selections. Provide a **"Copy `go-fix` command"** button.
