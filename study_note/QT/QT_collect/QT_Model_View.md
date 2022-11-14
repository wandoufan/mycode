# Qt的Model/View(模型/视图)架构

## 中文资料
https://blog.csdn.net/A642960662/article/details/123165863


## 基本概念
Model/View(模型/视图)架构是Qt用界面组件显示与编辑数据的一种结构，类似于MVC结构  
Model/View架构最重要的应用就是实现数据库应用程序，让用户通过界面来编辑和修改数据库中的数据  
这样将界面组件与数据源分离开来，可以将一个数据模型在不同界面中显示，也可以在不修改数据模型的情况下，设计特殊的界面组件  
例如：数据库中的一个数据表可以在一个QTableWidget组件中进行显示和编辑  
详见Qt帮助手册：Model/View Programming 
```
Data <---> Model <--(Delegate)--> View
```

## 1. Data(数据源)
Data(数据源)是实际的数据，数据来源可以是多种类型的，包括但不限于数据库  
例如：数据库中的一个数据表、SQL查询结果、内存中的一个StringList、磁盘中的一个文本文件  


## 2. Model(模型)
1. 功能
Model(模型)是视图和数据源之间的接口  
模型从数据源中提取需要的内容，然后传递给界面组件进行显示和编辑  
备注：数据模型中并不直接存储数据   

2. 类的继承关系
QAbstractltemModel类是所有数据模型类的基类，它是一个抽象类，不能直接使用  
```
                               | - QAbstractTableModel - QSqlQueryModel - QSqlTableModel - QSqlRelationTableModel
                               | - QAbstractProxyModel - QSortFilterProxyModel
QObject - QAbstractItemModel - | - QAbstractListModel - QStringListModel
                               | - QStandardItemModel
                               | - QFileSystemModel
                               | - QConcatenateTablesProxyModel
                               | - QDirModel                
```

3. 常用的数据模型类
QStringListModel  
用于处理字符串列表数据的数据模型类，以单列数据的形式显示  
QStandardltemModel  
标准的基于项数据的数据模型类，每个项数据可以是任何数据类型  
QFileSystemModel  
计算机上文件系统的数据模型类
QSortFilterProxyModel  
与其他数据模型结合，提供排序和过滤功能的数据模型类  
QSqlQueryModel  
用于数据库SQL查询结果的数据模型类  
QSqlTableModel  
用于数据库的一个数据表的数据模型类  
QSqlRelationalTableModel  
用于关系型数据表的数据模型类  
QDirModel
计算机上文件系统的数据模型类

4. 自定义数据模型
如果现有的模型类无法满足需求，用户可以从QAbstractltemModel、QAbstractListModel、QAbstractTableModel继承，生成自己定制的数据模型类  

5. QModelIndex
QModelIndex和上面的那些类之间没有继承关系，用来在数据模型中存取数据提供一个临时的指针  

6. QFileSystemModel和QDirModel的对比
二者的功能类似，都可以用来获取计算机中的文件和目录
但是QFileSystemModel使用了单独的线程，而QDirModel使用了主线程，可能会阻碍主线程
因此推荐使用QFileSystemModel


## 3. View(视图)
1. 功能
View(视图)是显示和编辑数据的界面组件  
视图从模型中获取每个数据项的模型索引(model index)，再通过模型索引获取数据，最后把数据传递给界面组件
备注：View中显示的数据结构可以与地Model中的数据结构完全不同，二者不必保持一致 
备注：视图中也不直接存储数据  

2. 类的继承关系
QAbstractItemView类是所有视图类的基类，它是一个抽象类，不能直接使用  
```
                                                             | - QListView - QListWidget
                                                             | - QTableView - QTableWidget
QWidget - QFrame - QAbstractScrollArea - QAbstractItemView - | - QTreeView - QTreeWidget
                                                             | - QColumnView
                                                             | - QHeaderView                 
```

3. 常用的视图类
备注：以下所有类都可以在Qt_designer的控件栏中找到  
QListView  
用于显示单列的列表数据，适用于一维数据的操作  
QTreeView  
用于显示树状结构数据，适用于树状结构数据的操作  
QTableView  
用于显示表格状数据，适用于二维表格型数据的操作  
QColumnView  
用多个QListView显示树状层次结构，树状结构的一层用一个QListView显示  
QHeaderView  
提供行表头或列表头的视图组件，如QTableView的行表头和列表头  

4. QItemSelectionModel
QItemSelectionModel与上面那些类之间没有继承关系，用来表示在视图界面中选中区域的数据模型  


