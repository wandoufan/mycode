# 在QT中调用ActiveX控件

## 基本情况
备注：一般不直接用c++去调用ocx控件，而是在QT或MFC里去实现调用ocx控件  
Qt提供了QtActiveX框架来实现微软ActiveX的开发，支持两种开发方式：  
1. 使用QAxContainer模块将已有的COM组件或ActiveX控件引入到QT的应用程序中  
QAxObject类支持COM组件  
QAxWidget类支持ActiveX控件  
2. 使用QAxServer模块将QT的应用程序或QT的对象导出成COM组件或ActiveX控件供他人使用  
QAxAggregated类定义了COM组件接口  
QAxFactory类定义了创建COM对象的工厂类  
QAxBindable类定义了QT对象和COM对象之间的转换关系  


## QT对象和COM组件的对应关系
Qt类中的属性对应COM组件中的属性  
Qt类中公有的插槽函数(slots)对应COM组件中的方法  
Qt类中的信号(signals)对应COM组件中的事件  


## QAxBase
QAxBase是一个抽象类，提供了API接口来初始化和调用COM对象  
QAxBase是QAxObject和QAxWidget的父类，提供了二者很多公用的基础函数  
注意：QAxBase是抽象类不能直接使用，必须由其子类QAxObject和QAxWidget来实例化  
QAxBase在COM数据类型和等价的Qt数据类型之间作了转换，但有的COM types没有等价的Qt数据结构  
注意：使用前要先声明'#include <QAxBase>'  
注意：QAxContainer模块不是QTcore自带的，使用QAxObject类和QAxWidget类之前，要在项目的.pro文件中进行声明：'QT +=  axcontainer'，否则报错'QAxObject' file not found  
**常用函数**
1. bool setControl(const QString &)
通过setControl函数来建立与控件之间的连接，包括以下多种方法：  
方法一：使用控件的classid，classid可以在注册表中查询，这是最有效的连接方式  
```
hw_pen -> setControl("{E8F5278C-0C72-4561-8F7E-CCBC3E48C2E3}");
```
方法二：使用已注册的控件的类名来建立连接，可以写版本号，也可以不写  
```
ctrl -> setControl("MSCal.Calendar");
ctrl -> setControl("Calendar Control 9.0");
```
方法三：直接写出控件所在的实际路径，但在不同的环境中路径可能不同  
注意：路径中用的是/，不是\  
```
hw_pen -> setControl("C:/Windows/SysWOW64/HWPenSign.ocx");
```
2. QVariant QAxBase::dynamicCall(const char \*function, const QVariant &var1 = QVariant(), ..., const QVariant &var8 = QVariant())
dynamicCall函数可以调用COM组件的方法，并返回方法的返回值  
当方法没有返回值，或调用方法失败时，返回一个无效的QVariant  
第一个参数是字符串格式的组件方法名，另外最多可以传递八个QVariant类型的参数作为该方法的参数  
```
//只写出方法名，如果不写参数不用加括号
hw_pen -> dynamicCall("HWInitialize");
//参数可以写到方法名后面
activeX->dynamicCall("Navigate(const QString&)", "www.qt-project.org");
activeX->dynamicCall("Value", 5);
//参数可以直接写到方法里面
activeX->dynamicCall("Navigate(\"www.qt-project.org\")");
//方法的返回结果可以用对应数据类型接收
QString text = activeX->dynamicCall("Text").toString();
```


## QAxObject
QAxObject类提供了一个支持COM对象的QObject  
QAxObject和QAxWidget都是QAxBase的子类  
注意：使用前要先声明'#include <QAxObject>'  
注意：QAxContainer模块不是QTcore自带的，使用QAxObject类和QAxWidget类之前，要在项目的.pro文件中进行声明：QT +=  axcontainer'，否则报错'QAxObject' file not found


