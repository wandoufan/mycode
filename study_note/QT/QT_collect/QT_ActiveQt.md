# ActiveQt框架

## 基本情况
Qt支持微软的ActiveX和COM，因此基于Windows系统的开发者可以实现：  
1. 在Qt程序中通过ActiveX server来访问和调用ActiveX控制和COM对象
2. 使Qt程序变成COM servers，可以带有一定数量的Qt objects和widgets作为ActiveX控制和COM对象


## 微软office接口
office中的Word、Excel、Access等应用都提供了详细的接口  
所有的对象、以及对象中的方法和属性，详细见下面：  
> https://docs.microsoft.com/zh-cn/office/vba/api/excel.workbooks


## ActiveQt框架的组成
ActiveQt框架包含以下两个模块：  
1. QAxContainer模块
2. QAxServer模块


-----------------QAxContainer模块-----------------
## 基本功能
QAxContainer模块将已有的COM组件或ActiveX控件导入到Qt程序中进行调用  
QAxContainer模块不是Qt core自带的，使用时需要在.pro文件中添加：  
```
QT += axcontainer
```
详见Qt 帮助手册："Using ActiveX controls and COM in Qt"  


## 常见报错
1. QAxBase::dynamicCall()执行失败
```
QAxBase::internalInvoke: No such method
```
要调用的函数和对象中的所有API都不匹配  
2. QAxBase::dynamicCall()执行失败
```
Error calling IDispatch member: Non-optional parameter missing
```
要调用的函数正确，但函数中的参数不够  
3. QAxBase::dynamicCall()执行失败
```
Error calling IDispatch member: Type mismatch in parameter n
```
要调用的函数正确，但函数的第n个参数类型不对
4. QAxScriptManager::call()执行失败
```
QAxScriptManager::call(): No script provides this function
```
5. 无法和COM对象建立连接
control可能需要管理员权限或者license key  
license key一般也传递给QAxBase::setControl()方法  


## 调用COM对象的API的方法
1. 产生一个C++命名空间
使用dumpcpp工具

2. 通过名字调用(常用)

3. 通过一个脚本引擎

4. 使用本地COM接口


## 类之间的继承关系
```
QObject -
		| - QAxObject - QAxScriptEngine
QAxBase -
		| - QAxWidget
QWidget -
```

## 包含的类
1. QAxBase
QAxBase是一个抽象类，可以提供初始化和访问COM对象的API  
2. QAxObject
QAxObject是一个封装了COM对象的QObject  
3. QAxWidget
QAxWidget是一个封装了ActiveX控制的QWidget  
4. QAxScript
QAxScript是一个脚本代码的封装容器  
5. QAxScriptEngine
QAxScriptEngine是一个脚本引擎的封装容器  
6. QAxScriptManager
QAxScriptManager是程序对象和脚本代码之间的连接桥梁  
7. QAxSelect
QAxSelect为已经注册的COM组件选择对话框  


