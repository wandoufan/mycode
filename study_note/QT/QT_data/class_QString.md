# QString

## 基本功能
QString类提供了一个编码的字符串，存储了若干个QChar类型的16位字符  
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

## QString常用函数
注意：有的函数直接修改原字符串，没有返回值；有的函数不改动原字符串，会把结果当做一个返回值  
1. &QString append()
在str1后面添加字符串str2  
```
str1.append(str2); 
```
2. &QString prepend()
在str1前面添加字符串str2  
```
str1.prepend(str2);
```
3. QString toUpper()
str2变大写  
```
str3 = str2.toUpper();
```
4. QString toLower()
str1变小写  
```
str3 = str1.toLower();
```
5. int size()
返回字符串中字符个数，其中一个汉字算一个字符  
```
num = str1.size();
```
6. int count()
返回字符串中字符个数，其中一个汉字算一个字符  
```
num = str1.count();
```
7. int length()
返回字符串中字符个数，其中一个汉字算一个字符  
```
num = str1.length(); 
```
8. QString trimmed()
去掉字符串首尾的空格  
```
str3 = str1.trimmed();
```
9. QString simplified()
去掉字符串首尾的空格，且当中间有多个连续空格时也用一个空格替换  
```
str3 = str1.simplified();
```
10. int indexOf(const QString &str, int from = 0 , Qt::CaseSensitivity cs = Qt::CaseSensitive)
查找str2在str1中首次出现的位置，如果没有找到str2则返回-1  
from参数设置开始查找的位置，默认为0；当from为-1时，从最后一次字符开始，以此类推  
cs参数用来指定查找时是否对大小写敏感，默认区分大小写，Qt::CaseInsensitive时不区分  
```
num = str1.indexOf(str2); 
```
11. int lastIndexOf(const QString &str, int from = -1, Qt::CaseSensitivity cs = Qt::CaseSensitive)
查找str2在str1中最后出现的位置，如果没有找到str2则返回-1  
from参数默认为-1；当from为-2时，从倒数第二个字符开始，以此类推  
cs参数用来指定查找时是否对大小写敏感，默认区分大小写，Qt::CaseInsensitive时不区分  
```
num = str1.lastIndexOf(str2);
```
12. bool contains(const QString &str, Qt::CaseSensitivity cs = Qt::CaseSensitive)
判断str1中是否包含str2字符串，返回true或false  
```
result = str1.contains("abc");
```
13. bool startsWith(const QString &s, Qt::CaseSensitivity cs = Qt::CaseSensitive)
判断str1是否以str2开头，返回true或false  
```
result = str1.startsWith(str2);
```
14. bool endsWith(const QString &s, Qt::CaseSensitivity cs = Qt::CaseSensitive)
判断str1是否以str2结尾，返回true或false  
```
result = str1.endsWith(str2);
```
15. QString left(int n)
从str1左边取n个字符  
```
str3 = str1.left(n);
```
16. QString right(int n)
从str1右边取n个字符  
```
str3 = str1.right(n);
```
17. QString section (const QString &sep, int start, int end = -1, SectionFlags flags = SectionDefault)
以逗号为分隔符将str1分割，然后提取出start到end的部分  
```
str3 = str1.section(',', 2, 3);
```
18. QChar at(int position)
获取字符串中指定位置的字符  
```
char1 = str1.at(n);
```
19. void resize(int size, QChar fillChar)
调整字符串str1的长度为n  
当n小于字符串的当前长度时，会把字符串截断，只保留前n个字符  
当n大于字符串的当前长度时，会将字符串填充到长度n，填充字符可以写到第二个参数里  
```
str1.resize(n);
```
20. QString arg(const QString &a, int fieldWidth = 0, QChar fillChar = QLatin1Char(' ')) const
向QString字符串中插入相应的QString类型的变量  
相当于C++提供的%d、%s、%c等通配符  
注意：这里的字符串中不再是通配符，而是从1开始计数的数字，与后面的参数一一对应  
```
sql_command = QString("insert into user_info values('%1', '%2', '%3', '%4');").arg(user_id).arg(user_name).arg(card_id).arg(user_remark);
```