# Ruby and Rails: The Bad Parts by Volodymyr Melnyk
<!-- tags: ruby -->

- [References](#references)
- [Good Parts](#good-parts)
- [Bad](#bad)
  - [Ruby isn’t Static- typed](#ruby-isnt-static--typed)
  - [Ruby has an unclear concept of Module](#ruby-has-an-unclear-concept-of-module)
  - [Proc and Lambda](#proc-and-lambda)
  - [Ruby Standard Library is a ghetto](#ruby-standard-library-is-a-ghetto)
    - [Abbrev](#abbrev)
    - [Delegator](#delegator)
    - [Alternate syntax](#alternate-syntax)
    - [`&&` versus `and`](#-versus-and)
    - [`||` versus `or`](#-versus-or)
  - [Values against expressions You should know!](#values-against-expressions-you-should-know)
  - [Boolean Algebra Fail](#boolean-algebra-fail)
  - [Ruby is not that strongly-typed language.](#ruby-is-not-that-strongly-typed-language)
  - [`nil`](#nil)

## References

These notes are compiled from https://speakerdeck.com/egoholic/ruby-and-rails-the-bad-parts.

## Good Parts

- It has high abilities in meta-programming
- It's good for DSL
- It allows to write prototypes very fast
- It has a huge ecosystem with tons of gems and development tools

## Bad

### Ruby isn’t Static- typed

Ruby has no typed signatures. This means that you need to do all type checks manually.

```ruby
x=5
y = “string"
lambda = ->{ x + y }

# you will not get an
# error until execution
# next code line:

lambda.call
```

### Ruby has an unclear concept of Module

In Ruby a module is a class which can’t have instances and can be included into another class or another class can be extended with it.

```ruby
module InstanceMethods; end
module ClassMethods; end
class C
  include InstanceMethods
  extend  ClassMethods
end
C.ancestors
#=> [C, InstanceMethods, Object, Kernel, BasicObject]
C.singleton_class.ancestors
#=> [
#   #<Class:C>, ClassMethods, #<Class:Object>,
# <Class:BasicObject>, Class, Module, Object, Kernel, # BasicObject
#]
```

### Proc and Lambda

In Ruby we have a `Proc` class and two types of its instances (it’s strange), but actually we need only one of them (as for me, I prefer lambdas).

```ruby
p1 = Proc.new { |a, b| a + b }
p2 = Proc.new { |a, b| return a + b }
l1 = ->(a, b) { a + b }
l2 = ->(a, b) { return a + b }
p1.class   # Proc
l1.class   # Proc
p1.lambda? # false
l1.lambda? # true
def mtd(pobj, a, b = nil)
  args = b ? [a, b] : [a]
  puts "method code 1"
  puts pobj.call *args
  puts "method code 2"
end

mtd p1, 1 
# method code 1 
# TypeError: nil can't be coerced into Fixnum
mtd p1, 1, 3 
# method code 1  # 4 
# method code 2
mtd p2, 1 
# method code 1 
# TypeError: nil can't be coerced into Fixnum
mtd p2, 1, 3 
# method code 1 
# LocalJumpError: unexpected return

mtd l1, 1 
# method code 1 
# ArgumentError: wrong number of arguments (1 for 2)
mtd l1, 1, 3 
# method code 1  # 4 
# method code 2
mtd l2, 1 
# method code 1 
# ArgumentError: wrong number of arguments (1 for 2)
mtd l2, 1, 3 
# method code 1  # 4 
# method code 2
```

### Ruby Standard Library is a ghetto

Ruby Standard Library has a huge number of low-quality and useless libraries.

#### Abbrev

```ruby
require 'abbrev'
%w{ car cone }.abbrev #=> {  “car” => "car", 
  "ca" => "car", 
  "cone" => "cone", 
  "con" => "cone", 
  "co" => "cone"  
}
```

#### Delegator

```ruby
class SimpleDelegator < Delegator
  def initialize obj 
    super 
    @delegate_sd_obj = obj  
  end
  
  def __getobj__  
    @delegate_sd_obj 
  end
  
  def __setobj__ obj  
    @delegate_sd_obj = obj 
  end  
end
```

#### Alternate syntax

Ruby has a lot of alternate syntaxes for different things. Because of that Ruby code can look very differently.


- `{...}` vs `do ... end` 
- `->() {...}`, `-> {}`, `lambda {|| }`, `lambda {}` 
- `def mtd(a, b)`, `def mtd a, b`
- `0..10`, `0...10`
- `%w{}`, `%w[]`, `%w()`, `%w//`, `%w""`, `%w||`, `%w[]`, `%W[]`, `%i[]`, `%i[]` 
`//`, `%r//`, `%s[]` 
- `''`, `""`

#### `&&` versus `and`

``` ruby
n = 1 && n + 1
# NoMethodError: undefined
# method `+' for nil


n = 1 #=> 1
n = 2 && n + 1 #=> 2
n = 2 && n + 1 #=> 3
n = 2 && n + 1 #=> 4
n = 2 && n + 1 #=> 5
n #=> 5
```

```ruby
n = 1 and n + 1 #=> 2

n = 1 #=> 1
n = 2 and n + 1 #=> 3
n = 2 and n + 1 #=> 3
n = 2 and n + 1 #=> 3
n = 2 and n + 1 #=> 3
n #=> 2
```

#### `||` versus `or`

```ruby
n = 1  n = 1 
n = nil || n + 2 #=> 3 


n = nil or n + 2 
# NoMethodError: undefined  
# method `+' for nil
```

### Values against expressions You should know!

### Boolean Algebra Fail

If `&&` and `||` are boolean operators, why their in/out arguments aren’t booleans?

```ruby
true && "string"
#=> "string"

1 || nil #=> 1
```

### Ruby is not that strongly-typed language.

Add more cases

### `nil`

`nil` is

- more code
  - checks
  - special cases
  - error handling 
- more specs / tests  
- more errors
