# QTableWidget

## 基本功能
QTableWidget用来提供数据表格相关的功能，它是QTableView的便利类  
不管是表头还是工作区，每个单元格的数据都是一个QTableWidgetItem对象  
除非进行设置，表头行和表头列默认都是从1开始递增（注意不是0）  
注意：在进行各种设置时，表头(行/列)和工作区是分开的，要用不同函数分别进行设置  
```
                                                             | - QListView - QListWidget
                                                             | - QTableView - QTableWidget
QWidget - QFrame - QAbstractScrollArea - QAbstractItemView - | - QTreeView - QTreeWidget
                                                             | - QColumnView
                                                             | - QHeaderView                 
```


## 工作区中可以存放的数据类型
1. QTableWidgetItem
QTableWidgetItem对象有一个setData()方法，可以存放QVariant数据  
将要存放的数据类型转换为QVariant，再添加到QTableWidgetItem对象中  
因此QTableWidget中可以存放几乎所有类型的数据  
2. QWidget
可以直接插入一个widget控件


## 关于设置表格样式
在QTableWidget中并没有提供设置单元格样式相关的函数，但父类QTableView中有一些方法可以设置表格样式
另外，通过其父类QTableView的horizontalHeader()方法和verticalHeader()方法，可以获取一个QHeaderView指针
在QHeaderView类中提供了大量设置表格样式的接口


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
tableWidget -> setRowCount(10);
tableWidget -> setColumnCount(5);
```


## 常用公共函数：获取表格中的信息
1. int QTableWidget::rowCount() const
返回表格的行数，对于空表格，默认值为0  

2. int QTableWidget::columnCount() const
返回表格的列数，对于空表格，默认值为0  

3. int QTableWidget::row(const QTableWidgetItem \*item) const

4. int QTableWidget::column(const QTableWidgetItem \*item) const


## 常用公共函数：设置表格的行数和列数
1. void QTableWidget::setRowCount(int rows)
设置表格的行数  

2. void QTableWidget::setColumnCount(int columns)
设置表格的列数  


## 常用公共函数：设置当前选中单元格
1. void QTableWidget::setCurrentCell(int row, int column)

2. void QTableWidget::setCurrentCell(int row, int column, QItemSelectionModel::SelectionFlags command)

3. void QTableWidget::setCurrentItem(QTableWidgetItem \*item)

4. void QTableWidget::setCurrentItem(QTableWidgetItem \*item, QItemSelectionModel::SelectionFlags command)


## 常用公共函数：获取当前选中单元格
1. int QTableWidget::currentRow() const

2. int QTableWidget::currentColumn() const

3. QTableWidgetItem \*QTableWidget::currentItem() const

4. QList<QTableWidgetItem \*> QTableWidget::selectedItems() const


## 常用公共函数：设置表头行/列的数据
1. void QTableWidget::setHorizontalHeaderItem(int column, QTableWidgetItem \*item)
对表头行中指定的某个单元格设置数据，没有进行设置的单元格还是默认值  
```
mytable -> setHorizontalHeaderItem(0, new QTableWidgetItem("id"));
mytable -> setHorizontalHeaderItem(1, new QTableWidgetItem("text"));
```

2. void QTableWidget::setVerticalHeaderItem(int row, QTableWidgetItem \*item)
对表头列中指定的某个单元格设置数据，没有进行设置的单元格还是默认值  

3. void QTableWidget::setHorizontalHeaderLabels(const QStringList &labels)
用QStringList向表头行中多个单元格设置数据，从第一个单元格开始，没有进行设置的单元格还是默认值  
```
QStringList header_list;
header_list << "id" << "text" << "visible" << "flashing" << "color";
mytable -> setHorizontalHeaderLabels(header_list);
```

4. void QTableWidget::setVerticalHeaderLabels(const QStringList &labels)
用QStringList向表头列中多个单元格设置数据，从第一个单元格开始，没有进行设置的单元格还是默认值  


## 常用公共函数：获取表头行/列的数据
1. QTableWidgetItem \*QTableWidget::horizontalHeaderItem(int column) const
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

2. QTableWidgetItem \*QTableWidget::verticalHeaderItem(int row) const
如果表头列中指定的单元格已经被设置，则返回该单元格中的数据对象  
如果单元格没有提前设置，则返回一个空指针nullptr  
注意：一定要先判断返回值是否为空指针，否则可能会造成一些内存错误  


## 常用公共函数：删除表头行/列的数据
1. QTableWidgetItem \*QTableWidget::takeHorizontalHeaderItem(int column)

2. QTableWidgetItem \*QTableWidget::takeVerticalHeaderItem(int row)


## 常用公共函数：设置工作区的数据
1. void QTableWidget::setItem(int row, int column, QTableWidgetItem \*item)
向指定的单元格中插入QTableWidgetItem数据  
```
//例1：把数据类型从QVariant转换成QString，然后放入单元格中
query.exec("select * from load_all;");
while(query.next())
{
    //插入新的一行
    int row = table_all -> rowCount();
    table_all -> insertRow(row);
    //插入数据
    table_all -> setItem(row, 0, new QTableWidgetItem(query.value(0).toString()));
    table_all -> setItem(row, 1, new QTableWidgetItem(query.value(1).toString()));
    table_all -> setItem(row, 2, new QTableWidgetItem(query.value(2).toString()));
    table_all -> setItem(row, 3, new QTableWidgetItem(query.value(3).toString()));
}
//例2：把数据类型保持为QVariant，然后放入单元格中(需要定义多个QTableWidgetItem指针)
while(query.next())
{
    //插入新的一行
    int row = table_all -> rowCount();
    table_all -> insertRow(row);
    //插入数据
    QTableWidgetItem *item0 = new QTableWidgetItem;
    item0-> setData(Qt::DisplayRole, query.value(0));
    table_all -> setItem(row, 0, item0);
    QTableWidgetItem *item1 = new QTableWidgetItem;
    item1-> setData(Qt::DisplayRole, query.value(1));
    table_all -> setItem(row, 1, item1);
    QTableWidgetItem *item2 = new QTableWidgetItem;
    item2-> setData(Qt::DisplayRole, query.value(2));
    table_all -> setItem(row, 2, item2);
    QTableWidgetItem *item3 = new QTableWidgetItem;
    item3-> setData(Qt::DisplayRole, query.value(3));
    table_all -> setItem(row, 3, item3);
}
```

2. void QTableWidget::setCellWidget(int row, int column, QWidget \*widget)
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


## 常用公共函数：获取工作区的数据
1. QTableWidgetItem \*QTableWidget::item(int row, int column) const
如果工作区的指定单元格已经被设置，则返回该单元格中的数据对象  
如果单元格没有提前设置，则返回一个空指针nullptr  

2. QWidget \*QTableWidget::cellWidget(int row, int column) const
返回指定单元格中的widget对象  

3. QList<QTableWidgetItem \*> QTableWidget::findItems(const QString &text, Qt::MatchFlags flags) const
获取所有匹配了text的单元格  

4. QTableWidgetItem \*QTableWidget::itemAt(const QPoint &point) const
根据指定位置获取单元格  

5. QTableWidgetItem \*QTableWidget::itemAt(int ax, int ay) const
根据指定位置获取单元格  


## 常用公共函数：删除工作区的数据
1. QTableWidgetItem \*QTableWidget::takeItem(int row, int column)

2. void QTableWidget::removeCellWidget(int row, int column)
删除单元格中插入的widget组件


## 公共槽函数：增加/删除表格中的行/列，删除所有数据
1. [slot] void QTableWidget::insertColumn(int column)
向指定位置插入新的一列  

2. [slot] void QTableWidget::insertRow(int row)
向指定位置插入新的一行  
```
channel_table -> insertRow(channel_table -> currentRow()); \\上插入一行
channel_table -> insertRow(channel_table -> currentRow() + 1); \\下插入一行
```
注意：对于一张空表格，其rowCount()为0，插入第一行时只能是上插入
```
//错误写法，无法实现插入一行的效果
table -> insertRow(table -> rowCount() + 1);
```

3. [slot] void QTableWidget::removeColumn(int column)
删除表中指定的一列  

4. [slot] void QTableWidget::removeRow(int row)
删除表中指定的一行  

5. [slot] void QTableWidget::clear()
删除视野中所有的单元格数据，这个方法会删除所有的选中区域和表头  
备注：如果不想删除表头，使用QTableWidget::clearContents()方法  

6. [slot] void QTableWidget::clearContents()
删除视野中所有的单元格数据，只删除选中区域，不删除表头  


## 信号函数
1. [signal] void QTableWidget::cellChanged(int row, int column)
当指定单元格中的数据发生改变时，会触发该信号函数  

2. [signal] void QTableWidget::itemChanged(QTableWidgetItem \*item)
当指定item的数据发生改变时，会触发该信号函数  

3. [signal] void QTableWidget::cellPressed(int row, int column)
当按下某个单元格时会触发该信号函数  

4. [signal] void QTableWidget::itemPressed(QTableWidgetItem \*item)
当按下某个单元格时会触发该信号函数  

5. [signal] void QTableWidget::cellClicked(int row, int column)
当左键单击单元格时，会触发该信号函数  

6. [signal] void QTableWidget::itemClicked(QTableWidgetItem \*item)
当左键单击单元格时，会触发该信号函数  

7. [signal] void QTableWidget::cellDoubleClicked(int row, int column)
当双击单元格时，会触发该信号函数  

8. [signal] void QTableWidget::itemDoubleClicked(QTableWidgetItem \*item)
当双击单元格时，会触发该信号函数  

9. [signal] void QTableWidget::currentCellChanged(int currentRow, int currentColumn, int previousRow, int previousColumn)
当前选中单元格发生变化时，会触发该信号函数  
信号函数会提供之前的选中单元格和当前的选中单元格的行列号  

10. [signal] void QTableWidget::currentItemChanged(QTableWidgetItem \*current, QTableWidgetItem \*previous)
当前选中单元格发生变化时，会触发该信号函数  
信号函数会提供之前的选中单元格和当前的选中单元格对应的QTableWidgetItem  

----------------------------------------------------


## 设置表格样式相关的函数示例
* void setEditTriggers(QAbstractItemView::EditTriggers triggers)
设置整个表格为不可编辑  
```
mytable -> setEditTriggers(QAbstractItemView::NoEditTriggers);
```
备注：如果要设置某个单元格不可编辑，使用QTableWidgetItem::setFlags()方法  

* void setSelectionBehavior(QAbstractItemView::SelectionBehavior behavior)
设置一次选中一整行，默认情况下是一次选中一个单元格  
```
mytable -> setSelectionBehavior(QAbstractItemView::SelectRows);
```

* 设置隐藏网格线，默认情况下会显示网格线
```
mytable -> setShowGrid(false);
```

* 设置隐藏整个表格的边框线，默认情况下会显示边框线
```
mytable->setFrameShape(QFrame::NoFrame);
```

* 设置允许一次选中多行(ctrl、shift、ctrl + A)
```
mytable -> setSelectionMode(QAbstractItemView::ExtendedSelection);
```

* 设置选中行的显示颜色
```
mytable -> setStyleSheet("selection-background-color:lightblue;");
```

* 设置表头行的显示颜色
```
channel_table -> horizontalHeader() -> setStyleSheet("QHeaderView::section{background:skyblue;}");
```

* 设置填充满整个表格
```
mytable -> horizontalHeader() -> setStretchLastSection(true);
```

* 设置隐藏表头列
```
mytable -> verticalHeader() -> setVisible(false);
```

* 设置表头行的高度
```
mytable -> horizontalHeader() -> setFixedHeight(100);
```

* 设置表头行第1列的宽度为150
```
mytable -> horizontalHeader() -> resizeSection(0,150);
```

* 设置工作区每行的高度
```
mytable -> verticalHeader() -> setDefaultSectionSize(10);
```

* 设置每列的宽度自动调整
默认情况下可以手动调整每列的宽度，设置之后宽度就不能手动调整了  
```
mytable -> horizontalHeader() -> setSectionResizeMode(QHeaderView::Stretch);
```


----------------------------------------------------

## 代码示例：通过右键菜单插入/删除一行数据
参考QMenu，创建右键菜单选项  
```
//创建菜单和菜单选项
channel_menu = new QMenu(channel_table);
add_channel = new QAction("add channel", this);
channel_menu -> addAction(add_channel);

