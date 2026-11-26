# Brainstorm or Lite

1. After reading available requirements, offer **Brainstorm | Lite** unless the user already chose. Recommend Brainstorm for unresolved direction, likely duplicated flows, or a material trade-off. Recommend Lite for a clear, bounded change. Wait for the choice.
2. **Lite:** Ask only material gaps in goal, scope, user behavior or acceptance. Keep the answers in the brief.
3. **Brainstorm:** Ask enough to state the problem, target users, constraints and success. Show a short working hypothesis and wait for the user's explicit confirmation. Keep clarifying if they revise it. Start no Goldfish before confirmation.
4. After confirmation, start exactly seven fresh **Standard** workers, one per lens, using the [host mapping](../../go-flow/references/agents.md#host-mapping). Batch when slots are limited. Give each the hypothesis, relevant source pointers and one lens:
   - Simplicity and reuse
   - Cost and capacity
   - User or developer experience
   - Migration and compatibility
   - Observability and operations
   - Maintainability
   - Alternative approaches
5. Request cited evidence, risks and questions for the user. Collect one result per lens; report missing coverage and let the user decide whether to retry or continue with incomplete input. Merge duplicate questions and resolve repo-answerable questions before asking. Present plausible alternatives and let the user confirm direction. Capture these decisions in `spec.md` under Requirements and Open questions; retain the normal [confirmation rule](../SKILL.md#confirmation).

Only delegate source retrieval when the current host cannot reach required sources directly and a compatible worker can. Use the [host mapping](../../go-flow/references/agents.md#host-mapping) and the blocked-source rule.
