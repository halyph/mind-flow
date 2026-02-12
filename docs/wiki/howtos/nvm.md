---
tags:
  - node.js
---

# nvm

## References

- Github [nvm-sh/nvm](https://github.com/nvm-sh/nvm)

## 1. List only **installed** versions

By default `nvm ls` list not-installed aliases. It is a noise.

```shell
➜ nvm ls
       v18.15.0
->      v24.9.0
default -> 24.9 (-> v24.9.0 *)
iojs -> N/A (default)
node -> stable (-> v24.9.0 *) (default)
stable -> 24.9 (-> v24.9.0 *) (default)
unstable -> N/A (default)
lts/* -> lts/krypton (-> N/A)
lts/argon -> v4.9.1 (-> N/A)
lts/boron -> v6.17.1 (-> N/A)
lts/carbon -> v8.17.0 (-> N/A)
lts/dubnium -> v10.24.1 (-> N/A)
lts/erbium -> v12.22.12 (-> N/A)
lts/fermium -> v14.21.3 (-> N/A)
lts/gallium -> v16.20.2 (-> N/A)
lts/hydrogen -> v18.20.8 (-> N/A)
lts/iron -> v20.20.0 (-> N/A)
lts/jod -> v22.22.0 (-> N/A)
lts/krypton -> v24.13.1 (-> N/A)
```

There are several options how to list only installed versions:

### Option 1: Filter out the N/A lines

```shell
➜ nvm ls | grep -v "N/A"
```

??? example "Sample"

    ```shell
    ➜ nvm ls | grep -v "N/A"
        v18.15.0 *
    ->      v24.9.0 *
    default -> 24.9 (-> v24.9.0 *)
    node -> stable (-> v24.9.0 *) (default)
    stable -> 24.9 (-> v24.9.0 *) (default)
    ```

### Option 2: Use `--no-alias` flag

```shell  
➜ nvm ls --no-alias
```

??? example "Sample"

    ```shell
    ➜ nvm ls --no-alias
        v18.15.0
    ->      v24.9.0
    ```