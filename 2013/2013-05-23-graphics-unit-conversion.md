# Graphics Unit Conversion
> | java |

Working with PDF files and with scanned images it always required to convert from point to millimeter, or from millimeter to pixel, and so on.  
  
There is very interesting quote from [iText in Action](http://www.manning.com/lowagie2/) book:  

> What is the measurement unit in PDF documents? Most of the measurements in PDFs are expressed in user space units. ISO-32000-1 (section 8.3.2.3) tells us “the  default  for  the  size  of  the  unit  in  default  user  space  (1/72  inch)  is approximately  the  same  as  a  point  (pt),  a  unit  widely  used  in  the  printing industry. It is not exactly the same; there is no universal definition of a point.” In short, 1 in. = 25.4 mm = 72 user units (which roughly corresponds to 72 pt).

Of course,  you can easily write these utilities by yourself. But, sometimes it makes sense to look around in your project, maybe you've already had all required utils.  
  
So, here are code snippets from several libraries  
  
[1\. Barcode4j](http://barcode4j.sourceforge.net/)  
  
```java
package org.krysalis.barcode4j.tools;

/**
 * Utility class for unit conversions.
 * 
 * @author Jeremias Maerki
 * @version $Id: UnitConv.java,v 1.2 2004/09/04 20:25:56 jmaerki Exp $
 */
public class UnitConv {

    /**
     * Utility class: Constructor prevents instantiating when subclassed.
     */
    protected UnitConv() {
        throw new UnsupportedOperationException();
    }
    
    /**
     * Converts millimeters (mm) to points (pt)
     * @param mm the value in mm
     * @return the value in pt
     */
    public static double mm2pt(double mm) {
        return mm * 2.835;
    }

    /**
     * Converts points (pt) to millimeters (mm)
     * @param pt the value in pt
     * @return the value in mm
     */
    public static double pt2mm(double pt) {
        return pt / 2.835;
    }
    
    /**
     * Converts millimeters (mm) to inches (in)
     * @param mm the value in mm
     * @return the value in inches
     */
    public static double mm2in(double mm) {
        return mm / 25.4;
    }
    
    /**
     * Converts inches (in) to millimeters (mm)
     * @param in the value in inches
     * @return the value in mm
     */
    public static double in2mm(double in) {
        return in * 25.4;
    }
    
    /**
     * Converts millimeters (mm) to pixels (px)
     * @param mm the value in mm
     * @param resolution the resolution in dpi (dots per inch)
     * @return the value in pixels
     */
    public static int mm2px(double mm, int resolution) {
        return (int)Math.round(mm2in(mm) * resolution);
    }
}
```

[2\. iText v.4.2](https://github.com/ymasory/iText-4.2.0)  

```java
package com.lowagie.text;

/**
 * A collection of convenience methods that were present in many different iText
 * classes.
 */

public class Utilities {

...
 
 /**
  * Measurement conversion from millimeters to points.
  * @param value a value in millimeters
  * @return a value in points
  * @since 2.1.2
  */
 public static final float millimetersToPoints(float value) {
     return inchesToPoints(millimetersToInches(value));
 }

 /**
  * Measurement conversion from millimeters to inches.
  * @param value a value in millimeters
  * @return a value in inches
  * @since 2.1.2
  */
 public static final float millimetersToInches(float value) {
     return value / 25.4f;
 }

 /**
  * Measurement conversion from points to millimeters.
  * @param value a value in points
  * @return a value in millimeters
  * @since 2.1.2
  */
 public static final float pointsToMillimeters(float value) {
     return inchesToMillimeters(pointsToInches(value));
 }

 /**
  * Measurement conversion from points to inches.
  * @param value a value in points
  * @return a value in inches
  * @since 2.1.2
  */
 public static final float pointsToInches(float value) {
     return value / 72f;
 }

 /**
  * Measurement conversion from inches to millimeters.
  * @param value a value in inches
  * @return a value in millimeters
  * @since 2.1.2
  */
 public static final float inchesToMillimeters(float value) {
     return value * 25.4f;
 }

 /**
  * Measurement conversion from inches to points.
  * @param value a value in inches
  * @return a value in points
  * @since 2.1.2
  */
 public static final float inchesToPoints(float value) {
     return value * 72f;
 }
    ...
}
```

[3\. FOP](http://xmlgraphics.apache.org/fop/)  

```java
package org.apache.fop.util;

import java.awt.geom.AffineTransform;

/**
 * Utility class for unit conversions.
 * @deprecated use org.apache.xmlgraphics.util.UnitConv instead.
 */
public final class UnitConv {

    /**
     * conversion factory from millimeters to inches.
     * @deprecated use org.apache.xmlgraphics.util.UnitConv.IN2MM instead.
     */
    public static final float IN2MM = org.apache.xmlgraphics.util.UnitConv.IN2MM;

    /**
     * conversion factory from centimeters to inches.
     * @deprecated use org.apache.xmlgraphics.util.UnitConv.IN2CM instead.
     */
    public static final float IN2CM = org.apache.xmlgraphics.util.UnitConv.IN2CM;

    /**
     * conversion factory from inches to points.
     * @deprecated use org.apache.xmlgraphics.util.UnitConv.IN2PT instead.
     */
    public static final int IN2PT = org.apache.xmlgraphics.util.UnitConv.IN2PT;

    /**
     * Converts millimeters (mm) to points (pt)
     * @param mm the value in mm
     * @return the value in pt
     * @deprecated use org.apache.xmlgraphics.util.UnitConv.mm2pt(mm) instead.
     */
    public static double mm2pt(double mm) {
        return org.apache.xmlgraphics.util.UnitConv.mm2pt(mm);
    }

    /**
     * Converts millimeters (mm) to millipoints (mpt)
     * @param mm the value in mm
     * @return the value in mpt
     * @deprecated use org.apache.xmlgraphics.util.UnitConv.mm2mpt(mm) instead.
     */
    public static double mm2mpt(double mm) {
        return org.apache.xmlgraphics.util.UnitConv.mm2mpt(mm);
    }

    /**
     * Converts points (pt) to millimeters (mm)
     * @param pt the value in pt
     * @return the value in mm
     * @deprecated use org.apache.xmlgraphics.util.UnitConv.pt2mm(pt) instead.
     */
    public static double pt2mm(double pt) {
        return org.apache.xmlgraphics.util.UnitConv.pt2mm(pt);
    }

    /**
     * Converts millimeters (mm) to inches (in)
     * @param mm the value in mm
     * @return the value in inches
     * @deprecated use org.apache.xmlgraphics.util.UnitConv.pt2mm(pt) instead.
     */
    public static double mm2in(double mm) {
        return org.apache.xmlgraphics.util.UnitConv.mm2in(mm);
    }

    /**
     * Converts inches (in) to millimeters (mm)
     * @param in the value in inches
     * @return the value in mm
     * @deprecated use org.apache.xmlgraphics.util.UnitConv.in2mm(in) instead.
     */
    public static double in2mm(double in) {
        return org.apache.xmlgraphics.util.UnitConv.in2mm(in);
    }

    /**
     * Converts inches (in) to millipoints (mpt)
     * @param in the value in inches
     * @return the value in mpt
     * @deprecated use org.apache.xmlgraphics.util.UnitConv.in2mpt(in) instead.
     */
    public static double in2mpt(double in) {
        return org.apache.xmlgraphics.util.UnitConv.in2mpt(in);
    }

    /**
     * Converts inches (in) to points (pt)
     * @param in the value in inches
     * @return the value in pt
     * @deprecated use org.apache.xmlgraphics.util.UnitConv.in2pt(in) instead.
     */
    public static double in2pt(double in) {
        return org.apache.xmlgraphics.util.UnitConv.in2pt(in);
    }

    /**
     * Converts millipoints (mpt) to inches (in)
     * @param mpt the value in mpt
     * @return the value in inches
     * @deprecated use org.apache.xmlgraphics.util.UnitConv.mpt2in(mpt) instead.
     */
    public static double mpt2in(double mpt) {
        return org.apache.xmlgraphics.util.UnitConv.mpt2in(mpt);
    }

    /**
     * Converts millimeters (mm) to pixels (px)
     * @param mm the value in mm
     * @param resolution the resolution in dpi (dots per inch)
     * @return the value in pixels
     * @deprecated use org.apache.xmlgraphics.util.UnitConv.mm2px(mm, resolution) instead.
     */
    public static double mm2px(double mm, int resolution) {
        return org.apache.xmlgraphics.util.UnitConv.mm2px(mm, resolution);
    }

    /**
     * Converts millipoints (mpt) to pixels (px)
     * @param mpt the value in mpt
     * @param resolution the resolution in dpi (dots per inch)
     * @return the value in pixels
     * @deprecated use org.apache.xmlgraphics.util.UnitConv.mpt2px(mpt, resolution) instead.
     */
    public static double mpt2px(double mpt, int resolution) {
        return org.apache.xmlgraphics.util.UnitConv.mpt2px(mpt, resolution);
    }

    /**
     * Converts a millipoint-based transformation matrix to points.
     * @param at a millipoint-based transformation matrix
     * @return a point-based transformation matrix
     * @deprecated use org.apache.xmlgraphics.util.UnitConv.mptToPt(at) instead.
     */
    public static AffineTransform mptToPt(AffineTransform at) {
        return org.apache.xmlgraphics.util.UnitConv.mptToPt(at);
    }

    /**
     * Converts a point-based transformation matrix to millipoints.
     * @param at a point-based transformation matrix
     * @return a millipoint-based transformation matrix
     * @deprecated use org.apache.xmlgraphics.util.UnitConv.ptToMpt(at) instead.
     */
    public static AffineTransform ptToMpt(AffineTransform at) {
        return org.apache.xmlgraphics.util.UnitConv.ptToMpt(at);
    }
}
```