# [WIP] Functional programming in Haskell - Part 1
> **tags**: | haskell | functional programming |

These notes are related to MOOC Stepik cource ["Функциональное программирование на языке Haskell"](https://stepik.org/course/75). This course is in Russian language and I decided to make notes. It might be useful for me in future or for somebody else.

## General thoughts which are not related to this course

In general, I've been doing programming language ecosystem discovery before jump into it. And here is the initial findings:

- [What I Wish I Knew When Learning Haskell by Stephen Diehl](http://dev.stephendiehl.com/hask/) - it's a huge writeup with tons of information.
- [State of the Haskell ecosystem](https://github.com/Gabriel439/post-rfc/blob/master/sotu.md) - it's a big report about ecosystem
  - [Educational resources](https://github.com/Gabriel439/post-rfc/blob/master/sotu.md#education) - this part is especially important for beginners
- [How I Start. Haskell With *Chris Allen*](https://howistart.org/posts/haskell/1) - Tutorial "how to write a package in Haskell and interact with the code inside of it."
- [Learn Haskell, by *Chris Allen*](https://github.com/bitemyapp/learnhaskell) - advices
- [Blog: "Haskell for all" by *Gabriel Gonzalez*](http://www.haskellforall.com). Gabriel blogs a lot about Haskell. But the next post might be interesting for beginners: 
  - [Detailed walkthrough for a beginner Haskell program](http://www.haskellforall.com/2018/10/detailed-walkthrough-for-beginner.html)
- [Exercism - Haskell](https://exercism.io/my/tracks/haskell) - **Exercism** is an online platform designed to help you improve your coding skills through practice and mentorship
- [The Haskell Tool Stack](https://docs.haskellstack.org/en/stable/README/) - **Stack** is a cross-platform program for developing Haskell projects
- [Haskell Docker image](https://hub.docker.com/_/haskell/)
- Cheat Sheets
  - [Basic Haskell Cheat Sheet](https://matela.com.br/pub/cheat-sheets/haskell-ucs-0.5.pdf)
  - [The Haskell Cheatsheet by *Justin Bailey*](http://cheatsheet.codeslower.com/)

## Development environment for this course

Right now I do not want to concentrate my attention on Haskell build tools. Also, I know that people do not recommend using Haskell Platform (see [here](https://github.com/bitemyapp/learnhaskell#also-do-not-install-haskell-platform)).
That's why I've decided to use docker image.

```bash
docker run -it --rm haskell:8
```

or you can mount current folder (assuming with source code) and run `ghci` or `ghc` from the container

```bash
docker run -it --rm -v $(pwd):/home haskell:8 /bin/bash

```

This approach is not perfect, but now you can avoid build tool issues.

## Status update

Unfortunatelly, my plan has been changed and I have decided to stop this course due to overload on other directions. But this particular course is cool and teacher is cool. I highly recommend it.
