# Rake

## Sample Rakefiles

```shell
➜ tree
.
├── Rakefile
└── rakelib
    └── mac_cheese.rake
```

`➜ cat Rakefile`

```ruby
task :default => "apple:go_to_store"

desc "Current dir"
task :pwd do
    puts "PWD = #{`pwd`}"
end

namespace :apple do
    desc "Go to Apple Store"
    task :go_to_store do
        puts "Going to the Apple Store"
    end
end

namespace :one do
    namespace :two do
        desc "Run task three"
        task :three do |t|
            puts "Nested task '#{t.name}'"
        end
    end
end

desc "Name prints 1st and 2nd arg"
task :name, [:first_name, :last_name] do |t, args|
    puts "First name is #{args.first_name}"
    puts "Last  name is #{args.last_name}"
end


namespace :gen do
    FORMATS = [:pdf, :html, :mobi, :epub]
    FORMATS.each do |f|
        desc "Generate the book in '#{f}'"
        task f do |t|
            sh "echo generate #{t.name}"
        end
    end
end
```

`➜  cat rakelib/mac_cheese.rake`

```ruby
desc "Make Mac and Cheese"
task :mac_and_cheese => [:boil_water, :buy_pasta, :buy_cheese] do
    puts "Making Mac & Cheese"
end

desc "Buy Cheese"
task :buy_cheese => [:go_to_store] do
    puts "Buying Cheese"
end

desc "Buy Pasta"
task :buy_pasta => [:go_to_store] do
    puts "Buying Pasta"
end

desc "Boild Water"
task :boil_water => [:buy_pasta, :buy_cheese] do
    puts "Boiling Water"
end

desc "Go to Store"
task :go_to_store do
    puts "Going to the Store"
end
```

## Rake Options & Commands

- `rake -T` (list available tasks)
- `rake -P` (list tasks & their dependencies)
- `rake -W` (list tasks & where they are defined)
- `rake -v` (verbose mode, echo system commands)
- `rake -t` (debugging mode)
- `rake -f` (use a specific Rakefile)

### `rake -T` (list available tasks)

```shell
➜ rake -T
rake apple:go_to_store           # Go to Apple Store
rake boil_water                  # Boild Water
rake buy_cheese                  # Buy Cheese
rake buy_pasta                   # Buy Pasta
rake gen:epub                    # Generate the book in 'epub'
rake gen:html                    # Generate the book in 'html'
rake gen:mobi                    # Generate the book in 'mobi'
rake gen:pdf                     # Generate the book in 'pdf'
rake go_to_store                 # Go to Store
rake mac_and_cheese              # Make Mac and Cheese
rake name[first_name,last_name]  # Name prints 1st and 2nd arg
rake one:two:three               # Run task three
rake pwd                         # Current dir
```

### `rake -P` (list tasks & their dependencies)

```shell
➜ rake -P
rake apple:go_to_store
rake boil_water
    buy_pasta
    buy_cheese
rake buy_cheese
    go_to_store
rake buy_pasta
    go_to_store
rake default
    mac_and_cheese
rake gen:epub
rake gen:html
rake gen:mobi
rake gen:pdf
rake go_to_store
rake mac_and_cheese
    boil_water
    buy_pasta
    buy_cheese
rake name
rake one:two:three
rake pwd
```

### `rake -W` (list tasks & where they are defined)

```shell
➜ rake -W
rake apple:go_to_store              /Users/halyph/Projects/tmp/Rakefile:10:in `block in <top (required)>'
rake boil_water                     /Users/halyph/Projects/tmp/rakelib/mac_cheese.rake:17:in `<top (required)>'
rake buy_cheese                     /Users/halyph/Projects/tmp/rakelib/mac_cheese.rake:7:in `<top (required)>'
rake buy_pasta                      /Users/halyph/Projects/tmp/rakelib/mac_cheese.rake:12:in `<top (required)>'
rake default                        /Users/halyph/Projects/tmp/Rakefile:1:in `<top (required)>'
rake gen:epub                       /Users/halyph/Projects/tmp/Rakefile:35:in `block (2 levels) in <top (required)>'
rake gen:html                       /Users/halyph/Projects/tmp/Rakefile:35:in `block (2 levels) in <top (required)>'
rake gen:mobi                       /Users/halyph/Projects/tmp/Rakefile:35:in `block (2 levels) in <top (required)>'
rake gen:pdf                        /Users/halyph/Projects/tmp/Rakefile:35:in `block (2 levels) in <top (required)>'
rake go_to_store                    /Users/halyph/Projects/tmp/rakelib/mac_cheese.rake:22:in `<top (required)>'
rake mac_and_cheese                 /Users/halyph/Projects/tmp/rakelib/mac_cheese.rake:2:in `<top (required)>'
rake name[first_name,last_name]     /Users/halyph/Projects/tmp/Rakefile:25:in `<top (required)>'
rake one:two:three                  /Users/halyph/Projects/tmp/Rakefile:18:in `block (2 levels) in <top (required)>'
rake pwd                            /Users/halyph/Projects/tmp/Rakefile:4:in `<top (required)>'
```

## Basic Use Cases

### Task arguments

```shell
➜ rake "name[John,Doe]"
First name is John
Last  name is Doe
```

### Nested Tasks

```shell
➜ rake one:two:three
Nested task 'one:two:three'
```

### Dependent Tasks

```shell
➜ rake mac_and_cheese
Going to the Store
Buying Pasta
Buying Cheese
Boiling Water
Making Mac & Cheese
```

### Default Task

```shell
➜ rake
Going to the Apple Store
```

### Dynamic task definition

```shell
➜ rake -T "gen"
rake gen:epub  # Generate the book in 'epub'
rake gen:html  # Generate the book in 'html'
rake gen:mobi  # Generate the book in 'mobi'
rake gen:pdf   # Generate the book in 'pdf'

➜ rake gen:pdf
echo generate gen:pdf
generate gen:pdf
```

### Silent run

```shell
# Silent OFF by default
➜ rake gen:html
echo generate gen:html
generate gen:html

# Silent ON, see `-s` option
➜ rake -s gen:html
generate gen:html
```

## Summary

Here I've shown only basic concepts, but there are much more (see *References*)

## References

- Video [Basic Rake by Jim Weirich](https://www.youtube.com/watch?v=AFPWDzHWjEY)
- Github repo [ruby/rake](https://github.com/ruby/rake)
  - [Rakefile Format](https://github.com/ruby/rake/blob/master/doc/rakefile.rdoc)
  - [Rake Command Line Usage](https://github.com/ruby/rake/blob/master/doc/command_line_usage.rdoc)
