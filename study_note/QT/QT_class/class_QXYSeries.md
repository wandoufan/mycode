# QXYSeries

## 基本功能
QXYSeries是Qt图表中x/y类型的数据来源，是曲线、折线、散点数据的基类  
一般用来对数据组中的数据点进行增删改查  
父类：QAbstractSeries  
子类：QLineSeries、QScatterSeries  


## 构造函数
没有构造函数，QXYSeries是抽象基类，不直接使用  


## 常用成员变量
1. color : QColor
这个属性设置图表中数据线或数据点的颜色  
备注：如果设置了其他图表主题，数据线的颜色可能会随着主题而改变  
1.1 virtual QColor color() const
1.2 virtual void setColor(const QColor &color)

2. pointLabelsClipping : bool
这个属性设置是否对数据点的标签进行裁剪  
默认为true，即对绘图区域边缘的标签进行裁剪  
2.1 bool pointLabelsClipping() const
2.2 void setPointLabelsClipping(bool enabled = true)

3. pointLabelsColor : QColor
这个属性设置数据点标签的颜色  
默认情况下，这个颜色是根据图表的主题来进行定义的  
3.1 QColor pointLabelsColor() const
3.2 void setPointLabelsColor(const QColor &color)

4. pointLabelsFont : QFont
这个属性设置数据点标签的字体  
4.1 QFont pointLabelsFont() const
4.2  void setPointLabelsFont(const QFont &font)

5. pointLabelsFormat : QString
这个属性设置数据点标签的显示格式  
QXYSeries支持以下两种标签格式  
```
@xPoint		The x-coordinate of the data point.
@yPoint		The y-coordinate of the data point.
```
标签格式的默认值为'@xPoint, @yPoint'  
5.1 QString pointLabelsFormat() const
5.2 void setPointLabelsFormat(const QString &format)

6. pointLabelsVisible : bool
这个属性设置数据点标签是否可见，默认为false  
6.1 bool pointLabelsVisible() const
6.2 void setPointLabelsVisible(bool visible = true)


## 常用公共函数：添加数据点
1. void QXYSeries::append(qreal x, qreal y)

2. void QXYSeries::append(const QPointF &point)

3. void QXYSeries::append(const QList<QPointF> &points))

4. void QXYSeries::insert(int index, const QPointF &point)


## 常用公共函数：删除数据点
1. void QXYSeries::remove(qreal x, qreal y)

2. void QXYSeries::remove(const QPointF &point)

3. void QXYSeries::remove(int index)

4. void QXYSeries::removePoints(int index, int count)
删除从index开始的count个数据点  

5. void QXYSeries::clear()
删除数据组中所有的数据点  


## 常用公共函数：修改数据点
1. void QXYSeries::replace(qreal oldX, qreal oldY, qreal newX, qreal newY)

2. void QXYSeries::replace(const QPointF &oldPoint, const QPointF &newPoint)

3. void QXYSeries::replace(int index, qreal newX, qreal newY)

4. void QXYSeries::replace(int index, const QPointF &newPoint)

5. void QXYSeries::replace(QList<QPointF> points)

6. void QXYSeries::replace(QVector<QPointF> points)


## 常用公共函数：查询数据点
1. const QPointF &QXYSeries::at(int index) const

2. QList<QPointF> QXYSeries::points() const

3. int QXYSeries::count() const
返回数据组中数据点的个数  