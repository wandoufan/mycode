# QString

## 基本功能
QString类提供了一个编码的字符串，存储了若干个QChar类型的16位字符  


## 使用示例
1. 初始化一个QString类型的字符串
```
QString str1 = "HELLO";
```
注意：QString类型的字符串不能直接用cout输出，否则报错，必须先转换为QByteArray格式  
2. null字符串和empty字符串的区别
null字符串是初始化之后还未赋值的字符串，empty字符串是长度为0的空字符串  
除了isNull()函数外，其他函数不会区分对待null字符串和empty字符串  
推荐使用isEmpty()函数，避免使用isNull()函数  
```
QString str1, str2="";
QString(str1).isNull();            // returns true
QString(str1).isEmpty();           // returns true
QString(str2).isNull();            // returns false
QString(str2).isEmpty();           // returns true
QString("abc").isNull();           // returns false
QString("abc").isEmpty();          // returns false
```


## 构造函数
1. QString::QString(const QByteArray &ba)

2. QString::QString(const char \*str)

3. QString::QString(QString &&other)

4. QString::QString(QLatin1String str)

5. QString::QString(int size, QChar ch)
字符串中的每个字符都设置为ch，长度为size  

6. QString::QString(QChar ch)
字符串的长度设置为1，字符为ch  

7. QString::QString()
构造一个null字符串，同时也是empty的  


## 数据类型转换相关的常用公共函数
注意：QString类型的字符串不能直接用cout输出，否则报错，必须先转换为QByteArray格式  
1. int toInt(bool \*ok = nullptr, int base = 10)
将字符串转换为整型并返回一个整型数字，当转换失败时返回0  
ok参数用来指示是否转换成功，当失败时ok为false，当成功时ok为true  
base参数用来设置数字进制，范围在2到36之间，默认为10进制  
当字符串以'0x'开始，用16进制；当字符串以'0'开始，用8进制  
```
bool ok;
QString str1 = "123";
int num = str.toInt(&ok);
```

2. QByteArray QString::toLatin1() const
返回一个QByteArray格式的Latin-1字符串表达式  
适合于普通的英文字符串，但不能包含中文，否则会产生乱码  
```
Qstring  str;
char*  ch;
QByteArray ba = str.toLatin1();
ch=ba.data();  //不能直接用cout输出QByteArray对象，而是要输出对象的data()方法
```

3. QByteArray QString::toLocal8Bit() const
返回一个QByteArray格式的8位编码字符串表达式  
```
Qstring  str;
char*  ch;
QByteArray ba = str.toLocal8Bit();
ch=ba.data();  //不能直接用cout输出QByteArray对象，而是要输出对象的data()方法
```

4. QByteArray QString::toUtf8() const
返回一个QByteArray格式的UTF8字符串表达式  
UTF8格式支持中文字符  
```
Qstring  str;
char*  ch;
QByteArray ba = str.toUtf8();
ch=ba.data();  //不能直接用cout输出QByteArray对象，而是要输出对象的data()方法
```

5. QStringList QString::split(const QString &sep, Qt::SplitBehavior behavior = Qt::KeepEmptyParts, Qt::CaseSensitivity cs = Qt::CaseSensitive)  
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


