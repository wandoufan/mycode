# QTcreator

## QTcreator提供的应用程序模板

## 创建界面的基类(base class)
1. QMainWindow

## QT项目的组织结构
```
       |--Demo.pro(项目管理文件，包括一些对项目的设置项)
       |--Headers(项目下所有的头文件*.h)--|--mainwindow.h(主窗口类的头文件)
       |
       |--Sources(项目下所有的C++文件*.cpp)--|--main.cpp(主函数文件，即程序入)
       |                                    |--mainwindow.cpp(主窗口类的实现文件)
Demo --|
       |--Forms(项目下所有的界面文件*.ui)--|--mainwindow.ui(主窗口的界面文件，使用XML语言)
```