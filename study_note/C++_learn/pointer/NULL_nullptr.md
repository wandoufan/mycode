# NULL和nullptr

## NULL
NULL是一个宏定义，在C和C++中的定义不同，不同的原因来自于C++中的重载函数机制  
在C中NULL为`(void *)0`，即一个指向整数0的空类型指针，是一个内存地址  
在C++中NULL就是整数0，因此在C++中将一个指针赋值为0，就相当于指针设置为空指针  
```
MyWidget(QWidget *parent = 0);
```
注意：NULL不是一个关键字  
注意：空类型指针`(void *)`和空指针(NULL)的概念不同，不要混淆


## nullptr
nullptr并非整型类别，甚至也不是指针类型，但是能转换成任意指针类  
nullptr的实际类型是std:nullptr_t  


## 二者的使用
在c++中'(void \*)'不能转化为任意类型的指针，即'int p=(void)'是错误的，但'int \*p=nullptr'是正确的  
Visual Studio 2010以及之后的版本都支持使用nullptr  
优先使用nullptr  