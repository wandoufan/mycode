# PluginDetailsView中的函数

## 基本说明
这些函数都是控件对象可以调用的与UI界面相关的函数  
详见QT帮助的'List of All Members for PluginDetailsView'  
备注：这些函数都是Widget的成员函数，因此对象类型必须是继承于QWidget的才能调用  


## 注意事项
1. 这里有很多函数都可以不经过实例化而直接调用  
即可以直接写函数名，前面没有对象或者指针来调用这个函数  
例如：下面两种写法都合法  
```
setWindowTitle("汉王手写签字板ESP370");
this -> setWindowTitle("汉王手写签字板ESP370");
```


## 组件属性设置相关的函数
* void setWindowTitle(const QString &)
窗口的标题名称默认是自己定义的类名，也可以用setWindowTitle函数进行修改  
一般在类的构造函数里来使用setWindowTitle函数  
```
setWindowTitle("汉王手写签字板ESP370");
```

* void QWidget::setFixedSize(int , int )
设置某个对象对应控件的大小，第一个参数是宽度，第二个参数是高度  
有的窗口在UI设计界面中可能显示不出来，就可以通过这个函数来调整大小  
```
//必须要通过某个对象来调用该函数
m_pHWPenSign->setFixedSize(600, 160);
```

* void QWidget::setGeometry(int , int , int , int )
设置某个对象对应控件的大小和位置  
其中，x坐标和y坐标的位置是相对于UI窗口的左上角，或显示屏的左上角  
第一个参数为x坐标  
第二个参数为y坐标  
第三个参数为控件的宽度  
第四个参数为控件的高度  

* void QWidget::show()
显示这个Widget对象及其子对象  
调用show()函数等同于调用showFullScreen()、showMaximized()、或setVisible(true)，具体取决于平台的默认选择  

* virtual void setVisible(bool)
设置Widget对象是否可见  

* void QWidget::setHidden(bool)
等同与setVisible(!hidden)  

* void QWidget::setLayout(QLayout \*layout)
设置Widget组件的内部布局形式  

* [slot] void QWidget::update()
这是一个槽函数，用来更新widget组件  
如果组件是disabled状态或者被隐藏了，则update函数不起作用  

* void setContextMenuPolicy(Qt::ContextMenuPolicy policy)
设置Widget组件如何显示快捷菜单，快捷菜单可以通过鼠标右键触发  
参数取值包括：  
1. Qt::NoContextMenu
组件没有快捷菜单，快捷菜单的访问请求会被转发给组件的父对象  
2. Qt::PreventContextMenu
组件没有快捷菜单，快捷菜单的访问请求也不会被转发给组件的父对象  
点击鼠标右键时，访问请求通过QWidget::mousePressEvent()和QWidget::mouseReleaseEvent()传送给了组件本身  
3. Qt::DefaultContextMenu（默认取值）
调用QWidget::contextMenuEvent()  
4. Qt::ActionsContextMenu
调用QWidget::actions()  
5. Qt::CustomContextMenu
调用QWidget::customContextMenuRequested()  
具体相应动作由信号对应的槽函数处理  



## action相关的函数
* QList<QAction \*> QWidget::actions() const
返回Widget组件的actions的列表(可能为空)  

* void QWidget::addAction(QAction \*action)
向Widget组件的actions列表中添加一个action(append方式添加)  

* void QWidget::addActions(QList<QAction \*> actions)
和上面函数功能类似，插入一个actions列表  
向Widget组件的actions列表中添加多个action组成的列表(append方式添加)  

* void QWidget::removeAction(QAction \*action)
从Widget组件的actions列表中删除一个action  

* void QWidget::insertAction(QAction \*before, QAction \*action)
向Widget组件的actions列表中插入一个action，插入位置在before之前  
当before是空指针或非法值时，会以append方式添加到列表的尾部  

* void QWidget::insertActions(QAction \*before, QList<QAction \*> actions)
和上面函数功能类似，插入一个actions列表  


## 鼠标操作相关的函数
1. void QWidget::mousePressEvent(QMouseEvent \*event)
一般使用时对mousePressEvent函数进行重写  
头文件示例：  
```
protected:
    void mousePressEvent(QMouseEvent *event) override;
```
源文件示例：  
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
2. void QWidget::mouseReleaseEvent(QMouseEvent \*event)

3. void QWidget::mouseMoveEvent(QMouseEvent \*event)