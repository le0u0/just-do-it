# HTML Render (`dev-view/*.html`)

Applies to all five human-readable HTML views in `~/.just-do-it/{project}/{branch}/dev-view/` (`spec.html`, `plan.html`, `plan-review.html`, `review.html`, `testing-guide.html`). Agents read compact `.md` files in `agent-view/`; the developer reads visual `.html` pages in `dev-view/` in a browser. (`dev-view/pr.md` and `dev-view/handoff.md` remain `.md`, and `dev-view/testing-guide.md` remains `.md` when requested.)

## 1. Visual Style

Use one shared warm-neutral palette and type scale across every `dev-view/*.html` file:

```css
:root {
  --bg: #faf7f2;
  --surface: #ffffff;
  --surface-alt: #f6efe3;
  --text: #2b2622;
  --muted: #6b625a;
  --border: #ddd3c6;
  --accent: #faaa6c;
  --accent-d: #e8924f;
  --pass: #1f7a3d;
  --pass-bg: #e3f4e8;
  --warn: #b25e09;
  --warn-bg: #fef3e2;
  --fail: #b3261e;
  --fail-bg: #fbe5e3;
}
```

- **Typography**: `16px/1.55 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang TC", "Noto Sans TC", sans-serif`; `h1` `28px` (`line-height: 1.25`), `h2` `20px–22px`, `h3` `16px` semibold; code in `ui-monospace, SFMono-Regular, Menlo, monospace` (`13px`).
- **Layout**:
  - `spec.html`, `plan.html`, `plan-review.html`, `review.html`: centered `.wrap` container (`max-width: 1040px–1080px`, `padding: 28px 20px 64px`), single column on mobile.
  - `testing-guide.html`: 2-column layout (`260px` sticky left `<nav>` + scrollable `<main>`) per [html-page.md](../../to-test-doc/references/html-page.md).
- **Badges & severity**:
  - `.badge.pass` (`--pass-bg` / `--pass`), `.badge.warn` (`--warn-bg` / `--warn`), `.badge.fail` (`--fail-bg` / `--fail`).
  - Review finding cards use left accent border by severity: `.sev-critical` (`--fail`), `.sev-major` (`--warn`), `.sev-minor` (`--accent-d`), `.sev-nit` (`--border`).
- **Motion**: wrap transitions in `@media (prefers-reduced-motion: reduce) { ... { transition: none; } }`.

## 2. HTML Tags & Serialization

- **Single self-contained HTML file**: inline `<style>` and minimal vanilla `<script>`, zero build step, works directly via `file://` or local HTTP preview.
- **Static semantic HTML vs `const DATA`**:
  - `spec.html`, `plan.html`, `plan-review.html`, and `review.html` use clean, multi-line semantic HTML (`<header>`, `<main>`, `<section>`, `<article class="card">`, `<figure>`, `<dialog>`) with no client-side `DATA` renderer.
  - `testing-guide.html` is the only report that uses a multi-line pretty-printed `const DATA = { ... };` block (serializing `<` as `\u003c`).
  - Escape untrusted text and validate URLs (`https?://` or safe relative paths; never `javascript:`) when rendering HTML.
- **Source `.md` hyperlink**: include a relative link in the header `.meta` row to the corresponding Markdown source file when present:
  - `spec.html` → `../agent-view/spec.md`
  - `plan.html` → `../agent-view/plan.md`
  - `plan-review.html` → `../agent-view/plan-review.md` (and `../agent-view/plan.md` if present)
  - `review.html` → `../agent-view/review.md`
  - `testing-guide.html` → `testing-guide.md` (only when `dev-view/testing-guide.md` is generated; omit otherwise)
