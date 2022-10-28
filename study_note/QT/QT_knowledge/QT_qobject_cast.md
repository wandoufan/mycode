# qobject_cast<>()的用法

## 函数定义
```
T qobject_cast(QObject *object)
```
如果object参数与T或T的子类类型一致，将object转换为类型T并返回，否则返回0  
如果object参数是0(即空指针)，则函数也返回0  
其中T必须是继承于QObject的子类，并且要使用Q_OBJECT宏进行声明  
备注：如果T没有使用Q_OBJECT宏进行声明，则返回值是无定义的  
```
QObject *obj = new QTimer;          // QTimer inherits QObject

QTimer *timer = qobject_cast<QTimer *>(obj);
// timer == (QObject *)obj

QAbstractButton *button = qobject_cast<QAbstractButton *>(obj);
// button == 0
```


## 基本说明
备注：qobject_cast函数的相关定义都是写在QObject类里面，但它并不是QObject类的成员函数  
qobject_cast<>()的功能类似于C++中的dynamic_cast<>()，可以进行Qt中的数据类型转换  
但qobject_cast<>()不需要RTTI的支持，并且可以跨越dll的边界工作  


## 应用场景：在槽函数中获取发出信号函数的对象
当某一个Object emit一个signal的时候，它就是一个sender, 系统会记录下当前是谁emit出这个signal的
所以你在对应的slot里就可以通过 sender()得到当前是谁invoke了你的slot
有可能多个 Object的signal会连接到同一个signal(例如多个Button可能会connect到一个slot函数onClick())
因此这是就 需要判断到底是哪个Object emit了这个signal，根据sender的不同来进行不同的处理
```
connect(ui -> pushButton, SIGNAL(clicked()), this, SLOT(click_test1()));
//槽函数定义
void MainWindow::click_test1()
{
    qDebug() << sender() -> objectName();//在槽函数中使用sender()函数可以获取到sender对象指针
    QPushButton *button = qobject_cast<QPushButton *>(sender());
    qDebug() << button -> objectName();
}
```


## 应用场景：获取当前焦点Widget
通过QWidget * QApplication::focusWidget()可以获得当前拥有焦点的widget，然后和你的那几个可能有焦点的widget逐一比对即可执行对应操作
```
QWidget * fWidget = qApp->focusWidget();
if (lineEdit1 == qobject_cast<QLineEdit *>(fWidget ))
{
        //lineEdit1
}
else if(lineEdit2 == qobject_cast<QLineEdit *>(fWidget ))
{ 
        //lineEdit2
}
else if(lineEdit3 == qobject_cast<QLineEdit *>(fWidget ))
{
        //lineEdit3
}
else if(textEdit == qobject_cast<QTextEdit *>(fWidget ))
{
        //textEdit
}
```