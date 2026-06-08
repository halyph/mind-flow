# When Tech Stack Chaos Hits Hard
<!-- tags: thoughts -->

![thumbnail](2025-11-15-tech-chaos/pic0.jpg)

Recently I read [Steve Francia](https://spf13.com/about/)'s post [Why Engineers Can't Be Rational About Programming Languages](https://spf13.com/p/the-hidden-conversation/) which deeply resonates with my experience.

Here is key idea:

> Instead of asking “which language is best?” we need to ask “what is this language going to cost us?” Not just in salaries, but in velocity, in technical debt, in hiring difficulty, in operational complexity, in every dimension that actually determines whether you survive.  
> ...  
> Choosing a programming language is the single most expensive economic decision your company will make. It will define your culture, constrain your budget, determine your hiring pipeline, set your operational costs, and ultimately dictate whether you can move fast enough to win your market.

I want to share some personal experiences, lessons learned, and thoughts. Of course, everything is subjective.

## Some anecdotes

*“The story, names, and characters are fictitious… or not. Reality is complicated.”*

### Case 1: Scala Playground

Team **A** built services in Scala using different frameworks: [Finagle](https://twitter.github.io/finagle/), [Spray](https://github.com/spray/spray), and possibly [Lift](https://www.liftweb.net/). It was early Scala days - no FP, just people experimenting with new toys.
Eventually, Team **A** shifted focus, leaving these services behind and handing them over to Team **B**, who primarily used Java + Spring.

*Drums are drumming 🥁…*

Team **B** did **not** enjoy touching this new pile of "fun". The main objective became: *avoid it as much as possible*.

### Case 2: Multiple Domains, Multiple Stacks

A team had many services split across **Java** and **Scala**, with two main domains:

- **Domain 1:** Java + [Spring](https://spring.io/), Scala + [Play](https://www.playframework.com/), Java + [Quarkus](https://quarkus.io/)
- **Domain 2:** Scala + [http4s](https://http4s.org/) + [Cats](https://typelevel.org/cats/), Scala + Spark

Some engineers preferred Domain 2, some Domain 1. But even within Domain 1, new joiners often knew only Spring and not Scala + Play.

This "freedom" of choice created a ticking *tech debt* bomb. No one could be an expert in all services, troubleshooting was hard, and switching between domains was painful. And all of this happened organically - not inherited from previous teams.


### Case 3: Microservices and the "Unloved Stack"

A team had many Scala + [akka-http](https://github.com/akka/akka-http) services with microservice templates, making maintenance easy. Anyone could contribute - maintenance paradise.

Then they merged with a team whose services were in Java + Spring Boot. As the original maintainers left, the remaining team had to take over.

Guess what happened: there was *so much passion* whenever we had a bug or a feature request. People fought over who would contribute.  
Of course, I’m joking.

Everyone avoided the "magical" Spring stack. One brave engineer became the main (and only) contributor. It became his destiny.

When he went on vacation or got sick, the whole system paused:

- "Don't breathe" they said
- "Let this shit peacefully run" 🤫

No rotation meant knowledge was concentrated in a single person - a perfectly engineered *"artificial tuberculosis island"* ☣️.

### Case 4: Same Story, Different Tech

A team with many **Go** services enjoyed similar structure, design approaches, tooling. Then they inherited a Java + Spring Boot service from another team.

The story repeated itself: volunteers were scarce, knowledge concentrated, and maintenance painful. Different team, same outcome.

### Case 5: Haskell Drama

Some smart engineers wrote services in **Haskell**. Shiny and elegant.

But when the Haskell experts left, no one could maintain them. The only solution: rewrite in a more maintainable language - one where you can actually find developers.

## Summary

*"Common sense isn’t that common. And sometimes it’s not even sense"*

- **Fewer languages = better outcomes.** Deep expertise, higher velocity, easier hiring.
- **Rotation is mandatory.** If 80–90% of your project(s) uses one dominant stack and 10–20% another, everyone should be able to contribute to the *"ugly duck"*. If resources allow, rewrite it in the dominant stack.
- **Avoid split teams.** A 50/50 split between stacks usually results in two sub-teams.
- **New tech stacks require careful thought.** Introduce a new programming language only if there’s a strong, demonstrable need (performance, platform constraints, etc.). A veto until proven necessary is often wise.
- **Anarchy in programming languages is expensive.** If you allow it, congratulations - it’s your personal mess to manage.

### But what about innovation?

Tough question. You can’t veto every initiative.

Imagine someone introduces Rust to a Java/Scala/Go/Python team, promising to maintain it. Everything works… until they leave. Then what? Rewrite? Find a victim to maintain the new "super performant" service?

Actionable advice: maintain a **Tech Radar** and evaluate new languages carefully. CVs and hype shouldn’t dictate your tech stack - you’re building sustainable foundations, not pet projects.


### Final Thought

Anarchy in languages and frameworks is fun for a while. But when teams scale, it hits hard - maintenance slows, tech debt explodes, and rotations become nightmares.

Pick your battles, limit tech stacks, and rotate knowledge. The business will thank you later.
