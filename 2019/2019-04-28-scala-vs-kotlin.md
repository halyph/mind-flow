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
  - [Optional Value](#optional-value)
    - [Nullable Types](#nullable-types)
- [Pattern Matching](#pattern-matching)
  - [Destructuring](#destructuring)
- [Composition](#composition)
  - [Composition with Traits](#composition-with-traits)
  - [Composition with Delegation](#composition-with-delegation)
- [Extensions](#extensions)

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

### Optional Value

**Scala**

 Scala solves optionality with the `Option` type, which is well adopted in Scala APIs

```scala
case class Booking(destination: Option[Destination] = None)
case class Destination(hotel: Option[Hotel] = None)
case class Hotel(name: String, stars: Option[Int] = None)

// The functional approach 

val bOpt = Some(Booking(Some(Destination(Some(Hotel("Sunset Paradise", Some(5)))))))

var stars = "*" * bOpt.flatMap(_.destination).flatMap(_.hotel).flatMap(_.stars).getOrElse(0)

// or `for` expressions can be used to access optional values
stars = "*" * (for {
  booking <- bOpt
  dest <- booking.destination hotel <- dest.hotel
  stars <- hotel.stars
} yield stars).getOrElse(0)
```

Kotlin solves optionality on the language level with Nullable types. Every type can also be a Nullable Type: Syntax: <Typename>?

**Kotlin**

```kotlin
class Booking(val destination:Destination? = null)
class Destination(val hotel:Hotel? = null)
class Hotel(val name:String, val stars:Int? = null)
```

Since nullability is part of the type system no wrapper is needed: The required type or null can be used.

```kotlin
val booking:Booking? = Booking(Destination(Hotel("Sunset Paradise", 5))) 

// To safely access nullable types the ? can be used with ?: for the alternative case.
val stars = "*".repeat(booking?.destination?.hotel?.stars ?: 0) //-> "*****"

//  After checking for not null a type is ‘smart casted’ to its non-null type: here from Booking? to Booking
if(booking != null) {
  println(booking.destination)
}
```

#### Nullable Types

- At first awkward, but eventually they are great to work with
- Less verbose than Options on the declaration and usage side
- Offers much better interoperability with Java than Scala Options
- Most loved feature in Kotlin!

## Pattern Matching

**Scala**

```scala
def matchItAll(p: Any): Any = {
  p match {
    case x: Int                       => s"$x"            // (1)
    case "Scala"                      => "Scala"          // (2)
    case Seq(_, 3, _*)                => "Seq(?, 3, *)"   // (3)
    case head :: tail                 => s"$head $tail"   // (4)
    case (firstEl, _)                 => s"$firstEl"      // (5)
    case Some(s:Long)                 => s"Some Long $s"  // (6)
    case x: Int if 1 to 10 contains x => s"$x"            // (7)
    case x: String if x.endsWith("!") => s"$x"            // (8)
    case _                            => "The default"    // (9)
  }
}
```

**Kotlin**

```kotlin
fun matchItAll(p:Any?):Any =
  when(p) {
    is Int -> "$p" // Smart case to Int  // (1) ✅
    "Kotlin" -> "Kotlin"                 // (2) ✅
    // N/A                               // (3) ❌
    // N/A                               // (4) ❌
    Pair("literal", "only") -> "..."     // (5) ️️️🔶
    is Long? -> "null or Long"️           // (6) 🔶
    in 1..10 -> "Value in 1..10"         // (7) 🔶
    //                                   // (8) 🔶
    else -> "The default"                // (9) 🔶
```

`when` without arguments provides a more readable if else condition tree

```kotlin
fun matchItAll(p:Any?):Any = when {
  p is String && p.endsWith("!") ->"$p"
  else -> "The default" // No smart cast
}
```

### Destructuring

**Scala**

```scala
case class Person(name:String, age:Int)
val john = Person("John", 42)
val Person(name, age) = john

// ...

object Person {
  def unapply(person: Person): Option[(String, Int)] =
    Some((person.name, person.age))
}
```

Every class with an `unapply` method in Scala can be destructured. By default generated in case classes.

**Kotlin**

```kotlin
data class Person(val name:String, val age:Int)
val john = Person("John", 42)
val (name, age) = john // // Kotlin support destructuring too.

john.component1() //-> John
john.component2() //-> 45

// ...
fun component1() = name
fun component2() = age
```

For destructuring to work operator `component<extractor-param-nr>` methods need to be available, which are by default generated in data classes.

- Kotlin’s when is no ‘match’ for Scala’s Pattern Matching features
- No `PartialFunctions` support
- Destructuring allows not for Pattern Matching
- when is more of an advanced switch statement

## Composition

### Composition with Traits

**Scala**

```scala
abstract class Ship(var health: Int = 100)

trait Gun {
  val strength: Int = 1
  def fireAt(ship: Ship) = { ship.health -= (1 * strength) }
}

trait Medic {
  val lives: Int = 10
  def repair(ship: Ship) = { ship.health += lives }
}
```

Scala traits allow mixing in state and behavior a.o.

```scala
class Commander extends Ship() with Gun with Medic {
  val info = s"Gun strength: $strength, Medic capacity: $lives"
}
```

Besides state and behavior the mixed-in types are unified in the implementing class

```scala
val commander = new Commander()
commander.fireAt(...)
commander.strength            //-> 1
commander.isInstanceOf[Gun]   //-> true
commander.isInstanceOf[Medic] //-> true
```

### Composition with Delegation

**Kotlin**

```kotlin
abstract class Ship(var health:Int = 100)

interface Gun {
  val strength:Int
  fun fireAt(ship: Ship) { ship.health =- (1 * strength) } 
}

interface Medic {
  val lives:Int
  fun repair(ship:Ship) { ship.health =+ lives } 
}
```

Using `by`, all public members of the given interface will be delegated to its implementation
```kotlin
class LazerGun(override val strength: Int = 5) : Gun
class MinorRepair(override val lives: Int = 10) : Medic
class Commander(gun:Gun, repair:Medic): Ship(), Gun by gun, Medic by repair
```

```kotlin
val commander = Commander(LazerGun(), MinorRepair())
commander.fireAt(...)

// yielding more or less the same results like traits
commander.strength // -> 5
commander is Gun   // -> true
commander is Medic // -> true
```

## Extensions

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

**Scala**

```scala
```

**Kotlin**

```kotlin
```