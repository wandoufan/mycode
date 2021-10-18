# include <stdio.h>
# include <iostream>
using namespace std;

/*C语言中空类型指针*/

/*
基本概念：
"void *"叫做空类型指针或无类型指针，可以指向任何类型的数据，相当于通用类型的指针
空类型指针只存储所指向的地址的值，不存储指针的类型，因此不知道所指向对象的地址长度(占几个字节)
注意：空类型指针和空指针(NULL)的概念不同，不要混淆
*/


void pointer_void_test()
{
	/*
	空类型指针的基本使用
	*/
	int *p_int, a = 1;
	p_int = &a;

	float *p_float, b = 3.14;
	p_float = &b;

	char *p_char, message[] = "this is a message";
	p_char = message;

	//定义一个空类型指针，空类型指针可以指向任意类型变量
	void *p_void;
	p_void = &a;
	p_void = &b;
	p_void = message;
	p_void = NULL;

	//任何类型的指针都可以直接赋值给空类型指针，无需进行强制类型转换
	//但空类型的指针赋值给一个具体类型的指针时，必须进行强制类型转换
	p_void = p_int;
	p_int = (int *)p_void;
	p_void = p_float;
	p_float = (float *)p_void;
	p_void = p_char;
	p_char = (char *)p_void;

	//不能直接输出空类型指针所指向的变量
	// cout << *p_void << endl;//不合法
	//不能对空类型指针所指向的变量进行算术运算
	// *p_void += 1;//不合法
}

void pointer_void_parameter(void * p1_void, void * p2_void)
{
	/*
	用空类型指针作为函数参数，代表通用类型的参数
	空类型指针参数一般用于模板函数中
	*/

	//对于传入的空类型指针要先进行类型转换，然后再进行使用
	//注意：转换时的数据类型要和传入时的数据类型相一致
	int a = *((int *)p1_void);
	float b = *((float *)p2_void);
	cout << a << endl;
	cout << b << endl;
}

void *pointer_void_return()
{
	/*
	空类型指针作为函数的返回参数，代表返回任意类型的指针
	*/
	int *p, a = 10;
	p = & a;
	return p;//返回一个整型指针
}

int main()
{
	pointer_void_test();

	int i = 1;
	float f = 3.14;
	//向函数中传入参数时，要先转换为空类型指针
	pointer_void_parameter((void *)(&i), (void *)(&f));

	//对于返回的空类型指针要先进行类型转换，然后再进行使用
	//注意：转换时的数据类型要和返回时的数据类型相一致
	int *p_int;
	p_int = (int *)(pointer_void_return());
	cout << *p_int << endl;

	return 0;
}