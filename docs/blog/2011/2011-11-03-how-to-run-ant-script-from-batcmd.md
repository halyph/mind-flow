# How to run ANT script from .BAT/.CMD?
> | tool | java |

Imagine you need to call ANT script from BAT/CMD file.  
Ant script:  

```xml
<project default="bat-test" name="Blog">
    <target description="check ant run" name="bat-test">
        <echo message="Message from ANT"> </echo>
    </target>
</project>
```

And here is BAT file:  
  
```
@echo off  
echo BAT - Before Ant run  
ant -f build.xml  
echo BAT - After Ant run  
```
  
Unfortunately, when you run this BAT you get the next output:  

```
BAT - Before Ant run  
Buildfile: D:\\Projects\\blog\\build.xml  
  
bat-test:  
     [echo] Message from ANT  
  
BUILD SUCCESSFUL  
Total time: 0 seconds  
```
  
So, where is the `"BAT - After Ant run"` echo message?  
  
The problem is that Ant on Windows executed via `ant.bat` file and based on this we're calling one BAT file from another. We have to use CALL command to solve this issues, here is official note from CALL help:  

>```
> Calls one batch program from another.  
> CALL [drive:][path]filename [batch-parameters]  
> batch-parameters   Specifies any command-line information required by the batch program.
>```

And, here is the update BAT file:  
  
```
@echo off  
echo BAT - Before Ant run  
call ant -f build.xml  
echo BAT - After Ant run
```
