# QT中的类

----------------------------/*QT常用类*/-------------------------------



## QChar
QChar类提供了一个16位编码的字符  
QChar是16位的，因此可以用来存储汉字，一个字符存储一个汉字  


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


## QIODevice
QIODevice类是QT中所有I/O设备的基础接口类  


## QFileDevice
QFileDevice类提供了接口用来从打开文件中读文件和写文件，其父类是QIODevice  


## QFile
QFile类提供了接口用来读文件和写文件，其父类是QFileDevice  
使用时需要包含头文件'#include <QFile>'  
**常用函数**
1. void setFileName(const QString &name)
设置文件名字，名字中可以是相对路径，可以是绝对路径，也可以没有路径  
注意：文件名路径时只支持"/"，不支持"\"  
```
myfile.setFileName("E:/test.raw");
```
2. bool QFile::open(QIODevice::OpenMode mode)
用指定模式打开文件，返回ture或false  
常用参数包括： QIODevice::ReadOnly、QIODevice::WriteOnly、QIODevice::ReadWrite  
备注：在WriteOnly和ReadWrite模式下，如果文件不存在，会在打开前自动创建该文件  
QIODevice::Truncate表示设备在打开前是截断的，设备所有早期的内容都会丢失  
```
myfile.open(QIODevice::WriteOnly | QIODevice::Truncate);
```
3. qint64 QIODevice::write(const char \*data, qint64 maxSize)
直接向文件中写入数据，返回数据的字节长度，写入失败时返回-1  
```
int number = myfile.write("this is a write test")
```
4. [override virtual] void QFileDevice::close()
调用QFileDevice::flush()函数，并关闭文件  
来自于flush()函数的error会被忽略  
5. bool QFileDevice::flush()
冲洗掉文件缓冲区的所有数据，返回返回ture或false  


## QImage
QImage类提供了不依赖于硬件的图像表示，主要用于I/O和直接逐像素访问、操作  
**使用示例**
1. 打开一个本地图片，调整大小后保存
```
QImage signimage;
signimage.load("E:/1.png");
signimage =  signimage.scaled(pic_width, pic_height);
signimage.save("E:/1.png");
```



----------------------------/*QT容器类*/-------------------------------


## QT容器类
1. 基本概念
QT提供了多个基于模板的容器类，这些容器类可以用于存储指定类型的数据项  
QT的容器类包括顺序容器类和关联容器类  
2. 容器类的特点
QT的容器类标准模板库(STL)中的容器类更轻巧、安全和易于使用  
这些容器类是隐式共享和可重入的，而且它们进行了速度和存储优化，因此可以减少可执行文件的大小  
这些容器类还是线程安全的，也就是说它们作为只读容器时可被多个线程访问  
3. 容器类的数据项
例如在QList<T>中，数据项T是一个具体的数据类型，且必须是一个可赋值的类型  
数据项T可以是int或float等简单类型，也可以是QString或QDate等类  
数据项T不能是QObject类或QObject的任何子类  
4. 示例：用QList定义一个字符串类型比的列表容器
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