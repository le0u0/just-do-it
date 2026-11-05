# Evals

Behavioral cases for the skills: file changes and executed commands, not just frontmatter and links.

## Run

1. Prepare disposable fixtures outside any real checkout. It creates git repos with a synthetic test runner and installs nothing.

   ```bash
   python3 evals/fixture.py prepare /private/tmp/just-do-it-evals-UNIQUE
   ```

2. For each case in `cases.json`, give a fresh agent only:
   - the skill path (from `skills/`, not an installed cache),
   - the generated `request.txt`,
   - the `repo` directory.

   Withhold `checks`, `before.json` and the fixture script. It saves its final answer as `response.md` beside `repo`.

3. Check files and commands:

   ```bash
   python3 evals/fixture.py check /private/tmp/just-do-it-evals-UNIQUE
   ```

4. Read traces and responses against each case's `checks`. For manager cases, confirm each handoff and that agents start no extra subagents.

5. Repeat without the skill as a baseline. A case that passes both ways may be redundant: shorten it unless it guards safety, approval, or scope.

Run a subset with `--case CASE_ID` (repeatable) on `prepare` and `check`.

## Limits

- The runner is synthetic.
- It logs arguments and file hashes at each call, so it catches config or spec edits used to narrow a run.
- It cannot validate real tests, browsers, or ticket tools.
- A failing focused command must stay a reported failure.