## 代码示例：通过调用office官方接口把已经存在的excel文件转成pdf文件
备注：实际测试，金山WPS软件也具有这个接口
```
QString excel_file_path = "D:/myexcel1.xlsx";
QString pdf_file_path = "D:/mypdf1.pdf";
QAxObject *excel =new QAxObject();
if(excel -> setControl("Excel.Application")) //连接Excel控件
{
    qDebug() << "连接成功";
    excel -> setProperty("Visible", false);//设置窗体不可见
    //备注：Workbooks对象是当前打开的所有Excel文件的集合
    QAxObject *workbooks = excel -> querySubObject("WorkBooks");//获取Excel控件中的Workbooks对象
    workbooks -> dynamicCall("Open(const QString&)", excel_file_path);//打开excel文件
    //备注：Workbook对象是Workbooks集合中的某个成员
    QAxObject *workbook = excel -> querySubObject("ActiveWorkBook");//获取Excel控件中正在活动的Workbook对象
    //备注：Worksheets对象是excel中的所有工作表的集合
    QAxObject *worksheets = workbook -> querySubObject("Worksheets");//获取excel中所有的工作表
    //备注：Worksheet对象是Worksheets集合中的某个成员
    QAxObject *worksheet1 = workbook -> querySubObject("WorkSheets(int)", 1);//获取excel中第一张工作表
    QAxObject *worksheet2 = workbook -> querySubObject("WorkSheets(int)", 2);//获取excel中第二张工作表
    QAxObject *worksheet3 = workbook -> querySubObject("WorkSheets(int)", 3);//获取excel中第三张工作表
    //尝试把每个工作表都缩放为一页，实测无效
    worksheet1 -> setProperty("Zoom", false);
    worksheet1 -> setProperty("FitToPagesWide", 1);
    worksheet1 -> setProperty("FitToPagesTall", 1);
    worksheet2 -> setProperty("Zoom", false);
    worksheet2 -> setProperty("FitToPagesWide", 1);
    worksheet2 -> setProperty("FitToPagesTall", 1);
    worksheet3 -> setProperty("Zoom", false);
    worksheet3 -> setProperty("FitToPagesWide", 1);
    worksheet3 -> setProperty("FitToPagesTall", 1);
    //把excel文件转换为pdf文件
    workbook -> dynamicCall("ExportAsFixedFormat(QVariant, QVariant)", 0, pdf_file_path);//调用Workbook对象中的格式转换函数
    workbook -> dynamicCall("Close()");
}
else
{
    qDebug() << "连接失败";
}
```
以上程序测试发现，第一次是可以用的，但在第二次调用EXCEL控件来转换为pdf时  
```
workbooks -> dynamicCall("Open(const QString&)", xlsx_file_name);//打开excel文件
```
这一行语句会发生如下报错：  
```
QAxBase: Error calling IDispatch member Open: Exception thrown by server
             Code       : -2146827284
             Source     : Microsoft Excel
             Description: ????? Workbooks ? Open ??
             Help       : xlmain11.chm
         Connect to the exception(int,QString,QString,QString) signal to catch this exception
C:\Program Files (x86)\SogouInput\Components\
```
尝试在第一次转换结束时，把相关的对象都手动删除掉，但仍然有同样报错，目前没有找到解决办法  
```
workbook -> dynamicCall("Close()");
workbooks -> dynamicCall("Close()");
excel -> dynamicCall("Quit()");
delete workbook;
delete workbooks;
delete excel;
```


-----------------QAxServer模块-----------------
## 基本功能
QAxServer模块将Qt程序或Qt对象导出成COM组件或ActiveX控件供他人使用  
备注：这个模块是一个只能在Windows系统上使用的静态库  
详见Qt 帮助手册："Building ActiveX servers in Qt"  

## 包含的类
1. QAxFactory
QAxFactory定义一个用来创建COM对象的工厂类  
2. QAxBindable
QAxBindable提供Qt widget和COM对象之间的接口  
3. QAxAggregated
QAxAggregated可以成为执行额外COM接口的子类  


-----------------ActiveQt框架提供的工具-----------------
## Interface Description Compiler(IDC)


## dumpcpp


## dumpdoc


## testcon(An ActiveX Test Container)


-----------------------old------------------------------





## QT对象和COM组件的对应关系
Qt类中的属性对应COM组件中的属性  
Qt类中公有的插槽函数(slots)对应COM组件中的方法  
Qt类中的信号(signals)对应COM组件中的事件  


## QAxWidget
QAxWidget类提供了一个支持ActiveX控件的QObject  
QAxObject和QAxWidget都是QAxBase的子类  
注意：使用前要先声明'#include <QAxWidget>'  
注意：QAxContainer模块不是QTcore自带的，使用QAxObject类和QAxWidget类之前，要在项目的.pro文件中进行声明：QT +=  axcontainer'，否则报错'QAxObject' file not found


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
备注：不知道classid的情况下，可以先使用路径，生成的.cpp文件中setcontrol函数会有写出classid  
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


## 获取ocx控件的文档
和dumpcpp.exe类似，QT还提供了dumpdoc.exe工具来自动生成ocx的文档  
可以通过ocx的文件路径或classid来指定ocx  
-o参数用来说明生成文档的路径，其中文档为html格式  
```
'dumpdoc.exe C:\cwui.ocx -o E:\cwui_doc.html'
```


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