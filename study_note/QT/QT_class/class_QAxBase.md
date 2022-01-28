# QAxBase

## 基本情况
QAxBase是一个抽象类，可以提供初始化和访问COM对象的API  
QAxBase在COM数据类型和等价的Qt数据类型之间作了转换，但有的COM types没有等价的Qt数据结构 
QAxBase不直接使用，而是为其子类QAxObject和QAxWidget提供基础函数  
使用时需要在.pro文件中添加：  
```
QT += axcontainer
```
父类：无  
子类：QAxObject、QAxWidget  


## 使用方法
1. 获取一个QAxObject对象或对象指针
2. 调用setControl()方法建立和COM组件的连接
3. 调用querySubObject()方法获取COM组件中的子对象(方法或属性)
4. 调用QObject::setProperty()方法来设置COM组件中的属性
5. 调用dynamicCall()方法来调用COM组件中的方法


## 构造函数
1. QAxBase::QAxBase(IUnknown \*iface = nullptr)


## 常用公共函数
1. bool QAxBase::setControl(const QString &)
通过setControl函数来建立与控件之间的连接  
1.1 这是最有效的连接方式  
使用控件的classid，classid可以在注册表中查询  
```
ctrl -> setControl("{E8F5278C-0C72-4561-8F7E-CCBC3E48C2E3}");
```
如果要在不同的电脑上连接控件，使用下面的模式  
```
<domain/username>:<password>@server/{8E27C92B-1264-101C-8A2F-040224009C02}
```
如果连接控件需要提供license，使用下面的模式  
```
{8E27C92B-1264-101C-8A2F-040224009C02}:<LicenseKey>
```
如果要连接一个已经在运行的对象，使用下面的的模式  
```
{8E27C92B-1264-101C-8A2F-040224009C02}&
```
1.2 这是第二快的连接方式  
使用已注册的控件的类名来建立连接，可以写版本号，也可以不写  
```
ctrl -> setControl("MSCal.Calendar");
```
1.3 这是最慢但最简单的方式  
使用控件的全名来建立连接  
```
ctrl -> setControl("Calendar Control 9.0");
```
1.4 从一个文件中去初始化对象  
```
ctrl -> setControl("c:/files/file.doc");
```
1.5 直接写出控件所在的实际路径，但在不同的环境中路径可能不同  
注意：路径中用的是/，不是\  
```
hw_pen -> setControl("C:/Windows/SysWOW64/HWPenSign.ocx");
```

2. QString QAxBase::control() const
返回连接对象的UUID  
如果之前建立连接时提供了license key和server名，还会把这些信息一起返回  
但返回信息中不包含用户名和密码  

3. QVariant QAxBase::dynamicCall(const char \*function, const QVariant &var1 = QVariant(), const QVariant &var2 = QVariant(), const QVariant &var3 = QVariant(), const QVariant &var4 = QVariant(), const QVariant &var5 = QVariant(), const QVariant &var6 = QVariant(), const QVariant &var7 = QVariant(), const QVariant &var8 = QVariant())
调用COM组件中的方法，传递参数var1-var8，并返回方法的返回值  
当方法没有返回值，或调用方法失败时，返回一个无效的QVariant  
3.1 只写出方法名，如果不写参数不用加括号
```
hw_pen -> dynamicCall("HWInitialize");
```
3.2 参数可以写到方法名后面
```
activeX->dynamicCall("Navigate(const QString&)", "www.qt-project.org");
activeX->dynamicCall("Value", 5);
```
3.3 参数可以直接写到方法里面
```
activeX->dynamicCall("Navigate(\"www.qt-project.org\")");
```
3.4 方法的返回结果可以用对应数据类型接收
```
QString text = activeX->dynamicCall("Text").toString();
```

4. QVariant QAxBase::dynamicCall(const char \*function, QList<QVariant> &vars)
这是一个重载函数  

5. QAxObject \*QAxBase::querySubObject(const char \*name, const QVariant &var1 = QVariant(), const QVariant &var2 = QVariant(), const QVariant &var3 = QVariant(), const QVariant &var4 = QVariant(), const QVariant &var5 = QVariant(), const QVariant &var6 = QVariant(), const QVariant &var7 = QVariant(), const QVariant &var8 = QVariant())
获取COM控件中的子对象，子对象可以是方法，也可以是属性  
如果name是方法名，必须在name字符串中包含函数参数  
如果name是属性名，则var1-var8参数可以忽略  
备注：可以通过子对象继续调用querySubObject()方法，来获取子对象的子对象  
```
QAxObject *excel =new QAxObject();
excel -> setControl("Excel.Application");//连接Excel控件
QAxObject *workbook = excel -> querySubObject("ActiveWorkBook");//获取Excel控件中正在活动的Workbook对象
QAxObject *worksheet = workbook -> querySubObject("WorkSheets(int)", 1);//获取Workbook中的第一张工作表
```

6. QAxObject \*QAxBase::querySubObject(const char \*name, QList<QVariant> &vars)
这是一个重载函数  

7. QStringList QAxBase::verbs() const
返回COM对象可以执行的所有动作  
如果COM对象不是一个可执行的IOIeObject，或者不支持任何动作，则返回一个空列表  
备注：OLE的默认动作不在这个列表中  