## 4. Delegate(代理功能)
1. 功能
Model/View提供了代理功能，当用户在视图组件上编辑数据时提供一个数据编辑器(默认为QLineEdit)  
通过这个数据编辑器，用户可以直接在View中对数据进行编辑，不必再专门弹出一个数据编辑窗口
例如：在表格组件中编辑其中一个单元格的数据时，代理会读取单元格中的数据并显示在一个QLineEdit里，用户在QLineEdit中编辑完数据之后，再把数据保存回单元格  
备注：不一定都是QLineEdit，如果编辑数字，使用QSpinBox，如果下拉选择，使用QComboBox  

2. 类的继承关系
QAbstractltemDelegate类是所有代理类的基类，它是一个抽象类，不能直接使用  
最常用的是其子类QStyledltemDelegate，它是Qt视图组件默认的代理类  
```
QObject - QAbstractItemDelegate - | - QStyledItemDelegate
                                  | - QItemDelegate - QSqlRelationalDelegate
```


## Model与View的常用搭配组合
```
使用自定义Model            使用预定义好的Model       View           应用
                          QFileSystemModel         QTreeView      以目录树的形式显示本机上所有的文件和目录  
QAbstractListModel        QStringListModel         QListView      在界面上显示和编辑字符串列表
QAbstractTableModel       QStandardltemModel       QTableView     以表格的形式显示和编辑各种类型的数据
```


----------------------一些说明----------------------

## 通信机制
模型、代理、视图三者之间使用信号与槽来实现通信  
当数据源发生变化时，数据模型发出信号来通知界面组件  
当用户在界面上操作数据时，界面组件发射信号来表示这些操作信息  
当编辑数据时，代理发射信号把编辑器的状态通知数据模型和界面组件  


## 排序功能
在Model/View架构中，有两种方法可以实现排序，具体选哪种方法取决于底层的Model
1. 如果model本身是可排序的，则QTableView与QTreeView都提供了API，允许以编程的方式对model数据进行排序
备注：可排序是指在子类中，对QAbstractItemModel::sort()方法进行了重新实现

2. 可以通过信号与槽机制，实现互动式的排序(例如：用户通过点击表头来实现排序)
信号函数：QHeaderView::sortIndicatorChanged()
槽函数：QTableView::sortByColumn()或QTreeView::sortByColumn()

3. 额外的方法
如果模型没有所要求的接口，或想用列表视图Listview来显示数据
还可以在视图显示数据之前使用代理模型(PROXY MODEL)来转换模型的结构


## 模型与视图的对应关系
1. 一个视图只能关联到一个数据模型上
一个数据模型可以被多个视图关联

2. 当多个视图关联到同一个数据模型时
如果使用了信号与槽机制，信号会被发送到每一个关联的视图上，保证了所有View都是对应同一个数据模型


--------------------QXXView以及对应便利类QXXWidget--------------------

## 便利类的定义
```
View类            对应的便利类
QListView         QListWidget
QTableView        QTableWidget
QTreeView         QTreeWidget
```
便利类为组件的每个节点或单元格创建一个项(item)，用来存储数据、格式设置等  
注意：便利类没有关联的数据模型，也无法进行设置  
例如：QTableView类中有setModel成员函数，而到了QTableWidget类中，该成员函数变成了私有  


## 便利类的优点
QTableWidget相当于是把Model和View结合在了一起，实际上是用项的方式集成了数据模型的功能
因此使用QTableWidget就避开了大量的QXXModel和QXXView的内容，学习和使用也会更加简单


## 便利类的局限性
便利类将界面与数据绑定在了一起，因此缺乏对大型数据源进行灵活处理的能力，只适用于小型数据的显示和编辑 
便利类为了保证数据与界面的同步，需要频繁的复制数据，性能方面不适合大型的应用程序


## QXXView和QXXWidget的区别
(以QTableWidget和QTableView为例)
1. 继承关系
QTableWidget是QTableView的子类，即QTableWidget继承于QTableView  

2. 类中的方法
QTableView中的方法主要是对表格的各种属性进行设置  
QTableWidget中的方法除了继承QTableView之外，还多了对表格数据进行读写的接口  

3. 单元格的数据类型
QTableView可以使用自定义的数据模型来显示内容  
QTableWidget只能使用标准的数据类型，其单元格中的数据是QTableWidgetItem对象  

4. 单元格的数据源
QTableView事先要通过setModel函数来绑定数据模型  
QTableWidget没有关联的数据模型，逐个将单元格内的信息填好即可  

