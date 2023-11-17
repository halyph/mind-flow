# Play 3.0.0 Release and Scala
> | scala |

## Thoughts

Play Team released on 2023-11-06 [Play 2.9.0](https://github.com/playframework/playframework/releases/tag/2.9.0) and [Play 3.0.0](https://github.com/playframework/playframework/releases/tag/3.0.0).  This is very interesting event especially in relation to [Lightbend is Changing the License for Akka][lightbend].

I am more interested in Play 3.0.0 features:

> Since late 2021, the project has undergone several major changes.
>
> - The project is now entirely driven by the community, and fully committed to Open Source.
> - The project transitioned from Lightbend Inc. to a core team of dedicated individuals.
> - Play has decided to use [Apache Pekko](https://pekko.apache.org) under the hood, instead of Akka.
>
> Play 3.0 is nearly identical to Play 2.9, and continues to offer support for the latest Java LTS versions and Scala 3. Play 2.9 and 3.0 will offer the same features and receive parallel maintenance, benefiting from identical enhancements and bug fixes.

I guess this release might be interested to some people. But, there are several major issues for me:

1. Play framework was cool/interesting in 2017, but then I personally switched to [Akka-http](https://github.com/akka/akka-http) and it was must better for my needs. In my current company some projects have been using [http4s](https://http4s.org) or [ZIO](https://zio.dev). Playframework is 90% legacy, means new projects will **not** use it and rather pick up Spring Boot Java/Kotlin, [Ktor](https://ktor.io), than looking into Play.
2. Scala 2 to Scala 3 migration is happening slowly.
3. Scala 3 is a "new" language and it's not clear for the business why they need to migrate to it instead of e.g. Kotlin.
4. Even [Lightbend][lightbend] decided to leave this "ship". 
5. Play and Java is not even considered, there are much better frameworks for Java.

## Rant

I had to use Playframework in the past because of project's needs, but there are always some things I didn't like:

1. Dependency Injection (DI) via [Guice](https://github.com/google/guice). I prefer manual DI. And it doesn't look natural to use the Java DI library with Scala, it is alien.
2. Default Play application layout (see [sample](https://www.playframework.com/documentation/3.0.x/Anatomy)), that's why I had to switch to "traditional" project layout. I can't say it was difficult, but it was an additional step(s).
3. Bloated dependency (e.g. template lib) when I need to build REST API only.
4. CoffeeScript is added as default to Play.
5. [Template language](https://www.playframework.com/documentation/3.0.x/JavaTemplates) is Scala.

## What about `Play1`?

Some people might not know that [Play1](https://github.com/playframework/play1) and [Playframework](https://github.com/playframework/playframework) (aka Play2) are two different frameworks.

`Play1` is pure Java framework. It was/is very dynamic, fast development cycle, etc. [*Codeborne*](https://codeborne.com) decided to fork it (see [codeborne/replay](https://github.com/codeborne/replay)) and make it even "better". I checked and indeed, Codeborne's fork is in active [development](https://github.com/codeborne/replay/graphs/contributors).

[lightbend]: ../2022/2022-09-09-akka-license.md "Lightbend is Changing the License for Akka"
