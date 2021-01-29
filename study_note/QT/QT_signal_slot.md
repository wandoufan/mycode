# QT中的信号与槽

## 信号与槽(signal & slot)机制的原理
1. 信号(signal)就是在特定情况下被触发的事件  
例如，PushButton最常见的信号就是鼠标单击时发射的clicked()信号  
2. 槽(slot)就是对信号响应的函数  
一个槽就是一个函数，与一般的C++函数是一样的，可以具有任何参数，也可以被直接调用  
也可以定义在类的任何部分(private、public或protected)  
槽函数与一般函数的不同的是：槽函数可以与一个信号关联，信号发射时槽函数自动执行  
3. SIGNAL和SLOT  
SIGNAL和SLOT是QT的宏，用于指明信号和槽，必须用它们将信号函数和槽函数包起来  


## connect()函数
1. 基本功能
```
[static] QMetaObject::Connection QObject::connect(const QObject *sender, const char *signal, const QObject *receiver, const char *method, Qt::ConnectionType type = Qt::AutoConnection)
```
connect函数用来创建信号函数与槽函数之间的关联关系  
如果连接成功，会返回一个连接句柄，这个句柄可以用来在随后关闭该连接  
如果连接失败，会返回一个非法的连接句柄  
2. 参数作用
sender是发射信号的对象的名称  
signal()是信号名称，相当特殊的函数，需要带括号，有参数时需要指明参数类型  
receiver是接收信号的对象的名称，常用this代表当前对象  
slot()是槽函数的名称，需要带括号，有参数时需要指明参数类型  
3. 注意事项
3.1 connect()是QObject类的一个静态函数，可以不经实例化而直接使用  
因此可以直接写为connect(sender, SIGNAL(signal()), receiver, SLOT(slot()));  
3.2 connect函数一般写在类的构造函数中  
3.3 信号函数与槽函数的参数只能写出参数类型，不能包含任何具体的参数名  
```
QLabel *label = new QLabel;
QScrollBar *scrollBar = new QScrollBar;
//正确写法
QObject::connect(scrollBar, SIGNAL(valueChanged(int)),
              label,  SLOT(setNum(int)));
//错误写法
QObject::connect(scrollBar, SIGNAL(valueChanged(int value)),
              label, SLOT(setNum(int value)));
```


## 槽函数的执行方式
1. 同步调用
发出信号后，当前线程等待槽函数执行完毕后，才会继续执行下面的语句  
2. 异步调用
发出信号后，立即执行下面的语句，不关心槽函数什么时候执行  
3. 注意事项
一定是发出信号函数之后，才可能开始执行槽函数，并不是程序执行到connect()函数时就自动去执行槽函数  
遇到槽函数最后才执行的问题，不一定是异步调用造成的，也需要检查一下是否触发了信号函数  


## connect()函数的ConnectionType参数
ConnectionType参数用来设置连接的类型，包括以下5种取值：  
1. Qt::AutoConnection（默认值）
当sender和receiver在同一个线程中时，采用Qt::DirectConnection类型  
当sender和receiver在不同线程中时，采用Qt::QueuedConnection类型  

2. Qt::DirectConnection
当信号函数发出时，槽函数立即被调用，槽函数是在sender的线程中被执行  
当sender和receiver在同一个线程中时，同步调用  
当sender和receiver在不同线程中时，同步调用，但有线程安全隐患  

3. Qt::QueuedConnection
当控制器返回到了receiver的线程之后，槽函数才在receiver的线程中被执行  
当sender和receiver在同一个线程中时，通过事件队列异步调用  
当sender和receiver在不同线程中时，通过事件队列异步调用，线程安全  
备注：使用该连接类型时，参数必须是QT元对象系统已知的  
如果参数是自己定义的，则在建立连接前需要先向元对象系统注册参数的类型  
注册方法详见帮助文档的说明  

4. Qt::BlockingQueuedConnection
和Qt::QueuedConnection基本相同，区别在于：  
sender的线程一直是锁死的状态，直到槽函数执行完返回
其中，槽函数也是在receiver的线程中被执行  
当sender和receiver在同一个线程中时，不可用  
当sender和receiver在不同线程中时，通过事件队列异步调用，线程安全  
注意：只有当sender和receiver在不同线程时，才可以使用该参数，否则程序会死锁(deadlock)

5. Qt::UniqueConnection
UniqueConnection参数可以用来防止重复连接，严格来说不算连接类型  
如果设置了该参数，在连接已经存在时，再建立一个完全相同的连接会失败  


