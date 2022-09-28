# Qt中的dll


## dll的编译和调用注意事项
1. 生成dll的编译器的位数必须和调用dll的编译器的位数(64位/32位)一致，否则会报错  
2. 生成dll的编译器的模式必须和调用dll的编译器的模式(debug/release)一致，否则会报错
3. dll文件、lib文件、h文件一般都放在Qt项目目录中

------------------------------Qt调用dll----------------------------


## 对调用了dll的Qt程序进行封装发布
windeployqt.exe工具好像只能把程序用到的Qt的dll给拷贝过来  
如果程序中使用了外部库，例如"snap7.dll"，windeployqt.exe工具就没有作用了  
对于这些外部库文件，必须手动拷贝过来，否则exe运行时会有相关报错  


## 1. 显式调用(只需要dll文件)
显式调用在程序执行到某个函数时才去加载对应的动态库，程序在运行前并不检查这些动态库是否存在  
显式调用只需要用到dll文件，不需要有.h文件，但需要知道接口的具体定义  
QLibrary是Qt中用来显式调用库文件的类  
详见class_QLibrary.md  


## 2. 隐式调用(需要dll文件、lib文件、h文件)
1. 基本说明
隐式调用在程序运行前，操作系统就会检查其依赖的动态库（如果缺少动态库程序就直接报错）  
隐式调用不需要使用任何Qt类，也不需要在代码中指出dll文件和lib文件  
2. 调用方法
在项目目录中新建一个include目录，把需要的dll文件、lib文件、h文件都拷贝进去  
打开.pro文件，在文件中右键 - 添加库  
库类型选择'外部库'，在库文件中找到并选择lib文件(这里选择的是lib文件，不是dll文件)  
平台可以取消Linux和Mac的勾选，只保留Windows  
其他默认，点击下一步，点击完成  
之后.pro文件中会自动出现如下内容  
```
win32:CONFIG(release, debug|release): LIBS += -L$$PWD/include/ -lIOLIB
else:win32:CONFIG(debug, debug|release): LIBS += -L$$PWD/include/ -lIOLIBd

INCLUDEPATH += $$PWD/include
DEPENDPATH += $$PWD/include
```
然后在.pro文件中手动添加上相关的头文件  
```
HEADERS += mainwindow.h\
         include/IOLib.h
```
最后引用相关的头文件即可
```
#include "include/IOLib.h"
```
3. 注意事项
最后编译生成的exe在打包或者单独运行时，还需要把dll文件手动拷贝到对应debug/release目录下  


-------------------------------创建dll(待补充)---------------------------

## 参考资料
> https://blog.csdn.net/xiaolong1126626497/article/details/112158922


## 不同编译器生成的库文件
1. 使用MSVC编译
编译后会产生mySharedLib.dll和mySharedLib.lib两个文件  
mySharedLib.dll在运行应用程序时调用，mySharedLib.lib在应用程序隐式调用动态链接库时调用  
2. 使用MinGW编译
编译后会产生mySharedLib.dll和mySharedLib.a两个文件  
mySharedLib.dll在运行应用程序时调用，mySharedLib.a在应用程序隐式调用动态链接库时调用  


## 1. 新建一个dll项目
新建项目 - Library - C++ Library  
其中，Detials步骤的Type选项选择默认的Shared Library  
Qt creator会自动生成一个和项目同名的{projectName}\_global.h文件，详见file_global_h.md  
备注：这里并不需要去继承某个Qt的类，只需要在定义类时加上一个宏声明  


## 2. 把原有项目改造成dll项目
一般情况下，工程可能之前已经创建好了，并且功能都已经完善，现在想生成库文件给被别人调用  
这时，只需要修改xxx.pro工程文件即可，在原有文件中加上以下语句  
```
TEMPLATE = lib
DEFINES += DLL_CREATETEST_LIBRARY
```


## 3. 自定义Qt控件项目
Qt的自定义控件项目最终也会编译出一个dll文件，详见QT_custom_plugin.md  
相关的类为：QDesignerCustomWidgetInterface  