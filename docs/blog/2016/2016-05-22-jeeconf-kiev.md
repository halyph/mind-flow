# JEEConf - Kyiv, 2016 - Report
> | conference | java |

This week (May 20–21, 2016) I attended [JEEConf](https://jeeconf.com) the 6th time. The conference was well organized, but there was one very important improvement — the organizer has changed the venue of the conference. Four of five stages were located on the same floor which was very convenient for attendees.

All buzzwords were on this conference: reactiveness, cloud, big data, nosql, scala/akka/spark.

This report is for myself just to keep track talks I’ve attended.

## Day 1 (May 20, 2016)

### **Search and analyze your data with ElasticSearch** by Anton Udovychenko ([slides](http://www.slideshare.net/AntonUdovychenko/search-and-analyze-your-data-with-elasticsearch-62204515))

>The importance of search for modern application is evident and nowadays it is higher than ever.
>A lot of projects use search forms as a primary interface for communication with a user. Though implementation of an intelligent search functionality is still a challenge and we need a good set of tools. In this presentation, I will talk through the high-level architecture and benefits of ElasticSearch with some examples. Aside from that, we will also take a look at its existing competitors, their similarities, and differences.

This talk was an Elasticsearch intro. I think it’s good overview and start point for further diving into the topic.

### **Lambda Architecture with Apache Spark** by [Taras Matyashovskyy](https://twitter.com/tmatyashovsky) ([slides](http://www.slideshare.net/tmatyashovsky/jeeconf-2016-lambda-architecture-with-apache-spark))

>A lot of players on the market have built successful MapReduce workflows to daily process terabytes of historical data. But who wants to wait for 24h to get updated analytics? This talk will introduce you to the lambda architecture designed to take advantages of both batch and streaming processing methods. So we will leverage fast access to historical data with real-time streaming data using Spark (Core, SQL, Streaming), Kafka, Apache Parquet, etc. Clear code plus intuitive demo are also included!

Taras has recommended to read [“Big Data. Principles and best practices of scalable realtime data systems”](https://www.manning.com/books/big-data) by Nathan Marz and James Warren. So, I’ve added this book in my reading backlog.

### **Caught in the Act: Kotlin Bytecode Generation and Runtime Performance** by [Dmitry Jemerov](https://twitter.com/intelliyole) ([slides](http://www.slideshare.net/intelliyole/kotlin-bytecode-generation-and-runtime-performance))

> In this talk, we’ll dive into the details of how various language features supported by Kotlin are translated to Java bytecode. We’ll use the JMH microbenchmarking tool to study the relative performance of various constructs and to understand how we can ensure top performance of the Kotlin code that we write.

This was an into [Kotlin’s](https://kotlinlang.org/) talk. There were plenty of code snippets Kotlin vs Java. Nice comparison.

IMHO, Kotlin is very similar in features to Groovy (with @TypeChecked or @CompileStatic). But, due to it’s (Kotlin) static nature, it looks more appealing for people. Kotlin looks very pragmatic (like Groovy).
It is interesting to see who will “survive” especially related to new [Gradle’s wave of adding Kotlin support](http://gradle.org/blog/kotlin-meets-gradle/).

### **Petabyte-Scale Text Processing with Spark** by Aleksey Slyusarenko ([Grammarly blog post](http://tech.grammarly.com/blog/posts/Petabyte-Scale-Text-Processing-with-Spark.html))

> At Grammarly, we have long used Amazon EMR with Hadoop and Pig in support of our big data processing needs. However, we were really excited about the improvements that the maturing Apache Spark offers over Hadoop and Pig, and so set about getting Spark to work with our petabyte text data set. This talk describes the challenges we had in the process and a scalable working setup of Spark that we have discovered as a result.

### **Lord of the Spark or an easy way for Java Developers to tame Big Data** by [Evgeny Borisov](https://twitter.com/jekaborisov) (no slides)

>Are you frightened of Big Data? Do you think it’s complicated, and in order to work in this field you need to learn a lot of new concepts, tools and paradigms?
>
>I have good news for you: Apache Spark, an open source Big Data processing framework, can spare you these concerns. You might heard that in order to use Spark you should know Scala or Python? Perhaps somebody had told you that Java API of Spark is limited, bulky and inconvenient? That all your previous Java experience is useless? Inversion of Control, design patterns, Java frameworks such as Spring, JUnit or Maven/Gradle are not your friends anymore?
>
>I have further good news for you: Writing Spark with Java can be very elegant and for sure more familiar to you. This talk is for Java developers who want to process Big Data in the most efficient and simple way, using the cutting edge technology — Spark. We will take a look on Spark API and cover its capabilities. Finally, I’ll demonstrate that in order to work with Spark you can still use the same techniques and knowledge you’ve gained in the world of Java.

## Lightning Talks

### **Code generation with Javac Plugin** by Oleksandr Radchykov

>Javac plugin API was introduced in java 8. We can use this API for getting cool things done (like code generation/code analyzing). However it is not widely used right now. Most of `java magic` projects like Lombok, Java-OO are using annotation processing. I want to show brand new approach for making the magic in java which has some benefits. Right now I have prototype which gives us the power of auto type casting in java and, if you want to use it, you shouldn’t add any dependencies to your project for using it, you should only add flag for compiler. In future I think it can be done through build tool plugin.

Unfortunately I missed the beginning of this talk. Looking forward for video record. The end of this talk was very interesting.

### **RxJava Applied: Concise Examples where It Shines** by Igor Lozynskyi ([slides](http://www.slideshare.net/neposuda/rxjava-applied), [github](https://github.com/aigor/rx-presentation))

>FRP & RxJava have already gained an important place in software development of all kinds, from mobile applications to high load servers. But it is just a beginning. The approach proposed by RxJava gives us such benefits as functional composition over observable streams, easy asynchronous programming, including error handling, an amazing toolbox of functions to build workflows.This talk is all about short but expressive examples where RxJava gives more possibilities requiring less code.

Intro into RxJava topic. Nice slides and sample. I hope people got the idea. Well done.

### **Different flavors of polymorphism in Scala** by h[Boris Trofimov](ttps://twitter.com/b0ris_1) ([slides](http://www.slideshare.net/b0ris_1/so-different-polymorphism-in-scala), [personal blog](http://www.btrofimoff.com/))

>Working with Scala can be compared to experiencing the “forth dimension”. Many of the features of Scala are unique and provide ways to look at application development in a new way. Polymorphism in Scala is multifaceted and this is going to be our topic.

Very interesting and clear sample of Scala’s polymorphism.

## Day 2 (May 21, 2016)

### **How to cook Apache Kafka with Camel and Spring Boot** by Ivan Vasyliev

>Will present basics of Apache Kafka for developers and show how to develop and test applications with use of Apache Camel and Spring Boot with Kafka in embedded mode.

### **WILD microSERVICES v2 (part 1)** by [Aleksandr Tarasov](https://twitter.com/aatarasoff) and [Kirill Tolkachev](https://twitter.com/tolkv) (github: [project](https://github.com/lavcraft/wild-microservices-in-kiev) and [lazybones templates](https://github.com/lavcraft/lazybones-templates))

>The following topics will be covered:
> - What are microservices? Where is the theory, bro?
> - What kind of technologies should we choose? What have we chosen and why?
> - Why RPC is still competetive in REST-domination era?
> - How to pack and distribute microservices? How can SpringBoot and Docker help us to solve our problems?
> - Why is service discovery considered as one of the crucial components? How to cook Spring Cloud and what problems > you may face in real life?
> - Security of microservices, API gateway and other.
> - Speakers will also cover other topics related to distributed system development.

This talk was divided in two sessions (I was on session #1 ONLY). Guys tried to show some live-coding.

I had a strong believe that live coding is very bad approach for a conference (git revision checkout works much better). I don’t want to spend my time watching while somebody typing and trying to resolve development issues.

So, why did I attended this talk? Because I know these speakers (from other conferences and podcast) and wanted to see them in action.

*About live coding*. I know only two speakers who are really good in this: [Venkat Subramaniam](https://twitter.com/venkat_s) and [Josh Long](https://twitter.com/starbuxman).

### **Introduction to Akka Streams** by [Dmytro Mantula](https://twitter.com/diez_dev)

>Streams of data and pipelines are everywhere. It’s a useful conceptual model: you have an input; you wire some little functions together to compose bigger and more complex pipelines; and you produce an output. To reach prominent throughput, we need to make these functions asynchronous, and parallelize them over input data.
>
>Akka Streams is a toolkit that provides a way to define and run a chain of asynchronous processing steps on a >sequence of elements, using tried-and-true actor model under the cover.
>
>In my talk I’m going to explain the motivation of using Akka Streams, and cover the following topics:
>
>- Problems of streaming data
>- Actor model in the nutshell
>- Problems of actor model from stream processing point of view
>- Problems of buffers and mailboxes overflow
>- What is back-pressure
>- How Akka Streams helps with resolving these problems
>- Code examples in Akka Streams

### **How to learn a programming language in 25 minutes** by [Dmytro Mantula](https://twitter.com/diez_dev) ([slides](http://www.slideshare.net/GlobalLogicUkraine/how-to-learn-a-programming-language-in-25-minutes))

> 3,5 years ago I was a “cool-Java-hacker”. Suddenly I decided to learn a course “FunProg in Scala”. It blew my mind! I felt I’m a Junior in Scala, but I had no willing to come back to Java… so I needed a job in Scala.
>
>But who needs a newbie without commercial experience but with Senior’s ambitions? Thus I started searching for lifehacks: how to mobilize my energy and learn the new programming paradigms in a short time. I found them. And eventually it developed into a system that I use to this day. My talk is about this system of continuous self-education.

### **Spring Boot under the Cover** by [Nicolas Fränkel](https://twitter.com/nicolas_frankel) ([slides](http://www.slideshare.net/nfrankel/javentura-spring-boot-under-the-hood))

>Spring Boot is a stack enabling you to kickstart your Spring application in a matter of minutes. It has been a resounding success among both developers already using Spring and microservices adopters. Favoring Spring Boot over the traditional Spring framework comes at a cost, though: you have to let Boot in control and some like to know everything what happens. Come to this talk to discover about auto-configuration and the different flavors of conditionals. After this talk, you’ll be able to understand Spring Boot internals and develop your own starter dependency.

### **The problem of real-time data binding** by Alexander Derkach ([slides](http://www.slideshare.net/AlexanderDerkach2/vertx-the-problem-of-realtime-data-binding-62182347))

>As the popularity of any event-driven application increases, the number of concurrent connections may increase. Applications that employ thread-per-client architecture, frustrate scalability by exhausting a server’s memory with excessive allocations and by exhausting a server’s CPU with excessive context-switching. One of obvious solutions, is exorcising blocking operations from such applications. Vert.x is event driven and non blocking toolkit, which may help you to achive this goal. In this talk, we are going to cover it’s core features and develop a primitive application using WebSockets, RxJava and Vert.x.