5. 数据与界面的同步
QTableView的Model和View是不会自动同步的，即Model中的数据变化时，View显示的数据不会随之改变
想要二者实现同步，必须自己去写代码来进行实现想要的功能
QTableWidget的数据与界面是自动关联的，即数据变化时，界面会随之变化


--------------------当前区域(Current item)和选中区域(selected items)--------------------

## 说明
在视图中，总有一个当前区域和一个选中区域，这是两个相互独立的状态
其中，当前区域和选择区域可以是重合的
视图要确保任何时候都有一个当前区域作为键盘导航


## 当前区域和选中区域的区别
1. 当前区域只能有一个
选中区域可以有一个，也可以有多个

2. 当用户操作键盘或鼠标时，当前区域会随着操作而改变
当用户进行交互操作时，区域是否处于选中状态取决于预设好的模式
这些模式详见：enum QAbstractItemView::SelectionBehavior、enum QAbstractItemView::SelectionMode

3. 如果按F2或者双击时，当前区域可以被编辑
当前区域可以与锚点一起使用，以指定应该选择或取消选择(或两者的组合)的范围

4. 当前区域由当前矩形来进行标识
选中区域由选中矩形来进行标识


-------------------Model/View数据同步与交换的过程---------------------

## 说明
1. model发出dataChanged()信号后，view会接收到该信号，然后view通过调用data()接口来获取数据
这一点是自己目前根据看到的资料做出的推测，没有看到这方面的明确说法

2. 不是只有dataChanged()信号才能通知View刷新界面，也可以直接使用beginResetModel()/endResetModel()函数

3. 实际测试，在进行view类实例化、点击视图中的数据、增删改数据等操作时
rowCount()、 columnCount()、 data()、 headerData()等这些函数会被触发调用
而且触发调用都是很多次，具体的次数可能与视图中的数据量有关系


## QAbstractItemModel::data()被触发的情况
data()函数一般不是手动调用的，而是被触发的，包括以下情况：
1. 当Model中没有内容时，即使发出了dataChanged()信号，data()函数也不会响应
备注：data()函数与dataChanged()信号之间好像是在框架内被绑定好了，不需要手动写出connect()函数来绑定  

2. 当Model中有内容时，发出了dataChanged()信号，data()函数就会随之被触发调用
备注：一个dataChanged()信号一般会触发data()函数多次，例如：修改单元格内容，然后再修改单元格颜色

3. 调用插入/删除/移动模型中的行/列等方法之后，各自会自动发出对应的信号(不是dataChanged())，也会进一步触发data()函数


## QAbstractItemModel::headerData()被触发的情况
类似于QAbstractItemModel::data()函数
当有QAbstractItemModel::headerDataChanged()信号时，headerData()函数会随之被触发响应


## Model中数据改变时通知View刷新界面
前提条件：把model和view关联起来
```
view -> setModel(model);
```
情景1：在调用setData()接口来自动发出dataChanged()信号
```
//在子类中对setData()接口重定义时，发出dataChanged()信号
bool StringListModel::setData(const QModelIndex &index, const QVariant &value, int role)
{
    qDebug() << "StringListModel::setData()";
    if (index.isValid() && role == Qt::EditRole)
    {
        stringList.replace(index.row(), value.toString());
        emit dataChanged(index, index, {role});
        return true;
    }
    return false;
}
```
情景2：手动发出dataChanged()信号
```
//在model内部的自定义函数中发出dataChanged()信号
void StringListModel::update_test1(int row)
{
    stringList.removeAt(row -1);
    stringList.replace(row, "test1 replace");
    stringList.insert(row + 1, "test1 insert");
    emit dataChanged(index(row - 1), index(row + 1), {Qt::EditRole});
}

//在外部调用model时发出dataChanged()信号
void MainWindow::on_pushButton_clicked()
{
    int row = 5;
    model -> stringList.removeAt(row -1);
    model -> stringList.replace(row, "update test replace");
    model -> stringList.insert(row + 1, "update test insert");
    emit model -> dataChanged(model -> index(row - 1), model -> index(row + 1), {Qt::EditRole});
}
```
情景3：使用beginResetModel()/endResetModel()函数
beginResetModel()/endResetModel()不需要用参数指明更新的区域范围，使用起来比dataChanged()信号更方便
```
//在model内部的自定义函数中使用beginResetModel()/endResetModel()函数
void StringListModel::update_test2(int row)
{
    beginResetModel();
    stringList.removeAt(row -1);
    stringList.replace(row, "test2 replace");
    stringList.insert(row + 1, "test2 insert");
    endResetModel();
}

//在外部调用model时使用beginResetModel()/endResetModel()函数
//备注：beginResetModel()/endResetModel()是protect的，不能直接在外部调用，必须再自己额外定义接口
void MainWindow::on_pushButton_clicked()
{
    model -> begin_reset();
    int row = 5;
    model -> stringList.removeAt(row -1);
    model -> stringList.replace(row, "update test replace");
    model -> stringList.insert(row + 1, "update test insert");
    model -> end_reset();
}
```
情景4：插入/删除/移动模型中的行/列等方法中使用对应的begin()/end()函数，界面会随之更新
```
//在子类中对insertRows()接口进行重定义时，调用beginInsertRows()/endInsertRows()方法
bool StringListModel::insertRows(int position, int rows, const QModelIndex &parent)
{
    beginInsertRows(QModelIndex(), position, position+rows-1);
    for (int row = 0; row < rows; ++row)
    {
        stringList.insert(position, "");
    }
    endInsertRows();
    return true;
}
```

