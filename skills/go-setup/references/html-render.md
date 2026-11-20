# HTML Render (`dev-view/*.html`)

Applies to human-readable HTML views in `~/.just-do-it/{project}/{branch}/dev-view/` (`research.html`, `plan.html`, `review.html`, `testing-guide.html`). Agents read the compact `.md` files in `agent-view/`; the developer reads the visual `.html` pages in `dev-view/` in a browser. (`dev-view/pr.md` and `dev-view/handoff.md` remain `.md`.)

## Core principles

1. **Single self-contained HTML file**: inline CSS and minimal vanilla JS, zero build step, works directly via `file://` or local HTTP preview.
2. **Low-token partial edits via multi-line `const DATA`**:
   - Place all page content inside a pretty-printed, multi-line `const DATA = { ... };` block at the top of `<script>` (or keep content in clean, multi-line semantic sections) so that later content updates only read and `edit_file` the changed lines (`StartLine`–`EndLine`) without reading or rewriting the CSS/JS shell.
   - For JSON embedded in a script element, serialize every `<` as `\u003c` so external text cannot close the script element. Escape untrusted text and validate URLs when rendering into HTML.
3. **Figure-first & scannable**: lead with the Goal, visual statechart/flow diagram, and inline attachment images before detail cards. Use short bullets and clear status badges—never walls of text.
4. **Inline attachment images**: reference downloaded ticket images with relative paths (`../agent-view/attachments/{ticket}/{filename}`). Render each image inside a `<figure>` card with filename caption and click-to-expand `<dialog>` lightbox.
5. **Statecharts & diagrams**: render statecharts (`stateDiagram-v2`) and flowcharts either as clean inline `<svg>` state nodes/arrows or via `<pre class="mermaid">`.

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
- **Layout**: max-width `1120px` centered container, `24px` padding, responsive 2-column sticky sidebar TOC + main content on desktop (`>860px`), single column on mobile, `@media print` hiding interactive controls.

## Page structures

### 1. `dev-view/research.html` (written by `go-research`)

- **Header**: Ticket key (linked to tracker URL), title, status badge, retrieved timestamp, and linked related tickets.
- **Visual Attachments Gallery**: grid of `<figure>` cards for every image in `../agent-view/attachments/{ticket}/` (plus a file list for non-image attachments and any missing/failed downloads).
- **Requirements & Acceptance Criteria**: grouped cards distinguishing confirmed requirements from comments/proposals.
- **Open Questions**: highlighted callout box for unresolved questions or unknown domain terms.
- **Code Pointers**: table or pill list of mapped entry points, source files, and test paths.

### 2. `dev-view/plan.html` (written by `go-plan`, reviewed by user for plan approval)

- **Header**: Ticket key & title, `Status: draft | approved` badge, and a prominent **Goal** card listing the functional bullet points that define when the task is done (never boilerplate like "tests pass").
- **Statechart & Invariants** (when the ticket has state transitions per [`statechart.md`](../../go-plan/references/statechart.md)):
  - Visual statechart diagram (`stateDiagram-v2` / SVG) showing states and user/system events.
  - Invariant & edge-case table (`State | Rule | Guarded transition / edge case`).
- **Implementation Steps**: numbered step cards showing `Do` bullets (what the step handles), `Reuse` (existing components/services confirmed with the user), `Test` seam & run status, `Commit` message, `Blocked by` badges, owned `Files`, and inline `<figure>` previews of any relevant attachment image from `../agent-view/attachments/{ticket}/`.
- **Testing, Decisions, Out of Scope & Deletions**: summary card of authorized unit/E2E specs, confirmed grill decisions, excluded scope, and approved file deletions.

### 3. `dev-view/review.html` (written by `go-review`, updated by `go-fix`)

- **Header**: Branch, baseline SHA → reviewed SHA, Tier badge (`Quick` / `Standard` / `Deep`), Round number, and open issue counts by severity (`Critical`, `Warning`, `Minor`).
- **Tests Bar**: pass/fail status badges summarized from `../agent-view/ut.md` and `../agent-view/e2e.md` (linking to `../agent-view/ut.md` and `../agent-view/e2e.md`, or marked `not run` when absent) so the developer sees immediately whether unit and E2E tests passed or failed.
- **Findings (`TODO`, `RESOLVED`, `IGNORED`, `PRE-EXISTING`)**:
  - Each `TODO` finding card displays its ID, severity badge, owning component/file, **Issue**, and **Fix**.
  - Interactive disposition selector (`Accept`, `Dispute`, `Ignore`) on each `TODO` card. Selecting `Dispute` reveals a textarea labelled `Reason` after the finding's reference, styled like the tester note in [html-page.md](../../to-test-doc/references/html-page.md). Include each disputed finding's text in the copyable `go-fix` request, preserving its ID and text. Retain entered text when switching selections. Provide a **"Copy `go-fix` command"** button.
