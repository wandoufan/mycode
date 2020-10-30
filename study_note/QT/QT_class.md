# QT中的类


----------------------------/*QT数据类型转换*/-------------------------------

## 数据类型转换
注意：在QT中str不是关键字，也不是系统函数，不能直接用str对数据进行格式转换  
备注：函数中有base参数的可以在类型转换的同时实现进制的转换  
1. QString转int
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
2. int转QString
2.1 QString number(long n, int base = 10)  
把整型转换为字符串并返回一个QString字符串  
base参数用来设置数字进制，范围在2到36之间，默认为10进制  
注意：只能用QString::number(num)格式，不能用str.number(num)格式  
```
int num = 100;
QString str = QString::number(num);
```
2.2 &QString setNum(int n, int base = 10)  
直接把整型数字写入一个QString字符串中，没有返回值  
注意：number()和setNum()的不同  
```
QString str;
str.setNum(1234, 2); //将整数1234转为2进制后再转为字符串
```
3. QString转QChar
注意：QString类型的字符串不能直接用cout输出，否则报错，必须先转换为QChar格式  
3.1 QByteArray toLatin1()  
返回一个QByteArray格式的Latin-1字符串表达式  
适合于普通的英文字符串，但不能包含中文，否则会产生乱码  
```
Qstring  str;
char*  ch;
QByteArray ba = str.toLatin1();
ch=ba.data();  //不能直接用cout输出QByteArray对象，而是要输出对象的data()方法
```
3.2 QByteArray toUtf8()  
返回一个QByteArray格式的UTF8字符串表达式  
UTF8格式支持中文字符  
```
Qstring  str;
char*  ch;
QByteArray ba = str.toUtf8();
ch=ba.data();  //不能直接用cout输出QByteArray对象，而是要输出对象的data()方法
```
4. QChar转QString
5. QStringList转换为QString
QString join(QString &separator)
将字符串列表中的元素拼接起来，返回一个QString
注意：join函数的连接字符串必须要有，可以是空字符串，但不能不写参数
```
QStringList alist;
alist << "a" << "b" << "c" << "d";
QString str1;
str1 = alist.join("+"); //写成str1 = alist.join();会报错，join函数必须要有参数
```
6. QString转QStringList
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
7. QVariant转QString
```
QVariant qv;
QString qs = qv.toString();
```
8. QString 转 QVariant
```
QString qs;
QVariant qv(qs);
```

----------------------------/*QT常用类*/-------------------------------

## QObject
QObject类是所有QT对象的基类  


## QAbstractButton
QAbstractButton类是所有widgets按钮的抽象基类，给按钮提供公用的函数功能  
QAbstractButton是QWidget类的子类  
QAbstractButton是QCheckBox, QPushButton, QRadioButton, QToolButton的父类  
1. isDown()
表示按钮button是否是pressed down按下的  
2. isChecked()
表示按钮是否被检查或者标记切换的  
只有可检查和切换（标记）的按钮可以标记或者取消标记checked or unchecked  
3. isEnabled()
表示按钮是否可以被用户点按  
4. setAutoRepeat()
设置按钮是否当用户长按按钮可以auto-repeat（自动重复执行）  
属性autoRepeatDelay和autoRepeatInterval定义了如何重复响应执行  
5. setCheckable()
设置按钮是否可切换或者标记的  


