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
当项目增删文件时，.pro文件会自动更新，不需要手动修改  
2. main.cpp文件  
main.cpp是实现main()函数的文件，包含创建窗口、显示窗口、运行应用程序等功能  
main()函数是整个程序的入口，程序从这里开始执行  
备注：窗口的标题默认是自己定义的类名，也可以用setWindowTitle函数进行修改
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


## UI设计窗口功能区域划分
双击项目中的.ui文件可以打开UI设计窗口，包括：  
1. 设计组件(左侧)  
分为多个组，如Layouts、Buttons、Display Widgets等  
2. 待设计窗体(中间)  
拖动一个组件到窗体上即可  
3. 编辑器(下方)  
Signals和Slots编辑器用于可视化地进行信号与槽的关联  
Action编辑器用于可视化设计Action  
4. 工具栏(上方)  
工具栏中的按钮主要用于实现布局和界面设计  
5. 对象浏览器(右上方)  
对象浏览器(Object Inspector)用树状显示各组件间的关系  
包含两列，即每个组件的对象名称和所属的类名称  
6. 属性编辑器(右下方)  
属性编辑器(Property Editor)中可以显示或修改某个选中的组件的属性值  
包含两列，即每个组件的属性和属性值  
属性从上到下可以分为多个组，实际表示了类的继承关系  
例如，label组件为：QObject→QWidget→QFrame→QLabel  
7. 输出面板(最下方)  
输出面板包括了问题、应用程序输出、编译输出等多个部分的程序运行信息  
其中应用程序输出可以查看到程序运行的中间结果，常用来进行代码调试  


## 界面设计布局
1. 组件之间的层次关系  
设计组件中包含一类containers组件，用来实现层次关系，将各个组件的分布设计更加美观  
例如，可以将三个checkBox放在一个groupBox中，移动groupBox时三个checkBox会随之移动  
另外，在每个containers组件内部可以单独设置不同的排版布局  
组件之间具体的层次关系可以在右上方的对象浏览器中查看  
2. 组件的排版布局  
设计组件中包含Layouts组件和Spacers组件，具体包括：  
Vertical Layout 垂直方向布局，组件自动在垂直方向上分布  
Horizontal Layout 水平方向布局，组件自动在水平方向上分布  
Grid Layout 网格状布局，网状布局大小改变时，每个网格的大小都改变  
Form Layout 窗体布局，与网格状布局类似，但是只有最右侧的一列网格会改变大小  
Horizontal Spacer 一个用于水平分隔的空格  
Vertical Spacer 一个用于垂直分隔的空格  
3. 伙伴关系(Buddy)  
伙伴关系是指将一个Label和一个组件相关联，在程序运行时即可用快捷键将输入光标切换到某个组件上  
点击上方工具栏中的"Edit Buddies"即可进入伙伴关系编辑模式  
编辑完成后点击工具栏的"Edit Widget"即可退回到组件编辑模式  
伙伴关系设置完成后可以在label组件的buddy属性中进行查看
4. Tab顺序  
Tab顺序是指程序在运行时，按下Tab键时输入光标的移动顺序  
点击上方工具栏中的"Edit Tab Order"即可进入Tab顺序编辑模式  
编辑完成后点击工具栏的"Edit Widget"即可退回到组件编辑模式  
注意：没有输入光标的组件是没有Tab顺序的，例如Label组件  


## UI方式实现和纯代码方式实现
1. 通过UI方式实现窗口的设计更加简单，让用户省去了繁琐的界面设计工作  
采用代码设计实现 UI 时，需要对组件的布局有个完整的规划，不如可视化设计直观，且编写代码工作量大  
但用纯代码方式可以在底层实现更加强大和灵活的设计功能  
2. 要采用纯代码方式，在创建项目时要将'Generate form'取消勾选，创建完成后项目目录下没有*.ui文件  
3. 用UI方式和纯代码方式实现同一个功能，二者的底层代码并不相同  
UI方式的底层代码是自动生成的(也可以有自定义的部分)，并不包含组件定义  
代码方式需要在头文件中将所有用到的组件都定义出来
4. 代码方式实现时，在头文件的类定义中没有指向界面的指针ui  
在cpp主文件中也不再去调用指针ui  


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


## QT使用技巧
1. 在头文件中自定义函数进行声明之后，可以自动在cpp文件中创建出该函数的框架  
自定义函数-右键-Refactor-Add Definition in qwdialog.cpp  
2. 注意变量名的大小写，否则经常会报错变量名未定义，例如'Qt'写成'QT'



