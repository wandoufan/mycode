# QAction

## 基本功能
QAction类提供了创建action的接口，这些action可以插入widget组件中  
QMenu相当于菜单，QAction相当于菜单栏中的选项  
父类：QObject  
子类：QWidgetAction  


## 注意事项
1. 对于每种类型action，一个widget组件最多只能有一个aciton
同一个action向widget组件中添加两次，也不会执行action两次  
2. 一个widget组件，默认aciton列表是空的  


## 创建action的方法
可以用QAction的构造函数来单独创建action对象，这样可以对action对象的各种属性进行详细设置
也可以直接使用QMenu::addAction()函数来创建并添加action对象，这样只设置text、icon等最常用属性  


## 添加action的方法
1. QWidget::addAction()
添加一个已经创建好的action对象  
2. QGraphicsWidget::addAction()
3. QMenu::addAction()
创建并添加一个新的action对象  


## 使用action的方法
一个action可以理解为一条指令，可以用作信号与槽机制中的发射信号的对象  
action设置完成后，一般要通过connect()函数与对应的槽函数关联起来  
```
connect(action1, SIGNAL(triggered()), this, SLOT(click_add()));
connect(action2, SIGNAL(triggered()), this, SLOT(click_modify()));
connect(action3, SIGNAL(triggered()), this, SLOT(click_delete()));
```


## 向Widget的actions列表中进行增删改查
相关函数详见QT_function.md  


## 构造函数
1. QAction::QAction(QObject \*parent = nullptr)
如果parent指向一个action列表，则这个构造的action对象会被自动插入action列表中  

2. QAction::QAction(const QString &text, QObject \*parent = nullptr)

3. QAction(const QIcon &icon, const QString &text, QObject \*parent = nullptr)


## 常用成员变量
1. autoRepeat : bool

2. checkable : bool

3. checked : bool

4. enabled : bool

5. font : QFont

6. icon : QIcon

7. iconText : QString

8. iconVisibleInMenu : bool

9. menuRole : MenuRole

10. priority : Priority

11. shortcut : QKeySequence

12. shortcutContext : Qt::ShortcutContext

13. shortcutVisibleInContextMenu : bool

14. statusTip : QString
这个属性设置action的状态文本  
当鼠标放在这个选项上之后，会在窗口的左下角自动出现设置的状态文本  

15. text : QString

16. toolTip : QString
这个属性设置action的工具提示文本  
备注：实测设置之后，鼠标放到选项上也没有任何反应  

17. visible : bool

18. whatsThis : QString
这个属性设置action的whatsThis文本  
备注：实测设置之后，鼠标放到选项上也没有任何反应  


## 常用公共函数
无