## QString
QString类提供了一个编码的字符串，存储了若干个QChar类型的16位字符  
1. 初始化一个QString类型的字符串
```
QString str1 = "HELLO";
```
注意：QString类型的字符串不能直接用cout输出，否则报错，必须先转换为QChar格式  
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
**QString常用函数**
注意：有的函数直接修改原字符串，没有返回值；有的函数不改动原字符串，会把结果当做一个返回值  
1. &QString append()
str1.append(str2); 在str1后面添加字符串str2  
2. &QString prepend()
str1.prepend(str2); 在str1前面添加字符串str2  
3. QString toUpper()
str3 = str2.toUpper(); str2变大写  
4. QString toLower()
str3 = str1.toLower(); str1变小写  
5. int size()
num = str1.size(); 返回字符串中字符个数，其中一个汉字算一个字符  
6. int count()
num = str1.count(); 返回字符串中字符个数，其中一个汉字算一个字符  
7. int length()
num = str1.length(); 返回字符串中字符个数，其中一个汉字算一个字符  
8. QString trimmed()
str3 = str1.trimmed(); 去掉字符串首尾的空格  
9. QString simplified()
str3 = str1.simplified(); 去掉字符串首尾的空格，且当中间有多个连续空格时也用一个空格替换  
10. int indexOf(const QString &str, int from = 0 , Qt::CaseSensitivity cs = Qt::CaseSensitive)
num = str1.indexOf(str2); 查找str2在str1中首次出现的位置，如果没有找到str2则返回-1  
from参数设置开始查找的位置，默认为0；当from为-1时，从最后一次字符开始，以此类推  
cs参数用来指定查找时是否对大小写敏感，默认区分大小写，Qt::CaseInsensitive时不区分  
11. int lastIndexOf(const QString &str, int from = -1, Qt::CaseSensitivity cs = Qt::CaseSensitive)
num = str1.lastIndexOf(str2); 查找str2在str1中最后出现的位置，如果没有找到str2则返回-1  
from参数默认为-1；当from为-2时，从倒数第二个字符开始，以此类推  
cs参数用来指定查找时是否对大小写敏感，默认区分大小写，Qt::CaseInsensitive时不区分  
12. bool contains(const QString &str, Qt::CaseSensitivity cs = Qt::CaseSensitive)
result = str1.contains("abc"); 判断str1中是否包含str2字符串，返回true或false  
13. bool startsWith(const QString &s, Qt::CaseSensitivity cs = Qt::CaseSensitive)
result = str1.startsWith(str2); 判断str1是否以str2开头，返回true或false  
14. bool endsWith(const QString &s, Qt::CaseSensitivity cs = Qt::CaseSensitive)
result = str1.endsWith(str2); 判断str1是否以str2结尾，返回true或false  
15. QString left(int n)
str3 = str1.left(n); 从str1左边取n个字符  
16. QString right(int n)
str3 = str1.right(n); 从str1右边取n个字符  
17. QString section (const QString &sep, int start, int end = -1, SectionFlags flags = SectionDefault)
str3 = str1.section(',', 2, 3); 以逗号为分隔符将str1分割，然后提取出start到end的部分  
18. QChar at(int position)
char1 = str1.at(n); 获取字符串中指定位置的字符  
19. void resize(int size, QChar fillChar)
str1.resize(n); 调整字符串str1的长度为n  
当n小于字符串的当前长度时，会把字符串截断，只保留前n个字符  
当n大于字符串的当前长度时，会将字符串填充到长度n，填充字符可以写到第二个参数里  


## QChar
QChar类提供了一个16位编码的字符  
QChar是16位的，因此可以用来存储汉字，一个字符存储一个汉字  


## QVariant
QVariant类提供了QT的通用数据类型的封装容器，支持几乎所有QT数据类型，有点类似json  
支持的类型包括int、float、char、json、bool、bytearray、list、hash、string...
如果有几种不同类型的数据需要传递，QVariant常用来替代结构体struct  
导出QVariant的数据类型和导入QVariant的数据类型是一致的  


## QDatetime
QDatetime类提供日期和时间相关的函数  
另外，还有QDate类和QTime类  
**常用函数**
1. QDateTime currentDateTime() 
获取当前时间日期，返回一个QDateTime对象  
```
QDateTime current_datetime = QDateTime::currentDateTime();
ui -> timeEdit -> setTime(current_datetime.time());
```
2. QString toString(const QString &format) 
按照一定格式转化成字符串，返回字符串对象  
```
QDateTime current_datetime = QDateTime::currentDateTime();
ui -> Edit_time -> setText(current_datetime.toString("hh:mm:ss"));
```
3. QDateTime fromString(const QString &string, Qt::DateFormat format = Qt::TextDate)
把时间日期的字符串按照一定格式转化为一个QDateTime对象  
```
QDateTime user_time = QDateTime::fromString(str, "hh:mm:ss");
ui -> timeEdit -> setTime(user_time.time());
```


## QTimer
QTimer类提供了计时器和定时器的功能  
注意：QTimer并不是一个可见的组件，在UI设计器里找不到它  
> http://c.biancheng.net/view/1848.html


## QFont
QFont类是专门用于管理文本的字体  
```
QFont font = ui -> textEdit -> font();
font.setUnderline(checked);
ui -> textEdit -> setFont(font);
```
**QFont常用函数**
setFamily() 设置字体  
setBold() 字体加粗  
setItalic() 斜体  
setOverline() 上划线  
setUnderline() 下划线  
setStrikeOut() 删除线  
setPointSize() 设置字体肉眼看到的实际大小，在不同设备上显示大小相同  
setPixelSize() 设置字体像素单位的大小，在不同设备上显示大小可能不同  