## 信号函数和槽函数的具体写法示例
注意：信号函数和槽函数必须在类中进行相应的声明，否则connect函数识别不到  
备注：信号函数只需要声明即可，不需要写出其具体定义；槽函数既需要声明也需要定义  
```
class QDESIGNER_WIDGET_EXPORT CustomButton : public QWidget
{
    Q_OBJECT
    Q_PROPERTY(bool Value READ Value WRITE SetValue NOTIFY valuechanged) //NOTIFY关键字后面是信号函数

public:
    CustomButton(QWidget *parent = 0);

public:
    bool Value();
    void SetValue(bool value);

//signals声明信号函数
signals:
    void ValueChanged(bool value);
    
//slots声明槽函数
private slots:
    void on_checkBox_clicked(bool checked);
}
```
在写函数的具体定义中要加上触发信号函数的语句  
使用emit关键字表示触发信号函数  
```
void CustomButton::SetValue(bool value)
{
    qt_button -> SetValue(value);
    emit valuechanged(); //执行写函数时触发信号函数
}
```


## 信号与槽的使用规则
1. 一个信号可以与多个槽关联，槽函数按建立连接时的顺序依次执行  
例如：当spinNum对象的数值变化时，addFun()和updateStatus()会依次响应  
```
connect(spinNum, SIGNAL(valueChanged(int)), this, SLOT(addFun(int));
connect(spinNum, SIGNAL(valueChanged(int)), this, SLOT(updateStatus(int));
```
2. 一个槽可以被多个信号关联  
例如：下面三个信号都可以触发槽函数setTextFontColor()  
```
connect(ui->rBtnBlue, SIGNAL(clicked()), this, SLOT(setTextFontColor()));
connect(ui->rBtnRed, SIGNAL(clicked()), this, SLOT(setTextFontColor()));
connect(ui->rBtnBlack, SIGNAL(clicked()), this, SLOT(setTextFontColor()));
```
3. 一个信号可以连接另一个信号，一个信号发射时也会发射另一个信号  
例如：valueChanged()函数会触发refreshInfo()函数  
```
connect(spinNum, SIGNAL(valueChanged(int)), this, SIGNAL(refreshInfo(int));
```
4. 信号的参数与槽的参数个数和类型都要一致  
至少信号的参数不能少于槽的参数，否则会编译报错  
5. 在使用信号与槽的函数的类中，必须在类的定义中加入宏Q_OBJECT  
而且，信号和槽必须得是类的成员函数  
6. 当一个信号发射时，与其关联的槽函数都会立即执行  
只有在信号关联的槽函数都执行完毕之后才会执行信号后面的代码  


## 设置信号与槽的四种方法
1. 在UI设计界面下方的编辑器中设置槽和信号  
设置完成后可以直接生效，其中槽函数只能从系统提供的常规函数中去选择  
2. 点击上方工具栏中的"Edit Signals\Slots"即可进入到信号与槽编辑模式  
选中一个组件作为sender，然后按住鼠标左键将其箭头拖动到其他组件处作为receiver  
在弹出的列表框中分别选择信号和槽函数，设置完成后可以直接生效，其中槽函数只能从系统提供的常规函数中去选择  
3. 可以在dialog.cpp文件中自定义出一个符合我们需要的槽函数  
选中需要设置的组件，右键'转到槽'，之后由系统自动创建出的槽函数框架，完成函数内容即可  
其中connect函数不需要再手动写出，由系统编译后在ui_dialog.h文件中调用setupUi()函数实现关联  
槽函数名是系统根据组件名自动创建出来的，例如void Dialog::on_checkBox_clicked(bool checked)  
注意：系统是根据槽函数名来实现信号和槽的关联，不要随意改动槽函数名  
4. 可以将多个信号(组件)关联到一个自定义的槽函数上，此时槽函数是一个复合函数  
复合函数不需要对应一个具体的组件，而是多个组件都通过connect函数关联到这个复合函数上  
需要手动在类的构造函数下加入connect函数，将不同信号和函数中不同操作关联起来  
构造函数示例：  
```
Dialog::Dialog(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::Dialog)
{
    ui->setupUi(this);
    connect(ui -> radioButton, SIGNAL(clicked()), this, SLOT(setTextFontColor()));
    connect(ui -> radioButton_2, SIGNAL(clicked()), this, SLOT(setTextFontColor()));
    connect(ui -> radioButton_3, SIGNAL(clicked()), this, SLOT(setTextFontColor()));
}
```
槽函数定义示例：  
```
void Dialog::setTextFontColor()
{
    QPalette plet = ui -> plainTextEdit -> palette();
    if (ui -> radioButton -> isChecked())
        plet.setColor(QPalette::Text, Qt::black);
    else if (ui -> radioButton_2 -> isChecked())
        plet.setColor(QPalette::Text, Qt::red);
    else if (ui -> radioButton_3 -> isChecked())
        plet.setColor(QPalette::Text, Qt::blue);
    else
        plet.setColor(QPalette::Text, Qt::yellow);
    ui -> plainTextEdit -> setPalette(plet);
}
```


