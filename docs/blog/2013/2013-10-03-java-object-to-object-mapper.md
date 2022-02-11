# Java Object to Object Mapper
> | java |

I've been using Dozer some time on the project. But, recently I have got very interesting error which motivates me to look around and try to use other Object to Object mapper.  
  
Here is the list of tools I've found:  

* [Dozer:](http://dozer.sourceforge.net/) Dozer is a Java Bean to Java Bean mapper that recursively copies data from one object to another. Typically, these Java Beans will be of different complex types.
* [Orika:](http://code.google.com/p/orika/) Orika is a Java Bean mapping framework that recursively copies (among other capabilities) data from one object to another. It can be very useful when developing multi-layered applications.
* [Transmorph](http://sourceforge.net/projects/transmorph/): Transmorph is a free java library used to convert a Java object of one type into an object of another type (with another signature, possibly parameterized).
* [EZMorph](http://ezmorph.sourceforge.net/): EZMorph is simple java library for transforming an Object to another Object. It supports transformations for primitives and Objects, for multidimensional arrays and transformations with DynaBeans
* [Commons-BeanUtils](http://jakarta.apache.org/commons/beanutils): ConvertUtils -> Utility methods for converting String scalar values to objects of the specified Class, String arrays to arrays of the specified Class.
* [Commons-Lang](http://jakarta.apache.org/commons/lang): ArrayUtils -> Operations on arrays, primitive arrays (like int\[\]) and primitive wrapper arrays (like Integer\[\]).
* [Commons-Convert](http://jakarta.apache.org/commons): Commons-Convert aims to provide a single library dedicated to the task of converting an object of one type to another. The first stage will focus on Object to String and String to Object conversions.
* [Morph](http://morph.sourceforge.net/): Morph is a Java framework that eases the internal interoperability of an application. As information flows through an application, it undergoes multiple transformations. Morph provides a standard way to implement these transformations.
* [Lorentz](http://gleamynode.net/dev/lorentz/docs/index.html): Lorentz is a generic object-to-object conversion framework. It provides a simple API to convert a Java objects of one type into an object of another type. (seems dead)
* [Spring framework](http://springframework.org/): Spring has an excellent support for PropertyEditors, that can also be used to transform Objects to/from Strings.
* [ModelMapper](http://modelmapper.org/): ModelMapper is an intelligent object mapping framework that automatically maps objects to each other. It uses a convention based approach to map objects while providing a simple refactoring safe API for handling specific use cases.
* [OTOM](https://otom.dev.java.net/): With OTOM, you can copy any data from any object to any other object. The possibilities are endless. Welcome to "Autumn".
* [Smooks](http://www.smooks.org/mediawiki/index.php?title=V1.2%3aSmooks_v1.2_User_Guide#Java_Binding): The Smooks JavaBean Cartridge allows you to create and populate Java objects from your message data (i.e. bind data to).
* [Nomin](http://nomin.sourceforge.net/): Nomin is a mapping engine for the Java platform transforming object trees according to declarative mapping rules. This Java mapping framework aims to reduce efforts when it's needed to map different structures to each other.
* [Modelbridge](http://www.modelbridge.org/): Modelbridge is an Eclipse plugin that lets you copy data between Java objects.
* [omapper](http://code.google.com/p/omapper/): This project aims at providing a simple library to ease the process of mapping objects or beans from one design layer to another design layer, using annotations. One can specify mappings both in source class (Sink Annotation) and target class(Source Annotation). Supports mapping composed user class objects and array fields. 
* [Moo](http://geoffreywiseman.github.io/Moo/): Moo maps an object or graph of objects to another object or set of objects while trying to stay as unintrusive as possible and easy-to-use. Moo makes it possible to create quick copies and data transfer objects.   
* [OpenL Tablets](http://openl-tablets.sourceforge.net/mapper): treats tables in Excel and Word files as a source of application logic. This approach may be unusual, but it has it's own unique advantages, in particular it allows to close the gap between business world and IT world.
* [JMapper](http://code.google.com/p/jmapper-framework/): JMapper Framework is a java bean to java bean mapper, allows you to perform the passage of data dynamically with annotations and / or XML.

## References

* [Dozer vs Orika vs Manual](http://blog.sokolenko.me/2013/05/dozer-vs-orika-vs-manual.html)
* [any tool for java object to object mapping?](http://stackoverflow.com/questions/1432764/any-tool-for-java-object-to-object-mapping)