# How to setup Ruby/Rails development environment, Part 1 - Ubuntu VM
> | ruby | rails | linux |

The most popular Ruby/Rails development platform isn't Windows. There are a lot of plug-ins, tutorials and blogs about Ruby/Rails on \*nix like system. But, I'm Windows user (yes I know, Linux - rules!), so how can I use all community knowledge and easily apply it?  
I've decided setup VMWare VM with [Ubuntu Server v.9.10](http://www.ubuntu.com/). And perform all Ruby/Rails development there via Putty (SSH).  
I assume that You have installed Ubuntu VM.  
  
This post is base on the next articles:  

* [Install Ruby on Rails on Ubuntu Karmic Koala 9.10](http://www.hackido.com/2009/11/install-ruby-on-rails-on-ubuntu-karmic.html)
* [Installing Ruby on Rails on Debian/Ubuntu](http://wiki.rubyonrails.org/getting-started/installation/linux)
* [Ubuntu Community documentation - RubyOnRails](https://help.ubuntu.com/community/RubyOnRails)      
* [Rails Development On Ubuntu](http://blog.michaelgreenly.com/2009/03/rails-development-on-ubuntu.html)
* [How Do I Enable Remote Access To MySQL Database Server?](http://www.cyberciti.biz/tips/how-do-i-enable-remote-access-to-mysql-database-server.html)

**Step 1:** Install Ubuntu VM - done

**Step 2:** Install [Putty](http://www.putty.org/) on Windows  

**Step 3**: Configure Putty - Ubuntu VM connection  
Check Ubuntu VM IP: `ifconfig`. Apply this VM IP in Putty setting. All next steps will be performed via Putty console  

**Step 4:** Update Ubuntu installation  

```bash
sudo apt-get update  
sudo apt-get dist-upgrade  
```
  
**Step 5**: Install all necessary libs  

```bash
sudo apt-get install build-essential  
sudo apt-get install ruby ri rdoc mysql-server libmysql-ruby ruby1.8-dev irb1.8 libdbd-mysql-perl libdbi-perl libmysql-ruby1.8 libmysqlclient15off libnet-daemon-perl libplrpc-perl libreadline-ruby1.8 libruby1.8 mysql-client-5.1 mysql-common mysql-server-5.1 rdoc1.8 ri1.8 ruby1.8 irb libopenssl-ruby libopenssl-ruby1.8 libhtml-template-perl mysql-server-core-5.1 libmysqlclient16 libreadline5 psmisc
```

**Step 6:** During installation MySQL will ask to setup credentials:  

```bash
user = "root"  
password = "root"
```

Check Ruby version  

```bash
$ ruby -v
ruby 1.8.7 (2009-06-12 patchlevel 174) [i486-linux]
```

**Step 7**: Install RubyGems  

```bash
wget http://production.cf.rubygems.org/rubygems/rubygems-1.3.6.tgz  
tar xvzf rubygems-1.3.6.tgz  
cd rubygems-1.3.6  
sudo ruby setup.rb  
  
sudo ln -s /usr/bin/gem1.8 /usr/bin/gem
```

**Step 8**: Install Rails  

```bash
sudo gem install rails 
```

**Step 9**: Install SQLlite  

```bash
sudo apt-get install sqlite3 libsqlite3-dev  
sudo gem install sqlite3-ruby    
```
**Step 10**: Install MySQL client  

```bash
sudo apt-get install libmysqlclient-dev  
sudo gem install mysql
```

**Step 11**: Test your Rails instalation  

```
$ rails myrailsapp
```