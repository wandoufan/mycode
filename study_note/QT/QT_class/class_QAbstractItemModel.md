# QAbstractItemModel

## 基本功能
QAbstractItemModel是一个抽象类，是Model/View架构中所有模型类的基类
详见Qt的Model/View(模型/视图)架构  
```
                               | - QAbstractTableModel - QSqlQueryModel - QSqlTableModel - QSqlRelationTableModel
                               | - QAbstractProxyModel - QSortFilterProxyModel
QObject - QAbstractItemModel - | - QAbstractListModel - QStringListModel
                               | - QStandardItemModel
                               | - QFileSystemModel
                               | - QConcatenateTablesProxyModel
                               | - QDirModel                
```
备注：QAbstractItemModel类中的函数很多，时间关系，没有完全记录


## 关于数据模型的基本单元
在Model/View架构中，数据模型为视图组件和代理提供存取数据的标准接口  
不管底层的数据结构是不是二维数组，QAbstractItemModel的子类都以表格的层次结构来表示数据  
视图组件读取数据之后，再以单列、树状、表格等不同形式表现给用户  
数据模型中存储数据的基本单元是项(item)，每个项都有一个行号、一个列号、还有一个父项  


## 关于父项的说明
1. 当数据模型是列表或者表格时，所有数据项的父项都是顶层项，顶层项总用QModelIndex()来表示
备注：顶层项相当于根节点，不属于列表或表格中的任意一项
2. 当数据模型是树状结构时，情况比较复杂
一个节点可以有父节点，也可以是其他节点的父节点
备注：在树状结构中，项一般习惯于称为节点


## 关于每个数据项(单元格)的单元数据角色(Qt::ItemDataRole)的理解
每个单元格可以有多个角色，在对单元格的数据进行设置时，可以针对每个角色分别设置数据
例如：Qt::DisplayRole角色设置为显示的文本数据，Qt::ToolTipRole角色设置为鼠标放置时的提示文本，
Qt::FontRole角色设置为文本字体，Qt::BackgroundRole角色设置为背景颜色
1. 在设置数据时
可以对其中一个角色进行设置，接口函数为setData()和setHeaderData()
也可以对其中多个角色进行设置，接口函数为setItemData()
2. 在读取数据时
也是同样的，可以读取一个角色的数据，也可以读取多个角色的数据


## 关于模型索引
为了保证数据的表示方式和数据的存取方式隔离，数据模型中引入了模型索引的概念  
通过数据模型存取的每个数据都有一个模型索引，视图组件和代理都通过模型索引来获取数据  
QModelIndex就是表示模型索引的类，为数据存取提供一个临时的指针  
如果需要使用持久性的模型索引，则使用QPersistentModelIndex  
由于模型内部的数据组织结构随时可能改变，因此模型索引是临时的  
备注：QModelIndex与QAbstractItemModel等类之间没有任何继承关系  


## 构造函数
1. QAbstractItemModel::QAbstractItemModel(QObject \*parent = nullptr)
备注：QAbstractItemModel是一个抽象类，一般不需要进行实例化 


## 常用公共函数：数据排序
[virtual] void QAbstractItemModel::sort(int column, Qt::SortOrder order = Qt::AscendingOrder)


## 常用公共函数：获取各种模型索引
1. [pure virtual] QModelIndex QAbstractItemModel::index(int row, int column, const QModelIndex &parent = QModelIndex()) const
备注：这个是纯虚函数，需要在子类中进行自定义
根据给定的行号、列号和父项，返回指定项的模型索引  

2. [pure virtual] QModelIndex QAbstractItemModel::parent(const QModelIndex &index) const
备注：这个是纯虚函数，需要在子类中进行自定义

3. [virtual] QModelIndex QAbstractItemModel::sibling(int row, int column, const QModelIndex &index) const
返回兄弟姐妹数据项的模型索引


## 常用公共函数：根据模型索引获取信息
1. [virtual] Qt::ItemFlags QAbstractItemModel::flags(const QModelIndex &index) const
获取模型索引对应的数据项的属性(单元格是否可以被选中/编辑等)

