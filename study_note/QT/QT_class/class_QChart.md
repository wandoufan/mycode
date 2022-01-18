# QChart

## 基本功能
QChart实现图表界面，用来管理图表的内容、颜色、大小等  
QChart是Charts模块中最核心的类  
曲线、折线、条形等不同类型的数据可以显示在同一张图表中  
父类：QGraphicsWidget  
子类：QPolarChart  


## 构造函数
1. QChart::QChart(QGraphicsItem \*parent = nullptr, Qt::WindowFlags wFlags = Qt::WindowFlags())


## 常用成员变量
1. animationDuration : int
这个属性设置图表中动画的持续时间  
1.1 int animationDuration() const  
1.2 void setAnimationDuration(int msecs)  

2. animationEasingCurve : QEasingCurve
这个属性设置图表中动画的缓和曲线  
2.1 QEasingCurve animationEasingCurve() const
2.2 void setAnimationEasingCurve(const QEasingCurve &curve)

3. animationOptions : QChart::AnimationOptions
这个属性设置图表中动画的选项  
通过这个属性可以设置是否使用动画  
3.1 QChart::AnimationOptions animationOptions() const
3.2 void setAnimationOptions(QChart::AnimationOptions options)

4. backgroundRoundness : qreal
这个属性设置图表背景角落的圆圈的直径  
4.1 qreal backgroundRoundness() const
4.2 void setBackgroundRoundness(qreal diameter)

5. backgroundVisible : bool
这个属性设置图表背景是否可见  
5.1 bool isBackgroundVisible() const
5.2 void setBackgroundVisible(bool visible = true)

6. chartType : const QChart::ChartType
这个属性设置图表是用笛卡尔坐标还是极坐标  
这个属性是在内部自动设置的，只能读，不能写  
6.1 QChart::ChartType chartType() const

7. dropShadowEnabled : bool
这个属性设置图表中的阴影效果是否生效  
备注：阴影效果也依赖于图表的主题，当更换主题时，阴影效果也可能改变  
7.1 bool isDropShadowEnabled() const
7.2 void setDropShadowEnabled(bool enabled = true)

8. locale : QLocale
这个属性设置图表中各种标签的位置  
除了QDateTimeAxis标签外，其他的各种标签都是当localizeNumbers为true时才放置  
8.1 QLocale locale() const
8.2 void setLocale(const QLocale &locale)

9. localizeNumbers : bool
这个属性设置是否放置数字  
当属性为true时，所有图表中的数字和标签会被locale : QLocale属性在某个位置  
当属性为false时，使用C locale，默认为false  
备注：这个属性不影响QDateTimeAxis标签，该标签总是使用locale属性设置  
9.1 bool localizeNumbers() const
9.2 void setLocalizeNumbers(bool localize)

10. margins : QMargins
这个属性设置图表矩形边框和图表绘图区域的最小间隙  
10.1 QMargins margins() const
10.2 void setMargins(const QMargins &margins)

11. plotArea : QRectF
这个属性设置图表的矩形边框  
11.1 QRectF plotArea() const
11.2 void setPlotArea(const QRectF &rect)

12. plotAreaBackgroundVisible : bool
这个属性设置图表绘图区域的背景是否可见  
备注：绘图区域的背景默认是不可见的，绘图区域一般会使用图表本身的背景  
12.1 bool isPlotAreaBackgroundVisible() const
12.2  void setPlotAreaBackgroundVisible(bool visible = true)

13. theme : QChart::ChartTheme
这个属性设置图表应用的主题  
13.1 QChart::ChartTheme theme() const
13.2 void setTheme(QChart::ChartTheme theme)

14. title : QString
这个属性设置图表的标题  
标题一般显示在图表正上方，图表标题支持HTML格式  
14.1 QString title() const
14.2 void setTitle(const QString &title)
14.3 void QChart::setTitleBrush(const QBrush &brush)
14.4 void QChart::setTitleFont(const QFont &font)


## 常用公共函数：图表的坐标轴
1. void QChart::addAxis(QAbstractAxis \*axis, Qt::Alignment alignment)
向图表中添加坐标轴，alignment参数指定坐标轴的位置  
添加之后，图表对象会成为坐标轴对象的所有者  
alignment参数取值详见手册，常用的x/y坐标轴的位置如下：  
```
chart -> addAxis(axis_x, Qt::AlignBottom);//添加坐标轴，放置到x轴的位置
chart -> addAxis(axis_y, Qt::AlignLeft);//添加坐标轴，放置到y轴的位置
```

2. void QChart::removeAxis(QAbstractAxis \*axis)
从图表中删除坐标轴  
删除之后，图表对象会释放和坐标轴对象之间的所属关系  

3. void QChart::createDefaultAxes()
在数据添加到图表之后，基于这些数据自动为图表创建对应的坐标轴  
在不想自己创建坐标轴的时候可以用这个函数快速的创建坐标轴  
但是自动创建出来的坐标轴比较简陋，如果需要对坐标轴详细设置，最好还是自己创建坐标轴  
备注：任何之前已经添加到图表的坐标轴会被删掉  
注意：必须把所有数据都添加到图表之后，才能调用这个函数  
在调用这个函数之后，再去添加的新数据不会自动关联到坐标轴上  
添加数据和坐标轴类型之间的关系：  
```
Series type 		Horizontal axis (X)		Vertical axis (Y)
QXYSeries 			QValueAxis 				QValueAxis
QBarSeries 			QBarCategoryAxis 		QValueAxis
QPieSeries 			None 					None
```
如果只向图表中添加一些x/y坐标轴类型的数据，图表中只会出现一组x/y坐标  
如果添加多种不同类型的数据，图表会对应创建不同类型的坐标轴  

4. QList<QAbstractAxis \*> QChart::axes(Qt::Orientations orientation = Qt::Horizontal|Qt::Vertical, QAbstractSeries \*series = nullptr) const
返回图表中指定数据类型对应的坐标轴  
如果没有指定数据类型，返回图表中所有的坐标轴  


## 常用公共函数：图表的数据来源
1. void QChart::addSeries(QAbstractSeries \*series)
向图表中添加数据  
添加之后，图表对象会成为数据对象的所有者  
默认情况下，添加的数据不会自动关联到任何坐标轴上  

2. void QChart::removeSeries(QAbstractSeries \*series)
从图表中删除指定数据  
删除之后，图表对象会释放和数据对象之间的所属关系  

3. void QChart::removeAllSeries()
从图表中删除所有数据  

4. QList<QAbstractSeries \*> QChart::series() const
返回图表中添加的所有数据对象  


## enum QChart::ChartTheme
集合中是Qt图表提供的所有主题  
```
QChart::ChartThemeLight				0	亮色主题(默认)
QChart::ChartThemeBlueCerulean		1	蓝色主题
QChart::ChartThemeDark				2	暗黑主题
QChart::ChartThemeBrownSand			3	沙棕色主题
QChart::ChartThemeBlueNcs			4	自然色主题
QChart::ChartThemeHighContrast		5	高对比度主题
QChart::ChartThemeBlueIcy			6	冰蓝主题
QChart::ChartThemeQt				7	Qt主题
```