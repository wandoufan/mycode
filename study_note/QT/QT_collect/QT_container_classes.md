# Qt中的容器类

## 基本概念
Qt提供了多个基于模板的容器类，这些容器类可以用于存储指定类型的数据项  
Qt的容器类包括顺序容器类和关联容器类  
容器类的一般格式为  
```
template <typename T>
```

## 容器类的特点
Qt中的容器类相比于STL(标准模板库)中的容器类更轻巧、安全和易于使用  
因此不必再使用STL中的容器类，可以直接使用Qt提供的容器类  
Qt容器类是隐式共享和可重入的，而且它们进行了速度和存储优化，因此可以减少可执行文件的大小  
Qt容器类还是线程安全的，也就是说它们作为只读容器时可被多个线程访问  


## 说明
1. 从Qt 5.14开始，除了QMultiMap之外的绝大部分容器类都支持基于范围的构造函数
Qt鼓励使用范围构造函数来替代不同的from/to函数  
```
//使用QVector对象来生成一个QSet对象，其中包含1，2，3，4，5
QVector<int> vector{1, 2, 3, 4, 4, 5};
QSet<int> set(vector.begin(), vector.end());
```
2. 容器类可以是嵌套的，即容器类中可以再包含另一个容器类
例如，可以定义如下QMap对象  
```
QMap<QString, QList<int>>
```


--------------------------容器类的数据项T--------------------------

## 数据项T的数据类型要求
数据项T必须能够提供copy构造函数和一个赋值运算符，对于有的操作，还要求有一个默认的构造函数  
大部分数据类型都能满足上述条件，都可以作为数据项存储到容器类中  
1. 数据项T可以是以下类型：
```
基本类型，如int或float等
Qt数据类型，如QString、QDate、QTime等
指针类型
```
2. 数据项T不能是以下类型：
```
QObject类或QObject的任何子类，如QWidget、QDialog、QTimer等
```
如果直接去实例化以下对象，编译器会提示QWidget的copy构造函数和赋值运算符被禁用  
```
QList<QWidget> list_widget;
```
备注：实际测试，没有发现Qt creator有任何报错或提示  
如果需要在容器中存储QObject及其子类，用指针的方式来进行存储  
```
QList<QWidget *> list_widget;
```
3. 自定义数据类型也可以作为数据项，但也要满足上述条件，示例如下：
```
class Employee
{
public:
	Employee() {} //默认构造函数
	Employee(const Employee &other); //copy构造函数

	Employee &operator=(const Employee &other); //赋值运算符

private:
	QString myName;
	QDate myDateOfBirth;
};
```
如果不定义任何显式的构造函数或赋值运算符，C++也可以提供默认的，以下示例也可以作为数据项：
```
struct Movie
{
	int id;
	QString title;
	QDate releaseDate;
};
```
4. Qt容器类都提供了<<()操作符和>>()操作符，以便于它们可以使用QDataStream来进行读写
这意味着存储在容器类中数据类型也必须支持<<()操作符和>>()操作符  
5. 有的容器类对于存储的数据项还有额外的要求，具体详见每个类的介绍
例如，`QMap<Key, T>`中的key类型必须提供operator<()  



--------------------------容器类的迭代器--------------------------

## 基本概念
迭代器是遍历访问集合元素的一种方式，从第一个元素开始直到所有元素被访问结束，迭代只能向前不能后退  
迭代的集合对象可以是序列类型的列表、元组、字符串等，也可以是非序列类型的集合、字典、文件句柄等  
Qt容器类提供了Java风格和STL风格的两种迭代器：  
Java风格的迭代器更容易使用，并且提供了高层次的函数功能  
STL风格的迭代器执行更加高效，并且可以与Qt和STL的通用算法一起使用  


