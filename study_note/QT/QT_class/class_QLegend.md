# QLegend

## 基本功能
QLegend类是QChart中的数据对应的图例  
当图表中的数据发生变化时，QChart会自动更新图例的状态  
默认情况下，图例是绑定在QChart上的，但可以通过设置解绑来使图例独立于QChart的布局  
QLegend对象不能被创造或删除，可以通过QChart类中的legend()方法获取  
父类：QGraphicsWidget  
子类：无  


## QLegend和QLegendMarker的区别
QLegend主要实现对图例的编辑，包括图例的位置、字体、颜色等
QLegendMarker主要实现图例与图表的对应关系，例如：点击图例可以显示/隐藏相应的图表等


## 关于图例太多导致显示不下的问题
1. 问题描述
一张图表中有十根曲线，每根曲线都有对应的名称标识
由于这10个名称都显示在一行，所以名称显示不全，会出现省略号
2. 问题解决
希望能够把图例分成两行显示，每一行五个图例，但目前没有找到这样设置的办法
要么把字体缩小，让10个图例的名称都显示在一行中
要么把图例显示在图标左侧或右侧，这样每个名称单独占一行


## 构造函数
QLegend没有构造函数，只能通过以下方法获取图例对象  
```
QLegend \*QChart::legend() const
```


## 常用成员变量
1. alignment : Qt::Alignment
这个属性设置图例在图表中的显示位置  
取值只支持以下几个，而且只能设置其中一个  
```
Qt::AlignTop, Qt::AlignBottom, Qt::AlignLeft, Qt::AlignRight
```
1.1 Qt::Alignment alignment() const
1.2 void setAlignment(Qt::Alignment alignment)

2. backgroundVisible : bool
这个属性设置图例的背景是否可见  
2.1 bool isBackgroundVisible() const
2.2 void setBackgroundVisible(bool visible = true)

3. borderColor : QColor
这个属性设置图例的边界线的颜色  
3.1 QColor borderColor()
3.2 void setBorderColor(QColor color)

4. color : QColor
这个属性设置图例的背景颜色(brush)
如果改变了这个背景颜色，图例的brush会被设置为Qt::SolidPattern  
4.1 QColor color()
4.2 void setColor(QColor color)

5. font : QFont
这个属性设置图例中的字体
5.1 QFont font() const
5.2 void setFont(const QFont &font)

6. labelColor : QColor
这个属性设置图例的标签颜色(brush)  
6.1 QColor labelColor() const
6.2 void setLabelColor(QColor color)

7. markerShape : MarkerShape
这个属性设置图例标识的形状，默认值为MarkerShapeRectangle  
备注：这个属性是在Qt 5.9版本引入的  
7.1 QLegend::MarkerShape markerShape() const
7.2 void setMarkerShape(QLegend::MarkerShape shape)

8. reverseMarkers : bool
这个属性设置是否反转图例的顺序，默认值为false  
8.1 bool reverseMarkers()
8.2 void setReverseMarkers(bool reverseMarkers = true)

9. howToolTips : bool
这个属性设置当图例的标签文本被截断时，是否显示提示文本，默认值是false  
9.1 bool showToolTips() const
9.2 void setShowToolTips(bool show)


## 常用公共函数：绑定/解绑图例与图表
1. void QLegend::attachToChart()

2. void QLegend::detachFromChart()

3. bool QLegend::isAttachedToChart()


## 常用公共函数：获取QPen/QBrush
1. QPen QLegend::pen() const

2. QBrush QLegend::labelBrush() const

3. QBrush QLegend::brush() const

4. void QLegend::setPen(const QPen &pen)

5. void QLegend::setLabelBrush(const QBrush &brush)

6. void QLegend::setBrush(const QBrush &brush)


## enum QLegend::MarkerShape
这个集合中包含了所有图例标识的形状，默认值为MarkerShapeRectangle  
```
Constant 						Value 	Description
QLegend::MarkerShapeDefault 	0 		默认形状，仅当独立的QLegendMarker
QLegend::MarkerShapeRectangle 	1 		矩形标识，标识尺寸由字体尺寸决定
QLegend::MarkerShapeCircle 		2 		圆形标识，标识尺寸由字体尺寸决定
QLegend::MarkerShapeFromSeries 	3 		标识形状由对应的数据类型来决定
对于点状图，标识形状是类似的小圆点
对于曲线图，标识形状是一个小线段
对于其他类型的图，标识形状是矩形
```


