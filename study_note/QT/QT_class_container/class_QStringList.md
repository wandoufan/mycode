# QStringList

## 基本功能
QStringList是一个字符串列表，经常作为一些Qt类的方法的返回值类型  
QStringList继承自QList，因此可以使用QList中的众多方法  
父类：QList  
子类：无  


## 代码示例
1. 以下两个定义相同：  
```
QList<QString> aList;
QStringList alist;
```
2. 初始字符串列表
```
QStringList fonts = { "Arial", "Helvetica", "Times" };
alist << "a" << "123" << "abc";
```


## 构造函数
1. template <typename InputIterator> QStringList::QStringList(InputIterator first, InputIterator last)

2. QStringList::QStringList(std::initializer_list<QString> args)

3. QStringList::QStringList(QList<QString> &&other)

4. QStringList::QStringList(const QList<QString> &other)

5. QStringList::QStringList(const QString &str)

6. QStringList::QStringList()


## 常用公共函数：排序
1. void QStringList::sort(Qt::CaseSensitivity cs = Qt::CaseSensitive)
按字典排序，默认大小写敏感  


## 常用公共函数：拼接字符串
1. QString QStringList::join(const QString &separator) const
将字符串列表中的元素拼接起来，返回一个QString  
注意：join函数的连接字符串必须要有，可以是空字符串，但不能不写参数  
```
QStringList alist;
alist << "a" << "b" << "c" << "d";
QString str1;
str1 = alist.join("+"); //写成str1 = alist.join();会报错，join函数必须要有参数
```

2. QString QStringList::join(QStringView separator) const
重载函数

3. QString QStringList::join(QLatin1String separator) const
重载函数

4. QString QStringList::join(QChar separator) const
重载函数


## 常用公共函数：获取列表中的信息
1. bool QStringList::contains(const QString &str, Qt::CaseSensitivity cs = Qt::CaseSensitive) const
判断字符串列表中是否包含指定字符串，默认为大小写敏感  

2. bool QStringList::contains(QLatin1String str, Qt::CaseSensitivity cs = Qt::CaseSensitive) const
重载函数

3. bool QStringList::contains(QStringView str, Qt::CaseSensitivity cs = Qt::CaseSensitive) const
重载函数

4. int QStringList::indexOf(const QRegExp &rx, int from = 0) const
从from位置开始向下检索，返回匹配到的第一个字符串的索引位置  
如果没有匹配到任何一个，则返回-1  

5. int QStringList::indexOf(QStringView str, int from = 0) const
重载函数

6. int QStringList::indexOf(QLatin1String str, int from = 0) const
重载函数

7. int QStringList::indexOf(QRegExp &rx, int from = 0) const
重载函数

8. int QStringList::indexOf(const QRegularExpression &re, int from = 0) const
重载函数

9. int QStringList::lastIndexOf(const QRegExp &rx, int from = -1) const
从from位置开始向前检索，返回匹配到最后一个字符串的索引位置  
如果没有匹配到任何一个，则返回-1  

10. int QStringList::lastIndexOf(QStringView str, int from = -1) const

11. int QStringList::lastIndexOf(QLatin1String str, int from = -1) const

12. int QStringList::lastIndexOf(QRegExp &rx, int from = -1) const

13. int QStringList::lastIndexOf(const QRegularExpression &re, int from = -1) const


## 常用公共函数：获取子列表
1. QStringList QStringList::filter(const QString &str, Qt::CaseSensitivity cs = Qt::CaseSensitive) const
返回一个子列表，该子列表中的每个字符串都包含子串str，默认为大小写敏感  
```
QStringList list;
list << "Bill Murray" << "John Doe" << "Bill Clinton";

QStringList result;
result = list.filter("Bill");
// result: ["Bill Murray", "Bill Clinton"]
```
以上代码效果等同于以下代码  
```
QStringList result;
foreach (const QString &str, list)
{
	if (str.contains("Bill"))
		result += str;
}
```

2. QStringList QStringList::filter(QStringView str, Qt::CaseSensitivity cs = Qt::CaseSensitive) const

3. QStringList QStringList::filter(const QRegExp &rx) const

4. QStringList QStringList::filter(const QRegularExpression &re) const


## 常用公共函数：替换字符串
1. QStringList &QStringList::replaceInStrings(const QString &before, const QString &after, Qt::CaseSensitivity cs = Qt::CaseSensitive)
检查字符串列表中的每个元素中是否包含before子串，如果包含，就替换成after子串  
注意：是替换每个字符串中的一部分，不是整体替换  
```
 QStringList list;
 list << "alpha" << "beta" << "gamma" << "epsilon";
 list.replaceInStrings("a", "o");
 // list == ["olpho", "beto", "gommo", "epsilon"]
```

2. QStringList &QStringList::replaceInStrings(QStringView before, QStringView after, Qt::CaseSensitivity cs = Qt::CaseSensitive)

3. QStringList &QStringList::replaceInStrings(const QRegExp &rx, const QString &after)

4. QStringList &QStringList::replaceInStrings(const QRegularExpression &re, const QString &after)
