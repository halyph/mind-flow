# How to run Netflix Eureka via Webapp Runner?
> | java |

Some time ago I had to run [Netflix Eureka server](https://github.com/Netflix/eureka) (to be more specific it was version 1.1.151) not using Spring Boot.

There were several ways:

- simply deploy **eureka-server.war** into Tomcat
- use [Jetty runner](http://www.eclipse.org/jetty/documentation/current/runner.html). 
>The idea of the jetty-runner is extremely simple – run a webapp directly from the command line using a single jar and as much default configuration as possible. Of course, if your webapp is not so straightforward, the jetty-runner has command line options which allow you to customize the execution environment.
- use [Webapp Runner](https://github.com/jsimone/webapp-runner). 
>Webapp runner is designed to allow you to launch an exploded or compressed war that is on your filesystem into a tomcat container with a simple java -jar command.

I decided to go with *Webapp Runner*.

So, here is the list of steps:

1. Download **eureka-server** war from maven central (e.g. http://mvnrepository.com/artifact/com.netflix.eureka/eureka-server/1.1.151). Also, we can clone the Netflix Eureka github repo and perform build locally. But, our intent is just get ready to use war file as quick as possible.
2. Rename **eureka-server-1.1.151.war** to **eureka-server.war**. 
3. Download **webapp-runnner** jar from maven central (e.g. http://mvnrepository.com/artifact/com.github.jsimone/webapp-runner/8.0.24.0)
4. I assume that **eureka-server.war** and **webapp-runner-8.0.24.0.jar** are located in the same directory. Now we can simply run the *eureka-server* on port 4000 via `runme.bat` file:

```
$ cat runme.bat
java -jar webapp-runner-8.0.24.0.jar eureka.war --path /eureka --port 4000
```

Local directory should have the next files/folders:

```
$ dir /b
eureka-server-1.1.151.war
eureka.war
runme.bat
target/
webapp-runner-8.0.24.0.jar
```

The server is up and running: check Eureka UI http://localhost:4000/eureka/ or registered apps http://localhost:4000/eureka/v2/apps/ XML output.

## References

- Github [Webapp Runner](https://github.com/jsimone/webapp-runner)
- Github [Netflix Eureka](https://github.com/Netflix/eureka)
- [Deploy a Java Web Application that launches with Jetty Runner](https://github.com/heroku/devcenter-jetty-runner)
- [Deploying Tomcat-based Java Web Applications with Webapp Runner](https://devcenter.heroku.com/articles/java-webapp-runner)
- [Standing up a local Netflix Eureka](http://www.java-allandsundry.com/2015/02/standing-up-local-netflix-eureka.html)