---
tags:
  - make
---

# GNU Make

## Resources

- [GNU Make Manual](https://www.gnu.org/software/make/manual/)
- [Makefile Tutorial](https://makefiletutorial.com)

## Colored Help

![](make/make_color_help.png)

??? example "Sample `Makefile`"

    See origin [My Ultimate Makefile for Golang Projects](https://betterprogramming.pub/my-ultimate-makefile-for-golang-projects-fcc8ca20c9bb)

    ```make
    GREEN  := $(shell tput -Txterm setaf 2)
    YELLOW := $(shell tput -Txterm setaf 3)
    WHITE  := $(shell tput -Txterm setaf 7)
    CYAN   := $(shell tput -Txterm setaf 6)
    RESET  := $(shell tput -Txterm sgr0)

    all: help

    ## Build:
    build: ## Build your project and put the output binary in out/bin/
        @echo "build target"

    clean: ## Remove build related file
        @echo clean target

    vendor: ## Copy of all packages needed to support builds and tests in the vendor directory
        @echo vendor target

    watch: ## Run the code with cosmtrek/air to have automatic reload on changes
        @echo watch target
        
    ## Test:
    test: ## Run the tests of the project
        @echo test target

    coverage: ## Run the tests of the project and export the coverage
        @echo coverage target

    ## Docker:
    docker-build: ## Use the dockerfile to build the container
        @echo docker-build target

    docker-release: ## Release the container with tag latest and version
        @echo docker-release target

    ## Help:
    help: ## Show this help.
        @echo ''
        @echo 'Usage:'
        @echo '  ${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
        @echo ''
        @echo 'Targets:'
        @awk 'BEGIN {FS = ":.*?## "} { \
            if (/^[a-zA-Z_-]+:.*?##.*$$/) {printf "    ${YELLOW}%-20s${GREEN}%s${RESET}\n", $$1, $$2} \
            else if (/^## .*$$/) {printf "  ${CYAN}%s${RESET}\n", substr($$1,4)} \
            }' $(MAKEFILE_LIST)
    ```

## Functions

```make
VERSION  := snapshot
NAME     := myapp_name

# sample make function: $(call fn_build,1:arg,2:arg,3:arg)
define fn_build
@echo arg 1: $(1)
@echo arg 2: $(2)
@echo arg 3: $(3)
endef

.PHONY: build-service
build-service:
	$(call fn_build,$@,$(NAME),$(VERSION))
```

??? note "output"

    ```
    ➜ make build-service VERSION=1.0.3
    arg 1: build-service
    arg 2: myapp_name
    arg 3: 1.0.3
    ```

## Automatic Variables

**Variable**     | **Details** 
-----------------|---------------
`$@` |  is the file name of the **target** of the rule
`$<` | is the name of the **first prerequisite**
`$?` | is the **name of all the prerequisites** that are **newer than the target**, with spaces between them. If the target does not exist, all prerequisites will be included
`$^` | is the **name of all the prerequisites**, with spaces between them

??? example "Sample `Makefile`"

    ```make
    main: one two
        @echo '$$@:' $@
        @echo '$$<:' $<
        @echo '$$?:' $?
        @echo '$$^:' $^

        @touch main

    one:
        @touch one

    two:
        @touch two

    clean:
        @rm -f main one two
    ```
    
    **Output**
    
    ```shell
    ➜ make main
    $@: main
    $<: one
    $?: one two
    $^: one two
    
    # update file "one"
    ➜ touch one

    # output for '$?' has been changed
    ➜ make main
    $@: main
    $<: one
    $?: one
    $^: one two
    ```

## Loops and Lists

List variable in Makefile can be single-line or multi-line (*can contain comments*).

```make
LIST_MULTILINE += AAA  # Comment 1
LIST_MULTILINE += BBB  # Comment 2
LIST_MULTILINE += CCC  # Comment 3
LIST_MULTILINE += DDD  # Comment 4

# single-line
LIST = Xxx Yyy Zzz

.PHONY: print-list
print-list:
	@for i in $(LIST_MULTILINE); do \
		echo elem: $$i; \
	done
	@echo '-------------'
	@for i in $(LIST); do \
		echo elem: $$i; \
	done
```


??? note "output"

    ```shell
    ➜ make print-list
    elem: AAA
    elem: BBB
    elem: CCC
    elem: DDD
    -------------
    elem: Xxx
    elem: Yyy
    elem: Zzz
    ```
