# Quick way to join array of String in Java without third party libraries
> | java |

As you probably know Java SE doesn't include such useful method as String join. Even old good JavaScript has this nice method:

>JavaScript `join()` Method  
>Definition and Usage  
>The `join()` method joins all elements of an array into a string, and returns the string. The elements will be separated by a specified separator. The default separator is comma (,).

How to implement the similar stuff in Java SE? The easiest what came to my head is:

```java
 /**
  * Join String arguments into one String separated by comma (",")
  * @param args input Strings
  * @return joined String
  */
 public static String join(String... args) {
  if(args.length <1) throw new IllegalArgumentException();
  
  String joined = Arrays.toString(args);
  String result = joined.substring(1, joined.length()-1);
  return result;
 }
```

Usage is pretty trivial:

```java
import static com.blogspot.HalypHUtils.join;

...

String joinedString = join("Banana", "Orange", "Apple", "Mango");
```
