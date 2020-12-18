# 在QT中调用dll

## DLL文件的应该放置的位置
在QT项目中，dll文件应该放在QT项目对应的Debug文件夹中  Debug文件夹里的debug和release两个子文件夹不用放  
经过测试，dll放在QT项目目录中、C:\Windows\SysWOW64\中、C:\Windows\system32\中都无法加载到  
另外，还需要注意使用的编译器是32位还是64位  

## 调用方式
显式调用只需要dll文件  
隐式调用需要dll文件、lib文件、h文件  

## 方法一 QLibrary
QLibrary是QT中用来加载库文件的类  
QLibrary属于显式调用方式，即在程序执行到某个函数时才去加载对应的动态库  
详见class_QLibrary.md  