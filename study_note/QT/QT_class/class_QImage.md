# QImage

## 基本功能
QImage类提供了不依赖于硬件的图像表示，主要用于I/O和直接逐像素访问、操作  
QImage可以直接用QPainter进行绘画操作，另外还支持十几种图像格式，但显示性能低于QPixmap  
父类：QPaintDevice  


## 代码示例
1. 打开一个本地图片，调整大小后保存
```
QImage signimage;
signimage.load("E:/1.png");
signimage =  signimage.scaled(pic_width, pic_height);
signimage.save("E:/1.png");
```


## 构造函数


## 常用公共函数



## 公共静态函数