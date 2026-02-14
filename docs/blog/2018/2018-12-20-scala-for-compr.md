# Scala `for`-comprehensions
<!-- tags: scala, video, functional programming -->

This is a complete copy of **Josh Suereth** & **Dick Wall** talk on *Scala World* conference: _"For: What is it good for? — Josh Suereth & Dick Wall"_ (see references).

Actually, I have found github repository with Jupiter notebooks. But, I don't like this format and decided to store these notes here.

- [References](#references)
- [01 - For "loops"](#01---for-loops)
- [02 - For with yield](#02---for-with-yield)
- [03 - Options](#03---options)
- [04 - Future](#04---future)
- [05 - Guards](#05---guards)
- [06 - Inline Assignments](#06---inline-assignments)
- [07 - Generators](#07---generators)
- [08 - For Grep and Glory](#08---for-grep-and-glory)
- [09 - Desugaring the fors](#09---desugaring-the-fors)
- [10 - Other Monads](#10---other-monads)
- [11 - `scala-arm`](#11---scala-arm)
- [12 - Monads don't mix](#12---monads-dont-mix)
- [13 - `Emm & M[_]`](#13---emm--m_)
- [14 - How to Option Your Futures](#14---how-to-option-your-futures)
- [15 - Sink](#15---sink)

## References

- [Youtube: For: What is it good for? — Josh Suereth & Dick Wall](https://www.youtube.com/watch?v=WDaw2yXAa50)
- [Github: dickwall/use-the-fors-luke](https://github.com/dickwall/use-the-fors-luke) - soutse code realted to "For: What is it good for?" talk
- [Github: jsuereth/intro-to-fp](https://github.com/jsuereth/intro-to-fp) - This repo contains nice sample of "monadic" Github client
- [Github: jsuereth/scala-arm](https://github.com/jsuereth/scala-arm) - This project aims to be the Scala Incubator project for Automatic-Resource-Management in the scala library 
- ["The Essence of the Iterator Pattern" post by *Eric Torreborre*](http://etorreborre.blogspot.com/2011/06/essence-of-iterator-pattern.html)

---

## 01 - For "loops"

### 01.01<!-- omit in toc -->

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

### 01.02<!-- omit in toc -->

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

### 01.03<!-- omit in toc -->

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

### 01.04<!-- omit in toc -->

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

### 01.05<!-- omit in toc -->

```scala
(1 to 10)

// Output
res0: scala.collection.immutable.Range.Inclusive = Range 1 to 10
```

### 01.06<!-- omit in toc -->

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

### 01.07<!-- omit in toc -->

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

### 01.08<!-- omit in toc -->

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

### 01.09<!-- omit in toc -->

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

### 02.01<!-- omit in toc -->

```scala
val squares = for (i <- 1 to 10) yield (i * i)

// Output
squares: collection.immutable.IndexedSeq[Int] = Vector(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
```

### 02.02<!-- omit in toc -->

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

### 02.03<!-- omit in toc -->

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

### 02.04<!-- omit in toc -->

```scala
val squares = (1 to 10).map(i => i * i)

// Output

squares: collection.immutable.IndexedSeq[Int] = Vector(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
```

### 02.05<!-- omit in toc -->

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

### 02.06<!-- omit in toc -->

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

### 02.07<!-- omit in toc -->

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

### 02.08<!-- omit in toc -->

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

### 02.09<!-- omit in toc -->

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

### 02.10<!-- omit in toc -->

```scala
for {
  i <- 1 to 3 // flatMap
  j <- 1 to 3 // flatMap
  k <- 1 to 3 // map
} yield i*j*k

// Output
res0: scala.collection.immutable.IndexedSeq[Int] = Vector(1, 2, 3, 2, 4, 6, 3, 6, 9, 2, 4, 6, 4, 8, 12, 6, 12, 18, 3, 6, 9, 6, 12, 18, 9, 18, 27)
```

## 03 - Options

### 03.01<!-- omit in toc -->

```scala
val x = 1
val y = 2
val z = 3

// Output
val result = x * y * z
x: Int = 1
y: Int = 2
z: Int = 3
result: Int = 6
```

### 03.02<!-- omit in toc -->

```scala
val ox = Some(1)
val oy = Some(2)
val oz = Some(3)

val oResult = for {
  x <- ox
  y <- oy
  z <- oz
} yield {
  x * y * z
}

// Output
ox: Some[Int] = Some(1)
oy: Some[Int] = Some(2)
oz: Some[Int] = Some(3)
oResult: Option[Int] = Some(6)
```

### 03.03<!-- omit in toc -->

```scala
val ox = Some(1)
val oy: Option[Int] = None
val oz = Some(3)

val oResult = for {
  x <- ox
  y <- oy
  z <- oz
} yield {
  x * y * z
}

// Output
ox: Some[Int] = Some(1)
oy: Option[Int] = None
oz: Some[Int] = Some(3)
oResult: Option[Int] = None
```

## 04 - Future

### 04.01<!-- omit in toc -->

```scala
import scala.concurrent._
import ExecutionContext.Implicits.global
import duration._

val f1 = Future { Thread.sleep(10000); 6 }
val f2 = Future { Thread.sleep(10000); 7 }

val f3 = for {
    x <- f1
    y <- f2
} yield x * y

f3.value

// Output
f1: Future[Int] = List(scala.concurrent.impl.CallbackRunnable@5e5167e0)
f2: Future[Int] = List()
f3: Future[Int] = List()
res2_3: Option[scala.util.Try[Int]] = None
```

### 04.02<!-- omit in toc -->

```scala
Await.result(f3, 11.seconds)
// Output
res3: Int = 42
```

### 04.03<!-- omit in toc -->

```scala
val f1 = Future { Thread.sleep(1000); 6 }
val f2 = Future { Thread.sleep(1000); 7 / 0 }

val f3 = for {
    x <- f1
    y <- f2
} yield x * y

f3.value
Await.result(f3, 2.seconds)

// Output
res0: Option[scala.util.Try[Int]] = None

java.lang.ArithmeticException: / by zero
at .$anonfun$f2$1(<console>:18)
at scala.runtime.java8.JFunction0$mcI$sp.apply(JFunction0$mcI$sp.java:23)
at scala.concurrent.Future$.$anonfun$apply$1(Future.scala:658)
at scala.util.Success.$anonfun$map$1(Try.scala:255)
at scala.util.Success.map(Try.scala:213)
at scala.concurrent.Future.$anonfun$map$1(Future.scala:292)
at scala.concurrent.impl.Promise.liftedTree1$1(Promise.scala:33)
at scala.concurrent.impl.Promise.$anonfun$transform$1(Promise.scala:33)
at scala.concurrent.impl.CallbackRunnable.run(Promise.scala:64)
at java.util.concurrent.ForkJoinTask$RunnableExecuteAction.exec(ForkJoinTask.java:1402)
at java.util.concurrent.ForkJoinTask.doExec(ForkJoinTask.java:289)
at java.util.concurrent.ForkJoinPool$WorkQueue.runTask(ForkJoinPool.java:1056)
at java.util.concurrent.ForkJoinPool.runWorker(ForkJoinPool.java:1692)
at java.util.concurrent.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:157)
```

## 05 - Guards

### 05.01<!-- omit in toc -->

```scala
for {
    x <- 1 to 10
    y <- 1 to 10
    if x % 4 < y % 5
    if x % 2 == 0
} yield x * y

// Output
res0: collection.immutable.IndexedSeq[Int] = Vector(
  6,
  8,
  16,
  18,
  4,
  8,
  12,
  16,
  24,
  28,
  32,
  36,
  18,
  24,
  48,
  54,
  8,
  16,
  24,
...
```

### 05.02<!-- omit in toc -->

```scala
for {
    i <- 1 to 10
    j <- 1 to 10
    if i % 3 == 0 || j % 3 == 0
    k <- 1 to 10
    if i * j * k % 2 == 0
} yield i * j * k

// Output
res1: collection.immutable.IndexedSeq[Int] = Vector(
  6,
  12,
  18,
  24,
  30,
  6,
  12,
  18,
  24,
  30,
  36,
  42,
  48,
  54,
  60,
  18,
  36,
  54,
  72,
...
```

### 05.03<!-- omit in toc -->

```scala
(1 to 10).flatMap { i =>
  (1 to 10).withFilter(j => i % 3 == 0 || j % 3 == 0).flatMap { j =>
    (1 to 10).withFilter(k => i * j * k % 2 == 0).map { k =>
      i * j * k
    }
  }
}

// Output
res2: collection.immutable.IndexedSeq[Int] = Vector(
  6,
  12,
  18,
  24,
  30,
  6,
  12,
  18,
  24,
  30,
  36,
  42,
  48,
  54,
  60,
  18,
  36,
  54,
  72,
...
```

### 05.04<!-- omit in toc -->

```scala
for {
    i <- 1 to 10
    j <- 1 to 10
    if i % 3 == 0 || j % 3 == 0
    k <- 1 to 10
    if i * j * k % 2 == 0
} yield i * j * k

// Output
res3: collection.immutable.IndexedSeq[Int] = Vector(
  6,
  12,
  18,
  24,
  30,
  6,
  12,
  18,
  24,
  30,
  36,
  42,
  48,
  54,
  60,
  18,
  36,
  54,
  72,
...
```

## 06 - Inline Assignments

### 06.01<!-- omit in toc -->

```scala
for {
    i <- 1 to 10
    j <- 1 to 10
    if i % 3 == 0 || j % 3 == 0
    k <- 1 to 10
    if i * j * k % 2 == 0
} yield i * j * k  // why repeat this?

// Output
res0: collection.immutable.IndexedSeq[Int] = Vector(
  6,
  12,
  18,
  24,
  30,
  6,
  12,
  18,
  24,
  30,
  36,
  42,
  48,
  54,
  60,
  18,
  36,
  54,
  72,
...
```

### 06.02<!-- omit in toc -->

```scala
for {
    i <- 1 to 10
    j <- 1 to 10
    if i % 3 == 0 || j % 3 == 0
    
    k <- 1 to 10
    
    mult = i * j * k
    if mult % 2 == 0
} yield mult

// Output
res1: collection.immutable.IndexedSeq[Int] = Vector(
  6,
  12,
  18,
  24,
  30,
  6,
  12,
  18,
  24,
  30,
  36,
  42,
  48,
  54,
  60,
  18,
  36,
  54,
  72,
...
```

### 06.03<!-- omit in toc -->

```scala
(1 to 10).flatMap { i =>
  (1 to 10).withFilter(j => i % 3 == 0 || j % 3 == 0).flatMap { j =>
    (1 to 10).map { k =>
      val mult = i * j * k
     (k, mult)
    }.withFilter { 
      case (k, mult) => mult % 2 == 0 
    }.map { 
      case(k, mult) => mult
    }
  }
}

// Output
res0: scala.collection.immutable.IndexedSeq[Int] = Vector(6, 12, 18, 24, 30, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 18, 36, 54, 72, 90, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 18, 36, 54, 72, 90, 108, 126, 144, 162, 180, 6, 12, 18, 24, 30, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 18, 36, 54, 72, 90, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 30, 60, 90, 120, 150, 18, 36, 54, 72, 90, 108, 126, 144, 162, 180, 42, 84, 126, 168, 210, 24, 48, 72, 96, 120, 144, 168, 192, 216, 240, 54, 108, 162, 216, 270, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 24, 48, 72, 96, 120, 144, 168, 192, 216, 240, 36, 72, 108, 144, 180, 216, 252, 288, 324, 360, 30, 60, 90, 120, 150, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 90,...
```

### 06.04<!-- omit in toc -->

```scala
// what else can we do with assiGnments?
val mults = for {
    i <- 1 to 5
    _ = println(s"i is $i")   // or logger.info(s"$i") - SIDE EFFECTS!
    j <- 1 to 5
} yield i * j

// Output
i is 1
i is 2
i is 3
i is 4
i is 5
mults: collection.immutable.IndexedSeq[Int] = Vector(
  1,
  2,
  3,
  4,
  5,
  2,
  4,
  6,
  8,
  10,
  3,
  6,
  9,
  12,
  15,
  4,
  8,
  12,
  16,
...
```

## 07 - Generators

### 07.01<!-- omit in toc -->

```scala
for (i <- 1 to 5) yield i * i
// Output
res0: collection.immutable.IndexedSeq[Int] = Vector(1, 4, 9, 16, 25)
```

### 07.02<!-- omit in toc -->

```scala
val treasureMap = Map(
  1 -> "Go to island",
  2 -> "Find big X on ground",
  3 -> "Dig to find treasure"
)

for ((stepNo, instruction) <- treasureMap) {
    println(s"Step $stepNo: $instruction")
}

// Output
Step 1: Go to island
Step 2: Find big X on ground
Step 3: Dig to find treasure
treasureMap: Map[Int, String] = Map(
  1 -> "Go to island",
  2 -> "Find big X on ground",
  3 -> "Dig to find treasure"
)
```

### 07.03<!-- omit in toc -->

```scala
treasureMap.head match {
    case (stepNo, instruction) => println(s"Step $stepNo: $instruction")
}
// Output
Step 1: Go to island
```

### 07.04<!-- omit in toc -->

```scala
treasureMap.map {
    case (stepNo, instruction) => println(s"Step $stepNo: $instruction")
}

// Output
Step 1: Go to island
Step 2: Find big X on ground
Step 3: Dig to find treasure
res3: collection.immutable.Iterable[Unit] = List((), (), ())
```

### 07.05<!-- omit in toc -->

```scala
val (stepNo, instruction) = treasureMap.head

// Output
stepNo: Int = 1
instruction: String = "Go to island"
```

### 07.06<!-- omit in toc -->

```scala
val foo: Any = "foo"
val (stepNo, instruction) = foo

// Output
scala.MatchError: foo (of class java.lang.String) (foo (of class java.lang.String))
```

### 07.07<!-- omit in toc -->

```scala
case class Person(first: String, last: String, age: Int)

val people = Seq(
  Person("Harry", "Potter", 30), 
  Person("Hermione", "Weasley", 30), 
  Person("Ginny", "Potter", 28))

for (Person(first, last, age) <- people) println(s"Amazingly, $first $last is now $age years old")

println("Are you feeling old yet?")

// Output
Amazingly, Harry Potter is now 30 years old
Amazingly, Hermione Weasley is now 30 years old
Amazingly, Ginny Potter is now 28 years old
Are you feeling old yet?
defined class Person
people: Seq[$user.Person] = List(
  Person("Harry", "Potter", 30),
  Person("Hermione", "Weasley", 30),
  Person("Ginny", "Potter", 28)
)
```

### 07.08<!-- omit in toc -->

```scala
object Even {
  def unapply(x: Int): Boolean = x % 2 == 0
}

for {
  x @ Even() <- 1 to 100
} yield x

// Output
defined object Even
res7_1: collection.immutable.IndexedSeq[Int] = Vector(
  2,
  4,
  6,
  8,
  10,
  12,
  14,
  16,
  18,
  20,
  22,
  24,
  26,
  28,
  30,
  32,
  34,
  36,
  38,
...
```

## 08 - For Grep and Glory

### 08.01<!-- omit in toc -->

```scala
val filesHere = (new java.io.File(".")).listFiles
for (file <- filesHere if file.getName.endsWith(".ipynb"))
    println(file)
```

### 08.02<!-- omit in toc -->

```scala
def fileLines(file: java.io.File) =
    scala.io.Source.fromFile(file).getLines.toList
```

### 08.03<!-- omit in toc -->

```scala
val grepResults = for {
  file     <- filesHere
  if file.getName.endsWith(".ipynb")
  line     <- fileLines(file)
  trimmed  =  line.trim
  if trimmed.length > 25
  if trimmed.matches(".*for.*")
} yield trimmed.length -> trimmed

grepResults foreach println
```

## 09 - Desugaring the fors

### 09.01<!-- omit in toc -->

```scala
object ForExpansion1 {
  val mults = for {
    i <- 1 to 3 // flatMap
    j <- 1 to 3 // flatMap
    k <- 1 to 3 // map
  } yield i*j*k
}
```

```
// Output
$ scalac -Xprint:parser  ForExpansion1.scala 
[[syntax trees at end of                    parser]] // ForExpansion1.scala
package <empty> {
  object ForExpansion1 extends scala.AnyRef {
    def <init>() = {
      super.<init>();
      ()
    };
    val mults = 1.to(3).flatMap(((i) => 1.to(3).flatMap(((j) => 1.to(3).map(((k) => i.$times(j).$times(k)))))))
  }
}
```

### 09.02<!-- omit in toc -->

```scala
object ForExpansion2 {
  val mults = for {
    i <- 1 to 10
    j <- 1 to 10
    if i % 3 == 0 || j % 3 == 0
    k <- 1 to 10
    if i * j * k % 2 == 0
  } yield i * j * k
}
```

```
// Output
$ scalac -Xprint:parser  ForExpansion2.scala 
[[syntax trees at end of                    parser]] // ForExpansion2.scala
package <empty> {
  object ForExpansion2 extends scala.AnyRef {
    def <init>() = {
      super.<init>();
      ()
    };
    val mults = 1.to(10).flatMap(((i) => 1.to(10).withFilter(((j) => i.$percent(3).$eq$eq(0).$bar$bar(j.$percent(3).$eq$eq(0)))).flatMap(((j) => 1.to(10).withFilter(((k) => i.$times(j).$times(k).$percent(2).$eq$eq(0))).map(((k) => i.$times(j).$times(k)))))))
  }
}
```

### 09.03<!-- omit in toc -->

```scala
object ForExpansion3 {
  val mults = for {
    i <- 1 to 10
    j <- 1 to 10
    if i % 3 == 0 || j % 3 == 0
    k <- 1 to 10
    mult = i * j * k
    if mult % 2 == 0
  } yield mult
}
```

```
// Output
$ scalac -Xprint:parser  ForExpansion3.scala 
[[syntax trees at end of                    parser]] // ForExpansion3.scala
package <empty> {
  object ForExpansion3 extends scala.AnyRef {
    def <init>() = {
      super.<init>();
      ()
    };
    val mults = 1.to(10).flatMap(((i) => 1.to(10).withFilter(((j) => i.$percent(3).$eq$eq(0).$bar$bar(j.$percent(3).$eq$eq(0)))).flatMap(((j) => 1.to(10).map(((k) => {
  val mult = i.$times(j).$times(k);
  scala.Tuple2(k, mult)
})).withFilter(((x$1) => x$1: @scala.unchecked match {
  case scala.Tuple2((k @ _), (mult @ _)) => mult.$percent(2).$eq$eq(0)
})).map(((x$2) => x$2: @scala.unchecked match {
      case scala.Tuple2((k @ _), (mult @ _)) => mult
    }))))))
  }
}
```

### 09.04<!-- omit in toc -->

```
$ scalac -Xshow-phases
    phase name  id  description
    ----------  --  -----------
        parser   1  parse source into ASTs, perform simple desugaring
         namer   2  resolve names, attach symbols to named trees
packageobjects   3  load package objects
         typer   4  the meat and potatoes: type the trees
        patmat   5  translate match expressions
superaccessors   6  add super accessors in traits and nested classes
    extmethods   7  add extension methods for inline classes
       pickler   8  serialize symbol tables
     refchecks   9  reference/override checking, translate nested objects
       uncurry  10  uncurry, translate function values to anonymous classes
     tailcalls  11  replace tail calls by jumps
    specialize  12  @specialized-driven class and method specialization
 explicitouter  13  this refs to outer pointers
       erasure  14  erase types, add interfaces for traits
   posterasure  15  clean up erased inline classes
      lazyvals  16  allocate bitmaps, translate lazy vals into lazified defs
    lambdalift  17  move nested functions to top level
  constructors  18  move field definitions into constructors
       flatten  19  eliminate inner classes
         mixin  20  mixin composition
       cleanup  21  platform-specific cleanups, generate reflective calls
    delambdafy  22  remove lambdas
         icode  23  generate portable intermediate code
           jvm  24  generate JVM bytecode
      terminal  25  the last phase during a compilation run
```

## 10 - Other Monads

### 10.01<!-- omit in toc -->

```scala
val e1: Either[String, Int] = Right(6)
val e2: Either[String, Int] = Right(7)

for {
    x <- e1.right
    y <- e2.right
} yield x * y

// Output
e1: Either[String, Int] = Right(6)
e2: Either[String, Int] = Right(7)
res0_2: Either[String, Int] = Right(42)
```

### 10.02<!-- omit in toc -->

```scala
val e1: Either[String, Int] = Right(6)
val e2: Either[String, Int] = Left("Bad Number")

for {
    x <- e1.right
    y <- e2.right
} yield x * y

// Output
e1: Either[String, Int] = Right(6)
e2: Either[String, Int] = Left("Bad Number")
res1_2: Either[String, Int] = Left("Bad Number")
```

### 10.03<!-- omit in toc -->

```scala
// add to classpath:
// ----
// classpath.add("org.scalactic" %% "scalactic" % "3.0.0")
// ----

import org.scalactic._

def parseName(input: String): String Or ErrorMessage = {
  val trimmed = input.trim
  if (!trimmed.isEmpty) Good(trimmed) else Bad(s""""${input}" is not a valid name""")
}

def parseAge(input: String): Int Or ErrorMessage = {
  try {
    val age = input.trim.toInt
    if (age >= 0) Good(age) else Bad(s""""${age}" is not a valid age""")
  }
  catch {
    case _: NumberFormatException => Bad(s""""${input}" is not a valid integer""")
  }
}

case class Person(name: String, age: Int)

def parsePerson(inputName: String, inputAge: String): Person Or ErrorMessage =
  for {
    name <- parseName(inputName)
    age <- parseAge(inputAge)
  } yield Person(name, age)

parsePerson("Sally", "25")
parsePerson("     ", "22")
parsePerson("Sally", "twenty eight")

// Output
res5_0: Or[Person, ErrorMessage] = Good(Person("Sally", 25))
res5_1: Or[Person, ErrorMessage] = Bad(
  """
"     " is not a valid name
  """
)
res5_2: Or[Person, ErrorMessage] = Bad(
  """
twenty eight" is not a valid integer
  """
)
```

### 10.04<!-- omit in toc -->

```scala
// add to classpath:
// ----
// classpath.add("org.typelevel" %% "cats" % "0.7.2")
// ----

import cats.data._

type IndexState[A] = State[Int, A]
// This returns a next `State` and the index to use for the current node.

def nextIdx: State[Int, Int] =
  State { currentIndex =>
    (currentIndex + 1, currentIndex)
  }

val program: State[Int, (Int, Int, Int)] = 
 for {
   x <- nextIdx
   y <- nextIdx
   z <- nextIdx
 } yield (x,y,z)

program.run(1).value
```

## 11 - `scala-arm`

```scala
// add to classpath:
// ----
// classpath.add("com.jsuereth" %% "scala-arm" % "1.4")
// ----

import java.io._
import resource._
// Copy input into output.
for {
  input  <- managed(new java.io.FileInputStream("test.txt"))
  output <- managed(new java.io.FileOutputStream("test2.txt"))
} {
  val buffer = new Array[Byte](512)
  def read(): Unit = input.read(buffer) match {
    case -1 => ()
    case  n =>
      output.write(buffer,0,n)
      read()
  }
  read()
}
```

## 12 - Monads don't mix

### 12.01<!-- omit in toc -->

```scala
case class Passenger(name: String, cellPhoneNumber: Option[String])
case class Carriage(passengers: List[Passenger])
case class Train(name: String, carriages: List[Carriage])
case class Route(name: String, activeTrain: Option[Train])

val route1 = Route("Glen Gach to Glen Pach",
  Some(Train("The Flying Scotsman",
    List(Carriage(List(
                    Passenger("Rob Roy", Some("121-212-1212")), 
                    Passenger("Connor McCleod", None))),
      Carriage(List(Passenger("Joey McDougall", Some("454-545-4545")))))
  ))
)

val route2 = Route("Defuncto 1", None)

val route3 = Route("Busy Route of Luddites",
  Some(Train("The Tech Express",
    List(Carriage(List(
                    Passenger("Ug", None), Passenger("Glug", None))),
      Carriage(Nil),
      Carriage(List(Passenger("Smug", Some("323-232-3232")))))
  ))
)

val routes = List(route1, route2, route3)

// ---

for {
  route <- routes
  active <- route.activeTrain   // huh!
  carriage <- active.carriages
  passenger <- carriage.passengers
  number <- passenger.cellPhoneNumber
} yield number


// Output
Main.scala:28: type mismatch;
 found   : List[String]
 required: Option[?]
    carriage <- active.carriages
             ^
```

### 12.02<!-- omit in toc -->

```scala
routes.flatMap { route =>  // Seq  (flatMap A => Seq[B])
    route.activeTrain.flatMap { active =>  // Option  (flatMap A => Option[B]) // these two
        active.carriages.flatMap { carriage =>  // Seq  (flatMap A => Seq[B])  // are the problem...
            carriage.passengers.flatMap { passenger =>  // Seq
                passenger.cellPhoneNumber.map { number =>  // Option
                    number
                }
            }
        }
    }
}

// Output
Main.scala:27: type mismatch;
 found   : List[String]
 required: Option[?]
        active.carriages.flatMap { carriage =>  // Seq  (flatMap A => Seq[B])  // are the problem...
                                 ^
```

### 12.03<!-- omit in toc -->

```scala
for {
    route <- routes
    active <- route.activeTrain.toSeq   // recommended whenever mixing options and seqs
    carriage <- active.carriages
    passenger <- carriage.passengers
    number <- passenger.cellPhoneNumber.toSeq  // unnecessary here, but still clear
} yield number

// Output
res2: List[String] = List("121-212-1212", "454-545-4545", "323-232-3232")
```

### 12.04<!-- omit in toc -->

```scala
import scala.concurrent._
import ExecutionContext.Implicits.global
import duration._

val fListONums = Future(List(1,2,3,4,5))
def square(x: Int): Future[Int] = Future(x * x)

for {
    nums <- fListONums
    num <- nums    // doh! - no mixie!
    sq <- square(num)
} yield sq

// Output
Main.scala:43: type mismatch;
 found   : scala.concurrent.Future[Int]
 required: scala.collection.GenTraversableOnce[?]
    sq <- square(num)
       ^
Main.scala:42: type mismatch;
 found   : List[Nothing]
 required: scala.concurrent.Future[?]
    num <- nums    // doh! - no mixie!
        ^
```

### 12.05<!-- omit in toc -->

```scala
val fListONums = Future(List(1,2,3,4,5))
def square(x: Int): Future[Int] = Future(x * x)

for {
    nums <- fListONums
    squares <- Future.traverse(nums)(x => square(x))  // Seq[Int] & Int => Future[Int] => Future[Seq[Int]]
} yield squares

// Output
fListONums: Future[List[Int]] = Success(List(1, 2, 3, 4, 5))
res4_2: Future[List[Int]] = Success(List(1, 4, 9, 16, 25))
```

## 13 - `Emm & M[_]`

### 13.01<!-- omit in toc -->

```scala
// classpath.addRepository("https://dl.bintray.com/djspiewak/maven")
// classpath.add("com.codecommit" %% "emm-cats" % "0.2.1")
// ---

import emm._
import emm.compat.cats._
import cats.std.list._
import cats.std.option._
import cats.std.future._
import scala.concurrent.{Await, Future}
import scala.concurrent.duration._

implicit val ec = scala.concurrent.ExecutionContext.global

type E = Future |: Option |: Base

val effect1 = Option(3).liftM[E]

val effect2 = Option(2).liftM[E]
//val effect2 = (None: Option[Int]).liftM[E]

val effect3 = Future { Thread.sleep(5000); 7}.liftM[E]

val effect4 = for {
  x <- effect1
  y <- effect2
  z <- effect3
} yield x * y * z

effect4.run.value

effect1
effect2
effect3

Await.result(effect4.run, 10 seconds)
```

## 14 - How to Option Your Futures

### 14.01<!-- omit in toc -->

```scala
import scala.concurrent._
import scala.concurrent.ExecutionContext.Implicits.global
import duration._

val f1 = Future(10)
val o2 = Option(20)
val f3 = Future(30)

val result = for {
    x <- f1
    y <- o2
    z <- f3
} yield x * y * z  // Sad Vader...

// Output
Main.scala:44: type mismatch;
 found   : scala.concurrent.Future[Int]
 required: Option[?]
    z <- f3
      ^
Main.scala:43: type mismatch;
 found   : Option[Nothing]
 required: scala.concurrent.Future[?]
    y <- o2
      ^
```

### 14.02<!-- omit in toc -->

```scala
val result = for {
    x   <- f1
    z   <- f3
    res =  for (y <- o2) yield x * y * z
} yield res

Await.result(result, 1.second)

// Output
result: Future[Option[Int]] = Success(Some(6000))
res2_1: Option[Int] = Some(6000)
```

### 14.03<!-- omit in toc -->

```scala
def multOptions(o1: Option[Int], o2: Option[Int], o3: Option[Int]): Option[Int] =
  for {
    x <- o1
    y <- o2
    z <- o3
  } yield x * y * z

val result = for {
    v1 <- f1
    v3 <- f3
} yield multOptions(Some(v1), o2, Some(v3))

Await.result(result, 1.second)

// Output
result: Future[Option[Int]] = Success(Some(6000))
res3_2: Option[Int] = Some(6000)
```

## 15 - Sink

### 15.01<!-- omit in toc -->

```scala
trait Sink[To] { sink =>
  def apply(t: To): Unit
  final def stage[E]: StagedSink[E, E, To] = StagedSink(StagedSink.stagedIdentity[E], this)
}

final case class StagedSink[First,Current,Final](staged: First => Traversable[Current], sink: Sink[Final]) {
  def map[B, To](f: Current => B)(implicit isDone: CanSink[First, B, Final, To]): To = isDone.result(this, f)
  def flatMap[B, To](f: Current => TraversableOnce[B])(implicit isDone: CanSink[First, B, Final, To]): To = isDone.result2(this, f)
  def withFilter(f: Current => Boolean): StagedSink[First, Current,Final] =
    StagedSink(staged andThen { xs => 
       for(x <- xs; if f(x)) yield x
    }, sink)
}

object StagedSink {
  def stagedIdentity[E]: E => Traversable[E] = (e: E) => List(e)
}

trait CanSink[First, Now, Final, To] {
  def result[E](in: StagedSink[First, E, Final], f: E => Now): To
  def result2[E](in: StagedSink[First, E, Final], f: E => TraversableOnce[Now]): To
}

trait LowPrioritySinkImplicits {
  implicit def sinkChain[First, Now, Final]: CanSink[First, Now, Final, StagedSink[First, Now, Final]] =
    new CanSink[First,Now, Final, StagedSink[First, Now, Final]] {
      def result[E](in: StagedSink[First, E, Final], f: E => Now): StagedSink[First, Now, Final] =
        StagedSink(in.staged andThen (x => x map f), in.sink)
      def result2[E](in: StagedSink[First, E, Final], f: E => TraversableOnce[Now]): StagedSink[First, Now, Final] =
        StagedSink(in.staged andThen (x => x flatMap f), in.sink)
    }
}

object CanSink extends LowPrioritySinkImplicits {
  implicit def finalSink[First, E]: CanSink[First, E,E, Sink[First]] =
    new CanSink[First, E,E, Sink[First]] {
      def result[A](ss: StagedSink[First, A, E], f: A => E): Sink[First] =
        new Sink[First] {
          def apply(in: First): Unit = {
            val staged = ss.staged.andThen { xs => xs map f }
            for { x <- staged(in) } ss.sink(x)
          }
        }
      def result2[A](ss: StagedSink[First, A, E], f: A => TraversableOnce[E]): Sink[First] =
        new Sink[First] {
          def apply(in: First): Unit = {
            val staged = ss.staged.andThen { xs => xs flatMap f }
            for { x <- staged(in) } ss.sink(x)
          }
        }
    }

}
```

### 15.02<!-- omit in toc -->

```scala
case class User(name: String, city: String) {
     def livesIn(in: String): Boolean = city == in
  }

  object stdout extends  Sink[String] {
     override def apply(in: String): Unit = System.out.println(in);
  }

  def userSink: Sink[User] =  
    for {
      user <- stdout.stage[User]
      if user livesIn "pittsburgh"
    } yield user.name


  for {
     user <- List(User("josh", "pittsburgh"), User("dick","morgan hill"))
  }  userSink(user)

// Output
josh
defined class User
defined object stdout
defined function userSink
```
