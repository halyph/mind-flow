# How Node.js Embeds the Standard Library

The JavaScript files from the Node.js standard library (https://github.com/nodejs/node/tree/main/lib/) are **embedded directly into the Node.js binary** during compilation, not distributed as separate `.js` files.

## History: When and Why

### Key Dates

- **2008**: Google releases Chrome and open-sources V8 JavaScript engine
- **Early 2009**: Ryan Dahl begins experimenting with server-side JavaScript using V8
- **May 27, 2009**: First version of Node.js released
- **June 22, 2009**: js2c.py committed to Node.js repository (commit 115c494e8fef48f13ee8c0a8ac16d6c0c7e5dce8)
- **November 8, 2009**: Ryan Dahl introduces Node.js at JSConf EU in Berlin (see [video](https://www.youtube.com/watch?v=EeYvFl7li9E))

### Why Ryan Dahl Chose to Embed V8

#### 1. Performance and the "JIT Revolution" (2008)

In 2008, Google released V8 with Chrome, revolutionizing JavaScript performance:
- **Just-In-Time (JIT) compilation**: V8 compiled JavaScript directly to native machine code, unlike previous engines that interpreted code
- Made JavaScript **fast enough** for server-side tasks like network I/O and file operations
- V8's performance characteristics enabled the "purely evented I/O" model that Dahl envisioned

#### 2. Designed for Embedding

V8 was explicitly designed as a standalone library for embedding in C++ applications:
- Clean C++ API for binding low-level Unix C libraries to JavaScript functions
- Could expose filesystem, networking, and process APIs to JavaScript
- Allowed building custom runtimes beyond web browsers

#### 3. JavaScript's "Clean Slate" for Server-Side I/O

Dahl had previously experimented with C and Ruby for non-blocking I/O but found limitations. JavaScript was uniquely positioned:
- **Already single-threaded** - no legacy multi-threading expectations
- **Event loop architecture** - designed for asynchronous operations (DOM events in browsers)
- **No existing I/O standard library** - Dahl could build purely non-blocking I/O from scratch without breaking existing conventions
- **No legacy baggage** - most languages were tied to "one thread per connection" models

#### 4. Open Source Licensing

- V8 released under **BSD license** (very permissive)
- Allowed Node.js to be developed as free, open-source project
- No licensing hurdles or commercial restrictions

### Historical References

**Primary sources documenting these decisions:**

1. **[Original 2009 JSConf EU Presentation](https://www.youtube.com/watch?v=ztspvPYybIY)** ⭐
   - Ryan Dahl's definitive explanation of why he combined V8 with an event loop
   - Explains the "concurrency problem" and the Node.js architecture
   - First public introduction of Node.js

2. **[Node.js Official Documentation on V8](https://nodejs.org/en/learn/getting-started/the-v8-javascript-engine)**
   - Modern summary of the V8-Node.js relationship

3. **[Dahl's 2018 "10 Things I Regret About Node.js" Talk](https://www.youtube.com/watch?v=M3BM9TB-8yA)** ⭐
   - Retrospective on original design choices
   - Discusses build system and V8 coupling decisions
   - Honest reflection on what worked and what didn't

### js2c Evolution Timeline

**2009-2018**: `js2c.py` (Python implementation)
- **Origin**: Borrowed from V8 project (Copyright 2006-2008 V8 authors)
- **Purpose**: V8 needed to embed ECMAScript builtins (like `Array.prototype.map`) as C++ byte arrays
- Ryan Dahl extended this pattern to embed entire Node.js standard library

**2018**: Python 3 compatibility refactoring

**May 2023**: Ported to C++ as `js2c.cc` (PR #46997 by Joyee Cheung)
- **Performance**: 1.5s → 0.1s (15x faster build time)
- **Memory**: 110MB → 66MB during build
- **Rationale**: "Makes it easier to use third-party dependencies. It is also much faster."
- **Additional benefit**: Better handling of linker limits (large static arrays in C++ can stress compilers/linkers)

### Why No Formal ADRs?

Despite extensive research, no formal documentation exists:
- ❌ Architecture Decision Records (ADRs)
- ❌ Design documents in `/doc/` explaining this choice
- ❌ Original 2009 discussions or GitHub issues
- ❌ Blog posts by Ryan Dahl specifically about embedding

**Why?** This was a **natural adoption of V8's proven practices** from day one (May 2009), aligned with Node.js's performance-first philosophy. It wasn't a deliberate architectural decision made later - it was foundational to the project's initial design.

## Why V8 Uses js2c (The Ancestry)

Before understanding Node.js's use of js2c, it's important to understand why V8 created this tool:

**The Problem:**
- JavaScript engines must implement parts of the ECMAScript specification in JavaScript itself
- Examples: `Array.prototype.map`, `String.prototype.trim`, Promise implementation
- These are called "JavaScript builtins" or "self-hosted builtins"

**Why not load from disk?**
- An engine cannot depend on an external filesystem to find its own basic functions
- Must be available before any user code runs
- Performance: disk I/O would slow down engine initialization

**The Solution:**
- Embed JavaScript implementations as C++ byte arrays
- V8 created `js2c` to automate this conversion
- JavaScript builtins become part of the compiled V8 library

**Ryan Dahl's Innovation:**
- Extended V8's `js2c` pattern to embed the **entire Node.js standard library**
- Applied the same logic to `fs`, `http`, `crypto`, etc.
- Inherited a proven solution from V8's existing architecture

## Build Process

### 1. js2c.cc - JavaScript to C++ Converter

**File:** `tools/js2c.cc`

A C++ program that converts JavaScript to C++ data structures:
- Reads all `.js` and `.mjs` files from `lib/` directory
- Converts each file into C++ static byte arrays
- Generates `node_javascript.cc` containing all embedded code as C++ data

### 2. node.gyp - Build Configuration

Orchestrates the embedding process:

```gyp
'action_name': 'node_js2c',
'inputs': [
  '<@(library_files)',  # All lib/*.js files
],
'outputs': [
  '<(SHARED_INTERMEDIATE_DIR)/node_javascript.cc',  # Generated C++ file
],
```

### 3. BuiltinLoader - Runtime Access

**Files:** `src/node_builtins.cc` and `src/node_builtins.h`

Runtime loader that accesses embedded modules:
- Stores JavaScript sources in a thread-safe in-memory map
- Loads modules by ID from embedded data
- No file I/O needed at runtime

## Evidence from Node.js Source Code

### From `lib/internal/bootstrap/realm.js`:
```javascript
// core modules are compiled into the node binary via node_javascript.cc
// generated by js2c.cc, so they can be loaded faster without the cost of I/O.
```

### From `src/node_builtins.h`:
```cpp
// JavaScript sources are bundled into the binary as static data.
// The tool tools/js2c.cc generates node_javascript.cc, which populates
// the source map.
```

### From `src/node_builtins.cc`:
```cpp
const auto source_it = source->find(id);  // Looks up embedded JS by ID
```

## The Complete Flow

### Basic Embedding (js2c)

1. **Build time:** `js2c.cc` reads `lib/*.js` → generates `node_javascript.cc` with C++ byte arrays
2. **Compile time:** `node_javascript.cc` gets compiled into the Node.js binary
3. **Runtime:** `BuiltinLoader` accesses embedded JavaScript from memory (no disk reads)

### Modern Optimization: V8 Snapshots (Node.js v12+)

Beyond just embedding source code, modern Node.js uses **V8 Snapshots** for even faster startup:

**How it works:**
1. During build, Node.js **executes** bootstrap code and core modules
2. Saves the resulting **heap state** (initialized objects, functions, etc.) into the binary
3. At runtime, deserializes the pre-initialized heap instead of parsing/executing from scratch

**Benefits:**
- Core modules aren't just *stored* - they're **pre-initialized**
- Eliminates parsing and initial execution time
- Significantly faster startup compared to parsing embedded JavaScript

**Files involved:**
- `tools/snapshot/` - Snapshot generation tools
- `tools/snapshot/node_mksnapshot.cc` - Main snapshot builder
- Built on top of V8's own startup snapshot system

### Internal vs Public Modules

The `BuiltinLoader` distinguishes between two types of embedded modules:

1. **Public modules** (e.g., `fs`, `http`, `crypto`)
   - Can be loaded via `require('fs')` from user code
   - Exposed API surface

2. **Internal modules** (e.g., `lib/internal/*`)
   - Cannot be `require()`d from user applications
   - Used internally by Node.js core
   - Access restricted by the loader

Both types are embedded using the same `js2c` process, but runtime access rules differ.

## Embedded Modules (73 files)

All standard library modules are embedded:
- Core: `fs.js`, `http.js`, `https.js`, `net.js`, `crypto.js`, `stream.js`, `buffer.js`, `events.js`
- Internal: `_http_agent.js`, `_http_client.js`, `_http_server.js`, etc.
- Utilities: `path.js`, `url.js`, `util.js`, `os.js`, `process.js`, etc.

## Benefits

1. **Performance** - Faster startup, no disk I/O for core modules
2. **Distribution** - Single binary is easier to distribute
3. **Security** - Core modules can't be tampered with

## Where to Find Source Code

### The Reality

The standard library `.js` files **do not exist as separate files** on your machine. They are **compiled directly into the Node.js binary**:

- **macOS/Linux**: `/usr/local/bin/node` or `/usr/bin/node`
- **Windows**: `C:\Program Files\nodejs\node.exe`

When you `require('fs')`, Node.js isn't reading a file from disk - it's accessing a memory address inside its own process where the code was loaded during startup.

### How to View the Source Code

#### Option 1: Chrome DevTools (Best for Debugging) ⭐

View embedded source code at runtime using Chrome's developer tools:

1. **Start Node.js with inspector:**
   ```bash
   node --inspect
   ```

2. **Open Chrome and navigate to:**
   ```
   chrome://inspect
   ```

3. **Click "Open dedicated DevTools for Node"**

4. **Go to the Sources tab**

5. **Look for the `node:internal` folder**
   - This shows all embedded internal modules
   - You can read, debug, and set breakpoints in the actual embedded code

**This is the closest you can get to "finding" the files on your machine locally!**

#### Option 2: Clone Node.js Repository

Get the source code before it's embedded:

```bash
git clone https://github.com/nodejs/node.git
cd node
git checkout v24.9.0  # Match your Node version
ls lib/  # All source files are here
```

#### Option 3: View on GitHub

- **Main branch**: https://github.com/nodejs/node/tree/main/lib/
- **Specific version**: https://github.com/nodejs/node/tree/v24.9.0/lib/

#### Option 4: TypeScript Type Definitions (Locally Available)

```bash
ls node_modules/@types/node/*.d.ts
```

These provide type signatures and documentation but **not implementations**.

### Summary Table

| Search Location | Result | Why? |
|----------------|--------|------|
| **Program Files / bin** | ❌ Not found | Code is inside the binary as byte arrays |
| **node_modules** | ❌ Not found | `node_modules` is only for 3rd-party packages (npm) |
| **GitHub (node/lib)** | ✅ Found | Source code before embedding |
| **Chrome DevTools (--inspect)** | ✅ Found | Inspector extracts embedded code at runtime |
| **@types/node** | ⚠️ Type signatures only | No implementation code |

### Development Mode (Advanced)

For Node.js core development, you can force Node.js to load modules from disk instead of embedded sources:

```bash
NODE_BUILTIN_MODULES_PATH=/path/to/node/lib node script.js
```

**Warning**: This is only for Node.js developers working on Node.js itself, not for regular application development.
