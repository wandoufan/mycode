# Qt提供的容器型的数据类型

## 基本概念
Qt提供了多个基于模板的容器类，这些容器类可以用于存储指定类型的数据项  
Qt的容器类包括顺序容器类和关联容器类  


## 容器类的特点
Qt的容器类标准模板库(STL)中的容器类更轻巧、安全和易于使用  
这些容器类是隐式共享和可重入的，而且它们进行了速度和存储优化，因此可以减少可执行文件的大小  
这些容器类还是线程安全的，也就是说它们作为只读容器时可被多个线程访问  


## 容器类的数据项T
容器类的一般格式为：template <typename T>  
数据项T是一个具体的数据类型，且必须是一个可赋值的类型  
数据项T可以是int或float等简单类型，也可以是QString或QDate等类  
数据项T不能是QObject类或QObject的任何子类  


## Qt顺序容器类
1. QList  
2. QLinkedList  
QLinkedList是链式列表，用链表结构存储数据项，是使用不连续的内存实现存储的  
基于迭代器访问数据项，不支持序列化访问，访问修改数据的速度相对较慢  
QLinkedList的接口函数与QList基本相同  

3. QVector  
QVector提供动态数组的功能，支持序列化访问  
QVector的性能比QList更高，因为QVector的数据项是连续存储的  
QVector的接口函数与QList基本相同  

4. QStack  
5. QQueue  

## Qt关联容器类
1. QMap  
2. QMultiMap  
3. QHash  
4. QMultiHash  
5. QSet  
