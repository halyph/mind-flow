# [WIP] Common misuses of new Java 8 features and other mistakes
> | java |

These notes are copy of [xpinjection/java8-misuses](https://github.com/xpinjection/java8-misuses) repository.

**Table of Contents**
- [Optional](#optional)
- [Lambdas](#lambdas)
- [Stream API](#stream-api)
  - [Incorrect](#incorrect)
  - [Misuses](#misuses)
- [References](#references)

---

## Optional

- StrictCheckOfValuePresence
  - https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/optional/StrictCheckOfValuePresence.java
- OptionalElvis
  - https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/optional/OptionalElvis.java
- HundredAndOneApproach
  - https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/optional/HundredAndOneApproach.java
- OptionalConstructorParameters
  - https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/optional/usage/OptionalConstructorParameters.java
- InternalOptionalUsage
  - https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/optional/usage/InternalOptionalUsage.java
- OptionalForCollections
  - https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/optional/usage/OptionalForCollections.java
- https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/optional/OptionalOverEngineering.java
- https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/optional/IfStatementIsNotAlwaysBadThing.java

// M. Alimenkov
Do not overuse Optional, never use it for parameters
Do not check for value presence, operate on it instead
Do not overuse Optional,don't be too clever

Optional container should be short lived
Wrap nullable values in Optional to operate on them
Use chained methods
Carefully choose what to wrap

## Lambdas

- AvoidLongLambdas
  - https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/lambda/AvoidLongLambdas.java
- AvoidComplexLambdas
  - https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/lambda/AvoidComplexLambdas.java
- ListSorting
  - https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/lambda/collections/ListSorting.java
- MapIterating
  - https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/lambda/collections/MapIterating.java
- https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/lambda/LazyCalculationsImprovePerformance.java
- https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/lambda/LambdasAreNotAlwaysTheBestOption.java
- https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/lambda/collections/EmulateMultimap.java
- https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/lambda/collections/RemoveElementWithIterator.java

Be concrete with functional interfaces
Avoid long or complex lambda expressions !
Prefer reusable method reference
Use specific methods on collections

Lazy calculation improve performance
Check popular API changes for lambda support

## Stream API

### Incorrect

- https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/stream/incorrect/UseStreamMoreThanOnce.java
- https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/stream/incorrect/ForgotTerminalOperation.java
- https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/stream/incorrect/InfiniteStreams.java

### Misuses

- https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/stream/SameOldCodeStyleWithNewConstructs.java
- https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/stream/NestedForEach.java
- https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/stream/MatchElementInFunctionalStyle.java
- https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/stream/ImperativeCodeMix.java
- https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/stream/collectors/ExternalCollectionForGrouping.java
- https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/stream/PreferSpecializedStreams.java
- https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/stream/DoNotNeglectDataStructures.java
- https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/stream/WantToUseStreamsEverywhere.java

- https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/stream/collectors/AvoidLoopsInStreams.java
- https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/stream/collectors/TrueFunctionalApproach.java
- https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/stream/collectors/StreamMayBeConvertedToArray.java
- https://github.com/xpinjection/java8-misuses/blob/master/src/com/xpinjection/java8/misused/stream/UntypedStreamsCouldBeConverted.java

Don't use external state with streams
Don't mix streams and imperative code 
Avoid complex nested streams
Avoid loop by design, think in pipeline
Follow true functional approach without side effects
Use typed streams for primitives
Take a look at extension like jool, StreamEx

## References

- [Repo - xpinjection/java8-misuses](https://github.com/xpinjection/java8-misuses)
- [Video - JUGLviv meetup: Java 8 – The Good, the Bad and the Ugly](https://www.youtube.com/watch?v=_BDMPpGf1fA)
- [Video - Java 8, the Good, the Bad and the Ugly [updated version] (Mikalai Alimenkou, XP Injection)](https://www.youtube.com/watch?v=td4vAzWPRpw)
- [Video - Common Mistakes Made in Functional Java](https://www.youtube.com/watch?v=VU7LyEOewvw)
- Libraries:
  - [jOOL](https://github.com/jOOQ/jOOL)
  - [StreamEx](https://github.com/amaembo/streamex)