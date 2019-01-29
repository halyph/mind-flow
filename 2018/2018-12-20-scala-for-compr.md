# Scala `for`-comprehensions
> **tags**: | scala | video |

This is a complete copy of **Josh Suereth** & **Dick Wall** talk on *Scala World* conference: _"For: What is it good for? — Josh Suereth & Dick Wall"_ (see references).

Actually, I have found github repo with Jupiter notebooks. But, I don't like this format and decided to store these notes here.

- [References](#references)
- [01 - For "loops"](#01---for-%22loops%22)
  - [01](#01)
  - [02](#02)
  - [03](#03)
  - [04](#04)
  - [05](#05)
  - [06](#06)
  - [07](#07)
  - [08](#08)
  - [09](#09)
- [02 - For with yield](#02---for-with-yield)

## References

- [Youtube: For: What is it good for? — Josh Suereth & Dick Wall](https://www.youtube.com/watch?v=WDaw2yXAa50)
- [Github: dickwall/use-the-fors-luke](https://github.com/dickwall/use-the-fors-luke)

---

## 01 - For "loops"

### 01

```scala
for (i <- 1 to 10) println("hello world")

// Output
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
```

### 02

```scala
for (i <- 1 to 10) println(i * i)

// Output
1
4
9
16
25
36
49
64
81
100
```

### 03

```scala
for (_ <- 1 to 10) println("hello world")

// Output
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
```

### 04

```scala
for (i <- 1 to 10) {
    print (f"the square of $i%2d")
    println(f" is ${i*i}%3d")
}

// Output
the square of  1 is   1
the square of  2 is   4
the square of  3 is   9
the square of  4 is  16
the square of  5 is  25
the square of  6 is  36
the square of  7 is  49
the square of  8 is  64
the square of  9 is  81
the square of 10 is 100
```

### 05

```scala
(1 to 10)

// Output
res0: scala.collection.immutable.Range.Inclusive = Range 1 to 10
```

### 06

```scala
(1 to 10).foreach { i =>
    print (f"the square of $i%2d")
    println(f" is ${i*i}%3d")
}

// Output
the square of  1 is   1
the square of  2 is   4
the square of  3 is   9
the square of  4 is  16
the square of  5 is  25
the square of  6 is  36
the square of  7 is  49
the square of  8 is  64
the square of  9 is  81
the square of 10 is 100
```

### 07

```scala
for {
    i <- 1 to 5
    j <- 1 to 5
} println(s"$i times $j is ${i*j}")

// Output
1 times 1 is 1
1 times 2 is 2
1 times 3 is 3
1 times 4 is 4
1 times 5 is 5
2 times 1 is 2
2 times 2 is 4
2 times 3 is 6
2 times 4 is 8
2 times 5 is 10
3 times 1 is 3
3 times 2 is 6
3 times 3 is 9
3 times 4 is 12
3 times 5 is 15
4 times 1 is 4
4 times 2 is 8
4 times 3 is 12
4 times 4 is 16
4 times 5 is 20
5 times 1 is 5
5 times 2 is 10
5 times 3 is 15
5 times 4 is 20
5 times 5 is 25
```

### 08

```scala
(1 to 5).foreach { i =>
  (1 to 5).foreach { j =>
    println(s"$i times $j is ${i*j}")
  }
}

// Output
1 times 1 is 1
1 times 2 is 2
1 times 3 is 3
1 times 4 is 4
1 times 5 is 5
2 times 1 is 2
2 times 2 is 4
2 times 3 is 6
2 times 4 is 8
2 times 5 is 10
3 times 1 is 3
3 times 2 is 6
3 times 3 is 9
3 times 4 is 12
3 times 5 is 15
4 times 1 is 4
4 times 2 is 8
4 times 3 is 12
4 times 4 is 16
4 times 5 is 20
5 times 1 is 5
5 times 2 is 10
5 times 3 is 15
5 times 4 is 20
5 times 5 is 25
```

### 09

```scala
val x1 = (1 to 5).foreach { i =>
  (1 to 5).foreach { j =>
    println(s"$i times $j is ${i*j}")
  }
}

val x2 = for {
  i <- 1 to 5
  j <- 1 to 5
} println(s"$i times $j is ${i*j}")

println(x1)
println(x2)

import scala.reflect.runtime.universe._
def typeOf[T: TypeTag](t: T) = typeTag[T]

typeOf(x1)
typeOf(x2)

// Output

1 times 1 is 1
1 times 2 is 2
1 times 3 is 3
1 times 4 is 4
1 times 5 is 5
2 times 1 is 2
2 times 2 is 4
2 times 3 is 6
2 times 4 is 8
2 times 5 is 10
3 times 1 is 3
3 times 2 is 6
3 times 3 is 9
3 times 4 is 12
3 times 5 is 15
4 times 1 is 4
4 times 2 is 8
4 times 3 is 12
4 times 4 is 16
4 times 5 is 20
5 times 1 is 5
5 times 2 is 10
5 times 3 is 15
5 times 4 is 20
5 times 5 is 25
x1: Unit = ()

1 times 1 is 1
1 times 2 is 2
1 times 3 is 3
1 times 4 is 4
1 times 5 is 5
2 times 1 is 2
2 times 2 is 4
2 times 3 is 6
2 times 4 is 8
2 times 5 is 10
3 times 1 is 3
3 times 2 is 6
3 times 3 is 9
3 times 4 is 12
3 times 5 is 15
4 times 1 is 4
4 times 2 is 8
4 times 3 is 12
4 times 4 is 16
4 times 5 is 20
5 times 1 is 5
5 times 2 is 10
5 times 3 is 15
5 times 4 is 20
5 times 5 is 25
x2: Unit = ()

()
()

import scala.reflect.runtime.universe._
typeOf: [T](t: T)(implicit evidence$1: reflect.runtime.universe.TypeTag[T])reflect.runtime.universe.TypeTag[T]

res2: reflect.runtime.universe.TypeTag[Unit] = TypeTag[Unit]
res3: reflect.runtime.universe.TypeTag[Unit] = TypeTag[Unit]
```

## 02 - For with yield

```scala

// Output
```

```scala

// Output
```

```scala

// Output
```

```scala

// Output
```

```scala

// Output
```

```scala

// Output
```