## QAxWidget
QAxWidget类提供了一个支持ActiveX控件的QObject  
QAxObject和QAxWidget都是QAxBase的子类  
注意：使用前要先声明'#include <QAxWidget>'  
注意：QAxContainer模块不是QTcore自带的，使用QAxObject类和QAxWidget类之前，要在项目的.pro文件中进行声明：QT +=  axcontainer'，否则报错'QAxObject' file not found


## QT调用控件方法一
利用QT提供的QAxObject类或QAxWidget类来完全手写代码  
1. 获取一个QAxObject或QAxWidget的实例化对象或对象指针  
2. 用setControl函数建立与控件之间的连接  
3. 用dynamicCall函数来调用控件中的各个方法  


## QT调用控件方法二
利用QT提供的dumpcpp.exe工具来自动生成代码  
备注：这种方法更简单，而且可以展示出类中提供的所有函数接口  
1. 用管理员权限打开cmd，在cmd中进入到dumpcpp.exe所在的目录  
dumpcpp.exe一般是位于QT的编译器目录的bin目录下，例如:'C:\Qt\5.15.1\msvc2019_64\bin'  
2. 在cmd中输入命令'dumpcpp.exe classid或ocx路径'  
```
'dumpcpp.exe C:/Windows/SysWOW64/HWPenSign.ocx'
'dumpcpp.exe {a0637eb8-68db-4cf0-a26c-1ca438e1d6d1}'
```
3. 在dumpcpp.exe的同目录下会生成.cpp和.h文件，例如'hwpensignlib.h'和'hwpensignlib.cpp'  
将这两个文件拷贝到QT项目目录下，可能项目识别不到这两个文件，需要在.pro文件中手动写入文件名  
4. 自动生成的.h文件中会定义一个继承于QAxWidget或QAxObject的子类  
子类中的方法就是控件提供的所有接口函数，在这里可以看到函数需要的参数和返回类型  
自动生成的.cpp文件中已经在构造函数里使用setControl函数和classid与控件建立了连接  
```
class HWPENSIGNLIB_EXPORT HWPenSign : public QAxWidget
```
5. 获取一个该子类的实例化对象或对象指针，然后直接调用类中成员函数即可，不必再使用dynamicCall函数


## QT调用控件方法三
通过将ocx控件生成dll来实现调用   
具体实现过程未测试  


## 汉王手写板开发中遇到的实际问题
1. 基本情况
下面以在QT中调用汉王手写板ESP370的HWPenSign.ocx控件为例进行介绍：  
HWPenSign.ocx文件有两个，都对应着同一个classid  
其中32位的在C:\Windows\SysWOW64目录下，64位的在C:\Windows\System32目录下  
2. 报错1
使用setControl函数+classid来连接控件，但报错对象无法初始化  
```
CoCreateInstance failure (没有注册类)
QAxBase::setControl: requested control {E8F5278C-0C72-4561-8F7E-CCBC3E48C2E3} could not be instantiated
QAxBase::dynamicCallHelper: Object is not initialized, or initialization failed
```
已经确认使用的classid没错，控件也已经进行了注册，但还是一直报错  
使用dumpcpp生成的代码默认使用的是classid连接，也是同样的报错  
最后使用setControl函数+ocx路径后对象连接成功  
3. 报错2
使用dynamicCall函数调用控件方法，但报错对象不支持自动化，尝试了各种办法都无法解决  
```
QAxBase::dynamicCallHelper: Object does not support automation
```
使用dumpcpp自动生成子类HWPenSign来直接调用控件的函数，不再使用dynamicCall函数  
不再有不支持化的报错，但调用初始化函数后手写板没反应，返回值1  
询问厂家，返回值1代表程序与设备不匹配，但没有具体信息，不知道原因  
4. 最终解决方法
之前程序都是用的默认64位编译器，改用32位编译器后问题彻底解决了  
可以使用classid来连接，也可以使用dynamicCall函数来调用，但前提是必须使用32位的编译器  
测试使用C:\Windows\System32下64位的ocx还是不行，只要用64位编译器就同样报错，原因未知  