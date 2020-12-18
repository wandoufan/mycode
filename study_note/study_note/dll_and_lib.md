# DLL(dynamic link library)动态链接库

## 基本概念
DLL是一个包含有代码和数据，且可以被多个程序或其他DLL调用的库，一般用在windows系统中  
DLL中常存放一些经常变动的参数和数据，程序可以不改变自身，而是通过调用DLL来实现更新  
例如，在税率计算程序中，税率参数会经常变动，将税率放入DLL中，无需重新安装整个程序就可以实现应用更新  
当某个程序需要调用DLL时就会创建依赖项，该程序就不再是独立的，且当该依赖项被损坏时，该程序就可能出问题  

## DLL的优点
通过使用DLL，程序可以实现模块化，模块只有被用到时才加载，减少内存占用，因此程序速度可以更快  
另外，当DLL更新后，不要求重新建立程序与该DLL之间的链接，程序更新更加便捷  

## 动态库与静态库(static link library)
计算机中的库文件包括动态库和静态库，发展历程为：无库->静态库->动态库  
静态库在程序的链接阶段被复制到了程序中，库中指令都被直接包含在最终生成的可以执行文件中了  
动态库在需要时才被加载到内存中供程序调用，最终生成的可执行文件中不必包含动态库  
在Liunx/Unix系统中静态库文件后缀为.a，动态库文件后缀为.so  
在windows系统中静态库文件后缀为.lib，动态库文件后缀为.dll  

## DLL的使用方式
1. 显式链接(explicit linking)
在程序执行到某个函数时才去加载对应的动态库，程序在运行前并不检查这些动态库是否存在  
2. 隐式链接(implicit linking)
在程序运行前，操作系统就会检查其依赖的动态库（如果缺少动态库程序就直接报错）  
并将动态库都加载到内存中，属于最常用的方式  

## Windows系统中作为DLL实现的文件
1. ActiveX 控件 (.ocx) 文件  
ActiveX 控件的一个示例是日历控件，它使您可以从日历中选择日期  
2. 控制面板 (.cpl) 文件  
.cpl 文件的一个示例是位于控制面板中的项，每个项都是一个专用DLL  
3. 设备驱动程序 (.drv) 文件  
设备驱动程序的一个示例是控制打印到打印机的打印机驱动程序  

## DLL文件的应该放置的位置
在QT项目中，dll文件应该放在QT项目对应的Debug文件夹中  Debug文件夹里的debug和release两个子文件夹不用放  
经过测试，dll放在QT项目目录中、C:\Windows\SysWOW64\中、C:\Windows\system32\中都无法加载到  
另外，还需要注意使用的编译器是32位还是64位  

## 查看DLL中的接口函数
拿到一个DLL文件，除了开发文档，还可以通过以下方法查看其提供的接口函数  
1. dumpbin.exe工具
安装Visual Studio后会有VS自带的dumpbin.exe工具，存放路径示例：  
```
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.27.29110\bin\Hostx64\x64\dumpbin.exe
```
在cmd中使用如下命令即可获得dll的函数：  
```
dumpbin -exports dll_file_path
```
获得的函数结果如下示例(没有详细的函数参数和返回值信息)：  
```
ordinal hint RVA      name
1    0 00001300 AutoFindNum
2    1 00001450 CTR_BUZLED
3    2 000012F0 CloseComm
4    3 00001430 ControlBuzzer
5    4 00001410 ControlLED
6    5 00002840 DllCanUnloadNow
7    6 00004E50 DllGetClassObject
8    7 000057D0 DllInstall
9    8 000057B0 DllRegisterServer
10    9 000057C0 DllUnregisterServer
11    A 00001330 GetSerNum
12    B 000013F0 GetVersionNum
```
2. Dependency Walker工具
下载地址：http://dependencywalker.com/  
可以扫描32或者64位的Windows模块（exe，dll，ocx，sys等）  
然后对其依赖关系进行分析并画出一棵模块依赖树  
这个工具也同样无法获得详细的函数参数和返回值信息  
