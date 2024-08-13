# Lambda Days - Krakow, 2019 - Report
> | scala | conference | functional programming | haskell |

I attended [Lambda Days](http://www.lambdadays.org/lambdadays2019) conference (21-22 February, 2019) in Krakow, Poland.

So, what's so special in this conference? The main idea is to attend one conference to check different functional programming communities: Scala, Erlang, Haskell, Elixir, F#, Lisp, Clojure, OCaml, Elm, PureScript, etc. And it's amazing how different FP languages solve the same/similar problems.

Here is the list of talks I've attended (some talks have been excluded from this list because I don't like it at all):

- [Day 1 (February 21, 2019)](#day-1-february-21-2019)
  - [1 - Keynote: F# Code I Love by Don Syme (*F# Language Designer*)](#1---keynote-f-code-i-love-by-don-syme-f-language-designer)
  - [2 - FP Design Patterns in Micro-Service Inter-Process Communication by Viaceslav Pozdniakov](#2---fp-design-patterns-in-micro-service-inter-process-communication-by-viaceslav-pozdniakov)
  - [3 - Empowering the Quantum revolution with Q# by John Azariah](#3---empowering-the-quantum-revolution-with-q-by-john-azariah)
  - [From Haskell to C#, A story of culture shocks and happy reunions by Øystein Kolsrud](#from-haskell-to-c-a-story-of-culture-shocks-and-happy-reunions-by-øystein-kolsrud)
  - [4 - Elm, Fable, and the Practical Implications of Programming Language Philosophy by Michael Newton](#4---elm-fable-and-the-practical-implications-of-programming-language-philosophy-by-michael-newton)
  - [5 - One year of using F# in production at SBTech by Anton Moldovan](#5---one-year-of-using-f-in-production-at-sbtech-by-anton-moldovan)
  - [6 - (Dys)functional DDD by Jarek Ratajski](#6---dysfunctional-ddd-by-jarek-ratajski)
- [Day 2 (February 22, 2019)](#day-2-february-22-2019)
  - [7 - Scala superpowers: effortless domain driven design by Bartosz Mikulski](#7---scala-superpowers-effortless-domain-driven-design-by-bartosz-mikulski)
  - [8 - Effective Data Engineering using higher kinded types by Animesh Kumar](#8---effective-data-engineering-using-higher-kinded-types-by-animesh-kumar)
  - [9 - Fast \& Functional by Michał Płachta](#9---fast--functional-by-michał-płachta)
  - [10 - Behind collaborative text editing by Bartosz Sypytkowski](#10---behind-collaborative-text-editing-by-bartosz-sypytkowski)
  - [11 - Teaching Functional Programming by Michael Sperber](#11---teaching-functional-programming-by-michael-sperber)

---

## Day 1 (February 21, 2019)

### 1 - Keynote: F# Code I Love by [Don Syme](https://github.com/dsyme) (*F# Language Designer*)

- [Video](https://www.youtube.com/watch?v=MGLxyyTF3OM)
- [@dsyme](https://twitter.com/dsyme) 

The most interesting for me was this paper: [The Early History of F# (HOPL IV - first draft)](https://fsharp.org/history/hopl-draft-1.pdf). This paper has 36 pages, you will like it if you like **IT history**.

### 2 - FP Design Patterns in Micro-Service Inter-Process Communication by [Viaceslav Pozdniakov](https://github.com/vipo)

> Design of correct and yet simple inter-process communication in micro-service architecture is a tough thing to do: communication protocols might be sync or async, some APIs use request/response model while others use streaming and so on. In this talk we will discuss which micro-service IPC design problems we (Wix.com) faced and how we solve them using FP building blocks: monads, semigroups, etc. Obviously, introduction of FP design patterns at our scale (>500 developers) is a huge effort, so we will also discuss an execution process of such changes.

- Video
- [Slides](https://speakerdeck.com/vipo/fp-design-patterns-in-micro-service-inter-process-communication)
- [@poznia](https://twitter.com/poznia)

The talk was interesting in terms of introducing FP concepts in big legacy Scala code base.

### 3 - Empowering the Quantum revolution with Q# by John Azariah

This talk was a little bit strange. The only outcome - I am motivated to study this subject.

### From Haskell to C#, A story of culture shocks and happy reunions by [Øystein Kolsrud](https://github.com/kolsrud)

> Six years ago, I joined Qlik as a software engineer in a group developing products in C#. My previous experience came primarily from Haskell and C++, but with C# I quickly realized that I could leverage my knowledge of functional programming also in this object oriented language! And (to the great confusion of my colleagues) I did! This talk focuses on my experience of using C# with a touch of Haskell and the reactions I got from my colleagues when doing so.

- Video
- [@oystein_kolsrud](https://twitter.com/oystein_kolsrud)

Shared experience of FP "injection" in OOP C# world, social aspects etc. There were some interesting ideas and case studies.

### 4 - Elm, Fable, and the Practical Implications of Programming Language Philosophy by Michael Newton

> On the surface, Elm and Fable (the F# to JavaScript compiler) look very similar - functional, ML based languages with a focus on pragmatism over complexity. In fact, the most common way of writing JavaScript in Fable is via the "Elmish" library which implements the, well, Elm architecture. But the philosophy behind the two languages is very different. Take a tour of the two languages with someone who's used both professionally, and we'll investigate how the different ideas behind them have lead to different features, different ecosystems, and even differences in how teams work with them.

- [Site](https://blog.mavnn.co.uk/)
- [@mavnn](https://twitter.com/mavnn)

Actually, it was "comparison" of two languages design, their origins and motivation.

### 5 - One year of using F# in production at SBTech by [Anton Moldovan](https://github.com/antyadev)

> In 2017 we started using F# for building high-load push-based queryable API and complex stateful stream processing for our core platform. At that time almost nobody has had F# experience but we decided to give a try. And on this talk, I will share our experience with adopting F# on real projects at SBTech.
>
> Agenda:
>
> - Why did we choose F# over C#?
> - A high-level overview of the architecture of our push-based queryable API.
> - Adopting F# for C#/OOP developers (inconveniences, C# interoperability, code style,  DDD, TDD)

- [medium](https://medium.com/@AntyaDev)
- [@AntyaDev](https://twitter.com/AntyaDev)
- [https://nbomber.com/](https://nbomber.com/) - Load test any system

The speaker shared his experience with F# and what motivated him to implement [NBbomber](https://nbomber.com/).

### 6 - (Dys)functional DDD by [Jarek Ratajski](https://github.com/jarekratajski)

> Domain Driven Design patterns are commonly used in business applications.
> There is, however, a visible mismatch when we look at them from a functional programming perspective. Some concepts seem to fit perfectly: like event sourcing. Some, however, seem to be built around mutability or side effects like aggregates or commands in CQRS. Some are just hard to grasp like domain events, integration events.
> 
> In this talk we will try to revisit the core concepts of DDD from a functional perspective and build a simple system using a little bit more functional approach.

- [@jarek000000](https://twitter.com/jarek000000)
- [Github: talk-related sources](https://github.com/jarekratajski/dysfunctional_ddd)

## Day 2 (February 22, 2019)

### 7 - Scala superpowers: effortless domain driven design by [Bartosz Mikulski](https://github.com/mikulskibartosz)

> Scala superpowers: effortless domain driven design
> Don't come to this talk. You will not hear anything cool. No new libraries, languages. No clever code. No buzzwords even. I want to show you how you can use the features you already know to write less code and make the code so easy to understand that people who join your project can be productive on their first day. You didn't come to a tech conference to see that, did you? Your new, shiny toys are not here. Go somewhere else ;)
>
> I want to show the audience how to use built-in Scala features (like case classes, value classes, structural types) to create the basis of a domain model. I want to show them the benefits of taking advantage of the type system and not using primitive types everywhere. In particular, I want to show how types can encode validation rules and make the code shorter and easier to test.

- [Slides](https://github.com/mikulskibartosz/effortless-domain-driven-design/)
- [@mikulskibartosz](https://twitter.com/mikulskibartosz)
- [medium](https://mikulskibartosz.name/)

### 8 - Effective Data Engineering using higher kinded types by Animesh Kumar

> In order to create a canonical framework for real-time and batch data processing in the order of 10s of TBs per day, a general purpose framework to instantiate and extend data pipelines is presented here that can be used to ingest, process, and derive ML based inferences from the base data.

The speaker has shared his experience of building abstractions on top of Flink and Spark.
He said that **Flink** it's for real-time process and **Spark** is for batch data processing.

### 9 - Fast & Functional by [Michał Płachta](https://github.com/miciek)

>  In this talk we are going to create a functional and blazingly fast microservice. We will use functional programming abstractions to quickly mix & match different HTTP libraries, state implementations and concurrency configurations. Each step will be followed by a performance analysis using different tools from JVM toolbox. This talk is for you if you want to see how cats IO monad, async-profiler, flame graphs and wrk are used together to create nanoseconds-fast Scala service for YouTube videos statistics.

- [Slides](https://speakerdeck.com/miciek/fast-and-functional-66b89d68-5d8c-4d2b-9bc2-5fa4adf16734)
- [Github - influencer-stats](https://github.com/miciek/influencer-stats) - related repo
- [Site](https://michalplachta.com/)
  - [Talks](https://michalplachta.com/talks/)
- [@miciek](https://twitter.com/miciek)

This talk was very interesting: Scala, abstraction, functional programming, performance, etc.

### 10 - Behind collaborative text editing by [Bartosz Sypytkowski](https://github.com/Horusiath)

> We’ll discuss the topic, that is well known from products such as Google Docs or Etherpad, and explain how Conflict-free Replicated Data Types will allow us to expand it into new territories. We'll take a peer-to-peer approach, with no central servers, constant internet connectivity or human assisted conflict resolution.
> 
> During this talk we'll focus on Replicated Growable Array data structure and how it allows us to build peer-to-peer collaborative text editors. What's more, we'll also cover how to properly optimize it to address issues of most common implementations.

- [Slides](https://www.slideshare.net/BartoszSypytkowski1/collaborative-text-editing-132892964)
  - **References**:
    - [Operational transformation discussion on HN](https://news.ycombinator.com/item?id=12311984)
    - [Video: JSON CRDT by Martin Kleppman](https://www.youtube.com/watch?v=B5NULPSiOGw)
    - [Article: Rope data structure](https://www.geeksforgeeks.org/ropes-data-structure-fast-string-concatenation/)
    - [PDF: Blockwise Replicated Growable Arrays](https://pages.lip6.fr/Marc.Shapiro/papers/rgasplit-group2016-11.pdf)
    - [Github: Examples of CRDT implementations](https://github.com/Horusiath/crdt-examples/)

This talk was interesting. The speaker highlighted the different approaches for handling "collaborative text editing". The slides are pretty detailed and can be used as an entry point into the subject.

### 11 - Teaching Functional Programming by [Michael Sperber](https://github.com/mikesperber)

> You want to teach functional programming to someone else: To enable fellow developers, as a professional trainer, or to teach students. However, as natural as functional programming feels to us, it is hard to teach well. In particular, professional functional languages are powerful tools for development, but are not necessarily the best tools beginners. This talk is about teaching functional programming well using the Program by Design / DeinProgramm approach. It will give an overview of effective teaching approaches, techniques and tools, and highlight pitfalls.

- [Site](http://www.deinprogramm.de/sperber/)
- [@sperbsen](https://twitter.com/sperbsen)

The speaker has tried to present his FP teaching methods. The speaker has been using [Racket](https://racket-lang.org/) language (based on the Scheme dialect of Lisp) while teaching the students. He claims that this tool is quite effective.
A lot of people have questions about the proposed methods. I suggest watching the video.

Another interesting point: he said the Python is not very good for teaching beginners programming (we had offline discussion about this).