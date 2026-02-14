# Go vs Python comparison
<!-- tags: python, golang, vs, comparison -->

It's not my writings and it's just a copy of [Go vs. Python by *Peter Bengtsson*](ttp://govspy.peterbe.com/) (see [References](#references) below)

- [References](#references)
- [Hello World](#hello-world)
- [Print](#print)
- [Comments](#comments)
- [Multiline Strings](#multiline-strings)
- [Lists](#lists)
- [Maps](#maps)
- [Booleans](#booleans)
- [Forloop](#forloop)
- [Range](#range)
- [Switch](#switch)
- [Variadic Functions](#variadic-functions)
- [Time Elapsed](#time-elapsed)
- [Closure Functions](#closure-functions)
- [Defer](#defer)
- [Panic Recover](#panic-recover)
- [Mutables](#mutables)
- [Structs](#structs)
- [Methods](#methods)
- [Goroutines](#goroutines)
- [Args](#args)
- [Import Alias](#import-alias)
- [Sprintf](#sprintf)
- [Uniqify](#uniqify)
- [Dotdict](#dotdict)

## References

- [http://govspy.peterbe.com/](http://govspy.peterbe.com/)

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

## Comments

**Go**

```golang
package main

// This is a general comment

/* This is also a comment
   but on multiple lines.
*/

/* This is the multi-line comment for the function main().
   To get access to this from the command line, run:

     godoc comments.go

*/

func main() {
}
```

**Python**

```python
"""This is a doc string for the whole module"""

# This is a inline comment


class Class(object):
    """This is the doc string for the class"""


print(__doc__)
print(Class.__doc__)
```

## Multiline Strings

**Go**

```golang
package main

import "fmt"

func main() {
	fmt.Println(`This is
a multi-line string.
`)
	fmt.Println(
		"O'word " +
			"Another \"word\" " +
			"Last word.")
}
```

**Python**

```python
print(
    """This is
a multi-line string.
"""
)
print("O'word " 'Another "word" ' "Last word.")
```

## Lists

**Go**

```golang
package main

import "fmt"

func main() {
	// initialized array
	var numbers [5]int // becomes [0, 0, 0, 0, 0]
	// change one of them
	numbers[2] = 100
	// create a new slice from an array
	some_numbers := numbers[1:3]
	fmt.Println(some_numbers) // [0, 100]
	// length of it
	fmt.Println(len(numbers))

	// initialize a slice
	var scores []float64
	scores = append(scores, 1.1) // recreate to append
	scores[0] = 2.2              // change your mind
	fmt.Println(scores)          // prints [2.2]

	// when you don't know for sure how much you're going
	// to put in it, one way is to
	var things [100]string
	things[0] = "Peter"
	things[1] = "Anders"
	fmt.Println(len(things)) // 100
}
```

**Python**

```python
# initialize list
numbers = [0] * 5
# change one of them
numbers[2] = 100
some_numbers = numbers[1:3]
print(some_numbers)  # [0, 100]
# length of it
print(len(numbers))  # 5

# initialize another
scores = []
scores.append(1.1)
scores[0] = 2.2
print(scores)  # [2.2]
```

## Maps

**Go**

```golang
//You can make a map of maps with:
elements : make(map[string]map[string]int)
elements["H"] = map[string]int{
    "protons": 1,
    "neutrons": 0,
}
```

```golang
//But note, this is what you have struct for.

package main

import "fmt"

func main() {
	elements := make(map[string]int)
	elements["H"] = 1
	fmt.Println(elements["H"])

	// remove by key
	elements["O"] = 8
	delete(elements, "O")

	// only do something with a element if it's in the map
	if number, ok := elements["O"]; ok {
		fmt.Println(number) // won't be printed
	}
	if number, ok := elements["H"]; ok {
		fmt.Println(number) // 1
	}

}
```

**Python**

```python
elements = {}
elements["H"] = 1
print(elements["H"])  # 1

# remove by key
elements["O"] = 8
elements.pop("O")

# do something depending on the being there
if "O" in elements:
    print(elements["O"])
if "H" in elements:
    print(elements["H"])
```

## Booleans

**Go**

```golang
x := 1
if x != 0 {
    fmt.Println("Yes")
}
var y []string
if len(y) != 0 {
    fmt.Println("this won't be printed")
}
```

**Python**

```python
x = 1
if x:
    print "Yes"
y = []
if y:
    print "this won't be printed"
```

**Go**

```golang
package main

import "fmt"

func main() {
	fmt.Println(true && false) // false
	fmt.Println(true || false) // true
	fmt.Println(!true)         // false

	x := 1
	if x != 0 {
		fmt.Println("Yes")
	}
	var y []string
	if len(y) != 0 {
		fmt.Println("this won't be printed")
	}

}
```

**Python**

```python
print(True and False)  # False
print(True or False)  # True
print(not True)  # False
```

## Forloop


```golang
package main

import "fmt"

func main() {
	i := 1
	for i <= 10 {
		fmt.Println(i)
		i += 1
	}

	// same thing more but more convenient
	for i := 1; i <= 10; i++ {
		fmt.Println(i)
	}
}
```

**Python**

```python
i = 1
while i <= 10:
    print(i)
    i += 1

# ...or...

for i in range(1, 11):
    print(i)
```

## Range

**Go**

```golang
package main

import "fmt"

func main() {
	names := []string{
		"Peter",
		"Anders",
		"Bengt",
	}
	/* This will print

	1. Peter
	2. Anders
	3. Bengt
	*/
	for i, name := range names {
		fmt.Printf("%d. %s\n", i+1, name)
	}
}
```

**Python**

```python
names = ["Peter", "Anders", "Bengt"]
for i, name in enumerate(names):
    print("{}. {}".format(i + 1, name))
```

## Switch

**Go**

```golang
package main

import (
	"fmt"
	"strconv"
)

func str2int(s string) int {
	i, err := strconv.Atoi(s)
	if err != nil {
		panic("Not a number")
	}
	return i
}

func main() {
	var number_string string
	fmt.Scanln(&number_string)
	number := str2int(number_string)

	switch number {
	case 8:
		fmt.Println("Oxygen")
	case 1:
		fmt.Println("Hydrogen")
	case 2:
		fmt.Println("Helium")
	case 11:
		fmt.Println("Sodium")
	default:
		fmt.Printf("I have no idea what %d is\n", number)
	}

	// Alternative solution

	fmt.Scanln(&number_string)
	db := map[int]string{
		1:  "Hydrogen",
		2:  "Helium",
		8:  "Oxygen",
		11: "Sodium",
	}
	number = str2int(number_string)
	if name, exists := db[number]; exists {
		fmt.Println(name)
	} else {
		fmt.Printf("I have no idea what %d is\n", number)
	}

}
```

**Python**

```python
def input_():
    return int(input())


number = input_()
if number == 8:
    print("Oxygen")
elif number == 1:
    print("Hydrogen")
elif number == 2:
    print("Helium")
elif number == 11:
    print("Sodium")
else:
    print("I have no idea what %d is" % number)


# Alternative solution
number = input_()
db = {1: "Hydrogen", 2: "Helium", 8: "Oxygen", 11: "Sodium"}
print(db.get(number, "I have no idea what %d is" % number))
```

## Variadic Functions

```golang
package main

import "fmt"

func average(numbers ...float64) float64 {
	total := 0.0
	for _, number := range numbers {
		total += number
	}
	return total / float64(len(numbers))
}

func main() {
	fmt.Println(average(1, 2, 3, 4)) // 2.5
}
```

**Python**

```python
def average(*numbers):
    return sum(numbers) / len(numbers)

print(average(1, 2, 3, 4))  # 10/4 = 2.5
```

## Time Elapsed

**Go**

```golang
package main

import "fmt"
import "time"

func main() {
	t0 := time.Now()
	elapsed := time.Since(t0)
	fmt.Printf("Took %s", elapsed)
}
```

**Python**

```python
import time

t0 = time.time()
time.sleep(3.5)  # for example
t1 = time.time()
print("Took {:.2f} seconds".format(t1 - t0))
```

## Closure Functions

**Go**

```golang
package main

import "fmt"

func main() {

	number := 0

	/* It has to be a local variable like this.
	   You can't do `func increment(amount int) {` */
	increment := func(amount int) {
		number += amount
	}
	increment(1)
	increment(2)

	fmt.Println(number) // 3

}
```

**Python**

```python
def run():
    def increment(amount):
        return number + amount

    number = 0
    number = increment(1)
    number = increment(2)
    print(number)  # 3


run()
```

## Defer

**Go**

```golang
package main

import (
	"os"
)

func main() {
	f, _ := os.Open("defer.py")
	defer f.Close()
	// you can now read from this
	// `f` thing and it'll be closed later

}
```

**Python**

```python
f = open("defer.py")
try:
    f.read()
finally:
    f.close()
```

## Panic Recover

**Go**

```golang
package main

import "fmt"

func main() {

	// Running this will print out:
	//    error was: Shit!
	defer func() {
		fmt.Println("error was:", recover())
	}()
	panic("Shit!")
}
```

**Python**

```python
try:
    raise Exception("Shit")
except Exception as e:
    print("error was:", e)
```

## Mutables

**Go**

```golang
package main

import (
	"fmt"
	"strings"
)

func upone_list(thing []string, index int) {
	thing[index] = strings.ToUpper(thing[index])
}

func upone_map(thing map[string]string, index string) {
	thing[index] = strings.ToUpper(thing[index])
}

func main() {
	// mutable
	list := []string{"a", "b", "c"}
	upone_list(list, 1)
	fmt.Println(list) // [a B c]

	// mutable
	dict := map[string]string{
		"a": "anders",
		"b": "bengt",
	}
	upone_map(dict, "b")
	fmt.Println(dict) // map[a:anders b:BENGT]
}
```

**Python**

```python
def upone(mutable, index):
    mutable[index] = mutable[index].upper()


list_ = ["a", "b", "c"]
upone(list_, 1)
print(list_)  # ['a', 'B', 'c']

dict_ = {"a": "anders", "b": "bengt"}
upone(dict_, "b")
print(dict_)  # {'a': 'anders', 'b': 'BENGT'}
```

## Structs

**Go**

```golang
package main

import (
	"fmt"
	"math"
)

type Point struct {
	x float64
	y float64
}

func distance(point1 Point, point2 Point) float64 {
	return math.Sqrt(point1.x*point2.x + point1.y*point2.y)
}

// Since structs get automatically copied,
// it's better to pass it as pointer.
func distance_better(point1 *Point, point2 *Point) float64 {
	return math.Sqrt(point1.x*point2.x + point1.y*point2.y)
}

func main() {
	p1 := Point{1, 3}
	p2 := Point{2, 4}
	fmt.Println(distance(p1, p2))          // 3.7416573867739413
	fmt.Println(distance_better(&p1, &p2)) // 3.7416573867739413
}
```

**Python**

```python
from math import sqrt


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(point1, point2):
    return sqrt(point1.x * point2.x + point1.y * point2.y)


p1 = Point(1, 3)
p2 = Point(2, 4)
print(distance(p1, p2))  # 3.74165738677
```

## Methods

**Go**

```golang
package main

import (
	"fmt"
	"math"
)

type Point struct {
	x float64
	y float64
}

func (this Point) distance(other Point) float64 {
	return math.Sqrt(this.x*other.x + this.y*other.y)
}

// Dince structs get automatically copied,
// it's better to pass it as pointer.
func (this *Point) distance_better(other *Point) float64 {
	return math.Sqrt(this.x*other.x + this.y*other.y)
}

func main() {
	p1 := Point{1, 3}
	p2 := Point{2, 4}
	fmt.Println(p1.distance(p2))         // 3.7416573867739413
	fmt.Println(p1.distance_better(&p2)) // 3.7416573867739413
}
```

**Python**

```python
from math import sqrt


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return sqrt(self.x * other.x + self.y * other.y)


p1 = Point(1, 3)
p2 = Point(2, 4)
print(p1.distance(p2))  # 3.74165738677
print(p2.distance(p1))  # 3.74165738677
```

## Goroutines

**Go**

```golang
package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"sync"
)

func f(url string) {
	response, err := http.Get(url)
	if err != nil {
		panic(err)
	}
	defer response.Body.Close()
	body, err := ioutil.ReadAll(response.Body)
	if err != nil {
		panic(err)
	}

	fmt.Println(len(body))
}

// See the example in https://golang.org/pkg/sync/#WaitGroup
func main() {
	var wg sync.WaitGroup
	urls := []string{
		"https://www.peterbe.com",
		"https://python.org",
		"https://golang.org",
	}
	for _, url := range urls {
		wg.Add(1)
		go func(url string) {
			defer wg.Done()
			f(url)
		}(url)
	}
	// Wait for the goroutines to finish
	wg.Wait()
}
```

**Python**

```python
import urllib2
import multiprocessing


def f(url):
    req = urllib2.urlopen(url)
    try:
        print(len(req.read()))
    finally:
        req.close()


urls = ("https://www.peterbe.com", "https://python.org", "https://golang.org")


if __name__ == "__main__":
    p = multiprocessing.Pool(3)
    p.map(f, urls)
```

## Args

**Go**

```golang
package main

import (
	"fmt"
	"os"
	"strings"
)

func transform(args []string) {
	for _, arg := range args {
		fmt.Println(strings.ToUpper(arg))
	}

}
func main() {
	args := os.Args[1:]
	transform(args)
}
```

**Python**

```python
import sys


def transform(*args):
    for arg in args:
        print(arg.upper())


if __name__ == "__main__":
    transform(*sys.argv[1:])
```

## Import Alias

**Go**

```golang
import (
    pb "github.com/golang/groupcache/groupcachepb"
)
// or
import (
    _ "image/png"  // You can also import packages that you won't actually use
)

// or 
package main

import (
	"fmt"
	s "strings"
)

func main() {
	fmt.Println(s.ToUpper("world"))
}
```

**Python**

```python
import string as s

print(s.upper("world"))
```

## Sprintf

**Go**

```golang
package main

import "fmt"

func main() {
	max := 10
	panic(fmt.Sprintf("The max. number is %d", max))
}
```

**Python**

```python
max = 10
raise Exception(f"The max. number is {max}")
```

## Uniqify

**Go**

```golang
package main

import "fmt"

func uniqify(items []string) []string {
	uniq := make([]string, 0)
	seen := make(map[string]bool)

	// For the highest memory efficiency, do:
	// seen := make(map[string]struct{})
	// see: https://stackoverflow.com/questions/37320287/maptstruct-and-maptbool-in-golang

	for _, i := range items {
		if _, exists := seen[i]; !exists {
			uniq = append(uniq, i)
			seen[i] = true
		}
	}

	return uniq
}

func main() {
	items := []string{"B", "B", "E", "Q", "Q", "Q"}
	items = uniqify(items)
	fmt.Println(items) // prints [B E Q]
}
```

**Python**

```python
def uniqify(seq):
    seen = {}
    unique = []
    for item in seq:
        if item not in seen:
            seen[item] = 1
            unique.append(item)
    return unique


items = ["B", "B", "E", "Q", "Q", "Q"]
print(uniqify(items))  # prints ['B', 'E', 'Q']
```

## Dotdict

**Go**

```golang
package main

import "fmt"

func main() {
	names := []string{"peter", "anders", "bengt", "bengtsson"}
	initials := make(map[string]int)
	for _, name := range names {
		initial := string(name[0])
		initials[initial]++
	}
	fmt.Println(initials)
	// outputs
	// map[p:1 a:1 b:2]
}
```

**Python**

```python
initials = {}
for name in ("peter", "anders", "bengt", "bengtsson"):
    initial = name[0]
    # if initial not in initials:
    #     initials[initial] = 0
    initials.setdefault(initial, 0)
    initials[initial] += 1

print(initials)
# outputs
# {'a': 1, 'p': 1, 'b': 2}
```