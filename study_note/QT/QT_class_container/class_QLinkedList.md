# QLinkedList

## 基本功能
QLinkedList是链式列表，用链表结构存储数据项，是使用不连续的内存实现存储的  
基于迭代器访问数据项，不支持序列化访问，访问修改数据的速度相对较慢  
QLinkedList的接口函数与QList总体上比较相似，但也不完全相同  


## 容器类之间的比较
QList<T>、QLinkedList<T>、QVector<T>三种容器类的功能和API接口都相似  
在大部分应用场景下，使用QList最合适，尽管是一个array-list，但可以实现非常快速的prepends和appends操作  
QList会把元素分配到堆内存空间中，除非`sizeof(T) <= sizeof(void*)`  
QLinkedList将零碎的内存空间链接起来存储元素，如果确实需要一个linked-list，可以使用QLinkedList  
QVector使用连续的内存空间来存储元素，因此性能是最好的  
备注：QVector和QVarLengthArray都支持C语言的数组，而QList不支持，这一点在提供C语言接口时要注意  