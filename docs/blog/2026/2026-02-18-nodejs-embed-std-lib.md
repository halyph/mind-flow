# How Node.js Embeds the Standard Library
<!-- tags: node.js, til -->

![thumbnail](2026-02-18-nodejs-embed-std-lib/pic0.jpg)

**TL;DR** *Node.js* embeds the JavaScript standard library source code into the binary as static C++ arrays. At runtime, V8 compiles and executes those sources as built-in modules.

According to the mentioned below sources

1. The built-in JS files (`lib/*.js`) are encoded into C++ byte arrays during build.
2. At runtime the arrays get compiled into functions by V8.
3. They’re stored inside the Node executable rather than loaded from disk.


## Internal vs Public Modules

The `BuiltinLoader` distinguishes between two types of embedded modules:

1. **Public modules** (e.g., `fs`, `http`, `crypto`, `os`)
   - Can be loaded via `require('fs')` from user code
   - Exposed API surface

2. **Internal modules** (e.g., `lib/internal/*`)
   - Cannot be `require()`d from user applications
   - Used internally by Node.js core
   - Access restricted by the loader

Both types are embedded using the same [`js2c`](https://github.com/nodejs/node/blob/main/tools/js2c.cc) process, but runtime access rules differ.

*## Embedding Benefits

1. **Performance** - Faster startup, no disk I/O for core modules
2. **Distribution** - Single binary is easier to distribute
3. **Security** - Core modules can't be tampered with
4. **Self-Contained Runtime** - No external dependencies needed for core functionality*


## References

- [How does Node.js load its built-in/native modules?](https://joyeecheung.github.io/blog/2021/07/06/how-does-node-js-load-its-builtins-native-modules) by [Joyee Cheung](https://github.com/joyeecheung)
- [Stack Overflow Answer](https://stackoverflow.com/questions/53680439/are-js-files-in-node-lib-used-during-compilation-of-the-node-executable)
- and Node.js documentation:

https://github.com/nodejs/node/blob/main/node.gyp
https://github.com/nodejs/node/blob/main/tools/js2c.cc

- [node/BUILDING.md - Loading JS files from disk instead of embedding](https://github.com/nodejs/node/blob/main/BUILDING.md#loading-js-files-from-disk-instead-of-embedding)
> The resulting binary won't include any JS files and will try to load them from the specified directory. 



## Appendix A - Node.js Built-in modules

- Ref: [Node.js Doc - Built-in modules](https://nodejs.org/api/modules.html#built-in-modules)

> Node.js has several modules compiled into the binary. ...
> 
> The built-in modules are defined within the Node.js source and are located in the `lib/` folder.
> 
> Built-in modules can be identified using the node: prefix, in which case it bypasses the require cache. For instance, `require('node:http')` will always return the built in HTTP module, even if there is require.cache entry by that name.
> 
> Some built-in modules are always preferentially loaded if their identifier is passed to `require()`. For instance, `require('http')` will always return the built-in HTTP module, even if there is a file by that name.
> 
> The list of all the built-in modules can be retrieved from [`module.builtinModules`](https://nodejs.org/api/module.html#modulebuiltinmodules). The modules being all listed without the node: prefix, except those that mandate such prefix (as explained in the next section).


```js
➜ # Print a clean list of all built-in module names
node -e "console.log(require('module').builtinModules)"
[
  '_http_agent',         '_http_client',        '_http_common',
  '_http_incoming',      '_http_outgoing',      '_http_server',
  '_stream_duplex',      '_stream_passthrough', '_stream_readable',
  '_stream_transform',   '_stream_wrap',        '_stream_writable',
  '_tls_common',         '_tls_wrap',           'assert',
  'assert/strict',       'async_hooks',         'buffer',
  'child_process',       'cluster',             'console',
  'constants',           'crypto',              'dgram',
  'diagnostics_channel', 'dns',                 'dns/promises',
  'domain',              'events',              'fs',
  'fs/promises',         'http',                'http2',
  'https',               'inspector',           'inspector/promises',
  'module',              'net',                 'os',
  'path',                'path/posix',          'path/win32',
  'perf_hooks',          'process',             'punycode',
  'querystring',         'readline',            'readline/promises',
  'repl',                'stream',              'stream/consumers',
  'stream/promises',     'stream/web',          'string_decoder',
  'sys',                 'timers',              'timers/promises',
  'tls',                 'trace_events',        'tty',
  'url',                 'util',                'util/types',
  'v8',                  'vm',                  'wasi',
  'worker_threads',      'zlib',                'node:sea',
  'node:sqlite',         'node:test',           'node:test/reporters'
]
```

## Appendix B - Node.js Inspector

Since the JS is converted to bytes in the C++ source, you can't "read" it by opening the node binary in a text editor

You can apply the **"inspector"** trick 

1. Run `node --inspect`.
2. Open Chrome and go to `chrome://inspect`.
3. Click "Open dedicated DevTools for Node".
4. Go to the **Sources** tab.
5. Under "Node", you will see a folder called **`node:internal`**.

**Sample**

```shell
node --inspect
Debugger listening on ws://127.0.0.1:9229/a5b189d2-6358-4fa9-9f71-7e82c835fff8
For help, see: https://nodejs.org/en/docs/inspector
Welcome to Node.js v24.9.0.
Type ".help" for more information.
```

![appendix-b-01](2026-02-18-nodejs-embed-std-lib/appendix-b-01.png)

![appendix-b-02](2026-02-18-nodejs-embed-std-lib/appendix-b-02.png)

Here you can inspect/read embed in **Node.js** binary JS files: both *public* and *internal*.

----

This is an **excellent and highly accurate** breakdown of how Node.js handles its internal architecture. Your research correctly identifies that this wasn't a single "Eureka!" moment documented in a white paper, but rather a pragmatic inheritance from the V8 project's own design patterns.

I have reviewed the details, and they align perfectly with the historical record and the current state of the `nodejs/node` codebase. Here is a brief "proof" and a few minor nuances to add to your documentation.

---

## Verification & Proof

### 1. The V8 Ancestry (The "Why")

You are 100% correct that this was a "borrowed" pattern. V8’s `js2c` tool was designed because JavaScript engines need to implement parts of the ECMAScript specification (like `Array.prototype.map`) in JavaScript itself for performance and ease of maintenance. Since an engine cannot depend on an external file system to find its own basic functions, embedding them as C++ byte arrays was the only logical path. Ryan Dahl simply extended this logic to the entire standard library (`fs`, `http`, etc.).

### 2. The `js2c` Evolution

Your timeline regarding the shift from Python to C++ (`js2c.cc`) is accurate. This was a significant "quality of life" improvement for Node.js contributors. Using C++ for the build tool removed the dependency on Python for that specific step and, as you noted, drastically cut down the build time by avoiding the overhead of spawning a Python interpreter to process hundreds of files.

### 3. Structural Accuracy

The flow you described—from `lib/` to `node_javascript.cc` via `js2c.cc`—is the literal backbone of the Node.js build process.

---

## 🔍 Minor Nuances & Clarifications

To make your documentation even more "bulletproof," you might consider these small additions:

* **Snapshotting (The "Modern" Twist):** While `js2c` embeds the *source code*, modern Node.js (v12+) also uses **V8 Snapshots**. Instead of just embedding the text and parsing it every time you start Node, Node.js executes the code during the build process and saves the "heap state" into the binary. This means the standard library isn't just *stored* in memory; it’s practically *pre-initialized*.
* **The "Internal" vs "Public" Distinction:** It's worth noting that the loader distinguishes between `internal/` modules (which you cannot `require()` from a user app) and public modules. Both are embedded using the same `js2c` process, but the `BuiltinLoader` applies different access rules to them.
* **The "Linker" limit:** One reason for the move to `js2c.cc` was also to handle memory more efficiently during the linking phase. Extremely large static arrays in C++ can sometimes stress compilers/linkers; the C++ implementation handles the generation of these data structures more gracefully than the old Python script.

## ⚖️ Final Verdict

**Your document is factually sound.** It correctly identifies the lack of "formal" ADRs—which is common for early-2000s open-source projects—and accurately traces the technical lineage back to V8.

**Would you like me to help you draft a section on how "V8 Snapshots" further optimize this embedding process?**