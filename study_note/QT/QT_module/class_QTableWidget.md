# QTableWidget

## 基本功能
QTableWidget用来提供数据表格相关的功能  
不管是表头还是工作区，每个单元格的数据都是一个QTableWidgetItem对象  
除非进行设置，表头行和表头列默认都是从1开始递增（注意不是0）  
注意：在进行各种设置时，表头和工作区是分开的，要用不同函数分别进行设置  


## QTableWidget和QTableView的区别
1. 继承关系
QTableWidget是QTableView的子类，即QTableWidget继承于QTableView  
2. 数据模型
QTableView可以使用自定义的数据模型来显示内容  
QTableView事先要通过setModel函数来绑定数据源  
QTableWidget只能使用标准的数据模型，其单元格中的数据是QTableWidgetItem对象  
QTableWidget不需要数据源，逐个将单元格内的信息填好即可  


## QTableWidget中存放的数据类型
QTableWidgetItem对象有一个setData()方法，可以存放QVariant数据  
将要存放的数据类型转换为QVariant，再添加到QTableWidgetItem对象中  
因此QTableWidget中可以存放几乎所有类型的数据  


## 构造函数
1. QTableWidget::QTableWidget(int rows, int columns, QWidget \*parent = nullptr)
使用指定的行数和列数创建一个表格对象  
```
tableWidget = new QTableWidget(12, 3, this);
```
2. QTableWidget::QTableWidget(QWidget \*parent = nullptr)
也可以先创建一个表格对象，随后再指定行数和列数  
```
tableWidget = new QTableWidget(this);
tableWidget->setRowCount(10);
tableWidget->setColumnCount(5);
```


## 常用函数
* int QTableWidget::rowCount() const
返回表格的行数  

* int QTableWidget::columnCount() const
返回表格的列数  

* void QTableWidget::setRowCount(int rows)
设置表格的行数  
```
//给表格增加一行
mytable -> setRowCount(mytable -> rowCount() + 1);
```

* void QTableWidget::setColumnCount(int columns)
设置表格的列数  

* void QTableWidget::setHorizontalHeaderItem(int column, QTableWidgetItem \*item)
对表头行中指定的某个单元格设置数据，没有进行设置的单元格还是默认值  
```
mytable -> setHorizontalHeaderItem(0, new QTableWidgetItem("id"));
mytable -> setHorizontalHeaderItem(1, new QTableWidgetItem("text"));
```

* void QTableWidget::setVerticalHeaderItem(int row, QTableWidgetItem \*item)
对表头列中指定的某个单元格设置数据，没有进行设置的单元格还是默认值  

* void QTableWidget::setHorizontalHeaderLabels(const QStringList &labels)
用QStringList向表头行中多个单元格设置数据，从第一个单元格开始，没有进行设置的单元格还是默认值  
```
QStringList header_list;
header_list << "id" << "text" << "visible" << "flashing" << "color";
mytable -> setHorizontalHeaderLabels(header_list);
```

* void QTableWidget::setVerticalHeaderLabels(const QStringList &labels)
用QStringList向表头列中多个单元格设置数据，从第一个单元格开始，没有进行设置的单元格还是默认值  

* QTableWidgetItem \*QTableWidget::horizontalHeaderItem(int column) const
如果表头行中指定的单元格已经被设置，则返回该单元格中的数据对象  
如果单元格没有提前设置，则返回一个空指针nullptr  
注意：一定要先判断返回值是否为空指针，否则可能会造成一些内存错误  
```
//设置表头行格式
QFont myfont;
myfont.setBold(true);
myfont.setPointSize(12);
for(int header = 0; header < mytable -> columnCount(); header++)
{
    QTableWidgetItem *header_item = mytable -> horizontalHeaderItem(header);
    if(header_item) //判断返回指针是否为空
    {
        header_item -> setFont(myfont);
    }
}
```

* QTableWidgetItem \*QTableWidget::verticalHeaderItem(int row) const
如果表头列中指定的单元格已经被设置，则返回该单元格中的数据对象  
如果单元格没有提前设置，则返回一个空指针nullptr  

* QTableWidgetItem \*QTableWidget::item(int row, int column) const
如果工作区的指定单元格已经被设置，则返回该单元格中的数据对象  
如果单元格没有提前设置，则返回一个空指针nullptr  

* void QTableWidget::setItem(int row, int column, QTableWidgetItem \*item)
向指定的单元格中插入QTableWidgetItem数据  
```
for(int i = 0; i < mytable -> rowCount(); i++)
{
    for (int j = 0; j < mytable -> columnCount(); j++)
    {
        mytable -> setItem(i, j, new QTableWidgetItem(QString::number(i + j + 2)));
    }
}
```

* void QTableWidget::setCellWidget(int row, int column, QWidget \*widget)
向指定的单元格中插入一个widget组件，插入后组件的所有者就变成了表格  
如果单元格中已经插入了一个组件，再插入一个新的组件，则原组件会被删除  
```
//向单元格中添加下拉菜单
for(int i = 0; i < mytable -> rowCount(); i++)
{
    QComboBox *choose_visible;
    choose_visible = new QComboBox(this);
    choose_visible -> addItem("Visible");
    choose_visible -> addItem("HalfVisible");
    choose_visible -> addItem("Invisible");
    mytable -> setCellWidget(i, 2, choose_visible);
}
```

* QWidget \*QTableWidget::cellWidget(int row, int column) const
返回指定单元格中的widget对象  

* [slot] void QTableWidget::insertColumn(int column)
插入表中指定的一列  

* [slot] void QTableWidget::insertRow(int row)
插入表中指定的一行  

* [slot] void QTableWidget::removeColumn(int column)
删除表中指定的一列  

* [slot] void QTableWidget::removeRow(int row)
删除表中指定的一行  


## 信号函数
* [signal] void QTableWidget::cellChanged(int row, int column)
当指定单元格中的数据发生改变时，会触发该信号函数  

* [signal] void QTableWidget::itemChanged(QTableWidgetItem \*item)
当指定item的数据发生改变时，会触发该信号函数  