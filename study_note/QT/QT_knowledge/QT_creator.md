# Qt creator

## 注意事项
1. Qt项目的存放路径一定不能有中文，否则无法编译  


## Qt使用技巧
1. 在头文件中自定义函数进行声明之后，可以自动在cpp文件中创建出该函数的框架  
自定义函数-右键-Refactor-Add Definition in qwdialog.cpp  
备注：有时候这个右键选项显示不出来，可能是在其他项目的源文件里已经定义了同名的函数，使系统误以为函数已经进行了定义，需要把其他项目或文件关闭  

2. 在UI界面中添加或更新控件之后，代码中可能会报错ui里没有该成员  
```
error: no member named 'label' in 'Ui::MainWindow'
```
对项目右键-清除/重新构建，之后就可以识别到该组件了  
注意：是'ui -> widget'，不是'this -> widget'  
有的时候尝试了清除、重新构建、项目重新关闭再打开，Qt creator重新关闭再打开等方法都不行，始终无法识别到控件  
这可能是UI界面对应的ui_xxx.h没有更新造成的，在项目目录中找到并删除该文件即可  
注意：是与main.cpp同一目录下的ui_xxx.h文件，不是debug/release目录中的ui_xxx.h文件  

3. 选择一个函数，右键 - Find Usages，可以搜索到项目中所有该函数被调用的地方
但实际测试，有的时候找到的并不全面

4. 选择一个函数或变量或者类，按F1可以打开其说明文档(如果有的话)  
按住左侧ctrl键，点击某一函数，就可以跳到该函数的定义处  
按F2也可以跳转到该函数定义的地方  
按F4可以在头文件和源文件之间切换  

5. 在其他界面按'ESC'键可以直接返回到代码编辑界面
在代码编辑界面连按多次'ESC'键，可以隐藏下面的信息输出栏，给代码更多的显示空间  

6. 左下角的定位器(Locator)可以搜索显示各种信息，例如：
'c class_name'可以跳转到指定的类定义  
'f file_name'可以打开指定的文件  

7. 代码整体右移：Tab键；代码整体左移：shift + Tab

8. 有时候明明很简单的代码却会产生报错，找不到报错原因，可能不是代码的问题
对项目右键-清除，之后可能报错就会消失  

9. Qt creator同时打开两个时，运行可能会产生报错"Cannot retrieve debugging output"


## Qtcreator提供的模板
1. Qt Widgets Application  
这是最常用的模板，支持桌面平台的GUI应用程序  
GUI的设计基于C++语言，采用Qt提供的一套C++类库  

2. Qt Console Application  
控制台应用程序，无GUI界面，一般用于学习C/C++语言  
注意：实际测试发现，Qt中的一些内容，如QChart无法在Qt Console Application中使用  
因此尽量使用 Qt Widgets Application，如果不想显示界面，就把界面显示的行给注释掉  

3. Qt Quick Application  
创建可部署的 Qt Quick 2 应用程序，其界面设计采用QML语言，程序架构采用C++语言  
利用 Qt Quick 可以设计非常炫的用户界面，一般用于移动设备或嵌入式设备上无边框的应用程序的设计  

4. Qt Quick Controls 2 Application  
创建基于 Qt Quick Controls 2 组件的可部署的 Qt Quick 2 应用程序  

5. Qt Canvas 3D Application  
创建 Qt Canvas 3D QML 项目，也是基于 QML 语言的界面设计，支持 3D 画布  


## 三个界面基类
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


-------------------------------Qt项目的配置-------------------------------

## 基本说明
1. 每种编译器的配置都相互独立，编译器下debug、profile、release三种模式的配置也都相互独立，也就是说每个都需要单独设置
2. Qt环境配置大多数都在'工具-选项-构建和运行'中进行设置


## 构建环境
可以在windows系统环境变量的基础上再添加一些路径作为Qt项目独有的路径  
备注：实际应用中发现，在打开项目之后路径会自己加载上，这些路径可能是写在代码或配置文件的某个地方  
1. INCLUDE
指定头文件(.h)的路径  
2. LIB
指定库文件(.lib)的路径  


