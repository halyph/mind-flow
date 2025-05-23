# Exploring Python’s Hidden CLI Modules
> | python | thoughts |

![alt text](2025-05-23-py-modules-cli/pic0.jpeg)

> **Note**: I am referring to the Python version 3.13.

## Intro

> TL;DR: Python’s standard library includes a surprising number of CLI tools—some helpful, some quirky. Here's a categorized list worth exploring.

If you’ve used Python for a while, you’ve probably come across modules that can be run directly from the command line. The most well-known is probably `venv`, but others like `http.server`, `uuid`, `json.tool`, and `unittest` have been lifesavers for me.

Python is famous for its *“batteries included”* philosophy. With a standard library this rich, I started wondering: how many modules actually offer a command-line interface? Turns out, quite a few - and you don’t need to scrape the CPython repo to find them. The official documentation [lists them neatly][pydoc-cmdline].

This post is just a *curiosity-driven* dive into those CLI-enabled modules, grouped into:

- General-Purpose Tools
- Python-Specific Tools
- Documentation & Introspection
- Educational / Easter Egg

Some are useful. Some are weird. All are built in.

## Modules

### General-Purpose Tools

*file, network, compression, system utilities*

| Module        | Sample CLI Usage                                                                       | Details                                                                                                        |
| ------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `base64`      | `echo "hello" \| base64`<br>`echo aGVsbG8K \| python3 -m base64 -d`                    | **Encode/decode Base64.** Useful for encoding binary data as ASCII text, e.g., for email or HTTP transmission. |
| `calendar`    | `python3 -m calendar 2025`                                                             | **Print yearly calendar.** Great for quick calendar checks in the terminal.                                    |
| `difflib`     | `python3 -m difflib file1.py file2.py`                                                 | **Show file differences.** Unified diff format helps visualize changes in code or text.                        |
| `filecmp`     | `python3 -m filecmp dir1 dir2`                                                         | **Compare files/directories.** Useful for checking duplicates or sync issues.                                  |
| `fileinput`   | `python3 -m fileinput file1.txt file2.txt`                                             | **Read from multiple files.** Treats multiple inputs as a single stream—ideal for batch processing.            |
| `ftplib`      | `python3 -m ftplib ftp.example.com`                                                    | **Interactive FTP session.** Helpful for manual file transfers or protocol debugging.                          |
| `gzip`        | `python3 -m gzip -d file.txt.gz`<br>`python3 -m gzip file.txt`                         | **Compress/decompress `.gz` files.** Lightweight alternative to external tools.                                |
| `http.server` | `python3 -m http.server 8000`                                                          | **Simple HTTP server.** Great for serving static files during local development.                               |
| `json.tool`   | `cat data.json \| python3 -m json.tool`                                                | **Pretty-print/validate JSON.** Helpful for debugging API responses and config files.                          |
| `mimetypes`   | `python3 -m mimetypes file.jpg`                                                        | **Guess file MIME type.** Useful in web or file server contexts.                                               |
| `platform`    | `python3 -m platform`                                                                  | **Show system/platform info.** Get OS, architecture, and Python version details.                               |
| `poplib`      | `python3 -m poplib`                                                                    | **Interact with POP3 email.** Mainly educational or for low-level debugging.                                   |
| `quopri`      | `echo "hello=0Aworld=" \| python3 -m quopri -d`                                        | **Encode/decode quoted-printable.** Commonly used in email transfer encoding.                                  |
| `random`      | `python3 -m random`                                                                    | **Generate random number.** Outputs a random float between 0 and 1.                                            |
| `sqlite3`     | `python3 -m sqlite3`<br>`sqlite> SELECT sqlite_version();`                             | **SQLite CLI shell.** Lightweight database querying without extra tools.                                       |
| `tarfile`     | `python3 -m tarfile -c archive.tar file1 file2`<br>`python3 -m tarfile -l archive.tar` | **Create/list `.tar` files.** Use Python to manage tar archives.                                               |
| `timeit`      | `python3 -m timeit "'-'.join(str(n) for n in range(100))"`                             | **Benchmark small code snippets.** Useful for quick performance checks.                                        |
| `uuid`        | `python3 -m uuid`                                                                      | **Generate UUID.** Create unique identifiers for systems or databases.                                         |
| `webbrowser`  | `python3 -m webbrowser https://example.com`                                            | **Open URLs in browser.** Automate browser launches from scripts.                                              |
| `zipfile`     | `python3 -m zipfile -c archive.zip file1 file2`<br>`python3 -m zipfile -l archive.zip` | **Create/list ZIP files.** Handle ZIP archives without needing external utilities.                             |

