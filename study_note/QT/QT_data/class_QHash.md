# QHash

## 基本功能
QHash<Key，T>是基于散列表来实现字典功能的容器类，基于哈希表实现  
QHah和QMap的功能类似，但QHash的查询速度更快  、
备注：使用QHash需要自定义一个名为qHash()的全局散列函数  
QHash一般不允许使用多值映射，如果想要实现多值映射，也可以使用QHash的子类QMultiHash  
```
\\继承关系
QHash -- QMultiHash
```


## QMap和QHash的区别
1. QHash中的元素采用无序方式存储，QMap中的元素按照key的顺序进行存储  
2. QHash的平均查询速度比QMap要更快  
3. QHash中的key必须是可以哈希的，而且必须支持'=='运算符，QMap中的key必须支持'<'等大小判断的运算符  