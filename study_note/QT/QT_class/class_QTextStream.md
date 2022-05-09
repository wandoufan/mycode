# QTextStream

## 基本功能
QTextStream提供了一个便利的接口用来读写文本文件  



## QDataStream和QTextStream的对比
QTextStream和QDataStream都是面向数据流的，都可以和QIODevice搭配使用  
QDataStream比QTextStream更强大，可以说TextStream能做的事情QDataStream都能做  
QTextStream和QDataStream二者的侧重点不同：  
1. QTextStream侧重于进行文本读写
这里所说的文本指的是普通的简单的QChar、QString、QLatin1Char、int等等  
和C语言中写文件或者网络传输的时候，先将内容填充到一个buffer，然后进行操作有点类似  
2. QDataStream侧重于数据格式和类型
在Linux C开发中，通过socket传输text文本数据比较容易  
但如果想通过socket传输特定的数据节结构而且跨平台以及CUP进行操作和解析就比较麻烦  
对于不同的平台以及不同的内存分配方式的CPU来说，解析的结果可能会有问题  
使用QDataSream就可以解决该问题，对特定格式的类型数据进行完美的输入与输出  