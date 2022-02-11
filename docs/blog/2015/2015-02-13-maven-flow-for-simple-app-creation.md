# Maven Flow for Simple App Creation
> | java | maven |

I provided my reflections about *"Java for Everything"* in the previous [post](2015-02-12-do-we-need-java-for-everything.md).
Here we will review other implementation of this concept.

I have the next concerns about any Java application (big or small):

- library dependency management must be simple
- it's very bad practice to distribute sources along with libraries (dependency management tools must be used instead: Ivy, Maven, Gradle, etc.)
- small application might have a little bit different project layout (not equals to traditional Maven layout)
- we should be able to setup IDE (in my case [Intellij IDEA](https://www.jetbrains.com/idea/)) as quick a possible. I hate editing Java programs in plain text editor
- it must be a convenient way to run Java application with different arguments in *production* and *development* modes

## Use Case

We have to create simple and small REST application based on [Spark Java framework](https://github.com/perwendel/spark) (A Sinatra inspired framework for Java).

Here is the source:

```java
import static spark.Spark.get;
import static spark.SparkBase.port;

public class App {
    public static void main( String[] args ) throws NumberFormatException {
        
        for(String arg: args) System.out.printf("> %s", arg);
        
        get("/hello", (request, response) -> {
            return "Hello World!";
        });
    }
}
```

So, here is the list of issues:

- get Spark dependency with all transitive dependencies
- pass command-line arguments into the app
- use this application in development mode and in "production" (packed in jar)

## Traditional Maven Way

- Generate empty project via Maven archetype

```bash
mvn archetype:generate \
-DgroupId=com.halyph \ 
-DartifactId=sparkblog \ 
-Dpackage=com.halyph.blog \ 
-Dversion=1.0-SNAPSHOT \
-DarchetypeGroupId=org.apache.maven.archetypes \ 
-DarchetypeArtifactId=maven-archetype-quickstart \
-DinteractiveMode=false
```

- Open this in IDEA (I don't use other IDEs) via "Open File or Project" and select folder with generated **pom.xml** file. We don't need tests, so we can delete *src->test* folder and remove junit dependency from **pom.xml** file. Now, we can easily run our application via IDE.

- Add Spark framework dependency to **pom.xml** and update our **App** class

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.halyph</groupId>
  <artifactId>sparkblog</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>jar</packaging>

  <name>sparkblog</name>
  <url>http://maven.apache.org</url>

  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>

  <dependencies>
    <dependency>
      <groupId>com.sparkjava</groupId>
      <artifactId>spark-core</artifactId>
      <version>2.1</version>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.1</version>
        <configuration>
          <target>1.8</target>
          <source>1.8</source>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

```java
package com.halyph.blog;

import static spark.Spark.get;

public class App {
    public static void main(String[] args) throws NumberFormatException {

        String myArgs = "";
        for (String arg : args) {
            System.out.printf("> %s", arg);
            myArgs += arg + " : ";
        }
        System.out.println();
        final String finalMyArgs = myArgs;
        get("/hello", (request, response) -> {
            return "Hello World!\n args = " + finalMyArgs;
        });
    }
}
```

This application can be easily run via IDE, but lets run it via Maven

- We should use [Exec Maven Plugin] to run the app with all dependencies

```bash
$ mvn clean compile exec:java -Dexec.mainClass="com.halyph.blog.App"  -Dexec.args="9090 one 1 2"
[INFO] Scanning for projects...
[INFO]
[INFO] ------------------------------------------------------------------------
[INFO] Building sparkblog 1.0-SNAPSHOT
[INFO] ------------------------------------------------------------------------
[INFO]
[INFO] --- maven-clean-plugin:2.4.1:clean (default-clean) @ sparkblog ---
[INFO] Deleting d:\MyProjects\jwrapper\bloggg\sparkblog\target
[INFO]
[INFO] --- maven-resources-plugin:2.5:resources (default-resources) @ sparkblog ---
[debug] execute contextualize
[INFO] Using 'UTF-8' encoding to copy filtered resources.
[INFO] skip non existing resourceDirectory d:\MyProjects\sparkblog\src\main\resources
[INFO]
[INFO] --- maven-compiler-plugin:3.1:compile (default-compile) @ sparkblog ---
[INFO] Changes detected - recompiling the module!
[INFO] Compiling 1 source file to d:\MyProjects\jwrapper\bloggg\sparkblog\target\classes
[INFO]
[INFO] >>> exec-maven-plugin:1.2.1:java (default-cli) @ sparkblog >>>
[INFO]
[INFO] <<< exec-maven-plugin:1.2.1:java (default-cli) @ sparkblog <<<
[INFO]
[INFO] --- exec-maven-plugin:1.2.1:java (default-cli) @ sparkblog ---
> 9090> one> 1> 2
[Thread-1] INFO spark.webserver.SparkServer - == Spark has ignited ...
[Thread-1] INFO spark.webserver.SparkServer - >> Listening on 0.0.0.0:4567
[Thread-1] INFO org.eclipse.jetty.server.Server - jetty-9.0.2.v20130417
[Thread-1] INFO org.eclipse.jetty.server.ServerConnector - Started ServerConnector@4afe75c9{HTTP/1.1}{0.0.0.0:4567}
```

In case the application run configurations is persistent ("main" class and CLI arguments are changing rarely) we can configure it in **pom.xml**:

```xml
 <build>
    <plugins>
      ...
      <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>exec-maven-plugin</artifactId>
        <version>1.3.2</version>
        <executions>
          <execution>
            <goals>
              <goal>java</goal>
            </goals>
          </execution>
        </executions>
        <configuration>
          <mainClass>com.halyph.blog.App</mainClass>
          <arguments>
            <argument>9090</argument>
            <argument>one</argument>
            <argument>1</argument>
            <argument>2</argument>
          </arguments>
        </configuration>
      </plugin>
    </plugins>
  </build>
```

- It's nice idea to use `mvn exec:java`, but it might be a little bit slow. So, we might decide to use some shell script which increase compiled application ramp up time. The problem is that the application have dependencies (which have transitive dependencies). I.e. `java` classpath have to be configured somehow.

Well, I borrowed the ideas from "[A better java shell script wrapper]" script. Here it is:

```bash
#!/usr/bin/env bash
#
# Copyright 2012 Zemian Deng
#
# A wrapper script that run any Java application in unix/cygwin bash env.
#
# This script is assumed to be located in an application's "bin" directory. It will
# auto resolve its directory location relative to the application path (which is one
# parent up from the script.) Therefore, this script can be run any where in the file
# system and it will still reference the same application directory.
#
# This script will by default auto setup a Java classpath that picks up any "config"
# and "lib" directories under the application directory. It also will also add a
# any typical Maven project output directories such as "target/test-classes",
# "target/classes", and "target/dependency" into classpath. This can be disable by
# setting RUN_JAVA_NO_AUTOCP=1.
#
# If the "Default parameters" section bellow doesn't match to user's env, then user
# may override these variables in their terminal session or preset them in shell's
# profile startup script. The values of all path should be in cygwin/unix path,
# and this script will auto convert them into Windows path where is needed.
#
# User may customize the Java classpath by setting RUN_JAVA_CP, which will prefix to existing
# classpath, or use the "-cp" option, which will postfix to existing classpath.
#
# Usage:
#   run-java [java_opts] <java_main_class> [-cp /more/classpath] [-Dsysprop=value]
#
# Example:
#   run-java example.Hello
#   run-java example.Hello -Dname=World
#   run-java org.junit.runner.JUnitCore example.HelloTest -cp "$HOME/apps/junit/lib/*"
#
# Created by: Zemian Deng 03/09/2012

# This run script dir (resolve to absolute path)
SCRIPT_DIR=$(cd $(dirname $0) && pwd)    # This dir is where this script live.
APP_DIR=$(cd $SCRIPT_DIR/.. && pwd)      # Assume the application dir is one level up from script dir.

# Default parameters
JAVA_HOME=${JAVA_HOME:=$HOME/apps/jdk}     # This is the home directory of Java development kit.
RUN_JAVA_CP=${RUN_JAVA_CP:=$CLASSPATH}     # A classpath prefix before -classpath option, default to $CLASSPATH
RUN_JAVA_OPTS=${RUN_JAVA_OPTS:=}           # Java options (-Xmx512m -XX:MaxPermSize=128m etc)
RUN_JAVA_DEBUG=${RUN_JAVA_DEBUG:=}         # If not empty, print the full java command line before executing it.
RUN_JAVA_NO_PARSE=${RUN_JAVA_NO_PARSE:=}   # If not empty, skip the auto parsing of -D and -cp options from script arguments.
RUN_JAVA_NO_AUTOCP=${RUN_JAVA_NO_AUTOCP:=} # If not empty, do not auto setup Java classpath
RUN_JAVA_DRY=${RUN_JAVA_DRY:=}             # If not empty, do not exec Java command, but just print

# OS specific support.  $var _must_ be set to either true or false.
CYGWIN=false;
case "`uname`" in
  CYGWIN*) CYGWIN=true ;;
esac

# Define where is the java executable is
JAVA_CMD=java
if [ -d "$JAVA_HOME" ]; then
	JAVA_CMD="$JAVA_HOME/bin/java"
fi

# Auto setup applciation's Java Classpath (only if they exists)
if [ -z "$RUN_JAVA_NO_AUTOCP" ]; then
	if [ -d "$APP_DIR/config" ]; then RUN_JAVA_CP="$RUN_JAVA_CP:$APP_DIR/config" ; fi
	if [ -d "$APP_DIR/target/test-classes" ]; then RUN_JAVA_CP="$RUN_JAVA_CP:$APP_DIR/target/test-classes" ; fi
	if [ -d "$APP_DIR/target/classes" ]; then RUN_JAVA_CP="$RUN_JAVA_CP:$APP_DIR/target/classes" ; fi
	if [ -d "$APP_DIR/target/dependency" ]; then RUN_JAVA_CP="$RUN_JAVA_CP:$APP_DIR/target/dependency/*" ; fi
	if [ -d "$APP_DIR/lib" ]; then RUN_JAVA_CP="$RUN_JAVA_CP:$APP_DIR/lib/*" ; fi
fi

ARGS="$@"
# Parse addition "-cp" and "-D" after the Java main class from script arguments
#   This is done for convenient sake so users do not have to export RUN_JAVA_CP and RUN_JAVA_OPTS
#   saparately, but now they can pass into end of this run-java script instead.
#   This can be disable by setting RUN_JAVA_NO_PARSE=1.
if [ -z "$RUN_JAVA_NO_PARSE" ]; then
	# Prepare variables for parsing
	FOUND_CP=
	NEW_ARGS[0]=''
	IDX=0

	# Parse all arguments and look for "-cp" and "-D"
	for ARG in "$@"; do
		if [[ -n $FOUND_CP ]]; then
			RUN_JAVA_CP="$RUN_JAVA_CP:$ARG"
			FOUND_CP=
		else
			case $ARG in
			'-cp')
				FOUND_CP=1
				;;
			'-D'*)
				RUN_JAVA_OPTS="$RUN_JAVA_OPTS $ARG"
				;;
			*)
				NEW_ARGS[$IDX]="$ARG"
				let IDX=$IDX+1
				;;
			esac
		fi
	done
	ARGS="${NEW_ARGS[@]}"
fi

# Convert Windows Java Classpath
if $CYGWIN; then
	RUN_JAVA_CP=$(cygpath -mp $RUN_JAVA_CP)
fi

# Display full Java command.
if [ -n "$RUN_JAVA_DEBUG" ] || [ -n "$RUN_JAVA_DRY" ]; then
	echo "$JAVA_CMD" $RUN_JAVA_OPTS -cp "$RUN_JAVA_CP" $ARGS
fi

# Run Java Main class
if [ -z "$RUN_JAVA_DRY" ]; then
	"$JAVA_CMD" $RUN_JAVA_OPTS -cp "$RUN_JAVA_CP" $ARGS
fi
```

The main idea is to run `mvn dependency:copy-dependencies`, this will generate all the jar files into `target/dependency` folder

```bash
$ mvn dependency:copy-dependencies
[INFO] Scanning for projects...
[INFO]
[INFO] ------------------------------------------------------------------------
[INFO] Building sparkblog 1.0-SNAPSHOT
[INFO] ------------------------------------------------------------------------
[INFO]
[INFO] --- maven-dependency-plugin:2.1:copy-dependencies (default-cli) @ sparkblog ---
[INFO] Copying spark-core-2.1.jar to d:\MyProjects\jwrapper\bloggg\sparkblog\target\dependency\spark-core-2.1.jar
[INFO] Copying jetty-http-9.0.2.v20130417.jar to d:\MyProjects\jwrapper\bloggg\sparkblog\target\dependency\jetty-http-9.0.2.v20130417.jar
[INFO] Copying jetty-io-9.0.2.v20130417.jar to d:\MyProjects\jwrapper\bloggg\sparkblog\target\dependency\jetty-io-9.0.2.v20130417.jar
[INFO] Copying jetty-security-9.0.2.v20130417.jar to d:\MyProjects\jwrapper\bloggg\sparkblog\target\dependency\jetty-security-9.0.2.v20130417.jar
[INFO] Copying jetty-server-9.0.2.v20130417.jar to d:\MyProjects\jwrapper\bloggg\sparkblog\target\dependency\jetty-server-9.0.2.v20130417.jar
[INFO] Copying jetty-servlet-9.0.2.v20130417.jar to d:\MyProjects\jwrapper\bloggg\sparkblog\target\dependency\jetty-servlet-9.0.2.v20130417.jar
[INFO] Copying jetty-util-9.0.2.v20130417.jar to d:\MyProjects\jwrapper\bloggg\sparkblog\target\dependency\jetty-util-9.0.2.v20130417.jar
[INFO] Copying jetty-webapp-9.0.2.v20130417.jar to d:\MyProjects\jwrapper\bloggg\sparkblog\target\dependency\jetty-webapp-9.0.2.v20130417.jar
[INFO] Copying jetty-xml-9.0.2.v20130417.jar to d:\MyProjects\jwrapper\bloggg\sparkblog\target\dependency\jetty-xml-9.0.2.v20130417.jar
[INFO] Copying javax.servlet-3.0.0.v201112011016.jar to d:\MyProjects\jwrapper\bloggg\sparkblog\target\dependency\javax.servlet-3.0.0.v201112011016.jar
[INFO] Copying slf4j-api-1.7.7.jar to d:\MyProjects\jwrapper\bloggg\sparkblog\target\dependency\slf4j-api-1.7.7.jar
[INFO] Copying slf4j-simple-1.7.7.jar to d:\MyProjects\jwrapper\bloggg\sparkblog\target\dependency\slf4j-simple-1.7.7.jar
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 2.978s
[INFO] Finished at: Thu Feb 12 18:22:54 EET 2015
[INFO] Final Memory: 9M/243M
[INFO] ------------------------------------------------------------------------
```

Now, we can reuse the provided *above* script **or** use the provided *below* one-liner:

```bash
java -cp target\classes;target\dependency\* com.halyph.blog.App 9090 one 1 2
```

This one-liner is very simple and can be transformed to shell/batch scripts depending on the level of re-use you'd like to implement.

- Now, it's time to created pre-packed application bundle which can be easily distributed. We will use [Maven Application Assembler Plugin]:

```xml
 <build>
    <plugins>
     ...
      <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>appassembler-maven-plugin</artifactId>
        <version>1.9</version>
        <!--
        This (executions) section can be omitted.
        In case it's omitted we should call the next command to generate wrapper:
        mvn package appassembler:assemble
        -->
        <executions>
          <execution>
            <phase>package</phase>
            <goals>
              <goal>assemble</goal>
            </goals>
          </execution>
        </executions>
        <configuration>
          <programs>
            <program>
              <mainClass>com.halyph.blog.App</mainClass>
              <id>app</id>
            </program>
          </programs>
        </configuration>
      </plugin>
    </plugins>
  </build>
```

> The Application Assembler Plugin is a Maven plugin for generating scripts for starting java applications. All dependencies and the artifact of the project itself are placed in a generated Maven repository in a defined assemble directory. All artifacts (dependencies + the artifact from the project) are added to the classpath in the generated bin scripts.

[Maven Application Assembler Plugin] usage:

```bash  
$ mvn package
$ target/appassembler/bin/app
```

> - All dependencies and the artifact itself are placed in the defined assemble directory (defaults to `$project.build.directory/appassembler`).
>
> - A `bin/` directory is created in the assemble directory and the generated bin scripts are placed in that directory (defaults to both unix shell scripts and Windows bat files).

Note: [Maven Application Assembler Plugin] have a lot of customization options, just check the documentation. 

## Summary

Here was shown that using such tool as Maven you can be productive and "agile" (use [Gradle](http://gradle.org) if you'd like to be in trend):

- generate project skeleton from scratch
- open it in IDE without ceremony
- call the app via Maven plugin
- call it as plain CLI application, but with small ceremony (need to run *dependency:copy-dependencies*)
- package the app for further distribution

Yes, it's not a simple *write-one* Java "script", but it's flexible enough to feel like it is.

## References

- [Do We Need Java for Everything?](2015-02-12-do-we-need-java-for-everything.md)
- [A better java shell script wrapper](http://saltnlight5.blogspot.com/2012/08/a-better-java-shell-script-wrapper.html)
- [Exec Maven Plugin](http://mojo.codehaus.org/exec-maven-plugin/usage.html)
- [Maven Application Assembler Plugin](http://mojo.codehaus.org/appassembler/appassembler-maven-plugin/usage-program.html)
- [Wrapper Script for Java Command-Line Applications](http://blog.plesslweb.ch/post/6628462331/wrapper-script-for-java-command-line-applications)
