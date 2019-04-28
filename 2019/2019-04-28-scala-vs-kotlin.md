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


**Scala**

```scala
```

**Kotlin**

```kotlin
```