# QAbstractItemModel

## 基本功能
QAbstractItemModel是一个抽象类，是Model/View架构中所有模型类的基类
QAbstractItemModel除了是所有模型类的基类，还可以直接继承QAbstractItemModel来实现自定义的数据模型
备注：如果是与QListView或QTableView搭配，建议继承QAbstractListModel或QAbstractTableModel来实现自定义的数据模型
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
1. [virtual] void QAbstractItemModel::sort(int column, Qt::SortOrder order = Qt::AscendingOrder)


## 常用公共函数：数据检索
1. [virtual] QModelIndexList QAbstractItemModel::match(const QModelIndex &start, int role, const QVariant &value, int hits = 1, Qt::MatchFlags flags = Qt::MatchFlags(Qt::MatchStartsWith|Qt::MatchWrap)) const
从start位置开始检索value，当检索到最后一个位置，或者匹配的个数达到hits时停止检索，最后以列表的形式返回模型中匹配的数据
备注：hits为-1，则代表检索所有的匹配数据，没有数量限制
备注：当没有检索到匹配数据时，返回列表为空
备注：返回列表中的顺序与模型中顺序可能不一致


## 常用公共函数：获取行数和列数
1. [pure virtual] int QAbstractItemModel::rowCount(const QModelIndex &parent = QModelIndex()) const
返回给定parent节点下面的行数，当父节点有效时，这意味着返回的是父节点的子节点数
在基于表格结构的子类中进行定义时，如果parent是合法的，则rowCount()应该返回0
(上述是帮助手册的原话，没看明白，感觉应该是parent是非法时，rowCount()返回0)

2. [pure virtual] int QAbstractItemModel::columnCount(const QModelIndex &parent = QModelIndex()) const
返回给定parent节点下面的列数
在大多数子类中，列的数量是独立于parent节点的，一般直接返回一个数字
备注：在基于表格结构的子类中进行定义时，如果parent是合法的，则columnCount()应该返回0


## 常用公共函数：获取各种模型索引
1. [pure virtual] QModelIndex QAbstractItemModel::index(int row, int column, const QModelIndex &parent = QModelIndex()) const
根据给定的行号、列号和父项，返回指定项的模型索引  
备注：这个是纯虚函数，需要在子类中进行自定义

2. [pure virtual] QModelIndex QAbstractItemModel::parent(const QModelIndex &index) const
备注：这个是纯虚函数，需要在子类中进行自定义

3. [virtual] QModelIndex QAbstractItemModel::sibling(int row, int column, const QModelIndex &index) const
返回兄弟姐妹数据项的模型索引

4. [virtual] QModelIndex QAbstractItemModel::buddy(const QModelIndex &index) const
返回兄弟姐妹数据项的模型索引


## 常用公共函数：根据模型索引获取信息
1. [virtual] Qt::ItemFlags QAbstractItemModel::flags(const QModelIndex &index) const
获取模型索引对应的数据项的属性(单元格是否可以被选中/编辑等)

2. bool QAbstractItemModel::hasIndex(int row, int column, const QModelIndex &parent = QModelIndex()) const

3. [virtual] bool QAbstractItemModel::hasChildren(const QModelIndex &parent = QModelIndex()) const


## 常用公共函数：读取/设置数据模型表头行/列的数据
1. [virtual] QVariant QAbstractItemModel::headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const
作用就是返回标题行/列的名称

2. [virtual] bool QAbstractItemModel::setHeaderData(int section, Qt::Orientation orientation, const QVariant &value, int role = Qt::EditRole)
对表头行/列的数据进行更新
当数据更新成功，则返回true，并自动发出headerDataChanged()信号，否则返回false
备注：如果在子类中对setHeaderData()函数进行了重定义，也必须在setHeaderData()中显示的发出该headerDataChanged()信号


