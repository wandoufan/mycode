# QString

## 基本功能
QString类提供了一个编码的字符串  
QString存储了若干个QChar类型的16位字符，每一个QChar都是UTF-16编码单元  


## QByteArray和QString的比较
大多数情况下，我们要使用的都是QString  
QString存储的是16位编码字符，因此可以很容易的存储非ASCII/非Latin-1字符  
而QByteArray更多的使用在以下两种情况：  
1. 需要存储原始二进制数据
2. 内存保护是非常重要的场景(如Qt在嵌入式Linux中应用)


## 使用示例
1. 初始化一个QString类型的字符串
注意：QString类型的字符串不能直接用cout输出，否则报错，必须先转换为QByteArray格式  
```
QString str1 = "HELLO";
cout << str1.toLatin1().data() << endl;
```

2. null字符串和empty字符串的区别
null字符串是初始化之后还未赋值的字符串，empty字符串是长度为0的空字符串  
null一定是empty，empty不一定是null  
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

3. QString中元素的类型为class QCharRef
```
cout << typeid(str[1]).name() << endl; //输出：class QCharRef
```

4. 取出数字字符串中的某一位进行计算
注意：不能使用'str[3]'这样的方式去取出某一位，因为这样获得的是QCharRef对象，没办法转换成数字  
先用at()方法获取一个QChar对象，再用QChar对象的digitValue()方法转换为数字  
```
QString str = "1234567";
int a = 10 + str.at(3).digitValue();
cout << a << endl;
```


## 构造函数
1. QString::QString(const QByteArray &ba)

2. QString::QString(const char \*str)

3. QString::QString(QString &&other)

4. QString::QString(QLatin1String str)
```
QString str1(QLatin1String("myname"));
```

5. QString::QString(int size, QChar ch)
字符串中的每个字符都设置为ch，长度为size  

6. QString::QString(QChar ch)
字符串的长度设置为1，字符为ch  

7. QString::QString()
构造一个null字符串，同时也是empty的  


