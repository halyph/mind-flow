# Python Bad Practices

> | python |

I've been using Python as scripting language on a non-regular basis. It means I can (I possibly do) write non-idiomatic Python code. I've decided to collect in one place popular Python anti-patterns and bad practices to avoid them. 

**Table of Contents**
- [References](#references)
  - [Original sources](#original-sources)
  - [Python standard library](#python-standard-library)
- [1 - Collections](#1---collections)
  - [1.1 - Iterate over a list](#11---iterate-over-a-list)
  - [1.2 - Iterate over a list in reverse order](#12---iterate-over-a-list-in-reverse-order)
  - [1.3 - Access the last element in a list](#13---access-the-last-element-in-a-list)
  - [1.4 - Use sequence unpacking](#14---use-sequence-unpacking)
  - [1.5 - Use lists comprehensions](#15---use-lists-comprehensions)
  - [1.6 - Use enumerate function](#16---use-enumerate-function)
  - [1.7 - Use keys to sort list](#17---use-keys-to-sort-list)
  - [1.8 - Use all/any functions](#18---use-allany-functions)
  - [1.9 - Dictionaries: avoid using keys() function](#19---dictionaries-avoid-using-keys-function)
  - [1.10 - Dictionaries: Iterate over keys and values](#110---dictionaries-iterate-over-keys-and-values)
  - [1.11 - Use dictionaries comprehension](#111---use-dictionaries-comprehension)
  - [1.12 - Use `namedtuple` instead of simple class](#112---use-namedtuple-instead-of-simple-class)
  - [1.13 - Use `defaultdict` and/or `Counter`](#113---use-defaultdict-andor-counter)
  - [1.14 - Modifying a list while iterating over it](#114---modifying-a-list-while-iterating-over-it)
- [2 - Functions](#2---functions)
  - [2.1 - Mutable Default Args](#21---mutable-default-args)
- [3 - Variable](#3---variable)
  - [3.1 - Misunderstanding Python scope rules](#31---misunderstanding-python-scope-rules)
  - [3.2 - Confusing how Python binds variables in closures](#32---confusing-how-python-binds-variables-in-closures)

---
## References

### Original sources

1. [Python Patterns](https://python-patterns.guide/) (see [src](https://github.com/brandon-rhodes/python-patterns))
2. [The Little Book of Python Anti-Patterns](https://docs.quantifiedcode.com/python-anti-patterns/) (see [src](https://github.com/quantifiedcode/python-anti-patterns))
3. [Python Data Structures Idioms](https://dev.to/mushketyk/python-data-structures-idioms-6ae) by Ivan Mushketyk
4. [Buggy Python Code: The 10 Most Common Mistakes That Python Developers Make](https://www.toptal.com/python/top-10-mistakes-that-python-programmers-make) by Martin Chikilian
5. [Youtube: 5 Common Python Mistakes and How to Fix Them](https://www.youtube.com/watch?v=zdJEYhA2AZQ) by Corey Schafer

### Python standard library

- [`all`](https://docs.python.org/3/library/functions.html#all)
- [`any`](https://docs.python.org/3/library/functions.html#any)
- [`range`](https://docs.python.org/3/library/stdtypes.html#typesseq-range)
- [`enumerate`](https://docs.python.org/3/library/functions.html#enumerate)
- [`sorted`](https://docs.python.org/3/library/functions.html#sorted)
- [`zip`](https://docs.python.org/3/library/functions.html#zip)
- [`collections.namedtuple`](https://docs.python.org/3/library/collections.html#collections.namedtuple)
- [`collections.defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict)
- [`collections.Counter`](https://docs.python.org/3/library/collections.html#collections.Counter)

---

## 1 - Collections

### 1.1 - Iterate over a list

Ref: [[3](#original-sources)]

**Very Bad**

```python
l = [1, 2, 3, 4, 5]
i = 0
while i < len(l):
    print(l[i])
    i += 1
```

**Bad**

```python
for i in range(len(l)):
    print(l[i])
```

**Good**

```python
for v in l:
    print(v)
```

---

### 1.2 - Iterate over a list in reverse order

Ref: [3]

**Bad**

```python
for i in range(len(l) - 1, -1, -1):
    print(l[i])
```

**Good**

```python
for i in reversed(l):
    print(i)
```

---

### 1.3 - Access the last element in a list

Ref: [3]

**Bad**

```python
l = [1, 2, 3, 4, 5]
>>> l[len(l) - 1]
5
```

**Good**

```python
>>> l[-1]
5
```

```python
>>> l[-2]
4
>>> l[-3]
3
```

---

### 1.4 - Use sequence unpacking

Ref: [3]

**Bad**

```python
l1 = l[0]
l2 = l[1]
l3 = l[2]
```

**Good**

```python
l1, l2, l3 = [1, 2, 3]

>>> l1
1
>>> l2
2
>>> l3
3
```

---

### 1.5 - Use lists comprehensions

Ref: [3]

**Bad**

```python
under_18_grades = []
for grade in grades:
    if grade.age <= 18:
        under_18_grades.append(grade)
```

**Good**

```python
under_18_grades = [grade for grade in grades if grade.age <= 18]
```

---

### 1.6 - Use enumerate function

Ref: [3]

**Bad**

```python
for i in range(len(menu_items)):
    menu_items = menu_items[i]
    print("{}. {}".format(i, menu_items))
```

**Good**

```python
for i, menu_items in enumerate(menu_items):
    print("{}. {}".format(i, menu_items))
```

---

### 1.7 - Use keys to sort list

Ref: [3]

```python
people = [Person('John', 30), Person('Peter', 28), Person('Joe', 42)]
```

**Bad**

```python
def compare_people(p1, p2):
    if p1.age < p2.age:
        return -1
    if p1.age > p2.age:
        return 1
    return 0

sorted(people, cmp=compare_people)

[Person(name='Peter', age=28), Person(name='John', age=30), Person(name='Joe', age=42)]
```

**Good**

```python
sorted(people, key=lambda p: p.age)

[Person(name='Peter', age=28), Person(name='John', age=30), Person(name='Joe', age=42)]
```

---

### 1.8 - Use all/any functions

Ref: [3]

**Bad**

```python
def all_true(lst):
    for v in lst:
        if not v:
            return False
    return True
```

**Good**

```python
all([True, False])
>> False

any([True, False])
>> True
```

```python
all([person.age > 18 for person in people])

# or generator

all(person.age > 18 for person in people)
```

---

### 1.9 - Dictionaries: avoid using keys() function

Ref: [3]

**Bad**

```python
for k in d.keys():
    print(k)
```

**Good**

```python
for k in d:
    print(k)
```

---

### 1.10 - Dictionaries: Iterate over keys and values

Ref: [3]

**Bad**

```python
for k in d:
    v = d[k]
    print(k, v)
```

**Good**

```python
for k, v in d.items():
    print(k, v)
```

---

### 1.11 - Use dictionaries comprehension

Ref: [3]

**Bad**

```python
d = {}
for person in people:
    d[person.name] = person
```

**Good**

```python
d = {person.name: person for person in people}
```

---

### 1.12 - Use `namedtuple` instead of simple class

Ref: [3]

**Bad**

```python
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

**Good**

```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
```

In addition `namedtuple` implements `__str__`, `__repr__`, and `__eq__` methods:

```python
>>> Point(1, 2)
Point(x=1, y=2)
>>> Point(1, 2) == Point(1, 2)
True
```

---

### 1.13 - Use `defaultdict` and/or `Counter`

Ref: [3]

> We need to count a number of times an element is encountered in a collection

**Bad**

```python
d = {}
for v in lst:
    if v not in d:
        d[v] = 1
    else:
        d[v] += 1
```

**Good**

```python
>>> d = defaultdict(lambda: 42)
>>> d['key']
42
```

```python
from collections import defaultdict
d = defaultdict(int)
for v in lst:
    d[v] += 1
```

**Good**

```python
from collections import Counter

>>> counter = Counter(lst)
>>> counter
Counter({4: 3, 1: 2, 2: 1, 3: 1, 5: 1})
```

---

### 1.14 - Modifying a list while iterating over it

Ref: [4]

**Bad**

```python
>>> odd = lambda x : bool(x % 2)
>>> numbers = [n for n in range(10)]
>>> for i in range(len(numbers)):
...     if odd(numbers[i]):
...         del numbers[i]  # BAD: Deleting item from a list while iterating over it
...
Traceback (most recent call last):
  	  File "<stdin>", line 2, in <module>
IndexError: list index out of range
```

**Good**

```python
>>> odd = lambda x : bool(x % 2)
>>> numbers = [n for n in range(10)]
>>> numbers[:] = [n for n in numbers if not odd(n)]  # ahh, the beauty of it all
>>> numbers
[0, 2, 4, 6, 8]
```

---

## 2 - Functions

### 2.1 - Mutable Default Args

Ref: [[4, 5](#original-sources)]

**Bad**

```python
def foo(bar=[]): # bar is optional and defaults to [] if not specified
    bar.append("baz")
    return bar
```

```python
>>> foo()
["baz"]
>>> foo()
["baz", "baz"]
>>> foo()
["baz", "baz", "baz"]
```

The default value for a function argument is only evaluated once, at the time that the function is defined. Thus, the *bar* argument is initialized to its default (i.e., an empty list) only when *foo()* is first defined, but then calls to *foo()* (i.e., without a bar argument specified) will continue to use the same list to which bar was originally initialized.

**Good**

```python
def foo(bar=None):
    if bar is None:  # or if not bar:
        bar = []
    bar.append("baz")
    return bar
```

```python
>>> foo()
["baz"]
>>> foo()
["baz"]
>>> foo()
["baz"]
```

---

## 3 - Variable

### 3.1 - Misunderstanding Python scope rules

Ref:

- [[4](#original-sources)]
- [Python scoping: understanding LEGB](https://blog.mozilla.org/webdev/2011/01/31/python-scoping-understanding-legb/)
- [Python Frequently Asked Questions: Why am I getting an UnboundLocalError when the variable has a value?](https://docs.python.org/3/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-valu)

#### Sample 1 <!-- omit in toc -->

**Bad**

```python
def func1(param=None):
    def func2():
        if not param:
            param = 'default'
        print param
    # Just return func2.
    return func2


if __name__ == '__main__':
   func1('test')()
```

```python
$ python test.py 
Traceback (most recent call last):
  File "test.py", line 11, in 
    func1('test')()
  File "test.py", line 3, in func2
    if not param:
UnboundLocalError: local variable 'param' referenced before assignment
```

**Good**

```python
def func1(param=None):
    def func2(param2=param):
        if not param2:
            param2 = 'default'
        print param2
    # Just return func2.
    return func2
```

#### Sample 2 <!-- omit in toc -->

**Bad**

```python
>>> x = 10
>>> def foo():
...     x += 1
...     print x
...
>>> foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in foo
UnboundLocalError: local variable 'x' referenced before assignment
```

```python
>>> lst = [1, 2, 3]
>>> def foo1():
...     lst.append(5)   # This works ok...
...
>>> foo1()
>>> lst
[1, 2, 3, 5]

>>> lst = [1, 2, 3]
>>> def foo2():
...     lst += [5]      # ... but this bombs!
...
>>> foo2()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in foo
UnboundLocalError: local variable 'lst' referenced before assignment
```

---

### 3.2 - Confusing how Python binds variables in closures

Ref: [[4](#original-sources)]

**Bad**

```python
>>> def create_multipliers():
...     return [lambda x : i * x for i in range(5)]
>>> for multiplier in create_multipliers():
...     print multiplier(2)
...
```

Expected

```
0
2
4
6
8
```

Actual

```
8
8
8
8
8
```

**Good**

```python
>>> def create_multipliers():
...     return [lambda x, i=i : i * x for i in range(5)]
...
>>> for multiplier in create_multipliers():
...     print multiplier(2)
...
0
2
4
6
8
```

---