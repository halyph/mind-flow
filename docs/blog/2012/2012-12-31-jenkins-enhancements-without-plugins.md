# Jenkins enhancements without plugins
> | jenkins | ci |

[Jenkins](http://jenkins-ci.org/) is a popular open source continuous integration server. I use it heavily. Jenkins is super extensible CI server with huge plugins repository.  
But I must admit that there are a lot of cases when all these Jenkins plugin's "zoo" doesn't help. What does it mean?:  

* we need a tons of plugin to solve some non-trivial problem,
* too many plugins dependencies which must be properly managed
* some available plugins partially provide required functionality
* some plugins provide required functionality but contain bugs
* or it might be impossible to find necessary plugin, and task have to be done ASAP

Based on these cases mentioned above we have at least two solutions:  

1.  Implement own plugin which will provide all required functionality. It will take some time and slowdown the overall progress for this particular business task
2.  Use some Jenkins extra facilities which gives us a chance for Jenkins automation without plugin writing

I'm a real fun od 2d solution (at least as a prototyping phase or quick-and-dirty solution right-now-right-away).  
  
So, what's the magic? Jenkins has two nice plugins (of cause there are much more similar plugin, but these two are the best for quick start) which give us a possibility to write Groovy scripts for _**build**_ and _**post-build**_ phases:  

* [Groovy plugin](https://wiki.jenkins-ci.org/display/JENKINS/Groovy+plugin) for Build phase
* [Groovy Postbuild Plugin](https://wiki.jenkins-ci.org/display/JENKINS/Groovy+Postbuild+Plugin) for Post-build phase

**Pros**:  

* Groovy scripts have access to whole Jenkins infrastructure (Jenkins packages) and can invoke functionality of third-party plugins installed in this Jenkins instance
* It's very easy to prototype your ideas and validate automation approaches
* It gives us very quick business results
* Groovy scripts can automate really amazing and non-trivial tasks

**Cons**:

* at the end these Groovy scripts are not easy for automated testing
* version managements for these scripts involve additional work (implement simple import/export tool for job configuration)
* these Groovy scripts can have dependency on some third-party plugins and these dependency must me somehow managed as well
* testing and debugging are really painful activities, because it involve too many interactions with Jenkins UI, etc. (yes, it can be somehow improved via extending both Groovy plugins, but it's extra work)