## 数据类型转换相关的常用公共函数
1. int toInt(bool \*ok = nullptr, int base = 10)
将字符串转换为10进制整型并返回一个整型数字，当转换失败时返回0  
ok参数用来指示是否转换成功，当失败时ok为false，当成功时ok为true  
base参数用来设置数字进制，范围在2到36之间，默认为10进制  
备注：8/16进制数字符串如果开头带有'0'/'0x'，可以直接进行转换，不用特意去掉  
```
bool ok;
QString str = "123";
int num = str.toInt(&ok);
```
注意：base参数是用来标识本字符串中数字的进制，而不是要返回的类型，返回的统一都是10进制整数  
```
bool ok;
QString str = "2df3";//16进制数的字符串
int num = str.toInt(&ok, 16);//输出：11763
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

5. QByteArray QString::toAscii() const
和toLatin1()方法的功能相同，已经过时了，不再使用  

6. float QString::toFloat(bool \*ok = nullptr) const
把字符串转换为单精度浮点数，如果转换失败，则返回0.0  

7. double QString::toDouble(bool \*ok = nullptr) const
把字符串转换为双精度浮点数，如果转换失败，则返回0.0  


## 进行了重载的常用公共函数
1. 重载函数append()
在string后面添加字符串str  
注意：添加后会改变原有字符串的内容  
```
QString &QString::append(const QString &str)
QString &QString::append(QChar ch)
QString &QString::append(const QChar *str, int len)
QString &QString::append(const QStringRef &reference)
QString &QString::append(QLatin1String str)
QString &QString::append(const char *str)
QString &QString::append(const QByteArray &ba)
```

2. 重载函数prepend()
在string前面添加字符串str  
```
QString &QString::prepend(const QString &str)
QString &QString::prepend(QChar ch)
QString &QString::prepend(const QChar *str, int len)
QString &QString::prepend(const QStringRef &str)
QString &QString::prepend(QLatin1String str)
QString &QString::prepend(const char *str)
QString &QString::prepend(const QByteArray &ba)
```

3. 重载函数arg()
```
QString QString::arg(const QString &a, int fieldWidth = 0, QChar fillChar = QLatin1Char(' ')) const
QString QString::arg(qlonglong a, int fieldWidth = 0, int base = 10, QChar fillChar = QLatin1Char(' ')) const
QString QString::arg(qulonglong a, int fieldWidth = 0, int base = 10, QChar fillChar = QLatin1Char(' ')) const
...
(数量太多，不再列举)
```
向QString字符串中插入变量，变量也可以是数字等类型，不必转换为字符串  
相当于C++提供的%d、%s、%c等通配符  
注意：这里的字符串中不再是通配符，而是从1开始计数的数字，与后面的参数一一对应  
```
sql_command = QString("insert into user_info values('%1', '%2', '%3', '%4');").arg(user_id).arg(user_name).arg(card_id).arg(user_remark);
```

4. 重载函数contains()
判断string中是否包含str字符串，返回true或false  
```
bool QString::contains(const QString &str, Qt::CaseSensitivity cs = Qt::CaseSensitive)
bool QString::contains(QChar ch, Qt::CaseSensitivity cs = Qt::CaseSensitive) const
bool QString::contains(const QStringRef &str, Qt::CaseSensitivity cs = Qt::CaseSensitive) const
bool QString::contains(QLatin1String str, Qt::CaseSensitivity cs = Qt::CaseSensitive) const
bool QString::contains(QStringView str, Qt::CaseSensitivity cs = Qt::CaseSensitive) const
bool QString::contains(const QRegExp &rx) const
bool QString::contains(QRegExp &rx) const
bool QString::contains(const QRegularExpression &re) const
bool QString::contains(const QRegularExpression &re, QRegularExpressionMatch *rmatch) const
```

5. 重载函数count()
判断string中包含str字符串的个数  
```
int QString::count(const QString &str, Qt::CaseSensitivity cs = Qt::CaseSensitive) const
int QString::count() const //相当于size()
int QString::count(QChar ch, Qt::CaseSensitivity cs = Qt::CaseSensitive) const
int QString::count(const QStringRef &str, Qt::CaseSensitivity cs = Qt::CaseSensitive) const
int QString::count(const QRegExp &rx) const
int QString::count(const QRegularExpression &re) const
```

6. 重载函数compare()
比较两个字符串，字符串按照ASCII码值的大小进行比较  
返回一个大于/小于/等于0的int类型，分别代表s1大于/小于/等于s2  
```
int QString::compare(const QString &other, Qt::CaseSensitivity cs = Qt::CaseSensitive) const
int QString::compare(const QStringRef &ref, Qt::CaseSensitivity cs = Qt::CaseSensitive) const
int QString::compare(QLatin1String other, Qt::CaseSensitivity cs = Qt::CaseSensitive) const
int QString::compare(QStringView s, Qt::CaseSensitivity cs = Qt::CaseSensitive) const
int QString::compare(QChar ch, Qt::CaseSensitivity cs = Qt::CaseSensitive) const
```

7. 重载函数remove()
从string中删除str，功能类似于replace(str, "", cs)  
```
QString &QString::remove(const QString &str, Qt::CaseSensitivity cs = Qt::CaseSensitive)
QString &QString::remove(QChar ch, Qt::CaseSensitivity cs = Qt::CaseSensitive)
QString &QString::remove(QLatin1String str, Qt::CaseSensitivity cs = Qt::CaseSensitive)
QString &QString::remove(const QRegExp &rx)
QString &QString::remove(const QRegularExpression &re)
```
示例  
```
QString t = "Ali Baba";
t.remove(QChar('a'), Qt::CaseInsensitive);
cout << t.data() <<endl; //输出"li Bb"
```

8. 重载函数replace()
从position位置开始的n个字符都替换成字符串after  
把字符/字符串before都替换成字符/字符串after  
```
QString &QString::replace(int position, int n, const QString &after)
QString &QString::replace(int position, int n, QChar after)
QString &QString::replace(int position, int n, const QChar *unicode, int size)
QString &QString::replace(QChar before, QChar after, Qt::CaseSensitivity cs = Qt::CaseSensitive)
QString &QString::replace(const QChar *before, int blen, const QChar *after, int alen, Qt::CaseSensitivity cs = Qt::CaseSensitive)
QString &QString::replace(QLatin1String before, QLatin1String after, Qt::CaseSensitivity cs = Qt::CaseSensitive)
QString &QString::replace(QLatin1String before, const QString &after, Qt::CaseSensitivity cs = Qt::CaseSensitive)
QString &QString::replace(const QString &before, QLatin1String after, Qt::CaseSensitivity cs = Qt::CaseSensitive)
QString &QString::replace(const QString &before, const QString &after, Qt::CaseSensitivity cs = Qt::CaseSensitive)
QString &QString::replace(QChar ch, const QString &after, Qt::CaseSensitivity cs = Qt::CaseSensitive)
QString &QString::replace(QChar c, QLatin1String after, Qt::CaseSensitivity cs = Qt::CaseSensitive)
QString &QString::replace(const QRegExp &rx, const QString &after)
QString &QString::replace(const QRegularExpression &re, const QString &after)
```
示例：  
```
QString str1 = "123456789";
QString str2 = "abcd";
str1.replace(2, 2, str2);
qDebug() << str1; //输出"12abcd56789"
```

9. 重载函数setNum()
把数字转换为字符串，如果字符串中原来有内容，会被抹去  
```
QString &QString::setNum(int n, int base = 10)
QString &QString::setNum(short n, int base = 10)
QString &QString::setNum(float n, char format = 'g', int precision = 6)
QString &QString::setNum(double n, char format = 'g', int precision = 6)
...
```
示例：  
```
QString str2 = "abcd";
str2.setNum(1234);
qDebug() << str2; //输出"1234"，原来的"abcd"被抹去
```

10. 重载函数split()
字符串按照指定分割符分割为多个字符串，并返回一个QStringList  
如果分割符在原始字符串中不匹配，则返回的列表中只包含一个原始字符串  
如果分割符为空字符串，则返回列表的元素为原始字符串的每个字符和前后各一个空字符串  
例如："abcd"用""分割出的列表为["","a","b","c","d",""]  
例如："/a/b/c/"用'/'分割出的列表为["", "a", "b", "c", ""]  
```
QStringList QString::split(const QString &sep, Qt::SplitBehavior behavior = Qt::KeepEmptyParts, Qt::CaseSensitivity cs = Qt::CaseSensitive)  
QStringList QString::split(QChar sep, Qt::SplitBehavior behavior = Qt::KeepEmptyParts, Qt::CaseSensitivity cs = Qt::CaseSensitive) const
...
```
示例：  
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
1. QString QString::mid(int position, int n = -1) const
从字符串的position位置开始，截取n个字符并返回  
如果position超出了合法索引范围，则返回一个空字符串  
如果从position开始，剩余的字符少于n个，则把剩余所有的字符都返回  
如果n为默认值-1，则把从position开始的所有字符都返回  

2. QStringRef QString::midRef(int position, int n = -1) const
和上面函数类似，但返回的是QStringRef对象

3. QString QString::toUpper()
str2变大写  

4. QString QString::toLower()
str1变小写  

5. int QString::size()
返回字符串中字符个数，其中一个汉字算一个字符  

6. int QString::count()
返回字符串中字符个数，其中一个汉字算一个字符  

7. int QString::length()
返回字符串中字符个数，其中一个汉字算一个字符  

8. QString QString::trimmed()
去掉字符串首尾的空格  

9. QString QString::simplified()
去掉字符串首尾的空格，且当中间有多个连续空格时也用一个空格替换  

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
20. void QString::clear()
清空字符串，str会变成NULL
```
QString str = "abc";
str.clear();
qDebug() << str; \\输出：""
qDebug() << str.isNull(); \\输出：true
qDebug() << str.isEmpty(); \\输出：true
```

## 静态公共函数
1. 重载函数compare()
```
[static] int QString::compare(const QString &s1, const QString &s2, Qt::CaseSensitivity cs = Qt::CaseSensitive)
[static] int QString::compare(const QString &s1, QLatin1String s2, Qt::CaseSensitivity cs = Qt::CaseSensitive)
[static] int QString::compare(QLatin1String s1, const QString &s2, Qt::CaseSensitivity cs = Qt::CaseSensitive)
[static] int QString::compare(const QString &s1, const QStringRef &s2, Qt::CaseSensitivity cs = Qt::CaseSensitive)
```
比较s1和s2两个字符串，字符串按照ASCII码值的大小进行比较  
返回一个大于/小于/等于0的int类型，分别代表s1大于/小于/等于s2  
cs参数默认为大小写敏感  
```
int x = QString::compare("aUtO", "AuTo", Qt::CaseInsensitive);  // x == 0
int y = QString::compare("auto", "Car", Qt::CaseSensitive);     // y > 0
int z = QString::compare("auto", "Car", Qt::CaseInsensitive);   // z < 0
```

2. 重载函数number()
```
[static] QString QString::number(int n, int base = 10)
[static] QString QString::number(long n, int base = 10)
[static] QString QString::number(uint n, int base = 10)
[static] QString QString::number(ulong n, int base = 10)
[static] QString QString::number(qlonglong n, int base = 10)
[static] QString QString::number(qulonglong n, int base = 10)
[static] QString QString::number(double n, char format = 'g', int precision = 6)
```
把数字转换为字符串并返回一个QString字符串  
base参数用来设置数字进制，范围在2到36之间，默认为10进制  
注意：只能用QString::number(num)格式，不能用str.number(num)格式  
```
int num = 100;
QString str = QString::number(num);
```

3. 重载函数fromLatin1()
```
[static] QString QString::fromLatin1(const QByteArray &str)
[static] QString QString::fromLatin1(const char *str, int size = -1)
```
把QByteArray转换为QString  