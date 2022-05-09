# QTableWidgetItem

## 基本功能
QTableWidgetItem用作QTableWidget表格中单元格的数据对象  
提供了成员函数用来对单元格数据的各种属性进行设置  
父类：无  
子类：无  


## 使用示例
1. 创建实例化对象时可以直接写入一个字符串
```
QTableWidgetItem *myItem;
myItem = new QTableWidgetItem("abc");
```


## 复制一个QTableWidgetItem
有时候需要把一个单元格中内容复制到另外一个单元格里  
如果先读出原单元格item中的QVariant，再读出QVariant中对应的数据，然后再将这个数据重新写入新单元格的item中  
这样操作会很麻烦，而且需要事先知道每个单元格中存储的数据类型  
可以直接把原单元格的item复制为新单元格的item  
```
for(int column = 0; column < channel_table -> columnCount(); column++)
{
    QTableWidgetItem *item_temp = channel_table -> item(from_row, column);//读出原有单元格的item
    if(item_temp)
        //注意：这里一定要写"item_temp -> clone()"，不能写成"item_temp"，否则无效
        channel_table -> setItem(to_row, column, item_temp -> clone());//向新单元格插入item
}
```


## 构造函数
1. QTableWidgetItem::QTableWidgetItem(const QIcon &icon, const QString &text, int type = Type)

2. QTableWidgetItem::QTableWidgetItem(const QString &text, int type = Type)

3. QTableWidgetItem::QTableWidgetItem(int type = Type)

4. QTableWidgetItem::QTableWidgetItem(const QTableWidgetItem &other)
直接复制其他的QTableWidgetItem  


## 常用公共函数
* QTableWidget \*QTableWidgetItem::tableWidget() const
返回一个包含这个item的数据表格  

* [virtual] QVariant QTableWidgetItem::data(int role) const
返回单元格中的数据，数据类型不同，role的取值也不同  
role的取值详见下面的Qt::ItemDataRole  

* [virtual] void QTableWidgetItem::setData(int role, const QVariant &value)
给QTableWidgetItem对象设置数据，value的数据类型不同，role的取值也不同  
role的取值详见namespace中的Qt::ItemDataRole  
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
flags的取值详见namespace中的Qt::ItemFlags  
```
//设置某个单元格不可以编辑修改
item -> setFlags(Qt::ItemIsEditable);
channel_table -> setItem(1, 1, item);
```
备注：Qt::ItemIsEditable在文档中写的是可以被编辑，但实际测试是不可编辑  
备注：如果要设置整个表格不可编辑，用QTableWidget中的setEditTriggers方法  

* [virtual] QTableWidgetItem \*QTableWidgetItem::clone() const
创建一个item的copy  


