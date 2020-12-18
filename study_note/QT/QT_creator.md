# QTcreator

## QT帮助文件
1. 当光标停留在一个类名或函数名上时，按F1可以查看其帮助文档  
2. 打开上方的帮助-目录-Qt Creator Manual，可以查看所有的帮助文档  
帮助文档界面下左侧有Bookmarks、Contents、Index和Search4种模式  


## QTcreator提供的应用程序模板
1. Qt Widgets Application  
这是最常用的模板，支持桌面平台的GUI应用程序  
GUI的设计基于C++语言，采用QT提供的一套C++类库  
2. Qt Console Application  
控制台应用程序，无GUI界面，一般用于学习C/C++语言  
3. Qt Quick Application  
创建可部署的 Qt Quick 2 应用程序，其界面设计采用QML语言，程序架构采用C++语言  
利用 Qt Quick 可以设计非常炫的用户界面，一般用于移动设备或嵌入式设备上无边框的应用程序的设计  
4. Qt Quick Controls 2 Application  
创建基于 Qt Quick Controls 2 组件的可部署的 Qt Quick 2 应用程序  
5. Qt Canvas 3D Application  
创建 Qt Canvas 3D QML 项目，也是基于 QML 语言的界面设计，支持 3D 画布  


## 创建界面的基类(base class)
1. QMainWindow 主窗口类  
主窗口具有主菜单栏、工具栏和状态栏，一般以独立窗口显示  
2. QWidget 所有具有可视界面类的基类  
QWidget继承于QObject类和QPaintdevice类，也是QMainWindow和QDialog的父类  
QWidget在没有指定父容器时可以作为独立的窗口，指定父容器之后可以作为父容器的内部组件  
选择QWidget创建的界面对各种界面组件都可以支持  
QWidget窗口可以被其父窗口或其他窗口挡住一部分  
3. QDialog 对话框窗口类  
QDialog主要用于短期任务或用户进行短期通讯的顶级窗口  
4. 三者之间比较  
QMainWindow和QWidget创建出来的窗口右上角都有放大、缩小和关闭按钮  
QDialog创建出来的窗口右上角只有问号和关闭按钮，没有放大和缩小按钮  


## 三种对话框类型
1. 模式对话框  
窗口创建后，主窗口其他内容都不能执行，只有等该窗口关闭退出后才能执行  
使用exec()函数来实现阻塞功能  
2. 非模式对话框  
窗口创建后，主窗口其他内容不受影响，可以正常执行  
使用show()函数来显示  
3. 半模式对话框  
窗口创建后，主窗口无法点击，但后台程序可以继续运行  
使用setModal(true)和setWindowModality()函数  


## 常用QDialog对话框类
QColorDialog（颜色对话框）  
QFileDialog（文件对话框）  
QFontDialog（字体对话框）  
QInputDialog（输入对话框）  
QMessageBox（消息对话框）  
QProgressDialog（进度对话框）  
QErrorMessage（错误信息对话框）  
QPageSetupDialog（页面设置对话框）  
QPrintDialog（打印对话框）  
QPrintPreviewDialog（打印预览对话框）  


## 项目组织结构
注意：QT项目的存放路径一定不能有中文，否则无法编译  
1. QMainWindow 主窗口类
```
       |--Demo.pro(项目管理文件，包括一些对项目的设置项)
       |--Headers(项目下所有的头文件*.h)--|--mainwindow.h(主窗口类的头文件)
       |
       |--Sources(项目下所有的C++文件*.cpp)--|--main.cpp(主函数文件，即程序入口)
       |                                    |--mainwindow.cpp(主窗口类的实现文件)
Demo1--|
       |--Forms(项目下所有的界面文件*.ui)--|--mainwindow.ui(主窗口的界面文件，使用XML语言)
```
2. QWidget 具有可视界面类的基类
```
       |--Demo.pro(项目管理文件，包括一些对项目的设置项)
       |--Headers(项目下所有的头文件*.h)--|--widget.h(主窗口类的头文件)
       |
       |--Sources(项目下所有的C++文件*.cpp)--|--main.cpp(主函数文件，即程序入口)
       |                                    |--widget.cpp(主窗口类的实现文件)
Demo2--|
       |--Forms(项目下所有的界面文件*.ui)--|--widget.ui(主窗口的界面文件，使用XML语言)
```
3. QDialog 对话框类
```
       |--Demo.pro(项目管理文件，包括一些对项目的设置项)
       |--Headers(项目下所有的头文件*.h)--|--dialog.h(主窗口类的头文件)
       |
       |--Sources(项目下所有的C++文件*.cpp)--|--main.cpp(主函数文件，即程序入口)
       |                                    |--dialog.cpp(主窗口类的实现文件)
Demo2--|
       |--Forms(项目下所有的界面文件*.ui)--|--dialog.ui(主窗口的界面文件，使用XML语言)
```