- **Tooltips (`<span title="...">`)**: show short file or command labels (e.g., `<span title="src/app/profile/profile-form.component.spec.ts">ProfileForm Unit Test</span>`) so `title` acts as the no-JS browser fallback and JS upgrades it to a keyboard-accessible tooltip.
- **Statecharts & diagrams**: render `stateDiagram-v2` and flowcharts as clean inline `<svg>` state nodes/arrows or `<pre class="mermaid">`.
- **Inline attachment images**: reference downloaded ticket images with relative paths (`../agent-view/attachments/{ticket}/{filename}`) inside `<figure>` cards with `<figcaption>` and a click-to-expand `<dialog id="attachment-preview">`.

## 3. Report Structures & Regeneration Rules

Re-rendering any `dev-view/*.html` updates that file in place. If generation or verification fails, keep the previous usable HTML file intact.

### 3.1 `dev-view/spec.html` (`to-spec`)
- **Header**: Ticket key (linked to tracker URL when `https?://`), title, status badge (`ready` / `awaiting confirmation` / `blocked`), retrieved timestamp, related tickets, and `<a href="../agent-view/spec.md">spec.md</a>`.
- **Visual Attachments Gallery**: grid of `<figure>` cards for every image in `../agent-view/attachments/{ticket}/` (plus a file list for non-image attachments and any missing/failed downloads).
- **Requirements & Acceptance Criteria**: grouped cards distinguishing confirmed requirements from comments/proposals.
- **Open Questions**: highlighted callout box for unresolved questions or unknown domain terms.
- **Code Pointers**: table or pill list of mapped entry points, source files, and test paths.

### 3.2 `dev-view/plan.html` (`to-plan`)
- **Header**: Ticket key & title, `Status: draft | approved` badge (matching `approval.json` via [approval.py](../../to-plan/references/approval.py)), `<a href="../agent-view/plan.md">plan.md</a>`, and an ordered **Goal** list (bold scenario titles; optional `.goal-expected` in `--pass` and `.goal-actual` in `--fail`, regular weight).
- **Statechart & Invariants** (when stateful per [statechart.md](../../to-plan/references/statechart.md)): visual statechart diagram + invariant/edge-case table (`State | Rule | Guarded transition / edge case`).
- **Implementation Pipelines & Steps**: visible pipeline assignment, order, dependencies, and precedent links; one stable `id="step-N"` anchor per in-scope step with `Do`, `Reuse`, `Test`, `Commit`, `Blocked by`, `Files` tooltips, and relevant attachment thumbnails.
- **Testing, Decisions, Out of Scope & Deletions**: summary card of authorized unit/E2E specs, confirmed grill decisions, excluded scope, and approved file deletions.
- **Regeneration**: preserve `id="step-N"` anchors and approved scope.

### 3.3 `dev-view/plan-review.html` (`go-review plan`)
- **Header**: Draft identity, coverage/snapshot, `<a href="../agent-view/plan-review.md">plan-review.md</a>`, and `<a href="../agent-view/plan.md">Reviewed plan</a>` (when present).
- **Findings**: numbered findings with severity, affected decision, evidence, impact, proposed change, and disposition label when available. Keep plan findings separate from code-test badges, `go-fix` commands, and code review reports.

### 3.4 `dev-view/review.html` (`go-review code`, `go-fix`)
- **Header**: Branch, `Coverage: full | incremental`, start SHA → reviewed SHA, tier (`Standard | Deep`), round, open issue counts by severity, checkout drift warning when dirty/mismatched, and `<a href="../agent-view/review.md">review.md</a>`.
- **Tests Bar**: show `agent-view/ut.md` and `agent-view/e2e.md` with `pass` / `fail` / `stale` / `not run`. Link `../agent-view/ut.md` or `../agent-view/e2e.md` only when present and not `not run`; omit `<a>` when `not run`.
- **Acceptance**: for ticket reviews, show each approved `Expected` result with its status and supporting evidence or gap.
- **Findings (`TODO`, `RESOLVED`, `IGNORED`, `PRE-EXISTING`)**:
  - Number only `TODO` cards (`data-id="1"`). Omit finding numbers in `RESOLVED`, `IGNORED`, and `PRE-EXISTING` while keeping severity and owner.
  - Each `TODO` card shows ID, severity, owner, short **How to verify** steps, green **Expected** (`.result-expected`), red **Actual** (`.result-actual`, qualifying inferred/unconfirmed results), **Fix**, and interactive disposition controls (`Accept (Fix)` / `Dispute` / `Ignore`).
  - `go-fix` and re-renders preserve findings and existing dispositions; resolved items move to `RESOLVED` without a number.

