# Do We Need Java for Everything?
> | java |

Some time ago one guy wrote a post [Java for Everything]. The main idea is to use Java even for shell scripting.
> I’m even taking this to an extreme and using Java for shell scripts. I’ve found that anything other than a simple wrapper shell script eventually grows to the point where I’m looking up the arcane syntax for removing some middle element from an array in bash ... Write it in Java to start with. If shelling out to run commands is clumsy, write a utility function to make it easy.
>I’ve also written a *java_launcher* shell script that allows me to write this at the top of Java programs:

```bash
#!/usr/bin/env java_launcher
# vim:ft=java
# lib:/home/lk/lib/teamten.jar
```

>I can make the Java programs executable and drop the .java extension. The script strips the header, compiles and caches the class file, and runs the result with the specified jars. It provides one of the big advantages of Python: the lack of build scripts for simple one-off programs.

Here is the actual source of [java_launcher]:

```bash
#!/bin/bash

# Put this script in your path and write the following line at the top of an
# executable Java source program:
#
#   #!/usr/bin/env java_launcher
#
# Additional documentation here: https://github.com/lkesteloot/java_launcher

# Quit on error.
set -e

# Get the name of the script, which the shell passes to us automatically.
SOURCE_PATHNAME=$1
if [ "$SOURCE_PATHNAME" = "" ]; then
    echo "java_launcher: Must supply name of script as first argument."
    exit 1
fi

# Skip the script name.
shift

# Compute the MD5 of both the source file and this script.
if [ -f /sbin/md5 ]; then
    # Mac OS/X.
    SUM=$(cat "$SOURCE_PATHNAME" $0 | md5)
else
    # Linux.
    SUM=$(cat "$SOURCE_PATHNAME" $0 | md5sum | cut -d' ' -f1)
fi
SOURCE_FILENAME=$(basename "$SOURCE_PATHNAME")
SOURCE_DIR=$(dirname "$SOURCE_PATHNAME")
CLASS_NAME=$(echo $SOURCE_FILENAME | sed -e 's/\.*//')
CACHE_DIR=$HOME/.java_launcher_cache
CLASS_DIR=$CACHE_DIR/$SUM
PROCESSED_SOURCE=$CLASS_DIR/${SOURCE_FILENAME}.java
PROCESSED_CLASS=$CLASS_DIR/${SOURCE_FILENAME}.class

# Process source to find libs for classpath. Relative jars are made relative to the
# source file.
export CLASSPATH=$(awk 'BEGIN { CLASSPATH="" } /^# lib:(.*)$/ { jar = substr($0, 7); if (substr(jar, 1, 1) != "/") jar = SOURCE_DIR "/" jar; if (CLASSPATH != "") CLASSPATH = CLASSPATH ":"; CLASSPATH = CLASSPATH jar } END { print CLASSPATH }' SOURCE_DIR="$SOURCE_DIR" < "$SOURCE_PATHNAME")

# Default libraries. Put default ones last.
SCRIPT_DIR=$(dirname $0)
LIB_DIR=$SCRIPT_DIR/java_lib
export CLASSPATH=$CLASSPATH:$LIB_DIR/\*

# Compile if necessary.
if [ -f "$PROCESSED_CLASS" ]; then
    # Refresh the dir so that we know we've used it recently.
    touch "$CLASS_DIR"
else
    mkdir -p "$CLASS_DIR"

    # Remove header. That's anything that starts with #. Replace the lines with
    # an empty line so the line numbers don't get thrown off.
    sed -e 's/^#.*//' < "$SOURCE_PATHNAME" > "$PROCESSED_SOURCE"

    # Compile real source to our cache.
    javac -d "$CLASS_DIR" "$PROCESSED_SOURCE"
fi

# Run the program, passing on arguments from command line.
export CLASSPATH=$CLASS_DIR:$CLASSPATH
java -Xmx1024m $CLASS_NAME $*
```

