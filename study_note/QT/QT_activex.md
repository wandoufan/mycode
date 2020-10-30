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
注意：使用前要先声明'#include <QAxBase>'  
注意：QAxContainer模块不是QTcore自带的，使用QAxObject类和QAxWidget类之前，要在项目的.pro文件中进行声明：'QT +=  axcontainer'，否则报错'QAxObject' file not found  
**常用函数**
1. QVariant QAxBase::dynamicCall(const char \*function, const QVariant &var1 = QVariant(), ..., const QVariant &var8 = QVariant())
dynamicCall函数可以调用COM组件的方法，并返回方法的返回值  
当方法没有返回值，或调用方法失败时，返回一个无效的QVariant  
第一个参数是字符串格式的组件方法名，另外最多可以传递八个QVariant类型的参数  
备注：这八个参数好像是给组件方法的参数  



2. QAxObject \*QAxBase::querySubObject(const char \*name, const QVariant &var1 = QVariant(), ..., const QVariant &var8 = QVariant())
querySubObject函数可以调用COM组件的方法或属性，返回一个QAxObject类型的指针  
当调用的是组件的方法时，字符串必须包含完整的函数标准  
当调用的是组件的属性时，字符串必须是属性名，后面的八个参数可以忽略  

3. 

## QAxObject
QAxObject类提供了一个支持COM对象的QObject  
QAxObject和QAxWidget都是QAxBase的子类  
注意：使用前要先声明'#include <QAxObject>'
注意：QAxContainer模块不是QTcore自带的，使用QAxObject类和QAxWidget类之前，要在项目的.pro文件中进行声明：QT +=  axcontainer'，否则报错'QAxObject' file not found
**常用函数**


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

