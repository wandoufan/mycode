# QAction

## 基本功能
QAction类提供了抽象的用户界面action，这些action可以插入widget组件中  
QAction的父类是QObject，子类是QWidgetAction  
所有的widget组件都有一个QAction类型的列表，列表有许多不同的表示形式  
默认的列表形式是创建一个QMenu(由actions()返回)  
QMenu相当于菜单，QAction相当于菜单栏中的选项  


## 注意事项
1. 对于每种类型action，一个widget组件最多只能有一个aciton
同一个action向widget组件中添加两次，也不会执行action两次  
2. 一个widget组件，默认aciton列表是空的  


## 向Widget的actions列表中进行增删改查
相关函数详见QT_function.md  


## 构造函数
1. QAction::QAction(QObject \*parent = nullptr)
用父指针来构造一个action对象  
如果父指针指向一个action列表，则这个构造的action对象会被自动插入action列表中  

2. QAction::QAction(const QString &text, QObject \*parent = nullptr)
用text和父指针来构造一个action对象，text为选项的名称  
如果父指针指向一个action列表，则这个构造的action对象会被自动插入action列表中  
```
QAction *action_add；
action_add = new QAction("add channel", this);
```

3. QAction(const QIcon &icon, const QString &text, QObject \*parent = nullptr)
用图标、text和父指针来构造一个action对象  
如果父指针指向一个action列表，则这个构造的action对象会被自动插入action列表中  


## 常用函数