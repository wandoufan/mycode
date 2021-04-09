# QTableWidgetItem

## 基本功能
QTableWidgetItem用作QTableWidget表格中单元格的数据对象  
提供了成员函数用来对单元格数据的各种属性进行设置  


## 使用示例
1. 创建实例化对象时可以直接写入一个字符串
```
QTableWidgetItem *myItem;
myItem = new QTableWidgetItem("abc");
```


## 构造函数
1. QTableWidgetItem::QTableWidgetItem(const QIcon &icon, const QString &text, int type = Type)

2. QTableWidgetItem::QTableWidgetItem(const QString &text, int type = Type)

3. QTableWidgetItem::QTableWidgetItem(int type = Type)


## 常用函数
* QTableWidget \*QTableWidgetItem::tableWidget() const
返回一个包含这个item的数据表格  

* [virtual] void QTableWidgetItem::setData(int role, const QVariant &value)
给QTableWidgetItem对象设置数据，value的数据类型不同，role的取值也不同  
role的取值详见下面的Qt::ItemDataRole  
备注：默认会把Qt::EditRole 和 Qt::DisplayRole当做相同的设置  
```
//把一个QColor对象写入到表格的一个单元格中
QVariant v_inner_color(inner_color);
QTableWidgetItem *item = new QTableWidgetItem();
item->setData(Qt::DecorationRole, v_inner_color);
channel_table -> setItem(0, 0, item);
```

* void QTableWidgetItem::setFlags(Qt::ItemFlags flags)
给QTableWidgetItem对象设置flag，这决定了单元格是否可以被选中或被修改  
```
//设置单元格不可以编辑修改
item -> setFlags(Qt::ItemIsEditable);
channel_table -> setItem(1, 1, item);
```
flags的取值详见帮助文档的Qt::ItemFlags  
备注：Qt::ItemIsEditable在文档中写的是可以被编辑，但实际测试是不可编辑  


## enum Qt::ItemDataRole
常用role的取值：  
```
Constant   Value   Description  
Qt::DisplayRole   0   用文本形式展示的关键数据(QString)  
Qt::DecorationRole   1   用图标的形式显示数据(QColor, QIcon or QPixmap)  
Qt::EditRole   2   可修改的数据(QString)  
```
