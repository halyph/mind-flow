---
tags:
  - leetcode
---

# Leetcode

## Glossary

Abbreviation | Meaning
-|-
**CI**   | Coding Interview
**SDI**  | System Design Interview
**CP**   | Competitive Programming  
**DSA**  | Data Structure and Algorithm  
**LC**   | LeetCode  
**CLRS** | Cormen, Leiserson, Rivest, and Stein  
**BFS**  | Breadth First Search  
**DFS**  | Depth First Search  
**DP**   | Dynamic Programming
**CTCI** | Cracking the Coding Interview
**EPI**  | Elements of Programming Interviews

## References

Just collection of links useful for coding interview

- **mind-flow**
  - [Resources for Practicing Coding Interview](../../blog/2018/2018-12-28-tech-interview-coding-prep-res.md)
  - [Algorithms, System Design, Interview Preparation - Github Repos](../../blog/2019/2019-01-17-algorithms-system-design-interview-preparation.md)
  - [Top "Algorithms and Data Structures" Books](../../blog/2019/2019-01-13-alg-and-ds-books.md)
- [Leetcode patterns](https://seanprashad.com/leetcode-patterns/), see [*repo*](https://github.com/seanprashad/leetcode-patterns)
- Neetcode
  - [Roadmap](https://neetcode.io/roadmap)
  - [Practice Problems](https://neetcode.io/practice)
- [Grind75](https://www.techinterviewhandbook.org/grind75)
- [PIRATE KING](https://www.piratekingdom.com/) - Leetcode Tips and tricks
- [Awesome Competitive Programming ](https://github.com/lnishan/awesome-competitive-programming) a curated list of awesome Competitive Programming, Algorithm and Data Structure resources
- **Books**' problems on LeetCode:
  - [Cracking The Coding Interview 6th Edition In Leetcode](https://leetcode.com/discuss/general-discussion/1152824/cracking-the-coding-interview-6th-edition-in-leetcode)
  - [Elements of Programming Interviews (EPI) In Leetcode](https://github.com/slgriff/EPI-to-LC)

### Repos

- [The Algorithms](https://github.com/TheAlgorithms) - Open Source resource for learning Data Structures & Algorithms and their implementation in any Programming Language
- [Swift Algorithm Club](https://github.com/raywenderlich/swift-algorithm-club)
- [williamfiset/**Algorithms**](https://github.com/williamfiset/Algorithms) is collection of algorithms and data structures (+ [Youtube](https://www.youtube.com/@WilliamFiset-videos))
- [Coding Interview University](https://github.com/jwasham/coding-interview-university)

## Patterns

[Source - Leetcode Patterns](https://seanprashad.com/leetcode-patterns/)

- If input array is *sorted* then: a) **Binary search** or b) **Two pointers**
- If asked for all *permutations*/*subsets* then **Backtracking**
- If given a *tree* then a) **DFS** or b) **BFS**
- If given a *graph* then a) **DFS** or b) **BFS**
- If given a *linked list* then: **Two pointers**
- If *recursion* is *banned* then **Stack**
- If must solve *in-place* then a) **Swap corresponding values** or b) **Store one or more different values in the same pointer**
- If asked for *maximum/minimum* subarray/subset/options then **Dynamic programming**
- If asked for *top/least K items* then **Heap** or **QuickSelect**
- If asked for *common strings* then a) Map or b) Trie
- Else
  - **Map/Set** for *O(1) time* & *O(n) space*
  - **Sort input** for *O(n * log n) time* and *O(1) space*

## Data structure

| Data structure | Key points |
|---|---|
| Primitive types | Know how int, char, double, etc. are represented in memory and the primitive operations on them.|
| Arrays  | Fast access for element at an index, slow lookups (unless sorted) and insertions. Be comfortable with notions of iteration, resizing, partitioning, merging, etc.|
| Strings | Know how strings are represented in memory. Understand basic operators such as comparison, copying, matching, joining, splitting, etc.|
| Lists | Understand trade-offs with respect to arrays. Be comfortable with iteration, insertion, and deletion within singly and doubly linked lists. Know how to implement a list with dynamic allocation, and with arrays.|
| Stacks and queues | Recognize where last-in first-out (stack) and first-in first-out (queue) semantics are applicable. Know array and linked list implementations.|
| Binary trees | Use for representing hierarchical data. Know about depth, height, leaves, search path, traversal sequences, successor/predecessor operations.|
| Heaps | Key benefit: 0(1) lookup find-max, O(log n) insertion, and 0(log n) deletion of max. Node and array representations. Min-heap variant.|
| Hash tables | Key benefit: 0(1) insertions, deletions and lookups. Key disadvantages: not suitable for order related queries; need for resizing; poor worst-case performance. Understand implementation using array of buckets and collision chains. Know hash functions for integers, strings, objects.|
| Binary search trees | Key benefit: O(log n) insertions, deletions, lookups, find-min, find-max, successor, predecessor when tree is height-balanced. Understand node fields, pointer implementation. Be familiar with notion of balance, and operations maintaining balance.|

## :lang-python: Python

### Convention for identifiers

Variable | Meaning
-|-
`i`, `j`, `k`     | for array indices
`lst`, `nums`     | list
`mat`             | matrix (list of lists)
`A`, `B`, `C`     | for arrays
`u`, `v`, `w`     | for vectors
`s`               | for a `String`
`sb`              | for a "StringBuilder" (aka `"".join(sb)`)
`ans`             | answer
`res`             | result
`acc`             | accumulator
`prev`            | previous
`nxt`             | next
`curr`            | current
`l` and `r`       | left and right
`mid`             | middle
`slow` and `fast` | pointers
`p1`, `p2`, `p3`  | pointers
`ptr`             | pointer

### Initialize List

We can create a list through `*` operator if the item in the list expression is an immutable object.

```python
>>> a = [None] * 3
>>> a
[None, None, None]
>>> a[0] = "foo"
>>> a
['foo', None, None]
```

However, if the item in the list expression is a **mutable** object, the `*` operator will copy the reference of the item `N` times (i.e. *all objects in the list point to the same address*). In order to avoid this pitfall, we should use a list comprehension to initialize a list:


```python
>>> a = [[]] * 3
>>> b = [[] for _ in range(3)]
>>> a[0].append("Hello")
>>> a
[['Hello'], ['Hello'], ['Hello']]
>>> b[0].append("Python")
>>> b
[['Python'], [], []]
```

### Initialize Matrix (List of Lists)

```python
>>> rows = 2
>>> cols = 3
>>> [[0] * cols for _ in range(rows)]
[[0, 0, 0], [0, 0, 0]]
```

Again, DON'T do this

```python
>>> a = [[0] * 3] * 3
>>> a
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> a[1][1] = 2
>>> a
[[0, 2, 0], [0, 2, 0], [0, 2, 0]]
```