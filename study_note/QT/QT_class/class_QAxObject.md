# QAxObject

## 基本情况
QAxObject是一个封装了COM对象的QObject  
QAxObject中没有什么可用的公共函数，主要就是用构造函数来获得一个对象  
使用时需要在.pro文件中添加：  
```
QT += axcontainer
```
父类：QObject、QAxBase  
子类：QAxScriptEngine  


## 构造函数
1. QAxObject::QAxObject(IUnknown \*iface, QObject \*parent = nullptr)
可以在构造时就初始化COM对象，也可以后面再用setControl()来连接COM对象  

2. QAxObject::QAxObject(const QString &c, QObject \*parent = nullptr)
可以在构造时就初始化COM对象，也可以后面再用setControl()来连接COM对象  
```
QAxObject *excel = new QAxObject("Excel.Application");
```

3. QAxObject::QAxObject(QObject \*parent = nullptr)


## 常用公共函数
1. bool QAxObject::doVerb(const QString &verb)
要求COM对象执行verb动作，如果COM对象可以执行该动作返回true，否则返回false  
所有可执行动作通过QAxBase::verbs()查看  

