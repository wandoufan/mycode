# QValueAxis

## 基本功能
QValueAxis用来向Qt图表中添加一个数值刻度类型的坐标轴  
父类：QAbstractAxis  
子类：QCategoryAxis  


## 构造函数
1. QValueAxis::QValueAxis(QObject \*parent = nullptr)


## 常用成员变量
1. labelFormat : QString
这个属性设置坐标轴标签的格式  
格式包括：d, i, o, x, X, f, F, e, E, g, G, c  
当QChart::localizeNumbers为true时，支持格式为：d, e, E, f, g, G, i  
1.1 QString labelFormat() const
1.2 void setLabelFormat(const QString &format)

2. max : qreal
这个属性设置坐标轴的最大值  
备注：QAbstractAxis::setMax()也有这个功能，没搞清楚二者区别  
2.1 qreal max() const
2.2 void setMax(qreal max)

3. min : qreal
这个属性设置坐标轴的最小值  
备注：QAbstractAxis::setMin()也有这个功能，没搞清楚二者区别  
3.1 qreal min() const
3.2 void setMin(qreal min)

4. minorTickCount : int
这个属性设置坐标轴上次要刻度的数量  
次要刻度对应的就是图表中的次要网格线的数量  
默认值为0，即没有次要网格线  
注意：这里的数量不是指总的次要刻度数量，而是两个主刻度之间的次要刻度数量  
4.1 int minorTickCount() const
4.2 void setMinorTickCount(int count)

5. tickAnchor : qreal
这个属性设置刻度和标签开始的基准值  
备注：这个属性从Qt 5.12版引入  
5.1 qreal tickAnchor() const
5.2 void setTickAnchor(qreal anchor)

6. tickCount : int
这个属性设置坐标轴上刻度的数量  
刻度对应的就是图表中网格线的数量  
默认值为5，最小值不能小于2  
6.1 int tickCount() const
6.2 void setTickCount(int count)

7. tickInterval : qreal
这个属性设置刻度和标签之间的间隔  
备注：这个属性从Qt 5.12版引入  
7.1 qreal tickInterval() const
7.2 void setTickInterval(qreal insterval)

8. tickType : TickType
这个属性设置刻度和标签的放置方法  
备注：这个属性从Qt 5.12版引入  
8.1 QValueAxis::TickType tickType() const
8.2 void setTickType(QValueAxis::TickType type)


## 常用公共函数
1. void QValueAxis::setRange(qreal min, qreal max)


## enum QValueAxis::TickType
这个属性设置刻度和标签的放置方法  
```
Constant					value 	Description
QValueAxis::TicksDynamic	0		
刻度根据开始值tickAnchor和间隔值tickInterval来设置
QValueAxis::TicksFixed		1		
刻度根据坐标轴范围来平均设置，刻度数量通过tickCount来设置
```

