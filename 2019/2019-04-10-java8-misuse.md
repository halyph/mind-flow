# [WIP] Common misuses of new Java 8 features and other mistakes
> | java |

These notes are copy of [xpinjection/java8-misuses](https://github.com/xpinjection/java8-misuses) repository.

**Table of Contents**
- [Domain Model](#domain-model)
- [1 - Optional](#1---optional)
  - [1.1 - Internal Optional Usage](#11---internal-optional-usage)
  - [1.2 - Optional Constructor Parameters](#12---optional-constructor-parameters)
  - [1.3 - Optional for resulted (method returns) Collections](#13---optional-for-resulted-method-returns-collections)
  - [1.4 - Use `flatMap` for getting nested Optional values](#14---use-flatmap-for-getting-nested-optional-values)
  - [1.5 - `if` statement with `Optional` is not always bad thing](#15---if-statement-with-optional-is-not-always-bad-thing)
  - [1.6 - Optional "elvis"](#16---optional-%22elvis%22)
  - [1.7 - Optional Over Engineering (`if` not `null` might be *simpler*)](#17---optional-over-engineering-if-not-null-might-be-simpler)
  - [1.8 - Value presence strict check (chained `ifPresent`)](#18---value-presence-strict-check-chained-ifpresent)
- [2 - Lambdas](#2---lambdas)
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

## 1 - Optional

> - Do not overuse Optional, never use it for parameters
> - Do not check for value presence, operate on it instead
> - Do not overuse Optional, don't be too clever
> - Optional container should be short lived
> - Wrap nullable values in Optional to operate on them
> - Use chained methods
> - Carefully choose what to wrap

### 1.1 - Internal Optional Usage

```java
package com.xpinjection.java8.misused.optional.usage;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;
import com.xpinjection.java8.misused.User;

import java.util.Optional;

public class InternalOptionalUsage {
    @Ugly
    class UnclearOptionalDependencyWithCheckForNull {
        private Printer printer;

        public void process(User user) {
            //some processing
            if (printer != null) {
                printer.print(user);
            }
        }

        public void setPrinter(Printer printer) {
            this.printer = printer;
        }
    }

    @Good
    class ValidInternalOptionalDependency {
        private Optional<Printer> printer = Optional.empty();

        public void process(User user) {
            //some processing
            printer.ifPresent(p -> p.print(user));
        }

        public void setPrinter(Printer printer) {
            this.printer = Optional.ofNullable(printer);
        }
    }

    interface Printer {
        void print(User user);
    }
}
```

### 1.2 - Optional Constructor Parameters

```java
package com.xpinjection.java8.misused.optional.usage;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;

import java.io.Serializable;
import java.util.Arrays;
import java.util.List;
import java.util.Optional;

public class OptionalConstructorParameters {
    @Ugly
    class OptionalLeaksOutsideClass {
        public List<Email> create() {
            Email noAttachment = new Email("First!", "No attachment", Optional.empty());
            Attachment attachment = new Attachment("/mnt/files/image.png", 370);
            Email withAttachment = new Email("Second!", "With attachment", Optional.of(attachment));
            return Arrays.asList(noAttachment, withAttachment);
        }

        class Email implements Serializable {
            private final String subject;
            private final String body;
            private final Optional<Attachment> attachment;

            Email(String subject, String body, Optional<Attachment> attachment) {
                this.subject = subject;
                this.body = body;
                this.attachment = attachment;
            }

            String getSubject() { return subject; }
            String getBody() { return body; }
            Optional<Attachment> getAttachment() { return attachment;}
        }
    }

    @Good
    class OverloadedConstructors {
        public List<Email> create() {
            Email noAttachment = new Email("First!", "No attachment");
            Attachment attachment = new Attachment("/mnt/files/image.png", 370);
            Email withAttachment = new Email("Second!", "With attachment", attachment);
            return Arrays.asList(noAttachment, withAttachment);
        }

        class Email implements Serializable {
            private final String subject;
            private final String body;
            private final Attachment attachment;

            Email(String subject, String body, Attachment attachment) {
                this.subject = subject;
                this.body = body;
                this.attachment = attachment;
            }

            Email(String subject, String body) {
                this(subject, body, null);
            }

            String getSubject() { return subject; }
            String getBody() { return body; }
            boolean hasAttachment() { return attachment != null; }
            Attachment getAttachment() { return attachment; }
        }
    }

    class Attachment {
        private final String path;
        private final int size;

        Attachment(String path, int size) {
            this.path = path;
            this.size = size;
        }

        String getPath() { return path; }
        int getSize() { return size; }
    }
}
```

### 1.3 - Optional for resulted (method returns) Collections

```java
package com.xpinjection.java8.misused.optional.usage;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;
import com.xpinjection.java8.misused.User;

import java.util.Collections;
import java.util.List;
import java.util.Optional;

public class OptionalForCollections {
    private static final String ADMIN_ROLE = "admin";

    @Ugly
    class TooVerbose {
        public User findAnyAdmin() {
            Optional<List<User>> users = findUsersByRole(ADMIN_ROLE);
            if (users.isPresent() && !users.get().isEmpty()) {
                return users.get().get(0);
            }
            throw new IllegalStateException("No admins found");
        }

        private Optional<List<User>> findUsersByRole(String role) {
            //real search in DB
            return Optional.empty();
        }
    }

    @Good
    class NiceAndClean {
        public User findAnyAdmin() {
            return findUsersByRole(ADMIN_ROLE).stream()
                    .findAny()
                    .orElseThrow(() -> new IllegalStateException("No admins found"));
        }

        private List<User> findUsersByRole(String role) {
            //real search in DB
            return Collections.emptyList();
        }
    }
}
```

### 1.4 - Use `flatMap` for getting nested Optional values

```java
package com.xpinjection.java8.misused.optional;

import com.xpinjection.java8.misused.Annotations.Bad;
import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;

import java.util.Optional;

import static java.util.Optional.empty;
import static java.util.Optional.ofNullable;

public class HundredAndOneApproach {
    @Ugly
    class SameOldImperativeStyle {
        public String getPersonCarInsuranceName(Person person) {
            String name = "Unknown";
            if (ofNullable(person).isPresent()) {
                if (person.getCar().isPresent()) {
                    if (person.getCar().get().getInsurance().isPresent()) {
                        name = person.getCar().get().getInsurance().get().getName();
                    }
                }
            }
            return name;
        }
    }

    @Ugly
    class UsingIfPresentInSameImperativeWayWithDirtyHack {
        public String getPersonCarInsuranceName(Person person) {
            final StringBuilder builder = new StringBuilder();
            ofNullable(person).ifPresent(
                    p -> p.getCar().ifPresent(
                            c -> c.getInsurance().ifPresent(
                                    i -> builder.append(i.getName())
                            )
                    )
            );
            return builder.toString();
        }
    }

    @Bad
    class UsingMapWithUncheckedGet {
        public String getPersonCarInsuranceName(Person person) {
            return ofNullable(person)
                    .map(Person::getCar)
                    .map(car -> car.get().getInsurance())
                    .map(insurance -> insurance.get().getName())
                    .orElse("Unknown");
        }
    }

    @Ugly
    class UsingMapWithOrElseEmptyObjectToFixUncheckedGet {
        public String getPersonCarInsuranceName(Person person) {
            return ofNullable(person)
                    .map(Person::getCar)
                    .map(car -> car.orElseGet(Car::new).getInsurance())
                    .map(insurance -> insurance.orElseGet(Insurance::new).getName())
                    .orElse("Unknown");
        }
    }

    @Good
    class UsingFlatMap {
        public String getCarInsuranceNameFromPersonUsingFlatMap(Person person) {
            return ofNullable(person)
                    .flatMap(Person::getCar)
                    .flatMap(Car::getInsurance)
                    .map(Insurance::getName)
                    .orElse("Unknown");
        }
    }

    class Person {
        Optional<Car> getCar() {
            return empty(); //stub
        }
    }

    class Car {
        Optional<Insurance> getInsurance() {
            return empty(); //stub
        }
    }

    class Insurance {
        String getName() {
            return ""; //stub
        }
    }
}
```

### 1.5 - `if` statement with `Optional` is not always bad thing

```java
package com.xpinjection.java8.misused.optional;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;

import java.util.Optional;
import java.util.stream.Stream;

public class IfStatementIsNotAlwaysBadThing {
    @Ugly
    class CombineSomeOptionalsInCleverWay {
        public Optional<Integer> sum(Optional<Integer> first, Optional<Integer> second) {
            return Stream.of(first, second)
                    .filter(Optional::isPresent)
                    .map(Optional::get)
                    .reduce(Integer::sum);
        }
    }

    @Ugly
    class PlayMapGameInEvenMoreCleverWay {
        public Optional<Integer> sum(Optional<Integer> first, Optional<Integer> second) {
            return first.map(b -> second.map(a -> b + a).orElse(b))
                    .map(Optional::of)
                    .orElse(second);
        }
    }

    @Good
    class OldSchoolButTotallyClearCode {
        public Optional<Integer> sum(Optional<Integer> first, Optional<Integer> second) {
            if (!first.isPresent() && !second.isPresent()) {
                return Optional.empty();
            }
            return Optional.of(first.orElse(0) + second.orElse(0));
        }
    }
}
```

### 1.6 - Optional "elvis"

```java
package com.xpinjection.java8.misused.optional;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;
import com.xpinjection.java8.misused.User;

import static java.util.Optional.ofNullable;

public class OptionalElvis {
    @Ugly
    class BeforeJava8 {
        public String getUserName(User user) {
            return (user != null && user.getName() != null) ? user.getName() : "default";
        }
    }

    @Ugly
    class UsingOptionalIsPresent {
        public String getUserName(User user) {
            if (ofNullable(user).isPresent()) {
                if (ofNullable(user.getName()).isPresent()) {
                    return user.getName();
                }
            }
            return "default";
        }
    }

    @Good
    class UsingOrElse {
        String getUserName(User user) {
            return ofNullable(user)
                    .map(User::getName)
                    .orElse("default");
        }
    }
}
```

### 1.7 - Optional Over Engineering (`if` not `null` might be *simpler*)

```java
package com.xpinjection.java8.misused.optional;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;
import com.xpinjection.java8.misused.Role;

import java.util.Optional;

public class OptionalOverEngineering {
    @Ugly
    class NullProtectionOverEngineering {
        public Role copyRole(Role role) {
            Role copy = new Role();

            Optional.ofNullable(role.getName())
                    .ifPresent(copy::setName);
            copy.setPermissions(role.getPermissions());
            return copy;
        }
    }

    @Good
    class SimpleConditionalCopying {
        public Role copyRole(Role role) {
            Role copy = new Role();

            if (role.getName() != null) {
                copy.setName(role.getName());
            }
            copy.setPermissions(role.getPermissions());
            return copy;
        }
    }
}
```

### 1.8 - Value presence strict check (chained `ifPresent`)

```java
package com.xpinjection.java8.misused.optional;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;
import com.xpinjection.java8.misused.User;

import java.util.Optional;

public class StrictCheckOfValuePresence {
    @Ugly
    class ManualCheckForPresenceToThrowException {
        public String getUserName(Long userId) {
            Optional<User> user = findById(userId);
            if (user.isPresent()) {
                return user.get().getName();
            }
            throw new IllegalStateException("User not found");
        }

        public void deleteUser(Long userId) {
            Optional<User> user = findById(userId);
            if (user.isPresent()) {
                delete(user.get());
            }
        }

        private void delete(User user) {
            //delete from DB
        }
    }

    @Good
    class OrElseThrowUsage {
        public String getUserName(Long userId) {
            return findById(userId)
                    .orElseThrow(() -> new IllegalStateException("User not found"))
                    .getName();
        }

        public void deleteUser(Long userId) {
            findById(userId).ifPresent(this::delete);
        }

        private void delete(User user) {
            //delete from DB
        }
    }

    private Optional<User> findById(Long userId) {
        //search in DB
        return Optional.of(new User(5L, "Mikalai", 33));
    }
}
```

## 2 - Lambdas

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