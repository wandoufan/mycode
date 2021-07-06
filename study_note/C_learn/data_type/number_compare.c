#include <stdio.h>

/*C语言中的数字比较大小*/

/*
注意：对于浮点型或整形等数字之间比较大小时，不能连续比较，只能分开比较！
即不能写成"0 < f < 10"的形式，必须写成"0 < f && f < 10"
*/

void test1()
{
	/*错误示例*/
	float f = 3.14;
	if(0 < f < 10)
	{
		printf("111111\n");
	}
	if(10 < f < 20)
	{
		printf("222222\n"); //也会被执行
	}
}

void test2()
{
	/*正确示例*/
	float f = 3.14;
	if(0 < f && f < 10)
	{
		printf("333333\n");
	}
	if(10 < f && f < 20)
	{
		printf("444444\n");
	}
}

int main()
{
	test1();
	test2();
}