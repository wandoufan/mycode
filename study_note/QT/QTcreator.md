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


## UI设计窗口布局
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


## QT项目的组织结构
注意：QT项目的存放路径一定不能有中文，否则无法编译  
```
       |--Demo.pro(项目管理文件，包括一些对项目的设置项)
       |--Headers(项目下所有的头文件*.h)--|--mainwindow.h(主窗口类的头文件)
       |
       |--Sources(项目下所有的C++文件*.cpp)--|--main.cpp(主函数文件，即程序入口)
       |                                    |--mainwindow.cpp(主窗口类的实现文件)
Demo --|
       |--Forms(项目下所有的界面文件*.ui)--|--mainwindow.ui(主窗口的界面文件，使用XML语言)
```
1. .pro文件
.pro文件是项目的管理文件，文件名就是项目名，相当于配置文件  
主要用于记录项目的一些设置，以及项目包含文件的组织管理  
当项目增删文件时，.pro文件会自动更新，不需要手动修改  
2. .ui文件
