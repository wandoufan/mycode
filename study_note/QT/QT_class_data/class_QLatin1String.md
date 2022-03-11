# QLatin1String

## 基本功能
QLatin1String类可以将US-ASCII/Latin-1编码成为字符串  
许多QString的成员函数被重载后，只能接收char指针作为参数，而不是QString  
这些成员函数通常被优化来避免为char指针数据来构造一个QString对象  
```
QString str;
if(str == "auto")//执行更快
{...}
if(str == QString("auto"))//执行更慢
{...}
```
上面第一种比第二种执行更快，因为它不需要构建临时的QString对象，也不需要对字符数据进行深拷贝  
```
QString str;
if(str == QLatin1String("auto")//执行更快
{...}
```
QLatin1String是一个非常高效的转换器，和上面第一种方法的效果一样，而且比QString::fromLatin1()转换更快  


## 使用示例
1. 使用构造函数后，可以用QLatin1String来替换QString
```
QLabel *label = new QLabel(QLatin1String("MOD"), this);
```


## 构造函数
1. QLatin1String::QLatin1String(const QByteArray &str)
构建一个存储str的QLatin1String对象  
注意：str数据没有被拷贝下来，必须要保证QLatin1String对象的生命周期内，str数据不会被删除或修改  

2. QLatin1String::QLatin1String(const char \*str, int size)
构建一个存储size大小str的QLatin1String对象  
注意：str数据没有被拷贝下来，必须要保证QLatin1String对象的生命周期内，str数据不会被删除或修改  

3. QLatin1String::QLatin1String(const char \*first, const char \*last)
构建一个QLatin1String对象，数据为从first开始，长度last-first的字符串  
first和last可以同时为空指针，此时会构造出一个空的Latin-1字符串  
注意：str数据没有被拷贝下来，必须要保证QLatin1String对象的生命周期内，str数据不会被删除或修改  

4. QLatin1String::QLatin1String(const char \*str)
构建一个存储str的QLatin1String对象  
注意：str数据没有被拷贝下来，必须要保证QLatin1String对象的生命周期内，str数据不会被删除或修改  


## 常用公共函数
