# Scala vs Kotlin
> | java | kotlin | vs | comparison |

This page is just collection of notes from ["Kotlin vs Scala" by Urs Peter & Joost Heijkoop](https://www.youtube.com/watch?v=MsMejigb1Zk)

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
  - [Extensions ++ (Function types with receiver)](#extensions--function-types-with-receiver)
- [Collections](#collections)
  - [Collection Examples](#collection-examples)
- [Concurrency](#concurrency)
  - [Scala Futures](#scala-futures)
  - [Kotlin Coroutines](#kotlin-coroutines)
    - [Kotlin Coroutines to the rescue](#kotlin-coroutines-to-the-rescue)
    - [Kotlin Coroutines under the hood](#kotlin-coroutines-under-the-hood)
    - [Kotlin Coroutines Interoperability](#kotlin-coroutines-interoperability)
  - [Some final words on Coroutines](#some-final-words-on-coroutines)

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

Scala `implicits` are a (too?) powerful language feature which allows implementing a variety of patterns:

- Extensions for existing classes (implicit classes)
- Implicit contexts (implicit parameters)
- Implicit conversions (implicit methods)
- Type-classes (Context Bounds)

Kotlin’s extension mechanism is more limited and similar to:

- Extensions for existing classes

**Scala**

```scala
implicit class RichInt(val value:Int) extends AnyVal {
  def square = value * value
}

2.square //-> 4
```

**Kotlin**

The syntax for an extension is: `<type-to-extend>.methodName() {...}`.
The type to extend can also be a generic

```kotlin
// this refers to the instance of the extended class
fun Int.square(): Int = this * this

2.square() //-> 4
```

```kotlin
listOf(1,2,3).sum()  // Convenience methods on Collections

listOf("a", "a", "a").map{it.toUpperCase()}  // Higher-Order Functions

"hi".reversed() // Convenience methods on Collections

File("/tmp.txt").useLines {
  lines -> lines.joinToString(" ") // Loans on IO APIs
}

val x:Int? = null
x?.let{ it * it} ?: -1 // counterpart of Scala’s Option.map(...)
```

### Extensions ++ (Function types with receiver)

Kotlin supports *Function Types with Receiver* which are the key ingredient for *type safe builders and DSLs*.

**Kotlin**

```kotlin
class PersonBuilder(var name:String? = null, var age:Int? = null) {
  fun toPerson() = Person(name ?: "John Doe", age ?: 0)
}

// Function Types with Receiver
// read like: when invoking create() on PersonBuilder, the builder instance is provided
fun person(create:PersonBuilder.() -> Unit):Person {
  val builder = PersonBuilder()
  builder.create()
  return builder.toPerson()
}
```

Consequently, DSL-like syntax can be used to create complex objects

```kotlin
person {
  name = "Super Trooper"
  age = 42
}
```

Example Spring’s Routing DSL solely built on Extensions

```kotlin
router { 
  accept(TEXT_HTML).nest {
    GET("/") { ok().render("index") }
    GET("/sse") { ok().render("sse") }
    GET("/users", userHandler::findAllView)
  }
  "/api".nest {
    accept(APPLICATION_JSON).nest {
      GET("/users", userHandler::findAll)
    }
  accept(TEXT_EVENT_STREAM).nest {
    GET("/users", userHandler::stream) }
  }
  resources("/**", ClassPathResource("static/"))
}
```

## Collections

**Scala** created its own (very advanced) mutable, immutable and parallel collections

- `Vector`, `List`, `Stream`, `Map`, `Set` etc.
- Scala collections can be extended with little effort
- Interoperability with Java is achieved with implicit conversions `scala.collection.JavaConversions`

**Kotlin** relies - for the time being - on Java collections with some additions:

- Builder methods: `listOf(1,2,3)`, `mapOf("a" to 1)`
- Rich set of higher-order functions (`zip`, `windowed`, `fold`)
- Additions on numeric collections (`sum()`, `average()`)
- Immutable Views on mutable collections

### Collection Examples

**Scala**

```scala
// (1) Immutable coll. (default)
val l = Seq(1,2,3)
val l2 = l :+ 4
// l -> 1,2,3
// l 2 -> 1,2,3,4

// (2) Mutable coll.
val ml = ListBuffer(1,2,3)
ml :+ 4
// ml -> 1,2,3,4

// (3) Ranges
(1 to 3).map(_ + 1)

// (4) Higher Order functions
Map("a" -> 1).forall(_._2 > 10)
// true

// (5) Advanced methods
List(1,2,3).sliding(2)
// List(List(1,2), List(2,3))

// (6) Conversion from coll. X->Y
Set("a" -> 1).toMap

// (7) Union
List(1,2) ++ List(3,4)
//1,2,3,4
```

**Kotlin**

```kotlin
// (1) Immutable coll. (default)
val l = listOf(1,2,3)
val l2 = l + 4
// l -> 1,2,3
// l2 -> 1,2,3,4

// (2) Mutable coll.
val ml = mutableListOf(1,2,3)
ml + 4
//ml -> 1,2,3,4

// (3) Ranges
(1..3).map{it + 1}

// (4) Higher Order functions
mapOf("a" to 1).all{it.value > 10}
// true

// (5) Advanced methods
listOf(1,2,3).windowed(2)
// List(List(1,2), List(2,3))

// (6) Conversion from coll. X->Y
setOf("a" to 1).toMap()

// (7) Union
listOf(1,2) + listOf(3,4)
// 1,2,3,4
```

## Concurrency

### Scala Futures

*Sequential Programming...*

```scala
def temperatureIn(city: String):Int = Random.nextInt(30)
val ams = temperatureIn("Amsterdam")
val zrh = temperatureIn("Zurich")
println(s"AMS: ${ams} ZRH: ${zrh}")
//AMS: 24 ZRH: 26
```

*Async on the other hand...*

Futures, Streams and Actors are the common building blocks for concurrency in Scala

```scala
def temperatureIn(city: String):Future[Int] = Future{
  Thread.sleep(1000)
  Random.nextInt(30)
}

val amsFuture = temperatureIn("Amsterdam")
val zrhFuture = temperatureIn("Zurich")
// Since they are libraries - and not language features -
// they force you to tightly bind your code to their API and abstractions.
val temperatures = amsFuture.flatMap(ams =>
  zrhFuture.map(zrh => s"AMS: ${ams} ZRH: ${zrh}")
)

println(Await.result(temperatures, 5 seconds))
//AMS: 24 ZRH: 26
```

The business intent of my code gets lost in all the ‘combinator jungle’

### Kotlin Coroutines

#### Kotlin Coroutines to the rescue

The concurrency building blocks of Kotlin rely on Coroutines.
With Coroutines logic can be expressed sequentially whereas the underlying
implementation figures out the asynchrony.

```kotlin
// A method marked suspend can be run within a coroutine that can suspend it without blocking a Thread
suspend fun temperatureIn(city: String): Int {
  delay(1000)
  return Random().nextInt(30)
}

// To start a coroutine at least one suspending function is required (here async)
val ams = async { temperatureIn("Amsterdam") }
val zrh = async { temperatureIn("Zurich") }

// await suspends the coroutine until some computation is done and returns the result
println("AMS: ${ams.await()} ZRH: ${zrh.await()}")
//AMS: 24 ZRH: 26
```

#### Kotlin Coroutines under the hood

```kotlin
suspend fun temperatureIn(city: String): Int {
  delay(1000)
  return Random().nextInt(30)
}
```

`suspend` methods get an additional Continuation parameter compiled in

```java
// Java
Object temperatureIn(String city, Continuation<Int> cont){...}
```

`Continuation` is a callback interface used by the underlying async processor

```kotlin
public interface Continuation<in T> {
  public val context: CoroutineContext
  public fun resume(value: T)
  public fun resumeWithException(exception: Throwable)
}
```

#### Kotlin Coroutines Interoperability

```kotlin
public CompletableFuture<Integer> temperatureIn(String city) {
  return CompletableFuture.supplyAsync(() -> {
   return new Random().nextInt(30);
   });
}
```

```kotlin
suspend fun <T> CompletableFuture<T>.await(): T =
  suspendCoroutine<T> { cont: Continuation<T> ->
    whenComplete { result, exception ->
      if (exception == null) // the future has been completed normally
        cont.resume(result)
      else // the future has completed with an exception
        cont.resumeWithException(exception)
    }
  }
```

Kotlin’s coroutine integration library offers suspended extension methods that ‘lift’ other concurrency abstractions into coroutines

### Some final words on Coroutines

**Kotlin**

Coroutines is not a new concept. It already exists in a variety of languages:

- async/await in C#, ECMAScript
- channels and select in Go
- generators/yield in C# and Python

Besides basic Coroutines Kotlin also supports:

- **channels** for stateless communication between Coroutines
- **actors** for stateful communication between Coroutines

**Scala**

- [scala/scala-async](https://github.com/scala/scala-async)
