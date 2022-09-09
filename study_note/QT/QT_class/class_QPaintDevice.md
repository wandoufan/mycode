# QPaintDevice

## 基本功能
QPaintDevice是所有支持QPainter绘图的设备类的基类  
父类：无  
子类：QGLFramebufferObject, QGLPixelBuffer, QImage, QOpenGLPaintDevice, QPagedPaintDevice, QPaintDeviceWindow, QPicture, QPixmap, QSvgGenerator, and QWidget  
使用时在.pro文件中要添加  
```
QT += gui
```


## 详细说明
QPaintDevice一般不直接使用，常用QPainter来绘图的类包括：
```
QImage
QPicture
QPixmap
QWidget
QPagedPaintDevice - QPdfWriter
QPagedPaintDevice - QPrinter
```


## 构造函数
QPaintDevice是抽象基类，没有构造函数  