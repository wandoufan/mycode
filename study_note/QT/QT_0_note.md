# Qt应用程序开发框架

## 参考资料
> http://c.biancheng.net/view/1792.html

## 概念
Qt是一个1991年由Qt Company开发的跨平台C++图形用户界面应用程序开发框架  
Qt既可以开发GUI程序，也可以用于开发不带GUI的命令行程序，如控制台工具和服务器  
QT除了支持GUI方面的功能，还封装了网络编程、多线程、数据库链接、视频音频等相关功能  
Qt的用户界面和功能设计都是通过C++语言编程实现的，也有用于移动端的QML编程(不常用)  

## GUI
GUI(Graphical User Interface)图形用户界面图形用户接口，是采用图形方式显示的计算机操作用户界面  
用户可以通过鼠标等输入设备操纵屏幕上的图标或菜单选项来实现计算机的交互功能  

## Qt的优点
Qt开源并且跨平台，在Windows、Linux、Mac OS X、iOS、Android等平台都可以运行  
Qt提供了丰富的工具，如：基于XML的界面设计器Qt Designer，跨平台的开发工具Qt Creator  
Qt提供了丰富的库，除了界面库之外还包括：音频库、3d库、数据库SDK、WebEngine等  
QT简单易学，具有良好的封装性，不需要去具体了解windows API  
QT可以独立安装，会最终编译为本地代码，不需要其他库的支撑，而JAVA要安装虚拟机，C#要安装.NET Framework  

## Qt的应用
Qt被广泛应用于嵌入式、电力系统、军工系统等要与硬件交互的界面系统中，主要用于桌面程序和嵌入式  
许多大型软件都是用 Qt 开发的，如 Autodesk Maya、Google Earth、Skype、WPS Office等  
另外还有：豆瓣电台、虾米音乐、淘宝助理、千牛、暴雪的战网客户端、咪咕音乐、Google地图等等  

## QT和MFC的对比
QT和MFC都是基于C++的GUI解决方案，但二者各有不同：  
1. MFC只能用在windows平台，而QT是跨平台的，可以直接在其他平台运行  
2. MFC仍然需要去了解windows API，而QT已经封装了底层细节，学习相对简单  

## QT使用的编译器
QT在安装时提供了MinGW组件和MSVC组件作为将来C++代码的编译器  
MinGW是Windows平台上使用的GNU工具集导入库的集合  
MSVC允许使用本地已经安装过的Visual Studio来作为编译器  
另外还有UWP组件主要用于Windows10平台的编译器  

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

