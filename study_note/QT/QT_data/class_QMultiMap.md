# QMultiMap

## 基本功能
QMultiMap是QMap的便捷子类，可以提供多值映射的Key-value功能  
注意：QMultiMap不提供'[]'操作符  
```
\\继承关系
QMap -- QMultiMap
```


## 使用示例
1. 一个key可以对应多个value
```
QMultiMap<QString, int> map1, map2, map3;

map1.insert("plenty", 100);
map1.insert("plenty", 2000);
// map1.size() == 2

map2.insert("plenty", 5000);
// map2.size() == 1

map3 = map1 + map2;
// map3.size() == 3
```


## 常用公共函数
1. typename QMap<Key, T>::iterator QMultiMap::insert(const Key &key, const T &value)
QMultiMap::insert()等于QMap::insertMulti()  
插入一组键值对，如果key已经存在，则会创建一组新的键值对  

2. typename QMap<Key, T>::iterator QMultiMap::replace(const Key &key, const T &value)
QMultiMap::replace()等于QMap::insert()  
插入一组键值对，如果key已经存在，则value会被替换成新插入的value值  
如果有多组key已经存在，则最近插入的value会被替换成新插入的value值  

3. value(key)
返回key对应的所有value中最新插入的那个value值  

4. QList<T> QMultiMap::values(const Key &key) const
返回key对应的所有value，在返回的列表中，元素按照最近插入到最早插入的顺序排列  

5. int QMultiMap::count(const Key &key, const T &value) const
返回key-value键值对的个数  