## 影子构建(shadow build)
在Qt项目的构建设置中有一个shadow build选项，默认是勾选的  
影子构建是指将构建过程中的中间文件和目标程序都放到独立的构建目录中，实现源代码目录和构建目录的彻底分离  
这对程序源代码的发布很方便，不会将构建过程中的中间文件混杂进来  
备注：虽然是两个目录，但Qt要求这两个目录要位于同一级目录中(默认就是这样，不要改动构建目录位置了)
备注：默认编译目录可以在'工具-选项-构建和运行-default build property'中进行设置  
构建目录有默认的命名格式，示例如下：  
```
build-test-Desktop_Qt_5_15_1_MSVC2015_64bit-Release
```


## 构建套件(Kit)
构建套件就相当于编译环境，Qt会自动检测到一个构建套件作为默认的编译环境，也支持自己手动添加编译环境  
当构建套件有问题时，会显示黄色或红色的感叹号，把鼠标放上去可以看到详细的报错信息  
特别的，在Qt5.2.1 + VS 2010环境下用默认编译器对项目代码编译时发现，用的构建套件有黄色感叹号  
具体警示信息为构建套件没有设置调试器(None)，但实际并不影响代码编译  
编译环境主要包括以下因素：  
1. 套件名称
```
Desktop Qt %{Qt:Version} MSVC2015 64bit
```
2. 编译器Compiler
Qt Creator支持使用MSVC或MinGW来作为编译器  
一般推荐使用MSVC来作为默认的构建套件，因为编译和调试的速度更快 
注意：实际测试，使用MinGW32位编译器有内存空间的限制，大约是2GB，超出范围后程序会崩溃 
备注：一般C和C++的编译器都选择同一个  
```
Microsoft Vistual C++ Compiler 10.0 (x86)
Microsoft Vistual C++ Compiler 14.0 (x86)
```
MSVC编译器版本和VS版本的对应关系为
```
10.0 	 VS 2010
11.0 	 VS 2012
12.0 	 VS 2013
14.0 	 VS 2015
15.0 	 VS 2017
16.0 	 VS 2019 
```
也可以使用MinGW来作为编译器，需要在安装Qt Creator时就进行勾选  
```
C:\Qt2\Tools\mingw810_64\bin\gcc.exe //C语言
C:\Qt2\Tools\mingw810_64\bin\g++.exe //C++语言
C:\Qt2\Tools\mingw810_32\bin\gcc.exe //C语言
C:\Qt2\Tools\mingw810_32\bin\g++.exe //C++语言
```
3. 调试器Debugger
备注：一般Windows系统都自带调试器，Qt会自己识别，在有的Win7系统上可能需要额外安装  
```
C:\Program Files\Windows Kits\10\Debuggers\x64\cdb.exe
C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\cdb.exe
```
4. Qt版本Version
```
Qt 5.2.1 MSVC2010 32bit OpenGL
C:\Qt\5.15.1\msvc2015_64\bin\qmake.exe
```
5. 可以在不安装整个MSVC2015的情况下，为Qt单独下载和配置MSVC的编译器
https://www.cnblogs.com/sggggr/p/12791740.html


-------------------------------Qt项目的运行选项-------------------------------

## 项目运行选项
备注：以下选项都在'编辑 - 项目右键'中  
1. 构建
增量编译，只编译有变化的部分，然后生成exe程序(不会运行程序)  
备注：执行后会产生项目构建目录  

2. 执行qmake
根据.pro文件生成相应的Makefile  
备注：执行后会产生项目构建目录  

3. 部署
备注：暂时没找到详细解释  

4. 运行(相当于点击三角运行图标)
如果已有Makefile，会直接进行编译  
如果没有Makefile，会先根据.pro文件生成Makefile，然后再进行编译  
在编译结束后会自动运行生成的exe程序  

