# QAbstractListModel

## 基本功能
QAbstractListModel是一个一维的数据模型
QAbstractListModel是一个抽象类，一般用来继承，然后实现一个自定义的数据模型
详见Qt的Model/View(模型/视图)架构  
```
QObject - QAbstractItemModel - QAbstractListModel - QStringListModel
```


## 说明
QAbstractListModel中的函数很少，都是对基类QAbstractItemModel中的虚函数或纯虚函数进行了具体定义


## 构造函数
1. QAbstractListModel::QAbstractListModel(QObject \*parent = nullptr)


## 重定义的公共函数
1. [override virtual] bool QAbstractListModel::dropMimeData(const QMimeData \*data, Qt::DropAction action, int row, int column, const QModelIndex &parent)

2. [override virtual] Qt::ItemFlags QAbstractListModel::flags(const QModelIndex &index) const

3. [override virtual] QModelIndex QAbstractListModel::index(int row, int column = 0, const QModelIndex &parent = ...) const

4. [override virtual] QModelIndex QAbstractListModel::sibling(int row, int column, const QModelIndex &idx) const
