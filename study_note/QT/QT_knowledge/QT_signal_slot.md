# QT中的信号与槽

## 信号与槽(signal & slot)机制的原理
1. 信号(signal)就是在特定情况下被触发的函数  
信号函数的返回类型都是void，不能指望从信号函数中返回有效信息  
信号函数只用signals作标识，没有private、public或protected的区分  
信号函数只需要声明即可，不需要写出其具体定义  
2. 槽(slot)就是对信号响应的函数  
一个槽就是一个函数，与一般的C++函数是一样的，可以具有任何参数，也可以被直接调用  
槽函数与一般函数的不同的是：槽函数可以与一个信号关联，信号发射时槽函数自动执行  
槽函数可以声明在类的任何部分(private、public或protected)  
槽函数既需要声明也需要定义  
备注：一个槽并不知道是否有任何信号与自己相关联  


## 信号与槽的性能问题
一般情况下，信号与槽机制的性能都可以满足使用，很难感知到其性能问题  
但在时间敏感的功能中，如计算时间戳，使用过多的信号与槽会带来明显的延时  
这种情况下，建议直接采用回调方式  
问题原因是Qt信号槽机制涉及函数查找及参数传递，其中包含了链表操作、事件处理以及线程中锁部分的处理  
一般情况下，信号槽与回调的效率有10倍之差，情况复杂时远不止10倍  


## 声明信号与槽函数
1. signals和slots
小写的signals和slots是Qt提供的关键字，这也是最常用的方式  
```
public slots:
    void func_slot();

signals:
    void func_signal();
```
2. Q_SIGNAL和Q_SLOT
Q_SIGNAL和Q_SLOT是由QObject类提供的宏，可以将单个函数标记为信号函数和槽函数  
当你使用第三方信号与槽机制时，可以用来替代signals和slots关键字  
一般的，当.pro文件中有`CONFIG += no_keywords`时使用这两个宏  
```
public Q_SLOT:
    void func_slot();

Q_SIGNAL:
    void func_signal();
```
3. Q_SIGNALS和Q_SLOTS
Q_SIGNAL和Q_SLOT是由QObject类提供的宏，可以将函数标记为信号函数和槽函数  
当你使用第三方信号与槽机制时，可以用来替代signals和slots关键字  
一般的，当.pro文件中有`CONFIG += no_keywords`时使用这两个宏  
```
public Q_SLOTS:
    void func_slot1();
    void func_slot2();

Q_SIGNALS:
    void func_signal1();
    void func_signal2();
```
4. 第三方信号与槽机制
除了Qt自身提供的信号与槽机制，Qt还支持使用第三方信号与槽机制  
甚至还可以在同一个项目中同时使用这两种机制，只需要在.pro文件中加上如下语句  
```
CONFIG += no_keywords
```
这会告诉Qt不要去定义关键字signals、slots、emit，因为这些名字将要被第三方库去使用  
自己在声明信号与槽函数时，用下面的宏来替代关键字名字  
Q_SIGNAL、Q_SLOT、Q_SIGNALS、Q_SLOTS、Q_EMIT  
备注：关于第三方信号与槽机制，没有实际用过，也不太了解  


## 槽函数的类型
1. public slots:
任何对象的信号函数都可以和该槽函数关联  
适用于彼此互不了解的对象之前进行数据通信  
2. protected slots:
当前类及其子类的信号函数可以和该槽函数关联  
3. private slots:
只有类自己可以将信号与该槽函数关联  


## emit关键字
系统自带的信号函数如clicked()可以直接使用，自定义的信号函数必须在相应的位置用emit关键字来表示触发信号函数


## connect()函数
1. 基本功能
```
[static] QMetaObject::Connection QObject::connect(const QObject *sender, const char *signal, const QObject *receiver, const char *method, Qt::ConnectionType type = Qt::AutoConnection)
```
connect函数用来创建信号函数与槽函数之间的关联关系  
如果连接成功，会返回一个连接句柄，这个句柄可以用来在随后关闭该连接  
如果连接失败，会返回一个非法的连接句柄  
2. 参数作用
sender是发射信号的对象指针的名称  
signal()是信号名称，相当特殊的函数，需要带括号，有参数时需要指明参数类型  
receiver是接收信号的对象指针的名称，常用this代表当前对象  
slot()是槽函数的名称，需要带括号，有参数时需要指明参数类型  