## 4. Interaction Behavior Snippets

### 4.1 Attachment Lightbox (`spec.html`, `plan.html`)

Open image fitted to viewport (`is-zoomed`), click image to toggle intrinsic size capped at `50vw` / `50dvh`, close on backdrop click or `Escape`, and return focus to opener:

```html
<dialog id="attachment-preview" class="attachment-preview" aria-label="Attachment preview">
  <button type="button" class="attachment-zoom" aria-label="Zoom out"></button>
</dialog>
```

```css
.attachment-trigger,.attachment-zoom{display:block;padding:0;border:0;background:transparent}
.attachment-trigger{width:100%;cursor:pointer}
.attachment-preview{padding:0;border:0;max-width:calc(100vw - 24px);max-height:calc(100dvh - 24px);overflow:visible;background:transparent}
.attachment-preview::backdrop{background:rgba(43,38,34,.55)}
.attachment-zoom{cursor:zoom-in}
.attachment-preview img{display:block;max-width:50vw;max-height:50dvh;border-radius:8px}
.attachment-preview.is-zoomed .attachment-zoom{cursor:zoom-out}
.attachment-preview.is-zoomed img{width:min(calc(100vw - 24px),calc((100dvh - 24px) * var(--image-ratio,1)));height:auto;max-width:none;max-height:none}
```

```js
const dlg = document.getElementById("attachment-preview");
if (dlg) {
  const img = new Image(), zoom = dlg.querySelector(".attachment-zoom");
  let opener, onBackdrop = false;
  const setZoom = z => { dlg.classList.toggle("is-zoomed", z); zoom.setAttribute("aria-label", z ? "Zoom out" : "Zoom in"); };
  const setRatio = i => { if (i.naturalHeight) dlg.style.setProperty("--image-ratio", i.naturalWidth / i.naturalHeight); };
  img.addEventListener("load", () => setRatio(img));
  document.querySelectorAll("[data-attachment-preview]").forEach(btn => btn.addEventListener("click", () => {
    const src = btn.querySelector("img"); opener = btn; img.src = src.currentSrc || src.src; img.alt = src.alt;
    zoom.append(img); dlg.style.removeProperty("--image-ratio"); setRatio(src); setZoom(true); dlg.showModal();
  }));
  zoom.addEventListener("click", () => setZoom(!dlg.classList.contains("is-zoomed")));
  dlg.addEventListener("pointerdown", e => { onBackdrop = e.target === dlg; });
  dlg.addEventListener("click", e => { if (onBackdrop && e.target === dlg) dlg.close(); });
  dlg.addEventListener("close", () => opener?.focus());
}
```

### 4.2 Path & Command Tooltips (`plan.html`, `review.html`)

```css
[title],.path-tooltip-trigger{cursor:help}
span[title],.path-tooltip-trigger{text-decoration:underline dotted;text-underline-offset:.16em}
.path-tooltip-trigger{position:relative;display:inline-block;max-width:100%;overflow-wrap:anywhere}
.path-tooltip{position:absolute;top:100%;left:0;z-index:5;width:max-content;max-width:min(32rem,calc(100vw - 40px));background:var(--text);color:var(--surface);padding:6px 9px;border-radius:6px;box-shadow:0 2px 8px rgba(0,0,0,.18);font:.8rem/1.4 ui-monospace,monospace;overflow-wrap:anywhere;visibility:hidden;opacity:0;pointer-events:none;transition:opacity .1s ease}
.path-tooltip.above{top:auto;bottom:100%}
.path-tooltip-trigger:not(.tooltip-dismissed):is(:hover,:focus)>.path-tooltip{visibility:visible;opacity:1;pointer-events:auto}
@media(prefers-reduced-motion:reduce){.path-tooltip{transition:none}}
```

