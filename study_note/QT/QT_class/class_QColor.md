# QColor

## 基本功能
QColor类用来生成基于RGB、HSV、CMYK值的各种颜色  
一般产生的都是各种颜色对象，然后被其他函数调用作为颜色参数  
颜色取值详见namespace中的enum Qt::GlobalColor  
RGB：(red, green, blue) 最常用的一种类型  
HSV：(hue, saturation, value)  
CMYK：(cyan, magenta, yellow and black)  


## 代码示例
1. 把QColor转换为QString
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
QColor mycolor;
mycolor = QColor(10, 100 , 50, 255);
```
2. QColor::QColor(QRgb color)

3. QColor::QColor(QRgba64 rgba64)

4. QColor::QColor(QLatin1String name)


## 常用公共函数
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


## 静态公共函数
1. [static] QStringList QColor::colorNames()
返回一个QStringList，包含了所有Qt中已知的颜色的名字  
经过测试，颜色本身一共148种，且与QColor对象的值无关  

2. [static] QColor QColor::fromRgb(QRgb rgb)
使用rgb参数返回一个QColor对象，其中rgb参数的alpha部分会被忽略掉  

3. [static] QColor QColor::fromRgb(int r, int g, int b, int a = 255)
使用rgb参数返回一个QColor对象，参数值范围必须在0-255之间  

3. [static] QColor QColor::fromRgbF(qreal r, qreal g, qreal b, qreal a = 1.0)
使用rgb参数返回一个QColor对象，参数值范围必须在0.0-1.0之间  

4. [static] bool QColor::isValidColor(const QString &name)
判断颜色名字是否合法  