2. bool QAbstractItemModel::hasIndex(int row, int column, const QModelIndex &parent = QModelIndex()) const

3. [virtual] bool QAbstractItemModel::hasChildren(const QModelIndex &parent = QModelIndex()) const


## 常用公共函数：向数据模型中插入数据
1. bool QAbstractItemModel::insertRow(int row, const QModelIndex &parent = QModelIndex())
在row之前插入一行

2. [virtual] bool QAbstractItemModel::insertRows(int row, int count, const QModelIndex &parent = QModelIndex())

3. bool QAbstractItemModel::insertColumn(int column, const QModelIndex &parent = QModelIndex())
在column之前插入一列

4. [virtual] bool QAbstractItemModel::insertColumns(int column, int count, const QModelIndex &parent = QModelIndex())


## 常用公共函数：从数据模型中删除数据
1. bool QAbstractItemModel::removeRow(int row, const QModelIndex &parent = QModelIndex())

2. [virtual] bool QAbstractItemModel::removeRows(int row, int count, const QModelIndex &parent = QModelIndex())

3. bool QAbstractItemModel::removeColumn(int column, const QModelIndex &parent = QModelIndex())

4. [virtual] bool QAbstractItemModel::removeColumns(int column, int count, const QModelIndex &parent = QModelIndex())


## 常用公共函数：在数据模型中移动数据
备注：只有在支持移动的数据模块中才可以使用这些函数
1. bool QAbstractItemModel::moveRow(const QModelIndex &sourceParent, int sourceRow, const QModelIndex &destinationParent, int destinationChild)

2. [virtual] bool QAbstractItemModel::moveRows(const QModelIndex &sourceParent, int sourceRow, int count, const QModelIndex &destinationParent, int destinationChild)

3. bool QAbstractItemModel::moveColumn(const QModelIndex &sourceParent, int sourceColumn, const QModelIndex &destinationParent, int destinationChild)

4. [virtual] bool QAbstractItemModel::moveColumns(const QModelIndex &sourceParent, int sourceColumn, int count, const QModelIndex &destinationParent, int destinationChild)


## 常用公共函数：读取/设置数据模型工作区的数据
1. [pure virtual] QVariant QAbstractItemModel::data(const QModelIndex &index, int role = Qt::DisplayRole) const
备注：这个是纯虚函数，需要在子类中进行自定义
如果没有要返回的值，则返回一个不合法的QVariant，不要返回0

2. [virtual] bool QAbstractItemModel::setData(const QModelIndex &index, const QVariant &value, int role = Qt::EditRole)
把index位置数据项的role角色的数据设置为value  
当数据更新成功，则返回true，并发出dataChanged()信号，否则返回false  

3. [virtual] QMap<int, QVariant> QAbstractItemModel::itemData(const QModelIndex &index) const
用map的形式返回index位置数据项的所有预定义角色的值  

4. [virtual] bool QAbstractItemModel::setItemData(const QModelIndex &index, const QMap<int, QVariant> &roles)
roles中是每一个角色以及对应的数值，把index位置数据项的数据按照roles进行设置  
不在roles中的角色的数值将不会被修改  
当数据更新成功，则返回true，否则返回false  


## 常用公共函数：读取/设置数据模型表头行/列的数据
1. [virtual] QVariant QAbstractItemModel::headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const

2. [virtual] bool QAbstractItemModel::setHeaderData(int section, Qt::Orientation orientation, const QVariant &value, int role = Qt::EditRole)
当数据更新成功，则返回true，并发出headerDataChanged()信号，否则返回false  


## 常用保护函数：创建模型索引对象
1. [protected] QModelIndex QAbstractItemModel::createIndex(int row, int column, void \*ptr = nullptr) const

2. [protected] QModelIndex QAbstractItemModel::createIndex(int row, int column, quintptr id) const

3. [protected] QModelIndexList QAbstractItemModel::persistentIndexList() const


## 信号函数