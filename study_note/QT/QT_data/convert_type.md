# QT数据类型转换

## 注意事项
1. 在QT中str不是关键字，也不是系统函数，不能直接用str对数据进行格式转换  
2. 函数中有base参数的可以在类型转换的同时实现进制的转换  

## QString转int
int toInt(bool \*ok = nullptr, int base = 10)  
将字符串转换为整型并返回一个整型数字，当转换失败时返回0  
ok参数用来指示是否转换成功，当失败时ok为false，当成功时ok为true  
base参数用来设置数字进制，范围在2到36之间，默认为10进制  
当字符串以'0x'开始，用16进制；当字符串以'0'开始，用8进制  
```
bool ok;
QString str1 = "123";
int num = str.toInt(&ok);
```

## int转QString
1. QString number(long n, int base = 10)  
把整型转换为字符串并返回一个QString字符串  
base参数用来设置数字进制，范围在2到36之间，默认为10进制  
注意：只能用QString::number(num)格式，不能用str.number(num)格式  
```
int num = 100;
QString str = QString::number(num);
```
2. &QString setNum(int n, int base = 10)  
直接把整型数字写入一个QString字符串中，没有返回值  
注意：number()和setNum()的不同  
```
QString str;
str.setNum(1234, 2); //将整数1234转为2进制后再转为字符串
```

## QString转QByteArray
注意：QString类型的字符串不能直接用cout输出，否则报错，必须先转换为QByteArray格式  
1. QByteArray toLatin1()  
返回一个QByteArray格式的Latin-1字符串表达式  
适合于普通的英文字符串，但不能包含中文，否则会产生乱码  
```
Qstring  str;
char*  ch;
QByteArray ba = str.toLatin1();
ch=ba.data();  //不能直接用cout输出QByteArray对象，而是要输出对象的data()方法
```
2. QByteArray toUtf8()  
返回一个QByteArray格式的UTF8字符串表达式  
UTF8格式支持中文字符  
```
Qstring  str;
char*  ch;
QByteArray ba = str.toUtf8();
ch=ba.data();  //不能直接用cout输出QByteArray对象，而是要输出对象的data()方法
```
3. QByteArray toLocal8Bit()  
返回一个QByteArray格式的8位编码字符串表达式  
```
Qstring  str;
char*  ch;
QByteArray ba = str.toLocal8Bit();
ch=ba.data();  //不能直接用cout输出QByteArray对象，而是要输出对象的data()方法
```

## QByteArray转QString

## QStringList转换为QString
QString join(QString &separator)
将字符串列表中的元素拼接起来，返回一个QString
注意：join函数的连接字符串必须要有，可以是空字符串，但不能不写参数
```
QStringList alist;
alist << "a" << "b" << "c" << "d";
QString str1;
str1 = alist.join("+"); //写成str1 = alist.join();会报错，join函数必须要有参数
```

## QString转QStringList
QStringList split(const QString &sep, Qt::SplitBehavior behavior = Qt::KeepEmptyParts, Qt::CaseSensitivity cs = Qt::CaseSensitive)  
字符串按照指定分割符分割为多个字符串，并返回一个QStringList  
如果分割符在原始字符串中不匹配，则返回的列表中只包含一个原始字符串  
如果分割符为空字符串，则返回列表的元素为原始字符串的每个字符和前后各一个空字符串  
例如："abcd"用""分割出的列表为["","a","b","c","d",""]  
例如："/a/b/c/"用'/'分割出的列表为["", "a", "b", "c", ""]  
```
QString str1 = "a,bb,ccc,dddd";
QStringList list1 = str1.split(','); //["a","bb","ccc","dddd"]
QByteArray byte1;
for(int i = 0; i < list1.size(); i++)
{
    byte1 = list1[i].toLatin1();
    cout << byte1.data() << endl;
}
```

## QVariant转QString
```
QVariant qv;
QString qs = qv.toString();
```

## QString 转 QVariant
```
QString qs;
QVariant qv(qs);
```