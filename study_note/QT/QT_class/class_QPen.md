# QPen

## 基本功能
QPen定义了QPainter描绘的线条和文字，可以对线条的颜色、虚实、粗细等做具体设置  
父类：无  
子类：无  


## 代码示例
1. 定义一个简单的QPen对象：蓝色，线宽为2，实线
```
QPen pen(Qt::blue, 2, Qt::SolidLine);
```


## 构造函数
1. QPen::QPen(QPen &&pen)

2. QPen::QPen(const QPen &pen)

3. QPen::QPen(const QBrush &brush, qreal width, Qt::PenStyle style = Qt::SolidLine, Qt::PenCapStyle cap = Qt::SquareCap, Qt::PenJoinStyle join = Qt::BevelJoin)

4. QPen::QPen(const QColor &color)

5. QPen::QPen(Qt::PenStyle style)

6. QPen::QPen()
构造一个默认的QPen对象(黑色，宽度为1，实线)
```
QPen pen();
```


## 常用公共函数：对线条进行设置
1. void QPen::setBrush(const QBrush &brush)

2. void QPen::setColor(const QColor &color)

3. void QPen::setStyle(Qt::PenStyle style)
设置线条的形式，默认为一条实线  

4. void QPen::setWidth(int width)
设置线条宽度  

5. void QPen::setWidthF(qreal width)
设置线条宽度  
