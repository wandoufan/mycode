# QAbstractTableModel

## 基本功能
QAbstractTableModel是一个一维的数据模型
QAbstractTableModel是一个抽象类，一般用来继承，然后实现一个自定义的数据模型
详见Qt的Model/View(模型/视图)架构  
```
QObject - QAbstractItemModel - QAbstractTableModel - QSqlQueryModel - QSqlTableModel - QSqlRelationTableModel
```


## 说明
QAbstractTableModel中的函数很少，都是对基类QAbstractItemModel中的虚函数或纯虚函数进行了具体定义


## 构造函数
1. QAbstractTableModel::QAbstractTableModel(QObject \*parent = nullptr)


## 重定义的公共函数
1. [override virtual] bool QAbstractTableModel::dropMimeData(const QMimeData \*data, Qt::DropAction action, int row, int column, const QModelIndex &parent)

2. [override virtual] Qt::ItemFlags QAbstractTableModel::flags(const QModelIndex &index) const

3. [override virtual] QModelIndex QAbstractTableModel::index(int row, int column, const QModelIndex &parent = ...) const

4. [override virtual] QModelIndex QAbstractTableModel::sibling(int row, int column, const QModelIndex &idx) const

