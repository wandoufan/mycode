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
**QT对象和COM组件的对应关系**
Qt类中的属性对应COM组件中的属性  
Qt类中公有的插槽函数(slots)对应COM组件中的方法  
Qt类中的信号(signals)对应COM组件中的事件  


## QAxObject
QAxObject类提供了一个支持COM对象的QObject  
QAxObject和QAxWidget都是QAxBase的子类  
注意：QAxContainer模块不是QTcore自带的，使用QAxObject类和QAxWidget类之前，要在项目的.pro文件中进行声明：QT +=  axcontainer'

1. QVariant QAxBase::dynamicCall(const char \*function, const QVariant &var1 = QVariant(), ..., const QVariant &var8 = QVariant())
dynamicCall函数可以调用COM组件的方法，并返回方法的返回值  
当方法没有返回值，或调用方法失败时，返回一个无效的QVariant  
第一个参数是字符串格式的组件方法名，另外最多可以传递八个QVariant类型的参数  
备注：这八个参数好像是给组件方法的参数  

关于QVariant类型
QVariant好像是QT的通用数据类型的封装容器 可以存储多种类型的数据
```
// QVariant转QString
QVariant qv;
QString qs = qv.toString();

// QString 转 QVariant
QString qs;
QVariant qv(qs);
```

## QAxWidget
类中函数：
```
webWidget = new QAxWidget;
//设置ActiveX控件为IEMicrosoft Web Browser
//设置ActiveX控件的id，最有效的方式就是使用UUID
//此处的{8856F961-340A-11D0-A96B-00C04FD705A2}就是Microsoft Web Browser控件的UUID
webWidget->setControl(QString::fromUtf8("{8856F961-340A-11D0-A96B-00C04FD705A2}")); 
webWidget->setObjectName(QString::fromUtf8("webWidget"));//设置控件的名称
webWidget->setFocusPolicy(Qt::StrongFocus);//设置控件接收键盘焦点的方式：鼠标单击、Tab键
webWidget->setProperty("DisplayAlerts",false); //不显示任何警告信息。
webWidget->setProperty("DisplayScrollBars",true); // 显示滚动条
```


## 实现过程
下面以在QT中调用汉王手写板的HWPenSign.ocx控件为例进行介绍：  
1. HWPenSign.ocx文件位于C:\Windows\SysWOW64目录下  


### 步骤一：获取ID
备注：不一定要用id去连接，setControl函数用控件名或控件路径也可以  

### 步骤二：
方法一
报错1
```
使用两个类都有如下报错：
CoCreateInstance failure (没有注册类)
QAxBase::setControl: requested control {E8F5278C-0C72-4561-8F7E-CCBC3E48C2E3} could not be instantiated
QAxBase::dynamicCallHelper: Object is not initialized, or initialization failed
```
**已经测试了的解决办法**
--> 试了把id换成路径+文件名，还是同样的报错
--> 试了用两个类都有同样报错
--> 用regsvr32 \*.ocx或regsvr32 \*.dll来手动注册了控件
**可能的解决办法**
--> HWPenSign.ocx是个控件不是组件，但在注册表里找到的是clsid
--> 如何获取uuid ，换上uuid试试
但是oleview.exe打开ocx时报错
--> 对象不能实例化，是不是调用方法不对，这可能不是个对象
--> 按两个函数搜一下，setControl和dynamicCallHelper
**最终解决办法**
id识别不出来，原因未知，用路径+文件名识别出来了
注意：路径中是/，不是\
-------------------------------------------------
报错2
```
QAxBase::dynamicCallHelper: Object does not support automation
```
**已经测试了的解决办法**
--> 试了用两个类都有同样报错
**可能的解决办法**
--> CoInitialize CoInitializeEx OleInitialize 这几个函数
头文件<windows.h>
调用CoInitializeEx(nullptr, COINIT_MULTITHREADED);
CoInitializeEx是 Windows提供的API函数，为当前线程初始化COM库并设置并发模式 。应用程序调用com库中的函数（除CoGetMalloc和内存分配函数）之前必须初始化com库。  
--> 试试querySubObject函数来替代dynamicCall函数


方法二
dumpcpp.exe
报错：dumpcpp: type library '{E8F5278C-0C72-4561-8F7E-CCBC3E48C2E3}' not found
--> 花了很多时间但没有找到这个报错的原因
--> 试试不用id，用路径+文件名来执行，没有报错，
在C:\Qt\5.15.1\msvc2019_64\bin目录(dumpcpp同目录)下找到生成的.cpp和.h文件
代码看不太懂，不会用