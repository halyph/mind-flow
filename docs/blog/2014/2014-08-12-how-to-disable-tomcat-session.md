# How to disable Tomcat session serialization
> | java |

Suppose you have the next error while restart/stop Tomcat (in my case Tomcat 7.x): 

```java
WARNING: Cannot serialize session attribute SPRING_SECURITY_CONTEXT for session 54DBA076EDC9B7A24C1AF76824DFD1EF
java.io.NotSerializableException: com.MyClass
 at java.io.ObjectOutputStream.writeObject0(ObjectOutputStream.java:1180)
 at java.io.ObjectOutputStream.defaultWriteFields(ObjectOutputStream.java:1528)
 at java.io.ObjectOutputStream.writeSerialData(ObjectOutputStream.java:1493)
 at java.io.ObjectOutputStream.writeOrdinaryObject(ObjectOutputStream.java:1416)
 at java.io.ObjectOutputStream.writeObject0(ObjectOutputStream.java:1174)
 at java.io.ObjectOutputStream.writeObject(ObjectOutputStream.java:346)
 at java.util.ArrayList.writeObject(ArrayList.java:710)
 at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
 at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
 at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
 at java.lang.reflect.Method.invoke(Method.java:601)
 at java.io.ObjectStreamClass.invokeWriteObject(ObjectStreamClass.java:975)
...
```

It means that Tomcat is trying to persist non-serializable objects which were added into the session. Tomcat uses Manager component which is used to create and maintain HTTP sessions for web application.

By default manager implementation configured to perform session persistence across restarts and we want to disable this functionality.

To disable this persistence feature, create a Context configuration file (_context.xml_) for your web application and add the following element there: 

```xml
<Manager pathname="" />
```

You can add this `context.xml` file to:

- App.war:/META-INF/context.xml
- TOMCAT_HOME/conf/Catalina/localhost/App.xml file
- TOMCAT_HOME/cont/context.xml

## References

- [Disable Session Persistence](http://tomcat.apache.org/tomcat-7.0-doc/config/manager.html#Disable_Session_Persistence)
- [Clustering/Session Replication HOW-TO](http://tomcat.apache.org/tomcat-7.0-doc/cluster-howto.html)
