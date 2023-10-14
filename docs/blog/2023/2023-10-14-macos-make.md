# Why MacOS make version is outdated?
> | macos | make | gnu |

MacOS `make` version is **3.81**. But the latest [GNU Make](https://savannah.gnu.org/projects/make/) version is 4.4.1.
Why so?

```shell
➜ make --version
GNU Make 3.81
Copyright (C) 2006  Free Software Foundation, Inc.
This is free software; see the source for copying conditions.
There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.

This program built for i386-apple-darwin11.3.0
```

The reason is licensing.  
⚠️ *3.81* is **GPLv2**, *3.82+* and later is **GPLv3**.


> ## [GNU make 3.81 released!](https://savannah.gnu.org/news/?id=4344)
> 
> *Item posted by [Paul D. Smith <psmith>](https://savannah.gnu.org/users/psmith) on Sat 01 Apr 2006 07:25:13 AM UTC.*
> 
> The next stable version of GNU make, version 3.81, has been released and is available for download from <ftp://ftp.gnu.org/gnu/make/>. 
> 
>  This version contains many bug fixes, as well as feature enhancements. There are also some backward-incompabilities. Please see the NEWS file that comes with the GNU  make distribution for complete details on user-visible changes.


> ## [GNU Make under GPLv3 going forward](https://savannah.gnu.org/news/?id=4896)
> 
> *Item posted by [Paul D. Smith <psmith>](https://savannah.gnu.org/users/psmith) on Wed 04 Jul 2007 07:39:26 PM UTC.*
> 
> All future releases of GNU Make will be licensed under GPLv3+ (GPL version 3 or later). I committed the necessary changes to the licensing and copyright statements into CVS today. 
> 
>  GNU Make 3.81 will be the last release under the previous license (GPLv2 or later).

You can read [HN](https://news.ycombinator.com/item?id=21812828) discussion regarding this topic.