## 常用公共函数
注意：有的函数直接修改原字符串，没有返回值；有的函数不改动原字符串，会把结果当做一个返回值  
1. &QString QString::append()
在str1后面添加字符串str2  
```
str1.append(str2); 
```
2. &QString QString::prepend()
在str1前面添加字符串str2  
```
str1.prepend(str2);
```
3. QString QString::toUpper()
str2变大写  
```
str3 = str2.toUpper();
```
4. QString QString::toLower()
str1变小写  
```
str3 = str1.toLower();
```
5. int QString::size()
返回字符串中字符个数，其中一个汉字算一个字符  
```
num = str1.size();
```
6. int QString::count()
返回字符串中字符个数，其中一个汉字算一个字符  
```
num = str1.count();
```
7. int QString::length()
返回字符串中字符个数，其中一个汉字算一个字符  
```
num = str1.length(); 
```
8. QString QString::trimmed()
去掉字符串首尾的空格  
```
str3 = str1.trimmed();
```
9. QString QString::simplified()
去掉字符串首尾的空格，且当中间有多个连续空格时也用一个空格替换  
```
str3 = str1.simplified();
```
10. int QString::indexOf(const QString &str, int from = 0 , Qt::CaseSensitivity cs = Qt::CaseSensitive)
查找str2在str1中首次出现的位置，如果没有找到str2则返回-1  
from参数设置开始查找的位置，默认为0；当from为-1时，从最后一次字符开始，以此类推  
cs参数用来指定查找时是否对大小写敏感，默认区分大小写，Qt::CaseInsensitive时不区分  
```
num = str1.indexOf(str2); 
```
11. int QString::lastIndexOf(const QString &str, int from = -1, Qt::CaseSensitivity cs = Qt::CaseSensitive)
查找str2在str1中最后出现的位置，如果没有找到str2则返回-1  
from参数默认为-1；当from为-2时，从倒数第二个字符开始，以此类推  
cs参数用来指定查找时是否对大小写敏感，默认区分大小写，Qt::CaseInsensitive时不区分  
```
num = str1.lastIndexOf(str2);
```
12. bool QString::contains(const QString &str, Qt::CaseSensitivity cs = Qt::CaseSensitive)
判断str1中是否包含str2字符串，返回true或false  
```
result = str1.contains("abc");
```
13. bool QString::startsWith(const QString &s, Qt::CaseSensitivity cs = Qt::CaseSensitive)
判断str1是否以str2开头，返回true或false  
```
result = str1.startsWith(str2);
```
14. bool QString::endsWith(const QString &s, Qt::CaseSensitivity cs = Qt::CaseSensitive)
判断str1是否以str2结尾，返回true或false  
```
result = str1.endsWith(str2);
```
15. QString QString::left(int n)
从str1左边取n个字符  
```
str3 = str1.left(n);
```
16. QString QString::right(int n)
从str1右边取n个字符  
```
str3 = str1.right(n);
```
17. QString QString::section (const QString &sep, int start, int end = -1, SectionFlags flags = SectionDefault)
以逗号为分隔符将str1分割，然后提取出start到end的部分  
```
str3 = str1.section(',', 2, 3);
```
18. QChar QString::at(int position)
获取字符串中指定位置的字符  
```
char1 = str1.at(n);
```
19. void QString::resize(int size, QChar fillChar)
调整字符串str1的长度为n  
当n小于字符串的当前长度时，会把字符串截断，只保留前n个字符  
当n大于字符串的当前长度时，会将字符串填充到长度n，填充字符可以写到第二个参数里  
```
str1.resize(n);
```
20. QString QString::arg(const QString &a, int fieldWidth = 0, QChar fillChar = QLatin1Char(' ')) const
向QString字符串中插入相应的QString类型的变量  
相当于C++提供的%d、%s、%c等通配符  
注意：这里的字符串中不再是通配符，而是从1开始计数的数字，与后面的参数一一对应  
```
sql_command = QString("insert into user_info values('%1', '%2', '%3', '%4');").arg(user_id).arg(user_name).arg(card_id).arg(user_remark);
```


## 静态公共函数
1. [static] int QString::compare(const QString &s1, const QString &s2, Qt::CaseSensitivity cs = Qt::CaseSensitive)
比较s1和s2两个字符串，字符串按照ASCII码值的大小进行比较  
返回一个大于/小于/等于0的int类型，分别代表s1大于/小于/等于s2  
cs参数默认为大小写敏感  
```
int x = QString::compare("aUtO", "AuTo", Qt::CaseInsensitive);  // x == 0
int y = QString::compare("auto", "Car", Qt::CaseSensitive);     // y > 0
int z = QString::compare("auto", "Car", Qt::CaseInsensitive);   // z < 0
```

2. [static] QString QString::number(int n, int base = 10)
把整型转换为字符串并返回一个QString字符串  
base参数用来设置数字进制，范围在2到36之间，默认为10进制  
注意：只能用QString::number(num)格式，不能用str.number(num)格式  
```
int num = 100;
QString str = QString::number(num);
```

3. [static] QString QString::fromLatin1(const QByteArray &str)
把QByteArray转换为QString  