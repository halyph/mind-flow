# Java PDF Libraries
> | java |

Recently I had a task to select some Java PDF libraries for PDF generation. But it wasn't a simple task.  
The first thing which came into my mind was iText. It's well know Java library with good reputation. But... there is some stopper. iText version 5+ is released under the AGPL license. I.e. we have to pay money if we want to use iText in commercial product.  
  
I've created the next small checklist which covers project needs:  

1. liberal license
2. support maximum amount of project features (e.g. absolute element positioning)
3. good documentation
4. huge amount of samples
5. possibility to render HTML to PDF

I've reviewed the next libraries:  

* [iText 5.0+](http://itextpdf.com/) AGPL license
* [iText 4.2](https://github.com/ymasory/iText-4.2.0) MPL/LGPL licenses
* [PDF Box](http://pdfbox.apache.org/) Apache License, Version 2.0
* [JPedal](http://sourceforge.net/projects/jpedal/) JPedal has a LGPL release to pride a full java PDF viewer under a LGPL license
* [FOP](http://xml.apache.org/fop/) Apache License, Version 2.0
* [gnujpdf](http://gnujpdf.sourceforge.net/) LGPL License
* [PJX](http://sourceforge.net/projects/pjx/) GPLv2 License
* [PDFjet](http://pdfjet.com/os/edition.html) Strange Open Source license model
* [jPod](http://sourceforge.net/projects/jpodlib/) BSD License
* [PDF Renderer](http://java.net/projects/pdf-renderer) Maintaining is not active

### iText review

* iText 2.1.7: the latest official release under the MPL & LGPL license;
* iText 4.2.0: the latest unofficial release under the MPL & LGPL license;
* iText 5.0.0 and higher: released under the AGPL license.

[Notes about iText 5.0+ vs iText 4.2](https://github.com/ymasory/iText-4.2.0#background)  

> _Beginning with iText version 5.0 the developers have moved to the AGPL to improve their ability to sell commercial licenses. .. To assist those desiring to stick with the old license was made the final MPL/LGPL version more easily available and forked on github._

### Apache™ FOP

Apache™ FOP (Formatting Objects Processor) is a print formatter driven by XSL formatting objects (XSL-FO) and an output independent formatter. It is a Java application that reads a formatting object (FO) tree and renders the resulting pages to a specified output. This lib doesn't have enough flexibility for absolute page element positioning. But, it might be really valuable as content convertor.

### Apache PDFBox

Very interesting project. It has very impressive amount of features. And most important it's in active development.  

## Summary

I've selected **iText** v.4.2 which has acceptable license and huge community. But the most important feature it's a very good documentation (actually it's a book [iText in Action — 2nd Edition](http://itextpdf.com/book/)), tons of samples. Almost all samples for iText v.5 can be easily applied to iText v.4.2.  
Other libraries have not so much samples/demos. And for quick start it's very important.  
  
Here is maven dependency info:  

```xml
<dependency>
    <groupid>com.lowagie</groupid>
    <artifactid>itext</artifactid>
    <version>4.2.0</version>
</dependency>
```

**PDFBox** is selected as backup library. I.e. I will use it when iText has some limitations.  
  
## References

* [http://stackoverflow.com/questions/14213195/itext-latest-maven-dependency](http://stackoverflow.com/questions/14213195/itext-latest-maven-dependency)
* [http://java-source.net/open-source/pdf-libraries](http://java-source.net/open-source/pdf-libraries)
* [http://javatoolbox.com/categories/pdf](http://javatoolbox.com/categories/pdf)