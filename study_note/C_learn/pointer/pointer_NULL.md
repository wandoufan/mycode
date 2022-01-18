# C语言中的空指针

## 基本概念
如果一个指针不指向任何数据，我们就称为空指针，用NULL表示  
注意：空指针用大写表示，小写的null没有任何特殊含义，只是一个普通的标识符  
注意：NULL不是一个关键字  
NULL本质上是一个宏定义，在stdio.h中具体定义如下：  
```
#define NULL ((void *)0)
```
也就是说，把数值0强制转换为`void *`类型，得到的就是空指针  


## 空指针NULL和空类型指针void *
空指针NULL不指向任何数据，相当于指向空白  
空类型指针`void *`指向了一块内存空间，只是在确定具体类型之前，不知道内存中存放的数据类型  


## 代码示例
1. 空指针可以直接进行输出，输出值为0
```
int main()
{
	int *p1 = NULL;
	printf("%d\n", p1);//输出值为0
	return 0;
}
```
2. 直接把数值0赋值给一个指针，不会报错，也可以输出0
但这样的写法是不专业的，不要把NULL和0等同起来  
注意：这是C语言的语法要求，在C++中允许直接把0赋值给一个指针  
```
int main()
{
	int *p1 = 0;
	printf("%d\n", p1);//输出值为0
	return 0;
}
```
3. 一个未经初始化的指针是野指针，并不是空指针，不要混淆
```
int main()
{
	int *p1;
	printf("%d\n", p1);//野指针的输出值为随机值
	return 0;
}
```