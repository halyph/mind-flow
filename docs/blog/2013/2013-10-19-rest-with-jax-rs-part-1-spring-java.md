# REST with JAX-RS: Part 1 - Spring Java Config
> | java | rest | spring | jax-rs |

There are many Java REST frameworks. We can devide these frameworks on three groups:

1. Spring MVC. It can be used to implement RESTful services. This framework has been widely used, mature, etc. But, Spring, in general, does not support JAX-RS standard.
2. JAX-RS implementation. I know at least four frameworks:
   * [Apache CXF](http://cxf.apache.org/ "Apache CXF") 
   * [Jersey](http://jersey.java.net/), the [reference implementation](http://en.wikipedia.org/wiki/Reference_implementation "Reference implementation") from [Oracle](http://en.wikipedia.org/wiki/Oracle_Corporation "Oracle Corporation")
   * [RESTeasy](http://www.jboss.org/resteasy), [JBoss](http://en.wikipedia.org/wiki/JBoss "JBoss")'s implementation
   * [Restlet](http://restlet.org/ "Restlet")
3. Non-Standard. I.e. frameworks which do not support JAX-RS, or addition many other features. Please note, it assume that Spring MVC can be called "standard" ;-)
   * [Dropwizard](http://dropwizard.codahale.com/) very cool frameworks. It supports not only JAX-RS. 
   * [RESTX](http://restx.io/), lightweight framework.

It's logically to ask yourself why don't use Spring MVC for REST services development. There is a  very good article on InfoQ: [A Comparison of Spring MVC and JAX-RS](http://www.infoq.com/articles/springmvc_jsx-rs). I consider to use JAX-RS frameworks for REST API and Spring MVC for everything else . The most popular are [Apache CXF](http://cxf.apache.org/ "Apache CXF")  and [Jersey](http://jersey.java.net/). Also, [Apache CXF](http://cxf.apache.org/ "Apache CXF") has SOAP services support. Actually, you can easily switch between JAX-RS frameworks till you use standard approaches.  
  
Let's create simple Spring JAX-RS application with Spring Java Configs (see sample application based on Spring context xml \[3\])  
  
Create `pom.xml` file  

```xml
<project xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://maven.apache.org/POM/4.0.0" xsi:schemalocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4\_0\_0.xsd">
    <modelversion>4.0.0</modelversion>
    <groupid>jaxrs-tutorials</groupid>
    <artifactid>jaxrs-tutorials</artifactid>
    <packaging>war</packaging>
    <version>1.0-SNAPSHOT</version>
    <name>jaxrs-tutorials Maven Webapp</name>
    <url>http://maven.apache.org</url>
 
    <properties>
        <project .build.sourceencoding="">UTF-8</project>
        <java-version>1.7</java-version>
 
        <cxf .version="">2.7.6</cxf>
        <org .springframework-version="">3.2.3.RELEASE</org>
        <org .slf4j-version="">1.7.5</org>
        <ch .qos.logback-version="">1.0.13</ch>
        <servlet-version>3.0.1</servlet-version>
        <jackson-version>2.0.2</jackson-version>
 
        <maven-compiler-plugin-version>3.0</maven-compiler-plugin-version>
        <tomcat7-maven-plugin-version>2.0</tomcat7-maven-plugin-version>
        <maven-war-plugin-version>2.2</maven-war-plugin-version>
        <maven-resources-plugin-version>2.6</maven-resources-plugin-version>
    </properties>
 
    <dependencies>
 
        <dependency>
            <groupid>org.apache.cxf</groupid>
            <artifactid>cxf-rt-frontend-jaxrs</artifactid>
            <version>${cxf.version}</version>
        </dependency>
 
        <!-- Spring -->
        <dependency>
            <groupid>org.springframework</groupid>
            <artifactid>spring-context</artifactid>
            <version>${org.springframework-version}</version>
            <exclusions>
                <!-- Exclude Commons Logging in favor of SLF4j -->
                <exclusion>
                    <groupid>commons-logging</groupid>
                    <artifactid>commons-logging</artifactid>
                </exclusion>
            </exclusions>
        </dependency>
        <dependency>
            <groupid>org.springframework</groupid>
            <artifactid>spring-webmvc</artifactid>
            <version>${org.springframework-version}</version>
        </dependency>
 
        <!-- Logging -->
        <dependency>
            <groupid>org.slf4j</groupid>
            <artifactid>slf4j-api</artifactid>
            <version>${org.slf4j-version}</version>
        </dependency>
        <dependency>
            <groupid>org.slf4j</groupid>
            <artifactid>jcl-over-slf4j</artifactid>
            <version>${org.slf4j-version}</version>
            <scope>runtime</scope>
        </dependency>
        <dependency>
            <groupid>ch.qos.logback</groupid>
            <artifactid>logback-classic</artifactid>
            <version>${ch.qos.logback-version}</version>
        </dependency>
 
        <!-- Servlet -->
        <dependency>
            <groupid>javax.servlet</groupid>
            <artifactid>javax.servlet-api</artifactid>
            <version>${servlet-version}</version>
            <scope>provided</scope>
        </dependency>
 
        <!-- JSON Provider -->
        <dependency>
            <groupid>com.fasterxml.jackson.jaxrs</groupid>
            <artifactid>jackson-jaxrs-json-provider</artifactid>
            <version>${jackson-version}</version>
        </dependency>
 
    </dependencies>
 
    <build>
 
        <finalname>jaxrs-tutorials</finalname>
 
        <plugins>
            <plugin>
                <groupid>org.apache.tomcat.maven</groupid>
                <artifactid>tomcat7-maven-plugin</artifactid>
                <version>2.0</version>
                <configuration>
                    <path>/</path>
                    <port>8080</port>
                </configuration>
            </plugin>
            <plugin>
                <groupid>org.apache.maven.plugins</groupid>
                <artifactid>maven-compiler-plugin</artifactid>
                <version>${maven-compiler-plugin-version}</version>
                <configuration>
                    <source>${java-version}
                    <target>${java-version}</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

Create some sample entity  

```java
package com.halyph.entity;  
  
public class User {  
  
    private Integer id;  
    private String name;  
  
    public User() {  
    }  
  
    public User(Integer id, String name) {  
        this.id = id;  
        this.name = name;  
    }  
  
    public Integer getId() {  
        return id;  
    }  
  
    public void setId(Integer id) {  
        this.id = id;  
    }  
  
    public void setName(String name) {  
        this.name = name;  
    }  
  
    public String getName() {  
        return name;  
    }  
  
    @Override  
    public String toString() {  
        return String.format("{id=%s,name=%s}", id, name);  
    }  
}  
```

We should implement Service(s) which manages this entity:  

```java
package com.halyph.service;  
  
import com.halyph.entity.User;  
  
import javax.ws.rs.core.Response;  
import java.util.Collection;  
  
public interface UserService {  
  
    Collection<User> getUsers();  
  
    User getUser(Integer id);  
  
    Response add(User user);  
  
}  
```

```java
package com.halyph.service;  
  
import com.halyph.entity.User;  
import org.springframework.stereotype.Service;  
  
import javax.ws.rs.core.Response;  
import java.util.Collection;  
import java.util.HashMap;  
import java.util.Map;  
  
@Service("userService")  
public class UserServiceImpl implements UserService {  
  
     private static Map<Integer, User> users = new HashMap<Integer, User>();  
  
    static {  
        users.put(1, new User(1, "foo"));  
        users.put(2, new User(2, "bar"));  
        users.put(3, new User(3, "baz"));  
    }  
  
    public UserServiceImpl() {  
    }  
  
    @Override  
    public Collection<User> getUsers() {  
        return users.values();  
    }  
  
    @Override  
    public User getUser(Integer id) {  
        return users.get(id);  
    }  
  
    @Override  
    public Response add(User user) {  
        user.setId(users.size()+1);  
        users.put(user.getId(), user);  
  
        //do more stuff to add user to the system..  
        return Response.status(Response.Status.OK).build();  
    }  
  
}  
```

It's time to introduce REST services. with the next endpoints **/api/users** and **/api/exception**. So, we  have bunch of REST URIs:  

* **GET /api/users** - get all users
* **GET /api/users/{id}** - get user with id
* **POST /api/users** - accept "user" json and create the specified user on back-end
* **GET /api/exception** - throw exception

```java
package com.halyph.rest;  
  
import com.halyph.entity.User;  
import com.halyph.service.UserService;  
import org.slf4j.Logger;  
import org.slf4j.LoggerFactory;  
import org.springframework.beans.factory.annotation.Autowired;  
  
import javax.ws.rs.Consumes;  
import javax.ws.rs.GET;  
import javax.ws.rs.POST;  
import javax.ws.rs.Path;  
import javax.ws.rs.PathParam;  
import javax.ws.rs.Produces;  
import javax.ws.rs.core.MediaType;  
import javax.ws.rs.core.Response;  
import java.util.Collection;  
  
@Path("/users")  
@Produces({MediaType.APPLICATION\_JSON})  
@Consumes({MediaType.APPLICATION\_JSON})  
public class UserResource {  
  
    private static Logger log = LoggerFactory.getLogger(UserResource.class);  
  
    @Autowired  
    UserService service;  
  
    public UserResource() {  
    }  
  
    @GET  
    public Collection<User> getUsers() {  
        return service.getUsers();  
    }  
  
    @GET  
    @Path("/{id}")  
    public User getUser(@PathParam("id") Integer id) {  
        return service.getUser(id);  
    }  
  
    @POST  
    public Response add(User user) {  
        log.info("Adding user {}", user.getName());  
        service.add(user);  
        return Response.status(Response.Status.OK).build();  
    }  
}  
```

Also we added **/api/exception** REST url to demonstrate how CXF deals with exceptions:  

```java
package com.halyph.rest;  
  
import javax.ws.rs.GET;  
import javax.ws.rs.Path;  
import javax.ws.rs.Produces;  
import javax.ws.rs.core.MediaType;  
  
@Path("/exception")  
public class ExceptionResource {  
  
    public ExceptionResource() { }  
  
    @GET  
    @Produces(MediaType.TEXT\_PLAIN)  
    public String generateException() throws Exception {  
        throw new Exception("generateException from ExceptionResource");  
    }  
}  
```

So, what's left? In general we are creating some `web.xml` where we configure Apache CXF, etc. But, we will use Spring feature and implement all our configuration in Spring Java Configs.  
Our web.xml will be empty, some App Servers still require it:  

Next, we should create some class which does the same work which had been done by `web.xml`:  

```java
package com.halyph.config;  
  
import org.apache.cxf.transport.servlet.CXFServlet;  
import org.springframework.web.WebApplicationInitializer;  
import org.springframework.web.context.ContextLoaderListener;  
import org.springframework.web.context.WebApplicationContext;  
import org.springframework.web.context.support.AnnotationConfigWebApplicationContext;  
  
import javax.servlet.ServletContext;  
import javax.servlet.ServletException;  
import javax.servlet.ServletRegistration;  
import java.util.Set;  
  
public class WebAppInitializer implements WebApplicationInitializer {  
  
    @Override  
    public void onStartup(ServletContext servletContext) throws ServletException {  
        servletContext.addListener(new ContextLoaderListener(createWebAppContext()));  
        addApacheCxfServlet(servletContext);  
    }  
  
    private void addApacheCxfServlet(ServletContext servletContext) {  
        CXFServlet cxfServlet = new CXFServlet();  
  
        ServletRegistration.Dynamic appServlet = servletContext.addServlet("CXFServlet", cxfServlet);  
        appServlet.setLoadOnStartup(1);  
  
        Set<String> mappingConflicts = appServlet.addMapping("/api/\*");  
    }  
  
    private WebApplicationContext createWebAppContext() {  
        AnnotationConfigWebApplicationContext appContext = new AnnotationConfigWebApplicationContext();  
        appContext.register(AppConfig.class);  
        return appContext;  
    }  
  
}  
```

So, `web.xml` is configured, now we should configure Spring context:  

```java
package com.halyph.config;  
  
import com.fasterxml.jackson.jaxrs.json.JacksonJsonProvider;  
import com.halyph.rest.UserResource;  
import org.apache.cxf.bus.spring.SpringBus;  
import org.apache.cxf.endpoint.Server;  
import org.apache.cxf.jaxrs.JAXRSServerFactoryBean;  
import com.halyph.rest.ExceptionResource;  
import com.halyph.service.UserService;  
import com.halyph.service.UserServiceImpl;  
import org.springframework.context.ApplicationContext;  
import org.springframework.context.annotation.Bean;  
import org.springframework.context.annotation.Configuration;  
import org.springframework.context.annotation.DependsOn;  
  
import javax.ws.rs.ApplicationPath;  
import javax.ws.rs.core.Application;  
import javax.ws.rs.ext.RuntimeDelegate;  
import java.util.Arrays;  
  
@Configuration  
public class AppConfig {  
  
    @ApplicationPath("/")  
    public class JaxRsApiApplication extends Application { }  
  
    @Bean(destroyMethod = "shutdown")  
    public SpringBus cxf() {  
        return new SpringBus();  
    }  
  
    @Bean  
    @DependsOn("cxf")  
    public Server jaxRsServer(ApplicationContext appContext) {  
        JAXRSServerFactoryBean factory = RuntimeDelegate.getInstance().createEndpoint(jaxRsApiApplication(), JAXRSServerFactoryBean.class);  
        factory.setServiceBeans(Arrays.<Object>asList(userResource(), exceptionResource()));  
        factory.setAddress("/" + factory.getAddress());  
        factory.setProvider(jsonProvider());  
        return factory.create();  
    }  
  
    @Bean  
    public JaxRsApiApplication jaxRsApiApplication() {  
        return new JaxRsApiApplication();  
    }  
  
    @Bean  
    public JacksonJsonProvider jsonProvider() {  
        return new JacksonJsonProvider();  
    }  
  
    @Bean  
    public UserService userService() {  
        return new UserServiceImpl();  
    }  
  
    @Bean  
    public UserResource userResource() {  
        return new UserResource();  
    }  
  
    @Bean  
    public ExceptionResource exceptionResource() {  
        return new ExceptionResource();  
    }  
}  
```

Please note, how service and rest beans have been registered, also we added jackson provider which serialize bean in JSON format.  
  
We almost done, now we should verify out work. Run application:  

```bash
mvn clean tomcat7:run
```
  
Test REST API:  

```bash
curl http://localhost:8080/api/users  
curl http://localhost:8080/api/users/1  
curl -v http://localhost:8080/api/exception  
curl http://localhost:8080/api/users -X POST -H "Content-Type: application/json" -d '{"name":"John"}'  
curl http://localhost:8080/api/users  
```

After the last call you should get four users from back-end.

```bash
$ curl http://localhost:8080/api/users
[{"id":1,"name":"foo"},{"id":2,"name":"bar"},{"id":3,"name":"baz"}]

$ curl http://localhost:8080/api/users -X POST -H "Content-Type: application/json" -d '{"name":"John"}'

$  curl http://localhost:8080/api/users
[{"id":1,"name":"foo"},{"id":2,"name":"bar"},{"id":3,"name":"baz"},{"id":4,"name":"John"}]
```

You can find sources on [GitHub](http://github.com/halyph/jaxrs-tutorials/tree/part/01-spring-java-config).  
  
## References

1. [InfoQ: A Comparison of Spring MVC and JAX-RS](http://www.infoq.com/articles/springmvc_jsx-rs)
2. [REST client, CXF server : JAX-RS or SPRING-MVC ?](http://deepintojee.wordpress.com/2010/12/07/rest-client-cxf-server-jax-rs-or-spring-mvc/)
3. [REST web services with JAX-RS, Apache CXF and Spring Security](http://www.buildfortheweb.com/2013/03/04/restful-web-services-with-jax-rs-apache-cxf-and-spring-security/)
4. [Official Apache CXF Doc: Configuring JAX-RS services in container with Spring configuration file](http://cxf.apache.org/docs/jaxrs-services-configuration.html#JAXRSServicesConfiguration-ConfiguringJAXRSservicesincontainerwithSpringconfigurationfile.).
5. [Converting Jersey REST Examples to Apache CXF](http://www.jroller.com/gmazza/entry/jersey_samples_on_cxf)
