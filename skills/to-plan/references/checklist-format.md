# Checklist Format

Return this checklist alongside the plan, per [writing rules](writing-rules.md).

## Structure

Use a single **Implementation scope** section. For each step, list one actionable checkbox, its stable step ID and a link to the corresponding anchor in `dev-view/plan.html`. Indent the target, working precedent or reason it does not apply, difference from that precedent, and an observable focused check. Record the approved pipeline and order. Reuse exact source or test paths and symbols from the step.

The scope section is approved together with the plan. Keep current step, blockers, evidence, commit SHAs, and findings in **Progress**. Checkbox state and Progress are mutable. Scope, precedents and acceptance changes require renewed approval. Add discoveries to Progress until approved. Untick invalidated work with a reason.

```markdown
# PROJ-123 checklist

## Implementation scope

- [ ] [Step 1](../dev-view/plan.html#step-1) · Pipeline Toolbar · Hide Export when the flag is off
  - Target: `src/toolbar.ts` and `src/toolbar.test.ts`.
  - Precedent: `FeatureFlagService.isEnabled` in `src/app/shared/feature-flag.service.ts`, used by the Print action.
  - Difference: Export uses its own flag. Print stays visible.
  - Verify: Turn Export off and assert the button disappears while Print remains.

## Progress

- Next: Waiting for plan approval.
- Evidence: Pending.
```

## Approval

Record and verify [approval](approval.md) before starting work. Update Progress to show the actually ready step or blocker. Preserve checks and evidence when resuming. Mark a step active only when work starts. The coordinator records delegated progress after integration and tracks any unrelated changes separately.
