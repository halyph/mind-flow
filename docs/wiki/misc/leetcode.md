---
icon: simple/leetcode
tags:
  - leetcode
---

# Leetcode

## Glossary

Abbreviation | Meaning |
-|-
**CI**  | Coding Interview
**SDI** | System Design Interview
**CP**  | Competitive Programming  
**DSA** | Data Structure and Algorithm  
**LC**  | LeetCode  
**CLRS** | Cormen, Leiserson, Rivest, and Stein  
**BFS** | Breadth First Search  
**DFS** | Depth First Search  
**DP**  | Dynamic Programming

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
- [PIRATE KING](https://www.piratekingdom.com/) - Leetcode Tips and tricks
- [Awesome Competitive Programming ](https://github.com/lnishan/awesome-competitive-programming) a curated list of awesome Competitive Programming, Algorithm and Data Structure resources

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

## :lang-java: Java

- `<>` diamond operator
- `Objects` utility class 
- `0b001_00001`
- Have a convention for identifiers:
  - `i, j ,k` for array indices
  - `A,B,C` for arrays
  - `u,v,w` for vectors
  - `s` for a `String`
  - `sb` for a `StringBuilder`

## Data structure

| Data structure | Key points |
|----|---|
| Primitive types | Know how int, char, double, etc. are represented in memory and the primitive operations on them.|
| Arrays  | Fast access for element at an index, slow lookups (unless sorted) and insertions. Be comfortable with no¬ tions of iteration, resizing, partitioning, merging, etc.|
| Strings | Know how strings are represented in memory. Understand basic operators such as comparison, copying, matching, joining, splitting, etc.|
| Lists | Understand trade-offs with respect to arrays. Be comfortable with iteration, insertion, and deletion within singly and doubly linked lists. Know how to implement a list with dynamic allocation, and with arrays.|
| Stacks and queues | Recognize where last-in first-out (stack) and first-in first-out (queue) semantics are applicable. Know array and linked list implementations.|
| Binary trees | Use for representing hierarchical data. Know about depth, height, leaves, search path, traversal sequences, successor/predecessor operations.|
| Heaps | Key benefit: 0(1) lookup find-max, O(log n) insertion, and 0(log n) deletion of max. Node and array representations. Min-heap variant.|
| Hash tables | Key benefit: 0(1) insertions, deletions and lookups. Key disadvantages: not suitable for orderrelated queries; need for resizing; poor worst-case performance. Understand implementation using array of buckets and collision chains. Know hash functions for integers, strings, objects.|
| Binary search trees | Key benefit: O(logn) insertions, deletions, lookups, find-min, find-max, successor, predecessor when tree is height-balanced. Understand node fields, pointer implementation. Be familiar with notion of balance, and operations maintaining balance.|
