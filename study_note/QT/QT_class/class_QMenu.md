# QMenu

## 基本功能
QMenu提供了菜单形式的widget，可以使用在菜单栏、上下文菜单和其他弹出式菜单中  
QMenu的父类是QWidget  
QMenu相当于菜单，QAction相当于菜单栏中的选项  
如果要创建窗口上方工具栏里的菜单，使用QMenuBar  


## 构造函数
1. QMenu::QMenu(const QString &title, QWidget \*parent = nullptr)
用title和父指针构造一个menu对象  
如果这个menu对象用作另一个menu的子菜单，则title即为子菜单对应的选项的名字  
```
menu1 = new QMenu("submenu", this);
```
2. QMenu::QMenu(QWidget \*parent = nullptr)
用父指针构造一个menu对象  
```
menu1 = new QMenu(this);
```


## 添加子菜单的函数
1. QAction \*QMenu::addMenu(QMenu \*menu)
在当前菜单中添加一个已经创建好的子菜单，返回菜单的menuAction()  
新添加的子菜单没有菜单的所有权  
```
QMenu *menu2 = new QMenu("submenu", this);
menu2 -> addAction("1");
menu2 -> addAction("2");
menu1 -> addMenu(menu2);
```
2. QMenu \*QMenu::addMenu(const QString &title)
在当前菜单中用title添加一个新的子菜单，返回这个子菜单对象  
其中，title即为子菜单对应的选项的名字  
```
QMenu *menu2 =  menu1 -> addMenu("submenu1");
menu2 -> addAction("a");
menu2 -> addAction("b");
```
3. QMenu \*QMenu::addMenu(const QIcon &icon, const QString &title)
在当前菜单中用图标和title添加一个新的子菜单，返回这个子菜单对象  


## 添加Action的函数
1. QMenu::addAction(QAction \*act)
向当前菜单中添加一个已经创建好的action对象  
```
menu1 -> addAction(action1);
```
2. QAction \*QMenu::addAction(const QString &text)
在当前菜单中用text添加一个新的action，返回这个action对象  
这个action对象的父指针默认为当前菜单  
```
QAction *action1 = menu1 -> addAction("add");
```
3. QAction \*QMenu::addAction(const QIcon &icon, const QString &text)
在当前菜单中用图标和text添加一个新的action，返回这个action对象  
4. QAction \*QMenu::addAction(const QString &text, const QObject \*receiver, const char \*member, const QKeySequence &shortcut = 0)
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
5. QAction \*QMenu::addAction(const QIcon &icon, const QString &text, const QObject \*receiver, const char \*member, const QKeySequence &shortcut = 0)
和上面函数功能一样，只是在创建action时多了一个图标  


## 其他常用函数
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