# Scala `for`-comprehensions
> | scala | video |

This is a complete copy of **Josh Suereth** & **Dick Wall** talk on *Scala World* conference: _"For: What is it good for? — Josh Suereth & Dick Wall"_ (see references).

Actually, I have found github repo with Jupiter notebooks. But, I don't like this format and decided to store these notes here.

- [References](#references)
- [01 - For "loops"](#01---for-%22loops%22)
  - [01.01](#0101)
  - [01.02](#0102)
  - [01.03](#0103)
  - [01.04](#0104)
  - [01.05](#0105)
  - [01.06](#0106)
  - [01.07](#0107)
  - [01.08](#0108)
  - [01.09](#0109)
- [02 - For with yield](#02---for-with-yield)
  - [02.01](#0201)
  - [02.02](#0202)
  - [02.03](#0203)
  - [02.04](#0204)
  - [02.05](#0205)
  - [02.06](#0206)
  - [02.07](#0207)
  - [02.08](#0208)
  - [02.09](#0209)
  - [02.10](#0210)
- [03 - Options, options, options](#03---options-options-options)

## References

- [Youtube: For: What is it good for? — Josh Suereth & Dick Wall](https://www.youtube.com/watch?v=WDaw2yXAa50)
- [Github: dickwall/use-the-fors-luke](https://github.com/dickwall/use-the-fors-luke)

---

## 01 - For "loops"

### 01.01

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

### 01.02

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

### 01.03

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

### 01.04

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

### 01.05

```scala
(1 to 10)

// Output
res0: scala.collection.immutable.Range.Inclusive = Range 1 to 10
```

### 01.06

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

### 01.07

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

### 01.08

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

### 01.09

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

### 02.01

```scala
val squares = for (i <- 1 to 10) yield (i * i)

// Output
squares: collection.immutable.IndexedSeq[Int] = Vector(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
```

### 02.02

```scala
val squareMap = (for (i <- 1 to 10) yield (i -> (i * i))).toMap

// Output
squareMap: Map[Int, Int] = Map(
  5 -> 25,
  10 -> 100,
  1 -> 1,
  6 -> 36,
  9 -> 81,
  2 -> 4,
  7 -> 49,
  3 -> 9,
  8 -> 64,
  4 -> 16
)
```

### 02.03

```scala
case class TimesResult(i: Int, j: Int, mult: Int)

val timesTable = for {
    i <- 1 to 5
    j <- 1 to 5
} yield TimesResult(i, j, i * j)

// Output

defined class TimesResult
timesTable: collection.immutable.IndexedSeq[$user.TimesResult] = Vector(
  TimesResult(1, 1, 1),
  TimesResult(1, 2, 2),
  TimesResult(1, 3, 3),
  TimesResult(1, 4, 4),
  TimesResult(1, 5, 5),
  TimesResult(2, 1, 2),
  TimesResult(2, 2, 4),
  TimesResult(2, 3, 6),
  TimesResult(2, 4, 8),
  TimesResult(2, 5, 10),
  TimesResult(3, 1, 3),
  TimesResult(3, 2, 6),
  TimesResult(3, 3, 9),
  TimesResult(3, 4, 12),
  TimesResult(3, 5, 15),
  TimesResult(4, 1, 4),
  TimesResult(4, 2, 8),
  TimesResult(4, 3, 12),
  TimesResult(4, 4, 16),
...
```

### 02.04

```scala
val squares = (1 to 10).map(i => i * i)

// Output

squares: collection.immutable.IndexedSeq[Int] = Vector(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
```

### 02.05

```scala
val squaresMap = (1 to 10).map(i => i -> (i * i)).toMap

// Output
squaresMap: scala.collection.immutable.Map[Int,Int] = Map(
  5 -> 25,
  10 -> 100,
  1 -> 1,
  6 -> 36,
  9 -> 81,
  2 -> 4,
  7 -> 49,
  3 -> 9,
  8 -> 64,
  4 -> 16
)
```

### 02.06

```scala
val timesTable = (1 to 5).map(i => (1 to 5).map (j => TimesResult(i, j, i * j)))

// Output

timesTable: collection.immutable.IndexedSeq[collection.immutable.IndexedSeq[TimesResult]] = Vector(
  Vector(
    TimesResult(1, 1, 1),
    TimesResult(1, 2, 2),
    TimesResult(1, 3, 3),
    TimesResult(1, 4, 4),
    TimesResult(1, 5, 5)
  ),
  Vector(
    TimesResult(2, 1, 2),
    TimesResult(2, 2, 4),
    TimesResult(2, 3, 6),
    TimesResult(2, 4, 8),
    TimesResult(2, 5, 10)
  ),
  Vector(
    TimesResult(3, 1, 3),
    TimesResult(3, 2, 6),
    TimesResult(3, 3, 9),
    TimesResult(3, 4, 12),
...
```

### 02.07

```scala

timesTable.flatten

// Output
res5: collection.immutable.IndexedSeq[TimesResult] = Vector(
  TimesResult(1, 1, 1),
  TimesResult(1, 2, 2),
  TimesResult(1, 3, 3),
  TimesResult(1, 4, 4),
  TimesResult(1, 5, 5),
  TimesResult(2, 1, 2),
  TimesResult(2, 2, 4),
  TimesResult(2, 3, 6),
  TimesResult(2, 4, 8),
  TimesResult(2, 5, 10),
  TimesResult(3, 1, 3),
  TimesResult(3, 2, 6),
  TimesResult(3, 3, 9),
  TimesResult(3, 4, 12),
  TimesResult(3, 5, 15),
  TimesResult(4, 1, 4),
  TimesResult(4, 2, 8),
  TimesResult(4, 3, 12),
  TimesResult(4, 4, 16),
...
```

### 02.08

```scala
val timesTableFlat = (1 to 5).flatMap(i => (1 to 5).map(j => TimesResult(i, j, i*j)))

// Output
timesTableFlat: collection.immutable.IndexedSeq[TimesResult] = Vector(
  TimesResult(1, 1, 1),
  TimesResult(1, 2, 2),
  TimesResult(1, 3, 3),
  TimesResult(1, 4, 4),
  TimesResult(1, 5, 5),
  TimesResult(2, 1, 2),
  TimesResult(2, 2, 4),
  TimesResult(2, 3, 6),
  TimesResult(2, 4, 8),
  TimesResult(2, 5, 10),
  TimesResult(3, 1, 3),
  TimesResult(3, 2, 6),
  TimesResult(3, 3, 9),
  TimesResult(3, 4, 12),
  TimesResult(3, 5, 15),
  TimesResult(4, 1, 4),
  TimesResult(4, 2, 8),
  TimesResult(4, 3, 12),
  TimesResult(4, 4, 16),
...
```

### 02.09

```scala

val timesTable = for {
    i <- 1 to 5 // flatMap
    j <- 1 to 5 // map
} yield TimesResult(i, j, i * j)

// Output
timesTableFlat: collection.immutable.IndexedSeq[TimesResult] = Vector(
  TimesResult(1, 1, 1),
  TimesResult(1, 2, 2),
  TimesResult(1, 3, 3),
  TimesResult(1, 4, 4),
  TimesResult(1, 5, 5),
  TimesResult(2, 1, 2),
  TimesResult(2, 2, 4),
  TimesResult(2, 3, 6),
  TimesResult(2, 4, 8),
  TimesResult(2, 5, 10),
  TimesResult(3, 1, 3),
  TimesResult(3, 2, 6),
  TimesResult(3, 3, 9),
  TimesResult(3, 4, 12),
  TimesResult(3, 5, 15),
  TimesResult(4, 1, 4),
  TimesResult(4, 2, 8),
  TimesResult(4, 3, 12),
  TimesResult(4, 4, 16),
...
```

### 02.10

```scala
for {
  i <- 1 to 3 // flatMap
  j <- 1 to 3 // flatMap
  k <- 1 to 3 // map
} yield i*j*k

// Output
res0: scala.collection.immutable.IndexedSeq[Int] = Vector(1, 2, 3, 2, 4, 6, 3, 6, 9, 2, 4, 6, 4, 8, 12, 6, 12, 18, 3, 6, 9, 6, 12, 18, 9, 18, 27)
```

## 03 - Options, options, options

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