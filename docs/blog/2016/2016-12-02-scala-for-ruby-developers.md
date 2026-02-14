# Scala for Ruby Developers
<!-- tags: scala, python, vs, comparison -->

- [References](#references)
- [1. Initial Ruby vs Scala comparison](#1-initial-ruby-vs-scala-comparison)
- [2.1 Map and Reduce](#21-map-and-reduce)
- [2.2 Labmdas](#22-labmdas)
- [3. Named Arguments](#3-named-arguments)
- [4. Partial Functions](#4-partial-functions)
- [5. Pattern Matching](#5-pattern-matching)
- [6. Random from array](#6-random-from-array)
- [7. Monkey Patching](#7-monkey-patching)
- [8. Mixins](#8-mixins)
- [9. Line Ending](#9-line-ending)
- [10. Dynamic calls](#10-dynamic-calls)
- [11. Duck Typing](#11-duck-typing)
- [12. Types](#12-types)


## References
- [Github - Ruby vs Scala](https://github.com/KamilLelonek/scala-vs-ruby)
  - http://www.slideshare.net/squixy/scala-vs-ruby-45694031
- http://www.slideshare.net/El_Picador/scala-vs-ruby

---

## 1. Initial Ruby vs Scala comparison

**Ruby**

- Designed for humans, not machines
- Extreme flexibility: if you mess up, it’s on you
- Everything has to be easy, elegant and fun
- DSL on top of DSLs on top of DSLs
- Testing is critical
- Things move quickly, learn to keep up
- Passionate and vibrant community

**Scala**

- Have the best of both object oriented and functional programming worlds
- Let the compiler do some of the work for you
- Concurrency matters
- Less ceremony than Java, but aiming for same or better performance
- Live in harmony with the Java ecosystem

## 2.1 Map and Reduce

**Ruby**

```ruby
def fun
  (3 .. 999).select { |n| n % 5 == 0 || n % 3 == 0 }.reduce :+
end
```

**Scala**

```scala
def fun = (3 to 999).filter { n => n % 5 == 0 || n % 3 == 0 }.reduce(_+_)
```

## 2.2 Labmdas

**Scala**

```scala
list.filter(_ % 2 == 0)

list.filter {
         e: Int => (e % 2 == 0))
        }
```

**Ruby**

```ruby
list.select do |e| 
  e % 2 == 0
end
```

## 3. Named Arguments

> Show an example of named arguments in constructors of functions

**Ruby**

```ruby
class Foo
  def initialize(foo:, bar:) end
end

Foo.new(foo: 1, bar: false)
```

```ruby
class Bar
  def initialize(foo, bar) end
end

Bar.new(foo = 1, bar = false)

```

**Scala**

```scala
case class Foo(foo: Int, bar: Boolean)

new Foo(foo = 1, bar = false)
```

```scala
def bar(attr: String) = {}

bar(attr = "")
```

## 4. Partial Functions

> You are given a function that sums two numbers:

**Ruby**

```ruby
def add(a, b)
  a + b
end
```

**Scala**

```scala
def add(a: Int, b: Int) = a + b
```

---

> Write a function called `add2`, that uses `add` function, takes one parameter and adds `2` to it.

**Ruby**

```ruby
[1] (pry) main: 0> def add(a, b)
[1] (pry) main: 0*   a + b
[1] (pry) main: 0* end
=> :add

[2] (pry) main: 0> add2 = -> b { add(2, b) }
=> #<Proc:0x007fa8b9975d38@(pry):4 (lambda)>

[3] (pry) main: 0> add2.(3)
=> 5

[3] (pry) main: 0> add2[3]
=> 5
```

**Scala**

```scala
scala> def add(a: Int, b: Int) = a + b
add: (a: Int, b: Int)Int

scala> val add2 = add(2, _: Int)
add2: Int => Int = <function1>

scala> add2(3)
res4: Int = 5
```

## 5. Pattern Matching

> Write a function that checks whether a given argument is an integer or string. Otherwise print `Not match`

**Ruby**

```ruby
[0] (pry) main: 0> def pattern_matching(value)
[0] (pry) main: 0*   case value
[0] (pry) main: 0*   when Integer then puts "Integer"
[0] (pry) main: 0*   when String  then puts "String"
[0] (pry) main: 0*   else              puts "Not match"
[0] (pry) main: 0*   end
[0] (pry) main: 0* end
=> :pattern_matching

[1] (pry) main: 0> pattern_matching("a")
String
=> nil
[2] (pry) main: 0> pattern_matching(1)
Integer
=> nil
[3] (pry) main: 0> pattern_matching(false)
Not match
=> nil

```

**Scala**

```scala
scala> :paste
// Entering paste mode (ctrl-D to finish)

def patternMatching(value: Any) = value match {
  case _: Integer => println("Integer")
  case _: String  => println("String")
  case _          => println("Not match")
}

// Exiting paste mode, now interpreting.

patternMatching: (value: Any)Unit

scala> patternMatching("a")
String

scala> patternMatching(1)
Integer

scala> patternMatching(false)
Not match
```



**Scala**

```scala
def matchTest(x: Any): Any = x match {
  case 1 => "one"
  case "two" => 2
  case y: Int => "scala.Int" case 2 :: tail => tail
}
```

**Ruby**

`gem install case`

```ruby
require 'case'

def matchTest x case x
 when 1 "one"
 when "two" 2
 when Case::All[Integer] "ruby.Integer"
 when Case::Array[2, Case::Any] x[1..-1]
end end
```

## 6. Random from array

> Write a function that finds a random element from given array.

**Ruby**

```ruby
def get_random_element(array)
  array.sample
end
```

**Scala**

```scala
import scala.util.Random

def getRandomElement[T](list: Seq[T]): T = list(Random nextInt list.length)
```

## 7. Monkey Patching

> Write a function belonging to String class that allows to remove all occurrences of given substring.

**Ruby**

```ruby
String.class_eval do    # ALWAYS .class_eval
  def remove(substring)
    gsub(substring, '')
  end
end
```

**Scala**

```scala
implicit class SuperString(val string: String) extends AnyVal {
  def remove(substring: String) = string.replaceAll(substring, "")
}
```

> Usage

**Ruby** 

```ruby
[0] (pry) main: 0> String.class_eval do    # ALWAYS .class_eval
[0] (pry) main: 0*   def remove(substring)
[0] (pry) main: 0*     gsub(substring, '')
[0] (pry) main: 0*   end
[0] (pry) main: 0* end
=> :remove

[1] (pry) main: 0> 'test'.remove 't'
=> "es"
```

**Scala**

```scala
scala> implicit class SuperString(val string: String) extends AnyVal {
     |   def remove(substring: String) = string.replaceAll(substring, "")
     | }
defined class SuperString

scala> "test" remove "t"
res0: String = es
```

**Ruby**

> Monkey Patching

```ruby
puts "a".to_s # => a

class String 
  def to_s
    "Monkey !"
  end
  def my_method 
    "Patch !"
  end 
end

puts "a".to_s # => Monkey !

puts "a".my_method # => Patch !
```

**Scala**

> Implicits

```scala
class MySuperString(original: String) { 
  def myMethod = "Patch !"
}

implicit def string2super(x: String) = new MySuperString(x)

println("a".myMethod) // => Patch !
```

## 8. Mixins

> Create a `Helper` mixin with auxilary method that can be adopted in many classes

**Scala**

```scala
scala> trait Helper {
     |   def help = "I'm from helper"
     | }
defined trait Helper

scala>

scala> class IncludeHelper extends Helper
defined class IncludeHelper

scala>

scala> (new IncludeHelper).help
res0: String = I'm from helper
```

**Ruby**

```ruby
[1] (pry) main: 0> module Helper
[1] (pry) main: 0*   def help
[1] (pry) main: 0*     "I'm from helper"
[1] (pry) main: 0*   end
[1] (pry) main: 0* end
=> :help
[2] (pry) main: 0> class IncludeHelper
[2] (pry) main: 0*   include Helper
[2] (pry) main: 0* end
=> IncludeHelper
[3] (pry) main: 0> IncludeHelper.new.help
=> "I'm from helper"
```

## 9. Line Ending

Both Languages should not end line with `;` 

## 10. Dynamic calls

**Ruby**

```ruby
class Animal
  def method_missing name, *args 
    if args.empty?
      puts "Animal says " + name.to_s
    else
      puts "Animal wants to " + name.to_s + args.join(", ")
    end
    self
  end 
end

# ---
animal = Animal.new
animal.qualk # => Animal says : qualks ! 
animal.say("hello") # => Animal wants to say hello
```

**Scala**

```scala
class Animal extends Dynamic {
  def _select_(name: String) = println("Animal says " + name)
  def _invoke_(name: String, args: Any*) = {
    println("Animal wants to " + name + args.mkString(", "))
    this
  } 
}

val animal = new Animal
animal.qualk // => Animal says qualk 
animal.say("hello") // => Animal wants to say hello
```

## 11. Duck Typing

**Ruby**

```ruby

class Duck
  def quack; end 
  def walk; end
end

class Platypus 
  def quack; end 
  def walk; end
end

def act_as_a_duck animal 
  animal.quack 
  animal.walk
end

duck = Duck.new
platypus = Platypus.new
act_as_a_duck(duck) 
act_as_a_duck(platypus)
```

**Scala**

```scala
class Duck {
  def quack = ... 
  def walk = ...
}

class Platypus {
  def quack = ... 
  def walk = ...
}

def ActAsADuck(a: { def quack; def walk }) = { 
  a.quack
  a.walk 
}

val duck = new Duck 
val platypus = new Platypus
ActAsADuck(duck)
ActAsADuck(platypus)
```

## 12. Types

**Scala**

```scala
var hash = new HashMap[Int, String]
```

**Ruby**

```ruby
hash = Hash.new 
hash = 3
```