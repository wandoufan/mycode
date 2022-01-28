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
备注：这里设置的是UI窗口左上角显示的程序名  
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
```
ui -> pushButton -> setContextMenuPolicy(Qt::CustomContextMenu);
```

* void QWidget::setCursor(const QCursor &)
为这个widget对象设置一个光标，当鼠标位于widget内部时，会应用这个单独设置的光标  
如果没有设置光标，则默认使用widget对象的父类的光标  

* QCursor QWidget::cursor() const
查询当前widget对象使用的光标，返回一个QCursor  


## action相关的函数
所有的widget组件都有一个QAction类型的列表，列表有许多不同的表示形式  
默认的列表形式是创建一个QMenu(由actions()返回)  

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


## 坐标位置转换函数
* QPoint QWidget::mapFrom(const QWidget \*parent, const QPoint &pos) const
从指定父类widget中坐标位置映射到当前子类widget中的坐标位置  
parent不能为空指针，必须是被调用widget的父类  

* QPoint QWidget::mapFromGlobal(const QPoint &pos) const
把全局坐标位置映射为widget中的坐标位置  

* QPoint QWidget::mapFromParent(const QPoint &pos) const
从父类widget中的坐标位置转换到当前子类widget中的坐标位置  
如果当前widget没有父类，则效果等同于mapFromGlobal()函数  

* QPoint QWidget::mapTo(const QWidget \*parent, const QPoint &pos) const
从当前子类widget中的坐标位置映射到指定父类widget中坐标位置  
parent不能为空指针，必须是被调用widget的父类  

* QPoint QWidget::mapToGlobal(const QPoint &pos) const
把widget中的坐标位置映射为全局坐标位置  

* QPoint QWidget::mapToParent(const QPoint &pos) const
从当前子类widget中的坐标位置映射到父类widget中的坐标位置  
如果当前widget没有父类，则效果等同于mapToGlobal()函数  


## QWidget中鼠标操作相关的事件
* [virtual protected] void QWidget::mousePressEvent(QMouseEvent \*event)
当鼠标的光标在widget内部并按下了鼠标按键时，就会调用mousePressEvent()函数  
或者当widget被鼠标选中，鼠标使用gradMouse()函数，也会调用mousePressEvent()函数  
按下鼠标按键但是不释放(松开)，效果等同于调用grabMouse()函数  
注意：一般使用时对mousePressEvent函数进行重写  
头文件示例：  
```
class SkyplotWidget : public QWidget
{
protected:
    void mousePressEvent(QMouseEvent *event) override;
}
```
源文件示例：  
```
void SkyplotWidget::mousePressEvent(QMouseEvent *event)
{
    if(event -> button() ==  Qt::RightButton)//鼠标点击右键
    {
        mouse_pos = event -> pos();
        mouse_global_pos = event -> globalPos();
        menu -> exec(mouse_global_pos);
    }
}
```

* void QWidget::mouseReleaseEvent(QMouseEvent \*event)
当释放(松开)鼠标的按键时，就会调用mouseReleaseEvent()函数  
widget已经接收过mouse press事件之后，才能接收到mouse release事件  
这意味着，如果在widget内部按下鼠标，然后在释放鼠标之前将鼠标拖动到其他地方，widget将接收到release事件  
有一个例外情况：按下鼠标时出现一个弹出式菜单，则这个菜单会立刻接收到鼠标事件  

* void QWidget::mouseMoveEvent(QMouseEvent \*event)
当按下鼠标的按键并移动鼠标时，就会调用mouseMoveEvent()函数  
这个函数通常用在抓取和拖动的操作中  
注意：默认情况下，只有鼠标按键被按下时才会去追踪光标的位置  
如果想要在不按下鼠标按键的情况下，随时能够获取到光标的位置  
则需要调用'setMouseTracking(true)'函数  

* [virtual protected] void QWidget::mouseDoubleClickEvent(QMouseEvent \*event)
当用户在widge内部双击，就会调用mouseDoubleClickEvent()函数  
双击之后，widget会接收到两次mouse press事件和两次mouse release事件  
如果操作过程中鼠标没有保持稳定，也可能会接收到一些mouse move事件  
注意：在第二次点击完成之前，没有办法区分是单击还是双击  
因此，一般推荐把双击当做单击的扩展，而不是用双击和单击分别触发不同的action  

* void QWidget::grabMouse()
grabMouse()函数用来捕获鼠标的输入  
这个选中的widget会接收所有的鼠标事件，直到调用了releaseMouse()函数  
而其他未被选中的widget不会接收到任何鼠标事件  
注意：使用这个函数必须非常小心，经常容易造成Bug  
备注：在正常的QT程序中基本没有必要去获取鼠标，因此一般不用这个函数  
备注：只有可见的(visible)widget可以捕获到鼠标的输入  