//设置点击菜单选项时关联的动作
connect(add_channel, SIGNAL(triggered()), this, SLOT(addChannel()));

//右键即可出现菜单
channel_table -> setContextMenuPolicy(Qt::CustomContextMenu);
connect(channel_table, &QTableWidget::customContextMenuRequested, [=]()
{
    channel_menu -> exec(QCursor::pos());
});
```
QTableWidget类本身不提供鼠标右键的信号函数，所以没办法直接感知右键点击了某一个单元格  
因此使用currentRow()函数来获取当前鼠标对应单元格的行号  
```
void Widget::addChannel()
{
    //向下插入一个新通道
    channel_table -> insertRow(channel_table -> currentRow() + 1);
}
```


## 代码示例：实现一行数据的上下移动
1. 基本思路
QTableWidget中没有直接提供接口实现该功能，只能自己写代码去实现  
先在目标位置新插入一个空行，然后将原有行的单元格逐个复制到新行中，最后删除原有数据行  
2. 代码示例
```
void ChannelTable::moveUp()
{
    //当前行向上移动一行
    if(channel_table -> rowCount() == 0)
        QMessageBox::about(NULL, "Note", "you need add a channel first");
    else
        this -> moveRow(channel_table -> currentRow(), channel_table -> currentRow() - 1);
}

