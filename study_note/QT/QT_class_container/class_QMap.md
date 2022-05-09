# QMap

## 基本功能
QMap<Key, T>是实现Key-value数据的容器类，基于红黑树实现  
备注：在Qt 5.8.1之后的版本中，可以使用指针类型来作为key  
父类：无  
子类：QMultiMap  


## QMap和QHash的区别
QMap和QHah的功能类似，都可以根据key值快速查找value值  
1. QHash中的元素采用无序方式存储，QMap中的元素按照key的顺序进行存储  
2. QHash的平均查询速度比QMap要更快，但需要的存储空间也更大  
3. QHash中的key必须是可以哈希的，而且必须支持'=='运算符，QMap中的key必须支持'<'等大小判断的运算符  
4. 在数据量小，要求查询速度时使用QHash，在数据量大，限制内存占用空间时使用QMap  


## 关于QMap中多值映射的说明
QMap中多个key对应的value值可以相同  
```
QMap<int, QString> map;
map.insert(1, "one");
map.insert(2, "one");
map.insert(3, "one");
map.insert(4, "four");
```
QMap不允许进行多值映射，即一个key不能对应多个value  
如果想要实现多值映射，也可以使用QMap的子类QMultiMap  
备注：QMap的很多函数中都有针对"一个key对应多个value"的描述及处理方式，这些是针对子类QMultiMap的  
```
QMap<int, QString> map;
map.insert(1, "three");
map.insert(1, "two");
map.insert(1, "one");
map.insert(4, "four");
//map的输出结果如下，在有相同key的情况下，只保留最新插入的键值对
//1 : "one"
//4 : "four"
```


## 关于在QMap中使用[]运算符的说明
可以使用[]符号去插入一组键值对，相当于insert()函数  
```
QMap<QString, int> map;
map["one"] = 1;
map.insert("two", 2);
```
可以使用[]符号去读取值，相当于value()函数  
```
int num1 = map["one"];
int num2 = map.value("two");
```
注意：当要读取的键值对在map中不存在时，使用[]符号读取会无意间把该键值对插入到map中  
因此，如果只是想读取，而不是插入，更加推荐使用value()函数，不推荐使用[]符号  
```
QMap<int, QString> map;
map.insert(1, "one");
//此时map中并没有key为2的键值对，用[]查询会把(2,"")插入到map中
qDebug() << map[2];
//此时map中并没有key为3的键值对，用[]查询会把(3,"")插入到map中
if(map[3] == "three")
{
    qDebug() << "test";
}
//输出map
QMapIterator<int, QString> iterator(map);
while(iterator.hasNext())
{
    iterator.next();
    qDebug() << iterator.key() << ":" << iterator.value();
}
//1 : "one"
//2 : ""
//3 : ""
```


## 使用示例
1. map中的键值对是按照key的大小进行自动排序的，不是按照添加的先后顺序排序的
```
QMap<int, QString> map;
map.insert(4, "four");
map.insert(3, "three");
map.insert(2, "two");
map.insert(1, "one");

foreach(int key, map.keys())
{
    qDebug() << key << ": " << map.value(key);
}
//1 :  "one"
//2 :  "two"
//3 :  "three"
//4 :  "four"
```
2. QMap支持使用多种运算符
```
QMap<int, QString> map1, map2, map3;
map1[1] = "one";
map2[1] = "one";
map3[1] = "two";
qDebug() << map1.operator==(map2);
qDebug() << (map1 == map2);
qDebug() << map1.operator==(map3);
qDebug() << (map1 == map3);
```


## QMap支持的所有运算符
```
QMap<Key, T> &operator=(QMap<Key, T> &&other)
QMap<Key, T> &operator=(const QMap<Key, T> &other)
bool operator!=(const QMap<Key, T> &other) const
bool operator==(const QMap<Key, T> &other) const
T &operator[](const Key &key)
const T operator[](const Key &key) const
```


## 构造函数
1. QMap::QMap(const typename std::map<Key, T> &other)
创建一个other的拷贝  

2. QMap::QMap(QMap<Key, T> &&other)
创建一个QMap实例，使它指向other指向的同一个对象  

3. QMap::QMap(std::initializer_list<std::pair<Key, T> > list)
使用初始化列表list中的每个元素来创建一个Map  
备注：仅当编译器支持C++11时，可以使用该构造函数  

4. QMap::QMap()
创建一个空的Map  


## 常用公共函数：获取map中的信息
1. int QMap::size() const
返回键值对的个数  

2. int QMap::count() const
返回键值对的个数  

3. int QMap::count(const Key &key) const
返回与key绑定的键值对的个数  

4. bool QMap::contains(const Key &key) const
判断map中是否包含与key绑定的键值对  

5. bool QMap::isEmpty() const

