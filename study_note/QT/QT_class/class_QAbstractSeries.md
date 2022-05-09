# QAbstractSeries

## 基本功能
QAbstractSeries作为Qt图表中的数据来源，是所有图表数据类的基类  
数据在不同类型的图表中有不同的表现形式，例如在曲线图中，数据指的就是曲线本身  
一般用来设置数据组的名字等各种属性，绑定数据组和坐标轴等  
但是不包括向数据组中添加具体的数据点，添加数据点使用QXYSeries  
父类：QObject  
子类：QAbstractBarSeries, QAreaSeries, QBoxPlotSeries, QCandlestickSeries, QPieSeries, and QXYSeries


## 关于图表中每组数据的名称标识
在图表中添加多组数据之后，会自动在图表正上方显示出每组数据的名称，以及一个带颜色的方块
1. 这个标识的名称可以通过QAbstractSeries::setName(const QString &name)方法设置
标识的颜色可以通过QXYSeries::setColor(const QColor &color)方法进行设置  
2. 名称标识的以下特性没有找到可以设置的地方
位置无法设置，只能显示在正上方  
颜色标识的形状无法设置，只能显示为方框  
名称的字体无法设置，只能按默认字体显示  
3. 当图表中有多组曲线时，可能会名称标识显示不下，造成每个名称都显示为...  
由于无法设置字体大小，只能把图表本身尺寸拉大  
备注：实测用QXYSeries::setPointLabelsFont(const QFont &font)方法无法设置这里的字体  


## 构造函数
没有构造函数，QAbstractSeries是抽象基类，不直接使用  


## 常用成员变量
1. name : QString
这个属性设置数据的名字  
这个名字会显示在图表中，作为该组数据的标签，支持HTML格式  
1.1 QString name() const
1.2 void setName(const QString &name)

2. opacity : qreal
这个属性设置数据的透明度  
属性合法范围为0.0(完全透明)-1.0(完全不透明)，默认值为1.0  
2.1 qreal opacity() const
2.2 void setOpacity(qreal opacity)

3. type : const SeriesType
这个属性设置数据的类型  
属性只能读，不能写  
3.1 virtual QAbstractSeries::SeriesType type() const = 0

4. useOpenGL : bool
这个属性设置在图表上渲染描绘数据时是否使用OpenGL进行加速，默认值为false  
这个在文档中有很多具体介绍，用到了再看  
4.1  bool useOpenGL() const
4.2 void setUseOpenGL(bool enable = true)

5. visible : bool
这个属性设置数据是否可见，默认值为true  
5.1 bool isVisible() const
5.2 void setVisible(bool visible = true)


## 常用公共函数
1. bool QAbstractSeries::attachAxis(QAbstractAxis \*axis)
把数据和坐标轴之间进行绑定  
备注：如果同一方向的多个轴被绑定到相同的数据上，这些轴就有相同的最大值和最小值  
注意：如果是x/y坐标轴，则要把数据和x轴、y轴都进行绑定  
```
m_data -> attachAxis(axis_x);
m_data -> attachAxis(axis_y);
```

2. QList<QAbstractAxis \*> QAbstractSeries::attachedAxes()
返回绑定在数据上所有的坐标轴  
一般来说，除了饼状图没有数据轴绑定外，x轴和y轴都是绑定在同一组数据上  

3. bool QAbstractSeries::detachAxis(QAbstractAxis \*axis)
把数据和坐标轴之间进行解绑  

4. void QAbstractSeries::hide()
把数据的可见性设置为false  
备注：好像和setVisible()功能一样  

5. void QAbstractSeries::show()
把数据的可见性设置为true  
备注：好像和setVisible()功能一样  

6. QChart \*QAbstractSeries::chart() const
返回数据所属的图表  
备注：数据添加到图表时就自动绑定，数据从图表删除时就自动解绑  

