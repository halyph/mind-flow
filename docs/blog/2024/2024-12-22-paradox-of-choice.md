# Paradox of Choice in Ruby
> | ruby |

[The Paradox of Choice – Why More Is Less](https://en.wikipedia.org/wiki/The_Paradox_of_Choice) - is it applicable to programming languages?

I've been using simple (in terms of syntax) languages (*Python*, *Go*) for some time and have an understanding of why such fancy, flexible language as *Ruby* has sort of "irritation" from some software engineers.

*Please note*, that I am talking about language only, avoiding ecosystem, Rails, and so on.

**Ruby** is too flexible. It has too many ways of doing the same things using different methods. I want to concentrate on simple code, which I can read and understand quickly. Yes, I want to see elegant code as well, but today it's more important for me to follow a "less is more" approach, with few possible variations.

From my perspective, Ruby aligns more closely with Perl than with Python. I don't understand why they haven't deprecated some legacy in Ruby. It would make the language cleaner and remove ambiguity.

On the other hand, [**Ruby on Rails**](https://rubyonrails.org/) follows the *"Less is More"* principle, exemplified by its [Convention over Configuration](https://rubyonrails.org/doctrine#convention-over-configuration) approach. This principle was a key factor in the framework's early success.


## Samples of "More is More" in Ruby language

I decided to collect basic samples of doing the same/similar things in Ruby, ignoring meta-programming. It's not exhaustive list of "questionable" features. I am too lazy to write really long post, but it should give you of a feeling of what I mean.

### Loading Code

- `require`: Loads a library or file once. Commonly used for loading gems or external libraries.
- `require_relative`: Similar to `require`, but resolves file paths relative to the file making the call.
- `load`: Loads and re-evaluates the code in a file every time it’s called.
- `autoload`: Registers the given file to be loaded when the given constant is first referenced.

### Mixing In Modules

- `include`: Mixes module methods as instance methods into a class.
- `extend`: Adds module methods as class methods or singleton methods.
- `prepend`: Similar to include, but methods are added to the top of the method lookup chain, overriding existing methods.


### Array

```ruby
array = [1, 2, 3, 4]
```

#### Using `%w` for Strings

To create an array of strings without quotes and commas:

```ruby
array = %w[apple banana cherry]
# => ["apple", "banana", "cherry"]
```
For strings with interpolation or escape sequences, use `%W`:

```ruby
name = "John"
array = %W[hello #{name} world]
# => ["hello", "John", "world"]
```

#### Using `%i` for Symbols 

To create an array of symbols:

```ruby
array = %i[one two three]
# => [:one, :two, :three]
```

#### Using `Array()` Method

The Array() method can convert other types to arrays.

```ruby
array = Array(1..5)
# => [1, 2, 3, 4, 5]
```

### String

#### Alternative to single `'` and double-quote `"` delimiters

Ruby provides an alternative to single and double-quote delimiters, which comes in handy
sometimes when the string you want to quote contains the delimiter you need. 

You can use various delimiters with `%Q`. The most common are `[ ]`, `{ }`, `( )`, `| |`, or `/ /`. The opening and closing delimiters must match.

```ruby
%q/general single-quoted string/  # => general single-quoted string
%Q!general double-quoted string!  # => general double-quoted string
%Q{Seconds/day: #{24*60*60}}      # => Seconds/day: 86400
%!general double-quoted string!   # => general double-quoted string
%{Seconds/day: #{24*60*60}}       # => Seconds/day: 86400
```

#### Here document (or heredoc)

A heredoc allows you to build a multi-line string.

```ruby
string = <<END_OF_STRING
  The body of the string is the input lines up to
  one starting with the same text that followed the '<<'
END_OF_STRING
```

```ruby
string = <<-END_OF_STRING
The body of the string is the input lines up to
one starting with the same text that followed the '<<'
  END_OF_STRING
```

And if you put a tilde after the << characters you can indent the text.

```ruby
def a_long_string
  <<~END_OF_STRING
      Faster than a speeding bullet, more powerful than
      a locomotive, able to leap tall buildings in a single
      bound—look, up there in the sky, it's a bird, it's a
      plane, it's Superman!
  END_OF_STRING
end
puts a_long_string 
```

You can also have multiple here documents on a single line

```ruby
print <<-STRING1, <<-STRING2
  Concat
        STRING1
  enate
  STRING2

# produces:
# Concat
# enate
```

### Hash

```ruby
{ :one => "eins", :two => "zwei", :three => "drei" }
```

Using this syntax we tell Ruby that we want the keys to be symbols.

```ruby
{ one: "eins", two: "zwei", three: "drei" }
```

### Conditional Statements `if` vs `unless`

Executes code if the condition is `false`.

```ruby
unless x >= 0
  puts "x is negative"
else
  puts "x is non-negative"
end
```

```ruby
puts "x is negative" unless x >= 0
```

### Loops

#### `loop`

```ruby
i = 1

loop do
  puts "Message number #{i}"

  i = i + 1
  if i == 6
    break
  end
end
```

#### `while`

```ruby
i = 1

while i <= 5 do
  puts "Message number #{i}"
  i = i + 1
end
```

#### `for`

```ruby
for i in 1..5 do
  puts "Message number #{i}"
end
```

#### `until`

```ruby
i = 1

until i == 6 do
  puts "Message number #{i}"
  i = i + 1
end
```

#### `begin` ... `end` block

```ruby
print "Hello\n" while false
begin
  print "Goodbye\n"
end while false

# produces:
# Goodbye 
```

### Aliases

#### `length` / `size`: Return the number of elements in the array

```ruby
arr = [1, 2, 3]
arr.length  # => 3
arr.size    # => 3
```

#### `map` / `collect`: Create a new array by applying a block to each element

```ruby
arr = [1, 2, 3]
arr.map { |x| x * 2 }       # => [2, 4, 6]
arr.collect { |x| x * 2 }   # => [2, 4, 6]
```

#### `reduce` / `inject`: Combine all elements of the array by applying a binary operation

```ruby
arr = [1, 2, 3]
arr.reduce(:+)    # => 6
arr.inject(:+)    # => 6
```

#### `find` / `detect`: Return the first element that satisfies the block

```ruby
arr = [1, 2, 3, 4]
arr.find { |x| x > 2 }     # => 3
arr.detect { |x| x > 2 }   # => 3
```

#### `select` / `find_all` / `filter`: Return all elements that satisfy the block

```ruby
arr = [1, 2, 3, 4]
arr.select { |x| x.even? }       # => [2, 4]
arr.find_all { |x| x.even? }     # => [2, 4]
```

#### key? / has_key?: Check if a key exists in the hash

```ruby
hash = { a: 1, b: 2 }
hash.key?(:a)       # => true
hash.has_key?(:a)   # => true
```

#### `reject` / `delete_if`: Return elements that do not satisfy the block

```ruby
arr = [1, 2, 3, 4]
arr.reject { |x| x.even? }    # => [1, 3]
arr.delete_if { |x| x.even? } # => [1, 3]
```

#### `exists?` / `exist?`: Check if a file exists

```ruby
File.exists?("file.txt")  # => true or false
File.exist?("file.txt")   # => true or false
```
#### `size` / `size?`

- `size`: Returns the size of the file in bytes.
- `size?`: Returns the size if the file is non-empty; otherwise, returns nil.

```ruby
File.size("file.txt")  # => 1024
File.size?("file.txt") # => 1024 or nil
```

There are more similar cases, but you've got what I mean 😉, right? 