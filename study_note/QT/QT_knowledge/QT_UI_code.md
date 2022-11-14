# Qt的界面编码


## UI+代码方式和纯代码方式的对比
1. 采用纯代码设计实现界面时，需要对组件的布局有个完整的规划，不如UI方式设计直观，且编写代码工作量大
但用纯代码方式可以在底层实现更加强大和灵活的设计功能

2. UI+代码方式不需要先定义界面中的各个控件，直接设置控件的各种属性即可
纯代码方式要首先去把界面中的控件定义出来，然后再去设置控件属性


-------------------- 1. 完全用纯代码方式实现UI界面 --------------------
## 说明
1. 要采用纯代码方式，在创建项目时要将'Generate form'取消勾选，创建完成后项目目录下没有.ui文件  

2. 纯代码方式实现时，在头文件的类定义中没有指向界面的指针ui，在源文件中也不再去调用指针ui  


## 代码示例
头文件
```
#include <QWidget>
#include <QPushButton>
#include <QLabel>
#include <QLineEdit>
#include <QGridLayout>

class UiCode : public QWidget
{
public:
    UiCode();

private:
    QLabel *label1;
    QPushButton *button1, *button2;
    QLineEdit *editor1;
    QGridLayout *layout;
};
```
源文件
```
#include "uicode.h"

UiCode::UiCode()
{
    //设置控件属性
    label1 = new QLabel("input:");
    editor1 = new QLineEdit;
    button1 = new QPushButton("ok");
    button2 = new QPushButton("cancel");
    //设置布局
    layout = new QGridLayout;
    layout -> addWidget(label1, 0, 0);
    layout -> addWidget(editor1, 0, 1);
    layout -> addWidget(button1, 1, 0);
    layout -> addWidget(button2, 1, 1);
    this -> setLayout(layout);
}
```
调用文件
```
//注意：类声明不能写在函数里，否则弹出的窗口会自动关闭
class MainWindow : public QMainWindow
{
...

private:
    UiCode code;
};

void MainWindow::on_pushButton_clicked()
{
    code.show();
}
```


-------------------- 2. 用.ui文件 + 代码的方式实现UI界面 --------------------
## 说明
1. 由.h、.cpp、.ui共3个文件组成，其中.ui文件还会在编译后在build目录下生成对应的ui_xx.h文件  

2. 在代码中可以调用指针UI来调用控件，并对控件的属性进行设置


## 注意事项
在构造函数的定义中一定不要忘了对ui指针进行实例化！
```
\\写在初始化列表中
ui(new Ui::MainWindow)
\\或者写在构造函数中
ui = new Ui::MainWindow;
```
如果没有对ui指针进行实例化，就会造成内存报错，程序闪退


## 代码示例
头文件
```
//必须要在Ui这个命名空间中声明这个类
namespace Ui { class MainWindow; }


class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

//必须要声明出这个ui指针
private:
    Ui::MainWindow *ui;
};
```
源文件
```
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)//必须要对ui指针进行实例化
{
    ui->setupUi(this);

    //通过ui指针对界面中的各个控件进行属性设置
    ...
}

MainWindow::~MainWindow()
{
    delete ui;
}
```

---------------------------------------------------

## 代码示例：用代码来批量创建控件
1. 情况说明
有时候需要在UI界面上创建几十个甚至更多的控件，如QLabel、QPushButton等
如果在Qt designer上逐个手动创建，实现起来会很麻烦，可以使用代码来进行批量创建
在代码中，如果每个控件的对象名都手写出来也会很麻烦，可以把控件对象指针批量添加到QVector或QList等容器类中
备注：在代码中并没有具体定义出每个控件的对象名称
注意：容器类的数据项不支持QObject类及其子类(包括所有的Qt控件类)，因此添加到容器类的是对象指针，而不是对象

2. 具体代码
在界面中创建80个QCheckBox，来让用户勾选通道
```
QVector<QCheckBox *> input_channels_list;
for(int i = 0; i < 80; i++)
{
    QString checkbox_name = QString("channel_%1").arg(i);
    input_channels_list.append(new QCheckBox(checkbox_name));
}
QGridLayout *gridlayout = new QGridLayout;
int row = 0;
int column = 0;
for(int i = 0; i < 80; i++)
{
    //布局：每行10个通道，共8行
    qDebug() << i << ": " <<  row << ", " << column;
    gridlayout -> addWidget(input_channels_list[i], row, column);
    if(column < 9)
        column += 1;
    else
        column = 0;
    if(column == 0)
        row += 1;
}
ui -> groupBox_input_channels -> setLayout(gridlayout);
```