6. bool QMap::empty() const
这个方法由STL(标准模板库)提供，等同于isEmpty()  


## 常用公共函数：获取键值对中的key
1. const Key &QMap::firstKey() const
获取map中第一个键值对的key，也就是最小的key  
调用该函数时，map不能为空，否则会产生报错  

2. const Key &QMap::lastKey() const
获取map中最后一个键值对的key，也就是最大的key  
调用该函数时，map不能为空，否则会产生报错  

3. const Key QMap::key(const T &value, const Key &defaultKey = Key()) const
返回value对应的第一个key，如果map中没有包含该键值对，则返回defaultKey  
如果没有设置defaultKey，则函数返回一个default-constructed key  

4. QList<Key> QMap::keys() const
以列表的形式返回map中的所有key，列表中的key按升序排列  

5. QList<Key> QMap::keys(const T &value) const
以列表的形式返回map中的所有与value相关联的key，列表中的key按升序排列  


## 常用公共函数：获取键值对中的value
1. T &QMap::first()
获取map中第一个键值对的value，也就是最小的key对应的value  
调用该函数时，map不能为空，否则会产生报错  

2. T &QMap::last()
获取map中最后一个键值对的value，也就是最大的key对应的value  
调用该函数时，map不能为空，否则会产生报错  

3. const T QMap::value(const Key &key, const T &defaultValue = T()) const
返回指定key对应的value，相当于[key]，当对应的值不存在时返回defaultValue  
使用value函数没有找到键对应的值时，如果不指定default，则会返回default-constructed value  
例如，要查找的值是字符串类型时，默认会返回一个空的字符串  

4. QList<T> QMap::values() const
以列表的形式返回map中的所有的value，列表中的value按升序排列  
如果一个key对应了多个value，则所有的value都会添加到列表中，而不是只添加最新的一个键值对  


## 常用公共函数：查找键值对
1. QMap::iterator QMap::find(const Key &key)
返回一个SLT风格的迭代器，迭代器指向这个key对应的键值对  
如果map中不包含该键值对，则函数返回QMap::end()  
如果map中包含多个key对应的键值对，迭代器指向最新插入的键值对  

2. QMap::iterator QMap::lowerBound(const Key &key)
返回一个SLT风格的迭代器，迭代器指向这个key对应的键值对  
如果map中包含多个key对应的键值对，迭代器指向第一个键值对  
如果map中不包含该键值对，则迭代器指向旁边的具有更大key值的键值对  


## 常用公共函数：插入/修改键值对
1. QMap::iterator QMap::insert(const Key &key, const T &value)
向map中加入一组键值对，或者对已有的键修改对应的值  
如果map中已经存在一个关联了key的键值对，则该键值对的值会被value替换  
如果map中已经存在多个关联了key的键值对，则最新插入的一组键值对的值会被value替换  

2. QMap::iterator QMap::insert(QMap::const_iterator pos, const Key &key, const T &value)
重载函数  

3. void QMap::insert(const QMap<Key, T> &map)
重载函数  
把map参数中的所有键值对插入到当前map中  
如果map参数和当前map中存在相同的key，则当前map中的value值会被替换成map参数中的value值  


## 常用公共函数：删除键值对
1. void QMap::clear()
清除所有元素  

2. int QMap::remove(const Key &key)
删除key对应的所有键值对，如果键值对存在，则在删除后返回1，否则返回0  

3. T QMap::take(const Key &key)
删除key对应的键值对，并返回key关联的value值  
如果map中不存在该键值对，则函数返回default-constructed value  
如果key对应了多个键值对，则只删除最新插入的一组键值对  

4. QMap::iterator QMap::erase(QMap::iterator pos)
删除pos位置的键值对，返回一个STL风格的迭代器，迭代器指向pos位置的下一组键值对  


## 常用公共函数：map层面的操作
1. void QMap::swap(QMap<Key, T> &other)
把这两个map相互交换  

2. bool QMap::operator==(const QMap<Key, T> &other) const
比较两个map是否相同，仅当两个map中的键值对完全相同，才认为两个map相同  
```
qDebug() << map1.operator==(map2);
```

3. bool QMap::operator!=(const QMap<Key, T> &other) const
比较两个map是否相同，仅当两个map中的键值对完全相同，才认为两个map相同  
```
qDebug() << map1.operator==(map3);
```


## 常用公共函数：把QMap转换为其他类型的数据
1. std::map<Key, T> QMap::toStdMap() const
转换为STL(标准模板库)的map数据  


## 常用公共函数：获取STL风格的迭代器
1. QMap::iterator QMap::begin()
返回一个SLT风格的迭代器，迭代器指向第一组键值对  

2. QMap::iterator QMap::end()
返回一个SLT风格的迭代器，迭代器指向最后一组键值对  