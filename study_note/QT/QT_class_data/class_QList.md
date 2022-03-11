# QList

## 基本功能
QList是提供列表功能的模板类，属于一个顺序容器类  
在声明QList时，必须写明QList中要存放的数据类型  
注意：一个列表中只能存放一种数据类型，不能多个数据类型混合存放，但可以存放结构体  
QList是最常用的容器类，相当于数组或列表，支持序列化访问，且访问修改数据的速度很快  
父类：无  
子类：QByteArrayList、QItemSelection、QQueue、QStringList  


## 三种容器类的对比
QList<T>、QLinkedList<T>、QVector<T>提供了相似的函数接口  


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
```
for(int i = 0; i < alist.size(); i++)
{
    qDebug() << alist[i];
}
```
2. QList<QString>也可以写为QStringList，以下两个定义相同  
```
QList<QString> aList;
QStringList alist;
```
3. 向list中添加元素时可以直接用'<<'，比使用append方法简便  
```
alist << "a" << "123" << "abc";
```
4. 在创建列表时可以直接添加元素  
```
QList<QString> alist = { "one", "two", "three" };
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


## 构造函数
1. template <typename InputIterator> QList::QList(InputIterator first, InputIterator last)
从迭代器InputIterator的范围[first, last)中构建一个列表  
迭代器中的值必须转化为数据项T  

2. QList::QList(std::initializer_list<T> args)
通过参数从std::initializer_list中构建一个列表  
备注：仅当编译器支持C++11时，可以使用该构造函数  

3. QList::QList(QList<T> &&other)
创建一个QList实例，使它指向other指向的同一个对象  

4. QList::QList(const QList<T> &other)
创建一个other的拷贝  

5. QList::QList()
创建一个空列表  


## 数据类型转换相关的常用公共函数
1. QString QStringList::join(const QString &separator) const
将字符串列表中的元素拼接起来，返回一个QString  
注意：join函数的连接字符串必须要有，可以是空字符串，但不能不写参数  
```
QStringList alist;
alist << "a" << "b" << "c" << "d";
QString str1;
str1 = alist.join("+"); //写成str1 = alist.join();会报错，join函数必须要有参数
```


## 常用公共函数
* int QList::size() const
返回列表中元素的个数  

* int QList::count() const
返回列表中元素的个数，效果等同于size()  

* T &QList::first()
返回列表中的第一个元素，列表必须不能为空  

* T &QList::last()
返回列表中的最后一个元素，列表必须不能为空  

* bool QList::isEmpty() const
判断列表是否为空  

* bool QList::startsWith(const T &value) const
判断列表是否以value元素为开头  

* void QList::append(const T &value)
在列表末尾添加元素value  

* void QList::append(const QList<T> &value)
在列表末尾添加一个新的列表  

* void QList::prepend(const T &value)
在列表开头添加元素value  

* void QList::insert(int i, const T &value)
向列表中插入元素  
如果i = 0，元素插在列表最开头，如果i = 表长，元素插在列表最后面  

* void QList::replace(int i, const T &value)
用value替换列表i位置的元素  

* void QList::move(int from, int to)
将元素从from移动到to，等价于'insert(to, takeAt(from))'  

* void QList::swap(QList<T> &other)
将当前列表和other列表进行交换  
备注：不是部分元素交换，而是整个列表相互交换  
```
alist << "a" << "b" << "c";
blist << "1";
alist.swap(blist);
qDebug() << alist; //("1")
qDebug() << blist; //("a", "b", "c")
```

* T QList::takeAt(int i)
删除指定位置的元素，并返回该元素  
如果不需要返回元素，则使用remove()函数更高效  

* void QList::removeAt(int i)
删除指定位置的元素，注意函数没有返回值  

* void QList::removeFirst()
删除第一个元素，等价于'removeAt(0)'  

* void QList::removeLast()
删除最后一个元素，等价于'removeAt(size() - 1)'  

* bool QList::removeOne(const T &value)
删除列表中的第一个value元素，并返回True；如果列表中没有该元素，则返回False  
```
list << "sun" << "cloud" << "sun" << "rain";
list.removeOne("sun");
// list: ["cloud", "sun", "rain"]
```

* int QList::removeAll(const T &value)
删除列表中所有的value元素，并返回删除元素的个数  
```
list << "sun" << "cloud" << "sun" << "rain";
list.removeAll("sun");
// list: ["cloud", "rain"]
```

* void QList::clear()
清除列表中的所有元素  