# Annotated UI changes

1. Treat the annotation and accompanying instruction as the direct request. Read only the supplied route, element identifiers, screenshot and relevant context. Resolve the exact element to its rendered component, call site and existing tests. If more than one matches after checking, ask the user to identify it before editing.
2. Read applicable project rules and comparable components. Cite the reused component, function or UI flow. Keep neighboring controls and unrelated paths in place.
3. Run the relevant scoped `dev-tdd` and `go-ut` authoring steps inline. Use the actual suite and fixtures, with an observable assertion that catches the requested change. Write specs even when the user leaves test execution to themselves; run only authorized tests. If there is no unit setup or no unit-testable behavior, state the evidence and gap.
4. Confirm delivery by reading the source and spec diff together. Report the annotated target and source location, the spec and fixture, what it asserts, and actual run evidence or reason no run was made. Check project style and affected neighboring behavior before delivery.
