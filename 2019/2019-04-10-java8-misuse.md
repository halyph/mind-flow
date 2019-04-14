# [WIP] Common misuses of Java 8 features
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
  - [2.1 - Avoid Complex Lambdas](#21---avoid-complex-lambdas)
  - [2.2 - Avoid Long Lambdas](#22---avoid-long-lambdas)
  - [2.3 - Class Design (methods' naming)](#23---class-design-methods-naming)
  - [2.4 - Lambdas are not always the best option (method reference works as well)](#24---lambdas-are-not-always-the-best-option-method-reference-works-as-well)
  - [2.5 - Lazy calculations improve performance (*log* if `logger.isDebugEnabled()`)](#25---lazy-calculations-improve-performance-log-if-loggerisdebugenabled)
  - [2.6 - Emulate Multimap](#26---emulate-multimap)
  - [2.7 - Sorting the list using existing predefined comparator](#27---sorting-the-list-using-existing-predefined-comparator)
  - [2.8 - Iterating the map (`forEach` and map transform)](#28---iterating-the-map-foreach-and-map-transform)
  - [2.9 - Remove with predicate](#29---remove-with-predicate)
- [3- Stream API](#3--stream-api)
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

## 3- Stream API

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