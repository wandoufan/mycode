# QT中的信号与槽

## 信号与槽(signal & slot)机制
1. 信号(signal)就是在特定情况下被触发的事件  
例如，PushButton最常见的信号就是鼠标单击时发射的clicked()信号  
2. 槽(slot)就是对信号响应的函数  
一个槽就是一个函数，与一般的C++函数是一样的，可以具有任何参数，也可以被直接调用  
也可以定义在类的任何部分(private、public或protected)  
槽函数与一般函数的不同的是：槽函数可以与一个信号关联，信号发射时槽函数自动执行  
3. 信号与槽关联是用QObject::connect()函数实现的  
函数基本格式为QObject::connect(sender, SIGNAL(signal()), receiver, SLOT(slot()));  
connect()是QObject类的一个静态函数，而QObject是所有QT类的基类，故实际调用时可以忽略  
直接写为connect(sender, SIGNAL(signal()), receiver, SLOT(slot()));  
sender是发射信号的对象的名称  
signal()是信号名称，相当特殊的函数，需要带括号，有参数时需要指明参数  
receiver是接收信号的对象的名称，常用this代表本对象  
slot()是槽函数的名称，需要带括号，有参数时需要指明参数  
4. SIGNAL和SLOT  
SIGNAL和SLOT是QT的宏，用于指明信号和槽，并将它们的参数转换为相应的字符串  


## 信号与槽的使用规则
1. 一个信号可以与多个槽关联，槽函数按建立连接时的顺序依次执行  
例如：当spinNum对象的数值变化时，addFun()和updateStatus()会依次响应  
connect(spinNum, SIGNAL(valueChanged(int)), this, SLOT(addFun(int));  
connect(spinNum, SIGNAL(valueChanged(int)), this, SLOT(updateStatus(int));  
2. 一个槽可以被多个信号关联  
例如：下面三个信号都可以触发槽函数setTextFontColor()  
connect(ui->rBtnBlue,SIGNAL(clicked()),this,SLOT(setTextFontColor()));  
connect(ui->rBtnRed,SIGNAL(clicked()),this,SLOT(setTextFontColor()));  
connect(ui->rBtnBlack,SIGNAL(clicked()),this,SLOT(setTextFontColor()));  
3. 一个信号可以连接另一个信号，一个信号发射时也会发射另一个信号  
例如：valueChanged()函数会触发refreshInfo()函数  
connect(spinNum, SIGNAL(valueChanged(int)), this, SIGNAL(refreshInfo(int));  
4. 信号的参数与槽的参数个数和类型都要一致  
至少信号的参数不能少于槽的参数，否则会编译报错  
5. 在使用信号与槽的函数的类中，必须在类的定义中加入宏Q_OBJECT  
6. 当一个信号发射时，与其关联的槽函数都会立即执行  
只有在信号关联的槽函数都执行完毕之后才会执行信号后面的代码  
7. 定义的槽函数必须放在类中的slot下面，否则connect函数识别不到  


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
备注：系统不仅会在cpp文件中自动创建出槽函数框架，同时也会自动在.h头文件中自动对槽函数进行声明  
4. 可以将多个信号(组件)关联到一个自定义的槽函数上，此时槽函数是一个复合函数  
复合函数不需要对应一个具体的组件，而是多个组件都通过connect函数关联到这个复合函数上  
需要手动在类的构造函数下加入connect函数，将不同信号和函数中不同操作关联起来  
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
然后手动在类中声明自定义的槽函数上，具体定义如下：  
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
clicked信号关联的槽函数是带有参数的，例如，void on_checkBox_clicked(bool checked)  
当button带有checkable属性时：  
如果button是checked状态时，checked参数值为true；  
如果button时unchecked状态时，checked参数值为false；  

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


## clicked()和clicked(bool)的比较
1. 相同点：
clicked()和clicked(bool)都会被鼠标左键点击一次而触发  
2. 不同点：
clicked()关联的槽函数是不带参数的，clicked(bool)关联的槽函数是带有参数的  
例如，clicked(bool) 会将CheckBox组件当前的选择状态作为一个参数传递给关联槽函数  
而如果用clicked()，则需要在槽函数中用代码去读取CheckBox组件的选中状态  


## toggled()和clicked()的比较
1. 相同点：
当点击按钮时，状态信号都会被发送  
2. 不同点：
toggled要比clicked更容易触发  
clicked有的toggled有，而toggled有的，clicked却不一定有  
当调用setDown(),setChecked()或toggle()函数时，clicked不会被触发  
当用户有点击行为，或调用setChecked()函数时，都会触发toggled  


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

