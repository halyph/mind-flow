# Scripting in Scala
> | scala |

Scala language compiles sources code to Java bytecode.  But, it has some nice scripting facilities. Let's review them.

So, the `scala` command is also a shell-script wrapper around the java command.

According to official [scala utility] documentation (here highlighted only post-related notes):

> `scala [ <option> ]... [ <torun> <argument>... ]`
>
> The `scala` utility runs Scala code using a Java runtime environment. 
>
>If a **script** file is specified to run, then the file is read and all Scala statements and declarations in the file are processed in order. Any arguments specified will be available via the argsvariable. 
>
>Script files may have an **optional header** that is ignored if present. There are two ways to format the header: either beginning with #! and ending with !#, or beginning with ::#! and ending with ::!#.
>
> Such a header must have each header boundary start at the beginning of a line. Headers can be used to make stand-alone script files, as shown in the examples below.
> 
>Here is a complete Scala script (**check.sh**) for Unix:
>
>```
>#!/bin/sh
>exec scala "$0" "$@"
>!#
>Console.println("Hello, world!")
>argv.toList foreach Console.println
>```
>Here is a complete Scala script (**check.bat**) for MS Windows:
>
>```
>::#!
>@echo off
>call scala %0 %*
>goto :eof
>::!#
>Console.println("Hello, world!")
>argv.toList foreach Console.println
>```
>If you want to use the compilation cache to speed up multiple executions of the script (**check.sh**), then add **-savecompiled** to the scala command:
>
>```
>#!/bin/sh
>exec scala -savecompiled "$0" "$@"
>!#
>Console.println("Hello, world!")
>argv.toList foreach Console.println
>```

These tricks give us an ability to run Scala script as plain shell script. Also, based on the setting above this script can have input parameters and *almost* cross-platform (see script header differences for Linux **.vs.** Windows).

Now, we should save the mentioned above code snippet in some file (e.g. **check.sh**) and make it executable. This script can be run as any Linux shell script `./check.sh` (`check.bat` - Windows).

## Scala utility internals

### Linux

Linux script header uses the next items:

- `#!` it's [shebang] interpreter directive
- `exec` is used to run `scala` without creation new process. Commands which go right after `exec` will not be executed
- `!#` is simple marker for `scala` utility (see notes below)

E.g. 
This script 

```
#! /bin/sh
echo Header
exec echo
!#
echo Body
```

will have the next output

```
$ ./test.sh
Header
```

We will get error in case `exec` is removed:

```
#! /bin/sh
echo Header
!#
echo Body
```

Output

```
$ ./test.sh
Header
./test.sh: line 4: !#: command not found
Body

```

### Windows

Windows batch script header uses the next items:

- `::` is a remark without displaying or executing that line when the batch file is run (see [Information on batch files]).
- `::#!`  is simple marker for `scala` utility (see notes below)
- `@echo off` disable echo
- `call` calls one batch program from another.
- `goto :eof` go to end of file
- `::!#` is simple marker for `scala` utility (see notes below)

The OS-specific script settings were identified, now let's dive deeper to understand how `scala` utility works.

### `scala` internals

This utility performs the next flow to run script:

1. Run `scala.tools.nsc.MainGenericRunner#process` and identify run target "as Script" (there are other targets) `ScriptRunner.runScriptAndCatch(settings, thingToRun, command.arguments)` 
2. `ScriptRunner` creates temp file `File.makeTemp("scalacmd", ".scala")`
3. Run compiler and clean script header

```scala
class ScriptRunner extends HasCompileSocket {
...
  private def withCompiledScript(
      settings: GenericRunnerSettings,
      scriptFile: String)
      (handler: String => Boolean): Boolean =
    {
      def mainClass = scriptMain(settings)
  
         val compiler = newGlobal(settings, reporter)
         new compiler.Run compile List(scriptFile)
```

```scala
class Global
    /** If this compilation is scripted, convert the source to a script source. */
    private def scripted(s: SourceFile) = s match {
      case b: BatchSourceFile if settings.script.isSetByUser => ScriptSourceFile(b)
      case _ => s
    }

    /** Compile abstract file until `globalPhase`, but at least
     *  to phase "namer".
     */
    def compileLate(file: AbstractFile) {
      if (!compiledFiles(file.path))
        compileLate(new CompilationUnit(scripted(getSourceFile(file))))
    }

```

4. Cleanup shell script (remove header) via `SourceFile`. Now, it's clear why script's header have such *strange* closing markers (see line 21, `content drop headerLen` - actual header remove)

```scala
object ScriptSourceFile {
  /** Length of the script header from the given content, if there is one.
   *  The header begins with "#!" or "::#!" and ends with a line starting
   *  with "!#" or "::!#".
   */
  def headerLength(cs: Array[Char]): Int = {
    val headerPattern = Pattern.compile("""((?m)^(::)?!#.*|^.*/env .*)(\r|\n|\r\n)""")
    val headerStarts  = List("#!", "::#!")

    if (headerStarts exists (cs startsWith _)) {
      val matcher = headerPattern matcher cs.mkString
      if (matcher.find) matcher.end
      else throw new IOException("script file does not close its header with !# or ::!#")
    }
    else 0
  }

  def apply(file: AbstractFile, content: Array[Char]) = {
    val underlying = new BatchSourceFile(file, content)
    val headerLen = headerLength(content)
    val stripped = new ScriptSourceFile(underlying, content drop headerLen, headerLen)

    stripped
  }
```

## Add libraries to Scala script

Scala script libraries (**jar**s) can be added in script's header section:

```bash
#!/bin/sh
exec scala -classpath "lib/lib.1.jar:lib/lib.2.jar" "$0" "$@"
!#
```

## Summary

There is nothing magical in Scala interpretation. Every single peace of code must be compiled. Such interesting *scripting* approach can be applied to Java as well.

Unfortunately, Scala is not looks like nice scripting language (because it's **not** designed for this use case). It will be uncomfortable "scripting" in Scala without IDE.

- [scala utility](http://www.scala-lang.org/files/archive/nightly/docs-2.10.1/manual/html/scala.html)
- [shebang](http://en.wikipedia.org/wiki/Shebang_(Unix))
- [Information on batch files](http://www.computerhope.com/batch.htm)

## References

- [System Scripting with Scala](http://timperrett.com/2011/08/01/system-scripting-with-scala/)
- [scala utility]
- [shebang]
- [Information on batch files]
- Scala Sources:
  - [ScriptRunner.scala](https://github.com/scala/scala/blob/v2.11.5/src/compiler/scala/tools/nsc/ScriptRunner.scala#)
  - [SourceFile.scala](https://github.com/scala/scala/blob/v2.11.5/src/reflect/scala/reflect/internal/util/SourceFile.scala)
  - [Global.scala](https://github.com/scala/scala/blob/v2.11.5/src/compiler/scala/tools/nsc/Global.scala)