## 常用公共函数：读取/设置数据模型工作区的数据
1. [pure virtual] QVariant QAbstractItemModel::data(const QModelIndex &index, int role = Qt::DisplayRole) const
根据索引和角色返回一个数据，如果没有要返回的值，则返回一个不合法的QVariant，不要返回0
备注：这个是纯虚函数，具体的返回数据需要在子类中进行自定义
注意：data()函数一般不是手动调用的，而是通过dataChanged()信号触发的，详见QT_Model_View.md

2. [virtual] bool QAbstractItemModel::setData(const QModelIndex &index, const QVariant &value, int role = Qt::EditRole)
把index位置数据项的role角色的数据设置为value  
当数据更新成功，则返回true，并自动发出dataChanged()信号，否则返回false  
备注：如果在子类中对setData()函数进行了重定义，也必须在setData()中显示的发出该dataChanged()信号

3. [virtual] QMap<int, QVariant> QAbstractItemModel::itemData(const QModelIndex &index) const
用map的形式返回index位置数据项的所有预定义角色的值  

4. [virtual] bool QAbstractItemModel::setItemData(const QModelIndex &index, const QMap<int, QVariant> &roles)
roles中是每一个角色以及对应的数值，把index位置数据项的数据按照roles进行设置  
不在roles中的角色的数值将不会被修改  
当数据更新成功，则返回true，否则返回false    


## 常用公共函数：向数据模型中插入行/列
注意：这里插入的行/列都是空的一行/一列，并不包含数据，设置数据需要额外调用setData()接口
1. bool QAbstractItemModel::insertRow(int row, const QModelIndex &parent = QModelIndex())
在row之前插入一行

2. [virtual] bool QAbstractItemModel::insertRows(int row, int count, const QModelIndex &parent = QModelIndex())
在row之前插入count行
备注：直接调用基类中的接口，不会做任何操作，直接返回false，要想真正使用这个函数，需要在子类中自己进行定义

3. bool QAbstractItemModel::insertColumn(int column, const QModelIndex &parent = QModelIndex())
在column之前插入一列

4. [virtual] bool QAbstractItemModel::insertColumns(int column, int count, const QModelIndex &parent = QModelIndex())
在column之前插入count列
备注：直接调用基类中的接口，不会做任何操作，直接返回false，要想真正使用这个函数，需要在子类中自己进行定义


## 常用公共函数：从数据模型中删除行/列
1. bool QAbstractItemModel::removeRow(int row, const QModelIndex &parent = QModelIndex())

2. [virtual] bool QAbstractItemModel::removeRows(int row, int count, const QModelIndex &parent = QModelIndex())
备注：直接调用基类中的接口，不会做任何操作，直接返回false，要想真正使用这个函数，需要在子类中自己进行定义

3. bool QAbstractItemModel::removeColumn(int column, const QModelIndex &parent = QModelIndex())

4. [virtual] bool QAbstractItemModel::removeColumns(int column, int count, const QModelIndex &parent = QModelIndex())
备注：直接调用基类中的接口，不会做任何操作，直接返回false，要想真正使用这个函数，需要在子类中自己进行定义


## 常用公共函数：在数据模型中移动行/列
备注：只有在支持移动的数据模块中才可以使用这些函数
1. bool QAbstractItemModel::moveRow(const QModelIndex &sourceParent, int sourceRow, const QModelIndex &destinationParent, int destinationChild)

2. [virtual] bool QAbstractItemModel::moveRows(const QModelIndex &sourceParent, int sourceRow, int count, const QModelIndex &destinationParent, int destinationChild)
备注：直接调用基类中的接口，不会做任何操作，直接返回false，要想真正使用这个函数，需要在子类中自己进行定义

3. bool QAbstractItemModel::moveColumn(const QModelIndex &sourceParent, int sourceColumn, const QModelIndex &destinationParent, int destinationChild)