## 1. Java风格的迭代器
1. 基本情况
Java风格的迭代器是在Qt 4版本中提出的，是Qt程序的标准应用  
Java风格的迭代器比STL风格的迭代器更加高效，但效率要稍微低一些  
它的API是基于Java的迭代器类实现的  
2. Java迭代器类
对于每个容器类，有两个Java类型的迭代器类：一个用于只读操作，一个用于读写操作  
如果无需修改数据，则使用只读迭代器，因为只读迭代器速度更快  
其中，最常用的是QList和QMap对应的迭代器类  
QLinkedList、QVector、QSet对应的迭代器类的API接口和QList对应的迭代器类完全相同  
QHash对应的迭代器类的API接口和QMap对应的迭代器类完全相同  
```
Containers 							Read-only iterator 			Read-write iterator

QList<T>, QQueue<T> 				QListIterator<T> 			QMutableListIterator<T>
QLinkedList<T> 						QLinkedListIterator<T>		QMutableLinkedListIterator<T>
QVector<T>, QStack<T> 				QVectorIterator<T>			QMutableVectorIterator<T>
QSet<T>								QSetIterator<T>				QMutableSetIterator<T>
QMap<Key, T>, QMultiMap<Key, T>		QMapIterator<Key, T>		QMutableMapIterator<Key, T>
QHash<Key, T>, QMultiHash<Key, T>	QHashIterator<Key, T>		QMutableHashIterator<Key, T>
```
3. 指针位置
与STL风格的迭代器不同，Java风格的迭代器并不直接指向容器中的元素，而是指向元素之间的位置  
因此，指针的位置包括：第一个元素之前，两个元素之间，最后一个元素之后  


## 2. STL风格的迭代器
1. 基本情况
STL风格的迭代器是在Qt 2.0版本中提出的，执行效率更高  
2. STL迭代器类
对于每个容器类，有两个STL类型迭代器：一个用于只读操作，一个用于读写操作  
如果无需修改数据，则使用只读迭代器，因为只读迭代器速度更快  
```
Containers 							Read-only iterator 					Read-write iterator

QList<T>, QQueue<T>					QList<T>::const_iterator 			QList<T>::iterator
QLinkedList<T>						QLinkedList<T>::const_iterator 		QLinkedList<T>::iterator
QVector<T>, QStack<T>				QVector<T>::const_iterator 			QVector<T>::iterator
QSet<T>								QSet<T>::const_iterator 			QSet<T>::iterator
QMap<Key, T>, QMultiMap<Key, T>		QMap<Key, T>::const_iterator 		QMap<Key, T>::iterator
QHash<Key, T>, QMultiHash<Key, T>	QHash<Key, T>::const_iterator		QHash<Key, T>::iterator
```
3. 指针位置
与Java风格的迭代器不同，STL风格的迭代器指针直接指向容器中的元素，而不是元素之间的位置  
4. STL中的运算符
```
表达式 			含义
*i 				返回当前元素
++i 			迭代器指向下一个元素
i += n 			迭代器指向下n个元素
--i 			迭代器指向前一个元素
i -= n 			迭代器指向前n个元素
i - j 			返回迭代器i和迭代器j之间的元素的个数
```


## 3. foreach关键字
如果只是想按顺序逐个访问容器类中的所有元素，不进行增删改操作，可以使用foreach关键字  
使用foreach相比使用只读迭代器，代码会更加简洁  
详见keyword_foreach.md  



--------------------------所有的Qt容器类--------------------------

## 1. 顺序容器类(sequential containers)
Qt提供以下顺序容器类：  
```
QList
QLinkedList
QVector
QStack
QQueue
```
### 容器类之间的比较
QList<T>、QLinkedList<T>、QVector<T>三种容器类的功能和API接口都相似  
在大部分应用场景下，使用QList最合适，尽管是一个array-list，但可以实现非常快速的prepends和appends操作  
QList会把元素分配到堆内存空间中，除非`sizeof(T) <= sizeof(void*)`  
QLinkedList将零碎的内存空间链接起来存储元素，如果确实需要一个linked-list，可以使用QLinkedList  
QVector使用连续的内存空间来存储元素，因此性能是最好的  
备注：QVector和QVarLengthArray都支持C语言的数组，而QList不支持，这一点在提供C语言接口时要注意  
QStack和QQueue是提供LIFO和FIFO的便利类  


