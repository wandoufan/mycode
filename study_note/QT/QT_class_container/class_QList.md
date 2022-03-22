# QList

## 基本功能
QList<T>提供基于索引的列表功能，是一个模板类，属于顺序容器类  
在声明QList时，必须写明QList中要存放的数据类型  
注意：一个列表中只能存放一种数据类型，不能多个数据类型混合存放，但可以存放结构体  
QList会把元素分配到堆内存空间中，除非`sizeof(T) <= sizeof(void*)`
QList是最常用的容器类，相当于数组或列表，支持序列化访问，且访问修改数据的速度很快  
父类：无  
子类：QByteArrayList、QItemSelection、QQueue、QStringList  


## 容器类之间的比较
QList<T>、QLinkedList<T>、QVector<T>三种容器类的功能和API接口都相似  
在大部分应用场景下，使用QList最合适，尽管是一个array-list，但可以实现非常快速的prepends和appends操作  
QList会把元素分配到堆内存空间中，除非`sizeof(T) <= sizeof(void*)`  
QLinkedList将零碎的内存空间链接起来存储元素，如果确实需要一个linked-list，可以使用QLinkedList  
QVector使用连续的内存空间来存储元素，因此性能是最好的  
备注：QVector和QVarLengthArray都支持C语言的数组，而QList不支持，这一点在提供C语言接口时要注意  


## 关于双层列表的说明
QList据说是不支持双层列表，即不能列表内部再嵌套列表  
但实际测试，双层列表在定义、赋值、取值时都没有产生报错  
```
//定义
QList<QList<int>> list1;
//赋值
for(int i = 0; i < 10; i ++)
{
    QList<int> list2;
    for(int j = 0; j < 5; j++)
    {
        list2.append(i + j);
    }
    list1.append(list2);
}
//取值
for(int i = 0; i < 10; i ++)
{
    for(int j = 0; j < 5; j++)
    {

        qDebug() << list1[i][j];
    }
}
```
另一种思路是QList中存放一个结构体，然后结构体中再存放一个QList，这样还可以存放多种类型的数据  
```
//定义
struct ChannelValue
{
    QList<int> value_list;
};
QList<ChannelValue> channel_list;
//赋值
for(int i = 0; i < 5; i++)
{
    struct ChannelValue channel_value;
    for(int j = 0; j < 10; j++)
    {
        channel_value.value_list.append(i + j);
    }
    channel_list.append(channel_value);
}
//取值
for(int i = 0; i < 5; i++)
{
    for(int j = 0; j < 10; j++)
    {
        qDebug() << channel_list[i].value_list[j];
    }
}
```


## 使用示例
1. QList中可以使用[]操作符去访问元素，而C++中的list不可以使用[]操作符  
另外，相比于at()或value()方法，使用[]操作符获取到的元素还可以直接修改元素值  
```
for(int i = 0; i < alist.size(); i++)
{
    qDebug() << alist[i];
    alist[i] += 1;
}
```
2. QList<QString>也可以写为QStringList，以下两个定义相同  
```
QList<QString> aList;
QStringList alist;
```
3. 向QList中添加元素时可以直接用'<<'，比使用append方法简便  
```
alist << "a" << "123" << "abc";
```
4. 在创建列表时可以用{}直接添加元素  
```
QList<QString> list1 = {"one", "two", "three"};
QList<int> list2 = {1, 2, 3, 4, 5};
QList<int> list3{1, 2, 3, 4, 4, 5};//等号也可以省略
```
5. 使用QList来存放结构体
```
struct ChannelInfo
{
    int Index;
    QString ID;
    QString Name;
    QString Alias;
    QString Symbol;
};

QList<ChannelInfo> m_channel_list;
```


## QList支持的所有运算符
```
QList<T> &operator=(QList<T> &&other)
QList<T> &operator=(const QList<T> &other)
bool operator!=(const QList<T> &other) const
QList<T> operator+(const QList<T> &other) const
QList<T> &operator+=(const QList<T> &other)
QList<T> &operator+=(const T &value)
QList<T> &operator<<(const QList<T> &other)
QList<T> &operator<<(const T &value)
bool operator==(const QList<T> &other) const
T &operator[](int i)
const T &operator[](int i) const
```


