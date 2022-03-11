# QSet

## 基本功能
QSet<T>是实现散列表集合的容器类，相当于集合，数据项不允许有重复的  
QSet按照无序方式存储数据，查找值的速度非常快  
QSet内部就是用QHash实现的，只是hash函数已经定义好了  


## 使用示例
1. 可以直接使用<<符号插入元素，相当于insert()函数
```
set.insert("one");
set << "twelve" << "fifteen" << "nineteen";
```