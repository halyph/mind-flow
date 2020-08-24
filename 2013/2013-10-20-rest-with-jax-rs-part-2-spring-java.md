# REST with JAX-RS: Part 2 - Spring Java Config and CXF Improvement
> | java | rest | spring | jax-rs |
  
See previous post:  

* [REST with JAX-RS: Part 1 - Spring Java Config](2013-10-19-rest-with-jax-rs-part-1-spring-java.md)

Sample application from part 1 has several issues:

1. It doesn't have application wide REST exception handler. This handler should catch and wrap all internal exceptions and present in some "standard" JSON format
2. There are no autowiring for REST Resources and JAX-RS providers. I.e. we shouldn't declare REST service beans/providers manually in AppConfig (see [part1](2013-10-19-rest-with-jax-rs-part-1-spring-java.md))
3. CXF object mapper (Jackson) should be configured and registered in CXF somehow

Let's try to fix all these issues.
  
JAX-RS has special approach for exception handling - [ExceptionMapper](http://cxf.apache.org/docs/jax-rs-basics.html#JAX-RSBasics-Exceptionhandling).  
Let's define two mappers:  

* **GeneralExceptionMapper** - will catch and handle all **Exceptions**
* **NotFoundExceptionMapper** - will catch and handle only **NotFoundException**

```java
package com.halyph.rest.provider;  
  
import javax.ws.rs.NotFoundException;  
import javax.ws.rs.Produces;  
import javax.ws.rs.core.MediaType;  
import javax.ws.rs.core.Response;  
import javax.ws.rs.ext.ExceptionMapper;  
import javax.ws.rs.ext.Provider;  
import java.util.Date;  
import java.util.HashMap;  
import java.util.Map;  
  
@Provider  
@Produces(MediaType.APPLICATION\_JSON)  
public class NotFoundExceptionMapper implements ExceptionMapper<NotFoundException> {  
    /**  
     * Map an exception to a {@link javax.ws.rs.core.Response}.  
     *  
     * @param exception the exception to map to a response.  
     * @return a response mapped from the supplied exception.  
     */  
    @Override  
    public Response toResponse(final NotFoundException exception) {  
        Map<String, Object> info = new HashMap<>();  
        info.put("msg", exception.getMessage());  
        info.put("date", new Date());  
        info.put("details", "The requested resource hasn't been found");  
  
        return Response  
                .status(Response.Status.INTERNAL\_SERVER\_ERROR)  
                .entity(info)  
                .type(MediaType.APPLICATION\_JSON)  
                .build();  
    }  
}  
```

```java
package com.halyph.rest.provider;  
  
import javax.ws.rs.Produces;  
import javax.ws.rs.core.MediaType;  
import javax.ws.rs.core.Response;  
import javax.ws.rs.ext.ExceptionMapper;  
import javax.ws.rs.ext.Provider;  
import java.util.Date;  
import java.util.HashMap;  
import java.util.Map;  
  
@Provider  
@Produces(MediaType.APPLICATION\_JSON)  
public class GeneralExceptionMapper implements ExceptionMapper<exception> {  
    /**  
     * Map an exception to a {@link javax.ws.rs.core.Response}.  
     *  
     * @param exception the exception to map to a response.  
     * @return a response mapped from the supplied exception.  
     */  
    @Override  
    public Response toResponse(final Exception exception) {  
        Map<String, Object> info = new HashMap<>();  
        info.put("msg", exception.getMessage());  
        info.put("date", new Date());  
  
        return Response  
                .status(Response.Status.INTERNAL\_SERVER\_ERROR)  
                .entity(info)  
                .type(MediaType.APPLICATION\_JSON)  
                .build();  
    }  
}  
```
  
And, modify **UserResource** which throws **NotFoundException** when some user can't be found by specified id  

```java
@RestService  
@Path("/users")  
@Produces({MediaType.APPLICATION\_JSON})  
@Consumes({MediaType.APPLICATION\_JSON})  
public class UserResource {  
  
 ...  
    @GET  
    @Path("/{id}")  
    public User getUser(@PathParam("id") Integer id) {  
        User user = service.getUser(id);  
        if (user == null) {  
            throw new NotFoundException();  
        } else {  
            return user;  
        }  
    }  
  
    ...  
}  
```
  
Now, we have to implement REST resource/provider autowiring. 1st we create custom `@RestService` annotation.  

```java
package com.halyph.util.annotation;  
  
import java.lang.annotation.Documented;  
import java.lang.annotation.ElementType;  
import java.lang.annotation.Retention;  
import java.lang.annotation.RetentionPolicy;  
import java.lang.annotation.Target;  
  
@Retention(RetentionPolicy.RUNTIME)  
@Target(ElementType.TYPE)  
@Documented  
public @interface RestService {  
}  
```
  
Now we have to implement Spring bean scanners which scan specified package and register "selected" beans in Spring context.  
   
```java
package com.halyph.util;  
  
import org.springframework.context.ApplicationContext;  
import org.springframework.context.annotation.ClassPathBeanDefinitionScanner;  
import org.springframework.context.support.GenericApplicationContext;  
import org.springframework.core.type.filter.AnnotationTypeFilter;  
  
import javax.ws.rs.ext.Provider;  
import java.util.ArrayList;  
import java.util.List;  
  
public final class RestProviderBeanScanner {  
  
    private RestProviderBeanScanner() { }  
    public static List<Object> scan(ApplicationContext applicationContext, String... basePackages) {  
        GenericApplicationContext genericAppContext = new GenericApplicationContext();  
        ClassPathBeanDefinitionScanner scanner = new ClassPathBeanDefinitionScanner(genericAppContext, false);  
  
        scanner.addIncludeFilter(new AnnotationTypeFilter(Provider.class));  
        scanner.scan(basePackages);  
        genericAppContext.setParent(applicationContext);  
        genericAppContext.refresh();  
  
        return new ArrayList<>(genericAppContext.getBeansWithAnnotation(Provider.class).values());  
    }  
}  
```

```java
package com.halyph.util;  
  
import com.halyph.util.annotation.RestService;  
import org.springframework.context.ApplicationContext;  
import org.springframework.context.annotation.ClassPathBeanDefinitionScanner;  
import org.springframework.context.support.GenericApplicationContext;  
import org.springframework.core.type.filter.AnnotationTypeFilter;  
  
import java.util.ArrayList;  
import java.util.List;  
  
public final class RestServiceBeanScanner {  
  
    private RestServiceBeanScanner() { }  
  
    public static List<Object> scan(ApplicationContext applicationContext, String... basePackages) {  
        GenericApplicationContext genericAppContext = new GenericApplicationContext();  
        ClassPathBeanDefinitionScanner scanner = new ClassPathBeanDefinitionScanner(genericAppContext, false);  
  
        scanner.addIncludeFilter(new AnnotationTypeFilter(RestService.class));  
        scanner.scan(basePackages);  
        genericAppContext.setParent(applicationContext);  
        genericAppContext.refresh();  
  
        List<Object> restResources = new ArrayList<>(genericAppContext.getBeansWithAnnotation(RestService.class).values());  
  
        return restResources;  
    }  
}
```

These two classes (scanner) **RestServiceBeanScanner** and **RestProviderBeanScanner** are almost identical and should be refactored to support generic scanner type. Let's left this for home work.  
  
There is additional issue with missed Object Mapper configuration:  

```java
package com.halyph.rest.provider;  
  
import com.fasterxml.jackson.databind.ObjectMapper;  
import com.fasterxml.jackson.databind.SerializationFeature;  
  
import javax.ws.rs.ext.ContextResolver;  
import javax.ws.rs.ext.Provider;  
import java.text.DateFormat;  
import java.text.SimpleDateFormat;  
import java.util.TimeZone;  
  
@Provider  
public class ObjectMapperProvider implements ContextResolver<Objectmapper> {  
  
    final ObjectMapper objectMapper;  
  
    public ObjectMapperProvider() {  
        this.objectMapper = new ObjectMapper();  
        this.objectMapper.configure(SerializationFeature.INDENT\_OUTPUT, true);  
  
        //set up ISO 8601 date/time stamp format:  
        final DateFormat df = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:sss'Z'");  
        df.setTimeZone(TimeZone.getTimeZone("UTC"));  
        this.objectMapper.setDateFormat(df);  
    }  
  
    @Override  
    public ObjectMapper getContext(Class type) {  
        return this.objectMapper;  
    }  
}
```
  
We have to update AppConfig:  

* Add **@ComponentScan** to register services
* Call **RestProviderBeanScanner** to register providers: json provider, _ExceptionMapper_ and  ObjectMapperProvider
* Call **RestServiceBeanScanner** to register REST services marked with **@RestService** annotation

```java 
package com.halyph.config;  
  
import com.fasterxml.jackson.jaxrs.json.JacksonJsonProvider;  
import com.halyph.util.RestProviderBeanScanner;  
import com.halyph.util.RestServiceBeanScanner;  
import org.apache.cxf.bus.spring.SpringBus;  
import org.apache.cxf.endpoint.Server;  
import org.apache.cxf.jaxrs.JAXRSServerFactoryBean;  
import org.springframework.context.ApplicationContext;  
import org.springframework.context.annotation.Bean;  
import org.springframework.context.annotation.ComponentScan;  
import org.springframework.context.annotation.Configuration;  
import org.springframework.context.annotation.DependsOn;  
  
import javax.ws.rs.ApplicationPath;  
import javax.ws.rs.core.Application;  
import javax.ws.rs.ext.RuntimeDelegate;  
import java.util.List;  
  
@Configuration  
@ComponentScan(AppConfig.SERVICE\_PACKAGE)  
public class AppConfig {  
  
    public static final String BASE\_PACKAGE = "com.halyph";  
    public static final String SERVICE\_PACKAGE = BASE\_PACKAGE + ".service";  
    private static final String RESOURCES\_PACKAGE = BASE\_PACKAGE + ".rest";  
    private static final String PROVIDER\_PACKAGE = BASE\_PACKAGE + ".rest.provider";  
  
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
        factory.setServiceBeans(restServiceList(appContext));  
        factory.setAddress("/" + factory.getAddress());  
        factory.setProviders(restProviderList(appContext, jsonProvider()));  
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
  
    private List<Object> restServiceList(ApplicationContext appContext) {  
        return RestServiceBeanScanner.scan(appContext, AppConfig.RESOURCES\_PACKAGE);  
    }  
  
    private List<Object> restProviderList(final ApplicationContext appContext,  
                                          final JacksonJsonProvider jsonProvider) {  
        final List<Object> providers = RestProviderBeanScanner.scan(appContext, PROVIDER\_PACKAGE);  
        providers.add(jsonProvider);  
        return providers;  
    }  
  
}  
```
  
Now, we should test this. 1st run application:  

```bash
mvn clean tomcat7:run
```
  
Verify REST API calls:  

```bash
# pretty printed JSON, see ObjectMapperProvider 
$  curl http://localhost:8080/api/users
[ {
  "id" : 1,
  "name" : "foo"
}, {
  "id" : 2,
  "name" : "bar"
}, {
  "id" : 3,
  "name" : "baz"
} ]

# try to get non-existent user, expected to get NotFoundException JSON
$ curl http://localhost:8080/api/users/100
{
  "details" : "The requested resource hasn't been found",
  "date" : "2013-10-19T13:39:034Z",
  "msg" : null
}

# try to get GeneralException JSON
$  curl http://localhost:8080/api/exception
{
  "date" : "2013-10-19T13:40:049Z",
  "msg" : "generateException from ExceptionResource"
} 
```

You can find sources on [GitHub](https://github.com/halyph/jaxrs-tutorials/tree/part/02-spring-java-config-improved)  
  
## References

1. [Apache CXF exception handler for jaxrs (REST)](http://www.luckyryan.com/2013/06/15/apache-cxf-exception-handler-for-jaxrs-rest/)
2. [Official documentation: Apache CXF Exception handling](http://cxf.apache.org/docs/jax-rs-basics.html#JAX-RSBasics-Exceptionhandling)