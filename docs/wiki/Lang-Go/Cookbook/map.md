---
tags:
  - golang
---

# Maps

## 1. Sort a map

```go
package main

import (
	"fmt"
	"sort"
)

var (
	barVal = map[string]int{
		"alpha":   1,
		"bravo":   2,
		"charlie": 3,
		"delta":   4,
		"echo":    5,
		"foxtrot": 6,
	}
)

func main() {
	fmt.Println("**unsorted:**  ")
	for k, v := range barVal {
		fmt.Printf("%v -> %v  \n", k, v) // read random keys
	}
	keys := make([]string, len(barVal)) // storing all keys in separate slice
	i := 0
	for k := range barVal {
		keys[i] = k
		i++
	}
	sort.Strings(keys) // sorting the keys slice

	fmt.Println("\n**sorted:**  ")
	for _, k := range keys {
		fmt.Printf("%v -> %v  \n", k, barVal[k]) // reading key from keys and value from barVal
	}
}
```

??? example "Output"
    **unsorted:**  
    alpha -> 1  
    bravo -> 2  
    charlie -> 3  
    delta -> 4  
    echo -> 5  
    foxtrot -> 6  

    **sorted:**  
    alpha -> 1  
    bravo -> 2  
    charlie -> 3  
    delta -> 4  
    echo -> 5  
    foxtrot -> 6  

## 2. Invert a map

```go
package main

import (
	"fmt"
)

var (
	barVal = map[string]int{
		"alpha":   34,
		"bravo":   56,
		"charlie": 23,
		"delta":   87,
		"echo":    56,
		"foxtrot": 12,
		"golf":    34,
		"hotel":   16,
		"indio":   87,
		"juliet":  65,
		"kilo":    43,
		"lima":    98,
	}
)

func main() {
	invMap := make(map[int][]string, len(barVal)) // interchanging types of keys and values
	for k, v := range barVal {
		if _, ok := invMap[v]; ok {
			invMap[v] = append(invMap[v], ",") // add comma before adding another value
		}
		invMap[v] = append(invMap[v], k) // key becomes value and value becomes key
	}
	fmt.Println("**inverted:**  ")
	for k, v := range invMap {
		fmt.Printf("%v -> %v  \n", k, v)
	}
}
```

??? example "Output"
    **inverted:**  
    98 -> [lima]  
    56 -> [bravo , echo]  
    12 -> [foxtrot]  
    16 -> [hotel]  
    43 -> [kilo]  
    34 -> [alpha , golf]  
    23 -> [charlie]  
    87 -> [delta , indio]  
    65 -> [juliet]  