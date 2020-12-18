# QDebug

## 基本功能
QDebug类提供了可以产生debugging信息的输出流，常用来输出调试信息  
使用QtDebug前要'#include <QDebug>'  


## QtDebug常用函数
1. qDebug()
qDebug是最常用的函数，可以代替cout输出一个或多个参数信息  
qDebug函数可以直接使用，不必声明所属的类，也不必通过对象引用  
qDebug函数输出信息时自动换行，后面不需要写endl  
对应QString类型的数据，qDebug函数也可以不经过格式转换而直接输出  
```
QString s1, s2;
s1 = "this is test";
s2 = "这是一个测试";
qDebug() << s1;
qDebug() << s2;
qDebug() << s1 << "  " << s2;
```