# *nix-like environments for Windows
> | cygwin | linux | MinGW |

\*nix like environment is good for developer and sysadmins, and really
useful for end-user. That's why we've got KDE, Gnome and similar. But, I
like it a lot even if I'm Windows user ;-). There are several cases to
set up \*nix environment on Windows:

* setup Virtual Machine with some Linux distributive and you've got
fully functional Linux. You can use [VMware](http://www.vmware.com/) or
[VirtualBox](http://www.virtualbox.org/). 
* or you can setup Linux-like environment in Windows (i.e. bash, gcc,make, grep, find, sed, etc.).

Here is "my" list of choice for such environments:

1. [MinGW](http://www.mingw.org/) - Minimalist GNU for Windows. My top
choice if you need GNU development programming tool set. Additional, if
you need bash and similar tools install MSYS - general purpose command
line environment.
2. [Cygwin](http://cygwin.com/) -  is a Linux-like environment for
Windows. It's very powerful if you need to develop OS-portable
application on windows (it's provide substantial Linux API
functionality).
3. [GnuWin32](http://gnuwin32.sourceforge.net/) - provides ports of tools
with a [GNU](http://www.gnu.org/) or similar open source licenses. Check
package list on their home page.
4. [UWIN](http://www2.research.att.com/sw/tools/uwin/) - it's the
similar to MinGW and GnuWin32, but less popular.

I prefer to use MinGW/MSYS and Cygwin because they have great community
support.
