# Python is the second best language for anything
<!-- tags: python -->

## Main Part

**Disclaimer**: It's another blah-blah post, feel free to read Hacker News :-P it will be more useful for you.

What other programming languages do I associate with Python, or to be precise what other scripting languages? I would say the following:

- [Ruby](https://en.wikipedia.org/wiki/Ruby_(programming_language))
- [Groovy](https://en.wikipedia.org/wiki/Apache_Groovy)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
- [Perl](https://en.wikipedia.org/wiki/Perl)
- [PHP](https://en.wikipedia.org/wiki/PHP)
- [Lua](https://en.wikipedia.org/wiki/Lua_(programming_language))
- [Tcl](https://en.wikipedia.org/wiki/Tcl)
- [Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) (_and similar shell scripting languages_)
- [Powershell](https://en.wikipedia.org/wiki/PowerShell)
- [VBA](https://en.wikipedia.org/wiki/Visual_Basic_for_Applications)
- [Autohokey](https://www.autohotkey.com/)
- [AutoIt](https://www.autoitscript.com)
- [newLISP](https://en.wikipedia.org/wiki/NewLISP)
- [R](https://en.wikipedia.org/wiki/R_(programming_language))
- [Matlab](https://en.wikipedia.org/wiki/MATLAB)
- [Maple](https://en.wikipedia.org/wiki/Maple_(software))

Actually, I decided to make this list only as an exercise for myself, to identify from a historical perspective what I touched during all these years. 

I used some of these languages at the university or early in my career. I.e. I don't know the status quo for them, new features, their communities, etc. But all of them somehow build Python-association in my brain in a way I can use Python instead of them and be "happy".
If you look closer at this list you will notice some domain-specific language (like GUI automation, scripting, and math tools).

But the true **Python** competitor in general sense is **Ruby**. These two are very similar in terms of exploitation, and I preferred Ruby before my personal Python era began.

I was not too fond of Python. But since everybody around me has been using Python in some or another way, I decided to use it as well, to simplify knowledge/tool sharing, contribution to other tools, etc.
Even today, I am not a big Python fan, but there is convenience: a massive amount of libs, books, blogs, etc. It's like a universal hammer for everything.

So, what does it mean _"Python is the second best language for anything"_ for me? 

It means I will start prototyping any simple things, or throw-away scripts in Python. Even if I don't know the domain I am 99% sure there is at least some library for my current problem.

There are several exceptions:

- **Web**: Javascript
- **System Programming**: C
- **Back-End**: Go, Java, Scala
- **CLI**: Go
- **Desktop**: Java

The following domains will be covered by Python ([PoC](https://en.wikipedia.org/wiki/Proof_of_concept), my personal projects):

- Scripting
- Infrastructure
- Machine Learning/Data Science/Data Analysis/Data Engineering
- CLI: *when I don't need to distribute the app*

Again, Python is not the best language in the world, it definitely has some sort of ugliness, but it's popular, and I accepted this.

## Concerns

### Concurrency

This topic is not well aligned in my head when I am talking about Python and concurrency in the same sentence. I would use JVM languages (Java, Scala)
or Go instead of Python when I need to implement something performant and concurrent.

### Packaging and Distribution

It's not related to Python only, but to other scripting languages as well. If you need to distribute some Python app you have to be prepared.
Your users must know how to use [Pip](https://pip.pypa.io) and [virtual environment](https://docs.python.org/3/library/venv.html). But it's not the end of story.

How do you package/assemble your app? There are so many ways for building your Python app, see [PyPA Projects](https://packaging.python.org/en/latest/key_projects/).
I don't understand why such old community hasn't agreed on some recommended build tools. Why do they need such crazy numbers of different tools?
But I am talking as seasonal Python user. Maybe there are some reason. Anyway, what I wanted to say: I try to avoid as much as possible any Python tools ceremonies and
use only simplest possible standard tools: `pip`, `venv` and `requirements.txt`.

Just check [Distributing Python Modules](https://docs.python.org/3.10/distributing/index.html), and you will find such creatures: [distutils](https://docs.python.org/3.10/library/distutils.html), [setuptools](https://setuptools.pypa.io), [wheel](https://wheel.readthedocs.io) and so on. What? Really? 

Do not forget, Python went public in 1991 (31 years ago). FTW!

P.S. [Poetry](https://python-poetry.org) is a new cool kid in Python community. Maybe it will solve all problems, but it's not yet a standard and that's why I am not ready for big investments.
