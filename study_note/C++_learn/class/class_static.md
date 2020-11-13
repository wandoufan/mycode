# 类中的静态成员

## 基本概念
1. 静态成员的定义
在类中用static声明的成员变量和成员方法都称为静态成员  
静态成员既有public，也有private  
2. 静态成员的好处
以往实现数据共享的方式是设置全局变量或全局对象，但代码量大时可能会造成程序的混乱  
静态成员可以解决这个问题，既实现数据封装隐藏，也能实现数据共享和外部访问  
静态成员变量可以看做类的多个对象之间的全局变量  
3. 静态成员的坏处
和全局变量一样，类的对象过多时会造成代码混乱，很难查出是哪个对象修改了静态成员  


## 静态成员变量
1. 注意事项
静态成员变量可以被类的多个对象共享，但只用存储一处，节省了内存空间  
当有一个对象修改了静态成员变量的值，其他对象的这个变量都会改变值  
静态成员变量具有静态生存期，在程序中初始化时开始，到程序结束时消失  
注意：静态成员变量的内存空间不会随着对象的产生而分配，也不会随着对象的消失而释放  
即静态成员变量的内存空间不能用构造函数创建，也不能用析构函数释放  
2. 声明和初始化
在类内部声明格式:'static int number;'  
在类外部初始化格式:'<数据类型><类名>::<静态成员变量> = <值>'  
注意：静态成员变量的内存空间不能通过定义类对象的方式来分配，必须在类的外部进行初始化  
注意：静态成员变量使用前必须初始化，且不能是通过一个对象进行初始化  
3. 引用格式
当静态成员变量为public时，可以有两种方式访问，通过对象引用和直接引用  
对象引用的格式: '<对象名>.<静态成员变量>'  
直接引用的格式: '<类名>::<静态成员变量>'  


## 静态成员方法
1. 注意事项
如果把函数成员声明为静态的，就可以把函数与类的任何特定对象独立开来  
静态成员函数一般都是公有的public，可以让外部不需要实例化对象就能任意调用  
静态成员函数即使在类对象不存在的情况下也能通过'类名::函数名'被调用  
静态成员函数没有this指针，只能访问类中的静态成员变量和其他静态成员函数  
2. 引用格式
当静态成员方法为public时，可以有两种方式访问，通过对象引用和直接引用  
对象引用的格式: '<对象名>.<静态成员方法>'  
直接引用的格式: '<类名>::<静态成员方法>'  