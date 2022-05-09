# Qt应用程序开发框架

## 概念
Qt是一个1991年由Qt Company开发的跨平台C++图形用户界面应用程序开发框架  
Qt既可以开发GUI程序，也可以用于开发不带GUI的命令行程序，如控制台工具和服务器  
QT除了支持GUI方面的功能，还封装了网络编程、多线程、数据库链接、视频音频等相关功能  
Qt的用户界面和功能设计都是通过C++语言编程实现的，也有用于移动端的QML编程(不常用)  


## GUI
GUI(Graphical User Interface)图形用户界面图形用户接口，是采用图形方式显示的计算机操作用户界面  
用户可以通过鼠标等输入设备操纵屏幕上的图标或菜单选项来实现计算机的交互功能  


## Qt的优点
1. Qt开源并且跨平台
在Windows、Linux、Mac OS X、iOS、Android等平台都可以运行  
2. Qt提供了丰富的工具
如：基于XML的界面设计器Qt Designer，跨平台的开发工具Qt Creator  
3. Qt提供了丰富的库，除了界面库之外还包括：音频库、3d库、数据库SDK、WebEngine等  
4. QT简单易学
具有良好的封装性，不需要去具体了解windows API  
5. QT不需要第三方支持
QT可以独立安装，会最终编译为本地代码，不需要其他库的支撑
而JAVA要安装虚拟机，C#要安装.NET Framework  


## Qt的缺点
1. 网络模块性能一般
使用Qt网络模块开发小型功能没问题，大型系统可选用其他库，毕竟C++相关的网络库非常多  
2. 信号与槽机制存在性能问题
对时间敏感的功能建议采用回调方式实现  


## 基于Visual Studio + Qt的开发方式
一般来说，我们开发Qt程序都是采用Qt Creator + MSVC的方式  
如果要开发的程序只在Windows上运行，不用考虑跨平台，也不用Qt Creator设计界面，那么也可以用VS + Qt的方式开发  
这时可以把Qt当做一个界面库在VS中进行调用  
备注：需要安装VS、Qt，然后在VS中安装Qt插件  


## QT提供的工具集
QT提供了很多开发工具，常用的包括：  
1. qmake
qmake是QT最核心的工具，可以生成跨平台的.pro项目文件，也可以根据不同的操作系统和编译工具生成相应的Makefile，用于构建可执行程序或链接库  
qmake.exe路径示例(不同编译器目录下都有对应的qmake工具):
```
C:\Qt2\5.15.1\msvc2015_64\bin\qmake.exe
C:\Qt3\Qt5.2.1\5.2.1\msvc2010_opengl\bin\qmake.exe
```
2. UIC
即user interface compiler，用户界面编译器，QT使用XML语法格式的.ui文件来定义用户界面，uic根据.ui文件生成用于创建用户界面的C++代码头文件，例如ui_*.h  
3. MOC
即Meta-Object Compiler，元对象编译器，MOC会处理C++头文件的类定义里面的Q_OBJECT宏，并生成源代码文件，例如moc_*.cpp，其中包含相应类的元对象代码。元对象代码主要用于实现QT信号/槽机制、运行时类型定义、动态属性系统等  
4. RCC
即resource compiler，资源文件编译器，RCC在项目构建过程中编译.qrc资源文件，并将资源文件链接到最终的QT程序中  
5. QTcreator
QTcreator是QT的集成开发环境，是QT最常用工具  
包含项目生成管理、代码编辑、图形界面可视化编辑、编译生成、程序调试、上下文帮助、版本控制系统等众多功能  
6. designer
即QT设计师，专门用于可视化编辑GUI，并生成用于定义GUI的.ui文件  
7. cmake
cmake工具需要在安装Qt时勾选才会有，也可以到后期单独安装  
cmake.exe路径示例：  
```
C:\Qt2\Tools\CMake_64\bin\cmake.exe
C:\Qt2\Tools\CMake_64\bin\cmake-gui.exe
```

