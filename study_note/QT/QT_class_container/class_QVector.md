# QVector

## 基本功能
QVector提供动态数组的功能，支持序列化访问  
QVector的性能比QList更高，因为QVector使用连续的内存空间来存储数据  


## 容器类之间的比较
QList<T>、QLinkedList<T>、QVector<T>三种容器类的功能和API接口都相似  
在大部分应用场景下，使用QList最合适，尽管是一个array-list，但可以实现非常快速的prepends和appends操作  
QList会把元素分配到堆内存空间中，除非`sizeof(T) <= sizeof(void*)`  
QLinkedList将零碎的内存空间链接起来存储元素，如果确实需要一个linked-list，可以使用QLinkedList  
QVector使用连续的内存空间来存储元素，因此性能是最好的  
备注：QVector和QVarLengthArray都支持C语言的数组，而QList不支持，这一点在提供C语言接口时要注意  


## 常用公共函数
QVector的接口函数以及用法与QList总体上比较类似，不再详细记录  