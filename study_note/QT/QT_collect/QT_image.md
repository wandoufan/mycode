# Qt中的图像处理


## 继承关系
```
			 - QPixmap -  QBitmap
QPaintDevice - QImage
			 - QPicture
```


## 图像处理相关的类
Qt中提供了四个类来处理图像数据：  
1. QImage
QImage主要实现I/O操作，以及像素级别访问和操作  
2. QPixmap
QPixmap主要实现在屏幕上显示图像  
3. QBitmap
QBitmap只是一个继承于QPixmap的便捷类，确保深度为1  
4. QPicture
QPicture是一个记录和回放QPainter命令的绘制设备  


