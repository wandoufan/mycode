# Qt中绘制图表

## Charts模块简介
Charts模块提供了一系列可以实现图表功能的的组件  
它基于Qt Graphics View Framework实现，因此图表可以融合到用户接口中  
Qt Charts可以用作QWidgets、QGraphicsWidget或QML types  


## Charts模块使用
1. 如果要导入Qt Charts QML类型，需要在.qml文件中添加
```
import QtCharts 2.15
```
2. 如果要在程序中使用Charts模块中的C++类，需要在代码中添加
```
#include <QtCharts>
using namespace QtCharts;
```
3. 在Qt Widgets Application中使用QChart
需要在.pro文件中添加  
```
QT += charts
```
4. 在Qt Quick Application中使用QChart
使用Qt Creator的Qt Quick Application模板创建的项目是基于Qt Quick 2，默认使用的是QGuiApplication  
项目中所有的QGuiApplication实例必须被替换成QApplication  
因为Charts模块基于Qt Graphics View Framework实现的  
为了正确链接Charts模块，需要在.pro文件中添加  
```
QT += charts
```
5. 在Qt Console Application中使用QChart
经过反复尝试都失败了，在.pro文件中添加了各种内容都还是不行  
在程序编译时会报错'程序异常结束'，报错的地方就是QChart类定义的行  
最后只能改用Qt Widgets Application模板，把界面显示的行给注释掉  


## Charts模块支持的图表类型
备注：在帮助手册中搜索"Qt Charts Overview"  
曲线、折线、条形等不同类型的数据可以显示在同一张图表中  
```
折线图			Line charts
曲线图			spline charts
折线面积图		Area charts
点状图			scatter charts
条形图			Bar charts
饼状图			Pie charts
方块胡须图		Box-and-whiskers charts
蜡烛图			Candlestick charts
极坐标图			Polar charts
```


## Charts模块支持的坐标轴类型
备注：在帮助手册中搜索"Qt Charts Overview"  
```
值坐标轴			Value axis
类别坐标轴		Category axis
条形类别坐标轴	Bar category axis
日期时间坐标轴	Date-time axis
对数值坐标轴		Logarithmic value axis
```


## Charts模块支持的图表主题
备注：在帮助手册中搜索"Qt Charts Overview"  
主题是Qt已经预定义好的UI风格，包括颜色、笔画、字体、坐标轴、标题等元素  
这些主题的元素可以进行自定义设置(具体方法不知道)  
也可以通过修改Qt Charts源码来添加一个新的主题  
```
亮色主题			Light theme(默认)
蓝色主题			Cerulean blue theme
暗黑主题			Dark theme
沙棕色主题		Sand brown theme
自然色主题		Natural color system (NCS) blue theme
高对比度主题		High contrast theme
冰蓝主题			Icy blue theme
Qt主题			Qt theme
```


## 官方提供的图表代码示例
备注：在帮助手册中搜索"Qt Charts Examples"


## Charts模块中类的继承关系
1. 图表中的数据
QLineSeries和QSplineSeries虽然很常用，但几乎没有提供函数接口，只用来生成对象  
常用的函数都来自其基类QAbstractSeries和QXYSeries  
```
QObject - QAbstractSeries - QXYSeries - QLineSeries - QSplineSeries
									  - QScatterSeries
						  - QAbstractBarSeries
						  - QAreaSeries
						  - QBoxPlotSeries
						  - QCandlestickSeries
						  - QPieSeries
```
2. 图表中的坐标轴
```
QObject - QAbstractAxis - QValueAxis - QCategoryAxis
						- QBarCategoryAxis
						- QDateTimeAxis
						- QLogValueAxis
```


## 画一个曲线示波图用到的类
1. QChart
2. QChartView
3. QAbstractSeries
4. QXYSeries
5. QSplineSeries
6. QAbstractAxis
7. QValueAxis


## Charts模块中的所有类
1. QAbstractAxis
特殊坐标轴类的基类
Base class used for specialized axis classes

2. QAbstractBarSeries
所有条形图类的抽象基类
Abstract parent class for all bar series classes

3. QAbstractSeries
所有Qt图表数据类的基类
Base class for all Qt Chart series

4. QAreaLegendMarker
在折线面积图中添加标注功能
Legend marker for an area series

5. QAreaSeries
在折线面积图中显示的数据
Presents data in area charts

