---
tags:
  - java
  - data structure
  - algorithm
---

# Java Collections Libraries

## Overview

- *Popular*
  - [Java Collections Framework](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/package-summary.html)
  - [Apache Commons Collections](https://github.com/apache/commons-collections)
  - [Guava](https://github.com/google/guava) [^1]
  - [Eclipse Collections](https://github.com/eclipse/eclipse-collections)
  - [fastutil](https://fastutil.di.unimi.it) [^2]
  - [JCTools](https://github.com/JCTools/JCTools) [^3]
- *Graph*
  - [JGraphT](https://github.com/jgrapht/jgrapht) [^4]
  - [JUNG](https://github.com/jrtom/jung) [^5]
- *Persistent collections*
  - [vavr](https://github.com/vavr-io/vavr) [^6]
- *Personal repos*
  - [**kevin-wayne/algs4**](https://github.com/kevin-wayne/algs4/) *"Algorithms" 4th edition book's code and libraries*
  - [**java-algorithms-implementation**](https://github.com/phishman3579/java-algorithms-implementation) *sample algorithms and data structures implemented*
  - [**williamfiset/Algorithms**](https://github.com/williamfiset/Algorithms) *is a collection of algorithms and data structures*

## Java Collections Framework

Name | Description |
---------|----------|
`ArrayList` | An indexed sequence that grows and shrinks dynamically
`LinkedList` | An ordered sequence that allows efficient insertions and removal at any location
`ArrayDeque` | A double-ended queue that is implemented as a circular array
`HashSet` | An unordered collection that rejects duplicates
`TreeSet` | A sorted set
`EnumSet` | A set of enumerated type values
`LinkedHashSet` | A set that remembers the order in which elements were inserted
`PriorityQueue` | A collection that allows efficient removal of the smallest element
`HashMap` | A data structure that stores key/value associations
`TreeMap` | A map in which the keys are sorted
`EnumMap` | A map in which the keys belong to an enumerated type
`LinkedHashMap` | A map that remembers the order in which entries were added
`WeakHashMap` | A map with values that can be reclaimed by the garbage collector if they are not used elsewhere
`IdentityHashMap` | A map with keys that are compared by ==, not equals

[^1]: **Guava** is a set of core Java libraries from Google that includes new collection types (such as multimap and multiset), immutable collections, a graph library, and utilities for concurrency, I/O, hashing, primitives, strings, and more! It is widely used on most Java projects within Google, and widely used by many other companies as well.
[^2]: **fastutil** extends the Java Collections Framework by providing type-specific maps, sets, lists, and queues with a small memory footprint and fast access and insertion; it provides also big (64-bit) arrays, sets, and lists, sorting algorithms, fast, practical I/O classes for binary and text files, and facilities for memory mapping large files.
[^3]: **JCTools** Java Concurrency Tools for the JVM. This project aims to offer some concurrent data structures currently missing from the JDK.
[^4]: **JGraphT** is Java class library that provides mathematical graph-theory objects and algorithms.
[^5]: **JUNG** is the Java Universal Network/Graph Framework.
[^6]: **vavr** provides persistent collections, functional abstractions for error handling, concurrent programming, pattern matching and much more.
