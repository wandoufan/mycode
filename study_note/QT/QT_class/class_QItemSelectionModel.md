# QItemSelectionModel

## 基本功能
QItemSelectionModel是Model/View架构中的一个类，用来表示在视图界面中选中区域的数据模型
例如：在表格中，通过鼠标选中一个单元格或一片区域之后，被选中的部分就会以其他颜色显示，这个就是通过QItemSelectionModel实现
```
QObject - QItemSelectionModel
```


## 说明
QItemSelectionModel不是一个单独的数据模型，而是其他数据模型的一部分  
用来代表其他数据模型中被选中的区域的数据，因此QItemSelectionModel一定要和其他数据模型关联起来  


## 构造函数
1. QItemSelectionModel::QItemSelectionModel(QAbstractItemModel \*model = nullptr)

2. QItemSelectionModel::QItemSelectionModel(QAbstractItemModel \*model, QObject \*parent)


## 常用公共函数：关联的数据模型
1. QAbstractItemModel \*QItemSelectionModel::model()

2. const QAbstractItemModel \*QItemSelectionModel::model() const

3. void QItemSelectionModel::setModel(QAbstractItemModel \*model)


## 常用公共函数：选中的区域
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


## 槽函数：清除选择区域
1. [virtual slot] void QItemSelectionModel::clear()

2. [virtual slot] void QItemSelectionModel::clearCurrentIndex()

3. [slot] void QItemSelectionModel::clearSelection()
