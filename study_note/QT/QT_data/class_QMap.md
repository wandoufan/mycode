# QMap

## 基本功能
QMap<Key, T>是实现Key-value数据的容器类，相当于字典  
在Qt 5.8.1之后的版本中，可以使用指针类型来作为key  
除非使用QMap::insertMulti()添加键值对，否则QMap正常情况下不允许多值映射  


## 使用示例
```
QMap<QString, int> map;
map["one"] = 1;
map["two"] = 2;
map["three "] = 3;
```

```
QMap<int, QVariant> all_channel_info;
```



## QMap和QHash的比较
1. QHash采用无序方式存储，QMap按照key的顺序进行存储  
2. QHash的查询速度比QMap要更快  


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


## 常用函数
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
