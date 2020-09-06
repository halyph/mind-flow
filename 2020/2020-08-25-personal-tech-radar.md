# Personal Programming Languages Tech Radar - 2020 H2
> | python | java | scala |

Why "personal" Tech Radar? Well, [Technology Radar](https://www.thoughtworks.com/de/radar) was "invented" by ThoughtWorks company
(I guess, and I have zero motivation to prove this).
It is used for companies technology landscape evaluation. So, how I can use this for personal technology set definition?

We are living in a very dynamic world. Things are changing very fast. Software engineers like to try new "silver bullet" here-and-there.
You know *"the grass is always greener on the other side*" ;-) So, it's important to follow some guidance even for own personal development,
especially in Programming Languages space.

I have a weakness look around and try new "shiny" programming languages. But, now, I don't see any value in this. It's a waste of time. Better to work on something fundamental like math, instead of learning new syntax every year or two.

So, some time ago I defined a list of programming languages I am willing to invest in wiht some reasonnings. **This** list is defined for **2020 H2**. And I can assume that for **2021 H1** it will be updated.

So, following Tech Radar tradition I need to select some criterias.

The **Radar Ring Semantics** (in decreasing level of investment):

- **ADOPT**: technologies with broad adoption, in which I am willing to invest long-term. I feel strongly that the industry should be adopting these items. I use them when appropriate on our projects.
- **TRIAL**: worth pursuing. It’s important to understand how to build up this capability. I can try this technology on a project that can handle the risk.
- **ASSESS**: worth exploring with the goal of understanding how it will affect me.
- **HOLD**: Proceed with caution.

**Technology Domains**:

- Back-End
- Scripting/Automation
- Infrastructure
- Web
- Desktop
- Machine Learning
- System programming

## Technology Domains

### Back-End

This is the obvious part for me, since I've been using mainly two languages: **Java** and **Scala**.  
JVM is my primary platform, so all **.Net** programming languages are automatically removed from this list (i.e. C#, F# and so on).

What about other JVM languages:

- **Kotlin** (it is on hype in 2020). This languge could not bring anything new to my current tech stack Java/Scala. Even conceptually, this language is not even close to **Scala**. Yes, it's better than **Java**, but come on, why do I need a slightly different language?
- **Clojure**. It's dynamic, Lisp, and is not popular.
- **Groovy**. Unfortunatelly, it's like with **Kotlin**.
- **[Ceylon](https://ceylon-lang.org)**. According to [Github](https://github.com/ceylon), it's dead.

Other languages:

- **Golang**. Yep, it's very interesting alternative. But, I just could not use it after **Scala**. Golang syntax is very weak and limited. Ideologically, it's not my language for the backend.
- **Javascript** (via *Node.js*). It's not for me. I don't see any benefits there.

### Scripting/Automation

- **Python** is my main language in this area: 1) I've been using it at work; 2) popularity
- **Ruby** I used it many years ago. But now this niche is occupied by **Python**. But estetically **Ruby** is much better language than **Python**. I've been using **Python** only because of its total dominance. Sad, but true ;-(
- **Groovy**. Another sad story. **Groovy** was my main scriping languge for several years. Then there was a huge popularity decrease and I switched to **Scala**/**Python**.
- **Javascript** (via *Node.js*). I think it's pretty good alternative, but I am with **Python** now.
- **Golang** is well suited to CLI application. I think it's a perfect fit.
 
### Infrastructure

- **Golang** is very popular in this domain. Kubernetes and all other Cloud Native stuff it is **Golang** (mainly). Furtunatelly, we can use other languages (e.g. **Python**) while implementing Kubernetes operators. But, I would use **Golang** if it is required. Nothing domatic.
- **Rust**. Another interesting language, but it's much more complicated than **Golang** and community is not as big as in **Golang**.

### Web

There are *only* two candidates: **Javascript** and **TypeScript**.

All other languages ([Clojurescript](https://clojurescript.org), [CoffeeScript](https://coffeescript.org), [PureScript](https://www.purescript.org), [Scala.js](https://www.scala-js.org), [Elm](https://elm-lang.org)) are not interested for me because of popularity.

### Desktop

- **Java**. I haven't developed for Desktop for some time. But, I would use **Java** in case I need something right now and right away.
- **Swift**. It's a perfect fit for MacOS native app.
- **Objective-C** is slowly declining in popularity (but it should be already dead).
- **C++**. I don't want to touch this monster.
- **Python**. I think it's nice alternative. It has good bindings: [Qt](http://qt.io), [wxPython](https://www.wxpython.org), etc.

### Machine Learning

- **Python** is a king on the Machine Learning scene.
- **R**. This language is losing popularity in ML. But, it's still big. So, I should consider it.
- **[Julia](https://julialang.org)**. I know nothing about this languge.

### System programming

- **C** is simple and quite powerful. For something small, it's good enough.
- **C++**. Again, I don't want to touch this monster. It doesn't worth investments.
- **Rust** is a very interesting and powerful language. At least, I preffer **Rust** over **C++**.

## Summary

|             | Ring   | Back-End | Scripting, Automation | Infrastructure | Web    | Desktop | Machine Learning | System programming |
|-------------|--------|----------|----------------------|----------------|--------|---------|------------------|--------------------|
| Java        | ADOPT  | ADOPT    |                      |                |        | ADOPT   |                  |                    |
| Scala       | ADOPT  | ADOPT    |                      |                |        |         |                  |                    |
| Python      | ADOPT  |          | ADOPT                | ASSESS         |        | ADOPT   | ADOPT            |                    |
| Golang      | TRIAL  |          | ASSESS               | TRIAL          |        |         |                  |                    |
| Javascript  | ADOPT  |          | HOLD                 |                | ADOPT  |         |                  |                    |
| TypeScript  | ASSESS |          | HOLD                 |                | ASSESS |         |                  |                    |
| Haskell     | ASSESS | ASSESS   |                      |                |        |         |                  |                    |
| R           | ASSESS |          |                      |                |        |         | ASSESS           |                    |
| C           | ADOPT  |          |                      |                |        |         |                  | ADOPT              |
| C++         | HOLD   |          |                      |                |        | HOLD    |                  | HOLD               |
| Rust        | HOLD   | HOLD     |                      | HOLD           |        |         |                  | HOLD               |
| Swift       | HOLD   |          |                      |                |        | HOLD    |                  |                    |
| Kotlin      | HOLD   | HOLD     |                      |                |        |         |                  |                    |
| Clojure     | HOLD   | HOLD     |                      |                |        |         |                  |                    |
| Objective-C | HOLD   |          |                      |                |        | HOLD    |                  |                    |
| Groovy      | HOLD   |          | HOLD                 |                |        |         |                  |                    |
| Ruby        | HOLD   |          | HOLD                 |                |        |         |                  |                    |
| Julia       | HOLD   |          |                      |                |        |         | HOLD             |                    |
