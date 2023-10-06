---
tags:
  - sdkman
  - jvm
---

# sdkman

[**skdman**](https://sdkman.io) is a tool for managing parallel versions of multiple Software Development Kits on most Unix based systems. It provides a convenient Command Line Interface (CLI) and API for installing, switching, removing and listing Candidates.

I've been using it for managing:

- Java
- Maven
- Sbt

## List locally installed Java

```shell
sdk list java | grep -e installed -e local
```

??? example

    ```shell
    ➜ sdk list java | grep -e installed -e local
    Temurin       |     | 20           | tem     | installed  | 20-tem
                  | >>> | 17.0.7       | tem     | installed  | 17.0.7-tem
                  |     | 17.0.1       | tem     | local only | 17.0.1-tem
                  |     | 11.0.16.1    | tem     | local only | 11.0.16.1-tem
    Unclassified  |     | 8u121        | none    | local only | 8u121
    ```