## 构造函数
1. template <typename InputIterator> QList::QList(InputIterator first, InputIterator last)
这是基于范围[first, last)的构造函数，使用迭代器作为参数  
```
QVector<int> vector = {1, 2, 3, 4, 5};
QList<int> list(vector.begin(), vector.end());
```

2. QList::QList(std::initializer_list<T> args)
通过参数从std::initializer_list中构建一个列表  
备注：仅当编译器支持C++11时，可以使用该构造函数  

3. QList::QList(QList<T> &&other)
创建一个QList实例，使它指向other指向的同一个对象  

4. QList::QList(const QList<T> &other)
创建一个other的拷贝  

5. QList::QList()
创建一个空列表  


## 常用公共函数：获取列表中的信息
1. int QList::size() const
返回列表中元素的个数  

2. int QList::length() const

3. int QList::count() const
返回列表中元素的个数，效果等同于size()  

4. bool QList::empty() const
这个方法由STL(标准模板库)提供，等同于isEmpty()  

5. bool QList::isEmpty() const

6. bool QList::startsWith(const T &value) const
判断列表是否以value元素为开头  

7. bool QList::endsWith(const T &value) const
判断列表是否以value元素为结尾  

8. bool QList::contains(const T &value) const
判断列表中是否包含元素value  

9. int QList::indexOf(const T &value, int from = 0) const
返回列表中找到的第一个value值对应的索引位置，如果没有找到任何匹配项，则返回-1  
from参数用来指定开始查找的位置，默认从头开始查找  


## 常用公共函数：获取列表中的元素
1. T &QList::first()
返回列表中的第一个元素，列表必须不能为空  

2. T &QList::last()
返回列表中的最后一个元素，列表必须不能为空  

3. T &QList::front()
这个方法由STL(标准模板库)提供，等同于first()  

4. T &QList::back()
这个方法由STL(标准模板库)提供，等同于last()  

5. const T &QList::constFirst() const
返回第一个元素，这个函数在Qt 5.6中被引入  

6. const T &QList::constLast() const
返回最后一个元素，这个函数在Qt 5.6中被引入  

7. const T &QList::at(int i) const
返回索引位置i对应的元素，i必须在合法的索引范围内  
这个函数的执行速度非常快，可以在常量时间内完成  

8. T QList::value(int i) const
返回索引位置i对应的元素，如果i超出了索引范围，则会返回一个默认构造值  
如果能够确定i在合法范围内，则尽量使用at()方法，其执行速度更快  

9. T QList::value(int i, const T &defaultValue) const
这是一个重载函数，用defaultValue参数来指定i超出了索引范围时返回的默认值  

10. T &QList::operator\[](int i)
返回索引位置i对应的元素，i必须在合法的索引范围内  
注意：相比于at()或value()方法，使用\[]符号获取的元素可以直接修改元素值  


## 常用公共函数：获取子列表
1. QList<T> QList::mid(int pos, int length = -1) const
获取一个从pos位置开始的子列表  
length参数指定子列表长度，length默认值为-1，代表从pos位置一直到列表结尾  


## 常用公共函数：向列表中增加元素
1. void QList::insert(int i, const T &value)
向列表i位置插入元素value  
如果i = 0，元素插在列表最开头，如果i = 列表长度，元素插在列表最后面  

2. void QList::append(const T &value)
在列表末尾添加元素value  

3. void QList::append(const QList<T> &value)
在列表末尾添加一个新的列表  

4. void QList::prepend(const T &value)
在列表开头添加元素value  

5. void QList::push_back(const T &value)
这个方法由STL(标准模板库)提供，等同于append()  

6. void QList::push_front(const T &value)
这个方法由STL(标准模板库)提供，等同于prepend()  


## 常用公共函数：从列表中删除元素
1. void QList::clear()

2. void QList::removeAt(int i)
删除指定位置的元素  

3. void QList::removeFirst()
删除第一个元素，效果等于'removeAt(0)'  

