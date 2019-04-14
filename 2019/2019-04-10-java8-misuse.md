# [WIP] Common misuses of new Java 8 features and other mistakes
> | java |

These notes are copy of [xpinjection/java8-misuses](https://github.com/xpinjection/java8-misuses) repository.

**Table of Contents**
- [Domain Model](#domain-model)
- [Optional](#optional)
- [Lambdas](#lambdas)
- [Stream API](#stream-api)
  - [Incorrect](#incorrect)
  - [Misuses](#misuses)
- [References](#references)

---

## Domain Model

All the cases are based on the next domain model:

```java
package com.xpinjection.java8.misused;

public class Annotations {
    public @interface Good{}
    public @interface Bad{}
    public @interface Ugly{}
}
```

```java
public enum Permission {ADD, EDIT, SEARCH, DELETE}
```

```java
public class Role {
    private String name;
    private Set<Permission> permissions = EnumSet.noneOf(Permission.class);

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public Set<Permission> getPermissions() { return permissions; }
    public void setPermissions(Set<Permission> permissions) { this.permissions = permissions; }

    @Override public boolean equals(Object o) { // ... the details are not important  }
    @Override public int hashCode() { return name.hashCode(); }
}
```

```java
public class User {
    private Long id;
    private String name;
    private int age;
    private Set<Role> roles = new HashSet<>();

    public User(long id, String name, int age) {
        this.id = id;
        this.name = name;
        this.age = age;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }

    public void setName(String name) { this.name = name; }
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }
    public Set<Role> getRoles() { return roles; }
    public void setRoles(Set<Role> roles) { this.roles = roles; }
}
```

```java
public class UserDto {
    private Long id;
    private String name;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

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