## connect()函数注意事项
1. connect()是QObject类的一个静态函数，可以不经实例化而直接使用
```
connect(sender, SIGNAL(signal()), receiver, SLOT(slot()));
```
2. 使用信号与槽的类中必须加入Q_OBJECT宏，而且信号和槽必须得是类的成员函数
```
class MainWindow : public QMainWindow
{
    Q_OBJECT
    ...
```
否则会产生报错：
```
LNK2019: 无法解析的外部符号...
```
3. connect函数有两种写法，实现的效果相同
```
//写法一：Qt4语法风格(常用标准写法)
connect(ui -> checkBox, SIGNAL(clicked(bool)), this, SLOT(click_test(bool)));
//写法二：Qt5语法风格(不再使用SIGNAL和SLOT标识，也不再写出函数参数)
connect(ui -> checkBox, &QAbstractButton::clicked, this, &MainWindow::click_test);
```
4. sender和receiver都必须是指针类型，如果不是，前面要加上&  
```
QThreadSend thread_send;
QThreadReceive thread_receive;
connect(&thread_send, SIGNAL(sendData(int)), &thread_receive, SLOT(receiveData(int)));
```
否则会产生报错：
```
error: no matching member function for call to 'connect'
```


## 信号与槽的函数参数说明
1. 语法格式
信号函数与槽函数的参数只能写出参数类型，不能包含任何具体的参数名  
另外，信号函数和槽函数即使没有参数，也要写出括号，不能省略  
```
QLabel *label = new QLabel;
QScrollBar *scrollBar = new QScrollBar;
//正确写法
QObject::connect(scrollBar, SIGNAL(valueChanged(int)), label, SLOT(setNum(int)));
//错误写法
QObject::connect(scrollBar, SIGNAL(valueChanged(int value)), label, SLOT(setNum(int value)));
```
2. 参数个数要求
信号函数的参数个数要大于或等于槽函数的参数，否则会编译报错  
当参数个数相等时，参数的类型和顺序要完全相同  
当信号函数参数较多时，前面部分的参数的类型和顺序要完全相同，信号中多余的参数会被忽略  
备注：在Qt的信号与槽机制中，信号函数最多能携带6个参数  
3. 参数类型
正常情况下信号与槽之间只能传递通用数据类型，如int、string等  
复杂数据如QVector<int>、结构体等类型就不能传递了  
如果需要传递复杂数据，则要先将复杂数据包成通用类型的数据  
```
https://blog.csdn.net/a1356467/article/details/108519772
```


## 使用lambda表达式来向槽函数传递更多参数
1. 场景说明
在使用Qt预定义的信号函数(如clicked()等信号)时，信号中的参数是无法修改的  
但有的时候，除了信号函数中的参数，槽函数还需要获取额外的参数  
例如：需要传送一个或多个参数给槽函数进行相应的运算  

2. 语法说明： 
2.1. connect函数中可以只有三个参数，第3个参数this可以省略
```
connect(ui -> pushButton, &QPushButton::clicked, [=](){click_test1(i);});
```
2.2 如果[]中写的是"="，则传递到槽函数的参数可以是一个局部变量，也可以是类的成员变量
如果[]中写的是"this"，则传递到槽函数的参数必须是类的成员变量
详见lambda表达式的语法  
2.3. 不再使用SINGAL和SLOT标识符
信号函数不再写为'SIGNAL(clicked())'，而是'&QPushButton::clicked'  
2.4. 槽函数写在lambda的函数体中，即通过lambda函数再去调用槽函数

