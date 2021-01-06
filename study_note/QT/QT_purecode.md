# QT纯代码实现界面

## UI方式实现和代码方式实现
1. 通过UI方式实现窗口的设计更加简单，让用户省去了繁琐的界面设计工作  
采用代码设计实现 UI 时，需要对组件的布局有个完整的规划，不如可视化设计直观，且编写代码工作量大  
但用纯代码方式可以在底层实现更加强大和灵活的设计功能  
2. 要采用纯代码方式，在创建项目时要将'Generate form'取消勾选，创建完成后项目目录下没有.ui文件  
3. 用UI方式和纯代码方式实现同一个功能，二者的底层代码并不相同  
UI方式的底层代码是自动生成的(也可以有自定义的部分)，并不包含组件定义  
代码方式需要在头文件中将所有用到的组件都定义出来  
4. 代码方式实现时，在头文件的类定义中没有指向界面的指针ui  
在cpp主文件中也不再去调用指针ui  
5. 对于用纯代码插入的组件，在UI界面的编辑器里是不可见的，只有程序运行之后才能看见  
因此，不能通过UI编辑器来拖动这些组件的位置，只能用代码参数设置  

## 代码示例
示例：已经有了一个UI界面，并设置了一些组件  
现在用代码在UI界面中插入文本框PlainTextEdit并设置属性  
在.h文件中：  
```
class Widget : public QWidget
{
    Q_OBJECT

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();

public:
    QPlainTextEdit *mytext;
    QPalette plet;

private:
    Ui::Widget *ui;

//其他省略...
};
```
在.cpp文件中：  
```
Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    QString content = "custom text test";
    mytext = new QPlainTextEdit(content, this);//是否有this不一样
    plet = mytext -> palette();
    plet.setColor(QPalette::Base, Qt::blue);
    mytext -> setPalette(plet);
    mytext -> setGeometry(600, 50, 100, 100);
    mytext -> show();//不调用show()函数是显示不出来的

//其他省略...
}
```
1. 在获取初始化控件对象时，是否有this指针是不一样的
如果加上this参数，则说明对象的父类是当前的UI界面  
程序运行后，插入的文本框会显示在UI窗口里面  
设置的位置参数也是相对于UI窗口的左上角的距离  
如果没有this参数，则说明对象的父类默认为空  
程序运行后，插入的文本框与UI窗口无关，会单独显示成一个窗口  
设置的位置参数是相对于显示屏的左上角的距离  
2. 在对象的属性都设置完毕之后一定要调用show()函数  
否则这个对象运行后是显示不出来的  