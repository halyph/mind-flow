# Maven Build Number Plugin - Sample Usage
> | maven |

[buildnumber-maven-plugin](http://mojo.codehaus.org/buildnumber-maven-plugin).  
  
This post is based on:  

* [http://mojo.codehaus.org/buildnumber-maven-plugin/usage.html](http://mojo.codehaus.org/buildnumber-maven-plugin/usage.html)
* [http://www.site.lalitbhatt.com/maven-build-number-plugin](http://www.site.lalitbhatt.com/maven-build-number-plugin)
* [http://blog.peterlynch.ca/2009/11/buildnumber-maven-plugin-helpful.html](http://blog.peterlynch.ca/2009/11/buildnumber-maven-plugin-helpful.html)
* [http://apollo.ucalgary.ca/tlcprojectswiki/index.php/Public/Project\_Versioning\_-\_Best\_Practices#Build\_Versioning](http://apollo.ucalgary.ca/tlcprojectswiki/index.php/Public/Project_Versioning_-_Best_Practices#Build_Versioning)

We have some project and need to include into jar manifest file sequential build number which isn't based on VCS (SVN, Git, Mercurial, etc.) revision number. Let's create appropriate pom.xml file and implement small demo to verify the result.  
  
Generate maven project

```bash
$ mvn archetype:generate -DgroupId=org.halyph -DartifactId=buildNoTest\
-DarchetypeArtifactId=maven-archetype-quickstart \
-DinteractiveMode=false
```

Create the `pom.xml`

```xml
<project xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://maven.apache.org/POM/4.0.0" xsi:schemalocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
 <modelversion>4.0.0</modelversion>
 <groupid>org.halyph</groupid>
 <artifactid>buildNoTest</artifactid>
 <packaging>jar</packaging>
 <version>1.0-SNAPSHOT</version>
 <name>buildNoTest</name>
 <url>http://maven.apache.org</url>
 
 <dependencies>
  <dependency>
   <groupid>junit</groupid>
   <artifactid>junit</artifactid>
   <version>3.8.1</version>
   <scope>test</scope>
  </dependency>
 </dependencies>
 
 <properties>
  <project .build.sourceencoding="">UTF-8</project>
 </properties>
 
 <!-- 
 If you have access to scm then you can place actual url's. 
 Otherwise with <revisionOnScmFailure /> you can give some fake URLs as follows. 
 -->
 <scm>
  <connection>scm:svn:http://none</connection>
  <developerconnection>scm:svn:https://none</developerconnection>
  <url>scm:svn:https://none</url>
 </scm>
 
 <build>
  <resources>
   <resource>
    <directory>src/main/resources</directory>
   </resource>
   <resource>
    <directory>src/main/filtered-resources</directory>
    <filtering>true</filtering>
   </resource>
  </resources>
  <plugins>
   <plugin>
    <groupid>org.codehaus.mojo</groupid>
    <artifactid>buildnumber-maven-plugin</artifactid>
    <version>1.1</version>
    <executions>
     <execution>
      <phase>generate-resources</phase>
      <goals>
       <goal>create</goal>
      </goals>
     </execution>
    </executions>
    <configuration>
     <!-- 
      doCheck and doUpdate actually talk to repository if it's true,
      Check would check that there are no local changes. 
      Update would update it 
     -->
     <docheck>false</docheck>
     <doupdate>false</doupdate>
     <!-- 
      This ensures that even if we are not connected to scm than also
      take the version from local .svn file 
     -->
     <revisiononscmfailure>
      
     <!--
      Generate sequence build number based on:
      build number and timestamp      
     -->
     <format>Build: #{0} ({1,date})</format>
     <items>
      <item>buildNumber\d*</item>
      <item>timestamp</item>
     </items>
    </revisiononscmfailure></configuration>
   </plugin>
   <plugin>
    <groupid>org.apache.maven.plugins</groupid>
    <artifactid>maven-jar-plugin</artifactid>
    <version>2.1</version>
    <configuration>
     <archive>
      <!-- will put the entries into META-INF/MANIFEST.MF file -->
      <manifestentries>
       <implementation-version>${project.version}</implementation-version>
       <implementation-build>${buildNumber}</implementation-build>
      </manifestentries>
     </archive>
    </configuration>
   </plugin>
  </plugins>
 </build>
</project>
```

Create demo application to verify the results

```java
package org.halyph;

import java.io.IOException;
import java.util.ResourceBundle;
import java.util.jar.Attributes;
import java.util.jar.Manifest;

public class App
{
    public static void main( String[] args ) throws IOException
    {
        System.out.println("Verify Resource bundle" );
  
 // Check filtered resources based on generated build number
        ResourceBundle bundle = ResourceBundle.getBundle( "build" );
        String msg = bundle.getString( "build.message" );
        System.out.println(msg);

        System.out.println("\nVerify Generated MANIFEST.MF Properties" );

 // Check Manifest file based on generated build number
        Manifest mf = new Manifest();
        mf.read(Thread.currentThread().getContextClassLoader().getResourceAsStream("META-INF/MANIFEST.MF"));

        Attributes atts = mf.getMainAttributes();

        System.out.println("Implementation-Versio: " + atts.getValue("Implementation-Version"));
        System.out.println("Implementation-Build: " + atts.getValue("Implementation-Build"));
    }
}
```

Build application several time and Run

```bash
$ mvn install

$ mvn install

$ mvn install
```

```bash
$ java -cp target\buildNoTest-1.0-SNAPSHOT.jar org.halyph.App
Verify Resource bundle
Build: #3 (Jun 27, 2012)

Verify Generated MANIFEST.MF Properties
Implementation-Versio: 1.0-SNAPSHOT
Implementation-Build: Build: #3 (Jun 27, 2012)
```

## Summary

1. We should inform [buildnumber-maven-plugin](http://mojo.codehaus.org/buildnumber-maven-plugin) that we won't use version control revision as build number via adding fake `<scm>` section into `pom.xml` and `<revisionOnScmFailure />` into buildnumber-maven-plugin `<configuration>`
2. Implemented custom build number format, see `buildnumber-maven-plugin` `<configuration>/<format> and <configuration>/<items>`.
3. Added build number into jar manifest, see maven-jar-plugin pom.xml section
4. Tested if generated build number can be properly added in filtered resources
    1. created `src\main\filtered-resources\build.properties` file  
```build.message=${buildNumber}```
    2. added resource filtering, see section `<resource>` flag `<filtering>true</filtering>`
1. Demo application verifying the filtered resources and build number in jar manifest file

 You can git clone this project [github](https://github.com/halyph/blog-sandbox/tree/master/Maven/blogpost_062712)