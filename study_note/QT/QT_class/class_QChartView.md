# QChartView

## 基本功能
QChartView是一个独立运行的widget，可以用来展示图表  
一般用QChart做好的图表都要封装到QChartView中才能变成一个可以显示在UI界面上的控件  
父类： QGraphicsView  


## 构造函数
1. QChartView::QChartView(QChart \*chart, QWidget \*parent = nullptr)
在创建QChartView对象时直接添加QChart对象  

2. QChartView::QChartView(QWidget \*parent = nullptr)
先创建一个空的QChartView对象，之后再用setChar()方法添加QChart对象  


## 常用公共函数
1. void QChartView::setChart(QChart \*chart)
添加QChart对象  

2. QChart \*QChartView::chart() const
返回包含的QChart对象  

