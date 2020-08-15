# Overview: Optimistic vs. Pessimistic Locking
> | general |

Data Concurrency is a real problem in multi-user environment. How can we manage the data consistence when several users try to modify the same record(s) at the same time?  
This is a very interesting subject. Mostly, it's compromise. We can't easily pick one approach and forget about another.  
This subject was quite nice discussed in Martin's Fowler book: **"Patterns of Enterprise Application Architecture"**

And, you can find here the short Martin's overview: [Pessimistic Offline Lock](http://www.martinfowler.com/eaaCatalog/pessimisticOfflineLock.html) and [Optimistic Offline Lock](http://www.martinfowler.com/eaaCatalog/optimisticOfflineLock.html).  
  
[JBoss community documentation](http://docs.jboss.org/jbossas/docs/Server_Configuration_Guide/4/html/TransactionJTA_Overview-Pessimistic_and_optimistic_locking.html) has nice quotes about the subject:  

> The disadvantage of **pessimistic locking** is that a resource is locked from the time it is first accessed in a transaction until the transaction is finished, making it inaccessible to other transactions during that time. If most transactions simply look at the resource and never change it, an exclusive lock may be overkill as it may cause lock contention, and optimistic locking may be a better approach. With pessimistic locking, locks are applied in a fail-safe way. In the banking application example, an account is locked as soon as it is accessed in a transaction. Attempts to use the account in other transactions while it is locked will either result in the other process being delayed until the account lock is released, or that the process transaction will be rolled back. The lock exists until the transaction has either been committed or rolled back.

> With **optimistic locking**, a resource is not actually locked when it is first is accessed by a transaction. Instead, the state of the resource at the time when it would have been locked with the pessimistic locking approach is saved. Other transactions are able to concurrently access to the resource and the possibility of conflicting changes is possible. At commit time, when the resource is about to be updated in persistent storage, the state of the resource is read from storage again and compared to the state that was saved when the resource was first accessed in the transaction. If the two states differ, a conflicting update was made, and the transaction will be rolled back.

The most popular example of optimistic locking is SVN commit operation.