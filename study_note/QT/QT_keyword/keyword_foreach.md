# QT中的foreach关键字

## 基本说明
foreach实际是<QtGlobal>里定义的一个宏，用来遍历容器类中所有的元素  
如果只是想按顺序逐个访问容器类中的所有元素，不进行增删改操作，可以使用foreach关键字  
使用foreach相比使用迭代器，代码会更加简洁  
备注：标准C++中并没有foreach，只是Qt中增加了这一关键字，而C#和Java中有foreach  
注意：foreach遍历容器是通过创建一个容器的副本，所以不能修改原容器中元素的值  


## 语法格式
基本格式为：  
```
foreach(variable, container)
```
示例：
```
foreach(int i, list1)
```


## 说明
1. 对于QMap和QHash，foreach会自动访问键值对
因此，不要在循环体中再去调用values()方法，否则会产生不必要的copy  
备注：values()方法的作用是返回所有的键值对  
如果想要访问所有的键值对，可以使用Java风格的迭代器或STL风格的迭代器，速度会更快  
或者，也可以在foreach中获取到key，然后再用key来获得value  
```
//定义和赋值
QMap<QString, int> map;
map["one"] = 1;
map["two"] = 2;
map["three"] = 3;
map["four"] = 4;
//使用foreach遍历容器
foreach(QString key, map.keys())
{
    qDebug() << key << ": " << map[key];
}
```
2. 对于多值映射的map容器类，使用两层foreach循环
```
QMultiMap<QString, int> map;
...
foreach (const QString &str, map.uniqueKeys())
{
    foreach (int i, map.values(str))
        qDebug() << str << ':' << i;
}

```
3. 在foreach之外，Qt还提供了forever关键字来实现无限循环
```
forever
{
    ...
}
```
4. 如果担心命名空间污染，可以在.pro文件中禁用这些宏
```
CONFIG += no_keywords
```



## 代码示例
1. foreach和for一样，当循环语句只有一行时'{}'可以省略，有多行代码时必须加上'{}'
```
//定义和赋值
QList<int> list1;
for(int i = 0; i < 10; i ++)
{
    list1 << i;
}

int item;
//循环语句只有一行时，省略'{}'
foreach(item, list1)
    qDebug() << item;
//循环语句有多行时，必须加上'{}'
foreach(item, list1)
{
    qDebug() << item;
    qDebug() << item + 1;
}
```
2. 除非元素的数据类型中包含逗号(如`QPair<int, int>`)，迭代中用到的变量都可以直接在foreach语句中进行定义  
而且和for语句一样，在foreach语句中定义的变量是一个只在foreach中生效的局部变量  
```
foreach(int item, list1)
    qDebug() << item;
```
3. 和所有的C++循环结构一样，在foreach循环体中可以使用continue或break
```
//定义和赋值
QList<int> list1;
for(int i = 0; i < 10; i ++)
{
    list1 << i;
}
//使用continue
foreach(int item, list1)
{
    if(item == 3)
        continue;
    else
        qDebug() << item;
}
//使用break
foreach(int item, list1)
{
    if(item == 3)
        break;
    else
        qDebug() << item;
}
```



