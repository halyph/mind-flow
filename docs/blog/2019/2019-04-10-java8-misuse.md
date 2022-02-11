# Common misuses of Java 8+ features
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
  - [1.6 - Optional "elvis"](#16---optional-elvis)
  - [1.7 - Optional Over Engineering (`if` not `null` might be *simpler*)](#17---optional-over-engineering-if-not-null-might-be-simpler)
  - [1.8 - Value presence strict check (chained `ifPresent`)](#18---value-presence-strict-check-chained-ifpresent)
- [2 - Lambdas](#2---lambdas)
  - [2.1 - Avoid Complex Lambdas](#21---avoid-complex-lambdas)
  - [2.2 - Avoid Long Lambdas](#22---avoid-long-lambdas)
  - [2.3 - Class Design (methods' naming)](#23---class-design-methods-naming)
  - [2.4 - Lambdas are not always the best option (method reference works as well)](#24---lambdas-are-not-always-the-best-option-method-reference-works-as-well)
  - [2.5 - Lazy calculations improve performance (*log* if `logger.isDebugEnabled()`)](#25---lazy-calculations-improve-performance-log-if-loggerisdebugenabled)
  - [2.6 - Emulate Multimap](#26---emulate-multimap)
  - [2.7 - Sorting the list using existing predefined comparator](#27---sorting-the-list-using-existing-predefined-comparator)
  - [2.8 - Iterating the map (`forEach` and map transform)](#28---iterating-the-map-foreach-and-map-transform)
  - [2.9 - Remove with predicate](#29---remove-with-predicate)
  - [2.10 - Avoid code-duplication with lambdas](#210---avoid-code-duplication-with-lambdas)
  - [2.11 - List of optionals](#211---list-of-optionals)
  - [2.12 - Checked Exceptions & Lambda](#212---checked-exceptions--lambda)
- [3 - Stream API](#3---stream-api)
  - [Incorrect usage](#incorrect-usage)
    - [3.1 - Forgotten termin operation](#31---forgotten-termin-operation)
    - [3.2 - Infinite stream](#32---infinite-stream)
    - [3.3 - Use stream more than once](#33---use-stream-more-than-once)
  - [Collectors](#collectors)
    - [3.4 - Avoid `forEach` and apply mapping to target type](#34---avoid-foreach-and-apply-mapping-to-target-type)
    - [3.5 - Collectors chain](#35---collectors-chain)
    - [3.6 - Do not use external collection for grouping](#36---do-not-use-external-collection-for-grouping)
    - [3.7 - Calculate statistics in single run with collector](#37---calculate-statistics-in-single-run-with-collector)
    - [3.8 - Convert stream to array](#38---convert-stream-to-array)
    - [3.9 - Use functional approach when "map-reduce"](#39---use-functional-approach-when-%22map-reduce%22)
  - [Misuses](#misuses)
    - [3.10 - Stream generation](#310---stream-generation)
    - [3.11 - Use data structure features](#311---use-data-structure-features)
    - [3.12 - Do not mix imperative code with streams](#312---do-not-mix-imperative-code-with-streams)
    - [3.13 - Match element in functional style](#313---match-element-in-functional-style)
    - [3.14 - Nested `forEach` is *anti-pattern*](#314---nested-foreach-is-anti-pattern)
    - [3.15 - Prefer specialized streams](#315---prefer-specialized-streams)
    - [3.16 - Poor Domain Model causes complex Data Access code](#316---poor-domain-model-causes-complex-data-access-code)
    - [3.17 - Do not use old-style code with new constructs](#317---do-not-use-old-style-code-with-new-constructs)
    - [3.18 - Know when to use `skip` and `limit`](#318---know-when-to-use-skip-and-limit)
    - [3.19 - Type of stream could be changed](#319---type-of-stream-could-be-changed)
    - [3.20 - Use stream to build map is over-complication](#320---use-stream-to-build-map-is-over-complication)
- [4 - Time API](#4---time-api)
  - [4.1 - Ignore Java 8 Time API](#41---ignore-java-8-time-api)
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

> - Be concrete with functional interfaces
> - Avoid long or complex lambda expressions!
> - Prefer reusable method reference
> - Use specific methods on collections
> - Lazy calculation improve performance
> - Check popular API changes for lambda support

### 2.1 - Avoid Complex Lambdas

```java
package com.xpinjection.java8.misused.lambda;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;
import com.xpinjection.java8.misused.Permission;
import com.xpinjection.java8.misused.Role;
import com.xpinjection.java8.misused.User;

import java.util.HashSet;
import java.util.Set;
import java.util.function.Predicate;

import static java.util.stream.Collectors.toSet;

public class AvoidComplexLambdas {
    private final Set<User> users = new HashSet<>();

    @Ugly
    class UsingComplexLambdaInPlace {
        public Set<User> findEditors() {
            return users.stream()
                    .filter(u -> u.getRoles().stream()
                            .anyMatch(r -> r.getPermissions().contains(Permission.EDIT)))
                    .collect(toSet());
        }
    }

    @Good
    class ComplexityExtractedToMethodReference {
        public Set<User> checkPermission(Permission permission) {
            return users.stream()
                    //.filter(this::hasEditPermission)
                    .filter(hasPermission(Permission.EDIT))
                    .collect(toSet());
        }

        private Predicate<User> hasPermission(Permission permission) {
            return user -> user.getRoles().stream()
                    .map(Role::getPermissions)
                    .anyMatch(permissions -> permissions.contains(permission));
        }

        private boolean hasEditPermission(User user) {
            return hasPermission(Permission.EDIT).test(user);
        }
    }
}
```

### 2.2 - Avoid Long Lambdas

```java
package com.xpinjection.java8.misused.lambda;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;
import com.xpinjection.java8.misused.User;
import com.xpinjection.java8.misused.UserDto;

import java.util.List;
import java.util.function.Function;

import static java.util.stream.Collectors.toList;

public class AvoidLongLambdas {
    @Ugly
    class LongLambdaInPlace {
        public List<UserDto> convertToDto(List<User> users){
            return users.stream()
                    .map(user -> {
                        UserDto dto = new UserDto();
                        dto.setId(user.getId());
                        dto.setName(user.getName());
                        //it happens to be much more fields 
                        //   and much more logic in terms of remapping these fields
                        return dto;
                    })
                    .collect(toList());
        }
    }

    @Good
    class MethodReferenceInsteadOfLambda {
        //particular toDto could be implemented as a separate class or as a lambda function
        private final Function<User, UserDto> toDto = this::convertToDto;

        public List<UserDto> convertToDto(List<User> users){
            return users.stream()
                    .map(toDto)
                    .collect(toList());
        }

        private UserDto convertToDto(User user){
            UserDto dto = new UserDto();
            dto.setId(user.getId());
            dto.setName(user.getName());
            return dto;
        }
    }
}
```

### 2.3 - Class Design (methods' naming)

```java
package com.xpinjection.java8.misused.lambda;

import com.xpinjection.java8.misused.Annotations.Bad;
import com.xpinjection.java8.misused.Annotations.Good;

import java.util.function.Function;
import java.util.function.UnaryOperator;

public class ClassDesign {
    @Bad
    static class AmbiguousOverloadedMethods {
        interface AmbiguousService<T> {
            <R> R process(Function<T, R> fn);

            T process(UnaryOperator<T> fn);
        }

        public void usage(AmbiguousService<String> service) {
            //which method you intended to call??? both are acceptable.
            service.process(String::toUpperCase);
        }
    }

    @Good
    static class SeparateSpecializedMethods {
        interface ClearService<T> {
            <R> R convert(Function<T, R> fn);

            T process(UnaryOperator<T> fn);
        }

        public void usage(ClearService<String> service) {
            //now it's clear which method will be called.
            service.convert(String::toUpperCase);
        }
    }
}
```

### 2.4 - Lambdas are not always the best option (method reference works as well)

```java
package com.xpinjection.java8.misused.lambda;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;

import java.util.Optional;

public class LambdasAreNotAlwaysTheBestOption {
    @Ugly
    class UnneededLambdasUsage {
        public void processAndPrint(String name) {
            Optional.ofNullable(name)
                    //.filter(s -> !s.isEmpty())
                    .map(s -> s.toUpperCase())
                    .map(s -> doProcess(s))
                    .ifPresent(s -> System.out.print(s));
        }

        private String doProcess(String name) {
            return "MR. " + name;
        }
    }

    @Good
    class MethodReferenceUsage {
        public void processAndPrint(String name) {
            Optional.ofNullable(name)
                    //.filter(StringUtils::isNotEmpty) // replace with appropriate library method ref
                    .map(String::toUpperCase)
                    .map(this::doProcess)
                    .ifPresent(System.out::print);
        }

        private String doProcess(String name) {
            return "MR. " + name;
        }
    }
}
```

### 2.5 - Lazy calculations improve performance (*log* if `logger.isDebugEnabled()`)

```java
package com.xpinjection.java8.misused.lambda;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;
import com.xpinjection.java8.misused.User;

import java.util.Set;
import java.util.function.Supplier;

public class LazyCalculationsImprovePerformance {
    @Ugly
    static class LoggingWithAdditionalCheckToAvoidCalculations {
        private static final Log LOG = null; // init logger with factory

        public void sendWelcomeEmailToUsers(Set<User> users) {
            // send email
            if (LOG.isDebugEnabled()) {
                LOG.debug("Emails have been sent for users: " + users);
            }
        }

        interface Log {
            void debug(String message);

            boolean isDebugEnabled();
        }
    }

    @Good
    static class PassLambdaToLazyCalculateValueForLogMessage {
        private static final Log LOG = null; // init logger with factory

        public void sendWelcomeEmailToUsers(Set<User> users) {
            // send email
            LOG.debug(() -> "Emails have been sent for users: " + users);
        }

        interface Log {
            void debug(String message);

            boolean isDebugEnabled();

            default void debug(Supplier<String> message) {
                if (isDebugEnabled()) {
                    debug(message.get());
                }
            }
        }
    }
}
```

### 2.6 - Emulate Multimap

```java
package com.xpinjection.java8.misused.lambda.collections;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;
import com.xpinjection.java8.misused.User;

import java.util.*;

public class EmulateMultimap {
    private final Map<String, Set<User>> usersByRole = new HashMap<>();

    @Ugly
    class ManuallyInsertSetOnFirstValueForTheKey {
        public void addUser(User user) {
            user.getRoles().forEach(r -> {
                Set<User> usersInRole = usersByRole.get(r.getName());
                if (usersInRole == null) {
                    usersInRole = new HashSet<>();
                    usersByRole.put(r.getName(), usersInRole);
                }
                usersInRole.add(user);
            });
        }

        public Set<User> getUsersInRole(String role) {
            Set<User> users = usersByRole.get(role);
            return users == null ? Collections.emptySet() : users;
        }
    }

    @Good
    class ComputeEmptySetIfKeyIsAbsent {
        public void addUser(User user) {
            user.getRoles().forEach(r -> usersByRole
                    .computeIfAbsent(r.getName(), k -> new HashSet<>())
                    .add(user));
        }

        public Set<User> getUsersInRole(String role) {
            return usersByRole.getOrDefault(role, Collections.emptySet());
        }
    }
}
```

### 2.7 - Sorting the list using existing predefined comparator

```java
package com.xpinjection.java8.misused.lambda.collections;

import com.xpinjection.java8.misused.User;
import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;

import java.util.List;

import static java.util.Comparator.comparing;

public class ListSorting {
    @Ugly
    class UsingCustomComparator {
        public void sortUsersById(List<User> users) {
            users.sort((x, y) -> Long.compare(x.getId(), y.getId()));
        }
    }

    @Good
    class UsingExistingPredefinedComparator {
        public void sortUsersById(List<User> users) {
            users.sort(comparing(User::getId));
        }
    }
}
```

### 2.8 - Iterating the map (`forEach` and map transform)

```java
package com.xpinjection.java8.misused.lambda.collections;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;
import com.xpinjection.java8.misused.User;

import java.util.HashMap;
import java.util.Map;

import static java.util.stream.Collectors.toMap;

public class MapIterating {
    @Ugly
    class UsingOldGoodEntrySet {
        public Map<String, String> getUserNames(Map<String, User> users) {
            Map<String, String> userNames = new HashMap<>();
            users.entrySet().forEach(user ->
                    userNames.put(user.getKey(), user.getValue().getName()));
            return userNames;
        }
    }

    @Good
    class UsingMapForEach {
        public Map<String, String> getUserNames(Map<String, User> users) {
            Map<String, String> userNames = new HashMap<>();
            users.forEach((key, value) -> userNames.put(key, value.getName()));
            return userNames;
        }
    }

    @Good
    class UsingMapTransform {
        public Map<String, String> getUserNames(Map<String, User> users) {
            return users.entrySet().stream()
                    .collect(toMap(Map.Entry::getKey,
                            entry -> entry.getValue().getName()));
        }
    }
}
```

### 2.9 - Remove with predicate

```java
package com.xpinjection.java8.misused.lambda.collections;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;
import com.xpinjection.java8.misused.Permission;
import com.xpinjection.java8.misused.User;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

public class RemoveElementWithIterator {
    private final Set<User> users = new HashSet<>();

    @Ugly
    class ManuallyRemoveElementWithIteratorRemove {
        public void removeUsersWithPermission(Permission permission) {
            Iterator<User> iterator = users.iterator();
            while (iterator.hasNext()) {
                User user = iterator.next();
                if (user.getRoles().stream()
                        .anyMatch(r -> r.getPermissions().contains(permission))) {
                    iterator.remove();
                }
            }
        }
    }

    @Good
    class RemoveWithPredicate {
        public void removeUsersWithPermission(Permission permission) {
            users.removeIf(user -> user.getRoles().stream()
                    .anyMatch(r -> r.getPermissions().contains(permission)));
        }
    }
}
```

### 2.10 - Avoid code-duplication with lambdas

```java

// @Ugly
private void logUpper(String str) {
    //super interesting code
    System.out.println(str.toUpperCase());
    //even more interesting code
}
private void logLower(String str) {
    //super interesting code
    System.out.println(str.toLowerCase());
    //even more interesting code
}

// @Good
private void logUpper(String string) {
    doSuperCoolStuff(string, s -> s.toUpperCase());
}
private void logLower(String string) {
    doSuperCoolStuff(string, s -> s.toLowerCase());
}
private void doFoo(String str, Function<String, String> func) {
    //super interesting code
    System.out.println(func.apply(str));
    //even more interesting code
}
```

### 2.11 - List of optionals

```java
beerLib.stream()
    .map(Beer::getDescription) //returns optional 

//java 8 style
beerLib.stream()
    .map(Beer::getDescription) //returns optional
    .filter(Optional::isPresent)
    .map(Optional::get)
    .forEach(System.out::println);

//java 8 flatMap
beerLib.stream()
    .map(Beer::getDescription) //returns optional
    .flatMap(o -> o.map(Stream::of).orElse(Stream.empty()))
    .forEach(System.out::println);

//java 9 flatMap
beerLib.stream()
    .map(Beer::getDescription) //returns optional
    .flatMap(Optional::stream)
    .forEach(System.out::println);
```

### 2.12 - Checked Exceptions & Lambda

```java
public Beer doSomething(Beer beer) throws IsEmptyException { ... }

Function <Beer,Beer> fBeer = beer -> doSomething(beer) // Don't do this
```

```java
// @Ugly
public Beer doSomething(Beer beer) throws IsEmptyException { ... }

beerLib.stream()
    .map(beer -> {
        try {
            return doSomething(beer);
        } catch (IsEmptyException e) {
            throw new RuntimeException(e);
        }
    };)
    .collect(Collectors.toList());

beerLib.stream()
    .map(this::wrappedDoSomeThing)
    .collect(Collectors.toList());
```

Exception Utility

```java
// @Better
@FunctionalInterface
public interface CheckedFunction<T, R> {
    public R apply(T t) throws Exception;
}

public static <T, R> Function<T, R> wrap(CheckedFunction<T, R> function) {
    return t -> {
        try {
            return function.apply(t);
        } catch (Exception ex) {
            throw new RuntimeException(ex);
        }
    };
};

beerLib.stream()
    .map(wrap(beer -> doSomething(beer)))
    .collect(Collectors.toList());
```

## 3 - Stream API

> - Don't use external state with streams
> - Don't mix streams and imperative code
> - Avoid complex nested streams
> - Avoid loop by design, think in pipeline
> - Follow true functional approach without side effects
> - Use typed streams for primitives
> - Take a look at extension like jool, StreamEx
> - Stream is not a data structure

### Incorrect usage

#### 3.1 - Forgotten termin operation

```java
package com.xpinjection.java8.misused.stream.incorrect;

import com.xpinjection.java8.misused.Annotations.Bad;
import java.util.stream.IntStream;

public class ForgotTerminalOperation {
    @Bad
    public void willDoNothingInReality() {
        IntStream.range(1, 5)
                .peek(System.out::println)
                .peek(i -> {
                    if (i == 5)
                        throw new RuntimeException("bang");
                });
    }
}
```

#### 3.2 - Infinite stream

```java
package com.xpinjection.java8.misused.stream.incorrect;

import com.xpinjection.java8.misused.Annotations.Bad;
import com.xpinjection.java8.misused.Annotations.Good;

import java.util.stream.IntStream;

public class InfiniteStreams {
    @Bad
    public void infinite(){
        IntStream.iterate(0, i -> i + 1)
                .forEach(System.out::println);
    }

    @Good
    public void validOne(){
        IntStream.iterate(0, i -> i + 1)
                .limit(10)
                .forEach(System.out::println);
    }

    @Bad
    public void stillInfinite(){
        IntStream.iterate(0, i -> ( i + 1 ) % 2)
                .distinct()
                .limit(10)
                .forEach(System.out::println);
    }

    @Good
    public void butThisOneIfFine(){
        IntStream.iterate(0, i -> ( i + 1 ) % 2)
                .limit(10)
                .distinct()
                .forEach(System.out::println);
    }
}
```

- Look closer at the order of operations
- Only use infinite streams when absolute necessary

**Solution**:

```java
IntStrean.range(0, 10);
IntStrean.rangeClosed(0, 10);
IntStrean.iterate(0, i -> i < 10, i -> i + 10); // Java 9 and up
```


#### 3.3 - Use stream more than once

```java
package com.xpinjection.java8.misused.stream.incorrect;

import com.xpinjection.java8.misused.Annotations.Bad;

import java.util.Arrays;
import java.util.stream.IntStream;

public class UseStreamMoreThanOnce {
    @Bad
    public void streamIsClosedAfterTerminalOperation() {
        int[] array = new int[]{1, 2};
        IntStream stream = Arrays.stream(array);
        stream.forEach(System.out::println);
        array[0] = 2;
        stream.forEach(System.out::println);
        //IllegalStateException: stream has already been operated upon or closed
    }
}
```

### Collectors

#### 3.4 - Avoid `forEach` and apply mapping to target type

```java
package com.xpinjection.java8.misused.stream.collectors;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;
import com.xpinjection.java8.misused.User;

import java.util.HashSet;
import java.util.Set;
import java.util.concurrent.atomic.AtomicInteger;

public class AvoidLoopsInStreams {
    private final Set<User> users = new HashSet<>();

    @Ugly
    class UseExternalCounter {
        public double countAverageRolesPerUser() {
            if (users.isEmpty()) {
                return 0;
            }
            AtomicInteger totalCount = new AtomicInteger();
            users.forEach(u -> totalCount.addAndGet(u.getRoles().size()));
            return totalCount.doubleValue() / users.size();
        }
    }

    @Good
    class ApplyMappingsToTargetType {
        public double countAverageRolesPerUser() {
            return users.stream()
                    .mapToDouble(u -> u.getRoles().size())
                    .average()
                    .orElse(0);
        }
    }
}
```

#### 3.5 - Collectors chain

```java
package com.xpinjection.java8.misused.stream.collectors;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;
import com.xpinjection.java8.misused.User;

import java.util.List;
import java.util.Map;

import static java.util.Comparator.comparing;
import static java.util.stream.Collectors.*;

public class CollectorsChain {
    @Ugly
    class GroupByAndTransformResultingMap {
        public Map<String, Integer> getMaxAgeByUserName(List<User> users) {
            return users.stream()
                    .collect(groupingBy(User::getName))
                    .entrySet().stream()
                    .collect(toMap(
                            Map.Entry::getKey,
                            e -> e.getValue().stream()
                                    .map(User::getAge)
                                    .reduce(0, Integer::max)
                    ));
        }
    }

    @Ugly
    class GroupByWithMaxCollectorUnwrappingOptionalWithFinisher {
        public Map<String, Integer> getMaxAgeByUserName(List<User> users) {
            return users.stream().collect(groupingBy(User::getName,
                    collectingAndThen(maxBy(comparing(User::getAge)),
                            user -> user.get().getAge())));
        }
    }

    @Good
    class CollectToMapWithMergeFunction {
        public Map<String, Integer> getMaxAgeByUserName(List<User> users) {
            return users.stream()
                    .collect(toMap(User::getName,
                            User::getAge,
                            Integer::max));
        }
    }

    @Good
    class ApplyReduceCollectorAsDownstream {
        public Map<String, Integer> getMaxAgeByUserName(List<User> users) {
            return users.stream()
                    .collect(groupingBy(User::getName,
                            mapping(User::getAge,
                            reducing(0, Integer::max))));
        }
    }
}
```

#### 3.6 - Do not use external collection for grouping

```java
package com.xpinjection.java8.misused.stream.collectors;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;
import com.xpinjection.java8.misused.Permission;
import com.xpinjection.java8.misused.User;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

import static java.util.stream.Collectors.*;

public class ExternalCollectionForGrouping {
    private final Set<User> users = new HashSet<>();

    @Ugly
    class ExternalStateIsUsedForStreamOperations {
        public Map<String, Set<User>> findEditors() {
            Map<String, Set<User>> editors = new HashMap<>();
            users.forEach(u -> u.getRoles().stream()
                    .filter(r -> r.getPermissions().contains(Permission.EDIT))
                    .forEach(r -> {
                        //is it better to use Multiset and avoid this complex code
                        Set<User> usersInRole = editors.get(r.getName());
                        if (usersInRole == null) {
                            usersInRole = new HashSet<>();
                            editors.put(r.getName(), usersInRole);
                        }
                        usersInRole.add(u);
                    })
            );
            return editors;
        }
    }

    @Good
    class TuplesAreUsedWhenStateIsNeededOnLaterPhase {
        public Map<String, Set<User>> findEditors() {
            return users.stream()
                    .flatMap(u -> u.getRoles().stream()
                        .filter(r -> r.getPermissions().contains(Permission.EDIT))
                        .map(r -> new Pair<>(r, u))
                    ).collect(groupingBy(p -> p.getKey().getName(),
                            mapping(Pair::getValue, toSet())));
        }
    }

    //any tuple implementation from 3rd party libraries
    class Pair<K, V> {
        private final K key;
        private final V value;

        Pair(K key, V value) {
            this.key = key;
            this.value = value;
        }

        K getKey() {
            return key;
        }

        V getValue() {
            return value;
        }
    }
}
```

#### 3.7 - Calculate statistics in single run with collector

```java
package com.xpinjection.java8.misused.stream.collectors;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;
import com.xpinjection.java8.misused.User;

import java.util.IntSummaryStatistics;
import java.util.List;
import java.util.stream.IntStream;

import static java.util.stream.Collectors.summarizingInt;

public class StatisticsCalculation {
    @Ugly
    class IterateThroughValuesSeveralTimes {
        public void printNameStats(List<User> users) {
            getNameLengthStream(users)
                    .max()
                    .ifPresent(max -> System.out.println("MAX: " + max));
            getNameLengthStream(users)
                    .min()
                    .ifPresent(min -> System.out.println("MIN: " + min));
        }

        private IntStream getNameLengthStream(List<User> users) {
            return users.stream()
                    .mapToInt(user -> user.getName().length());
        }
    }

    @Good
    class CalculateStatisticsInSingleRunWithCollector {
        public void registerUsers(List<User> users) {
            IntSummaryStatistics statistics = users.stream()
                    .collect(summarizingInt(user -> user.getName().length()));
            System.out.println("MAX: " + statistics.getMax());
            System.out.println("MIN: " + statistics.getMin());
        }
    }
}
```

#### 3.8 - Convert stream to array

```java
package com.xpinjection.java8.misused.stream.collectors;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;
import com.xpinjection.java8.misused.User;

import java.util.List;
import java.util.stream.Collectors;

public class StreamMayBeConvertedToArray {
    @Ugly
    class ConvertToArrayViaList {
        public String[] getUserNames(List<User> users) {
            List<String> names = users.stream()
                    .map(User::getName)
                    .collect(Collectors.toList());
            return names.toArray(new String[names.size()]);
        }
    }

    @Good
    class ConvertToArrayDirectly {
        public String[] getUserNames(List<User> users) {
            return users.stream()
                    .map(User::getName)
                    .toArray(String[]::new);
        }
    }
}
```

#### 3.9 - Use functional approach when "map-reduce"

```java
package com.xpinjection.java8.misused.stream.collectors;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;
import com.xpinjection.java8.misused.User;

import java.util.List;

import static java.util.Comparator.comparingInt;

public class TrueFunctionalApproach {
    @Ugly
    class BeforeJava8 {
        public User findUsersWithMostRoles(List<User> users) {
            if (users.isEmpty()) {
                return null;
            }
            User mostPowerful = users.iterator().next();
            for (User user : users) {
                if (user.getRoles().size() > mostPowerful.getRoles().size()) {
                    mostPowerful = user;
                }
            }
            return mostPowerful;
        }
    }

    @Ugly
    class NaiveStreamsApproach {
        public User findUsersWithMostRoles(List<User> users) {
            return users.stream()
                    .sorted(comparingInt(u -> u.getRoles().size()))
                    .findFirst()
                    .orElse(null);
        }
    }

    @Ugly
    class StreamsWithReduction {
        public User findUsersWithMostRoles(List<User> users) {
            return users.stream()
                    .reduce((u1, u2) ->
                            u1.getRoles().size() > u2.getRoles().size() ? u1 : u2)
                    .orElse(null);
        }
    }

    @Good
    class MaxWithComparator {
        public User findUsersWithMostRoles(List<User> users) {
            return users.stream()
                    .max(comparingInt(u -> u.getRoles().size()))
                    .orElse(null);
        }
    }
}
```

### Misuses

#### 3.10 - Stream generation

```java
package com.xpinjection.java8.misused.stream;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;
import com.xpinjection.java8.misused.Permission;
import com.xpinjection.java8.misused.Role;

import java.util.Arrays;
import java.util.Collections;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class CreationOptions {
    @Ugly
    public Stream<Permission> getStreamFromList() {
        return Arrays.asList(Permission.ADD, Permission.DELETE).stream();
    }

    @Good
    public Stream<Permission> getStreamFromElements() {
        return Stream.of(Permission.ADD, Permission.DELETE);
    }

    @Ugly
    public Stream<Role> generateStreamByMappingCopies(int n) {
        return Collections.nCopies(n, "ignored").stream()
                .map(s -> new Role());
    }

    @Ugly
    public Stream<Role> generateStreamFromRange(int n) {
        return IntStream.range(0, n).mapToObj(i -> new Role());
    }

    @Good
    public Stream<Role> generateStreamFromSupplierWithLimit(int n) {
        return Stream.generate(Role::new).limit(n);
    }

    @Ugly
    public Stream<Role> generateStreamFromArrayWithRange(Role[] roles, int max) {
        int to = Integer.min(roles.length, max);
        return IntStream.range(0, to).mapToObj(i -> roles[i]);
    }

    @Good
    public Stream<Role> generateStreamFromArrayWithLimit(Role[] roles, int max) {
        return Stream.of(roles).limit(max);
    }
}
```

#### 3.11 - Use data structure features

```java
package com.xpinjection.java8.misused.stream;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;

import java.util.*;

import static java.util.stream.Collectors.toList;

public class DoNotNeglectDataStructures {
    @Ugly
    class UnnecessaryUseOfNestedStreamOperations {
        public List<Order> filterOrdersByStatuses(List<Order> orders, Set<Status> appropriateStatuses) {
            return orders.stream()
                    .filter(order ->
                            appropriateStatuses.stream().anyMatch(order.getStatus()::equals))
                    .collect(toList());
        }
    }

    @Good
    class UseOfDataStructure {
        public List<Order> filterOrdersByStatuses(List<Order> orders, Set<Status> appropriateStatuses) {
            return orders.stream()
                    .filter(order -> appropriateStatuses.contains(order.getStatus()))
                    .collect(toList());
        }
    }

    @Ugly
    class StateIsStoredInBadDataStructure {
        private final List<Order> orders = new ArrayList<>();

        public void placeOrder(Order order) {
            orders.add(order);
        }

        public List<Order> getOrdersInStatus(Status status) {
            return orders.stream()
                    .filter(order -> order.getStatus() == status)
                    .collect(toList());
        }
    }

    @Good
    class InternalDataStructureMayBeOptimizedForAccessMethods {
        //Use multimap instead from external collections like Guava
        private final Map<Status, List<Order>> orders = new EnumMap<>(Status.class);

        public void placeOrder(Order order) {
            orders.computeIfAbsent(order.getStatus(), status -> new ArrayList<>()).add(order);
        }

        public List<Order> getOrdersInStatus(Status status) {
            return orders.get(status);
        }
    }

    class Order {
        private Status status = Status.ACTIVE;

        Status getStatus() {
            return status;
        }

        void setStatus(Status status) {
            this.status = status;
        }
    }

    enum Status {
        ACTIVE, SUSPENDED, CLOSED
    }
}
```

#### 3.12 - Do not mix imperative code with streams

```java
package com.xpinjection.java8.misused.stream;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;
import com.xpinjection.java8.misused.Permission;
import com.xpinjection.java8.misused.Role;
import com.xpinjection.java8.misused.User;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class ImperativeCodeMix {
    private static final String ADMIN_ROLE = "admin";

    private final List<User> users = new ArrayList<>();

    @Ugly
    class TooVerboseMixOfStreamOperationsAndImperativeCode {
        public boolean hasAdmin() {
            return users.stream()
                    .map(u -> {
                        if (u == null) {
                            throw new NullPointerException();
                        }
                        return u;
                    })
                    .flatMap(u -> u.getRoles().stream())
                    .map(Role::getName)
                    .anyMatch(name -> ADMIN_ROLE.equals(name));
        }
    }

    @Good
    class NiceAndCleanStreamOperationsChain {
        public boolean hasAdmin(Permission permission) {
            return users.stream()
                    .map(Objects::requireNonNull)
                    .flatMap(u -> u.getRoles().stream())
                    .map(Role::getName)
                    .anyMatch(ADMIN_ROLE::equals);
        }
    }
}
```

#### 3.13 - Match element in functional style

```java
package com.xpinjection.java8.misused.stream;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;
import com.xpinjection.java8.misused.Permission;
import com.xpinjection.java8.misused.User;

import java.util.HashSet;
import java.util.Set;
import java.util.concurrent.atomic.AtomicBoolean;

public class MatchElementInFunctionalStyle {
    private final Set<User> users = new HashSet<>();

    @Ugly
    class UseOldSchoolIterationsWithForEachAndExternalBoolean {
        public boolean checkPermission(Permission permission) {
            AtomicBoolean found = new AtomicBoolean();
            users.forEach(
                    u -> u.getRoles().forEach(
                            r -> {
                                if (r.getPermissions().contains(permission)) {
                                    found.set(true);
                                }
                            }
                    )
            );
            return found.get();
        }
    }

    @Ugly
    class TryToUseFunctionalStyleWithStreamFilter {
        public boolean checkPermission(Permission permission) {
            return users.stream().filter(
                    u -> u.getRoles().stream()
                            .filter(r -> r.getPermissions().contains(permission))
                            .count() > 0)
                    .findFirst().isPresent();
        }
    }

    @Ugly
    class TryToUseStreamMatching {
        public boolean checkPermission(Permission permission) {
            return users.stream()
                    .anyMatch(u -> u.getRoles().stream()
                            .anyMatch(r -> r.getPermissions().contains(permission)));
        }
    }

    @Good
    class UseFlatMapForSubCollections {
        public boolean checkPermission(Permission permission) {
            return users.stream()
                    .flatMap(u -> u.getRoles().stream())
                    .anyMatch(r -> r.getPermissions().contains(permission));
        }
    }

    @Good
    class UseFlatMapWithMethodReferencesForSubCollections {
        public boolean checkPermission(Permission permission) {
            return users.stream()
                    .map(User::getRoles)
                    .flatMap(Set::stream)
                    .anyMatch(r -> r.getPermissions().contains(permission));
        }
    }
}
```

#### 3.14 - Nested `forEach` is *anti-pattern*

```java
package com.xpinjection.java8.misused.stream;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import static java.util.stream.Collectors.toSet;

public class NestedForEach {
    @Ugly
    class NestedForEachWithExternalCollection {
        public Set<String> retrievePromoRuleNames(List<BusinessTransaction> transactions) {
            Set<String> ruleNamesWithPromo = new HashSet<>();
            transactions.forEach(transaction -> transaction.getRules().stream()
                    .filter(BusinessRule::isPromotion)
                    .forEach(rule -> ruleNamesWithPromo.add(rule.getRuleName())));
            return ruleNamesWithPromo;
        }
    }

    @Good
    class StreamOperationsChain {
        public Set<String> retrievePromoRuleNames(List<BusinessTransaction> transactions) {
            return transactions.stream()
                    .flatMap(t -> t.getRules().stream())
                    .filter(BusinessRule::isPromotion)
                    .map(BusinessRule::getRuleName)
                    .collect(toSet());
        }
    }

    class BusinessTransaction {
        List<BusinessRule> getRules() {
            return new ArrayList<>(); //stub
        }
    }

    class BusinessRule {
        String getRuleName() {
            return ""; //stub
        }

        boolean isPromotion() {
            return false; //stub
        }
    }
}
```

#### 3.15 - Prefer specialized streams

```java
package com.xpinjection.java8.misused.stream;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;
import com.xpinjection.java8.misused.User;

import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class PreferSpecializedStreams {
    private final Set<User> users = new HashSet<>();

    @Ugly
    class GeneralStreamUsage {
        public int getTotalAge() {
            return users.stream()
                    .map(User::getAge)
                    .reduce(0, Integer::sum);
        }
    }

    @Good
    class SpecializedStreamUsage {
        public int getTotalAge() {
            return users.stream()
                    .mapToInt(User::getAge)
                    .sum();
        }
    }

    @Ugly
    class FlatMapToCountElementsInAllCollections {
        public int countEmployees(Map<String, List<User>> departments) {
            return (int) departments.values().stream()
                    .flatMap(List::stream)
                    .count();
        }
    }

    @Good
    class MapToIntToSimplifyCalculation {
        public long countEmployees(Map<String, List<User>> departments) {
            return departments.values().stream()
                    .mapToInt(List::size)
                    .sum();
        }
    }
}
```

#### 3.16 - Poor Domain Model causes complex Data Access code

```java
package com.xpinjection.java8.misused.stream;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;
import com.xpinjection.java8.misused.Role;
import com.xpinjection.java8.misused.User;

import java.util.ArrayList;
import java.util.List;

public class RichDomainModel {
    @Ugly
    class PoorDomainModelCausesComplexDataAccessCode {
        private final List<User> users = new ArrayList<>();

        public User findUserInRole(String roleName) {
            for (User user : users) {
                for (Role role : user.getRoles()) {
                    if (roleName.equals(role.getName())) {
                        return user;
                    }
                }
            }
            return null;
        }
    }

    @Ugly
    class StreamVersionLooksNotMuchBetter {
        private final List<User> users = new ArrayList<>();

        public User findUserInRole(String roleName) {
            return users.stream().filter(user -> user.getRoles().stream()
                            .map(Role::getName)
                            .anyMatch(roleName::equals))
                    .findAny()
                    .orElse(null);
        }
    }

    @Good
    class RichDomainModelCouldSimplifyAccessCode {
        private final List<BetterUser> users = new ArrayList<>();

        public User findUserInRole(String roleName) {
            return users.stream()
                    .filter(user -> user.hasRole(roleName))
                    .findAny()
                    .orElse(null);
        }

        class BetterUser extends User {
            BetterUser(long id, String name, int age) {
                super(id, name, age);
            }

            boolean hasRole(String roleName) {
                return getRoles().stream()
                        .map(Role::getName)
                        .anyMatch(roleName::equals);
            }
        }
    }
}
```

#### 3.17 - Do not use old-style code with new constructs

```java
package com.xpinjection.java8.misused.stream;

import com.xpinjection.java8.misused.User;
import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;

import java.util.Collection;
import java.util.Objects;

import static java.util.Optional.ofNullable;

public class SameOldCodeStyleWithNewConstructs {
    @Ugly
    class NoMoreThanSameOldLoopWithIf {
        public void registerUsers(Collection<User> users) {
            users.stream().forEach(user ->
                    ofNullable(user).ifPresent(u -> {
                        //register user
                    })
            );
        }
    }

    @Good
    class NewStreamStyleWithMethodReference {
        public void registerUsers(Collection<User> users) {
            users.stream()
                    .filter(Objects::nonNull)
                    .forEach(this::registerUser);
        }

        private void registerUser(User user){
            //register user
        }
    }
}
```

#### 3.18 - Know when to use `skip` and `limit`

```java
package com.xpinjection.java8.misused.stream;

import com.xpinjection.java8.misused.User;

import java.util.List;

import static com.xpinjection.java8.misused.Annotations.Good;
import static com.xpinjection.java8.misused.Annotations.Ugly;

public class SkipAndLimitOnListIsWaste {
    @Ugly
    class SkipSomeElementsAndThenTakeSomeForProcessing {
        public void registerUsers(List<User> users) {
            users.stream().skip(5).limit(10)
                    .forEach(SkipAndLimitOnListIsWaste.this::registerUser);
        }
    }

    @Good
    class SublistDoNotWasteProcessingTime {
        public void registerUsers(List<User> users) {
            users.subList(5, 15)
                    .forEach(SkipAndLimitOnListIsWaste.this::registerUser);
        }
    }

    private void registerUser(User user) {
        //register user
    }
}
```

#### 3.19 - Type of stream could be changed

```java
package com.xpinjection.java8.misused.stream;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;

import java.util.List;

public class UntypedStreamsCouldBeConverted {
    @Ugly
    class ProcessOnlyValuesOfSpecialType {
        public int countDoubleNaNs(List numbers) {
            int count = 0;
            for (Object e : numbers) {
                if (e instanceof Double) {
                    Double d = (Double) e;
                    if (d.isNaN()) {
                        count++;
                    }
                }
            }
            return count;
        }
    }

    @Good
    class TypeOfStreamCouldBeChanged {
        public int countDoubleNaNs(List numbers) {
            return (int) numbers.stream()
                    .filter(Double.class::isInstance)
                    .mapToDouble(Double.class::cast)
                    .filter(Double::isNaN)
                    .count();
        }
    }
}
```

#### 3.20 - Use stream to build map is over-complication

```java
package com.xpinjection.java8.misused.stream;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;

import java.util.AbstractMap;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Stream;

import static java.util.stream.Collectors.collectingAndThen;
import static java.util.stream.Collectors.toMap;

public class WantToUseStreamsEverywhere {
    @Ugly
    class UseStreamToBuildMap {
        public Map<String, Object> getJpaProperties() {
            return Stream.of(
                    new AbstractMap.SimpleEntry<>("hibernate.show_sql", "true"),
                    new AbstractMap.SimpleEntry<>("hibernate.format_sql", "true")
            ).collect(collectingAndThen(
                    toMap(Map.Entry::getKey, Map.Entry::getValue),
                    Collections::unmodifiableMap)
            );
        }
    }

    @Good
    class UseOldPlainMap {
        public Map<String, Object> getJpaProperties() {
            Map<String, Object> properties = new HashMap<>();
            properties.put("hibernate.show_sql", "true");
            properties.put("hibernate.format_sql", "true");
            return Collections.unmodifiableMap(properties);
        }
    }
}
```

## 4 - Time API

### 4.1 - Ignore Java 8 Time API

```java
package com.xpinjection.java8.misused.time;

import com.xpinjection.java8.misused.Annotations.Good;
import com.xpinjection.java8.misused.Annotations.Ugly;

import java.time.LocalDate;
import java.util.Calendar;
import java.util.Date;

import static java.time.temporal.ChronoUnit.DAYS;

public class TimeApiIgnorance {
    @Ugly
    class AddDayInPreJava8Style {
        public Date tomorrow() {
            Calendar now = Calendar.getInstance();
            now.add(Calendar.DAY_OF_MONTH, 1);
            return now.getTime();
        }
    }

    @Ugly
    class AddDayInefficient {
        public LocalDate tomorrow() {
            return LocalDate.now().plus(1, DAYS);
        }
    }

    @Good
    class AddDayInJava8Style {
        public LocalDate tomorrow() {
            return LocalDate.now().plusDays(1);
        }
    }
}

```

## References

- [Repo - xpinjection/java8-misuses](https://github.com/xpinjection/java8-misuses)
- [Video - JUGLviv meetup: Java 8 – The Good, the Bad and the Ugly](https://www.youtube.com/watch?v=_BDMPpGf1fA)
- [Video - Java 8, the Good, the Bad and the Ugly [updated version] (*Mikalai Alimenkou, XP Injection)*](https://www.youtube.com/watch?v=td4vAzWPRpw)
- [Video - Common Mistakes Made in Functional Java by *Brian Vermeer*](https://www.youtube.com/watch?v=VU7LyEOewvw)
  - [Slides - Writing better functional java code devnexus by *Brian Vermeer*](https://www.slideshare.net/BrianVermeer/writing-better-functional-java-code-devnexus-137963441)
- Libraries:
  - [jOOL](https://github.com/jOOQ/jOOL)
  - [StreamEx](https://github.com/amaembo/streamex)
