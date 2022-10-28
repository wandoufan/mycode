# Qt的Model/View(模型/视图)架构

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
用于处理字符串列表数据的数据模型类  
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
Model                View           应用
QFileSystemModel     QTreeView      以目录树的形式显示本机上所有的文件和目录  
QStringListModel     QListView      在界面上显示和编辑字符串列表
QStandardltemModel   QTableView     以表格的形式显示和编辑各种类型的数据
```


## 通信机制
模型、代理、视图三者之间使用信号与槽来实现通信  
当数据源发生变化时，数据模型发出信号来通知界面组件  
当用户在界面上操作数据时，界面组件发射信号来表示这些操作信息  
当编辑数据时，代理发射信号把编辑器的状态通知数据模型和界面组件  


----------------------------待总结------------------------------------


## QXXView以及对应便利类QXXWidget的区别 (以QTableWidget和QTableView为例)

--> QTableWidget相当于是把Model和View结合在了一起，因此使用QTableWidget就避开了大量的QXXModel和QXXView的内容
但QTableWidget也会有自己的局限性


## 便利类
QListView、QTableView、QTreeView分别提供QListWidget、QTableWidget、QTreeWidget这三个便利类  
便利类为组件的每个节点或单元格创建一个项(item)，用来存储数据、格式设置等  
因此，便利类没有数据模型，它实际上是用项的方式集成了数据模型的功能  
但这样就将界面与数据绑定了，因此便利类缺乏对大型数据源进行灵活处理的能力，只适用于小型数据的显示和编辑 


## QTableWidget和QTableView的区别
1. 继承关系
QTableWidget是QTableView的子类，即QTableWidget继承于QTableView  
QTableView中的方法主要是对表格的各种属性进行设置，QTableWidget中的方法主要是对表格的数据进行读写  
2. 单元格的数据类型
QTableView可以使用自定义的数据模型来显示内容  
QTableWidget只能使用标准的数据类型，其单元格中的数据是QTableWidgetItem对象  
3. 单元格的数据源
QTableView事先要通过setModel函数来绑定数据源  
QTableWidget不需要数据源，逐个将单元格内的信息填好即可  

## 数据的更新过程
```
Data <---> Model <--(Delegate)--> View
```
1. Model与Data的数据是自动关联的
当Model中的数据更新时，View中显示的数据会自动随之更新

2. Model中的数据与Data中的数据并没有自动关联
Data中的数据并不会自动传递到Model中，必须自己写代码从Data中读取，然后传递到Model中
Model中的数据发生改变，数据源Data中的数据并不会随之改变
如果要让数据源随之变化，也必须自己写代码实现

