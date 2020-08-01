# `@Override` Java Annotation Issue
> | java |

Let's create one simple interface and class which implements this interface:

```java
public interface IOverride {
    void doSomething();
}
public class Overridden implements IOverride {
    @Override
    public void doSomething() {
    }
}
```

And compile this stuff on JDK v.1.5:

```bash
# javac -d classes src\*.java
src\Overridden.java:2: method does not override a method from its superclass
        @Override
         ^
1 error
```

Let's try to do the same on **JDK v.1.6** - And, You've got **no** compilation error.

>Between Java 5 and Java 6 changes to the specification of @Override have been made. In Java 6 it is possible to add the @Override annotation to methods that implement methods of an interface which is not allowed in Java 5. (http://dertompson.com/2008/01/25/override-specification-changes-in-java-6/)

Also, I've found very interesting discussion on StackOverflow: http://stackoverflow.com/questions/94361/when-do-you-use-javas-override-annotation-and-why:

Q:
> What are the best practices for using Java's @Override annotation and why?
> It seems like it would be overkill to mark every single overridden method with the @Override annotation. Are there certain programming situations that call for using the @Override and others that should never use the @Override?

A:
> Use it every time you override a method for two benefits. Do it so that you can take advantage of the compiler checking to make sure you actually are overriding a method when you think you are. This way, if you make a common mistake of misspelling a method name or not correctly matching the parameters, you will be warned that you method does not actually override as you think it does. Secondly, it makes your code easier to understand because it is more obvious when methods are overwritten.
>
> Additionally, in Java 1.6 you can use it to mark when a method implements an interface for the same benefits. I think it would be better to have a separate annotation (like @Implements), but it's better than nothing.
