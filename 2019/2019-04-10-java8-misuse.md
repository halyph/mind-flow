# Common misuses of new Java 8 features and other mistakes
> | java |

These notes are copy of [xpinjection/java8-misuses](https://github.com/xpinjection/java8-misuses) repository.

**Table of Contents**
- [Optional](#optional)
- [Lambdas](#lambdas)
- [Stream API](#stream-api)
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

Optional container should be short lived
Wrap nullable values in Optional to operate on them
Use chanined methods
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

Be concrete with functional interfaces
Avoid long or complex lambda expressions
Prefer reusable method reference
Use specific methods on collections

## Stream API

## References

- [xpinjection/java8-misuses](https://github.com/xpinjection/java8-misuses)
- [Video - JUGLviv meetup: Java 8 – The Good, the Bad and the Ugly](https://www.youtube.com/watch?v=_BDMPpGf1fA)
