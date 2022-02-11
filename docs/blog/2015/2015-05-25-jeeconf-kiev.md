# JEEConf - Kyiv, 2015 - Report
> | conference | java |

It happened again - I attend [JEEConf](http://jeeconf.com), May 22-23, 2015. And as usual it was inspiring. Also, I can say that ["Scala"](http://www.scala-lang.org/) was the most dominated buzz word at this conference.

So, I attended the next talks:

- **Pragmatic Functional Refactoring with Java 8, by Richard Warburton** Java 8 functional features were introduced here. And were shown how we can refactor OOP program in functional way. I can say it's still a new way of thinking for Java developers.

- **Just what are you doing, HotSpot? by Gleb Smirnov** - Gleb gave us several advices for understanding tricky HotSpot behavior and why we should read HotSpot sources.

- **Lessons from Implementing a Modern B2C System in Scala, by Yuriy Guts** It was a case study talk about starting new project with Scala. The most interesting  was the issues appeared during project development, team's relationship with Scala, and Scala influences on non-Scala developers.

- **Spring Puzzlers, by Evgeny Borisov and Baruch Sadogursky** - We can say that this topic is unique. At least I'm not aware of similar talks on other Java conferences. Spring Puzzlers is a variation of classic Java puzzlers, but in Spring. It's really great collection of tricky Spring parts.

- **JVM Languages Q&A Panel with Jacek Laskowski, Baruch Sadogursky, Dmytro Mantula, Alexander Podkhalyuzin, Tomer Gabel** We can say that this panel was Groovy vs Scala. There are no other "languages" on this talk.

- **Building an Enterprise-less online bank, Anton Keks** - Anton doesn't love bloated Spring and likes simple and clean solution. He doesn't use Play Framework 2 on Scala because of slow compilation. Instead of this, he told us about his banking platform implemented on *Play 1.3* and *Java 8*, and all other items included in his stack.

- **Everything you wanted to know about writing async, high-concurrency HTTP applications in Java, but were afraid to ask, by Baruch Sadogursky** - Baruch shared his experience about implementing asynchronous file downloader in Java.

- **Scala Rock-Painting, by Dmytro Mantula** - This talk was like Scala puzzlers and/or Scala tricky parts. Speaker also gave us several suggesting how we can learn Scala more effectively via practicing *code katas* and/or [Anki](http://ankisrs.net) flesh cards. This talk highlighted the "dark" side of Scala. Really, recommend it.

- **Groovy under Macroscope, by Sergei Egorov and Baruch Sadogursky** - Sergei demoed us very hacky Groovy library [MacroGroovy](https://github.com/bsideup/MacroGroovy). It's nice to see true Groovy hacker and his creature.

- **About concurrency abstractions with Observable’s, Future’s, Akka (actors) in Scala, by Jacek Laskowski** - Jacek did Scala concurrency overview talk and highlighted other non-Akka libraries. It's nice to know that there are other *"good"* way to do concurrency without Akka.

- **Node.js and Evented I/O Alternatives on the JVM, by Niko Köbler** - I definitely heard about [Avatar.js](https://avatar-js.java.net), but Niko told us that [Avatar.js is dead](http://blog.n-k.de/2015/01/is-oracles-avatar-dead.html) and  [Oracle put development of Avatar on hold](http://blog.n-k.de/2015/02/current-status-of-oracles-project-avatar.html), i.e. full stop. As alternative were mentioned two solutions: **[DynJS](http://dynjs.org)** an ECMAScript runtime for the JVM and **[Nodyn](http://nodyn.io/)** - Node.js compatible framework on JVM. It's very interesting to see what will happen with them. *Nodyn* has strong RedHat support. Let's hope it's much stronger than Avatar.js had from  Oracle.

- **Do we need JMS in 21st century? by Mikalai Alimenkou** - The simple statements can be extracted from this talk: a) there are other non-JMS Message queues (MQs); b) we don't need bloated JMS for every tasks; c) use right MQ for right job

## Summary

- JEEConf has dedicated JVM track: 50% of this track was occupied by Scala (7 talks). As for me this is the sign ;-) Scala bandwagon reached Ukraine.

- *Microservices* everywhere. If you are not doing *microservices* - you should :-)

Yes, JEEConf is simply the best. [XP Injection](http://xpinjection.com/) did amazing work.

**Have fun, love Java!**

## References

* [JEEConf - Kiev, 2014 - Report](https://halyph.com/2014/05/jeeconf-kiev-2014-report.html)
* [JEEConf - Kiev, 2013 - Report](https://halyph.blogspot.com/2013/05/jeeconf-kiev-2013-report.html)
* [JEEConf - Kiev, 2012 - Report](https://halyph.blogspot.com/2012/05/this-year-we-had-second-jeeconf.html)
* [JEEConf - Kiev, 2011 - Report](https://halyph.blogspot.com/2011/05/jeeconf-kiev-2011-report.html)