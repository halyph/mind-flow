# Groovy or JRuby for Java developer
> | groovy | jruby | vs | comparison | java |

Today I've decided to share my own perception about the subject "Groovy vs JRuby" for Java developers.

When we are talking about any dynamic/scripting language like Ruby, Python, Groovy, etc. we are talking about quick development feedback (e.g. run - fix - run) no compilation, no packaging.

I must admit that mentioned above languages cover the same tasks' domain with own pros&cons. Now, we should differentiate *pragmatic* and *ecstatic* sides for each of them.

When we are talking about programming language we should clearly understand the difference between:

1. language (as syntax and semantic soup) - ecstatic side
2. language's ecosystem (community, tools, libraries, etc.) - pragmatic side

Let's discuss item (1). I think that learning a new programming language expand developer's mind. If we know many programming languages it helps us pick up any new language very quickly. I.e. to be pragmatic programmers we should learn many languages, dead simple.

In my opinion Ruby has much "nicer" syntax and language features in comparison to Groovy. Ruby meta model is very flexible that's why it has so many beatify frameworks and libraries (Rails, Cucumber, Rspec, etc.). But …

But Ruby ecosystem is totally different from Java/Groovy world. And it's really noticeable when we are trying to mix Ruby and Java in the same project.

Mixing JRuby and Java isn't a difficult task. But using Java API in Ruby code doesn't looks natural. And developing in mixed Java/Ruby environment isn't very comfortable:

* we have two package types: JARs and gems
* library versioning and dependency management is different
* Ruby/JRuby still has some cross-plafrom issues, especially on Windows (i.e. many Ruby gems do not support Windows and they must be fixed to support it, very annoying)
* it might be difficult to convince teammates to use Ruby on Java project

 I thought that Groovy isn't a (J)Ruby competitor until I've tried to automate some simple tasks in Groovy. I've got seamless integration with Java. It's really transparent and comfortable coding tool for Java developer. I have no mess with gems (Groovy uses JARs). And the Java ecosystem stays the same. Groovy has the similar dynamic power as Ruby. Yes, in some cases this "sugar" isn't so sweet as in Ruby. But, Groovy is really pragmatic choice for Java developer.

**Conclusion**: Ruby language is beautiful and sexy language, no doubts. But, we need a time to master Ruby ecosystem, deployment issues and tools philosophy. Also, JRuby/Java integration doesn't looks to me so pragmatic as Groovy/Java. It means investment in Ruby might be expensive.
 I will recommend to learn Ruby just to open another community for yourself (if you are Java developer), it should be as self-education task, no more. 

Links:

* [Transforming to Groovy](http://www.infoq.com/presentations/Transforming-to-Groovy)
* [Miro shared his thoughts about similar issue](http://thinkwrap.wordpress.com/2009/03/17/bye-bye-ruby-hello-groovy/)