## QPalette
Qpalette(调色板)类是专门用于管理组件的外观颜色，每个组件都有一个palette对象  
```
QPalette plet = ui -> plainTextEdit -> palette();
plet.setColor(QPalette::Text, Qt::blue);
ui -> plainTextEdit -> setPalette(plet);
```
1. 设置颜色显示区域的参数包括：  
QPalette::Base 设置文本输入窗口部件(如QtextEdit等)的底色  
QPalette::Text 设置文本输入窗口中文字的颜色  
QPalette:WindowText 通常指窗口看不见的前景色  
QPalette::Button 指按钮窗口部件的背景色  
QPalette::ButtonText 指按钮窗口部件的前景色  
QPalette::Background 背景色  
QPalette::Foreground 前景色  
2. 常用设置颜色的参数包括：  
Qt::black 黑色  
Qt::blue 蓝色  
Qt::red 红色  
Qt::yellow 黄色  
QColor(10, 100 , 50, 255) 用数字设置颜色  


## QColor
QColor类用来生成基于RGB、HSV、CMYK值的各种颜色  
一般产生的都是各种颜色对象，然后被其他函数调用作为颜色参数  
```
直接初始化一个QColor对象
QColor(10, 100 , 50, 255)
```
**QColor常用函数**
1. void QColor::setRgb(int r, int g, int b, int a = 255)
setRgb函数用来设置颜色对象的RGB值  
r参数用来设置红色，范围0到255之间  
g参数用来设置绿色，范围0到255之间  
b参数用来设置蓝色，范围0到255之间  
a参数用来设置alpha值，即颜色的透明度，默认为255  
```
QColor mycolor;
mycolor.setRgb(10, 100 , 50); 每个参数的含义，参数范围为0~255
```


## QMessageBox
QMessageBox类可以弹出一个对话框来通知用户或询问用户并获得回答  
QMessageBox类是QDialog类的子类  
注意：使用QMessageBox类时必须在开头声明头文件'#include <QMessageBox>'  
**QMessageBox常用函数**
1. QMessageBox::StandardButton QMessageBox::information(QWidget \*parent, const QString &title, const QString &text, QMessageBox::StandardButtons buttons = Ok, QMessageBox::StandardButton defaultButton = NoButton)
information函数用来显示通知信息，对话框为一个感叹号  
函数会在widget父类前面弹出一个对话框，并显示指定的标题和文本内容  
当用户按下'enter'时会触发一个默认按钮，默认按钮用第五个参数进行设置  
当用户按下'esc'时会退出对话框，相当于调用了'escape button'  
备注：如果QMessageBox的在函数参数中指定了父类，则在对话框运行时不能删除其父类  
第一个参数设置父控件指针，可以设为NULL  
第二个参数设置对话框标题  
第三个参数设置对话框内容  
第四个参数设置窗口中的按钮个数及形式(默认为OK)  
第五个参数设置用户按下'enter'时的触发按钮，默认'NoButton'由QMessageBox自动选择  
```
QMessageBox::information(NULL, "title", "content", QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
```
2. QMessageBox::StandardButton QMessageBox::critical(QWidget \*parent, const QString &title, const QString &text, QMessageBox::StandardButtons buttons = Ok, QMessageBox::StandardButton defaultButton = NoButton)
critical函数用来显示比较严重的警告信息，对话框为一个叉号  
3. QMessageBox::StandardButton QMessageBox::question(QWidget \*parent, const QString &title, const QString &text, QMessageBox::StandardButtons buttons = StandardButtons(Yes | No), QMessageBox::StandardButton defaultButton = NoButton)
question函数用来向用户询问问题并让用户进行选择，对话框为一个问号  
4. void QMessageBox::about(QWidget \*parent, const QString &title, const QString &text)
about函数用来弹出一个简单的对话框，对话框中没有标识符  
```
QMessageBox::about(NULL, "about", "this is about");
```


## QDebug
QDebug类提供了可以产生debugging信息的输出流，常用来输出调试信息  
注意：使用QtDebug类时必须在开头声明头文件'#include <QDebug>'  
**QtDebug常用函数**
1. qDebug()
qDebug是最常用的函数，可以代替cout输出一个或多个参数信息  
qDebug函数可以直接使用，不必声明所属的类，也不必通过对象引用  
```
qDebug() << "the result is " << str1;
```


----------------------------/*QT容器类*/-------------------------------


## QT容器类
1. 基本概念
QT提供了多个基于模板的容器类，这些容器类可以用于存储指定类型的数据项  
QT的容器类包括顺序容器类和关联容器类  
2. 容器类的特点
QT的容器类比标准模板库(STL)中的容器类更轻巧、安全和易于使用  
这些容器类是隐式共享和可重入的，而且它们进行了速度和存储优化，因此可以减少可执行文件的大小  
这些容器类还是线程安全的，也就是说它们作为只读容器时可被多个线程访问  
3. 容器类的数据项
例如在QList<T>中，数据项T是一个具体的数据类型，且必须是一个可赋值的类型  
数据项T可以是int或float等简单类型，也可以是QString或QDate等类  
数据项T不能是QObject类或QObject的任何子类  
4. 示例：用QList定义一个字符串类型的列表容器
```
QList<QString> aList;
aList.append("Monday");
aList.append("Tuesday");
aList.append("Wednesday");
QString str=aList[0];
```
5. QT顺序容器类
5.1 QList  
5.2 QLinkedList  
5.3 QVector  
5.4 QStack  
5.5 QQueue  
6. QT关联容器类
6.1 QMap  
6.2 QMultiMap  
6.3 QHash  
6.4 QMultiHash  
6.5 QSet  


