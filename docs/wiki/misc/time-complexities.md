# Time Complexities

## Examples Related to Time Complexities

### Ex 1: `O(n)` for loop

```go
package main

import (
	"fmt"
)

func fun1(n int) int {
	m := 0
	for i := 0; i < n; i++ {
		m += 1
	}
	return m
}
func main() {
	// N = 100, Number of instructions O(n) :: 100
	fmt.Println("N = 100, Number of instructions O(n) ::", fun1(100))
}
```

### Ex 2: `O(n^2)` Nested for loop

```go
package main

import (
	"fmt"
)

func fun2(n int) int {
	m := 0
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			m += 1
		}
	}
	return m
}
func main() {
	// N = 100, Number of instructions O(n^2) :: 10000
	fmt.Println("N = 100, Number of instructions O(n^2) ::", fun2(100))
}
```

### Ex 3: `O(n^2)` Arithmetic series

The exact number of steps will go the same way as those of the arithmetic series. In this case, the time complexity will be: `O(n + (n−1) + (n−2) + ...) =  O(n(n+1)/2)  =  O(n^2)`

```go
package main

import (
	"fmt"
)

func fun3(n int) int {
	m := 0
	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			m += 1
		}
	}
	return m
}
func main() {
	// N = 100, Number of instructions O(n^2) :: 4950
	fmt.Println("N = 100, Number of instructions O(n^2) ::", fun3(100))
}
```

### Ex 4: `O(log(n))` Double the iteration variable

```go
package main

import (
	"fmt"
)

func fun4(n int) int {
	m := 0
	i := 1
	for i < n {
		m += 1
		i = i * 2
	}
	return m
}
func main() {
	// N = 100, Number of instructions O(log(n)) :: 7
	fmt.Println("N = 100, Number of instructions O(log(n)) ::", fun4(100))
}
```

### Ex 5: `O(log(n))` Half the iteration variable

```go
package main

import (
	"fmt"
)

func fun5(n int) int {
	m := 0
	i := n
	for i > 0 {
		m += 1
		i = i / 2
	}
	return m
}
func main() {
	// N = 100, Number of instructions O(log(n)) :: 7
	fmt.Println("N = 100, Number of instructions O(log(n)) ::", fun5(100))
}
```

### Ex 6: `O(n ^ (3/2))` Square root iteration

In this example, we consider the size of the inner loop as the square root of `n`. The size of our program is `(n∗√n)`. Thus, its time complexity is `O(n ^ (3/2))`.

```go
package main

import (
	"fmt"
	"math"
)

func fun6(n int) int {
	m := 0
	for i := 0; i < n; i++ {
		sq := math.Sqrt(float64(n))
		for j := 0; j < int(sq); j++ {
			m += 1
		}
	}
	return m
}
func main() {
	// N = 100, Number of instructions O(n^(3/2)) :: 1000
	fmt.Println("N = 100, Number of instructions O(n^(3/2)) ::", fun6(100))
}
```

### Ex 7: Nested loop in `O(n)`

```go
package main

import (
	"fmt"
)

func fun7(n int) int {
	m := 0
	for i := n; i > 0; i /= 2 {
		for j := 0; j < i; j++ {
			m += 1
		}
	}
	return m
}
func main() {
	// N = 100, Number of instructions O(n) :: 197
	fmt.Println("N = 100, Number of instructions O(n) ::", fun7(100))
}

```

### Ex 8: `O(n^2)` Arithmetic progression

```go
package main

import (
	"fmt"
)

func fun8(n int) int {
	m := 0
	for i := 0; i < n; i++ {
		for j := i; j > 0; j-- {
			m += 1
		}
	}
	return m
}
func main() {
	// N = 100, Number of instructions O(n^2) :: 4950
	fmt.Println("N = 100, Number of instructions O(n^2) ::", fun8(100))
}
```

### Ex 9: `O(n^3)` Triple nested loop

```go
package main

import (
	"fmt"
)

func fun9(n int) int {
	m := 0
	for i := 0; i < n; i++ {
		for j := i; j < n; j++ {
			for k := j + 1; k < n; k++ {
				m += 1
			}
		}
	}
	return m
}
func main() {
	// N = 100, Number of instructions O(n^3) :: 166650
	fmt.Println("N = 100, Number of instructions O(n^3) ::", fun9(100))
}
```

### Ex 10: Multiple loops in `O(n)`

This is a tricky one. In this example, `j` is not initialized for every iteration. For `i=0`, the loop of `j` executes completely. But for the remaining values of `i`, the loop of `j` does not execute. Time complexity, in this case, is `O(n)`
 
```go
package main

import (
	"fmt"
)

func fun10(n int) int {
	j := 0
	m := 0
	for i := 0; i < n; i++ {
		for ; j < n; j++ {
			m += 1
		}
	}
	return m
}
func main() {
	// N = 100, Number of instructions O(n) :: 100
	fmt.Println("N = 100, Number of instructions O(n) ::", fun10(100))
}
```

## Construct a Double-Linked List

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