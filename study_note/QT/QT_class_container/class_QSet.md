# QSet

## 基本功能
QSet<T>是一个基于哈希表实现的容器类，相当于集合，元素不允许有重复的  
QSet按照无序方式存储数据，查找值的速度非常快  
QSet内部就是用QHash实现的，只是hash函数已经定义好了  
父类：无  
子类：无  


## QSet与STL中的set的比较
二者都是实现集合的功能，区别在于：
1. QSet是基于哈希表实现的，STL中的set是基于红黑树实现  
2. QSet对数据项T的数据类型是有要求的，详见QT_container_classes.md  


## QSet与QList的比较
二者的功能和使用方式比较类似，而且都有接口函数可以实现类型的互相转换，区别在于  
1. QList中的数据是有序的，QSet中的数据是无序的  
2. QList中可以使用[]运算符，QSet中不可以使用[]运算符  
3. QList中的数据可以重复，QSet中的数据不可以重复  


## 使用示例
1. 在创建集合时可以用{}直接添加元素  
```
QSet<QString> set1 = {"one", "two", "three"};
QSet<int> set2 = {1, 2, 3, 4, 5};
QSet<int> set3{1, 2, 3, 4, 5};
```
2. 集合中的元素是无序存放的，每次输出的顺序都不一样
```
QSet<int> set = {1, 2, 3, 4, 5};
foreach(int item, set)
{
    qDebug() << item;
}
```
3. 集合支持多种运算符
```
QSet<int> set = {1, 2, 3, 4, 5};
set += 6;
set -= 1;
set << 7;
QSet<int> set1 = {1, 2, 3, 4, 5};
qDebug() << (set == set1);
...
```


## QSet支持的所有运算符
```
bool operator!=(const QSet<T> &other) const
QSet<T> operator&(const QSet<T> &other) const
QSet<T> &operator&=(const QSet<T> &other)
QSet<T> &operator&=(const T &value)
QSet<T> operator+(const QSet<T> &other) const
QSet<T> &operator+=(const QSet<T> &other)
QSet<T> &operator+=(const T &value)
QSet<T> operator-(const QSet<T> &other) const
QSet<T> &operator-=(const QSet<T> &other)
QSet<T> &operator-=(const T &value)
QSet<T> &operator<<(const T &value)
bool operator==(const QSet<T> &other) const
QSet<T> operator|(const QSet<T> &other) const
QSet<T> &operator|=(const QSet<T> &other)
QSet<T> &operator|=(const T &value)
```


## 构造函数
1. template <typename InputIterator> QSet::QSet(InputIterator first, InputIterator last)
这是基于范围[first, last)的构造函数，使用迭代器作为参数  
```
QList<int> list = {1, 2, 3, 4, 4, 5};
QSet<int> set(list.begin(), list.end());
```

2. QSet::QSet(std::initializer_list<T> list)

3. QSet::QSet()


## 常用公共函数：获取集合中的信息
int QSet::size() const
返回集合中元素的个数  

int QSet::count() const
和size()功能一样  

bool QSet::isEmpty() const

bool QSet::empty() const
这个方法由STL(标准模板库)提供，等同于isEmpty()  

bool QSet::contains(const T &value) const
判断集合中是否包含value元素  

bool QSet::contains(const QSet<T> &other) const
判断当前集合是否包含other集合的所有元素，即判断other是否为当前集合的子集  

bool QSet::intersects(const QSet<T> &other) const
intersect：相交、交叉、贯穿；  
如果当前集合和other集合至少有一个共同元素，则返回true，否则返回false  

int QSet::capacity() const
返回集合的哈希表中buckets的数量  
这个函数用来了解集合中的内存使用情况，一般都用不上这个函数，仅做了解  


## 常用公共函数：获取集合中的元素
1. QSet::iterator QSet::find(const T &value)
在集合中查找value元素，返回一个指向该元素的STL风格迭代器  
如果集合中没有该元素，则返回QSet::end()  


## 常用公共函数：向集合中添加元素
1. QSet::iterator QSet::insert(const T &value)
如果集合中不包含value元素，则插入该元素，返回一个指向该元素的STL风格迭代器  


## 常用公共函数：从集合中删除元素
1. void QSet::clear()
清空集合中所有元素  

2. bool QSet::remove(const T &value)
删除集合中的value元素，返回是否删除成功  
如果集合中不包含value元素，就会删除失败，返回false  

3. QSet::iterator QSet::erase(QSet::const_iterator pos)
删除pos位置的元素，返回一个STL风格的迭代器，迭代器指向pos位置的下一个元素  

4. QSet::iterator QSet::erase(QSet::iterator pos)
重载函数  


## 常用公共函数：set层面的交并补操作
1. void QSet::swap(QSet<T> &other)
把当前集合和other集合进行交换  

2. QSet<T> &QSet::unite(const QSet<T> &other)
unite：并集；  
把other集合中的元素都添加到当集合中，返回当前集合本身  
```
QSet<int> set1 = {1, 2, 3, 4, 5};
QSet<int> set2 = {1, 2, 3, 6};
QSet<int> set3 = set1.unite(set2);
foreach(int item, set3)
{
    qDebug() << item;
}
//    6
//    4
//    5
//    2
//    3
//    1
```

3. QSet<T> &QSet::intersect(const QSet<T> &other)
intersect：相交、交叉、贯穿；  
只保留当前集合和other集合都有的共同元素，删掉其他所有元素，返回当前集合本身  
```
QSet<int> set1 = {1, 2, 3, 4, 5};
QSet<int> set2 = {1, 2, 3, 6};
QSet<int> set3 = set1.intersect(set2);
foreach(int item, set3)
{
    qDebug() << item;
}
//1
//2
//3
```

4. QSet<T> &QSet::subtract(const QSet<T> &other)
subtract：减去、删减、扣除；  
删掉当前集合和other集合都有的共同元素，只保留剩下的元素，返回当前集合本身  
```
QSet<int> set1 = {1, 2, 3, 4, 5};
QSet<int> set2 = {1, 2, 3, 6};
QSet<int> set3 = set1.subtract(set2);
foreach(int item, set3)
{
    qDebug() << item;
}
//4
//5
```


## 常用公共函数：把QSet转换为其他类型的数据
1. QList<T> QSet::toList() const
注意：由于QSet中的元素是无序的，所以由QSet转换过来的QList中的元素顺序是不确定的，而且每次执行都不一样  
```
QSet<int> set = {1, 2, 3, 4, 5};
QList<int> list = set.toList();
```


## 常用公共函数：获取STL风格的迭代器
QSet::iterator QSet::begin()

QSet::iterator QSet::end()


## 静态公共函数
1. [static] QSet<T> QSet::fromList(const QList<T> &list)
将QList转换为QSet  
```
QList<int> list = {1, 2, 3, 4, 4, 5};
QSet<int> set = QSet<int>::fromList(list);
```
注意：从Qt 5.14开始，Qt的容器类就都支持基于范围的构造函数，应该尽量使用范围构造函数来替代这个静态公共函数  
