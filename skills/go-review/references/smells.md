# Code Smells

Judgement calls: write "possible <smell>". Project rules override. Skip tooling-enforced items and anything outside changed lines.

- **Mysterious name:** does not say what the thing does or holds.
- **Duplicated code:** same logic in several places in the change.
- **Feature envy:** uses another object's data more than its own.
- **Data clumps:** same few fields or parameters always travel together.
- **Primitive obsession:** string or number standing in for a concept.
- **Repeated switches:** same `switch` or `if` chain on one type, in several places.
- **Shotgun surgery:** one small change forces edits in many files.
- **Divergent change:** one file edited for several unrelated reasons.
- **Speculative generality:** options or abstractions for needs nobody has.
- **Message chains:** long `a.b().c().d()` walks.
- **Middle man:** only passes calls on.
- **Refused bequest:** subclass ignores or overrides most of what it inherits.
