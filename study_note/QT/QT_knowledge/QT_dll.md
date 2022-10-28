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


-------------------------------创建dll---------------------------

## 不同编译器生成的文件
备注：编译只能生成库文件，dll配套的头文件不在编译目录中，需要自己去项目目录中拷贝
1. 使用MSVC编译
```
xx.dll、xx.exp、xx.lib、xx.obj
```

2. 使用MinGW编译
```
xx.dll、xx.o、xx.a
```


## 新建一个纯函数计算型的dll
1. Qt新建项目
项目选择Library - C++库
类型选择默认的共享库
模块根据需要进行选择，默认只有QtCore

2. Qt自动创建出的文件
dll_test.pro
dll_test.h/cpp
备注：这里面定义的类并不需要去继承某个Qt的类，只需要在定义类时加上一个对应的宏声明
dll_test_global.h
备注：Qt会自动生成这个和项目同名的{projectName}\_global.h文件，详见file_global_h.md

3. 编写代码
在头文件中
```
class DLL_TESTSHARED_EXPORT Dll_test
{

public:
    Dll_test();
    //需要先实例化类才能调用的接口函数
    int func_add(int a, int b);
    int func_multiply(int a, int b);
    int func_substract(int a, int b);
    int func_division(int a, int b);
};

//可以直接调用的接口函数
extern "C"
{
DLL_TESTSHARED_EXPORT int getNumber();
DLL_TESTSHARED_EXPORT int add(int a, int b);
/*
上面定义的类可以在C++中使用，但在C或C#中不一定能被实例化，也就无法使用类中定义的方法
因此可以考虑使用extern "C"定义接口函数，然后在接口函数中去对类进行实例化，通过实例化对象调用类中的方法
这样对于外部来说，类是不可见的，也不需要进行类的实例化
*/
DLL_TESTSHARED_EXPORT int func_add(int a, int b);
}
```
在源文件中
```
int Dll_test::func_add(int a, int b)
{
    return a + b;
}
...

int getNumber()
{
    return 123;
}

int add(int a, int b)
{
    return a + b;
}

//对类中的方法进行封装
int func_add(int a, int b)
{
    Dll_test dll;
    return dll.func_add(a, b);
}
```

4. 编译
选择32位或64位编译器，使用release模式
点击Qt左下角的锤子图标来构建项目，之后在项目编译目录中即可找到库文件
注意：这里不能点击左下角的三角图标来运行项目，否则会有弹窗报错
```
Could not find the executable, please specify one.
```

5. 打包库文件
在编译目录中找到xx.dll文件、xx.lib或xx.a文件
在项目目录中找到xx.h文件、xx_global.h文件
将这四个文件放在一起，打成压缩包即可

6. 测试
经过实际测试，这种dll可以在Qt项目中被调用，也可以在C#等其他语言环境中被调用


## 新建一个带有UI界面的dll
1. Qt新建项目
项目选择Library - C++库
类型选择默认的共享库
模块选择QtCore、QtGui、QtWidgets
在Qt项目上右键 - Add New - 添加一个.ui文件

2. Qt自动创建出的文件
dll_test.pro
dll_test.h/cpp
备注：这里面定义的类并不需要去继承某个Qt的类，只需要在定义类时加上一个对应的宏声明
dll_test_global.h
备注：Qt会自动生成这个和项目同名的{projectName}\_global.h文件，详见file_global_h.md
mywindow.ui
mywindow.h
mywindow.cpp

3. 编写代码
先根据需要在mywindow.ui、mywindow.h、mywindow.cpp中创建需要的UI界面以及相关功能
在dll_test.h头文件中
```
#include "mywindow.h"

extern "C"
{
DLL_TEST2SHARED_EXPORT void show_window();
}

```
在dll_test.cpp源文件中
```
void show_window()
{
    MyWindow *w = new MyWindow();
    w -> show();
}
```

4. 编译
选择32位或64位编译器，使用release模式
点击Qt左下角的锤子图标来构建项目，之后在项目编译目录中即可找到库文件
注意：这里不能点击左下角的三角图标来运行项目，否则会有弹窗报错
```
Could not find the executable, please specify one.
```

5. 打包库文件
在编译目录中找到xx.dll文件、xx.lib或xx.a文件
在项目目录中找到xx.h文件、xx_global.h文件、mywindow.h文件
将这五个文件放在一起，打成压缩包即可

6. 测试
经过实际测试，这种dll可以在Qt项目中被调用，调用后会自动显示出窗口界面
但在C#等其他语言环境中被调用后报错，报错原因未知
备注：已经用windeployqt.exe把相关的依赖库都拷贝过去了，但在C#环境中还是不行
有一个qtwinmigrate可能与此有关，待了解
https://blog.csdn.net/pythonofstar/article/details/124090871
https://blog.csdn.net/weixin_43935474/article/details/105531814


## 新建一个C语言的dll
创建过程同上，创建完成后默认生成的C++类定义可以删掉，也可以不删
头文件中的函数声明如下：
```
extern "C" __declspec (dllexport) int add(int a, int b);

extern "C"
{
__declspec(dllexport) int getNumber();
__declspec(dllexport) int sum(int a, int b);
}
```
源文件中正常写出函数定义即可


## 把原有项目改造成dll项目(待补充)
一般情况下，工程可能之前已经创建好了，并且功能都已经完善，现在想生成库文件给被别人调用  
这时，只需要修改xxx.pro工程文件即可，在原有文件中加上以下语句  
```
TEMPLATE = lib
DEFINES += DLL_CREATETEST_LIBRARY
```


## 自定义Qt控件项目(待补充)
Qt的自定义控件项目最终也会编译出一个dll文件，详见QT_custom_plugin.md  
相关的类为：QDesignerCustomWidgetInterface  