5. 重新构建
全量编译，编译所有的部分，然后生成exe程序(不会运行程序)  
备注：执行后会产生项目构建目录  

6. 清除
将debug/release目录中除了exe程序外，其他文件都清理掉  


## 关于生成项目构建目录的详细解释
执行qmake产生的项目构建目录中除了Makefile文件外，也会有debug/release目录，但目录为空  
构建/重新构建的debug/release目录中会生成.exe、.obj、.h、.cpp文件  



-------------------------------Qt项目的编译模式-------------------------------

## 编译模式
1. Debug
即调试版本，源代码和二进制目标程序一一对应，代码结构臃肿，运行速度慢  
生成的程序里有很多调试信息，方便对程序进行调试  
2. Release
即发行版，二进制目标程序进行了大量优化，比Debug版本小很多，运行性能更高  
对于耗时小的程序，Release和Debug区别不大，但对于耗时多的程序，Release的效果很明显  
3. Profile
Profile是上面两种版本之中取一个平衡,兼顾性能和调试  


## breakpoint断点
在QT的Debug模式下，可以打断点之后运行  
实际测试了一下，断点的地方只能显示出内存地址，而且每次运行到断点位置时程序会卡死  
1. F9加断点，再按F9，取消断点  
2. F10单步执行  


## release崩溃问题
对于相同代码的程序，有时候可能debug模式下能运行，但release模式下就会崩溃  
release模式下的要求比debug模式更加严格  
常见的崩溃原因：  
1. 定义了变量或指针但是没有进行初始化  

另外，代码中有些变量定义了但未使用，这种情况一般只显示为warning，不一定会造成崩溃  
在debug模式下不影响程序执行，但在release模式下就可能造成程序崩溃  
```
// result记录函数是否执行成功，但后续并没用到result
bool result = GetIndex();
```
程序崩溃时经常会有如下报错，但实际是内存方面错误，与sogou无关  
```
C:\Program Files (x86)\SogouInput\Components\
```


-------------------------Qt项目构建目录中生成的文件-------------------------

## .exp文件
exp文件是导出库文件，包含了导出函数和数据项的信息  
当Lib创建一个导入库文件(.lib)的同时也会创建一个导出库文件(.exp)  
如果你的程序链接到另一个程序，并且需要同时导入和导出到另一个程序中，这时候就要用到exp文件  
LINK工具将使用exp文件来创建dll文件  


## .obj文件
obj文件是目标文件/中间文件，是源代码中每个cpp文件经过编译后产生的  
obj文件是exe文件的前身，但不能直接执行，需要经过链接后才能成为exe文件  
obj文件中给出的是程序的相对地址，而exe文件中给出的是程序的绝对地址  


## pch文件
pch文件是被预先编译过的头文件(Pre-compiled Header)  
对于比较大型的工程编译时间都很长，通过使用PCH可以把那些不经常使用的头文件都预先编译出来，大大节省实际使用时候的编译时间  
实际应用中，还经常把外部调用的API的头文件编译为PCH，比如调用STL、调用Windows的APIwindows.h等等  
使用PCH也会有一些缺点，比如减弱文件之间的关联性  


## 清理构建目录中的多余文件
Qt项目在编译后会在构建目录中产生很多文件，如果只需要可执行文件以及动态库，可以清理掉多余文件  
备注：不是一定要删除，只是为了减少构建目录的规模，方便备份  
1. 用bat脚本
编写如下脚本，并放在构建目录中运行  
```
del /f /s *.obj;
del /f /s *.exp;
del /f /s *.lib;
del /f /s *.h;
del /f /s *.cpp;
del /f /s *.pch;
```
2. 提前在.pro文件配置
将所有的多余文件输出到一个temp目录中，编译之后统一删除掉  
```
UI_DIR = ./tmp/ui
MOC_DIR = ./tmp/moc
OBJECTS_DIR = ./tmp/obj
RCC_DIR = ./tmp/rcc
```