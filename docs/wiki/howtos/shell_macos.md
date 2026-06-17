# Shell MacOS

## `lsof` - list open files

### Check Process on Port

```shell
sudo lsof -i :PORTNUMBER
```

??? example

    ```shell
    ➜ sudo lsof -i :5432

    COMMAND    PID    USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
    postgres 29756 oivasiv    7u  IPv6 0xa7285793950712d5      0t0  TCP localhost:postgresql (LISTEN)
    postgres 29756 oivasiv    8u  IPv4 0xa728579d2f85d74d      0t0  TCP localhost:postgresql (LISTEN)
    ```

### List Listening Ports

```shell
sudo lsof -iTCP -sTCP:LISTEN -P -n
```

- `-P`: Disables port name resolution, displaying only port numbers.
- `-n`: Disables hostname resolution, displaying only IP addresses.
