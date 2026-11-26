# Plan approval

The user approves the specific plan and authored checklist scope after any required plan review. Record that approval in `agent-view/approval.json` before work. An approved status in Markdown is presentation metadata. A request to implement the current exact plan can supply approval in the same turn. An earlier approval of changed artifacts, or an old approved status without a matching record, requires renewal before work.

## Scope identity

Use [approval.py](approval.py) with Python 3.9+ to fingerprint the task before showing the plan and checklist for approval. Pass the absolute task folder containing `agent-view/`, the canonical repository root and the exact ticket branch; workers use the original ticket identity and task storage. Run:

```text
python3 <approval.py> fingerprint <task> <repository> <branch>
python3 <approval.py> record <task> <repository> <branch> --expected <presented-fingerprint>
python3 <approval.py> verify <task> <repository> <branch> [--expected <assigned-fingerprint>]
```

Record only after explicit user approval of the presented scope. Show approval in plan Markdown and HTML only after `record` succeeds. If Python or the inputs are unavailable, report the verification blocker before starting planned work.

The fingerprint includes repository, branch and task identity, exact spec bytes (or absence), plan content with only its status metadata normalized, and the authored checklist's Implementation scope section with top-level checkbox state normalized. Keep the blank separator before the next section stable. Keep Progress, evidence and dispositions outside Implementation scope.

The coordinator recomputes before starting or resuming, and assigns the accepted fingerprint and task identity to workers. Direct plan-mode `go-work` and delegated workers recompute before edits or test commands. Refuse a mismatched fingerprint. Any actual scope or spec change needs renewed approval and any review required by the route. Checkbox updates and progress outside the scope section preserve it. Never edit authored scope to represent progress.

A legacy checklist without an Implementation scope section can be migrated by `to-plan` using the existing steps. Present the migrated scope and obtain approval once. Direct work without a plan remains authorized by the direct request within its stated scope.
