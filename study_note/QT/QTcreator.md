# QTcreator

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
主窗口具有主菜单栏、工具栏和状态栏，类似于一般的应用程序的主窗口  
2. QWidget 所有具有可视界面类的基类  
选择QWidget创建的界面对各种界面组件都可以支持  
3. QDialog 对话框类  
QDialog可以建立一个基于对话框的界面  


## QT项目的组织结构
注意：QT项目的存放路径一定不能有中文，否则无法编译  
```
       |--Demo.pro(项目管理文件，包括一些对项目的设置项)
       |--Headers(项目下所有的头文件*.h)--|--mainwindow.h(主窗口类的头文件)
       |
       |--Sources(项目下所有的C++文件*.cpp)--|--main.cpp(主函数文件，即程序入)
       |                                    |--mainwindow.cpp(主窗口类的实现文件)
Demo --|
       |--Forms(项目下所有的界面文件*.ui)--|--mainwindow.ui(主窗口的界面文件，使用XML语言)
```