## 2. 关联容器类(associative containers)
Qt提供以下关联容器类：  
```
QMap
QMultiMap
QHash
QMultiHash
QSet
```
Multi-容器类可以把多种数值关联到一个key上  
Hash-容器类提供基于hash函数的快速查找，而不是在一个排序好的集合中进行二分查找  



--------------------------其他一些Container-Like类--------------------------

## 基本情况
Qt中还包含一些其他的模板类，在某些方面和容器类很相似  
但是这些模板类不提供迭代器，也不能使用foreach关键字  
```
QCache<Key, T>
QContiguousCache<T>
QPair<T1, T2>
```


--------------------------顺序容器类代码示例--------------------------

## 代码示例：只读的方式遍历访问顺序容器类的元素
```
//定义和赋值
QList<int> list1;
for(int i = 0; i < 10; i ++)
{
    list1 << i;
}
//遍历方法1：使用for循环遍历容器
for(int i = 0; i < list1.length(); i++)
{
    qDebug() << list1[i];
}
//遍历方法2：使用foreach遍历容器
int item;
foreach(item, list1)
{
    qDebug() << item;
}
//遍历方法3：使用Java风格的只读迭代器
QListIterator<int> iterator(list1);
while(iterator.hasNext())
{
    qDebug() << iterator.next();
}
```


## 代码示例：修改顺序容器类中的元素值
```
//定义和赋值
QList<int> list1;
for(int i = 0; i < 10; i ++)
{
    list1 << i;
}
//修改元素值方法1：使用[]操作符获取元素
for(int i = 0; i < list1.length(); i++)
{
    list1[i] += 10;
}
foreach(int item, list1)
{
    qDebug() << item;
}
//修改元素值方法2：使用replace方法
for(int i = 0; i < list1.length(); i++)
{
    list1.replace(i, 100);
}
foreach(int item, list1)
{
    qDebug() << item;
}
//修改元素值方法3：使用Java风格的读写迭代器
QMutableListIterator<int> iterator(list1);
while(iterator.hasNext())
{
    iterator.next() = 10;
}
foreach(int item, list1)
{
    qDebug() << item;
}
```


## 代码示例：删除顺序容器类中的部分元素
```
//定义和赋值
QList<int> list1;
for(int i = 0; i < 20; i ++)
{
    list1 << i;
}
//删除元素方法1：使用Java风格的读写迭代器
QMutableListIterator<int> iterator(list1);
while(iterator.hasNext())
{
    if(iterator.next() % 2 == 0)
        iterator.remove();
}
foreach(int item, list1)
{
    qDebug() << item;
}
//删除元素方法2：使用容器类自带的removeLast()等方法
for(int i = 0; i < 5; i++)
{
    list1.removeLast();
}
foreach(int item, list1)
{
    qDebug() << item;
}
//删除元素方法3：使用容器类自带的removeAt()等方法
//注意：removeAt()方法无法在for循环中使用，实测是无效的
list1.removeAt(5);
list1.removeAt(6);
list1.removeAt(7);
foreach(int item, list1)
{
    qDebug() << item;
}
```


--------------------------关联容器类代码示例--------------------------

## 代码示例：只读的方式遍历访问关联容器类的元素
```
//定义和赋值
QMap<QString, int> map;
map["one"] = 1;
map["two"] = 2;
map["three"] = 3;
map["four"] = 4;
//遍历方法1：使用foreach遍历容器
foreach(QString key, map.keys())
{
    qDebug() << key << ": " << map[key];
}
//遍历方法2：使用Java风格的只读迭代器
QMapIterator<QString, int> iterator(map);
while(iterator.hasNext())
{
    iterator.next();
    qDebug() << iterator.key() << "：" << iterator.value();
}
```