3. 当信号函数本身没有参数时(如clicked()信号)
```
//示例1：槽函数为click_test1(int i)函数，其包含了一个参数 
int i = 10;
connect(ui -> pushButton, &QPushButton::clicked, this, [=](){click_test1(i);});
void MainWindow::click_test1(int i)
{
    qDebug() << "click_test1 : " << i;
}

//示例2：槽函数为click_test1(int i, int j, int k)函数，其包含了多个参数  
connect(ui -> pushButton, &QPushButton::clicked, this, [=](){click_test1(1, 2, 3);});//可以直接把参数值写进去
void MainWindow::click_test1(int i, int j, int k)
{
    qDebug() << "click_test1 : " << i << ", " << j << ", " << k;
}
```
备注：这里也可以使用QSignalMapper机制，但QSignalMapper已过时而且使用局限较多，不建议使用  

4. 当信号函数本身就带有参数时(如clicked(bool)信号)
```
//示例1：
m_count = 1;
connect(ui -> checkBox, &QAbstractButton::clicked, [this](bool checked){click_test2(checked, m_count);});
void MainWindow::click_test2(bool checked, int count)
{
    qDebug() << "click_test2 : " << checked << ", " << count;
}

//示例2：也可以不使用lambda表达式，改为设置另一个槽函数来作为中间传递
connect(ui -> checkBox, SIGNAL(clicked(bool)), this, SLOT(click_test2_temp(bool)));
void MainWindow::click_test2_temp(bool checked)
{
    int i = 10;
    click_test2(checked, i);
}
```


## 信号与槽的使用规则
1. 一个信号可以关联多个槽，槽函数按建立连接时的顺序依次执行  
例如：当spinNum对象的数值变化时，addFun()和updateStatus()会依次响应  
```
connect(spinNum, SIGNAL(valueChanged(int)), this, SLOT(addFun(int));
connect(spinNum, SIGNAL(valueChanged(int)), this, SLOT(updateStatus(int));
```
2. 多个信号可以关联到一个槽
例如：下面三个信号都可以触发槽函数setTextFontColor()  
```
connect(ui -> radioButton, SIGNAL(clicked()), this, SLOT(setTextFontColor()));
connect(ui -> radioButton_2, SIGNAL(clicked()), this, SLOT(setTextFontColor()));
connect(ui -> radioButton_3, SIGNAL(clicked()), this, SLOT(setTextFontColor()));

```
3. 一个信号可以连接另一个信号，一个信号发射时也会发射另一个信号  
例如：valueChanged()函数会触发refreshInfo()函数  
```
connect(spinNum, SIGNAL(valueChanged(int)), this, SIGNAL(refreshInfo(int));
```
4. 当一个信号发射时，与其关联的槽函数都会立即执行  
只有在信号关联的槽函数都执行完毕之后才会执行信号后面的代码  


