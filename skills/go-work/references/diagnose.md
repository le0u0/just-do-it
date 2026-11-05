# Diagnose a Failure

Use for a failing test or bug report. Redact secrets in anything quoted.

## Steps

1. **Red loop first.** One command you ran that goes red on this exact failure. Try in order: failing test at the right seam, script against the running app, replay of captured input, bisect between known states. No loop: stop and say what you tried. Never theorize without one.
2. **Reproduce and minimize.** Confirm the symptom, then cut inputs and steps until each remaining piece is needed.
3. **Hypothesize.** 3 to 5 ranked, falsifiable guesses: "if X is the cause, changing Y fixes it." Show the user first when present.
4. **Probe.** One change per hypothesis. Prefer a debugger or targeted log, each log tagged uniquely, such as `[DEBUG-a4f2]`.
5. **Fix.** Turn the repro into a failing test at the seam where the bug occurs, watch it fail, fix, watch it pass. No right seam: report that as a finding.
6. **Clean up and record.** Re-run the loop, remove tagged logs and throwaway files. Return cause, rejected hypotheses, and evidence per [diagnose-format.md](diagnose-format.md).
