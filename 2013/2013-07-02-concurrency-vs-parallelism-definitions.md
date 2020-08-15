# Concurrency vs. Parallelism Definitions
> | general |

Recently I had long discussion in scope of  "concurrency" and "parallelism" definitions. That's why I've decided to pick the most trusted sources for these definitions in one place:  
  
[**From Akka documentation:**](http://doc.akka.io/docs/akka/2.1.4/general/terminology.html)  

> _Concurrency_ and _parallelism_ are related concepts, but there are small differences. **_Concurrency_** means that two or more tasks are making progress even though they might not be executing simultaneously. This can for example be realized with time slicing where parts of tasks are executed sequentially and mixed with parts of other tasks. **_Parallelism_** on the other hand arise when the execution can be truly simultaneous.
  
[**From Oracle "Multithreaded Programming Guide":**](http://docs.oracle.com/cd/E19455-01/806-5257/6je9h032b/index.html)  

> _**Parallelism**_ - A condition that arises when at least two threads are executing simultaneously.  
> **_Concurrency_** - A condition that exists when at least two threads are making progress. A more generalized form of parallelism that can include time-slicing as a form of virtual parallelism.