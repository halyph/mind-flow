# Distribute application as Native Single binary
> | golang | python | rust | haskell | ocaml | ruby | lisp |

Some time ago I had a pleasure to implement Ruby-based tool which theoretically must be easy to install and have no or limited dependencies.
I've picked `JRuby` and packed/distribute the application as a `jar`. I.e. JRE was the single dependency I had. In general it was very nice distribution model despite the fact that non-Java users must install JRE (Java SE Runtime Environment) to run the application.

All other approaches like Ruby, Python, Perl, etc. were not acceptable as they requires additional user's efforts for tool installation and/or package distribution. 

The idea was/is to have single native binary for all major platforms which requires no dependencies. Simply copy and run.

Now, the question: did I have other alternatives to implement this tool? Could it be implemented as native static binary? - Answer - YES. But, at that time there were only two mature solutions (acceptable for me): C and C++. And neither of them were very good for tool implementation and prototyping at the same time. Also, as far as I know, it's not a simple task to implement really cross-platform app, at least for Windows/Linux/OSX in C/C++. It adds additional maintenance efforts which I tried to avoid.

Looking now at this task I can say that this king of application is nice to implement in [Go](https://golang.org). Go has everything I need for really cross-platform application development and single static binary output which is awesome for tools/utilities writers.

I decided to look around and understand which other popular languages support compilation/packaging to native (semi-)single static binary. The term _"semi-single"_ static binary will be explained later.

## Compilers

Quick googling give us the next languages:

* [Rust](https://www.rust-lang.org)
* [Haskell](https://www.haskell.org)
* [OCaml](https://ocaml.org/)
* [Lisp](http://www.cliki.net/creating%20executables)
  * [SBCL](http://www.sbcl.org/) 
  * [Clozure CL](http://ccl.clozure.com/)
* [D](http://dlang.org/)

**Haskell**, **OCaml** and **Lisp** are not widely used. And these langs should be picked carefully due to language specific learning curve.

**D** language is not young and has small community. But it's much simpler and clean compared to C++, IMHO.

**Rust** is the new hype along with **Go**. I guess it will be good alternative to C/C++. Also, the language is much more powerful compared to **Go**, it might be additional selling point.

## Dynamic Languages

There is no direct compilation from interpret/dynamic language to native static binary. But, it's possible to pack application with language runtime into "archive"/executable to behave like static native binary.

- Python [freezing](http://docs.python-guide.org/en/latest/shipping/freezing/) (To _"Freeze"_ your code is to distribute to end-users as an executable which includes a bundled Python interpreter)
  - [bbFreeze](https://pypi.python.org/pypi/bbfreeze)
  - [py2exe](http://www.py2exe.org)
  - [pyInstaller](http://www.pyinstaller.org)
  - [cx_Freeze](http://cx-freeze.sourceforge.net)
  - [py2app](https://pythonhosted.org/py2app/)
- Perl
  - [PAR Packager](http://search.cpan.org/~rschupp/PAR-Packer-1.026/lib/pp.pm)
  - [Perl2Exe](http://www.indigostar.com/perl2exe.php)
- Node.js, Here is [sample approaches](https://github.com/nwjs/nw.js/wiki/how-to-package-and-distribute-your-apps)
- Ruby:
  - [RubyScript2Exe](http://www.erikveen.dds.nl/rubyscript2exe/)
  - [OCRA](http://ocra.rubyforge.org/)

Based on the list above, **Python** has many alternatives to accomplish single distribution artifact task. I.e. it's better to pick Python than other alternatives. Also, it looks like **Ruby** has limited and poor choices, i.e. it's not suitable for this kind of task.

## Summary

IMHO, **Go** has the most appealing tool chain for accomplish this task.