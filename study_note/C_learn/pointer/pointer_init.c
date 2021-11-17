#include <stdio.h>

/*整理总结C语言中指针的基本用法*/


void pointer_init()
{
	/*
	指针的定义与引用
	*/
	int i = 1, a = 2;
	int * p = &a;//在定义指针时直接赋值
	int * p1, * p2, * p3;
	p1 = & i; //先定义指针，再赋值，不用写*
	printf("* p1 : %d\n", * p1);
	p2 = & * p1; //p2等于p1所指向变量的地址对应的变量，即i
	printf("* p2 : %d\n", * p2);
	p3 = p1; //同一类型的指针可以相互赋值
	printf("* p3 : %d\n", * p3);
	printf("* & i : %d\n", * & i); //代表变量i的地址对应的变量，即i本身
}

void pointer_change1(int *pointer_1, int *pointer_2)
{
	/*
	以整型指针作为函数参数，指针指向整型变量
	在函数中改变外部变量的值，不需要return回传参数
	*/
	(*pointer_1) --;
	(*pointer_2) --;
}

void pointer_change2(int &a, int &b)
{
	/*
	以整型变量的地址作为函数参数
	在函数中改变外部变量的值，不需要return回传参数
	*/
	// printf("传入的值：%d\n", a);
	// printf("传入的值：%d\n", b);
	a ++;
	b ++;
}

int main()
{
	pointer_init();

	int a = 1, b = 2;
	int *p1 = &a, *p2 = &b;
	pointer_change1(p1, p2);
	printf("函数调用后的值 : %d\n", a);
	printf("函数调用后的值 : %d\n", b);
	pointer_change1(&a, &b);//直接以变量的地址作为参数也可以
	printf("函数调用后的值 : %d\n", a);
	printf("函数调用后的值 : %d\n", b);

	int c = 3, d = 4;
	//以变量本身作为参数，而不是把变量的地址或指向变量的指针作为参数
	pointer_change2(c, d);
	printf("函数调用后的值 : %d\n", c);
	printf("函数调用后的值 : %d\n", d);

	return 0;
}
