# QTableView

## 基本功能
QTableView提供一个基于Model/View(模型/视图)架构的二维数据表格  
具体可以参见QT_Model_View.md  


## QTableWidget和QTableView的区别
1. 继承关系
QTableWidget是QTableView的子类，即QTableWidget继承于QTableView  
2. 单元格的数据类型
QTableView可以使用自定义的数据模型来显示内容  
QTableWidget只能使用标准的数据类型，其单元格中的数据是QTableWidgetItem对象  
3. 单元格的数据源
QTableView事先要通过setModel函数来绑定数据源  
QTableWidget不需要数据源，逐个将单元格内的信息填好即可  


## 备注：
这个类里的方法很复杂，另外还和QHeaderView有关系，晚点有时间再总结