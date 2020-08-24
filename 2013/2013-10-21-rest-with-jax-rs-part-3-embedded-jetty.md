# REST with JAX-RS: Part 3 - Embedded Jetty
> | java | rest | spring | jax-rs |

See previous posts:  

* [REST with JAX-RS: Part 1 - Spring Java Config](2013-10-19-rest-with-jax-rs-part-1-spring-java.md)
* [REST with JAX-RS: Part 2 - Spring Java Config and CXF Improvement](2013-10-20-rest-with-jax-rs-part-2-spring-java.md)

There is one feature which I'd like to add. It's embedded Jetty server. I.e. we should be able to run our application from `main()` method.  
  
Update `pom.xml`, add jetty server as dependency  

```xml
...  
 <org.eclipse.jetty.version>9.0.6.v20130930</org.eclipse.jetty.version>  
...  
    <dependency>
        <groupId>org.eclipse.jetty</groupId>
        <artifactId>jetty-webapp</artifactId>
        <version>${org.eclipse.jetty.version}</version>
    </dependency>
...  
```

Create special **Launcher** class which runs embedded Jetty Server. Jetty configuration registers port, host, base REST URL (**_"/api/\*"_**) and the most important - proper Spring config.  

```java
package com.halyph;  
  
import com.halyph.config.AppConfig;  
import org.apache.cxf.transport.servlet.CXFServlet;  
import org.eclipse.jetty.server.Server;  
import org.eclipse.jetty.servlet.ServletContextHandler;  
import org.eclipse.jetty.servlet.ServletHolder;  
import org.springframework.web.context.ContextLoaderListener;  
import org.springframework.web.context.support.AnnotationConfigWebApplicationContext;  
  
  
public class Launcher {  
  
    public static final int PORT = 8080;  
  
    public static void main(final String\[\] args) throws Exception {  
        Server server = new Server(PORT);  
  
        // Register and map the dispatcher servlet  
        final ServletHolder servletHolder = new ServletHolder(new CXFServlet());  
        final ServletContextHandler context = new ServletContextHandler();  
        context.setContextPath("/");  
        context.addServlet(servletHolder, AppConfig.API\_BASE);  
        context.addEventListener(new ContextLoaderListener());  
  
        context.setInitParameter("contextClass", AnnotationConfigWebApplicationContext.class.getName());  
        context.setInitParameter("contextConfigLocation", AppConfig.class.getName());  
  
        server.setHandler(context);  
        server.start();  
        server.join();  
    }  
}  
```

You can find sources on [GitHub](https://github.com/halyph/jaxrs-tutorials/tree/part/03-embedded-jetty)  
  
## References

1. [Going REST: embedding Jetty with Spring and JAX-RS (Apache CXF)](http://aredko.blogspot.com/2013/01/going-rest-embedding-jetty-with-spring.html)
2. [Embedding Jetty or Tomcat in your Java Application](http://www.hascode.com/2013/07/embedding-jetty-or-tomcat-in-your-java-application/)