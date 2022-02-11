# Maven Resource Filtering
> | maven |

* [Using Maven profiles and resource filtering](http://www.manydesigns.com/en/portofino/documentation/tutorials/using-maven-profiles-and-resource-filtering)
* [How do I add resources to my JAR?](http://maven.apache.org/guides/getting-started/index.html#How_do_I_add_resources_to_my_JAR)

I assume that reader has a basic understanding of Maven resources.  

## Simple resource filtering

Let's generate the project:

```bash
$ mvn archetype:generate -DgroupId=org.halyph -DartifactId=proptest -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
```

```xml
<project xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://maven.apache.org/POM/4.0.0" xsi:schemalocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
    <modelversion>4.0.0</modelversion>
    <groupid>org.halyph</groupid>
    <artifactid>proptest</artifactid>
    <packaging>jar</packaging>
    <version>1.0-SNAPSHOT</version>
    <name>proptest</name>
    <url>http://maven.apache.org</url>
    <dependencies>
        <dependency>
            <groupid>junit</groupid>
            <artifactid>junit</artifactid>
            <version>3.8.1</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
</project>
```

Now, we have an application property file with bunch of properties which must be filtered `\proptest\src\main\resources\application.properties`: 

```
application.username=${jdbc.username}
application.password=${jdbc.password}
application.databaseName=${jdbc.databaseName}
```

We have to add build/resources and properties section into pom.xml: 

```xml
<project xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://maven.apache.org/POM/4.0.0" xsi:schemalocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
    <modelversion>4.0.0</modelversion>
    <groupid>org.halyph</groupid>
    <artifactid>proptest</artifactid>
    <packaging>jar</packaging>
    <version>1.0-SNAPSHOT</version>
    <name>proptest</name>
    <url>http://maven.apache.org</url>
    <dependencies>
        <dependency>
            <groupid>junit</groupid>
            <artifactid>junit</artifactid>
            <version>3.8.1</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
    <build>
        <resources>
            <resource>
                <directory>src/main/resources</directory>
                <filtering>true</filtering>
            </resource>
        </resources>
    </build>
    <properties>
        <jdbc.username="">default_username</jdbc>
        <jdbc.password="">default_password</jdbc>
        <jdbc.databasename="">default_databaseName</jdbc>
    </properties>
</project>
```

Lets run maven resource filtering and check the resulted `\proptest\target/classes/application.properties` file:

```bash
$ mvn process-resources
$ cat target/classes/application.properties

application.username=default_username
application.password=default_password
application.databaseName=default_databaseName
```

As you can see property values were successfully substituted.

## Resource filtering with external properties file

We can extract Maven properties in external property file `\proptest_extfile\src\main\filters\mysql_filters.properties`:

```
jdbc.username=mysql_username
jdbc.password=mysql_password
jdbc.databaseName=mysql_databaseName
```

also, we have to adjust `pom.xml` to work properly with external filters (added build/filters and removed properties):

```xml
<project xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://maven.apache.org/POM/4.0.0" xsi:schemalocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
    <modelversion>4.0.0</modelversion>
    <groupid>org.halyph</groupid>
    <artifactid>proptest</artifactid>
    <packaging>jar</packaging>
    <version>1.0-SNAPSHOT</version>
    <name>proptest</name>
    <url>http://maven.apache.org</url>
    <dependencies>
        <dependency>
            <groupid>junit</groupid>
            <artifactid>junit</artifactid>
            <version>3.8.1</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
    <build>
        <filters>
            <filter>src/main/filters/mysql_filters.properties</filter>
        </filters>
        <resources>
            <resource>
                <directory>src/main/resources</directory>
                <filtering>true</filtering>
            </resource>
        </resources>
    </build>
</project>
```

Let's check the resulted \proptest\target\classes\application.properties file: 

```bash
$ mvn process-resources
$ cat target/classes/application.properties

application.username=mysql_username
application.password=mysql_password
application.databaseName=mysql_databaseName
```

## Mixed resource filtering with external/internal properties

What happen if we have overlapped properties in pom.xml with external property file.  
Modified pom.xml: 

```xml
<project xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://maven.apache.org/POM/4.0.0" xsi:schemalocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
    <modelversion>4.0.0</modelversion>
    <groupid>org.halyph</groupid>
    <artifactid>proptest</artifactid>
    <packaging>jar</packaging>
    <version>1.0-SNAPSHOT</version>
    <name>proptest</name>
    <url>http://maven.apache.org</url>
    <dependencies>
        <dependency>
            <groupid>junit</groupid>
            <artifactid>junit</artifactid>
            <version>3.8.1</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
    <build>
        <filters>
            <filter>src/main/filters/mysql_filters.properties</filter>
        </filters>
        <resources>
            <resource>
                <directory>src/main/resources</directory>
                <filtering>true</filtering>
            </resource>
        </resources>
    </build>
    <properties>
        <jdbc.databasename="">default_databaseName</jdbc>
    </properties>
</project>
```

Now, check the resulted `\proptest\target\classes\application.properties` file:

```bash
$ mvn process-resources
$ cat target/classes/application.properties

application.username=mysql_username
application.password=mysql_password
application.databaseName=default_databaseName
```

In this case Maven uses `application.databaseName` property from `pom.xml`

## Managing properties with [properties-maven-plugin](http://mojo.codehaus.org/properties-maven-plugin/)

Please check the plugin home page for more details [http://mojo.codehaus.org/properties-maven-plugin](http://mojo.codehaus.org/properties-maven-plugin)  
  
This plugin read external property and they behave like were declared in `pom.xml`.  
Modified `pom.xml`:

```xml
<project xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://maven.apache.org/POM/4.0.0" xsi:schemalocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
    <modelversion>4.0.0</modelversion>
    <groupid>org.halyph</groupid>
    <artifactid>proptest</artifactid>
    <packaging>jar</packaging>
    <version>1.0-SNAPSHOT</version>
    <name>proptest</name>
    <url>http://maven.apache.org</url>
    <dependencies>
        <dependency>
            <groupid>junit</groupid>
            <artifactid>junit</artifactid>
            <version>3.8.1</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
    <build>
        <plugins>
            <plugin>
                <groupid>org.codehaus.mojo</groupid>
                <artifactid>properties-maven-plugin</artifactid>
                <version>1.0-alpha-2</version>
                <executions>
                    <execution>
                        <phase>initialize</phase>
                        <goals>
                            <goal>read-project-properties</goal>
                        </goals>
                        <configuration>
                            <files>
                                <file>src/main/filters/cust_mysql_filters.properties</file>
                            </files>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
        <filters>
            <filter>src/main/filters/mysql_filters.properties</filter>
        </filters>
        <resources>
            <resource>
                <directory>src/main/resources</directory>
                <filtering>true</filtering>
            </resource>
        </resources>
    </build>
</project>
```

Also, we have to add new external property file just to verify the property overlapping issue: 
`\proptest_extfile\src\main\filters\cust_mysql_filters.properties`:

```
jdbc.username=cust_mysql_username
jdbc.password=cust_mysql_password
jdbc.databaseName=cust_mysql_databaseName
```

Now, it's time to check the resulted file `\proptest\target\classes\application.properties` file:

```
$ mvn process-resources
$ cat target/classes/application.properties

application.username=cust_mysql_username
application.password=cust_mysql_password
application.databaseName=cust_mysql_databaseName
```

Have you noticed that we've got properties values from `cust_mysql_filters.properties`a nd Maven hasn't applied properties from `mysql_filters.properties` file?

So, as you can see we have several ways for managing/filtering properties with Maven. And, it's very convenient.