## 常用的系统自带信号
1. void clicked()
当鼠标左键被按下并释放时(即点击一次)会触发clicked()函数  
clicked信号关联的槽函数是不带参数的，无法直接获取button的checkable状态  
2. void clicked(bool checked = false)
当鼠标左键被按下并释放时(即点击一次)会触发clicked(bool)函数，并将当前button的状态传递给外界  
3. pressed()
当鼠标指针在按钮上时点击左键会触发pressed函数  
4. released()
当鼠标左键被释放时会触发released函数  
5. toggled()
当一个checkable button的标记状态发生改变时会触发toggled()函数  
6. toggled(bool)
当一个checkable button的标记状态发生改变时会触发toggled(bool)函数，并将当前状态传递给外界  
如果button是checked状态时，checked参数值为true；  
如果button时unchecked状态时，checked参数值为false；  
7. stateChanged(int)
8. accepted()
当对话框被交互式的关闭或调用accept函数关闭时就会触发accepted信号  
当使用close函数关闭对话框时不会发出accepted信号  
corresponding handler是onAccepted状态  
9. rejected()
当对话框被交互式的关闭或调用reject函数关闭时就会触发rejected信号  
当使用close函数关闭对话框时不会发出rejected信号  
corresponding handler是onRejected状态  
10. triggered()
triggered函数一般用于组件的右键菜单中，被QAction等被触发  


## clicked()和clicked(bool)的比较
1. 相同点：
clicked()和clicked(bool)都会被鼠标左键点击一次而触发  
2. 不同点：
clicked()关联的槽函数是不带参数的，clicked(bool)关联的槽函数是带有参数的  
例如，void on_checkBox_clicked(bool checked)  
如果button是checked状态时，checked参数值为true；  
如果button时unchecked状态时，checked参数值为false；  
clicked(bool) 会将CheckBox组件当前的选择状态作为一个参数传递给关联槽函数  
而如果用clicked()，则需要在槽函数中用代码去读取CheckBox组件的选中状态  


## toggled()和clicked()的比较
1. 相同点：
当点击按钮时，状态信号都会被发送  
2. 不同点：
toggled要比clicked更容易触发  
clicked有的toggled有，而toggled有的，clicked却不一定有  
当调用setDown(),setChecked()或toggle()函数时，clicked不会被触发  
当用户有点击行为，或调用setChecked()函数时，都会触发toggled  


## toggle和trigger的比较
toggle可以理解为开关，可以勾选为开或关的状态  
trigger可以理解为扳机，只点击一次  


## 常用的系统自带槽函数
备注：槽函数一般不在代码中直接被调用，点击button发出信号时就相当于调用了槽函数  
1. void close()
close函数关闭对话框  
2. void accept()
accept函数关闭对话框并发出accepted信号  
3. void reject()
reject函数关闭对话框并发出rejected信号  
4. void done(int result)
done函数关闭对话框并设置result结果  
5. bool open(QIODevice::OpenMode flags)
open函数打开对话框  
4. void quit()
quit函数正常的退出一个事件循环，相当于exit(0)  
5. void exit(int returnCode = 0)
exit函数退出一个事件循环并返回一个代码，0代表成功，非0值代表有错误  
6. int exec(QEventLoop::ProcessEventsFlags flags = AllEvents)
exec函数进入到主事件循环中并等待到exit函数被调用，然后返回exit函数的那个返回代码  
即exec()函数弹出的窗口可以一直保持，除非手动关闭  
exec()函数只能在窗口类QDialog中使用，不能在QWidget类中使用  
7. show()
show()函数用来调用显示一个非模式对话框，执行完成后返回主事件中  
即show()函数弹出一个对话框之后会很快自动关闭  


## on_pushButton_clicked函数
注意：这个函数是一个槽函数，而不是信号函数  
这个槽函数是最常见的命名方式，由系统自动生成  
这个槽函数对应的信号是clicked()函数，当点击按钮时会触发  