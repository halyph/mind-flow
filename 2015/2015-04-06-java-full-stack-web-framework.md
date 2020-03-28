# Java full stack web framework
> | java |

I believe that everybody knows the most popular full-stack web framework - [Ruby on Rails](http://rubyonrails.org). Of course there are other frameworks for Ruby language, but Rails is the number one. Now, the question: how many full-stack web frameworks exist for Java?

**UPDATE (2016-11-20)**: [CUBA Platform is open sourced under Apache License 2.0](https://www.cuba-platform.com/blog-tags/open-source)

## Overview

Let's define the desired items for full-stack web framework:

- CoC - [Convention over configuration](http://en.wikipedia.org/wiki/Convention_over_configuration)
- MVC - [Model-view-controller](http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)
- DRY - [Don't repeat yourself](http://en.wikipedia.org/wiki/Don%27t_repeat_yourself)
- Scaffolding (_it was one of the major selling point on the early stage of Rails_)
  - Easy prototyping
- Data/Persistent Layer / ORM
- DB schema migration
- URI Routing
- HTML Rendering / Template engines
- Testing
- REST API
- Security
- Caching
- Request Filtering
- Session Management
- Form Validation
- i18n/l10n

## Grails

I think  [Grails](https://grails.org) was and is the single "true" Rails reincarnation on JVM. Grails is based on [Groovy](http://www.groovy-lang.org/) language. It support all concepts Rails supports. It's based on Spring/Hibernate and Gradle since v.3.0 (Grails v.3.0.0 was released on **Mar 31, 2015**).

Grails v.3 is build on [Spring Boot](http://projects.spring.io/spring-boot/).

Some people arguing that Grails v.3 acts as simple wrapper on top of Spring Boot and now it does not worth any investments. But, we must not agree as CoC and DRY principles are very vague.

## Play Framework 2

[Play Framework 2](https://www.playframework.com/) is a special player. It has two implementations: Java and Scala. Actually Java version is not as powerful as Scala due to Java, as a language, "limitation". This framework lives under [Typesafe](http://typesafe.com/) umbrella, aka **"Typesafe Reactive Platform"**.

Play is just different. It's not Servlet-based and is built on [Netty](http://netty.io/) async framework. A lot of people claiming that Play is very cool and productive. I haven't tried it yet. But it looks promising and interesting.

## Code Generation Frameworks

I decided to define the special category "Code Generation". Frameworks which are related  to this category are not full stack, but can be called as RAD (Rapid Application Development) frameworks.

### Spring Roo

[Spring Roo](http://projects.spring.io/spring-roo/) was very popular some time ago and had a lot of investments from VMWare (former Spring stack owner). Later, the ownership was transferred to [DISIG](http://www.disid.com).

Spring Roo is code generation framework, built on top of Spring stack. It's useful for quick prototyping.

### JBoss Forge

[JBoss Forge](http://forge.jboss.org/) is conceptually equal to Spring Roo, but linked to Java EE stack (like [Wildfly](http://wildfly.org/), [TomEE](http://tomee.apache.org/apache-tomee.html)) and Maven. It's relly cool if you work with Java EE a lot. Forge is shine in prototyping and code generation. Community looks vibrant and active.

### AppFuse

[AppFuse](http://appfuse.org/) can be called as ramp-up framework. The main goal is to quickly generate project with pre-onfigured functionality (see `mvn archetype:generate`).

### JHipster

[JHipster](https://jhipster.github.io/) is brand new and based on Spring Boot and Angular.js v.1.x. Classical code generation like in Forge or Spring Roo. But, code generation is build on top of node.js tool [Yeoman](http://yeoman.io/). Concept is very interesting, especially when it uses so hipster's technologies ;-).
It can generate both back-end (REST endpoint) and front-end (Angular.js Single-page application), even [Liquibase](http://www.liquibase.org/) migrations (which is cool too).

## Domain-driven Frameworks

There is a very special category Domain-driven frameworks. For this category I've selected two most popular frameworks: [OpenXava](http://www.openxava.org/) and [Apache Isis](http://isis.apache.org/). The main idea is that they can generate views and RESTs based on domain entities. Both frameworks have active community. They have "own" concepts and no hipsters technologies. The usage domain is very narrow, I guess they can be easily used to quickly general application's back-offices (aka admin pages) and prototyping.

## Others

There are several others frameworks [Ninja](http://www.ninjaframework.org/), [Javalight](http://javalite.io/), [Jodd](http://joddframework.org/), [Jobby](http://jooby.org/) and [airlift](https://github.com/airlift/airlift). They are build by small communities (or my single developer) and have some applications. But, it's risky to invest in them. You can look into because of curiosity, but not more. As for me it's much safe to use Play/Grails than some unpopular frameworks.

## Summary

So, Java ecosystem has two full stack frameworks which use Java language minimally: **Grails** (Groovy/Java) and **Play** (Scala/Java). Also, we have a bunch of code generation frameworks and domain-driven frameworks (which occupy really special niche).

## References

- Full stack
  - [Grails](https://grails.org/)
  - [Play Framework 2](https://www.playframework.com/)
  - [Cuba-platform](https://www.cuba-platform.com) - CUBA Platform (Apache License 2.0)
- Code Generation
  - [Spring Roo](http://projects.spring.io/spring-roo/)
  - [JBoss Forge](http://forge.jboss.org/)
  - [AppFuse](http://appfuse.org/)
  - [JHipster](https://jhipster.github.io/)
- DD Frameworks
  - [OpenXava](http://www.openxava.org/)
  - ~~[Cuba-platform](https://www.cuba-platform.com) - CUBA Platform is free for applications with up to 5 concurrent sessions.~~
  - [Apache Isis](http://isis.apache.org/)
- Others
  - [Ninja](http://www.ninjaframework.org/)  
  - [Javalight](http://javalite.io/)
  - [Jodd](http://jodd.org/) and [Jodd µicro frameworks](http://joddframework.org/)
  - [Jobby](http://jooby.org/)
  - [airlift](https://github.com/airlift/airlift)
  - [Web4j](http://www.web4j.com/)
  - [Rife](http://rifers.org/) - dead
