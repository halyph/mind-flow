# Podman

## Access MacOS host from a podman container

**Reference**:
- [Access MacOS host from a docker container](https://medium.com/@balint_sera/access-macos-host-from-a-docker-container-e0c2d0273d7f)
- [How Podman can extract a container's external IP address](https://www.redhat.com/sysadmin/container-ip-address-podman)
- https://github.com/containers/podman/issues/10878

Simply use `host.containers.internal` as a reference to external IP address.

Run the following snippets in separate terminals.

<table>
  <tr>
    <th>Terminal 1</th>
  	<th>Terminal 2</th>
  </tr>
  <tr>
<td>

```shell
➜ podman run -it --rm busybox:1.36.0
/ # nc host.containers.internal:23456
Hello from busybox
```
</td>
<td>

```shell
➜ nc -l 0.0.0.0 23456
Hello from busybox
```
</td>
  </tr>
</table>
