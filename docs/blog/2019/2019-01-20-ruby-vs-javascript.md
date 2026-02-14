# Ruby vs Javascript comparison
<!-- tags: ruby, javascript, vs, comparison -->

First of all it's not my writings and it's just a copy of *Artem's Tyurin* [agentcooper/js-ruby-comparison](https://github.com/agentcooper/js-ruby-comparison) repo 

*Note:* This comparison uses pre-*ES6* code snippets.

- [Arrays](#arrays)
  - [Manipulation](#manipulation)
  - [Predicates](#predicates)
  - [Array map methong](#array-map-methong)
  - [Slices](#slices)
  - [Iterating elements](#iterating-elements)
- [Strings](#strings)
- [Hash](#hash)
- [Functions](#functions)
  - [Basic usage](#basic-usage)
  - [Multiple arguments](#multiple-arguments)
  - [Definition and invocation order](#definition-and-invocation-order)
- [Classes](#classes)
- [Math](#math)
- [Other](#other)

---

## Arrays

### Manipulation

**Ruby**

```ruby
a = ["1", "2"]
a.push("3")

a.map!(&:to_i) # [1, 2, 3]

a.delete_at(1)
a # [1, 3]

a.reverse! # [3, 1]

a.unshift(777) # [777, 3, 1]

a.last # [1]
```

**JavaScript**

```javascript
var a = ["1", "2"];
a.push("3");

a = a.map(function(n) { return parseInt(n, 10); });

a.splice(1, 1 /* how much */);
a; // [1, 3]

a.reverse() // [3, 1]

a.unshift(777); // 3
a; // [777, 3, 1]

/* or in place: */ var b = [3, 1];
                   [777].concat(b); // [777, 3, 1]
a.slice(-1)[0]; // 1
/* or */ a[a.length - 1]; // 1
```

### Predicates

**Ruby**

```ruby
a = [1, 2, 3]

a.index(2) # 1

a.all?{|n| n > 4} # false
a.any?{|n| n > 2} # true

a.keep_if{|n| n > 1} # [2, 3]
```

**JavaScript**

```javascript
var a = [1, 2, 3];

a.indexOf(2); // 1

a.every(function(n) { return n > 4; }); // false
a.some(function(n) { return n > 2; });  // true

a.filter(function(n) { return n > 1;}); // [2, 3]
```

### Array map methong

**Ruby**

```ruby
a = ["aaa  ", "  bbb", "  ccc  "]

a.map(&:strip) # ["aaa", "bbb", "ccc"]
```

**JavaScript**

```javascript
var a = ["aaa  ", "  bbb", "  ccc  "]

a.map(function(x) { return x.trim(); });               // ['aaa', 'bbb', 'ccc']
a.map(Function.prototype.call, String.prototype.trim); // ['aaa', 'bbb', 'ccc']
a.map(x => x.trim());                                  // ['aaa', 'bbb', 'ccc']
```

### Slices

**Ruby**

```ruby
a = [1, 2, 3, 4, 5]

a.slice(1..-2)  # [2, 3, 4]
a[1..-2]        # [2, 3, 4]
```

**JavaScript**

```javascript
var a = [1, 2, 3, 4, 5];

a.slice(1, -1); // [2, 3, 4]
```

### Iterating elements

```ruby
a = [1, 2, 3]

a.each {|n| puts n}

a.each do |n|
    puts n
end


for i in 0..(a.length - 1) do
  puts a[i]
end
```

**JavaScript**

```javascript
var a = [1, 2, 3];

a.forEach(function(n) { console.log(n); })

for (var i = 0; i < a.length; i++) {
  console.log(a[i]);
}

for (elem of a) {
  console.log(elem);
}
```

## Strings

**Ruby**

```ruby
'hello'.index('e')    # 1
'hello'.rindex('l')   # 3

if 'hello'.include? 'lo' then puts 'found' end

'hello' * 3           # 'hellohellohello'

'a/b/c'.split('/')    # ['a', 'b', 'c']
```

**JavaScript**

```javascript
'hello'.indexOf('e')             // 1
'hello'.lastIndexOf('l')         // 3

if (~'hello'.indexOf('lo')) { console.log('found'); }

(new Array(3 + 1)).join('hello') // 'hellohellohello'

'a/b/c'.split('/')               // ['a', 'b', 'c']
```

## Hash

**Ruby**

```ruby
h = {}
h['a'] = 1
h['b'] = 2

h.each {|key, value| puts "#{key} #{value}" }

h.keys # ['a', 'b']
h.has_key?('c') # false

h.length # 2

h.delete("b")
```

**JavaScript**

```javascript
var h = {};
h['a'] = 1;
h['b'] = 2;

for (key in h) { console.log(key, h[key]); }

Object.keys(h); // ['a', 'b']
h.hasOwnProperty('c') // false

Object.keys(h).length // 2

delete h.b
```

## Functions

### Basic usage

**Ruby**

```ruby
def plus_5(num = 0) num + 5 end

plus_5     # 5
plus_5(10) # 15

[5, 10, 15].map { |k| plus_5(k) } # [10, 15, 20]
```

**JavaScript**

```javascript
function plus_5(num) { return (num || 0) + 5; }

plus_5();   // 5
plus_5(10); // 15

[5, 10, 15].map(plus_5); // [10, 15, 20]
```

### Multiple arguments

**Ruby**

```ruby
def f(*args)
  puts args
end

```

**JavaScript**

```javascript
function f() {
  var args = Array.prototype.slice.call(arguments);
  console.log(args);
}
```

### Definition and invocation order

**Ruby**

```ruby
sample_func

def sample_func
  puts "Hello World"
end

# => NameError: undefined local
# variable or method `sample_func'
```

**JavaScript**

```javascript
sample_func();

function sample_func() {
  console.log("Hello World");
};

// => Hello World
```

## Classes

**Ruby**

```ruby
class Person
  attr_accessor :firstName, :lastName

  def initialize(firstName, lastName)
    @firstName = firstName
    @lastName = lastName
  end

  def fullName
    @firstName + " " + @lastName
  end
end

john = Person.new("John", "Malkovic")
john.fullName # "John Malkovic"
```

**JavaScript**

I'm lazy to write this example in ES6

```javascript
function Person(firstName, lastName) {
  this.firstName = firstName;
  this.lastName = lastName;
}

Person.prototype.fullName = function() {
  return this.firstName + " " + this.lastName;
}

var john = new Person("John", "Malkovic");
john.fullName(); // "John Malkovic"
```

## Math

**Ruby**

```ruby
[-5, -1, -8].max            # -1

[-5, 15, 20].reduce(0, &:+) # 30
```

**JavaScript**

```javascript
Math.max.apply(null, [-5, -1, -8]) // -1

[-5, 15, 20].reduce(function(sum, value) { return sum + value; }, 0) // 30
[-5, 15, 20].reduce((sum, value) => sum + value, 0) // 30
```

## Other

**Ruby**

```ruby
prng = Random.new()
prng.rand(5..9) # one of [5, 6, 7, 8, 9]

a, b = b, a # switch a and b
```

**JavaScript**

```javascript
function rand(a, b) { return Math.floor(Math.random() * (b - a + 1) + a); }
rand(5, 9); // one of [5, 6, 7, 8, 9]

a = [b, b = a][0] // do not try at home :-)
```