4. void QList::removeLast()
删除最后一个元素，效果等于'removeAt(size() - 1)'  

5. void QList::pop_front()
这个方法由STL(标准模板库)提供，等同于removeFirst()  

6. void QList::pop_back()
这个方法由STL(标准模板库)提供，等同于removeLast()  

7. T QList::takeAt(int i)
删除指定位置的元素，并返回该元素  
如果不需要返回元素，则使用removeAt()函数更高效  

8. T QList::takeLast()
删除列表中的第一个元素，并返回该元素，效果等于'takeAt(size() - 1)'  
如果不需要返回元素，则使用removeLast()函数更高效  

9. T QList::takeFirst()
删除列表中的第一个元素，并返回该元素，效果等于'takeAt(0)'  
如果不需要返回元素，则使用removeFirst()函数更高效  

10. bool QList::removeOne(const T &value)
删除列表中的第一个value元素，并返回True；如果列表中没有该元素，则返回False  
```
list << "sun" << "cloud" << "sun" << "rain";
list.removeOne("sun");
// list: ["cloud", "sun", "rain"]
```

11. int QList::removeAll(const T &value)
删除列表中所有的value元素，并返回删除元素的个数  
```
list << "sun" << "cloud" << "sun" << "rain";
list.removeAll("sun");
// list: ["cloud", "rain"]
```


## 常用公共函数：修改列表中的元素值
1. void QList::replace(int i, const T &value)
将列表位置i的元素值修改为value  


## 常用公共函数：移动列表中元素位置
1. void QList::move(int from, int to)
将元素从位置from移动到位置to，等价于'insert(to, takeAt(from))'  

2. void QList::swapItemsAt(int i, int j)
交换位置i和位置j的元素  
其中，i和j都要大于0，小于size()  
```
QList<QString> list;
list << "A" << "B" << "C" << "D" << "E" << "F";
list.swapItemsAt(1, 4);
// list: ["A", "E", "C", "D", "B", "F"]
```

3. void QList::swap(QList<T> &other)
将当前列表和other列表进行交换  
注意：不是部分元素交换，而是整个列表相互交换  
```
alist << "a" << "b" << "c";
blist << "1";
alist.swap(blist);
qDebug() << alist; //("1")
qDebug() << blist; //("a", "b", "c")
```


## 常用公共函数：把QList转换为其他类型的数据
1. QSet<T> QList::toSet() const

2. std::list<T> QList::toStdList() const
```
QList<double> list;
list << 1.2 << 0.5 << 3.14;
std::list<double> stdlist = list.toStdList();
```

3. QVector<T> QList::toVector() const


## 常用公共函数：获取列表的迭代器
QList::iterator QList::begin()
返回一个STL风格的迭代器，指向列表中的第一个元素 

QList::iterator QList::end()
返回一个STL风格的迭代器，指向列表中的最后一个元素 

QList::const_iterator QList::begin() const
重载函数  

QList::const_iterator QList::end() const
重载函数  

QList::const_iterator QList::cbegin() const
返回一个STL风格的迭代器，指向列表中的第一个元素  

QList::const_iterator QList::constBegin() const
返回一个STL风格的迭代器，指向列表中的第一个元素  

QList::const_iterator QList::cend() const
返回一个STL风格的迭代器，指向列表中的最后一个元素  

QList::const_iterator QList::constEnd() const
返回一个STL风格的迭代器，指向列表中的最后一个元素  

QList::const_reverse_iterator QList::crbegin() const
返回一个STL风格的逆序迭代器，指向列表中的第一个元素  

QList::const_reverse_iterator QList::crend() const
返回一个STL风格的逆序迭代器，指向列表中的最后一个元素  


## 静态公共函数
注意：从Qt 5.14开始，Qt的容器类就都支持基于范围的构造函数，应该尽量使用范围构造函数来替代下面的静态公共函数  
1. [static] QList<T> QList::fromSet(const QSet<T> &set)
2. [static] QList<T> QList::fromStdList(const std::list<T> &list)
3. [static] QList<T> QList::fromVector(const QVector<T> &vector)