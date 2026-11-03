# UI Exploration

Explore the flow before writing any spec. A spec written from source alone guesses locators, waits, and data, and fails on its first real run. Exploring opens the page and walks the flow; it never runs a spec.

- Find the app URL before opening anything: the project's documented base URL, else the dev servers already listening (`lsof -iTCP -sTCP:LISTEN -P -n`, keep ports 3000-3999, 4200, 5000-5999, 8000-8999). One result: use it. Several: ask which. None: report it; never start a server unasked.
- Use the browser tool the project names, named in the project docs, never one that would add a dependency to the project. When the project names none but its own Playwright is installed, drive that with a throwaway script in the scratchpad or system temp directory, never in the repository. A host-installed `playwright-skill` may serve the same exploration; it installs into its own folder, never the project's.
- Explore with a visible browser unless the environment has no display. Put the URL in one constant, and screenshots and scripts outside the repository. Open the base URL with the project's auth state and the seeded data the spec will use. When the tool cannot load the auth state or reach the page, report it.
- Walk the whole flow the spec covers, at the viewport sizes the requirement names. Use credentials the project documents; never invent or print one. Inspect targeted elements and attributes; take screenshots only for visual evidence. Send snapshots to files and read only the lines you need.
- Keep only the stable locators, the step order, loading and empty states, and the data the flow needs. Keep snapshots out of your notes and report.
- When seeded data is missing, report it; a reset needs the user's explicit request.
- Return behavior, generated interaction code, and stable locators. Generated code is authoring input, not compatibility proof. Change files only when asked.
