# The "Silent Watcher" Regression in MkDocs 1.6.1
<!-- tags: python, mkdocs -->

![thumbnail](2026-02-16-mkdocs-livereload-bug/pic0.jpeg)

**TL;DR**: MkDocs 1.6.1 does not watch for file changes when used with Click ≥ 8.3.0 due to a regression in Click’s boolean flag handling. The `livereload` flag defaults to `False` instead of `True`, silently disabling the file watcher.

**Environment**

| Component | Working ✅ | Broken ❌ |
|-----------|-----------|-----------|
| Python | 3.14.2 | - |
| MkDocs | 1.6.1 | 1.6.1 |
| Click | 8.2.1 | ≥ 8.3.0 |
| watchdog | 6.0.0 | - |
| OS | macOS (Apple Silicon) | - |

## Problem

The `mkdocs serve` command fails to detect file changes because the internal livereload server is never initialized, leaving the documentation in a static state.

**Expected** behavior after saving a file:

```
INFO    -  Detected file change: 'docs/...'
INFO    -  Building documentation...
INFO    -  Reloading browsers...
```

**Actual** behavior with Click ≥ 8.3.x:

Nothing happens. No watcher. No rebuild. No logs. The server behaves like a static file server.

## Why I excluded Watcher (aka `watchdog`)

Initially, `watchdog v6.0.0` was the primary suspect. The problem was **MkDocs was never telling it to start**.
With LLM help I proved that `watchdog` work properly on my machine.

## Click 8.3.x did the main harm

The issue is a "silent" breaking change in Click 8.3.0. MkDocs defines the `livereload` option with `default=True`. 
In Click 8.3.x, a regression in flag parsing causes these default values to be ignored or set to `False` unless explicitly provided in the command line.

### Evidence & Public Resources

**Source Code Proof**: In `mkdocs/commands/serve.py`, the file watcher (Watchdog) is only initialized if the `livereload` variable is truthy.

```python
# Reference: mkdocs/commands/serve.py
def serve(..., livereload=True, **kwargs):
    # The file watcher is behind a conditional gate
    if livereload:
        from mkdocs.livereload import LiveReloadServer
        # Logic to start Watchdog lives here
    else:
        # Falls back to a static server without a watcher
        server = _get_static_server(...)
```
```python
# Reference: mkdocs/livereload/__init__.py
def serve(self, ...):
    # This log only triggers if the LiveReloadServer was successfully started
    log.info(f"Watching paths for changes: {', '.join(repr(p) for p in self._paths)}")
    
    # This line starts the Watchdog observer
    if open_in_browser:
    log.info(f"Serving on {self.url} and opening it in a browser")
    else:
        log.info(f"Serving on {self.url}")
    self.serve_thread.start()
```

#### Upstream Confirmation

- **MkDocs Issue #4032**: [mkdocs does not watch for file changes when using click > 8.2.1](https://github.com/mkdocs/mkdocs/issues/4032). This is the definitive community thread confirming the regression.
- **Click Issue #3084 / #3111**: [New "default" behaviour in Click 8.3.x is broken](https://github.com/pallets/click/issues/3111). These upstream issues detail the "sentinel" value bug that broke negative and default boolean flags.
- **MkDocs-Material Issue #8478**: [mkdocs serve doesn't reload upon change anymore](https://github.com/squidfunk/mkdocs-material/issues/8478). Confirmation from the Material theme maintainer that this is an upstream dependency issue affecting all MkDocs users.

### How to Confirm the Bug with Click 8.3.x lib

By using a minimal reproduction script that mirrored MkDocs' CLI structure, we confirmed that Click 8.3.x fails to pass a `True` value for default flags. This bypassed all MkDocs logging as the application simply thought the user had intentionally disabled the watcher via `--no-livereload`.

```python
import click
import sys
from importlib.metadata import version

@click.command()
# This mimics the MkDocs 'serve' command definition
@click.option('--livereload', 'livereload', flag_value=True, default=True)
@click.option('--no-livereload', 'livereload', flag_value=False)
def serve(livereload):
    click.echo(f"Python Version: {sys.version.split()[0]}")
    click.echo(f"Click Version: {version('click')}")
    click.echo(f"Is livereload active? {livereload}")
    
    if livereload is True:
        click.secho("✅ SUCCESS: Watcher would start.", fg="green")
    else:
        click.secho("❌ BUG DETECTED: Watcher is disabled by default!", fg="red")

if __name__ == '__main__':
    serve()
```

1. Ensure Click 8.3.x is installed
```python
pip install "click>=8.3.0"
```

2. Run the script without arguments
```bash
python repro_click_bug.py
```
**Result**: You will see `❌ BUG DETECTED`. Even though the code says `default=True`, Click passes `False` to the function. This is why MkDocs never starts its watcher.

3. Run with the explicit flag:
```bash
python repro_click_bug.py --livereload
```

## Summary

1. The initial suspect is innocent.
2. Minor upstream releases can contain behavioral breaking changes.
3. Default values in CLI frameworks are API contracts.
4. Minimal reproductions beat speculation.
5. LLMs helped me to localize issue quickly. I love it.