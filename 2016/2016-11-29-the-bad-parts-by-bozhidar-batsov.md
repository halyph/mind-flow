# Ruby: The Bad Parts by Bozhidar Batsov
> **tags**: | ruby |

Table of Contents

- [Ruby: The Bad Parts by Bozhidar Batsov](#ruby-the-bad-parts-by-bozhidar-batsov)
  - [Reference](#reference)
- [The Problem :-)](#the-problem)
- [The Real Problem](#the-real-problem)
  - [Problems with the Runtime](#problems-with-the-runtime)
  - [Rubygems and Bundler](#rubygems-and-bundler)
- [The Rails Effect](#the-rails-effect)
- [Stewardship](#stewardship)
- [Problem with the Language](#problem-with-the-language)
  - [The useless stuff](#the-useless-stuff)
  - [The bad stuff](#the-bad-stuff)

---

These notes are compilled from:
* https://speakerdeck.com/bbatsov/ruby-the-bad-parts

## Reference

* http://batsov.com
  * http://batsov.com/articles/categories/style/
  * http://batsov.com/articles/2014/02/05/a-list-of-deprecated-stuff-in-ruby/
* [Ruby: The Bad Parts by Bozhidar Batsov](https://speakerdeck.com/bbatsov/ruby-the-bad-parts)
* [Ruby 4.0: To Infinity and Beyond (Athens Ruby Meetup) by Bozhidar Batsov](https://speakerdeck.com/bbatsov/ruby-4-dot-0-to-infinity-and-beyond-athens-ruby-meetup)


# The Problem :-)

* Ruby is oject-oriented
* Ruby is dynamically typed
* Ruby doesn’t have immutable data structures
* Ruby doesn’t have strong concurrency primitives
* Ruby doesn’t have enough parentheses :-)
* Ruby is not Clojure!

# The Real Problem

## Problems with the Runtime
* Ruby is slow -> MRI is slow
* Ruby’s threads suck -> MRI’s threads suck
* Running Ruby on Windows is a pain in the ass -> Running MRI on Windows is a pain in the ass
* Ruby doesn’t do JIT compilation -> MRI doesn’t do JIT compilation
* The core library is not very approachable for Rubyists

**Language != Runtime**


## Rubygems and Bundler
* bundle exec rake
* RubyGems 2.2 introduced support for Gemfile
  * http://blog.rubygems.org/2013/12/26/2.2.0-released.html

> *Major enhancements:*
>  * RubyGems can check for gem dependencies files (gem.deps.rb or Gemfile) when rubygems executables are started and uses the found dependencies. This means rake will work similar to bundle exec rake. To enable this set the RUBYGEMS_GEMDEPS environment variable to the location of your dependencies file. See Gem::use_gemdeps for further details.
> 
> * A RubyGems directory may now be shared amongst multiple ruby versions. Upon activation RubyGems will automatically compile missing extensions for the current platform when the built objects are missing. Issue #596 by Michal Papis By default different platforms do not share gem install locations so this must be configured by setting GEM_HOME to a common directory. Some gems use fixed paths for requiring extensions and are not compatible with sharing gem directories. The default sharing location may be configured by RubyGems packagers through Gem.default_ext_dir_for. Pull Request #744 by Vít Ondruch.

# The Rails Effect

* Ruby (2005) :-O
* Ruby (2006) - OMG, Rails is amazing
* Ruby (2008) - OMG, Rails is amazing & useful!
* Ruby (today) - Wev Development 96% (Rails 90%, Other - 10%), Other - 4%

> [Ruby 2.2.0 Released](https://www.ruby-lang.org/en/news/2014/12/25/ruby-2-2-0-released/)
>
> Ruby 2.2 includes many new features and improvements for the increasingly diverse and expanding demands for Ruby.
> 
> For example, Ruby’s Garbage Collector is now able to collect Symbol type objects. This reduces memory usage of Symbols; because GC was previously unable to collect them before 2.2. Since **Rails** 5.0 will require Symbol GC, it will support only Ruby 2.2 or later. (See **Rails** 4.2 release post for details.)
>
> Also, a reduced pause time thanks to the new Incremental Garbage Collector will be helpful for running **Rails** applications. Recent developments mentioned on the Rails blog suggest that **Rails** 5.0 will take advantage of Incremental GC as well as Symbol GC.

We need to grow out of Rails's shadwo!

# Stewardship

* Matz - Benevolent dictators are still dictators
* No clear vision
* No standard
* Informal deprecation policy
* Limited collaboration with alternative implementations
* Where’s the innovation?

# Problem with the Language

## The useless stuff

* `for` loops

```ruby
for name in names
    puts name
end
```
```ruby
names.each do |name|
  puts name
end
```

* `BEGIN` & `END`
  * Kernel#at_exit, anyone?
 
```ruby

END {
  puts 'Bye!'
}

puts 'Processing...'

BEGIN {
  puts 'Starting...'
}


puts 'Bye!'
puts 'Starting...'
puts 'Processing...'
```

* flip-flops
  * https://bugs.ruby-lang.org/issues/5400

```ruby
DATA.each_line do |line|
  print(line) if (line =~ /begin/)..(line =~ /end/)
end
```

* block comments
  * Must be placed at the very beginning of a line

```ruby
=begin
comment line
another comment line
=end

class SomeClass
=begin
This is a top comment.
Or is it?
=end
  def some_method
end end
```

* core lib aliases
  * Where is `filter`?

```ruby
collect => map
inject  => reduce
detect  => find
select  => find_all
sprintf => format
length  => size
raise   => fail
```

* procs
  * `Proc.new` or `Kernel#proc`
  * No arity check
  * Non-local return
  * Do we really need them?
  * So many languages are getting by just fine with only lambdas...
  
  
* Single-quoted string literals

* A ton of obscure %- something literals
  * ```%s, %x, %w, %W, %r, %q, %Q, %, %i```

* Two types of block syntax

```ruby
3.times {
  puts "Hello!"
}

3.times do
  puts "Hello!"
end
```

```ruby
for i in 1..3
  puts "Hello, Kiev!"
end

3.times {
  puts "Hello, Kiev!"
}

3.times do
  puts "Hello, Kiev!"
end

3.times do
  puts %(Hello, Kiev!)
end

3.times do
  puts %Q(Hello, Kiev!)
end

3.times do
  puts 'Hello, Kiev!'
end

3.times do
  puts %q(Hello, Kiev!)
end
```

```ruby
# 1
result = []
for name in names
  result << name.upcase
end

#2
result = []
names.each do |name|
  result << name.upcase
end

#3
names.collect { |name| name.upcase }

#4
names.collect(&:upcase)

#5
names.map(&:upcase)
```

## The bad stuff

* So many `nil`s floating around

```ruby
pry(main)> "TOP".upcase
=> "TOP"
pry(main)> "TOP".upcase!
=> nil
```

* `autoload` (deprecated & scheduled for removal in 3.0)

* `and`, `or`, `not`
  * Those are not flow of control operators!
  * `and` & `or` have the same precedence

* Mutable strings
  * Even JavaScript got this right...
  
* Reassignable constants

```ruby
pry(main)> A = 5
=> 5
pry(main)> A = 6
(pry):39: warning: already initialized constant A
(pry):38: warning: previous definition of A was here
=> 6
pry(main)> Class = 3
(pry):40: warning: already initialized constant Class
=> 3
pry(main)> Class
=> 3
```

* Class variables
  * Just forget about them...
  * ...and use class instance variables instead

```ruby
class Parent
  @@class_var = 'parent'
  def self.print_class_var
    puts @@class_var
end end
class Child < Parent
  @@class_var = 'child'
end
Parent.print_class_var # => will print "child"
```

* **Sets** are not first-class citizens

* Poorly named methods
  * `Kernel#puts`
  * `Kernel#println`, anyone?
  * `Kernel#print`

* `defined?`
  * Is any of the values returned by defined? a boolean? 
  * Is this the right behaviour for a predicate method?
  
```ruby
[1] pry(main)> defined? 10
=> "expression"
[2] pry(main)> defined? Test
=> nil
[3] pry(main)> defined? TrueClass
=> "constant"
```

* Enumerable#include?
  * `Enumerable#include`s? 

* `Kernel#%`
  * `'%d %d' % [20, 10]`
  * `sprintf('%d %d', 20, 10)`
  * 
```ruby
sprintf(
  '%{first} %{second}',
  first: 20, second: 10
)
```

* `format('%{first} %{second}', first: 20, second: 10)
  * In what universe would you prefer this over `Kernel#format`???

* Perl-style global variables
  * `$:`
  * `$LOAD_PATH`
  * `$;` 
  * `$FIELD_SEPARATOR`
  * `$*`
  * `$ARGV`
  * JRuby defines the English aliases by default
  * Let’s pray MRI will follow suit soon

* Ruby 1.9 hash syntax

```ruby
{ :one => 1, :two => 2 }
{ :'one.1' => 1, :'two.2' => 2 }
{ 'one' => 1, 'two' => 2 }
{ 1 => 'one', 2 => 'two' }
```

```ruby
{ one: 1, two: 2 }
{ 'one.1': 1, 'two.2': 2 }
```

```ruby
{
  ala: :bala,
  porto: :kala,
  trala: :lala
}
```

* Perl-style regexp interactions

```ruby
irb(main)> 'Bruce' =~ /B(.*)/
=> 0
irb(main)> $~
=> #<MatchData "Bruce" 1:"ruce">
irb(main)> $1
=> "ruce"
irb(main)> Regexp.last_match
=> #<MatchData "Bruce" 1:"ruce">
irb(main)> Regexp.last_match(0)
=> "Bruce"
irb(main)> Regexp.last_match(1)
=> "ruce"
```

```ruby
irb(main)> 'Bruce'.match(/B(.*)/)
=> #<MatchData "Bruce" 1:"ruce">
irb(main)> 'Bruce'.match(/B(.*)/) do |m|
irb(main)>   puts m[0]
irb(main)>   puts m[1]
irb(main)> end
Bruce
ruce
=> nil
```

* The documentation is somewhat lacking

```ruby
irb(main)> 'x' !~ /x/
=> false
irb(main)> 'x' !~ /y/
=> true
```

* [The Ruby Stdlib is a Ghetto](http://www.mikeperham.com/2010/11/22/the-ruby-stdlib-is-a-ghetto/)

>The Ruby Stdlib is a Ghetto
>Nov 22, 2010
>Much of Ruby's standard library (the set of classes shipped with the Ruby VM itself)
>is old and crufty. For laughs, go look at the code for some of the classes that
>you've never used. Chances are it's from 2000-2003 and doesn't even look like
>
>The canonical example is Ruby's net/http library. Its performance and API are just
>terrible. (Side note: how do you know if an API is terrible? If you have to consult
>the docs even after having used the API for the past 5 years.) But because it's in
>the standard library, most people use it as the base for higher-level API
>abstractions (e.g. `httparty`, `rest-client`).
>
>So looking at Ruby's core RDoc, my suggested list for removal (where removal means
>move to a rubygem):

- Net::*
- DRb
- REXML
- RSS
- Rinda
- WEBrick
- XML
- A ton of legacy code (often last updated 2000-2003)
- Horrible APIs
  - `net/http` anyone?

Any others I missed? Will Ruby 1.9.3 or 2.0 get a good spring cleaning or will we have to live with these classes forever?

1. Move the important bits to the Core Library
2. Remove everything outdated/obscure
3. Leverage modern Ruby feature in the Standard Library
