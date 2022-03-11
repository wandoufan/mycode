# QMap

## 基本功能
QMap<Key, T>是实现Key-value数据的容器类，基于红黑树实现  
QMap和QHah的功能类似，可以根据key值快速查找value值  
备注：在Qt 5.8.1之后的版本中，可以使用指针类型来作为key  
注意：除非使用QMap::insertMulti()添加键值对，否则QMap正常情况下不允许多值映射  
如果想要实现多值映射，也可以使用QMap的子类QMultiMap  
```
\\继承关系
QMap -- QMultiMap
```


## QMap和QHash的区别
1. QHash中的元素采用无序方式存储，QMap中的元素按照key的顺序进行存储  
2. QHash的平均查询速度比QMap要更快  
3. QHash中的key必须是可以哈希的，而且必须支持'=='运算符，QMap中的key必须支持'<'等大小判断的运算符  


## 使用示例
1. 可以使用[]符号去插入一组键值对，相当于insert()函数
```
QMap<QString, int> map;
map["one"] = 1;
map["two"] = 2;
map["three"] = 3;
map.insert("four", 4);
```
2. 可以使用[]符号去读取值，相当于value()函数
```
int num1 = map["thirteen"];
int num2 = map.value("thirteen");
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


## 常用公共函数
1. QMap::iterator QMap::insert(const Key &key, const T &value)
向map中加入一组键值对，或者对已有的键修改对应的值  

2. int QMap::remove(const Key &key)
删除key对应的所有键值对，如果键值对存在，则在删除后返回1，否则返回0  

3. void QMap::clear()
清除所有元素  

4. int QMap::size() const
返回元素个数  

5. const T QMap::value(const Key &key, const T &defaultValue = T()) const
返回指定键对应的值，相当于[key]，当对应的值不存在时返回defaultdefaultValue  
使用value函数没有找到键对应的值时，如果不指定default，则会返回一个默认的返回值  
例如，要查找的值是字符串类型时，默认会返回一个空的字符串  

6. QList<T> QMap::values() const
返回所有的键值对  