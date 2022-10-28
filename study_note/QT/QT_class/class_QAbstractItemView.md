# QAbstractItemView

## 基本功能
QAbstractItemView是一个抽象类，是Model/View架构中所有视图类的基类
详见Qt的Model/View(模型/视图)架构
```
QWidget - QFrame - QAbstractScrollArea - QAbstractItemView - | - QTableView - QTableWidget 
															 | - QTreeView
															 | - QListView
															 | - QHeaderView
															 | - QColumnView
```
备注：QAbstractItemView类中的函数很多，时间关系，没有完全记录


## QAbstractItemView提供的按键功能
```
按键                      功能
箭头                      修改当前单元格，并且选中             
Ctrl + 箭头               修改当前单元格，但是不选中
Shift + 箭头              修改当前单元格，并且选中，之前已经被选中的单元格仍然保持选中
Ctrl + 空格               固定当前选中单元格区域
Tab/Backtab               移动当前单元格到下一个/上一个单元格
Home/End                  选中当前行的第一个/最后一个单元格
Page up/Page down         向上/向下翻页
Ctrl+A                    选中表格中所有单元格
```


## 构造函数
1. QAbstractItemView::QAbstractItemView(QWidget \*parent = nullptr)
备注：QAbstractItemView是一个抽象类，一般不需要进行实例化  


## 常用公共函数：读取/设置关联的数据模型
1. QAbstractItemModel \*QAbstractItemView::model() const

2. [virtual] void QAbstractItemView::setModel(QAbstractItemModel \*model)



## 常用公共函数：读取/设置表格的选择模式和选择行为
1. QAbstractItemView::SelectionBehavior QAbstractItemView::selectionBehavior() const

2. void QAbstractItemView::setSelectionBehavior(QAbstractItemView::SelectionBehavior behavior)

3. QAbstractItemView::SelectionMode QAbstractItemView::selectionMode() const

4. void QAbstractItemView::setSelectionMode(QAbstractItemView::SelectionMode mode)


## enum QAbstractItemView::SelectionBehavior
```
Constant								Value			Description
QAbstractItemView::SelectItems 			0               选择单个单元格
QAbstractItemView::SelectRows			1 				一次选中一整行
QAbstractItemView::SelectColumns		2 				一次选中一整列
```


## enum QAbstractItemView::SelectionMode
备注：最常用的模式是SingleSelection和ExtendedSelection
```
Constant								Value	Description
QAbstractItemView::SingleSelection 		1 		当用户选中一个单元格时，之前已经被选中的单元格会变成不选中的状态
QAbstractItemView::ContiguousSelection	4		当用户按住shift时可以进行连续选择
QAbstractItemView::ExtendedSelection	3		当用户按住ctrl时可以进行多选，按住shift时可以进行连续选择
QAbstractItemView::MultiSelection		2		不需要按住ctrl或者shift，就能实现多选
QAbstractItemView::NoSelection			0		单元格不可被选中
```

