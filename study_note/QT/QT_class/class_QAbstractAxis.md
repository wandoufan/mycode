# QAbstractAxis

## 基本功能
QAbstractAxis作为Qt图标中的坐标轴，是所有图表坐标轴类的基类  
一般用来设置坐标轴的颜色、标题、网格线等各种属性  
但不包括向坐标轴中添加刻度值，添加刻度值使用QValueAxis  
备注：网格线和次要网格线的数量通过QValueAxis中的刻度数量来设置  
父类：QObject  
子类：QValueAxis，QBarCategoryAxis，QDateTimeAxis，QLogValueAxis  


## 构造函数
没有构造函数，QAbstractAxis是抽象基类，不直接使用  


## 常用成员变量
1. alignment : const Qt::Alignment
这个属性设置坐标轴的位置，取值详见namespace中的enum Qt::AlignmentFlag  
这个属性只能读，不能写  
1.1 Qt::Alignment alignment() const

2. color : QColor
这个属性设置坐标轴的颜色  
2.1 QColor linePenColor() const
2.2 void setLinePenColor(QColor color)

3. gridLineColor : QColor
这个属性设置网格线的颜色  
3.1 QColor gridLineColor()
3.2 void setGridLineColor(const QColor &color)

4. gridLinePen : QPen
这个属性设置用来画网格线的pen  
4.1 QPen gridLinePen() const
4.2 void setGridLinePen(const QPen &pen)

5. gridVisible : bool
这个属性设置网格线是否可见  
5.1 bool isGridLineVisible() const
5.2 void setGridLineVisible(bool visible = true)

6. labelsAngle : int
这个属性设置坐标轴标签的倾斜角度  
6.1 int labelsAngle() const
6.2 void setLabelsAngle(int angle)

7. labelsBrush : QBrush
这个属性设置用来画坐标轴标签的brush  
7.1 QBrush labelsBrush() const
7.2 void setLabelsBrush(const QBrush &brush)

8. labelsColor : QColor
这个属性设置坐标轴标签的颜色  
8.1 QColor labelsColor() const
8.2 void setLabelsColor(QColor color)

9. labelsFont : QFont
这个属性设置坐标轴标签的字体  
9.1 QFont labelsFont() const
9.2 void setLabelsFont(const QFont &font)

10. labelsVisible : bool
这个属性设置坐标轴标签是否可见  
10.1 bool labelsVisible() const
10.2 void setLabelsVisible(bool visible = true)

11. linePen : QPen
这个属性设置用来画线的pen  
备注：文档里没有具体说是什么线，应该是坐标轴线  
11.1 QPen linePen() const
11.2 void setLinePen(const QPen &pen)

12. lineVisible : bool
这个属性设置坐标轴线是否可见  
12.1 bool isLineVisible() const
12.2 void setLineVisible(bool visible = true)

13. minorGridLineColor : QColor
这个属性设置次要网格线的颜色  
仅当图表支持次要网格线时，该属性有效  
13.1 QColor minorGridLineColor()
13.2 void setMinorGridLineColor(const QColor &color)

14. minorGridLinePen : QPen
这个属性设置用来画次要网格线的pen  
仅当图表支持次要网格线时，该属性有效  
14.1 QPen minorGridLinePen() const
14.2 void setMinorGridLinePen(const QPen &pen)

15. minorGridVisible : bool
这个属性设置次要网格线是否可见  
仅当图表支持次要网格线时，该属性有效  
15.1 bool isMinorGridLineVisible() const
15.2 void setMinorGridLineVisible(bool visible = true)

16. orientation : const Qt::Orientation
这个属性设置坐标轴的朝向  
```
Qt::Horizontal
Qt::Vertical
```
这个属性只能读，不能写  
16.1 Qt::Orientation orientation() const

17. reverse : bool
这个属性设置是否使用反转坐标轴，默认为false  
17.1 bool isReverse() const
17.2 void setReverse(bool reverse = true)

18. shadesBorderColor : QColor
这个属性设置坐标轴阴影的边缘的颜色  
18.1 QColor shadesBorderColor() const
18.2 void setShadesBorderColor(QColor color)

19. shadesBrush : QBrush
这个属性设置用来画坐标轴阴影的brush  
19.1 QBrush shadesBrush() const
19.2 void setShadesBrush(const QBrush &brush)

20. shadesColor : QColor
这个属性设置坐标轴阴影的填充颜色  
20.1 QColor shadesColor() const
20.2 void setShadesColor(QColor color)

21. shadesPen : QPen
这个属性设置用来画坐标轴阴影的pen  
21.1 QPen shadesPen() const
21.2 void setShadesPen(const QPen &pen)

22. shadesVisible : bool
这个属性设置坐标轴阴影是否可见  
22.1 bool shadesVisible() const
22.2 void setShadesVisible(bool visible = true)

23. titleBrush : QBrush
这个属性设置用来画坐标轴标题的brush  
23.1 QBrush titleBrush() const
23.2 void setTitleBrush(const QBrush &brush)

24. titleFont : QFont
这个属性设置坐标轴标题的字体  
24.1 QFont titleFont() const
24.2 void setTitleFont(const QFont &font)

25. titleText : QString
这个属性设置坐标轴标题的文本内容  
默认为空，坐标轴标题支持HTML格式  
25.1 QString titleText() const
25.2 void setTitleText(const QString &title)

26. titleVisible : bool
这个属性设置坐标轴标题是否可见，默认为true  
26.1 bool isTitleVisible() const
26.2 void setTitleVisible(bool visible = true)

27. visible : bool
这个属性设置坐标轴是否可见  
27.1 bool isVisible() const
27.2 void setVisible(bool visible = true)


## 常用公共函数
1. void QAbstractAxis::hide()
设置坐标轴、坐标轴阴影、坐标轴标签、网格线都不可见  

2. void QAbstractAxis::show()
设置坐标轴、坐标轴阴影、坐标轴标签、网格线都可见  

3. void QAbstractAxis::setMax(const QVariant &max)
设置坐标轴显示的最大值  
根据坐标轴的实际类型，max参数会被转换成合适的值类型  
如果转换不能实现，这个函数不会做任何事情  

4. void QAbstractAxis::setMin(const QVariant &min)
设置坐标轴显示的最小值  
根据坐标轴的实际类型，min参数会被转换成合适的值类型  
如果转换不能实现，这个函数不会做任何事情  

5. void QAbstractAxis::setRange(const QVariant &min, const QVariant &max)
设置坐标轴显示的最小值和最大值  
根据坐标轴的实际类型，min和max参数会被转换成合适的值类型  
如果转换不能实现，这个函数不会做任何事情  
