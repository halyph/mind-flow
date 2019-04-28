# Scala vs Kotlin
> | java | kotlin | vs | comparison |

This page is just collection of notes from ["Kotlin vs Scala" by Urs Peter & Joost Heijkoop](https://www.youtube.com/watch?v=MsMejigb1Zk)

**Table of Contents**
- [Object Orientation](#object-orientation)
  - [Class](#class)
  - [Comparing OO between](#comparing-oo-between)
  - [Inheritance](#inheritance)
  - [Value Classes](#value-classes)
- [Functional Programming](#functional-programming)
  - [Declaring and Calling Functions](#declaring-and-calling-functions)
  - [Curring and partially applied functions](#curring-and-partially-applied-functions)
  - [Functions under the hood and Types](#functions-under-the-hood-and-types)
  - [Type Aliases](#type-aliases)
- [Null Safety](#null-safety)

---

## Object Orientation

### Class

**Scala**

```scala
class Person(val name:String, var age:Int = 0)
```

**Kotlin**

```kotlin
class Person(val name:String, var age:Int = 0)
```

### Comparing OO between

**Scala**

```scala
class Person(var name: String, var age: Int = 0) extends Ordered[Person] {
  
  def sayHi(): String = {
    "Hi"
  }
  
  override def compare(other: Person): Int = age - other.age

  def +(lifetime: Int): Person = {
    age += lifetime
    this
  }
}

object Person {
  def newBorn(name:String) = new Person(name, 0)
  def apply() = new Person("John Doe", -1)
}
```

**Kotlin**

```kotlin
class Person(var name: String, var age: Int = 0): Comparable<Person> {
  
  fun sayHi(): String {
    return "Hi"
  }

  operator fun plus(lifetime: Int): Person {
    age += lifetime
    return this
  }

  override operator fun compareTo(p: Person) = age - p.age
  
  companion object {
    fun newBorn(name:String) = Person(name)
    operator fun invoke() = Person("John Doe")
  }
}
```

### Inheritance

**Scala**

```scala
class Species(val kind:String) {
  def eats:Seq[String] = Seq()
}

class Person(val name:String, var age:Int) extends Species("Homo Sapiens") {
  override def eats:Seq[String] = Seq("...")
}
```

**Kotlin**

```kotlin
open class Species(val kind:String) {
  open fun eats():List<String> = emptyList()
}

class Person(val name:String, var age:Int = 0):Species("Homo Sapiens") {
  override fun eats():List<String> = listOf("...")
}
```

### Value Classes

**Scala**

```scala
case class Person(name:String, var age:Int = 0)
```

**Kotlin**

```kotlin
data class Person(val name:String, var age:Int = 0)
```

```java
val jack = Person("Jack", 42)
// jack: Person(name=Jack, age=32)

jack == Person("Jack", 42)
// res1: true

val fred = jack.copy(name = "Fred")
// fred: Person(name=Jack, age=32)
```

## Functional Programming

### Declaring and Calling Functions

**Scala**

```scala
def doWithText(path: File, transFun: (String) => String): String =
  transFun(FileUtils.readFileToString(path))

doWithText(new File("/news.txt"), txt => txt.toUpperCase())
doWithText(new File("/news.txt"), _.toUpperCase())


def writeToFile(file: File, block: => String) {
  if (file.isFile) FileUtils.writeStringToFile(file, block)
}

writeToFile(new File("/srocks.txt"), "Scala rocks! " * 1000)
```

**Kotlin**

```kotlin
fun doWithText(path: File, transFun: (String) -> String): String =
  transFun(FileUtils.readFileToString(path))

// On the call-side a function must be wrapped within {}
doWithText(File("/text.txt")){ txt -> txt.toUpperCase() }

// it serves as placeholder of the function parameter.
doWithText(File("/text.txt")){ it.toUpperCase() }

// Kotlin supports no-argument functions, similar to Scala’s call-by name arguments
fun writeToFile(file:File, block: () -> String) {
  if(file.isFile)FileUtils.writeStringToFile(file, block())
}

// On the call-side the empty argument and arrow can be omitted
writeToFile(File("/krocks.txt")){"Kotlin rocks! ".repeat(1000)}
```

### Curring and partially applied functions

**Scala**

```scala
def modN(n: Int)(x: Int) = ((x % n) == 0) 
val modTwo = modN(2)(_)
Seq(1,2,3) filter modTwo

val greaterThan100 = Math.max(100, _:Int) 
greaterThan100(200)
```

**Kotlin**

*Currying and partially applied functions are not available in Kotlin*

### Functions under the hood and Types

**Scala**

- Abstract Types
- Higher-kinded Types
- Type Classes, Phantom Types
- Structural Types
- Specialized Types
- Dynamic Types
- Self-Types
- Union Types

```scala
trait Function1[-T1, +R] extends AnyRef {
  def apply(v1: T1): R
}
```

**Kotlin**

Identical approach for Kotlin Functions, counting up to Function22 like Scala

Kotlin’s type features are identical to Java with the addition of Variance (contra-, co- invariant) and Type Aliases

```kotlin
interface Function1<in P1, out R> : Function<R> {
  operator fun invoke(p1: P1): R
}
```

### Type Aliases

**Scala**

```scala
type IntToStringFun = Function1[Int, String]
```

**Kotlin**

```kotlin
typealias IntToStringFun = Function1<Int, String>
```

## Null Safety

**Scala**

```scala
```

**Kotlin**

```kotlin
```

**Scala**

```scala
```

**Kotlin**

```kotlin
```