```js
document.querySelectorAll("span[title]").forEach((t, i) => {
  const tip = document.createElement("span");
  tip.id = "path-tooltip-" + i; tip.className = "path-tooltip"; tip.setAttribute("role", "tooltip"); tip.textContent = t.title;
  t.classList.add("path-tooltip-trigger"); t.tabIndex = 0; t.setAttribute("aria-describedby", tip.id);
  t.append(tip); t.removeAttribute("title");
  const show = () => {
    t.classList.remove("tooltip-dismissed");
    const {left, top, bottom} = t.getBoundingClientRect();
    const maxL = document.documentElement.clientWidth - tip.offsetWidth - 12;
    tip.style.left = Math.max(12, Math.min(left, maxL)) - left + "px";
    tip.classList.toggle("above", bottom + tip.offsetHeight > innerHeight && top > innerHeight - bottom);
  };
  t.addEventListener("pointerenter", show); t.addEventListener("focus", show);
});
document.addEventListener("keydown", e => {
  if (e.key === "Escape") document.querySelectorAll(".path-tooltip-trigger:is(:hover,:focus)").forEach(t => t.classList.add("tooltip-dismissed"));
});
```

### 4.3 Review Dispositions & Copy `go-fix` Command (`review.html`)

Each `TODO` card `.card[data-id]` includes `.seg` buttons (`data-action="fix|dispute|ignore"`, `aria-pressed`) and a `Reason` `<label hidden><textarea data-dispute></textarea></label>` revealed only for `dispute` (retaining entered text across switches). Clipboard failures on `file://` show inline feedback instead of failing silently:

```js
const cards = [...document.querySelectorAll(".card[data-id]")];
const disp = Object.fromEntries(cards.map(c => [c.dataset.id, "fix"]));
const preview = document.getElementById("cmd-preview"), copyBtn = document.getElementById("copy-btn");
function updateCmd() {
  if (!preview) return;
  const b = { fix: [], dispute: [], ignore: [] };
  Object.entries(disp).forEach(([id, act]) => b[act].push(id));
  const parts = [];
  if (b.fix.length) parts.push("fix findings " + b.fix.join(", "));
  b.dispute.forEach(id => {
    const c = cards.find(x => x.dataset.id === id);
    const reason = c.querySelector("textarea[data-dispute]").value.trim();
    const finding = c.querySelector(".result-actual").textContent.trim();
    parts.push("dispute " + id + " (" + finding + ")" + (reason ? ": " + reason : ""));
  });
  if (b.ignore.length) parts.push("ignore " + b.ignore.join(", "));
  preview.textContent = "/go-fix " + (parts.join("; ") || "set status to approved");
}
cards.forEach(c => {
  c.addEventListener("click", e => {
    const btn = e.target.closest("button[data-action]");
    if (!btn) return;
    disp[c.dataset.id] = btn.dataset.action;
    c.querySelector("label").hidden = btn.dataset.action !== "dispute";
    c.querySelectorAll("button[data-action]").forEach(x => x.setAttribute("aria-pressed", String(x === btn)));
    updateCmd();
  });
  c.querySelector("textarea[data-dispute]")?.addEventListener("input", updateCmd);
});
updateCmd();
copyBtn?.addEventListener("click", async () => {
  try { await navigator.clipboard.writeText(preview.textContent); copyBtn.textContent = "Copied!"; }
  catch { copyBtn.textContent = "Copy failed — select command below"; }
  setTimeout(() => copyBtn.textContent = "Copy go-fix command", 2000);
});
```
