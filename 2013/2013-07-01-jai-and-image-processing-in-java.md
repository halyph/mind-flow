# JAI and Image Processing in Java
> | java |

I have minimal experience with Image Processing and when I'm talking about it I mean:  

* read/write different image formats (jpg, png, tiff, ice, etc.)
* flip, rotate image
* crop and clip image by defined path
* convert image's color (e.g. RGB to gray scale)
* reduce image size
* find edges
* image histograms and color counting
* different operations (e.g. AND, OR and XOR)
* read image meta info

Of course, I don't want to waist time implementing all these by myself, because it's basic operation in Image Processing (IP) domain. And I believe that all these tasks are pretty much trivial for any engineer who's working in Image Processing.

As usual I have strict restriction regarding the licence of selected library (which can be used in any commercial product).

So, I've started googling. Here is the initial (and filtered) results:

* [Java Advanced Imaging (JAI)](http://www.oracle.com/technetwork/java/javase/tech/jai-142803.html) - Sun Binary Code License
* [ImageJ](http://rsb.info.nih.gov/ij/) - Open Source, Public Domain 
* Apache [Commons Imaging](http://commons.apache.org/proper/commons-imaging/index.html) - Apache License 2.0
* [JAITools](http://jaitools.org/) - Simplified BSD License
* [Marvin](http://marvinproject.sourceforge.net/en/index.html) - LGPL License

## JAI

This library was developed by SUN. Unfortunately, it's not supported anymore. But, it's very powerful and has nice facilities.

JAI is available for Windows, Linux, Mac OS X, and Solaris, and takes advantage of native acceleration when available. However, you can use the JAI libraries on any platform if you add the following JAR files to your classpath: 

* `jai_core.jar` and `jai_codec.jar` ([http://download.java.net/media/jai/builds/release/1\_1\_3/](http://download.java.net/media/jai/builds/release/1_1_3/))
* `jai_imageio.jar` ([http://download.java.net/media/jai-imageio/builds/release/1.1/](http://download.java.net/media/jai-imageio/builds/release/1.1/))

## JAI Tutorials, Guides, Sources

* [Java Advanced Imaging API FAQ](http://www.oracle.com/technetwork/java/jaifaq-138288.html)
* [Java Image Processing Cookbook, by Rafael Santos](http://www.lac.inpe.br/JIPCookbook/) it's very cool book with tons of samples
* [Programming in Java™ Advanced Imaging](http://docs.oracle.com/cd/E19957-01/806-5413-10/806-5413-10.pdf) book. Just "google" it.

Also, you should check the JAI sources. Here is the [master JAI project](https://java.net/projects/jai) on java.net with several sub-projects:

* [Jai-core](https://java.net/projects/jai-core)
* [Jai-demos](https://java.net/projects/jai-demos)
* [Jai-webstart](https://java.net/projects/jai-webstart)
* [Jaistuff](https://java.net/projects/jaistuff)

JAI Licenses. It's very tricky question. Here is the quote from [java.net](https://www.java.net//node/665499):

> _As far as I know, the libraries from JAI and JAI Image I/O Tools can be  
> bundled with a commercial product or can be downloaded on the fly using  
> the Java Web Start technology._  
> _You might like to take a look at how people have been using JAI and JAI  
> Image I/O Tools:_  
> _[http://java.sun.com/products/java-media/jai/success/](http://java.sun.com/products/java-media/jai/success/ "http://java.sun.com/products/java-media/jai/success/")_  
> _As for commercial license, you might like to read the LICENSE and README  
> files for the binaries:_  
> _[http://download.java.net/media/jai/builds/release/1\_1\_3/LICENSE-jai.txt](http://download.java.net/media/jai/builds/release/1_1_3/LICENSE-jai.txt "http://download.java.net/media/jai/builds/release/1_1_3/LICENSE-jai.txt")  
> [http://download.java.net/media/jai/builds/release/1\_1\_3/DISTRIBUTIONREAD...](http://download.java.net/media/jai/builds/release/1_1_3/DISTRIBUTIONREADME-jai.txt "http://download.java.net/media/jai/builds/release/1_1_3/DISTRIBUTIONREADME-jai.txt")  
> [http://download.java.net/media/jai-imageio/builds/release/1.1/LICENSE-ja...](http://download.java.net/media/jai-imageio/builds/release/1.1/LICENSE-jai_imageio.txt "http://download.java.net/media/jai-imageio/builds/release/1.1/LICENSE-jai_imageio.txt")  
> [http://download.java.net/media/jai-imageio/builds/release/1.1/DISTRIBUTI...](http://download.java.net/media/jai-imageio/builds/release/1.1/DISTRIBUTIONREADME-jai_imageio.txt "http://download.java.net/media/jai-imageio/builds/release/1.1/DISTRIBUTIONREADME-jai_imageio.txt")_  
> _and the licenses for the source code (if you make your own build of JAI):_  
> _[https://jai.dev.java.net/#Licenses](https://jai.dev.java.net/#Licenses "https://jai.dev.java.net/#Licenses")  
> [https://jai-imageio.dev.java.net/index.html#Licenses](https://jai-imageio.dev.java.net/index.html#Licenses "https://jai-imageio.dev.java.net/index.html#Licenses")

I'm not sure whether you can include this library into your commercial project. You should answer on this question by yourself.

## ImageJ

It's a very popular application/library in Java community. I've considered it also. This library has very big community. Also, it has many plugins. [Documentation](http://rsb.info.nih.gov/ij/docs/index.html) (User Guide, tutorials, wiki, FAQ, etc) are located in one place, easy to find. But, I wouldn't use ImageJ in case of simple image processing operations.

## Other Libraries

I've reviewed the mentioned above other libraries and I must say they have nice features also. But they are too heavy (as well as ImageJ) for the tasks I've been trying to accomplish.  
  
## Summary  

* JAI isn't maintained by Oracle. You should be careful when including it in commercial product
* [ImageJ](http://rsb.info.nih.gov/ij/), [Commons Imaging](http://commons.apache.org/proper/commons-imaging/index.html), [JAITools](http://jaitools.org/) , and [Marvin](http://marvinproject.sourceforge.net/en/index.html) are providing huge set of IP facilities, but it might be redundant in your case.
* Plain Java core image library can solve almost all your needs, except TIFF/PDF file  processing.
* TIFF/PDF file processing should be done by 3d-party libraries (e.g. iText, JAI).

## References

* [open source image processing lib in java](http://stackoverflow.com/questions/2407113/open-source-image-processing-lib-in-java)
* [Java Advanced Imaging (JAI) Library for Enhanced Image Support](http://www.icesoft.org/wiki/display/PDF/Java+Advanced+Imaging+%28JAI%29+Library+for+Enhanced+Image+Support)
* [https://java.net/projects/jai](https://java.net/projects/jai) 
* [Where to find an up-to-date tutorial of JAI programming](https://www.java.net//node/671977?force=621)
* [Commercial licence of JAI and Image IO libraries](https://www.java.net/node/665499?force=446)
* [Where can I download Jai and Jai-imageio?](http://stackoverflow.com/questions/7502181/where-can-i-download-jai-and-jai-imageio)
* [Is JAI still being maintained?](https://www.java.net//forum/topic/javadesktop/java-desktop-technologies/jai-imageio/jai-still-being-maintained)
* [JAI Status](https://www.java.net//node/695373)