And suppose we'd like to run **helloworld** Java "script" using different jars located in default library location (**java_lib/**) and custom (**/home/username/mylib1.jar** and **/home/username/mylib2.jar**)

```bash
#!/usr/bin/env java_launcher
# vim:ft=java
# lib:/home/username/mylib1.jar:/home/username/mylib2.jar

public class helloworld {
    public static void main(String[] args) {
        System.out.println("Hello world!");
    }
}
```

It can be run like this: `$ ./helloworld`

### So, how does java_launcher work?

1. This launcher script works on Linux/MacOSX only. We should have additional **java_launcher.bat** script for Windows (cygwin and msys are not native Windows solution).    
2. It supports two types of CLASSPATH lib folders
    - *default* **$SCRIPT_DIR/java_lib** located in the same folder where the actual Java script located 
    - *custom* libs, they should be listed at the head **lib** section of the script (see sample above). The script uses AWK to extract jars from **lib** section 
3. **java_launcher** uses MD5 hashing to track source changes and (re)compile the source script only when it has been changed. See MD5 calculated `SUM` variable above 
4. *launcher* has dedicated folder where it stores the processed and compiled script (based on MD5 hash changes). See the next variables: `CACHE_DIR`, `PROCESSED_SOURCE` and `PROCESSED_CLASS`.   
5. Then it combines the *default* and *custom* libs in resulted CLASSPATH 

### Drawbacks

I see the next drawbacks:

- libs should be distributed along with actual "script". The common use case is to have minimal required script, which downloads all required dependencies by yourself
- launcher is not cross-platform
- Java script requires additional configuration to be opened/edited in IDE (project file, adjust all dependencies, etc.)
- it's very hard to edit Java code in plain editor (Java language is verbose). Scripting in Java without IDE might be real pain

## Why not Groovy?

I don't think that Java is "good" language for scripting (see drawbacks above). Groovy is much better language with nice scripting capabilities. Every Groovy script might be treated like a Java code snippet (with some exceptions [[1]][Differences from Java] and [[2]](http://groovy-lang.org/differences.html)). But, the most important is that Groovy has build-in [Grape dependency manager]:
> Grape (The Groovy Adaptable Packaging Engine or Groovy Advanced Packaging Engine) is the infrastructure enabling the grab() calls in Groovy, a set of classes leveraging Ivy to allow for a repository driven module system for Groovy. This allows a developer to write a script with an essentially arbitrary library requirement, and ship just the script. Grape will, at runtime, download as needed and link the named libraries and all dependencies forming a transitive closure when the script is run from existing repositories such as JCenter, Ibiblio, Codehaus, and java.net.

Sample usage:

```groovy
@Grapes([
   @Grab(group='commons-primitives', module='commons-primitives', version='1.0'),
   @Grab(group='org.ccil.cowan.tagsoup', module='tagsoup', version='0.9.7')])
class Example {
// ...
}
```

> One or more `groovy.lang.Grab` annotations can be added at any place that annotations are accepted to tell the compiler that this code relies on the specific library. This will have the effect of adding the library to the classloader of the groovy compiler. This annotation is detected and evaluated before any other resolution of classes in the script, so imported classes can be properly resolved by a @Grab annotation.

**So, I have no idea why to reinvent the wheel.** Use Groovy for scripting and Java for everything else.

## References

- [Java for Everything](http://www.teamten.com/lawrence/writings/java-for-everything.html)
- Some reflections to the original post [Java for Everything]:
  - [Hacker News](https://news.ycombinator.com/item?id=8677556)
  - [Reddit](http://www.reddit.com/r/programming/duplicates/2nvybk/java_for_everything)
- [java_launcher](https://github.com/lkesteloot/java_launcher) source code
- [Groovy Differences from Java](https://groovy-lang.org/differences.html)
- [Grape dependency manager](https://groovy-lang.org/grape.html)