These built-in modules can be handy on systems where only Python is available.

### Python-Specific Tools

*development, testing, packaging, debugging*

| Module                   | Purpose                                          |
| ------------------------ | ------------------------------------------------ |
| `asyncio`                | Async event loop and coroutine support           |
| `code`                   | Launch interactive Python shell                  |
| `compileall`             | Compile all .py files to .pyc bytecode           |
| `cProfile` / `profile`   | Performance profiling of Python programs         |
| `dis`                    | Disassemble Python bytecode                      |
| `encodings.rot_13`       | ROT13 codec (Python-specific codec example)      |
| `ensurepip`              | Bootstrap pip installation                       |
| `idlelib`                | Launch the IDLE development environment          |
| `json.tool`              | Pretty-print and validate JSON                   |
| `pdb`                    | Python debugger                                  |
| `pickle` / `pickletools` | Serialize and inspect Python objects             |
| `py_compile`             | Compile Python source to bytecode                |
| `runpy`                  | Run Python modules as scripts                    |
| `site`                   | Site-specific configuration hook for Python      |
| `sysconfig`              | Access Python build configuration info           |
| `tabnanny`               | Detect indentation errors in Python source files |
| `tokenize`               | Convert Python source code into tokens           |
| `trace`                  | Trace program execution, function calls          |
| `unittest`               | Run unit tests                                   |
| `venv`                   | Create isolated Python environments              |
| `zipapp`                 | Package Python apps into executable ZIPs         |

### Documentation & Introspection Tools

*auto-generating or validating Python docs*

| Module     | Purpose                                              |
| ---------- | ---------------------------------------------------- |
| `pydoc`    | Generate/view Python docstrings in text/HTML         |
| `doctest`  | Test examples embedded in docstrings                 |
| `inspect`  | Introspect live objects for signatures, source, etc. |
| `pyclbr`   | Class browser support via introspection              |
| `ast`      | Parse and analyze abstract syntax trees              |
| `symtable` | Analyze symbol tables used by the compiler           |

### Educational / Easter Egg

| Module       | Purpose                          |
| ------------ | -------------------------------- |
| `antigravity` | **Open XKCD comic.** Launches a browser to the [classic XKCD comic #353](https://xkcd.com/353/) | 
| `this`       | The Zen of Python                |
| `turtledemo` | Demos for turtle graphics module |

## Thoughts

You might be wondering why all these CLI interfaces exist in the first place. Python’s core team values backward compatibility, and although some outdated modules are gradually being removed (see [PEP 594][PEP 594] and [PEP 632][PEP 632]), a lot of legacy code remains.

>Back in the early days of Python, the interpreter came with a large set of useful modules. This was often referred to as “batteries included” philosophy and was one of the cornerstones to Python’s success story. Users didn’t have to figure out how to download and install separate packages in order to write a simple web server or parse email.

Today, this legacy can feel bloated, but it’s also part of what made Python so approachable and powerful. The good news is, with ongoing cleanup efforts, the standard library is becoming more maintainable and less painful for core contributors.

In the meantime, these built-in CLI tools are still worth knowing about. Especially if you're working in a minimal environment where installing extra tools isn’t an option.

## References

- PEPs: 
  - [PEP 594 – Removing dead batteries from the standard library][PEP 594]
  - [PEP 632 – Deprecate distutils module][PEP 632]
- [Modules command-line interface (CLI)][pydoc-cmdline]

## Bonus: Packages I'd Remove Tomorrow

Here’s my personal hit list of packages I believe should be deprecated and removed as soon as possible from the standard library:


1. [**tkinter**](https://github.com/python/cpython/tree/3.13/Lib/tkinter) — GUI toolkit with a dated feel and platform inconsistencies.
2. [**turtledemo**](https://github.com/python/cpython/tree/3.13/Lib/turtledemo) — Educational, but better suited as a pip-installable package or separate teaching tool.
3. [**idlelib**](https://github.com/python/cpython/tree/3.13/Lib/idlelib) — Underused legacy IDE; doesn’t belong in the core distribution anymore.
4. [**xmlrpc**](https://github.com/python/cpython/tree/main/Lib/xmlrpc) — Outdated protocol, mostly replaced by REST or gRPC in modern projects.


[pydoc-cmdline]: https://docs.python.org/3.13/library/cmdline.html
[PEP 594]: https://peps.python.org/pep-0594/
[PEP 632]: https://peps.python.org/pep-0632/