4. [virtual] bool QAbstractItemModel::moveColumns(const QModelIndex &sourceParent, int sourceColumn, int count, const QModelIndex &destinationParent, int destinationChild)
备注：直接调用基类中的接口，不会做任何操作，直接返回false，要想真正使用这个函数，需要在子类中自己进行定义


## 常用保护函数：创建模型索引对象
1. [protected] QModelIndex QAbstractItemModel::createIndex(int row, int column, void \*ptr = nullptr) const

2. [protected] QModelIndex QAbstractItemModel::createIndex(int row, int column, quintptr id) const

3. [protected] QModelIndexList QAbstractItemModel::persistentIndexList() const


## 常用保护函数：开始/结束重置数据模型
1. [protected] void QAbstractItemModel::beginResetModel()
开始模型重置操作，在重新设置数据模型的任何内部数据结构之前，必须调用这个函数
重置操作会把数据模型重置到当前状态(关联在这个模型上的所有视图都会被重置)
当一个数据模型被重置则意味着，之前从这个模型上查询到的所有数据都变成了非法的，必须重新查询
同时也意味着当前数据项和所有被选中的数据项都变成了非法的
当模型的数据发生重大变化时，直接调用这个函数，比发出dataChanged()信号来通知其他组件要更有效
备注：beginResetModel()/endResetModel()不需要用参数指明更新的区域范围，使用起来比dataChanged()信号更方便

2. [protected] void QAbstractItemModel::endResetModel()
结束模型重置操作，在重新设置数据模型的任何内部数据结构之后，必须调用这个函数


## 常用保护函数：开始/结束插入行/列
备注：如果在子类中对insertRows()/insertColumns()进行了重新定义，必须在进行插入数据之前/之后调用下面这些函数
备注：调用beginInsert函数会自动发出信号函数，Model关联的View必须在数据插入之前对信号函数做出反应，否则View可能会以非法状态结束
1. [protected] void QAbstractItemModel::beginInsertRows(const QModelIndex &parent, int first, int last)

2. [protected] void QAbstractItemModel::endInsertRows()

3. [protected] void QAbstractItemModel::beginInsertColumns(const QModelIndex &parent, int first, int last)

4. [protected] void QAbstractItemModel::endInsertColumns()


## 常用保护函数：开始/结束删除行/列
备注：如果在子类中对removeRows()/removeColumns()进行了重新定义，必须在进行删除数据之前/之后调用下面这些函数
备注：调用beginRemove函数会自动发出信号函数，Model关联的View必须在数据删除之前对信号函数做出反应，否则View可能会以非法状态结束
1. [protected] void QAbstractItemModel::beginRemoveRows(const QModelIndex &parent, int first, int last)

2. [protected] void QAbstractItemModel::endRemoveRows()

3. [protected] void QAbstractItemModel::beginRemoveColumns(const QModelIndex &parent, int first, int last)

4. [protected] void QAbstractItemModel::endRemoveColumns()


## 常用保护函数：开始/结束移动行/列
备注：这几个函数的作用有点复杂，没有完全看懂，但类似于上面的函数
1. [protected] bool QAbstractItemModel::beginMoveRows(const QModelIndex &sourceParent, int sourceFirst, int sourceLast, const QModelIndex &destinationParent, int destinationChild)

2. [protected] void QAbstractItemModel::endMoveRows()

3. [protected] bool QAbstractItemModel::beginMoveColumns(const QModelIndex &sourceParent, int sourceFirst, int sourceLast, const QModelIndex &destinationParent, int destinationChild)

4. [protected] void QAbstractItemModel::endMoveColumns()


