# How to download jars from Maven Central
> | java | maven |

We know how to download Java libraries with it's dependencies (transitive included) via Maven _pom.xml_, Ant/Ivy _build.xml_ script, Gradle _build.gradle_ script etc. 
But what if we need to download them without these scripts.

There are several ways to do this.
Assume that we'd like to download `spark-core` library (`groupId=com.sparkjava, artifactId=spark-core, version=2.1`) with all dependencies from [Maven Central](http://search.maven.org/#artifactdetails%7Ccom.sparkjava%7Cspark-core%7C2.1%7Cjar) into `lib` folder.

## Use Maven3 dependency plugin

Here is there variants for lib download:

```bash Download library with all dependencies
# Specify repoUrl (it's optional)
mvn dependency:get -DrepoUrl=http://download.java.net/maven/2/ -DgroupId=com.sparkjava -DartifactId=spark-core -Dversion=2.1

# OR use default repoUrl
mvn dependency:get -DgroupId=com.sparkjava -DartifactId=spark-core -Dversion=2.1

# OR use parameter artifact as groupId:artifactId:version
mvn dependency:get -Dartifact=com.sparkjava:spark-core:2.1
```

Now we need to copy just downloaded artifacts in our working directory:

```bash Copy jars from local maven repo
mvn dependency:copy-dependencies -f $HOME/.m2/repository/com/sparkjava/spark-core/2.1/spark-core-2.1.pom -DoutputDirectory=$(pwd)/lib
# the previous command doesn't copy spark-core-x.x.jar, that's why we should copy it manually
cp $HOME/.m2/repository/com/sparkjava/spark-core/2.1/spark-core-2.1.jar $(pwd)/lib
```

## Use standalone Ivy

We can use Ivy as standalone jar to download Maven dependencies without creating Ant build file:

```bash
# 1. Download the latest ivy jar (currently it's v.2.4.0)
curl -L -O http://search.maven.org/remotecontent?filepath=org/apache/ivy/ivy/2.4.0/ivy-2.4.0.jar

# 2. Run ivy.jar to retrieve all dependencies
java -jar ivy-2.4.0.jar -dependency com.sparkjava spark-core 2.1 -retrieve "lib/[artifact]-[revision](-[classifier]).[ext]"
```

As you can see Ivy downloads approach is much simpler. The only cons (or pros, it depends) that **ivy.jar** should be additionally downloaded.

## Calling Ivy from Groovy or Java

Here I've decided to store [Evgeny's Goldin](http://makandracards.com/evgeny-goldin/5817-calling-ivy-from-groovy-or-java) code snippet as a reference for myself. Programmatic artifacts downloads is not a common operation. It's alway nice to know the general concept how it can be done. Especially when Ivy documentation is not very informative.

```java Groovy snippet of calling Ivy
import org.apache.ivy.Ivy
import org.apache.ivy.core.module.descriptor.DefaultDependencyDescriptor
import org.apache.ivy.core.module.descriptor.DefaultModuleDescriptor
import org.apache.ivy.core.module.id.ModuleRevisionId
import org.apache.ivy.core.resolve.ResolveOptions
import org.apache.ivy.core.settings.IvySettings
import org.apache.ivy.plugins.resolver.URLResolver
import org.apache.ivy.core.report.ResolveReport
import org.apache.ivy.plugins.parser.xml.XmlModuleDescriptorWriter


public File resolveArtifact(String groupId, String artifactId, String version) {
        //creates clear ivy settings
        IvySettings ivySettings = new IvySettings();
        //url resolver for configuration of maven repo
        URLResolver resolver = new URLResolver();
        resolver.setM2compatible(true);
        resolver.setName('central');
        //you can specify the url resolution pattern strategy
        resolver.addArtifactPattern(
            'http://repo1.maven.org/maven2/[organisation]/[module]/[revision]/[artifact](-[revision]).[ext]');
        //adding maven repo resolver
        ivySettings.addResolver(resolver);
        //set to the default resolver
        ivySettings.setDefaultResolver(resolver.getName());
        //creates an Ivy instance with settings
        Ivy ivy = Ivy.newInstance(ivySettings);

        File ivyfile = File.createTempFile('ivy', '.xml');
        ivyfile.deleteOnExit();

        String[] dep = [groupId, artifactId, version]

        DefaultModuleDescriptor md =
                DefaultModuleDescriptor.newDefaultInstance(ModuleRevisionId.newInstance(dep[0],
                dep[1] + '-caller', 'working'));

        DefaultDependencyDescriptor dd = new DefaultDependencyDescriptor(md,
                ModuleRevisionId.newInstance(dep[0], dep[1], dep[2]), false, false, true);
        md.addDependency(dd);

        //creates an ivy configuration file
        XmlModuleDescriptorWriter.write(md, ivyfile);

        String[] confs = ['default'];
        ResolveOptions resolveOptions = new ResolveOptions().setConfs(confs);

        //init resolve report
        ResolveReport report = ivy.resolve(ivyfile.toURL(), resolveOptions);

        //so you can get the jar library
        File jarArtifactFile = report.getAllArtifactsReports()[0].getLocalFile();

        return jarArtifactFile;
}

resolveArtifact( 'log4j', 'log4j', '1.2.16' )
```

## References

- [Using Maven to download dependencies to a directory on the command line - Stack Overflow](http://stackoverflow.com/questions/15450383/using-maven-to-download-dependencies-to-a-directory-on-the-command-line/15456621)
- [Simplest Ivy code to programmatically retrieve dependency from Maven Central - Stack Overflow](http://stackoverflow.com/questions/15598612/simplest-ivy-code-to-programmatically-retrieve-dependency-from-maven-central)
- [Calling Ivy from Groovy or Java](http://makandracards.com/evgeny-goldin/5817-calling-ivy-from-groovy-or-java)
