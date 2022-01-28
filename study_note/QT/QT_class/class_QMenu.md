# QMenu

## 基本功能
QMenu提供了菜单形式的widget，可以使用在菜单栏、上下文菜单和其他弹出式菜单中  
QMenu相当于菜单，QAction相当于菜单栏中的选项  
备注：如果要创建窗口上方工具栏里的菜单，使用QMenuBar  
父类：QWidget  
子类：无  


## 代码示例
详见最下面"下拉菜单的实现形式"  


## 构造函数
1. QMenu::QMenu(const QString &title, QWidget \*parent = nullptr)
如果这个menu对象用作另一个menu的子菜单，则title即为子菜单对应的选项的名字  

2. QMenu::QMenu(QWidget \*parent = nullptr)


## 常用成员变量
1. icon : QIcon
这个属性设置菜单的图标，等同于QAction::icon属性  
1.1 QIcon icon() const
1.2 void setIcon(const QIcon &icon)

2. separatorsCollapsible : bool

3. tearOffEnabled : bool

4. title : QString
这个属性设置菜单的标题，等同于QAction::text属性  
备注：这个标题其实就是菜单的文本内容  
4.1 QString title() const
4.2 void setTitle(const QString &title)

5. toolTipsVisible : bool


## 常用公共函数：添加子菜单
1. QAction \*QMenu::addMenu(QMenu \*menu)
添加一个已经创建好的子菜单，返回菜单关联的QAction对象  
```
QMenu *menu2 = new QMenu("submenu", this);
menu2 -> addAction("1");
menu2 -> addAction("2");
menu1 -> addMenu(menu2);
```

2. QMenu \*QMenu::addMenu(const QString &title)
创建并添加一个新的子菜单，返回这个子菜单对象  
```
QMenu *menu2 =  menu1 -> addMenu("submenu1");
menu2 -> addAction("a");
menu2 -> addAction("b");
```

3. QMenu \*QMenu::addMenu(const QIcon &icon, const QString &title)
创建并添加一个新的子菜单，返回这个子菜单对象  

4. QAction \*QMenu::insertMenu(QAction \*before, QMenu \*menu)
插入一个已经创建好的子菜单，返回菜单关联的QAction对象  


## 常用公共函数：添加子action
```
QMenu中的addAction()函数都是创建并添加一个新的action对象  
QMenu的父类QWidget中的addAction()函数是添加一个已经创建好的action对象  
```
1. QAction \*QMenu::addAction(const QString &text)

2. QAction \*QMenu::addAction(const QIcon &icon, const QString &text)

3. QAction \*QMenu::addAction(const QString &text, const QObject \*receiver, const char \*member, const QKeySequence &shortcut = 0)
在菜单中添加action时，顺便添加action的槽函数  
这个action的triggered()信号被连接到了接收对象的槽上  
```
menu1 -> addAction("show", this, SLOT(onShowAboutAction()));
```
也可以先添加action，添加完成后用connect函数连接槽函数  
注意：这里的信号函数一般都用triggered()  
```
connect(action1, SIGNAL(triggered()), this, SLOT(click_add()));
```

4. QAction \*QMenu::addAction(const QIcon &icon, const QString &text, const QObject \*receiver, const char \*member, const QKeySequence &shortcut = 0)
和上面函数功能一样，只是在创建action时多了一个图标  

5. template <typename Functor> QAction \*QMenu::addAction(const QString &text, Functor functor, const QKeySequence &shortcut = 0)

6. template <typename Functor> QAction \*QMenu::addAction(const QString &text, const QObject \*context, Functor functor, const QKeySequence &shortcut = 0)

7. template <typename Functor> QAction \*QMenu::addAction(const QIcon &icon, const QString &text, Functor functor, const QKeySequence &shortcut = 0)

8. template <typename Functor> QAction \*QMenu::addAction(const QIcon &icon, const QString &text, const QObject \*context, Functor functor, const QKeySequence &shortcut = 0)


## 常用公共函数：添加子section
section的接口函数和action的接口函数很类似，返回值也是一个QAction指针  
但是没搞明白这个section有什么作用，实际测试添加section后也没有任何显示  


## 常用公共函数：其他
1. QAction \*QMenu::addSeparator()
在当前菜单中添加一个空白的action，显示效果为在菜单选项中添加一个空白分割  
```
menu1 -> addSeparator();
```

2. QAction \*QMenu::exec()
同步执行当前菜单，返回触发的action，如果没有触发action则返回空  
常用用法包括：  
```
//1. 根据当前鼠标位置
menu1 -> exec(QCursor::pos());
//2. 和某个widget保持一致
menu1 -> exec(somewidget.mapToGlobal(QPoint(0,0)));
//3. 根据QMouseEvent *event进行反应
menu1 -> exec(event -> globalPos());
```

3. QAction \*QMenu::defaultAction() const

4. void QMenu::setDefaultAction(QAction \*act)
设置默认要执行的action  

5. QAction \*QMenu::activeAction() const

6. void QMenu::setActiveAction(QAction \*act)
设置当前高亮的action  

---------------------------------------------------------------

## 下拉菜单的实现形式
1. 指定组件设置左键下拉式菜单
不需要右键，左键点击按钮时弹出下拉菜单  
```
ui -> pushButton -> setMenu(menu1);
```

2. 指定组件设置右键弹出式菜单
备注：在组件上点击右键时，组件本身是无法感知到点击的  
方法1：用connect函数关联起来  
```
ui -> pushButton -> setContextMenuPolicy(Qt::CustomContextMenu);
connect(ui->pushButton,&QPushButton::customContextMenuRequested,[=](const QPoint &pos)
    {
        qDebug() << pos;
        menu1 -> exec(QCursor::pos());
    });
```
方法2：  
```

```

3. 在窗口任意位置右键弹出菜单
不关联某个组件，鼠标指到哪里就在哪里弹出菜单  
方法1（简单写法）：直接在构造函数里添加action  
```
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    addAction(new QAction("add", this));
    addAction(new QAction("modify", this));
    addAction(new QAction("delete", this));

    setContextMenuPolicy(Qt::ActionsContextMenu);
}
```
方法2（复杂写法）：对mousePressEvent函数进行重写  
头文件  
```
protected:
    void mousePressEvent(QMouseEvent *event) override;
```
源文件  
```
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    action1 = new QAction("add", this);
    action2 = new QAction("modify", this);
    action3 = new QAction("delete", this);
    menu1 = new QMenu(this);
    menu1 -> addAction(action1);
    menu1 -> addAction(action2);
    menu1 -> addAction(action3);

    connect(action1, SIGNAL(triggered()), this, SLOT(click_add()));
    connect(action2, SIGNAL(triggered()), this, SLOT(click_modify()));
    connect(action3, SIGNAL(triggered()), this, SLOT(click_delete()));
}

void MainWindow::mousePressEvent(QMouseEvent *event)
{
    if(event -> button() ==  Qt::RightButton)//判断当前事件为鼠标右击
    {
    	//注意：这里一定要用globalPos()函数，不能用pos()函数
        QPoint mouse_pos = event -> globalPos();//鼠标当前位置
        menu1 -> exec(mouse_pos);
    }
}
```