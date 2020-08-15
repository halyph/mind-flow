# Java Reflection: Invoke Constructor Issue
> | java |

Let's imagine we have the next classes:

```java
package test.clazz;

public class First {
 private FirstArg arg;

 public FirstArg getArg() {
  return arg;
 }

 public First (FirstArg arg) {
  this.arg = arg;
  System.out.println("First() - constructor");
 }
}

public class FirstArg {
 public FirstArg() {
  System.out.println("FirstArg.FirstArg()");
 }
}

public class SecondArg  extends FirstArg{
 public SecondArg() {
  System.out.println("SecondArg.SecondArg()");
 }
}
```

And we can easily instantiate `First` class with `FirstArg` or `SecondArg`:

```
First f1Old = new First(new FirstArg());
First f2Old = new First(new SecondArg());
System.out.println(f1Old.getArg().getClass());
System.out.println(f2Old.getArg().getClass());
```

We'll get the next output: 

```
FirstArg.FirstArg()
First() - constructor
FirstArg.FirstArg()
SecondArg.SecondArg()
First() - constructor
class test.clazz.FirstArg
class test.clazz.SecondArg
```

Now, we have to instantiate `First` class with `FirstArg` or `SecondArg`, but via Java reflection:

```java
public final class ConstructionUtil {
 public static Object instantiateClassOld(String className, Object iView) {
  try {
   Class iViewClass = iView.getClass();
   Class clazz = Class.forName(className);

   Constructor ctor = clazz.getDeclaredConstructor(iViewClass);
   ctor.setAccessible(true);
   return ctor.newInstance(iView);
  } catch (Exception e) {
   e.printStackTrace();
   return null;
  }
 }
} 
```

Check reflection based class instantiation:

```java
Object cls = instantiateClassOld("test.clazz.First", new FirstArg());
First f1 = (First) cls;
Object cls2 = instantiateClassOld("test.clazz.First", new SecondArg());
First f2 = (First) cls2;
System.out.println(f1.getArg().getClass());
System.out.println(f2.getArg().getClass());
```

And we'll get Exception: 

```
FirstArg.FirstArg()
First() - constructor
FirstArg.FirstArg()
SecondArg.SecondArg()
java.lang.NoSuchMethodException: test.clazz.First.(test.clazz.SecondArg)
 at java.lang.Class.getConstructor0(Unknown Source)
 at java.lang.Class.getDeclaredConstructor(Unknown Source)
 at test.ConstructionUtil.instantiateClassOld(ConstructionUtil.java:63)
 at test.ConstructionUtil.main(ConstructionUtil.java:22)
 ```

Reflection mechanism can't find `First(SecondArg arg)` constructor.
We have to patch `instantiateClassOld` method like this:

```java
public final class ConstructionUtil {
 public static Object instantiateClassNew(String className, Object iView) {
  try {
   Class iViewClass = iView.getClass();
   Class clazz = Class.forName(className);
   try {
    Constructor ctor = clazz.getDeclaredConstructor(iViewClass);
    ctor.setAccessible(true);
    return ctor.newInstance(iView);

   } catch (NoSuchMethodException e) {
    Constructor[] constructors = clazz.getDeclaredConstructors();
    for (Constructor c : constructors) {
     if (c.getParameterTypes().length > 1)
      continue;
     Class type = c.getParameterTypes()[0];
     if (type.isAssignableFrom(iView.getClass())) {
      return c.newInstance(type.cast(iView));
     }

    }
   }
   return null;

  } catch (Exception e) {
   e.printStackTrace();
   return null;
  }
 }
} 
```

And run it again:

```java
Object cls = instantiateClassNew("test.clazz.First",new FirstArg());
First f1 = (First) cls;
Object cls2 = instantiateClassNew("test.clazz.First",new SecondArg());
First f2 = (First) cls2;
System.out.println(f1.getArg().getClass());
System.out.println(f2.getArg().getClass());
```

Output:

```
FirstArg.FirstArg()
First() - constructor
FirstArg.FirstArg()
SecondArg.SecondArg()
First() - constructor
class test.clazz.FirstArg
class test.clazz.SecondArg
```

We should be careful when invoke methods via reflection with polymorphic arguments.
