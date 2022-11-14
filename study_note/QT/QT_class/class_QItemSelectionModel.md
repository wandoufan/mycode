# QItemSelectionModel

## 基本功能
QItemSelectionModel是Model/View架构中的一个类，用来表示在视图界面中选中区域的数据模型
例如：在表格中，通过鼠标选中一个单元格或一片区域之后，被选中的部分就会以其他颜色显示，这个就是通过QItemSelectionModel实现
```
QObject - QItemSelectionModel
```
备注：QItemSelectionModel和Model/View中的类之间都没有继承关系


## 说明
1. QItemSelectionModel不是一个单独的数据模型，而是其他数据模型的一部分  
用来代表其他数据模型中被选中的区域的数据，因此QItemSelectionModel一定要和其他数据模型关联起来  
2. 选中区域可以有一个，也可以有多个


## 构造函数
1. QItemSelectionModel::QItemSelectionModel(QAbstractItemModel \*model = nullptr)

2. QItemSelectionModel::QItemSelectionModel(QAbstractItemModel \*model, QObject \*parent)


## 常用公共函数：读取/设置关联的数据模型
1. QAbstractItemModel \*QItemSelectionModel::model()

2. const QAbstractItemModel \*QItemSelectionModel::model() const

3. void QItemSelectionModel::setModel(QAbstractItemModel \*model)


## 常用公共函数：获取当前区域
1. QModelIndex QItemSelectionModel::currentIndex() const
返回当前区域对应的index，如果没有当前区域，则返回一个非法的index


## 常用公共函数：获取选中区域
1. QModelIndex QItemSelectionModel::currentIndex() const

2. QModelIndexList QItemSelectionModel::selectedIndexes() const

3. QModelIndexList QItemSelectionModel::selectedRows(int column = 0) const

4. QModelIndexList QItemSelectionModel::selectedColumns(int row = 0) const

5. const QItemSelection QItemSelectionModel::selection() const


## 常用公共函数：判断是否选中
1. bool QItemSelectionModel::rowIntersectsSelection(int row, const QModelIndex &parent) const
如果parent的第row行有任意元素被选中，则返回true，否则返回false  

2. bool QItemSelectionModel::isRowSelected(int row, const QModelIndex &parent) const
如果parent的第row行的所有元素都被选中，则返回true，否则返回false  

3. bool QItemSelectionModel::columnIntersectsSelection(int column, const QModelIndex &parent) const
如果parent的第column列有任意元素被选中，则返回true，否则返回false  

4. bool QItemSelectionModel::isColumnSelected(int column, const QModelIndex &parent) const
如果parent的第column列的所有元素都被选中，则返回true，否则返回false 

5. bool QItemSelectionModel::isSelected(const QModelIndex &index) const

6. bool QItemSelectionModel::hasSelection() const


## 公共槽函数：清除选中区域
备注：都会发出相应的信号函数
1. [virtual slot] void QItemSelectionModel::clear()

2. [virtual slot] void QItemSelectionModel::clearCurrentIndex()

3. [slot] void QItemSelectionModel::clearSelection()


## 公共槽函数：重置选中区域
1. [virtual slot] void QItemSelectionModel::reset()
清除选中区域，但不发出任何信号函数


## 公共槽函数：按照指定模式设置选中区域
备注：都会发出相应的信号函数
1. [virtual slot] void QItemSelectionModel::select(const QModelIndex &index, QItemSelectionModel::SelectionFlags command)

2. [virtual slot] void QItemSelectionModel::select(const QItemSelection &selection, QItemSelectionModel::SelectionFlags command)

3. [virtual slot] void QItemSelectionModel::setCurrentIndex(const QModelIndex &index, QItemSelectionModel::SelectionFlags command)


## enum QItemSelectionModel::SelectionFlag
这个集合描述了选中区域的设置模式
```
Constant								Value			Description
QItemSelectionModel::NoUpdate			0x0000 			不更新任何选中区域
QItemSelectionModel::Clear				0x0001 			整个选中区域都会被清除
QItemSelectionModel::Select				0x0002 			所有指定的索引会被选中
QItemSelectionModel::Deselect			0x0004 			所有指定的索引会被取消选中
QItemSelectionModel::Toggle				0x0008 			所有指定的索引被选中或取消选中取决它们当前的状态
QItemSelectionModel::Current			0x0010 			当前区域会被更新
QItemSelectionModel::Rows				0x0020 			所有索引会被扩展到整个行
QItemSelectionModel::Columns			0x0040 			所有索引会被扩展到整个列
QItemSelectionModel::SelectCurrent		Select | Current
QItemSelectionModel::ToggleCurrent		Toggle | Current
QItemSelectionModel::ClearAndSelect		Clear | Select
```