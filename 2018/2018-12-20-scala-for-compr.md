# Scala `for`-comprehensions
> | scala | video |

This is a complete copy of **Josh Suereth** & **Dick Wall** talk on *Scala World* conference: _"For: What is it good for? — Josh Suereth & Dick Wall"_ (see references).

Actually, I have found github repo with Jupiter notebooks. But, I don't like this format and decided to store these notes here.

- [References](#references)
- [01 - For "loops"](#01---for-%22loops%22)
- [02 - For with yield](#02---for-with-yield)
- [03 - Options](#03---options)
- [04 - Future](#04---future)
- [05 - Guards](#05---guards)
- [06 - Inline Assignments](#06---inline-assignments)
- [07 - Generators](#07---generators)
- [08 - For Grep and Glory](#08---for-grep-and-glory)
- [09 - Desugaring the fors](#09---desugaring-the-fors)
- [10 - Other Monads](#10---other-monads)

## References

- [Youtube: For: What is it good for? — Josh Suereth & Dick Wall](https://www.youtube.com/watch?v=WDaw2yXAa50)
- [Github: dickwall/use-the-fors-luke](https://github.com/dickwall/use-the-fors-luke) - soutse code realted to "For: What is it good for?" talk
- [Github: jsuereth/intro-to-fp](https://github.com/jsuereth/intro-to-fp) - This repo contains nice sample of "monadic" Github client

---

## 01 - For "loops"

### 01.01 <!-- omit in toc -->

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

### 01.02 <!-- omit in toc -->

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

### 01.03 <!-- omit in toc -->

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

### 01.04 <!-- omit in toc -->

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

### 01.05 <!-- omit in toc -->

```scala
(1 to 10)

// Output
res0: scala.collection.immutable.Range.Inclusive = Range 1 to 10
```

### 01.06 <!-- omit in toc -->

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

### 01.07 <!-- omit in toc -->

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

### 01.08 <!-- omit in toc -->

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

### 01.09 <!-- omit in toc -->

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

### 02.01 <!-- omit in toc -->

```scala
val squares = for (i <- 1 to 10) yield (i * i)

// Output
squares: collection.immutable.IndexedSeq[Int] = Vector(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
```

### 02.02 <!-- omit in toc -->

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

### 02.03 <!-- omit in toc -->

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

### 02.04 <!-- omit in toc -->

```scala
val squares = (1 to 10).map(i => i * i)

// Output

squares: collection.immutable.IndexedSeq[Int] = Vector(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
```

### 02.05 <!-- omit in toc -->

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

### 02.06 <!-- omit in toc -->

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

### 02.07 <!-- omit in toc -->

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

### 02.08 <!-- omit in toc -->

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

### 02.09 <!-- omit in toc -->

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

### 02.10 <!-- omit in toc -->

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

### 03.01 <!-- omit in toc -->

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

### 03.02 <!-- omit in toc -->

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

### 03.03 <!-- omit in toc -->

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

### 04.01 <!-- omit in toc -->

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

### 04.02 <!-- omit in toc -->

```scala
Await.result(f3, 11.seconds)
// Output
res3: Int = 42
```

### 04.03 <!-- omit in toc -->

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

### 05.01 <!-- omit in toc -->

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

### 05.02 <!-- omit in toc -->

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

### 05.03 <!-- omit in toc -->

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

### 05.04 <!-- omit in toc -->

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

### 06.01 <!-- omit in toc -->

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

### 06.02 <!-- omit in toc -->

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

### 06.03 <!-- omit in toc -->

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

### 06.04 <!-- omit in toc -->

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

### 07.01 <!-- omit in toc -->

```scala
for (i <- 1 to 5) yield i * i
// Output
res0: collection.immutable.IndexedSeq[Int] = Vector(1, 4, 9, 16, 25)
```

### 07.02 <!-- omit in toc -->

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

### 07.03 <!-- omit in toc -->

```scala
treasureMap.head match {
    case (stepNo, instruction) => println(s"Step $stepNo: $instruction")
}
// Output
Step 1: Go to island
```

### 07.04 <!-- omit in toc -->

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

### 07.05 <!-- omit in toc -->

```scala
val (stepNo, instruction) = treasureMap.head

// Output
stepNo: Int = 1
instruction: String = "Go to island"
```

### 07.06 <!-- omit in toc -->

```scala
val foo: Any = "foo"
val (stepNo, instruction) = foo

// Output
scala.MatchError: foo (of class java.lang.String) (foo (of class java.lang.String))
```

### 07.07 <!-- omit in toc -->

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

### 07.08 <!-- omit in toc -->

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

### 08.01 <!-- omit in toc -->

```scala
val filesHere = (new java.io.File(".")).listFiles
for (file <- filesHere if file.getName.endsWith(".ipynb"))
    println(file)
```

### 08.02 <!-- omit in toc -->

```scala
def fileLines(file: java.io.File) =
    scala.io.Source.fromFile(file).getLines.toList
```

### 08.03 <!-- omit in toc -->

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

### 09.01 <!-- omit in toc -->

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

### 09.02 <!-- omit in toc -->

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

### 09.03 <!-- omit in toc -->

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

### 09.04 <!-- omit in toc -->

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

### 10.01 <!-- omit in toc -->

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