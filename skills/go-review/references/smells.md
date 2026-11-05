# Code Smells

Signs the changed code may be badly structured.

## Rules

- Judgement calls, never hard violations: write "possible <smell>".
- Project rules override them.
- Skip what tooling enforces and anything outside changed lines.

## Smells

- **Mysterious name:** name does not say what the thing does or holds.
- **Duplicated code:** same logic in more than one place in the change.
- **Feature envy:** method uses another object's data more than its own.
- **Data clumps:** same few fields or parameters always travel together.
- **Primitive obsession:** string or number standing in for a real concept.
- **Repeated switches:** same `switch` or `if` chain on one type, in several places.
- **Shotgun surgery:** one small change forces edits in many files.
- **Divergent change:** one file edited for several unrelated reasons.
- **Speculative generality:** options or abstractions for needs nobody has.
- **Message chains:** long `a.b().c().d()` walks the caller should not know about.
- **Middle man:** class or function that only passes calls on.
- **Refused bequest:** subclass ignores or overrides most of what it inherits.
