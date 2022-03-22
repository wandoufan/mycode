# QMutableListIterator

## 基本功能
QMutableListIterator是一个Java风格的迭代器  
QMutableListIterator对应QList<T>和QQueue<T>两个容器类，既可以读数据，也可以写数据  
父类：无  
子类：无  


## 指针位置
与STL风格的迭代器不同，Java风格的迭代器并不直接指向容器中的元素，而是指向元素之间的位置  
因此，指针的位置包括：第一个元素之前，两个元素之间，最后一个元素之后  


## 代码示例
1. 在循环过程中修改元素的值
```
//定义和赋值
QList<int> list1;
for(int i = 0; i < 10; i ++)
{
    list1 << i;
}
//修改元素值
QMutableListIterator<int> iterator(list1);
while(iterator.hasNext())
{
    iterator.next() = 10;
}
//输出元素值
foreach(int item, list1)
{
    qDebug() << item;
}
```
2. 在循环过程中删除部分元素
```
//定义和赋值
QList<int> list1;
for(int i = 0; i < 20; i ++)
{
    list1 << i;
}
//删除部分元素
QMutableListIterator<int> iterator(list1);
while(iterator.hasNext())
{
    if(iterator.next() > 15)
        iterator.remove();
}
//输出元素值
foreach(int item, list1)
{
    qDebug() << item;
}
```


## 构造函数
1. QMutableListIterator::QMutableListIterator(QList<T> &list)
定义的迭代器的数据项必须和对应的容器类的数据项完全相同  
注意：实例化迭代器之后，指针的默认初始位置是在第一个元素之前  
```
QMutableListIterator<int> iterator(list1);
```


## 常用公共函数：获取容器类的信息
1. bool QMutableListIterator::hasNext() const
判断指针位置的后面是否还有元素  

2. bool QMutableListIterator::hasPrevious() const
判断指针位置的前面是否还有元素  

3. bool QMutableListIterator::findNext(const T &value)
从当前位置向下查找value元素，返回是否查找成功  
注意：调用该方法后指针位置会改变  

4. bool QMutableListIterator::findPrevious(const T &value)
从当前位置向前查找value元素，返回是否查找成功  
注意：调用该方法后指针位置会改变  


## 常用公共函数：获取容器类的元素
1. T &QMutableListIterator::next()
返回下一个元素，然后把指针向下移动一个位置  

2. T &QMutableListIterator::previous()
返回前一个元素，然后把指针向前移动一个位置  

3. T &QMutableListIterator::peekNext() const
返回下一个元素，不移动指针位置  

4. T &QMutableListIterator::peekPrevious() const
返回前一个元素，不移动指针位置  

5. const T &QMutableListIterator::value() const
在调用遍历函数过程中，指针可能会跳过若干元素，使用value()方法可以返回这些元素中的最后一项  
遍历函数包括：next(), previous(), findNext(), findPrevious()  
在调用next()或findNext()之后，此时调用value()的效果等于调用peekPrevious()  
在调用previous()或findPrevious()之后，此时调用value()的效果等于调用peekNext()  


## 常用公共函数：对容器类中的元素进行增删改
1. void QMutableListIterator::insert(const T &value)
在当前指针位置插入value元素，执行之后指针位置位于新插入元素的后面  

2. void QMutableListIterator::remove()
在调用遍历函数过程中，指针可能会跳过若干元素，使用remove()方法可以删除这些元素中的最后一项  
遍历函数包括：next(), previous(), findNext(), findPrevious()  

3. void QMutableListIterator::setValue(const T &value) const
在调用遍历函数过程中，指针可能会跳过若干元素，使用setValue()方法可以修改这些元素中的最后一项的元素值为value  
遍历函数包括：next(), previous(), findNext(), findPrevious()  


## 常用公共函数：移动指针的位置
1. void QMutableListIterator::toFront()
把指针的位置移动到第一个元素之前  

2. void QMutableListIterator::toBack()
把指针的位置移动到最后一个元素之后  