## QList
QList是最常用的容器类，相当于数组或列表，支持序列化访问，且访问修改数据的速度很快  
备注：QList中可以使用[]操作符去访问元素，而C++中的list不可以使用[]操作符  
备注：QList<QString>也可以写为QStringList，以下两个定义相同  
```
QList<QString> aList;
QStringList alist;
```
**QList常用函数**
1. insert()
2. void removeAt(int i)
删除指定索引位置i的元素，注意函数没有返回值
3. replace()
4. move()
5. swap()
6. append()
7. prepend()
8. removeFirst()
9. removeLast()
9. int removeAll(item & value)
删除列表中指定的元素  
10. isEmpty()
在数据项为空时返回true  
11. size()
返回列表中数据项的个数  
12. void clear()
清除列表中的所有元素  
13. 


## QLinkedList
QLinkedList是链式列表，用链表结构存储数据项，是使用不连续的内存实现存储的  
基于迭代器访问数据项，不支持序列化访问，访问修改数据的速度相对较慢  
QLinkedList的接口函数与QList基本相同  


## QVector
QVector提供动态数组的功能，支持序列化访问  
QVector的性能比QList更高，因为QVector的数据项是连续存储的  
QVector的接口函数与QList基本相同  


## QStack
QStack是实现先进后出的容器类，相当于堆栈  
1. push()
2. pop()


## QQueue
QQueue是实现先进先出的容器类，相当于队列  
1. enqueue()
2. dequeue()


## QSet
QSet<T>是实现散列表集合的容器类，相当于集合  
QSet按照无序方式存储数据，查找值的速度非常快  
QSet内部就是用QHash实现的，只是hash函数已经定义好了  
示例：  
```
QSet<QString> set;
set << "dog" << "cat" << "tiger";
```
1. contains()
判断元素是否是集合成员，返回一个布尔值  
set.contains("cat")  


## QMap
QMap<Key, T>是实现Key-value数据的容器类，相当于字典  
QMap是按照key的顺序进行存储数据的，查找速度相对QHash会更慢  
除非使用QMap::insertMulti()添加键值对，否则QMap正常情况下不允许多值映射  
示例：  
```
QMap<QString, int> map;
map["one"] = 1;
map["two"] = 2;
map["three "] = 3;
```
1. insert(key, value)
向map中加入一组键值对或者对已有的键修改对应的值  
map.insert("four", 4);  
2. remove(key)
删除一组键值对  
map.remove("two");  
4. value(key, default)
返回指定键对应的值，相当于[key]，当对应的值不存在时返回default  
int num1 = map["one"];  
int num2 = map.value("two");  
int code = map.value("ten", 10);  
使用value函数没有找到键对应的值时，如果不指定default，则会返回一个缺省的返回值  
例如，要查找的值是字符串类型时，默认会返回一个空的字符串  


## QMultiMap
QMultiMap是QMap的子类，可以用来处理多值映射，即一个key可以对应多个value  
注意：QMultiMap不提供'[]'操作符  
QMultiMap中的大多数函数与QMap一致，但有少部分函数与QMap定义不一致  
示例：  
```
QMultiMap<QString, int> map1, map2, map3;
map1.insert("plenty", 100);
mapl.insert("plenty", 2000); // map1.size() == 2
map2.insert("plenty", 5000); // map2.size() == 1
map3 = map1 + map2; // map3.size() == 3
```
1. insert()
QMultiMap::insert()等于QMap::insertMulti()  
2. replace()
QMultiMap::replace()等于QMap::insert()  
3. value(key)
返回key对应的所有value中最新插入的那个value值  
4. values(key)
返回key对应的所有value，返回值是QList<T>类型  
QList<int> values = map.values("plenty");  


## QHash
QHash<Key，T>是基于散列表来实现字典功能的容器类  
QHash是按照无序方式存储数据的，查找速度相对QMap会快很多  
使用QHash需要自定义一个名为qHash()的全局散列函数  
QMap的键必须提供'<'运算符，而QHash的键必须提供'=='运算符  


## QMultiHash
QMultiHash是QHash的子类，可以用来处理多值映射，类似于QMultiMap  

---------------------------------------------------------------------