# C++中的NULL和nullptr

## C++中的空指针NULL
NULL是一个宏，但在C和C++中的定义不同，不同的原因来自于C++中的重载机制  
在C语言中，NULL的定义如下：  
```
#define NULL ((void *)0)
```
在C++中，NULL的重新定义如下：  
```
#define NULL 0
```
在C++中NULL就是整数0，因此在C++中将一个指针赋值为0，就相当于指针设置为空指针  
```
int *p = NULL;//方法一
int *p = 0;//方法二
int *p = nullptr;//方法三
```
注意：NULL不是一个关键字  


## C++中NULL存在的问题
由于C++对NULL进行了重载，在重载函数中产生了歧义问题，不同编译器下可能运行结果不一样  
编译器在遇到0时，要判断是数值0还是空指针，大多数编译器会优先认为0是一个数值  
代码示例：  
```
void func(int * p)//重载函数1
{
	cout << "函数参数为整型指针：" << p << endl;
}

void func(int p)//重载函数2
{
	cout << "函数参数为整型：" << p << endl;
}

int main()
{
	func(0);//编译器要判断0是数值还是空指针，实际会调用重载函数2
	return 0;
}
```


## C++中的nullptr
为了解决上述问题，在C++11中引入了nullptr来替代NULL  
nullptr并非整型类别，甚至也不是指针类型，nullptr的本质是一个std:nullptr_t类型的变量  
nullptr可以被转换成任何指针类型，但不能被转换为其他数据类型  
Visual Studio 2010以及之后的版本都支持使用nullptr，推荐优先使用nullptr  
注意：nullptr是一个关键字  
```
int main()
{
	int *p1 = nullptr;
	float *p2 = nullptr;
	char *p3 = nullptr;
	// bool b = nullptr;//错误
	// int a = nullptr;//错误
	// float f = nullptr;//错误
	return 0;
}
```


## C++中的void *
C++中的空类型指针也和C语言中的不完全一样  
在c++中，`(void *)`不能隐式的转换为其他类型的指针  
备注：这部分暂时没有看太懂  
