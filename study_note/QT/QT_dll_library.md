# Qt中的dll

## 参考资料
https://blog.csdn.net/xiaolong1126626497/article/details/112158922

------------------------------调用dll----------------------------

## DLL文件的应该放置的位置
在QT项目中，dll文件应该放在QT项目对应的运行目录中  
运行目录中的debug和release两个子文件夹不用放  
经过测试，dll放在QT项目目录中、C:\Windows\SysWOW64\中、C:\Windows\system32\中都无法加载到  
另外，还需要注意使用的编译器是32位还是64位  


## 调用方式
1. 显式调用只需要dll文件  
2. 隐式调用需要dll文件、lib文件、h文件  


## 用到的Qt类
1. QLibrary
QLibrary是QT中用来加载库文件的类  
QLibrary属于显式调用方式，即在程序执行到某个函数时才去加载对应的动态库  
详见class_QLibrary.md  

-------------------------------创建dll(待补充)---------------------------

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