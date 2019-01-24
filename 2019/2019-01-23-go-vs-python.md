# Go vs Python comparison
> **tags**: | python | golang | vs | comparison |

It's not my writings and it's just a copy of posts from [Go vs. Python by *Peter Bengtsson*](ttp://govspy.peterbe.com/) (see [References](#references) below)

## References

- http://govspy.peterbe.com/

---

## Hello World

**Go**

```golang
package main

import "fmt"

func main() {
    fmt.Println("Hello world")
}
```

**Python**

```python
print("Hello world")
```

## Print

**Go**

```golang
package main

import "fmt"

func main() {
	fmt.Println("Some string")
	fmt.Print("Some string")
	fmt.Printf("Name: %s, Age: %d\n", "Peter", 35)
}
```

**Python**

```python
print("Some string")
print("Some string", end="")  # no newline character printed
print("Name: {}, Age: {}".format("Peter", 35))
```

## 

**Go**

```golang
```

**Python**

```python
```