## 多个信号可以关联到一个槽时的槽函数处理方法
1. 场景说明
例如：多个checkBox控件的clicked()信号都关联到了同一个槽函数上，需要在槽函数内部知道到底是哪个checkBox控件被触发了
2. 方法一：在槽函数中去逐个检查控件的状态
```
//槽函数定义
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
3. 方法二：在槽函数中获取发送信号的对象(推荐)
备注：必须要用connect()函数绑定之后，才能在槽函数中获取到sender对象
```
connect(ui -> pushButton, SIGNAL(clicked()), this, SLOT(click_test1()));
//槽函数定义
void MainWindow::click_test1()
{
    qDebug() << sender() -> objectName();//在槽函数中使用sender()函数可以获取到sender对象指针
    //这个地方需要用qobject_cast<>()对sender()对象做类型转换，详见QT_qobject_cast.md
    QPushButton *button = qobject_cast<QPushButton *>(sender());
    qDebug() << button -> objectName();
}
```
4. 方法三：使用lambda表达式实现(推荐)
```
//在写connect()函数时就直接额外添加一个参数用来标识对应的控件
connect(ui -> checkBox, &QAbstractButton::clicked, [=](bool checked){click_test2(checked, 1);});
connect(ui -> checkBox_2, &QAbstractButton::clicked, [=](bool checked){click_test2(checked, 2);});
connect(ui -> checkBox_3, &QAbstractButton::clicked, [=](bool checked){click_test2(checked, 3);});
connect(ui -> checkBox_4, &QAbstractButton::clicked, [=](bool checked){click_test2(checked, 4);});
//槽函数定义
void MainWindow::click_test2(bool checked, int count)
{
    QString info = QString("点击了第%1个checkBox，状态为:%2").arg(count).arg(checked);
    qDebug() << info;
}
```

5. 方法三：使用QSignalMapper类实现
详见class_QSignalMapper.md类  
备注：QSignalMapper已过时而且使用局限较多，不建议使用  

-----------------------------------------------------------------------------------------

## 槽函数的执行方式
1. 同步调用(串行)
发出信号后，当前线程等待槽函数执行完毕后，才会继续执行下面的语句  
2. 异步调用(并行)
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

--------------------------------------------------------------------------------------

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
show()函数用来调用显示一个非模态对话框，执行完成后返回主事件中  
即show()函数弹出一个对话框之后会很快自动关闭  


## on_pushButton_clicked函数
注意：这个函数是一个槽函数，而不是信号函数  
这个槽函数是最常见的命名方式，由系统自动生成  
这个槽函数对应的信号是clicked()函数，当点击按钮时会触发  

-------------------------------------------------------------------------------

## 代码示例1：用信号与槽机制实现父窗口和子窗口之间数据互传
备注：这个问题本质上是线程同步，如果不使用信号与槽机制也可以实现，详见QT_thread.md  
1. 问题描述
父窗口(A类)为属性显示窗口，子窗口(B类)为属性设置窗口  
在父窗口中双击后即可弹出子窗口，要求两个窗口之间实现数据双向传输  
父窗口 -> 子窗口：把属性的默认值显示在子窗口中  
子窗口 -> 父窗口：把设置之后的属性值写回到父窗口中  
注意：A类和B类是写在不同头文件中，并不在同一个头文件  
2. 父窗口 -> 子窗口
在初始化对象b时，直接通过构造函数向B中传输A中的数据  
3. 子窗口 -> 父窗口
在子窗口中定义sendData函数，在任意一个子窗口函数中emit这个sendData函数  
在父窗口中用connect函数将子窗口对象、sendData函数、主窗口的getData函数关联起来  
4. 代码示例
4.1 A.h  
```
# include "B.h"

class A : public QDialog
{
    Q_OBJECT

public slots:
    void getData(QString text, int num);

private:
    B *b;
};
```
4.2 A.cpp  
```
A::A(QWidget *parent)
    : QDialog(parent)
{
    ......

    //通过构造函数向子窗口b中传输父窗口A中的数据
    b = new B("name", 10);
    //利用信号与槽机制，将sendData函数中的数据传送给getData函数
    connect(b, SIGNAL(sendData(QString, int)), this, SLOT(getData(QString, int)));
}

void Widget::getData(QString text, int num)
{
    //在getData函数中可以使用子窗口b中的数据
    qDebug() << "text: " << text;
    qDebug() << "num: " << num;
}
```
4.3 B.h  
```
class B : public QDialog
{
    Q_OBJECT

public:
    B(QString text, int num);

public slots:
    void emitSignal();

signals:
    void sendData(QString text, int num);

};
```
4.4 B.cpp  
```
B::B(QString text, int num)
{
    //设置界面布局
    input_text = new QLineEdit();
    input_num = new QSpinBox();
    confirm_button = new QPushButton("confirm");

    //设置初始值
    input_text -> setText(text);
    input_num -> setValue(num);

    //设置信号与槽
    //点击子窗口的确认按钮后，发出信号，并关闭子窗口
    connect(confirm_button, SIGNAL(clicked()), this, SLOT(emitSignal()));
    connect(confirm_button, SIGNAL(clicked()), this, SLOT(close()));

    this -> show();
}

void B::emitSignal()
{
    emit sendData(input_text -> text(), input_num -> value());
}
```


