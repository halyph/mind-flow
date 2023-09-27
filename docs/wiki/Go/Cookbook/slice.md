# Slices

## Simulating operations with `append`

- See [go/wiki/SliceTricks](https://github.com/golang/go/wiki/SliceTricks)

The `append` method is very versatile and can be used for all kinds of manipulations:

| What?      | How? (Snippet)                          |
| ----------- | ------------------------------------ |
| Append a slice `b` to an existing slice `a` | `a = append(a, b...)` |
| Delete item at index `i`| `a = append(a[:i], a[i+1:]...)` |
| Cut from index `i` till `j` out of slice `a` | `a = append(a[:i], a[j:]...)` |
| Extend slice a with a new slice of length `j` | `a = append(a, make([]T, j)...)` |
| Insert item x at index `i` | `a = append(a[:i], append([]T{x}, a[i:]...)...)` |
| Insert a new slice of length `j` at index `i` | `a = append(a[:i], append(make([]T, j), a[i:]...)...)` |
| Insert an existing slice `b` at index `i` | `a = append(a[:i], append(b, a[i:]...)...)` |
| Pop highest element from stack | `x, a = a[len(a)-1], a[:len(a)-1]`|
| Push an element x on a stack | `a = append(a, x)`|

So to represent a resizable sequence of elements use a slice and the `append` function.
