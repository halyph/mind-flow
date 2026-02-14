# Scala for Python Developers by _Kevin Stanton_
<!-- tags: scala, python, vs, comparison -->

- [Reference](#reference)
- [1. Classes](#1-classes)
- [2. Dictionaries and Maps](#2-dictionaries-and-maps)
- [3. IO and Files](#3-io-and-files)
- [4. For Comprehensions](#4-for-comprehensions)
- [5. Function literals](#5-function-literals)
- [6. Functions one-liner](#6-functions-one-liner)
- [7. Functions](#7-functions)
- [8. Java interop](#8-java-interop)
- [9. Lists](#9-lists)
  - [9.1. Overview](#91-overview)
  - [9.2. Concatenating lists](#92-concatenating-lists)
  - [9.3. Sorting a list](#93-sorting-a-list)
- [10. Looping range and notes on operators](#10-looping-range-and-notes-on-operators)
  - [10.1. Loop over range of numbers](#101-loop-over-range-of-numbers)
  - [10.2. Operators](#102-operators)
- [11. Sets](#11-sets)
- [12. Tuples](#12-tuples)

## Reference

- [Github - stantonk/scala-for-python-developers](https://github.com/stantonk/scala-for-python-developers)

---

## 1. Classes

**Python**

```python
class Dog(object):
    def __init__(self, name):
        print 'This line runs upon instantiation'
        self.name = name
    def speak(self):
        print '%s: Bark!' % self.name
    def command(self, cmd):
        print '%s ::%s::' % (self.name, cmd)
dog = Dog('Rover')
dog.speak()
dog.command('sit')
```

**Scala**

```scala
class Dog(name: String) {
  /*
  The body of the class can contain code for the primary constructor, instead
  of an explicitly defined constructor method like in Java or Python. Also,
  note that the parameters for the constructor are in the class definition
  portion at the top. Scala automatically places them in fields named after
  the parameter name. Less boilerplate!
   */
  println("This line runs upon instantiation")

  /*
  Notice how there is no equals sign on the speak method, that's because it
  doesn't return anything. Technically, it returns Unit, which is like Java's
  void and Python's None.
   */
  def speak() { println(this.name + ": Bark!") }

  def command(cmd: String) = {
    println(name + " ::" + cmd + "::")
  }
}

val dog = new Dog("Rover")
// This line runs upon instantiation of a Dog, it is the primary constructor
// dog: Dog = Dog@11727596

dog.speak()
// Rover: Bark!

dog.command("sit")
// Rover ::sit::
```

## 2. Dictionaries and Maps

**Python**

```python

>>> x = {"dog": "Woof", "cat": "Meow"}
>>> for k, v in x.items():
...   print "%s=%s" % (k, v)
...
dog=Woof
cat=Meow
>>> print "the dog says " + x["dog"] + " and the cat says " + x["cat"]
the dog says Woof and the cat says Meow
>>> print x.get("duck", "quack")
quack
>>> x['fox'] = '??????'
>>> print "what does the fox say: " + x['fox']
what does the fox say: ??????
```

**Scala**

```scala
var x = Map("dog" -> "Woof", "cat" -> "Meow")
for ((k, v) <- x)
  printf("%s=%s\n", k, v)
// dog=Woof
// cat=Meow

println("the dog says " + x("dog") + " and the cat says " + x("cat")) // like lists, note parens..not brackets
// the dog says Woof and the cat says Meow

println(x.getOrElse("duck", "quack"))
// quack

x += ("fox" -> "??????")

println("what does the fox say: " + x("fox"))
// what does the fox say: ??????
```

## 3. IO and Files

**Python**

```python
import sys
if len(sys.argv) > 0:
    for line in open(sys.argv[1]):
        print line.rstrip('\r\n') # scala.io.Source removes line terminators
else:
    sys.stderr.write('Please enter filename')

```

**Scala**
 
```scala
import scala.io.Source

if (args.length > 0) {
  for (line <- Source.fromFile(args(0)).getLines)
    println(line)
} else {
  Console.err.println("Please enter filename")
}
```

## 4. For Comprehensions

**Python**

```python
Python
l = [1, 2, 3, 4, 5, 6]
evens = [n for n in l if n % 2 == 0]
```

**Scala**

```scala
val l = List(1, 2, 3, 4, 5, 6)
val evens = for (n <- l if n % 2 == 0) yield n
```

## 5. Function literals

**Python**

```python

# Python does not have a function literal syntax per se, but functions are first

# class objects and you can treat them in similar ways in Scala.

greeting = lambda name: "Hello " + name
print greeting("world")

def greet(name): return "Hello " + name

greeting = greet
print greeting("world")

```

**Scala**

```scala
var greeting = (name: String) => "Hello " + name
println(greeting("world"))

def greet(name: String) = "Hello " + name
greeting = greet
println(greeting("world"))
```

## 6. Functions one-liner

**Python**

```python
def max2(x, y): return x if x > y else y
>>> max2(17, 19)
19
>>> max2(19, 17)
19
```

**Scala**

```scala
// scala, function definition (brief)
def max2(x: Int, y: Int) = if (x > y) x else y

max2(17, 19)
// res2: Int = 19
max2(19, 17)
// res3: Int = 19
```

## 7. Functions

**Python**

```python

def max(x, y):
  if x > y:
    return x
  else:
    return y
```

**Scala**

```scala
def max(x: Int, y: Int): Int = {
  if (x > y) x
  else y
}

/*
Note that type information is present in the function definition. Scala is a
statically-typed language. But it's type system is advanced, and usually it can
infer the type. So you can leave some type information off for improved
readability.
 */

def max(x: Int, y: Int) = {
  if (x > y) x
  else y
}

/*
Seen in the second form, Scala can usually infer the return type. So you can
leave it off. In some cases it can't infer the return type, i.e. recursion.
Also, note how there is no explicit return statement in the functions. In Scala,
the last statement executed in the body of a function becomes the return value.
 */

def max(x: Int, y: Int): Int = {
  if (x > y) return x
  else return y
}
/*
You can use return statements, but if you do, Scala's compiler cannot infer
the return type so you must specify it.
http://stackoverflow.com/questions/2209179/type-inference-on-method-return-type
*/
```

##  8. Java interop

**Python**

_This isn't for Python programmers, but it is pretty cool to see how seamlessly
Java code can be used in Scala. The entire world of existing Java libraries
can be leveraged._

**Scala**

```scala
import java.io.{FileReader, BufferedReader, IOException}

if (args.length > 0) {

  try {
    val reader = new BufferedReader(new FileReader(args(0)))

    var done = false
    while (!done) {
      val line = reader.readLine
      if (line == null) done = true else println(line)
    }

  } catch {
    case ioe: IOException => println("ERROR: IOException")
  }

} else {
  println("ERROR: no file specified")
}

```

## 9. Lists

### 9.1. Overview

**Python**

```python
l = ["one", "two", "three"]
print l[0]
for a in l:
  print a
*/
```

**Scala**

```scala
val l = List("one", "two", "three")
println(l(0))
for (a <- l)
  println(a)
```

Note how the list is indexed with parens, not square brackets. This is because
you're actually making a method call.

`println(l(0))` <-- outputs "one"
`println(l.apply(0))` <-- outputs "one"
 
### 9.2. Concatenating lists

**Python**

```python
list1 = [1, 2]
list2 = [3, 4]
biglist = list1 + list2
```

**Scala**

```scala
// scala concatenating lists
val list1 = List(1, 2)
val list2 = List(3, 4)
val biglist = list1 ::: list2
```

Note: In Scala, Lists are immutable. Python's lists, however, are mutable.
Arrays, on the other hand, are mutable.

scala, prepend an element (using the "cons" operator, ::) to an existing
list will generate a new list:

```scala
val list3 = List(2, 3)
val newlist = 1 :: list3
```

In **python**, you would do this using concatenation and a temporary list of length 1:

```python
list1 = [2, 3]
newlist = [1] + list1
```

Or you could prepend the 1 to the existing list at the front, but this would be
inefficient:

```python
list1.insert(0, 1)
```

### 9.3. Sorting a list

**Python**

```python
alist = [7, 2, 18, 3, 6]
sorted(alist) # returns a new list, sorted
alist.sort() # sorts the list in place
```

**Scala**

```scala
val alist = List(7, 2, 18, 3, 6)
println(alist.sorted)
```

## 10. Looping range and notes on operators

### 10.1. Loop over range of numbers

**Python**

```python
for i in range(0, 5):
    print i
```

Note, last number printed is 4.

**Scala**

```scala
// Scala is inclusive over the range, last number printed is 5
for (i <- 0 to 5)
  println(i)

// interesting to note, this code is equivalent:
for (i <- 0.to(5))
  println(i)
// because "to" is actually not an operator, but a method on Int, see:
0.to(5)
// res16: scala.collection.immutable.Range.Inclusive = Range(0, 1, 2, 3, 4, 5)

0 to 5
// res17: scala.collection.immutable.Range.Inclusive = Range(0, 1, 2, 3, 4, 5)
```

### 10.2. Operators

This may seem somewhat odd, but it actually is similar (at least to my
non-expert eye) to how operators are implemented in languages like Python
and PHP, e.g.

**Python**

```python
>>> x = 5
>>> x.__add__
<method-wrapper '__add__' of int object at 0x7fc339c10788>
  >>> x.__add__(2)
7
>>> x + 2
7
```

**Scala**

```scala
val x = 5
// x: Int = 5

x.+(2)
// res20: Int = 7

x + 2
// res21: Int = 7
```

## 11. Sets

**Python**

```python
>>> basket1 = set(["apple", "pear"])
>>> basket1.add("strawberry")
>>> basket2 = set(["grape", "apple", "starfruit"])
>>> print "common to both: %s" % (basket1 & basket2)
common to both: set(['apple'])
>>> print "in either basket: %s" % (basket1 | basket2)
in either basket: set(['strawberry', 'grape', 'apple', 'pear', 'starfruit'])
```

**Scala**

```scala
var basket1 = Set("apple", "pear")
// basket1: scala.collection.immutable.Set[String] = Set(apple, pear)
basket1 += "strawberry"
var basket2 = Set("grape", "apple", "starfruit")
// basket2: scala.collection.immutable.Set[String] = Set(grape, apple, starfruit)
println("common to both: " + (basket1 & basket2))
// common to both: Set(apple)
println("in either basket: " + (basket1 | basket2))
// in either basket: Set(grape, apple, pear, strawberry, starfruit)

// If you needed a mutable set:
import scala.collection.mutable
val mutableSet = mutable.Set("a", "b")
mutableSet += "c"

// or maybe an immutable HashSet?
import scala.collection.immutable.HashSet
var hashSet = HashSet(1, 2, 3)
```

## 12. Tuples

**Python**

```python

>>> pair = (1, "foo")
>>> print pair[0]
1
>>> print pair[1]
foo
```

**Scala**

```scala
val pair = (1, "foo")
// pair: (Int, String) = (1,foo)
println(pair._1)
// 1
println(pair._2)
// foo
```

Scala has tuples too (yay, no JavaBean silliness for returning multiple values of varied types!)

Both Scala and Python tuples are immutable, but Scala's are type safe, hence the strange accessing mechanism (pair._1 vs. pair[0]).

Scala actually defines multiple tuple types, up to Tuple22, to achieve this.
