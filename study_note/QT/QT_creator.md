# QT creator

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
2. QWidget 所有具有可视界面组件类的基类  
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
备注：Dialog中可以使用setModal(true)和setWindowModality()函数进行设置  
1. 模态对话框  
子窗口创建后，主窗口其他内容都不能点击，只有等子窗口关闭退出后才能继续点击  
能够封锁其他窗口获取输入的称为模态窗口  
使用exec()函数来实现阻塞功能  
备注：模态窗口的子窗口不会被封锁  
2. 非模态对话框  
子窗口创建后，主窗口其他内容不受影响，可以正常点击  
使用show()函数来显示  
3. 半模态对话框  
子窗口创建后，主窗口无法点击，但后台程序可以继续运行  


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


## QT使用技巧
1. 在头文件中自定义函数进行声明之后，可以自动在cpp文件中创建出该函数的框架  
自定义函数-右键-Refactor-Add Definition in qwdialog.cpp  
备注：有时候这个右键选项显示不出来，可能是在其他源文件里已经定义了同名的函数，使系统误以为函数已经进行了定义，需要把其他项目或文件关闭  

2. UI界面中更新组件之后，代码中会报错ui里没有该成员  
对项目右键-清除，之后就可以识别到该组件了  

3. 按住左侧ctrl键，点击某一函数，就可以跳到该函数的定义处  

4. 选择一个函数或变量，按F1可以打开其说明文档(如果有的话)  
按F2可以跳转到其定义的地方  

5. 在其他界面按'ESC'键可以直接返回到代码编辑界面
在代码编辑界面连按多次'ESC'键，可以隐藏下面的信息输出栏，给代码更多的显示空间  

6. 左下角的定位器(Locator)可以搜索显示各种信息，例如：
'c class_name'可以跳转到指定的类定义  
'f file_name'可以打开指定的文件  

7. 代码整体右移：Tab键；代码整体左移：shift + Tab