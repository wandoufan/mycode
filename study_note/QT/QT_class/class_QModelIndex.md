# QModelIndex

## 基本功能
QModelIndex用来在Model/View架构中作为数据模型的模型索引，在数据模型中定位一条数据项  
每条数据项的模型索引由一个行号、一个列号、还有一个父项组成  
详见Qt的Model/View(模型/视图)架构  
父类：无
子类：无


## 注意事项
QModelIndex对象一般是通过QAbstractItemModel::createIndex()方法进行创建的，QModelIndex的构造函数获得的是一个非法的对象


## 构造函数
1. QModelIndex::QModelIndex()
创建一个空的模型索引，这个模型索引在数据模型中对应的位置是非法的  


## 常用公共函数：获取模型索引中的三个基本信息
1. int QModelIndex::row() const

2. int QModelIndex::column() const

3. QModelIndex QModelIndex::parent() const


## 常用公共函数：获取当前索引的兄弟姊妹索引
备注：如果在指定位置没有找到对应的数据项，则返回一个非法的模型索引
1. QModelIndex QModelIndex::sibling(int row, int column) const

2. QModelIndex QModelIndex::siblingAtColumn(int column) const

3. QModelIndex QModelIndex::siblingAtRow(int row) const


## 常用公共函数：获取其他信息
1. QVariant QModelIndex::data(int role = Qt::DisplayRole) const
获取模型索引对应的数据

2. Qt::ItemFlags QModelIndex::flags() const
返回对应数据项的属性设置(单元格是否可以被选中/编辑等)

3. bool QModelIndex::isValid() const
合法的模型索引是指模型索引属于一个数据模型，并且行号和列号都没有超出合法范围

4. const QAbstractItemModel \*QModelIndex::model() const
返回对应的数据模型


## 常用公共函数：提供的操作符
1. bool QModelIndex::operator!=(const QModelIndex &other) const

2. bool QModelIndex::operator<(const QModelIndex &other) const
备注：在很多数据模型中，模型索引的比较大小都没有进行定义，只有在使用了QMap的数据模型中才能比较大小  

3. bool QModelIndex::operator==(const QModelIndex &other) const
