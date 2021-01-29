# QColor

## 基本功能
QColor类用来生成基于RGB、HSV、CMYK值的各种颜色  
一般产生的都是各种颜色对象，然后被其他函数调用作为颜色参数  
备注：没有找到函数可以直接把QColor转换为QString类型，只能自己写函数转换  
```
QString SkyplotWidget::colorToString(QColor color)
{
    QString text = "(" + QString::number(color.red()) + ", "
            + QString::number(color.green()) + ", "
            + QString::number(color.blue()) + ")";
    return text;
}
```


## 构造函数
1. QColor::QColor(int r, int g, int b, int a = 255)
```
mycolor = QColor(10, 100 , 50, 255)
```
2. QColor::QColor(QRgb color)
3. QColor::QColor(QRgba64 rgba64)
4. QColor::QColor(QLatin1String name)


## enum Qt::GlobalColor
颜色也可以用下面的参数进行赋值  
```
Constant  Value  Description

Qt::white  3  White (#ffffff)
Qt::black  2  Black (#000000)
Qt::red  7  Red (#ff0000)
Qt::darkRed  13  Dark red (#800000)
Qt::green  8  Green (#00ff00) 
Qt::darkGreen  14  Dark green (#008000) 
Qt::blue  9  Blue (#0000ff) 
Qt::darkBlue  15  Dark blue (#000080) 
Qt::cyan  10  Cyan (#00ffff) 
Qt::darkCyan  16  Dark cyan (#008080) 
Qt::magenta  11  Magenta (#ff00ff) 
Qt::darkMagenta  17  Dark magenta (#800080) 
Qt::yellow  12  Yellow (#ffff00) 
Qt::darkYellow  18  Dark yellow (#808000) 
Qt::gray  5  Gray (#a0a0a4) 
Qt::darkGray  4  Dark gray (#808080) 
Qt::lightGray  6  Light gray (#c0c0c0) 
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

2. bool QColor::isValid() const
判断当前的QColor对象是否是一个合法值  

3. QString QColor::name() const
用"#RRGGBB"的格式返回当前的QColor对象的字符串值  
例如：返回值为"#ff0000"  