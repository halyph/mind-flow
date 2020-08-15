# Java Barcode Generation and Scanning Library
> | java |

Recently I had to pick library which can generate and scan different 2D barcodes. Actually I was interested in [QR Code](http://en.wikipedia.org/wiki/QR_code) and [Data Matrix](http://en.wikipedia.org/wiki/Data_Matrix). There is only ONE open source Java library which generates and scans barcode, it's [Zxing](http://code.google.com/p/zxing/). You might say there are others, but they cost money.  
  
I've been following Zxing some time and must admit that this library has very vibrant community, code base is clean, plenty of unit tests. Also, API is very clean. Here is a simple code snippet for scanning Data Matrix barcode:  
  
```java
String filename = "file.png";  

Map<DecodeHintType,Object> hints = new EnumMap<DecodeHintType,Object>(DecodeHintType.class);  
hints.put(DecodeHintType.POSSIBLE\_FORMATS, Arrays.asList(BarcodeFormat.DATA_MATRIX));  
hints.put(DecodeHintType.TRY_HARDER, Boolean.TRUE);  
BinaryBitmap binaryBitmap = new BinaryBitmap(new HybridBinarizer(  
        new BufferedImageLuminanceSource(  
            ImageIO.read(new FileInputStream(filename)))));  
  
Result result = new MultiFormatReader().decode(binaryBitmap, hints);  
System.out.println(result.getText());  
```
  
I've tested Zxing v.2.2 QR Code/Data Matrix scanning. And Zxing implementation for QR Code scanning is more robust and well implemented in comparison to Data Matrix. I.e. if you have freedom and can choose any of these two barcodes, than select QR Code.  
  
Note, there are several open source barcode generation libraries and only a few barcode scanners (actually one Zxing for Java)