----------------------设计自定义数据模型-------------------------

## 说明
1. 对于Qt::ItemDataRole中定义的各个角色，不必都进行实现，一般实现最重要的Qt::DisplayRole就足够了


## 关于数据模型与数据源
1. 数据源可以直接作为数据模型的一个成员变量
可以在数据模型的成员函数中对数据源进行读写
也可以在外部通过数据模型对数据源进行读写(数据源需要是public的)

2. 数据源也可以单独作为一个类存放起来
可以在数据模型的成员函数中对数据源的类进行调用
也可以在外部直接对数据源的类进行读写(不必通过数据模型)，读写完成后调用数据模型的信号函数或reset函数即可


## 选择自定义模型的基类
1. 如果是无层次的数据结构，如列表或表格，选择QAbstractListModel或QAbstractTableModel进行继承更方便

2. 如果是有层次的数据结构，如树状结构，那只能选择QAbstractItemModel作为基类


## 以QAbstractListModel为基类时需要实现的接口函数
1. 对于只读的模型，至少需要实现：
rowCount()、 data()

2. 如果模型需要实现编辑功能，需要额外实现：
setData()、 flags()
备注：记得要在setData()中手动发出dataChanged()信号

3. 如果需要控制模型标题栏的呈现方式，需要额外实现：
headerData()、 setHeaderData()
备注：记得要在setHeaderData()中手动发出headerDataChanged()信号

4. 如果需要实现插入/删除行的功能，需要额外实现：
insertRows()、removeRows()
备注：在调用插入/删除函数之前/之后，记得要调用对应的begin/end函数


## 以QAbstractTableModel为基类时需要实现的接口函数
1. 对于只读的模型，至少需要实现：
rowCount()、 columnCount()、 data()

2. 如果模型需要实现编辑功能，需要额外实现：
setData()、 flags()
备注：记得要在setData()中手动发出dataChanged()信号

3. 如果需要控制模型标题栏的呈现方式，需要额外实现：
headerData()、 setHeaderData()
备注：记得要在setHeaderData()中手动发出headerDataChanged()信号

4. 如果需要实现插入/删除行/列的功能，需要额外实现：
insertRows()、removeRows()、insertColumns()、removeColumns()
备注：在调用插入/删除函数之前/之后，记得要调用对应的begin/end函数


## 以QAbstractItemModel为基类时需要实现的接口函数
1. 对于只读的模型，至少需要实现：
index()、 parent()、 rowCount()、 columnCount()、 data()

2. 如果模型需要实现编辑功能，需要额外实现：
setData()、 flags()
备注：记得要在setData()中手动发出dataChanged()信号

3. 如果需要控制模型标题栏的呈现方式，需要额外实现：
headerData()、 setHeaderData()
备注：记得要在setHeaderData()中手动发出headerDataChanged()信号

4. 如果需要实现插入/删除行/列的功能，需要额外实现：
insertRows()、removeRows()、insertColumns()、removeColumns()
备注：在调用插入/删除函数之前/之后，记得要调用对应的begin/end函数


