# QTableWidget

## 基本功能
QTableWidget用来提供数据表格相关的功能  
不管是表头还是工作区，每个单元格的数据都是一个QTableWidgetItem对象  
除非进行设置，表头行和表头列默认都是从1开始递增（注意不是0）  
注意：在进行各种设置时，表头(行/列)和工作区是分开的，要用不同函数分别进行设置  


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
tableWidget -> setRowCount(10);
tableWidget -> setColumnCount(5);
```


## 常用函数
* int QTableWidget::currentRow() const
返回当前选择单元格的行数  
可以自动识别鼠标所在位置，不需要提供其他参数，非常方便  

* int QTableWidget::currentColumn() const
返回当前选择单元格的列数  
可以自动识别鼠标所在位置，不需要提供其他参数，非常方便  

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

* [slot] void QTableWidget::insertColumn(int column)
插入表中指定的一列  

* [slot] void QTableWidget::insertRow(int row)
插入表中指定的一行  
```
channel_table -> insertRow(channel_table -> currentRow()); \\上插入一行
channel_table -> insertRow(channel_table -> currentRow() + 1); \\下插入一行
```

* [slot] void QTableWidget::removeColumn(int column)
删除表中指定的一列  

* [slot] void QTableWidget::removeRow(int row)
删除表中指定的一行  

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


## 设置表格样式相关的函数
备注：以下函数在QTableWidget类中并没有找到(属于公共函数)，但实际测试有效  

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


## 设置单元格宽和高相关的函数
注意：使用horizontalHeader()和verticalHeader()需要#include <QHeaderView>  

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


## 信号函数
* [signal] void QTableWidget::cellChanged(int row, int column)
当指定单元格中的数据发生改变时，会触发该信号函数  

* [signal] void QTableWidget::cellClicked(int row, int column)
当左键单击单元格时，会触发该信号函数  

* [signal] void QTableWidget::cellDoubleClicked(int row, int column)
当双击单元格时，会触发该信号函数  

* [signal] void QTableWidget::itemChanged(QTableWidgetItem \*item)
当指定item的数据发生改变时，会触发该信号函数  


## 通过右键菜单插入/删除一行数据
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


## 实现一行数据的上下移动
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