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

* [virtual] QVariant QTableWidgetItem::data(int role) const
返回单元格中的数据，数据类型不同，role的取值也不同  
role的取值详见下面的Qt::ItemDataRole  

* [virtual] void QTableWidgetItem::setData(int role, const QVariant &value)
给QTableWidgetItem对象设置数据，value的数据类型不同，role的取值也不同  
role的取值详见下面的Qt::ItemDataRole  
```
//把一个QColor对象写入到表格的一个单元格中
QVariant v_inner_color(inner_color);
QTableWidgetItem *item = new QTableWidgetItem();
item->setData(Qt::DecorationRole, v_inner_color);
//备注：可以简化写为 item->setData(Qt::DisplayRole, QVariant(inner_color));
channel_table -> setItem(0, 0, item);
```

* void QTableWidgetItem::setFlags(Qt::ItemFlags flags)
给QTableWidgetItem对象设置flag，这决定了单元格是否可以被选中或被修改  
```
//设置某个单元格不可以编辑修改
item -> setFlags(Qt::ItemIsEditable);
channel_table -> setItem(1, 1, item);
```
flags的取值详见下面的Qt::ItemFlags  
备注：Qt::ItemIsEditable在文档中写的是可以被编辑，但实际测试是不可编辑  
备注：如果要设置整个表格不可编辑，用QTableWidget中的setEditTriggers方法  


## enum Qt::ItemDataRole
常用role的取值：  
```
Constant   Value   Description  
//通用角色及相关类型
Qt::DisplayRole   0   用文本形式展示的关键数据(QString)
备注：默认会把Qt::EditRole 和 Qt::DisplayRole当做相同的设置
Qt::DecorationRole   1   用图标的形式显示数据(QColor, QIcon or QPixmap)
备注：显示的颜色在单元格中是一个小方块，不能填满整个单元格
Qt::EditRole   2   可编辑修改的文本数据(QString)
Qt::ToolTipRole   3   实现当鼠标处于选中的数据时，显示出数据的相关提示(QString)
Qt::StatusTipRole   4   在状态栏显示提示的数据(QString)
Qt::WhatsThisRole   5   在"What's This?"模式下会显示出来的数据(QString)
Qt::SizeHintRole   13   可以提示相应大小(QSize)

//描述外观和元数据的角色及相关类型
Qt::FontRole   6   可以改变数据的字体(QFont)
Qt::TextAlignmentRole   7   可以将文本的位置进行居中、居左居右调整(Qt::Alignment)
Qt::BackgroundRole   8   可以改变背景色(QBrush)
备注：显示的颜色会填满整个单元格
Qt::ForegroundRole   9   可以改变前景色(QBrush)
Qt::CheckStateRole   10   设置的列则可以显示出一个CheckBox(Qt::CheckState)
Qt::InitialSortOrderRole   14

//可访问性角色及相关类型
Qt::AccessibleTextRole   11   用于辅助功能和插件扩展的文本(如屏幕阅读器)(QString)
Qt::AccessibleDescriptionRole   12   用于无障碍项目的描述(QString)

//用户角色
Qt::UserRole   0x0100   用于应用程序的特定目的(自己定义用途).用户自己决定使用什么数据,如何处理数据
```


## enum Qt::ItemFlag
常用flag的取值  
```
Constant   Value   Description
Qt::NoItemFlags   0   没有任何属性设置
Qt::ItemIsSelectable   1   可以被选中
Qt::ItemIsEditable   2   可以被编辑（实际测试是不可被编辑）
Qt::ItemIsDragEnabled   4   
Qt::ItemIsDropEnabled   8   
Qt::ItemIsUserCheckable   16   
Qt::ItemIsEnabled   32   
Qt::ItemIsAutoTristate   64   
Qt::ItemNeverHasChildren   128   
Qt::ItemIsUserTristate   256   
```