## 有信号函数：非私有：数据改变
1. [signal] void QAbstractItemModel::dataChanged(const QModelIndex &topLeft, const QModelIndex &bottomRight, const QVector<int> &roles = ...)
只要item中的数据发生改变，就会发出此信号
topLeft和bottomRight参数代表数据变化区域的左上角和右下角，roles参数代表变化的数据对应的数据角色(可以有多个)
备注：如果是一维模型，topLeft和bottomRight参数代表数据变化区域的第一行和最后一行
备注：如果在子类中对setData()函数进行了重定义，也必须在setData()中显示的发出该dataChanged()信号
备注：这个信号函数是非私有，可以自己手动在任意位置发出，不是只能用在setData()中
```
//topLeft和bottomRight参数可以用index()方法获取
emit dataChanged(index(0, 0), index(3, 4), {Qt::EditRole});
//topLeft和bottomRight参数也可以用createIndex()方法获取
emit dataChanged(createIndex(0, 0), createIndex(3, 4), {Qt::EditRole});
//如果是一维模型，column参数默认为0，可以只写第一个row参数
emit dataChanged(index(row - 1), index(row + 1), {Qt::EditRole});
```

2. [signal] void QAbstractItemModel::headerDataChanged(Qt::Orientation orientation, int first, int last)
只要header中的数据发生改变，就会发出此信号
备注：如果在子类中对setHeaderData()函数进行了重定义，也必须在setHeaderData()中显示的发出该headerDataChanged()信号
备注：如果改变了行数或列数，不必发出此信号，使用begin/end函数即可
备注：这个信号函数是非私有，可以自己手动在任意位置发出，不是只能用在setHeaderData()中

3. [signal] void QAbstractItemModel::layoutAboutToBeChanged(const QList<QPersistentModelIndex> &parents = ..., QAbstractItemModel::LayoutChangeHint hint = ...)

4. [signal] void QAbstractItemModel::layoutChanged(const QList<QPersistentModelIndex> &parents = ..., QAbstractItemModel::LayoutChangeHint hint = ...)


## 信号函数：私有：即将进行各种操作
注意：私有信号函数只能在QAbstractItemModel中发出，不能在子类代码中显式发出
注意：私有信号函数可以用于信号连接，但不能由用户手动发出，都是由系统自动发出的
1. [signal] void QAbstractItemModel::rowsAboutToBeInserted(const QModelIndex &parent, int start, int end)

2. [signal] void QAbstractItemModel::rowsAboutToBeMoved(const QModelIndex &sourceParent, int sourceStart, int sourceEnd, const QModelIndex &destinationParent, int destinationRow)

3. [signal] void QAbstractItemModel::rowsAboutToBeRemoved(const QModelIndex &parent, int first, int last)

4. [signal] void QAbstractItemModel::columnsAboutToBeInserted(const QModelIndex &parent, int first, int last)

5. [signal] void QAbstractItemModel::columnsAboutToBeMoved(const QModelIndex &sourceParent, int sourceStart, int sourceEnd, const QModelIndex &destinationParent, int destinationColumn)

6. [signal] void QAbstractItemModel::columnsAboutToBeRemoved(const QModelIndex &parent, int first, int last)

7. [signal] void QAbstractItemModel::modelAboutToBeReset()


## 信号函数：私有：已经进行了各种操作
注意：私有信号函数只能在QAbstractItemModel中发出，不能在子类代码中显式发出
注意：私有信号函数可以用于信号连接，但不能由用户手动发出，都是由系统自动发出的
1. [signal] void QAbstractItemModel::rowsInserted(const QModelIndex &parent, int first, int last)

2. [signal] void QAbstractItemModel::rowsMoved(const QModelIndex &parent, int start, int end, const QModelIndex &destination, int row)

3. [signal] void QAbstractItemModel::rowsRemoved(const QModelIndex &parent, int first, int last)

4. [signal] void QAbstractItemModel::columnsInserted(const QModelIndex &parent, int first, int last)

5. [signal] void QAbstractItemModel::columnsMoved(const QModelIndex &parent, int start, int end, const QModelIndex &destination, int column)

6. [signal] void QAbstractItemModel::columnsRemoved(const QModelIndex &parent, int first, int last)

7. [signal] void QAbstractItemModel::modelReset()

