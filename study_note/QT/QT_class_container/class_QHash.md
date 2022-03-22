# QHash

## 基本功能
QHash<Key，T>是基于散列表来实现字典功能的容器类，基于哈希表实现  
QHash一般不允许使用多值映射，如果想要实现多值映射，也可以使用QHash的子类QMultiHash  
父类：无  
子类：QMultiHash  


## QMap和QHash的区别
QHah和QMap的功能类似，但QHash的查询速度更快  
1. QHash中的元素采用无序方式存储，QMap中的元素按照key的顺序进行存储  
2. QHash的平均查询速度比QMap要更快，但需要的存储空间也更大  
3. QHash中的key必须是可以哈希的，而且必须支持'=='运算符，QMap中的key必须支持'<'等大小判断的运算符  
4. 在数据量小，要求查询速度时使用QHash，在数据量大，限制内存占用空间时使用QMap  


## 代码示例
1. 使用qHash()函数计算字符串
```
QHash<QString, int> hash;
hash.insert("one", 1);
hash.insert("two", 2);
hash.insert("three", 3);
hash.insert("four", 4);
QList<QString> key_list = hash.keys();
foreach(QString key, key_list)
{
    qDebug() << qHash(key);
}
//3149094
//110182
//110339486
//115276
```
2. QHash中可以使用[]运算符，且使用规则与QMap中一样
```
QHash<int, QString> hash;
hash[1] = "one";
hash[2] = "two";
```


## QHash支持的所有运算符  
```
QHash<K, V> &operator=(QHash<K, V> &&other)
QHash<K, V> &operator=(const QHash<K, V> &other)
bool operator!=(const QHash<K, V> &other) const
bool operator==(const QHash<K, V> &other) const
T &operator[](const Key &key)
const T operator[](const Key &key) const
```


## 构造函数
1. template <typename InputIterator> QHash::QHash(InputIterator begin, InputIterator end)
这是基于范围[begin, end)的构造函数，使用迭代器作为参数  

2. QHash::QHash(QHash<K, V> &&other)

3. QHash::QHash(const QHash<K, V> &other)

4. QHash::QHash(std::initializer_list<std::pair<Key, T> > list)

5. QHash::QHash()



## 常用公共函数
QHash的接口函数以及[]运算符的用法与QMap总体上比较类似，不再详细记录  


--------------------哈希函数-------------------------

## 哈希函数的要求
1. 对于相同的key，计算出的结果要完全一致
2. 对于不同的key，计算出的结果尽可能均匀分布到整个地址空间


## QHash实现的键值哈希函数
```
uint qHash(const QSslDiffieHellmanParameters &dhparam, uint seed)
uint qHash(const QUrl &url, uint seed = 0)
uint qHash(const QOcspResponse &response, uint seed)
uint qHash(const QHash<Key, T> &key, uint seed = 0)
uint qHash(const QBitArray &key, uint seed = 0)
uint qHash(char key, uint seed = 0)
uint qHash(const QDateTime &key, uint seed = 0)
uint qHash(QSslEllipticCurve curve, uint seed)
uint qHash(QLatin1String key, uint seed = 0)
uint qHash(uchar key, uint seed = 0)
uint qHash(const QDate &key, uint seed = 0)
uint qHash(signed char key, uint seed = 0)
uint qHash(const QTime &key, uint seed = 0)
uint qHash(const QSet<T> &key, uint seed = 0)
uint qHash(const T *key, uint seed = 0)
uint qHash(ushort key, uint seed = 0)
uint qHash(short key, uint seed = 0)
uint qHash(uint key, uint seed = 0)
uint qHash(const QPair<T1, T2> &key, uint seed = 0)
uint qHash(int key, uint seed = 0)
uint qHash(const std::pair<T1, T2> &key, uint seed = 0)
uint qHash(const QVersionNumber &key, uint seed = 0)
uint qHash(ulong key, uint seed = 0)
uint qHash(long key, uint seed = 0)
uint qHash(quint64 key, uint seed = 0)
uint qHash(qint64 key, uint seed = 0)
uint qHash(float key, uint seed = 0)
uint qHash(double key, uint seed = 0)
uint qHash(long double key, uint seed = 0)
uint qHash(const QChar key, uint seed = 0)
uint qHash(const QByteArray &key, uint seed = 0)
uint qHash(const QString &key, uint seed = 0)
uint qHash(const QStringRef &key, uint seed = 0)
uint qHashBits(const void *p, size_t len, uint seed = 0)
uint qHashRange(InputIterator first, InputIterator last, uint seed = 0)
uint qHashRangeCommutative(InputIterator first, InputIterator last, uint seed = 0)
```




