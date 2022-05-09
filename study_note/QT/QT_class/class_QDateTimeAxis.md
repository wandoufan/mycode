# QDateTimeAxis

## 基本功能
QDateTimeAxis用来向Qt图表的中添加一个日期时间类型的坐标轴  
在把qreal类型数据定义为float类型数据的操作系统上，不能使用QDateTimeAxis  
父类：QAbstractAxis  
子类：无  


## 关于向时间日期坐标轴中添加数据点
QDateTimeAxis坐标轴可以和任何QXYSeries数据(包括QLineSeries、QSplineSeries)搭配  
以x轴是时间轴为例，使用append()方法添加数据点时，y轴是正常的数值  
但x轴的日期时间要使用QDateTime::toMSecsSinceEpoch()方法转换为毫秒值  
备注：必须用toMSecsSinceEpoch()方法，其他的toSecsSinceEpoch()方法不行  
```
//定义起始时间和结束时间
QDateTime start_time, finish_time;
start_time.setDate(QDate(2022, 5, 7));
start_time.setTime(QTime(11, 0, 0));
finish_time.setDate(QDate(2022, 5, 7));
finish_time.setTime(QTime(11, 30, 0));
//定义时间坐标轴
QDateTimeAxis * axis_x;
axis_x = new QDateTimeAxis;
axis_x -> setTitleText("时间");
axis_x -> setRange(start_time, finish_time);
axis_x -> setFormat("hh:mm:ss");
axis_x -> setTickCount(7);
axis_x -> setLinePenColor(QColor(Qt::black));
//定义数据
QSplineSeries * data1;
data1 = new QSplineSeries;
data1 -> setName("滑油温度");
data1 -> setColor(QColor(Qt::blue));
//添加数据点
data1 -> append(start_time.toMSecsSinceEpoch(), 20);
data1 -> append(finish_time.toMSecsSinceEpoch(), 50);
```


## 构造函数
1. QDateTimeAxis::QDateTimeAxis(QObject \*parent = nullptr)


## 常用成员变量
1. format : QString
这个属性设置坐标轴上日期时间标签的格式  
具体的格式详见QDateTime  
1.1 QString format() const
1.2 void setFormat(QString format)

2. max : QDateTime
这个属性设置坐标轴上的最大值(最晚的日期时间)  
设置这个属性时，如果有必要，最小值会自动调整，以确保时间范围合法  
2.1 QDateTime max() const
2.2 void setMax(QDateTime max)

3. min : QDateTime
这个属性设置坐标轴上的最小值(最早的日期时间)  
设置这个属性时，如果有必要，最大值会自动调整，以确保时间范围合法  
3.1 QDateTime min() const
3.2 void setMin(QDateTime min)

4. tickCount : int
这个属性设置坐标轴上刻度/标签的数量  
4.1 int tickCount() const
4.2 void setTickCount(int count)


## 常用公共函数
1. void QDateTimeAxis::setRange(QDateTime min, QDateTime max)


## 常用信号函数
1. [signal] void QDateTimeAxis::formatChanged(QString format)

2. [signal] void QDateTimeAxis::maxChanged(QDateTime max)

3. [signal] void QDateTimeAxis::minChanged(QDateTime min)

4. [signal] void QDateTimeAxis::rangeChanged(QDateTime min, QDateTime max)

5. [signal] void QDateTimeAxis::tickCountChanged(int tickCount)