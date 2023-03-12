# Strings and Text

## 1. Reverse a String

```go
package main

import "fmt"

func reverse(s string) string {
	runes := []rune(s)
	n := len(runes)
	mid := n / 2

	for i := 0; i < mid; i++ {
		runes[i], runes[n-1-i] = runes[n-1-i], runes[i]
	}

	return string(runes)
}

func main() {
	// reverse a string:
	str := "the quick brown 狐 jumped over the lazy 犬"

	fmt.Printf("The reversed string using variant is: `%s`\n", reverse(str))
}
```

??? example "Output"
    The reversed string using variant is: `犬 yzal eht revo depmuj 狐 nworb kciuq eht`