6. QBarCategoryAxis
向图表的坐标轴添加类别
Adds categories to a chart's axes

7. QBarLegendMarker
在条形图中添加标注功能
Legend marker for a bar series

8. QBarSeries
在垂直条形图中显示的数据
把一些系列数据按类别分组，用垂直条的形式显示出来
Presents a series of data as vertical bars grouped by category

9. QBarSet
表示条形图中的一组条形
Represents one set of bars in a bar chart

10. QBoxPlotLegendMarker
Legend marker for a box plot series

11. QBoxPlotSeries
Presents data in box-and-whiskers charts

12. QBoxSet
Represents one item in a box-and-whiskers chart

13. QCandlestickLegendMarker
Legend marker for a candlestick series

14. QCandlestickModelMapper
Abstract model mapper class for candlestick series

15. QCandlestickSeries
在蜡烛图中显示的数据
Presents data as candlesticks

16. QCandlestickSet
Represents a single candlestick item in a candlestick chart

17. QCategoryAxis
Places named ranges on the axis

18. QChart
Manages the graphical representation of the chart's series, legends, and axes

19. QChartView
Standalone widget that can display charts

20. QDateTimeAxis
向图表的坐标轴中添加日期和时间
Adds dates and times to a chart's axis

21. QHBarModelMapper
Horizontal model mapper for bar series

22. QHBoxPlotModelMapper
Horizontal model mapper for box plot series

23. QHCandlestickModelMapper
Horizontal model mapper for a candlestick series

24. QHPieModelMapper
Horizontal model mapper for pie series

25. QHXYModelMapper
Horizontal model mapper for line, spline, and scatter series

26. QHorizontalBarSeries
在水平条形图中显示的数据
把一些系列数据按类别分组，用水平条的形式显示出来
Presents a series of data as horizontal bars grouped by category

27. QHorizontalPercentBarSeries
Presents a series of categorized data as a percentage of each category

28. QHorizontalStackedBarSeries
Presents a series of data as horizontally stacked bars, with one bar per category

29. QLegend
Displays the legend of a chart

30. QLegendMarker
Abstract object that can be used to access markers within a legend

31. QLineSeries
在折线图中显示的数据
Presents data in line charts

32. QLogValueAxis
Adds a logarithmic scale to a chart's axis

33. QPercentBarSeries
Presents a series of categorized data as a percentage of each category

34. QPieLegendMarker
Legend marker for a pie series

35. QPieSeries
在饼状图中显示的数据
Presents data in pie charts

36. QPieSlice
Represents a single slice in a pie series

37. QPolarChart
Presents data in polar charts

38. QScatterSeries
在点状图中显示的数据
Presents data in scatter charts

39. QSplineSeries
在曲线图中显示的数据
Presents data as spline charts

40. QStackedBarSeries
Presents a series of data as vertically stacked bars, with one bar per category

41. QVBarModelMapper
Vertical model mapper for bar series

42. QVBoxPlotModelMapper
Vertical model mapper for box plot series

43. QVCandlestickModelMapper
Vertical model mapper for a candlestick series

44. QVPieModelMapper
Vertical model mapper for pie series

45. QVXYModelMapper
Vertical model mapper for line, spline, and scatter series

46. QValueAxis
Adds values to a chart's axes

47. QXYLegendMarker
Legend marker for a line, spline, or scatter series

48. QXYSeries
x/y坐标轴类型的数据的基类，子类包括QLineSeries、QSplineSeries、QScatterSeries
Base class for line, spline, and scatter series


-------------------------------------------------------------

## 代码示例
1. 画曲线示波图，使用createDefaultAxes()函数自动创建的坐标轴
```
//定义变量
QChart * m_chart;
QChartView * m_chartview;
QSplineSeries * m_data1, * m_data2;
//初始化图表数据
m_data1 = new QSplineSeries();
m_data2 = new QSplineSeries();
m_data1 -> setName("滑油温度");
m_data2 -> setName("环境温度");
m_data1 -> setColor(QColor(Qt::blue));
m_data2 -> setColor(QColor(Qt::green));
for(int i = 0; i < 100; i ++)
{
    m_data1 -> append(i, 2 * i);
    m_data2 -> append(i, i);
}
//初始化图表
m_chart = new QChart();
m_chart -> setTitle("环境&油温 / ambient*oilsump");
//图表中添加数据
m_chart -> addSeries(m_data1);
m_chart -> addSeries(m_data2);
//自动创建坐标轴
m_chart -> createDefaultAxes();
//初始化图表显示控件
m_chartview = new QChartView(m_chart);
//setRenderHint()函数来自于父类QGraphicsView，具体功能还没搞清楚，但加上之后画出来的线更好看一些
m_chartview -> setRenderHint(QPainter::Antialiasing);
```

