# How to Generate PermGen leak?
> | java |

I'm sure that a lot of Java developers experienced `java.lang.OutOfMemoryError: PermGen space` (OOME PermGen). It was very common to get this error after multiple WAR re-deploys on Tomcat v.6.x. Permanent generation (PermGen) region of memory is used to store the internal representation of loaded classes (and much more, see here [[1]] and [[2]]).

So, we can get **OOME PermGen** when ClassLoader whats to store class definition, but there is not enough space in PermGen - i.e. loaded too many classes. 

Based on this **OOME PermGen** error can be generated via:

- decreasing PermGen size
- loading huge amount of classes

I highly recommend to read [What is a PermGen leak?](https://plumbr.eu/blog/what-is-a-permgen-leak) post to get more info about this issue.

## Disclaimer

The current post is totally based on [How (not) to create a permgen leak?](https://plumbr.eu/blog/how-not-to-create-a-permgen-leak)

## Generate PermGen leak

The main idea is dynamically create a lot of classes via byte code manipulation library. We are going to use [Javassist](http://www.csg.ci.i.u-tokyo.ac.jp/~chiba/javassist/) as it's the simplest library with nice API.

- We assume that it's `maven` based project. So, let's add Javassist to `pom.xml`.

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.mycompany.app</groupId>
  <artifactId>my-app</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>jar</packaging>

  <name>my-app</name>
  <url>http://maven.apache.org</url>

  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <skipTests>true</skipTests>
  </properties>

  <dependencies>
    <dependency>
      <groupId>org.javassist</groupId>
      <artifactId>javassist</artifactId>
      <version>3.15.0-GA</version>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>appassembler-maven-plugin</artifactId>
        <version>1.9</version>
        <configuration>
          <extraJvmArguments>-XX:PermSize=2M -XX:MaxPermSize=4M</extraJvmArguments>
          <programs>
            <program>
              <mainClass>com.mycompany.app.App</mainClass>
              <id>app</id>
            </program>
          </programs>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

- Also, we should set **PermGen** and **MaxPermGen** size to 2M and 4M respectively (it gives us a chance to get error as quickly as possible). Maven `Appassembler` plugin [[3]] uses `extraJvmArguments` parameter while generating wrapper scripts: shell and batch (see `pom.xml` above, `<extraJvmArguments>-XX:PermSize=2M -XX:MaxPermSize=2M</extraJvmArguments>`).

> --XX:PermSize<size> - Set initial PermGen Size

> --XX:MaxPermSize<size> - Set the maximum PermGen Size

- Below is a simple application which dynamically creates 1000 classes to cause PermGem leak. Class creation is very simple and self explanatory. The main idea is that we should use byte code manipulation library to create classes dynamically.

See additional comments in the next code snippet

```java
package com.mycompany.app;

import javassist.CannotCompileException;
import javassist.ClassPool;

import java.util.concurrent.TimeUnit;

/**
 * Steps to build and run demo application: <br />
 *
 * <li>mvn clean package appassembler:assemble
 * <li>target/appassembler/bin/app
 *
 */
public class App {
    /**
     * We should use static block for OutOfMemoryError "initialization"
     * It's very important to have it. In other case JVM won't be able to
     * throw (actually create new OutOfMemoryError) this exception because
     * there will be no free memory for this. That's why we creating it beforehand.
     * As you can see we intentionally added output to highlight that THIS error
     * was produces by us.
     */
    static {
        new OutOfMemoryError().printStackTrace();
        try {
            TimeUnit.SECONDS.sleep(1);
            System.out.println("=====================");
            System.out.println("Initialized/created OutOfMemoryError");
            System.out.println("=====================");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) throws Exception {
        System.out.println("Start dynamic class creation.....\n");
        for (int i = 0; i < 1000; i++) {
            Class clazz = createClass("MyClass" + i);
            // we use this output as indicator to see the rough number of created classes
            // it's not necessary to print every single (just created) class
            if(i % 50 == 0) System.out.println(clazz);
        }
    }

    private static Class createClass(String className) throws CannotCompileException {
        ClassPool pool = ClassPool.getDefault();
        return pool.makeClass(className).toClass();
    }
}
```

- Run the application

```bash
$ mvn clean package appassembler:assemble
$ target/appassembler/bin/app
java.lang.OutOfMemoryError
	at com.mycompany.app.App.<clinit>(App.java:15)
=====================
Initialized/created OutOfMemoryError
=====================
Start dynamic class creation.....

class MyClass0
class MyClass50
class MyClass100
class MyClass150
class MyClass200
class MyClass250
class MyClass300
class MyClass350
class MyClass400
class MyClass450
class MyClass500
class MyClass550
Exception in thread "Reference Handler" java.lang.OutOfMemoryError: PermGen space
	at java.lang.ref.Reference$ReferenceHandler.run(Reference.java:140)
Exception in thread "main" java.lang.OutOfMemoryError: PermGen space
	at javassist.ClassPool.toClass(ClassPool.java:1089)
	at javassist.ClassPool.toClass(ClassPool.java:1032)
	at javassist.ClassPool.toClass(ClassPool.java:990)
	at javassist.CtClass.toClass(CtClass.java:1125)
	at com.mycompany.app.App.createClass(App.java:36)
	at com.mycompany.app.App.main(App.java:29)
```

The next command runs under the hood:
`java -XX:PermSize=2M -XX:MaxPermSize=4M -classpath "$CLASSPATH" com.mycompany.app.App`

As you can see it was possible to create about 550 `MyClass` classes before we've got an expected error.

### Tomcat Leaks

Tomcat team created a nice [wiki page](http://wiki.apache.org/tomcat/MemoryLeakProtection) where listed and shown the situations where leaks can be detected and fixed.

## References

- [What is a PermGen leak?](https://plumbr.eu/blog/what-is-a-permgen-leak)
- [How (not) to create a permgen leak?](https://blogs.oracle.com/jonthecollector/entry/)
- [Where Has the Java PermGen Gone?](http://www.infoq.com/articles/Java-PERMGEN-Removed) PermGen is replace with Metaspace in Java 8
- [Presenting the Permanent Generation](https://blogs.oracle.com/jonthecollector/presenting-the-permanent-generation) General intro into the subject
- [Javassist - Creating Java classes at runtime for evaluating numerical expressions](http://www.javaranch.com/journal/200711/creating_java_classes_runtime_expression_evaluation.html) Small article how to create Java classes dynamically
- [Tomcat Wiki MemoryLeakProtection](http://wiki.apache.org/tomcat/MemoryLeakProtection)
