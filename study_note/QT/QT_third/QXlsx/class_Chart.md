# Chart

## 基本功能
用来绘制各种图表：饼状图、柱状图、折线图等  
```
#include "xlsxchart.h"
```


## 说明
QXlsx提供的Chart功能过于简单，没有设置图表x/y轴单位和含义的接口，也不能标注每根折线的含义  
如果需要实现图表功能，使用Qt的charts模块  


## 代码示例
```
Chart *chart;
chart = xlsx.insertChart(1, 1, QSize(300, 300));
chart -> setChartType(Chart::CT_Area);
chart -> addSeries("A1:A9");
```


## 构造函数
Chart类没有构造函数，一般通过Document的insertChart方法获得一个Chart对象指针  
备注：先获取这个Chart指针，再进一步设置图表的数据
```
Chart *chart;
chart = xlsx.insertChart(3, 3, QSize(300, 300));
```


## 常用公共函数
1. void addSeries(const CellRange &range, AbstractSheet \*sheet = 0);
获取图表中的数据来源，range默认为当前工作表中的单元格范围  
```
chart -> addSeries("A1:A9");
```
sheet参数可以从指定工作表中读取单元格的数据  
```
AbstractSheet *sheet_data;
sheet_data = xlsx.sheet("sheet_data");
chart -> addSeries("A1:A9", sheet_data);
```

2. void setChartType(ChartType type);
设置图表类型，详见enum Chart::ChartType  
```
chart -> setChartType(Chart::CT_Area);
```

3. void setChartStyle(int id);

4. void saveToXmlFile(QIODevice \*device) const;

5. bool loadFromXmlFile(QIODevice \*device);


## enum Chart::ChartType
```
Constant				Value	Description
Chart::CT_Area			1		曲线面积图
Chart::CT_Area3D		2		3D版曲线面积图
Chart::CT_Line			3		折线图
Chart::CT_Line3D		4		3D折线图
Chart::CT_Scatter		7		也是折线图，但数值经过了分散处理(一般用不上)
Chart::CT_Pie			8		饼状图
Chart::CT_Pie3D			9		3D饼状图
Chart::CT_Doughnut		10		环形图
Chart::CT_Bar			11		柱状图
Chart::CT_Bar3D			12		3D柱状图
```
另外，集合中还包括如下取值，但实测不可用，会导致表格文件无法正常打开
```
CT_Stock,
CT_Radar,
CT_OfPie,
CT_Surface,
CT_Surface3D,
CT_Bubble
```