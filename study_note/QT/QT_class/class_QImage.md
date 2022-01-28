# QImage

## 基本功能
QImage类提供了不依赖于硬件的图像表示，主要用于I/O和直接逐像素访问、操作  
QImage可以直接用QPainter进行绘画操作，另外还支持十几种图像格式，但显示性能低于QPixmap  
父类：QPaintDevice  


## 详细说明
1. 当使用在一个QImage对象上使用QPainter时，绘画任务不会占用当前的GUI线程，而是另外启动一个线程  
2. QImage对象用数值来进行传输，因为QImage类使用了implicit data sharing机制
QImage对象也可以变成数据流，并进行比较  
3. Qt支持的图片格式
```
format		Description							Qt's support
BMP			Windows Bitmap						Read/write
GIF			Graphic Interchange Format			Read
JPG			Joint Photographic Experts Group	Read/write
JPE			GJoint Photographic Experts Group	Read/write
PNG			Portable Network Graphics			Read/write
PBM			Portable Bitmap						Read
PGM			Portable Graymap					Read
PPM			Portable Pixmap						Read/write
XBM			X11 Bitmap							Read/write
XPM			X11 Pixmap							Read/write
```


## 代码示例
1. 打开一个本地图片，调整大小后保存
```
QImage signimage;
signimage.load("E:/1.png");
signimage = signimage.scaled(pic_width, pic_height);
signimage.save("E:/1.png");
```
2. 读取.qrc中的某个图片资源，然后转换为QImage
```
QImage image_logo(":/MyImage/image/avic.jpeg");
```
'/MyImage'为前缀名  
'/image'为图片文件所在的目录名  
'/avic.jpeg'为图片名字  
为了获取正确的路径，最好选择图片文件，右键 - copy path  


## 构造函数
1. QImage()

2. QImage(QImage &&other)

3. QImage(const QImage &image)

4. QImage(const QString &fileName, const char \*format = nullptr)
加载图片文件来生成一个QImage对象  
fileName可以是磁盘中的一个实际文件，也可以是一个已经嵌入程序中的资源(.qrc)  

5. QImage(const char \*const [] xpm)

6. QImage(const uchar \*data, int width, int height, int bytesPerLine, QImage::Format format, QImageCleanupFunction cleanupFunction = nullptr, void \*cleanupInfo = nullptr)

7. QImage(uchar \*data, int width, int height, int bytesPerLine, QImage::Format format, QImageCleanupFunction cleanupFunction = nullptr, void \*cleanupInfo = nullptr)

8. QImage(const uchar \*data, int width, int height, QImage::Format format, QImageCleanupFunction cleanupFunction = nullptr, void \*cleanupInfo = nullptr)

9. QImage(uchar \*data, int width, int height, QImage::Format format, QImageCleanupFunction cleanupFunction = nullptr, void \*cleanupInfo = nullptr)

10. QImage(int width, int height, QImage::Format format)

11. QImage(const QSize &size, QImage::Format format)


## 常用公共函数：图片读取
1. bool QImage::load(const QString &fileName, const char \*format = nullptr)
从本地文件中加载图片  
fileName可以是磁盘中的一个实际文件，也可以是一个已经嵌入程序中的资源(.qrc)  

2. bool QImage::load(QIODevice \*device, const char \*format)
从一个给定的设备中加载图片  
这个函数可以把加载的图片直接转换成一个QByteArray对象  

3. bool QImage::loadFromData(const uchar \*data, int len, const char \*format = nullptr)
从二进制数据data的第len个字符开始加载图片  

4. bool QImage::loadFromData(const QByteArray &data, const char \*format = nullptr)
从QByteArray格式的数据中加载图片  


## 常用公共函数：图片保存
1. bool QImage::save(const QString &fileName, const char \*format = nullptr, int quality = -1) const
用给定的fileName来保存图片，保存时可以用format来指定图片格式  
quality用来指定压缩程度，范围在0-100之间  
quality为0时获得一个压缩后的小文件，为100时获得一个未压缩的大文件  

2. bool QImage::save(QIODevice \*device, const char \*format = nullptr, int quality = -1) const
把图片保存到一个指定的设备中 
这个函数可以把图片直接保存到一个QByteArray对象中，例如：  
```
// writes image into ba in PNG format
QImage image;
QByteArray ba;
QBuffer buffer(&ba);
buffer.open(QIODevice::WriteOnly);
image.save(&buffer, "PNG");
```


## 常用公共函数：修改图片


## 常用公共函数：获取图片尺寸信息
1. QSize QImage::size() const

2. int QImage::width() const

3. int QImage::height() const

4. int QImage::dotsPerMeterX() const

5. int QImage::dotsPerMeterY() const

6. QRect QImage::rect() const
返回图片的外切矩形  

7. bool QImage::valid(const QPoint &pos) const
判断给定的pos坐标是否位于图片范围之内  

8. bool QImage::valid(int x, int y) const
判断给定的pos坐标是否位于图片范围之内  

9. QPoint QImage::offset() const
返回图片补偿的像素个数  

10. void QImage::setOffset(const QPoint &offset)
设置图片补偿的像素个数  


## 常用公共函数：获取图片颜色信息


## 常用公共函数：获取图片文本信息


## 常用公共函数：获取图片底层信息


## 常用公共函数：对图片进行缩放

## 公共静态函数