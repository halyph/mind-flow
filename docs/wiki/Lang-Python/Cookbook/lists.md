---
tags:
  - python
---

# Lists

## Transpose matrix

Use `zip(*matrix)` to transpose the matrix (convert rows to columns).

```python
>>> matrix = [
...     [1, 2, 3],
...     [3, 1, 2],
...     [2, 3, 1]
... ]
>>> list(zip(*matrix))
[(1, 3, 2), (2, 1, 3), (3, 2, 1)]
```