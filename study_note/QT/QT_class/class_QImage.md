# QImage

## 基本功能
QImage类提供了不依赖于硬件的图像表示，主要用于I/O和直接逐像素访问、操作  
QImage可以直接用QPainter进行绘画操作，另外还支持十几种图像格式，但显示性能低于QPixmap  
父类：QPaintDevice  
子类：无  


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
QImage image;
image.load("E:/1.png");
image = image.scaled(pic_width, pic_height);
image.save("E:/1.png");
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
```
QImage image = QImage("D:/1.png");
```

5. QImage(const char \*const [] xpm)

6. QImage(const uchar \*data, int width, int height, int bytesPerLine, QImage::Format format, QImageCleanupFunction cleanupFunction = nullptr, void \*cleanupInfo = nullptr)

7. QImage(uchar \*data, int width, int height, int bytesPerLine, QImage::Format format, QImageCleanupFunction cleanupFunction = nullptr, void \*cleanupInfo = nullptr)

8. QImage(const uchar \*data, int width, int height, QImage::Format format, QImageCleanupFunction cleanupFunction = nullptr, void \*cleanupInfo = nullptr)

9. QImage(uchar \*data, int width, int height, QImage::Format format, QImageCleanupFunction cleanupFunction = nullptr, void \*cleanupInfo = nullptr)

10. QImage(int width, int height, QImage::Format format)

11. QImage(const QSize &size, QImage::Format format)


## 常用公共函数：获取图片基本信息
1. bool QImage::isNull() const

2. QImage::Format QImage::format() const
获取图片格式  


## 常用公共函数：获取图片尺寸信息
1. QSize QImage::size() const

2. int QImage::width() const

3. int QImage::height() const

4. QRect QImage::rect() const
返回图片的外切矩形(0, 0, width(), height())  

5. bool QImage::valid(const QPoint &pos) const
判断给定的pos坐标是否位于图片范围之内  

6. bool QImage::valid(int x, int y) const
判断给定的pos坐标是否位于图片范围之内  

7. int QImage::dotsPerMeterX() const
返回在水平方向上每一米包含的像素个数，这里的每一米是指物理长度  

8. int QImage::dotsPerMeterY() const
返回在垂直方向上每一米包含的像素个数，这里的每一米是指物理长度  


## 常用公共函数：获取图片颜色信息
1. bool QImage::allGray() const
判断图片是否是灰度图，即红绿蓝三个颜色的数值相同  

2. QRgb QImage::color(int i) const
返回颜色信息，参数i表示索引位置，从0开始  


## 常用公共函数：获取图片的像素信息
1. int QImage::bitPlaneCount() const
返回位图平面的数量，即多少位构成一个像素，常见的值包括32、24、8、1

2. int QImage::depth() const
返回图片的深度，常见的值包括64、32、24、16、8、1  
深度就是指用多少位来存储一个像素  


## 常用公共函数：获取图片中的像素数据
1. uchar \*QImage::bits()
返回一个指针，指向第一个像素数据，效果等于scanLine(0)  

2. uchar \*QImage::scanLine(int i)
返回一个指针，指向第i个像素数据  


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
fileName参数指定保存图片的名称和路径  
format参数指定图片的保存格式  
quality参数指定压缩程度，范围在0-100之间  
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


## 常用公共函数：对图片进行镜像反转
1. QImage &&QImage::mirrored(bool horizontal = false, bool vertical = true) &&
horizontal参数指定为水平反转  
vertical参数指定为垂直反转  
注意：原QImage对象不会发生改变

2. QImage QImage::mirrored(bool horizontal = false, bool vertical = true) const &


## 常用公共函数：对图片进行部分截取
1. QImage QImage::copy(const QRect &rectangle = QRect()) const
截取图片的子区域，并作为一个QImage返回  
如果子区域超出了图片范围，则超出部分的像素值会被设置为0  

2. QImage QImage::copy(int x, int y, int width, int height) const
重载函数  


## 常用公共函数：对图片进行缩放
1. QImage QImage::scaled(const QSize &size, Qt::AspectRatioMode aspectRatioMode = Qt::IgnoreAspectRatio, Qt::TransformationMode transformMode = Qt::FastTransformation) const
获取QImage的一个copy对象，进行缩放后返回copy对象  
aspectRatioMode参数设置缩放时的宽高比例，取值详见namespace_enum.md  
transformMode参数指定在缩放时是否要进行平滑处理，取值详见namespace_enum.md  
注意：原QImage对象的尺寸并不会改变  

2. QImage QImage::scaled(int width, int height, Qt::AspectRatioMode aspectRatioMode = Qt::IgnoreAspectRatio, Qt::TransformationMode transformMode = Qt::FastTransformation) const
重载函数

3. QImage QImage::scaledToHeight(int height, Qt::TransformationMode mode = Qt::FastTransformation) const
将QImage缩放到指定的高度，缩放过程中宽高比例不变  

4. QImage QImage::scaledToWidth(int width, Qt::TransformationMode mode = Qt::FastTransformation) const
将QImage缩放到指定的宽度，缩放过程中宽高比例不变  


## 常用公共函数：其他
1. void QImage::swap(QImage &other)
对两个图片对象进行交换  


## 公共静态函数
1. [static] QImage QImage::fromData(const uchar \*data, int size, const char \*format = nullptr)

2. [static] QImage QImage::fromData(const QByteArray &data, const char \*format = nullptr)

3. [static] QImage::Format QImage::toImageFormat(QPixelFormat format)

4. [static] QPixelFormat QImage::toPixelFormat(QImage::Format format)

5. [static] QTransform QImage::trueMatrix(const QTransform &matrix, int width, int height)