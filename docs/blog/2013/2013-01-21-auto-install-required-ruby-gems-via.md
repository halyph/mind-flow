# Auto install required Ruby gems via script
> | ruby |

When you are writing Ruby scripts for yourself it's cool until you need to distribute it. It might happen (as usual it is) that your scripts requires one or more gems. It means that the consumer of your script should additionally setup all required gems. But it looks ugly. There is a nice simple solution which provide simple way for automatic gem install.
Let's imagine that we are using some gem in our script, to be concrete, I've picked artii gem as a sample:

```ruby
begin
  gem "artii"
rescue LoadError
  system("gem install artii")
  Gem.clear_paths
end
 
require 'artii'
 
a = Artii::Base.new
puts a.asciify('Blog!')
```

Let's run it:

```bash
$ jruby text.rb
Successfully installed artii-2.0.3
1 gem installed
  ____  _             _
 |  _ \| |           | |
 | |_) | | ___   __ _| |
 |  _ <| |/ _ \ / _` | |
 | |_) | | (_) | (_| |_|
 |____/|_|\___/ \__, (_)
                 __/ |
                |___/
 
$ jruby text.rb
  ____  _             _
 |  _ \| |           | |
 | |_) | | ___   __ _| |
 |  _ <| |/ _ \ / _` | |
 | |_) | | (_) | (_| |_|
 |____/|_|\___/ \__, (_)
                 __/ |
                |___/
```

As you can see, when we run script 1st time it installs artii gem, but when we run this script 2d time it identified that gem has been installed already.

## Links

- [SO: After installing a gem within a script, how do I load the gem?](http://stackoverflow.com/questions/9384756/after-installing-a-gem-within-a-script-how-do-i-load-the-gem)