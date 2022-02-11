# How to disable System.out?
> | java |

I have a legacy code base with tons of `System.out.println()`. Actually, I don't need this in production, but during development it's cool enough to have. So, I've decided to disable `System.out`:  

```java
package org.halyph;  
  
import java.io.OutputStream;  
import java.io.PrintStream;  
  
public class DisableMain {  
	public static void main(String\[\] args) {  
		PrintStream printStreamOriginal = System.out;  
  
		boolean DEBUG = true;  
		if (!DEBUG) {  
			System.setOut(new PrintStream(new OutputStream() {  
				public void close() {}  
				public void flush() {}  
				public void write(byte[] b) {}  
				public void write(byte[] b, int off, int len) {}  
				public void write(int b) {  
				}  
			}));  
		}  
  
		long a = System.currentTimeMillis();  
		for (int i = 0; i < 1000000; i++) {  
			System.out.println("Hello");  
		}  
  
		long b = System.currentTimeMillis() - a;  
  
		System.setOut(printStreamOriginal);  
		System.out.println(b);  
	}  
}
```

So, plain looped **println** required ~10 seconds on my laptop, and only ~1 second with null output stream.