## 项目中包含的文件
1. .pro文件  
.pro文件是项目的管理文件，文件名就是项目名，相当于配置文件  
主要用于记录项目的一些设置，以及项目包含文件的组织管理  
当项目中要用到一些非标准库时，要在.pro文件中进行声明，例如：'QT += axcontainer'  
当项目增删文件时，.pro文件会自动更新，不需要手动修改  
注意：实际使用发现删除QT项目中的文件夹没反应，必须到.pro文件中将该文件注释掉  
例如，向QT项目目录中拷贝了一个cpp文件和一个头文件，但QT中打开项目始终显示不出来，需要在.pro文件手动加上这两个文件的声明  
2. main.cpp文件  
main.cpp是实现main()函数的文件，包含创建窗口、显示窗口、运行应用程序等功能  
main()函数是整个程序的入口，程序从这里开始执行  
```
int main(int argc, char *argv[])
{
    QApplication a(argc, argv); //用QApplication类定义并创建应用程序对象a
    Widget w; //用Widget类定义并创建窗口对象w
    w.setWindowTitle("this is a calcultor"); //修改窗口的标题
    w.show(); //w.show()用来显示窗口
    return a.exec(); //a.exec()用来启动应用程序，开始应用程序的消息循环和事件处理
}
```


## 与窗体相关的4个文件(以QWidget类为例)
1. widget.h
定义窗体类的头文件，定义了一个继承自类QWidget的类Widget  
另外还对自己定义出的那些槽函数进行了声明，和widget.cpp文件中定义出的槽函数一一对应  
2. widget.cpp
Widget类的功能实现的源程序文件  
3. widget.ui
窗体界面文件，由UI设计器自动生成，存储了窗体上各个组件的属性设置和布局  
使用XML语言，一般用UI设计器可视化设计生成  
4. ui_widget.h
根据用户设置的窗体组件及属性、信号与槽的关联等自动生成一个类的定义文件，类名为Ui_Widget  
该文件不在项目目录下，而是在对widget.ui编译后才在build目录下生成该文件  


## QT类中的构造函数和析构函数
QT项目的.h头文件中，类中会自动对其构造函数和析构函数进行声明，但构造函数和析构函数的具体定义部分会自动生成在.cpp主文件的最上方，用户可以自己在定义部分添加需要的内容  


## 元对象系统(Meta-Object System)
1. 基本概念
Qt的元对象系统提供了对象之间通信的信号与槽机制、运行时类型信息和动态属性系统  
2. 元对象系统由以下三个基础组成：
2.1 QObject类是所有使用元对象系统的类的基类  
2.2 在一个类的private部分声明Q_OBJECT宏，然后类就可以使用元对象的信号与槽等各种特性  
2.3 MOC(元对象编辑器)为每个QObject的子类提供必要的代码来实现元对象系统的特性  
3. 元对象系统提供的其他功能：


## 属性系统
1. 基本概念
QT提供一个Q_PROPERTY()宏可以定义属性，它也是基于元对象系统实现的  
QT的属性系统与C++编译器无关，可以用任何标准的C++编译器去编译一个定义了属性的QT程序  
2. Q_PROPERTY()宏
3. 属性的使用
4. 动态属性
5. 类的附加信息


## QT项目编译选项
1. Debug
即调试版本，源代码和二进制目标程序一一对应，代码结构臃肿，运行速度慢  
生成的程序里有很多调试信息，方便对程序进行调试  
2. Release
即发行版，二进制目标程序进行了大量优化，比Debug版本小很多，运行性能更高  
3. Profile
Profile是上面两种版本之中取一个平衡,兼顾性能和调试  
备注：有时候可能debug版本能运行，但release版本会报错  


## QT使用技巧
1. 在头文件中自定义函数进行声明之后，可以自动在cpp文件中创建出该函数的框架  
自定义函数-右键-Refactor-Add Definition in qwdialog.cpp  
2. 注意变量名的大小写，否则经常会报错变量名未定义，例如'Qt'写成'QT'  
3. 在代码中使用ui指针指向某个组件时，明明有这个组件，却会报错ui里没有该成员  
例如：'ui -> pushButton'，报错：no member named 'pushButton' in 'Ui::Widget  
对项目右键-清除，之后就可以识别到该组件了  



