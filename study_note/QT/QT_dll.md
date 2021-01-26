# 在QT中调用dll

## DLL文件的应该放置的位置
在QT项目中，dll文件应该放在QT项目对应的运行目录中  
运行目录中的debug和release两个子文件夹不用放  
经过测试，dll放在QT项目目录中、C:\Windows\SysWOW64\中、C:\Windows\system32\中都无法加载到  
另外，还需要注意使用的编译器是32位还是64位  

## 待研究测试
dll可能是放在C:\Windows\SysWOW64\中，然后注册到注册表里？

## 调用方式
显式调用只需要dll文件  
隐式调用需要dll文件、lib文件、h文件  

## 方法一 QLibrary
QLibrary是QT中用来加载库文件的类  
QLibrary属于显式调用方式，即在程序执行到某个函数时才去加载对应的动态库  
详见class_QLibrary.md  

## 创建dll(待研究)
如何编写产生一个dll，可以拿去被别人调用？
> https://blog.csdn.net/xiaolong1126626497/article/details/112158922
方式一：  
在新建项目时就要选择C++ Library项目  
方式二：  
一般情况下，工程可能之前已经创建好了，并且功能都已经完，现在想生成库文件给被别人调用  
这时，只需要修改xxx.pro工程文件即可  