2. 画曲线示波图，使用自己定义的的坐标轴
```
//定义变量
QChart * m_chart;
QChartView * m_chartview;
QSplineSeries * m_data1, * m_data2;
QValueAxis * m_axis1, * m_axis2;
//初始化图表数据
m_data1 = new QSplineSeries();
m_data2 = new QSplineSeries();
m_data1 -> setName("滑油温度");
m_data2 -> setName("环境温度");
m_data1 -> setColor(QColor(Qt::blue));
m_data2 -> setColor(QColor(Qt::green));
for(int i = 0; i < 100; i ++)
{
    m_data1 -> append(i, 2 * i);
    m_data2 -> append(i, i);
}
//初始化图表坐标轴
m_axis1 = new QValueAxis();
m_axis2 = new QValueAxis();
m_axis1 -> setTitleText("x轴:时间");
m_axis2 -> setTitleText("y轴:温度");
m_axis1 -> setRange(0, 150);
m_axis2 -> setRange(0, 250);
m_axis1 -> setTickCount(6);
m_axis2 -> setTickCount(6);
m_axis1 -> setMinorTickCount(2);
m_axis2 -> setMinorTickCount(1);
//初始化图表，向图表中添加数据和坐标轴
m_chart = new QChart();
m_chart -> setTitle("环境&油温 / ambient*oilsump");
m_chart -> setTitleFont(QFont("SimSun", 10, 80, false));
m_chart -> addAxis(m_axis1, Qt::AlignBottom);//添加坐标轴，放置到x轴的位置
m_chart -> addAxis(m_axis2, Qt::AlignLeft);//添加坐标轴，放置到y轴的位置
m_chart -> addSeries(m_data1);
m_chart -> addSeries(m_data2);
//将数据和坐标轴绑定
m_data1 -> attachAxis(m_axis1);
m_data1 -> attachAxis(m_axis2);
m_data2 -> attachAxis(m_axis1);
m_data2 -> attachAxis(m_axis2);
//设置图表主题
//    m_chart -> setTheme(QChart::ChartThemeBlueCerulean);
//    m_chart -> setTheme(QChart::ChartThemeDark);
//    m_chart -> setTheme(QChart::ChartThemeBrownSand);
//    m_chart -> setTheme(QChart::ChartThemeBlueNcs);
//    m_chart -> setTheme(QChart::ChartThemeHighContrast);
//    m_chart -> setTheme(QChart::ChartThemeBlueIcy);
//    m_chart -> setTheme(QChart::ChartThemeQt);
//初始化图表显示控件
m_chartview = new QChartView(m_chart);
//setRenderHint()函数来自于父类QGraphicsView，具体功能还没搞清楚，但加上之后画出来的线更好看一些
m_chartview -> setRenderHint(QPainter::Antialiasing);
```

3. 把QChart转换成QImage，并保存为图片格式的文件
```
//初始化图表显示控件
m_chartview = new QChartView(m_chart);
//setRenderHint()函数来自于父类QGraphicsView，具体功能还没搞清楚，但加上之后画出来的线更好看一些
m_chartview -> setRenderHint(QPainter::Antialiasing);
//把图表保存成图片格式文件
QPixmap pixmap = m_chartview -> grab();
QImage image = pixmap.toImage();
image.save("D:/chart.png");
```

4. 调整QChart的大小
在不调整大小的情况下，生成的图片默认为(640, 480)  
实际测试，调用Chart自带的zoom()函数之后，显示出来的图表大小并没有变化，生成的图片大小也没有变化  
目前测试，使用QWidget的resize()函数调整大小是有效的，生成图片文件的大小也会随之改变  
使用QImage的函数来调整图片文件大小应该也可以，但还没有进行具体测试  
```
m_chartview = new QChartView(m_chart);
m_chartview -> resize(480, 360);//通过widget来调整图表大小
```