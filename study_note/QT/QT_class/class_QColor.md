# QColor

## 基本功能
QColor类用来生成基于RGB、HSV、CMYK值的各种颜色  
一般产生的都是各种颜色对象，然后被其他函数调用作为颜色参数  
```
直接初始化一个QColor对象
QColor(10, 100 , 50, 255)
```


## QColor常用函数
1. void QColor::setRgb(int r, int g, int b, int a = 255)
setRgb函数用来设置颜色对象的RGB值  
r参数用来设置红色，范围0到255之间  
g参数用来设置绿色，范围0到255之间  
b参数用来设置蓝色，范围0到255之间  
a参数用来设置alpha值，即颜色的透明度，默认为255  
```
QColor mycolor;
mycolor.setRgb(10, 100 , 50); 每个参数的含义，参数范围为0~255
```