---
tags:
  - golang
---

# `container`

- [heap](https://pkg.go.dev/container/heap) provides heap operations for any type that implements heap.Interface.
- [list](https://pkg.go.dev/container/list) implements a doubly linked list.
- [ring](https://pkg.go.dev/container/ring) implements operations on circular lists.

## `container/list`

### Construct a Double-Linked List

```go
package main

import (
	"container/list"
	"fmt"
)

func insertListElements(n int) *list.List { // add elements in list from 1 to n
	lst := list.New()
	for i := 1; i <= n; i++ {
		lst.PushBack(i) // insertion here
	}
	return lst
}

func main() {
	n := 5
	myList := insertListElements(n)
	for e := myList.Front(); e != nil; e = e.Next() {
		fmt.Println(e.Value)
	}
}
```

??? example "Output"
    ```
    1
    2
    3
    4
    5
    ```
