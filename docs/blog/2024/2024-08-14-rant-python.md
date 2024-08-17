# Everybody Python, FTW?
> | python |

WARN: It's *"Old Man Yells at Cloud"* kind of post.

Just check any languages' popularity site, job sites, or ML/AI madness. People are running and screaming "P-y-t-h-o-n!".  
Python is top of the top.

I need to use this language because it's what everyone around me is using. I can't just stick with Ruby, Clojure, or any other language I prefer because the team relies on Python. To collaborate effectively, contribute meaningfully, and improve the existing codebase, I have to work with the tools and languages that are standard here.

I don't like Python due to many reasons:

## Package/Dependency management

How come language created in 1991 still has so [many package managers](https://dublog.net/blog/so-many-python-package-managers/)? Community and/or core team could **not** agree upon some standard way of doing things? 

Yes, I know there is several PEPs related to this issue, but the fact is - we still need to choose the tool.  
Even Ruby has smaller numbers of package management tools (last time I worked with Ruby it was `bundler` + `rake`)

- **Java** has two popular solutions: `maven` and `gradle`
- **Scala** has one dominated `sbt` and less popular `mill`
- **Go**, **Rust**, **Elixir** they all have only one way for management dependencies
- **OCaml** has `opam`
- **Haskell** has `stack` and `cabal`

In Python we have many moving parts:
- manage Python versions: `pyenv`, `conda` (like `rbenv`, `sdkman`)  
- virtual environments `venv` (standard), `virtualenv`, `pipenv`
- [package managers](https://dublog.net/blog/so-many-python-package-managers/), good luck there. Many can say "use `requirements.txt` or `Poetry`". Really? 

What about [PEP 20 – The Zen of Python](https://peps.python.org/pep-0020/) *"There should be one and preferably only one obvious way to do it"*. Never heard?! Nah, "it's not applied to package and dependency management".

If `pip` and `venv` are the answer, then why have people created so many 3rd-party solutions?

I'm certain someone might approach me and say, "You’ve mixed up the tools; you should be using A, B, and C".  
And that’s exactly the issue - there's too much inconsistency in the community, a lack of clear standards, and overall, it's just a mess.

## Language

This is purely a matter of personal preference:

1. *I didn't like indentation at first*, but I’ve come to accept it (even Scala 3 gave in to this). Now, thanks to a bit of [Stockholm syndrome](https://en.wikipedia.org/wiki/Stockholm_syndrome), I've actually grown to like it.
2. The "Pythonic Way" - just follow the crowd and don't ask questions.
3. *Type hints* - seriously? How many years will it take to fully embrace this? Just check [awesome-python-typing](https://github.com/typeddjango/awesome-python-typing), we need more tools.
4. The `self` parameter - need I say more?
5. Deeply nested `for`-comprehensions are a nightmare to read, so instead, we get clunky `map`/`filter`/`reduce` where chaining is practically impossible.

## Code formatters

After Go (`gofmt`) and Scala (`scalafmt`, `scalafix`) where we have only several options for code formatting Python is exceptional:

- several fat formatters (`black`, `autopep8`, `yapf`)
- imports formatters (`autoflake`, `isort` and so on)
- many small/micro/do-one-things formatters (15+)  

and many more, check this repo [awesome-python-code-formatters](https://github.com/life4/awesome-python-code-formatters).

Remember *"There should be one and preferably only one obvious way to do it"* - it's a joke.

## The End

There are plenty of other great languages for scripting, prototyping, ML/AI, and more, but Python has clearly come out on top. I’ve been using it out of practicality and common sense. However, I can’t help but hope that Python’s reign will eventually decline, making room for other languages to take its place.