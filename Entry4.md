# Custom Types in Python {#gradient}

---

Back in python 3.5 there was the `NewType` type in the `typing` module. Then in python 3.10 & 3.11 there was a `TypeAlias` type in the `typing` module. TypeAlias has been deprecated in 3.12. Instead, we are encouraged to use the `type` keyword.
Example:
Old:

```python
from typing import TypeAlias
Point: TypeAlias = tuple[int, int]
```

New:

```python
type Point = tuple[int, int]
```

[Previous Page](Entry3.md) [Next Page](Entry5.md)