## 代码示例：以QAbstractListModel为基类的自定义数据模型
1. 头文件
```
class StringListModel : public QAbstractListModel
{
    Q_OBJECT

public:
    StringListModel(const QStringList &strings, QObject *parent = nullptr);

    //重定义的接口：只读数据模型
    int rowCount(const QModelIndex &parent = QModelIndex()) const override;
    QVariant data(const QModelIndex &index, int role) const override;
    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override;
    //重定义的接口：可编辑数据模型
    Qt::ItemFlags flags(const QModelIndex &index) const override;
    bool setData(const QModelIndex &index, const QVariant &value, int role = Qt::EditRole) override;
    //重定义的接口：插入和删除行
    bool insertRows(int position, int rows, const QModelIndex &index = QModelIndex()) override;
    bool removeRows(int position, int rows, const QModelIndex &index = QModelIndex()) override;
    //用public的方式声明，使得在数据模型外部可以调用到protect的reset函数
    void begin_reset()
    {
        beginResetModel();
    }
    void end_reset()
    {
        endResetModel();
    }
    //用来进行更新测试的自定义接口
    void update_test1(int row);
    void update_test2(int row);

public:
    //数据源作为数据模型的一个成员变量，并且声明为public，方便外部直接调用
    QStringList stringList;
};
```
2. 源文件
```
StringListModel::StringListModel(const QStringList &strings, QObject *parent)
    : QAbstractListModel(parent),
      stringList(strings)
{

}

int StringListModel::rowCount(const QModelIndex &parent) const
{
    return stringList.count();
}

QVariant StringListModel::data(const QModelIndex &index, int role) const
{
    if (!index.isValid())
        return QVariant();

    if (index.row() >= stringList.size())
        return QVariant();

    if (role == Qt::DisplayRole || role == Qt::EditRole)
        return stringList.at(index.row());
    else
        return QVariant();
}

QVariant StringListModel::headerData(int section, Qt::Orientation orientation, int role) const
{
    if (role != Qt::DisplayRole)
        return QVariant();

    if (orientation == Qt::Horizontal)
        return QStringLiteral("Column %1").arg(section);
    else
        return QStringLiteral("Row %1").arg(section);
}

Qt::ItemFlags StringListModel::flags(const QModelIndex &index) const
{
    if (!index.isValid())
        return Qt::ItemIsEnabled;

    return QAbstractItemModel::flags(index) | Qt::ItemIsEditable;
}

bool StringListModel::setData(const QModelIndex &index, const QVariant &value, int role)
{
    if (index.isValid() && role == Qt::EditRole)
    {
        stringList.replace(index.row(), value.toString());
        emit dataChanged(index, index, {role});
        return true;
    }
    return false;
}

bool StringListModel::insertRows(int position, int rows, const QModelIndex &parent)
{
    beginInsertRows(QModelIndex(), position, position+rows-1);

    for (int row = 0; row < rows; ++row)
    {
        stringList.insert(position, "");
    }

    endInsertRows();
    return true;
}

bool StringListModel::removeRows(int position, int rows, const QModelIndex &parent)
{
    beginRemoveRows(QModelIndex(), position, position+rows-1);

    for (int row = 0; row < rows; ++row)
    {
        stringList.removeAt(position);
    }

    endRemoveRows();
    return true;
}

void StringListModel::update_test1(int row)
{
    stringList.removeAt(row -1);
    stringList.replace(row, "test1 replace");
    stringList.insert(row + 1, "test1 insert");
    emit dataChanged(index(row - 1), index(row + 1), {Qt::EditRole});
}

void StringListModel::update_test2(int row)
{
    beginResetModel();
    stringList.removeAt(row -1);
    stringList.replace(row, "test2 replace");
    stringList.insert(row + 1, "test2 insert");
    endResetModel();
}
```
3. 调用代码
```
void MainWindow::init()
{
    //模型
    QStringList string_list;
    for(int i = 1; i < 10; i++)
    {
        string_list << QString("this is data %1").arg(i);
    } 
    model = new StringListModel(string_list);
    //视图
    table_view = new QTableView;
    table_view -> setModel(model);
    table_view -> setFixedSize(500, 600);
    table_view->setSelectionBehavior(QAbstractItemView::SelectRows);
    table_view->setSelectionMode(QAbstractItemView::ExtendedSelection);
    table_view->setEditTriggers(QAbstractItemView::NoEditTriggers);
    table_view->verticalHeader()->setVisible(false);
    table_view->horizontalHeader()->setVisible(true);
    table_view->horizontalHeader()->setDefaultSectionSize(50);
    table_view->horizontalHeader()->setSectionResizeMode(QHeaderView::Fixed);
    table_view->horizontalHeader()->setStretchLastSection(true);
    table_view->horizontalHeader()->resizeSection(1, 200);
    table_view->horizontalHeader()->resizeSection(2, 150);
    table_view->horizontalHeader()->resizeSection(3, 120);
    table_view->horizontalHeader()->resizeSection(4, 200);
    table_view->horizontalHeader()->setHighlightSections(false);
    table_view -> show();
}

void MainWindow::update()
{
    model -> setData(model -> index(1), QVariant("this is test1"), Qt::EditRole);
    model -> insertRows(4, 3);
    model -> removeRows(2, 3);
}
```
-------------------------------------