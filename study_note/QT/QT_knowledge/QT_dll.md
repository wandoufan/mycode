# Qt中的dll


------------------------------调用dll----------------------------

## 注意事项
1. 使用的编译器的位数必须和调用的库的位数一致，否则会报错  
2. dll文件、lib文件、h文件一般都放在Qt项目目录中


## 对调用了dll的Qt程序进行封装发布
windeployqt.exe工具好像只能把程序用到的Qt的dll给拷贝过来  
如果程序中使用了外部库，例如"snap7.dll"，windeployqt.exe工具就没有作用了  
对于这些外部库文件，必须手动拷贝过来，否则exe运行时会有相关报错  


## 1. 显式调用(只需要dll文件)
QLibrary是Qt中用来显式调用库文件的类  
详见class_QLibrary.md  


## 2. 隐式调用(需要dll文件、lib文件、h文件)
不需要使用任何Qt类，直接#include头文件，然后就可以调用到头文件中提供的接口函数  
备注：需要在.pro文件中添加头文件及其路径
参考demo23_snap7_dll项目


-------------------------------创建dll(待补充)---------------------------

## 参考资料
> https://blog.csdn.net/xiaolong1126626497/article/details/112158922


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