void ChannelTable::moveDown()
{
    //当前行向下移动一行
    if(channel_table -> rowCount() == 0)
        QMessageBox::about(NULL, "Note", "you need add a channel first");
    else
        this -> moveRow(channel_table -> currentRow(), channel_table -> currentRow() + 1);
}

void ChannelTable::moveRow(int from_row, int to_row)
{
    //把from_row行的数据移动到to_row行
    if(from_row == to_row)
        return;
    if(from_row < 0 || to_row < 0)
        return;
    if(from_row >= channel_table -> rowCount() || to_row >= channel_table -> rowCount())
        return;
    if(from_row > to_row)
    {
        channel_table -> insertRow(to_row);
        this -> copyRow(from_row + 1, to_row);
        channel_table -> removeRow(from_row + 1);
    }
    if(from_row < to_row)
    {
        channel_table -> insertRow(to_row + 1);
        this -> copyRow(from_row, to_row + 1);
        channel_table -> removeRow(from_row);
    }
}

void ChannelTable::copyRow(int from_row, int to_row)
{
    //把from_row行的数据拷贝到to_row行
    for(int column = 0; column < channel_table -> columnCount(); column++)
    {
        QTableWidgetItem *item_temp = channel_table -> item(from_row, column);
        if(item_temp)
            channel_table -> setItem(to_row, column, item_temp -> clone());
    }
}
```