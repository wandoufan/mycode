# Qt的Model/View(模型/视图)架构

## 基本概念
Model/View(模型/视图)架构是Qt用界面组件显示与编辑数据的一种结构，类似于MVC结构  
GUI应用程序的一个很重要的功能就是由用户在界面上编辑和修改数据，例如数据库应用程序  
在数据库应用程序中，用户在界面上执行各种操作，实际上是修改了界面组件所关联的数据库内的数据  
将界面组件与数据源分离开来，可以将一个数据模型在不同界面中显示，也可以在不修改数据模型的情况下，设计特殊的界面组件  


## 1. Data(数据源)
Data(数据源)是实际的数据  
例如：数据库中的一个数据表、SQL查询结果、内存中的一个变量、磁盘中的一个文件  


## 2. Model(模型)
1. 功能
Model(模型)是视图和数据源之间的接口  
模型从数据源中提取需要的内容，然后传递给界面组件进行显示和编辑  
备注：数据并没有直接存储在数据模型里  
2. 类的继承关系
QAbstractltemModel类是所有数据模型类的基类，它是一个抽象类，不能直接使用  
```
父类 -> 子类
QObject -> QAbstractItemModel -> QAbstractListModel -> QStringListModel
                              -> QAbstractProxyModel -> ...
                              -> QConcatenateTablesProxyModel
                              -> QDirModel
                              -> QFileSystemModel
                              -> QStandardItemModel
                              -> QAbstractTableModel -> QSqlQueryModel -> QSqlTableModel -> QSqlRelationTableModel
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
4. 自定义数据模型
如果现有的模型类无法满足需求，用户可以从QAbstractltemModel、QAbstractListModel、QAbstractTableModel继承，生成自己定制的数据模型类  
5. QModelIndex
QModelIndex和上面的那些类之间没有继承关系，用来在一个数据模型中定位数据  


## 3. View(视图)
1. 功能
View(视图)是显示和编辑数据的界面组件  
视图从模型中获取每个数据项的模型索引(model index)，再通过模型索引获取数据，最后把数据传递给界面组件  
2. 类的继承关系
QAbstractItemView类是所有视图类的基类，它是一个抽象类，不能直接使用  
```
父类 -> 子类
QObject、QPaintdevice -> QWidget -> QFrame -> QAbstractScrollArea -> QAbstractItemView

QAbstractItemView -> QListView -> QListWidget
                               -> QUndoView
                  -> QTableView -> QTableWidget
                  -> QTreeView -> QTreeWidget
                  -> QColumnView
                  -> QHeaderView
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


## 4. Delegate(代理功能)
1. 功能
Model/View提供了代理功能，当用户在视图组件上编辑数据时提供一个数据编辑器(默认为QLineEdit)  
例如：在表格组件中编辑其中一个单元格的数据时，代理会读取单元格中的数据并显示在一个QLineEdit里，用户在QLineEdit中编辑完数据之后，再把数据保存回单元格  
备注：不一定都是QLineEdit，如果编辑数字，用QSpinBox更合适  
2. 类的继承关系
QAbstractltemDelegate类是所有代理类的基类，它是一个抽象类，不能直接使用  
最常用的是其子类QStyledltemDelegate，它是Qt视图组件默认的代理类  
```
父类 -> 子类
QObject -> QAbstractItemDelegate -> QStyledItemDelegate
                                 -> QItemDelegate -> QSqlRelationalDelegate
```


## 通信机制
模型、代理、视图三者之间使用信号与槽来实现通信  
当数据源发生变化时，数据模型发出信号来通知界面组件  
当用户在界面上操作数据时，界面组件发射信号来表示这些操作信息  
当编辑数据时，代理发射信号把编辑器的状态通知数据模型和界面组件  


