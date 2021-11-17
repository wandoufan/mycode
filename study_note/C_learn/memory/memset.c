#include <stdio.h>
#include <string.h>

/*
memset()函数的用法
1. 标准形式
void *memset(void *s, int c, unsigned long n);
将指针s所指向的内存单元的前n个字节，用整型c进行替换(一般是0)
其中，指针s是void型的，因此可以为任何类型的数据进行初始化
注意：使用前要先'# include <string.h>'

2. 作用
每种类型的变量都各自的初始化方法，memset()是初始化内存的万能函数，可以直接操作内存空间
memset()一般用来给结构体或数组进行初始化，而且一般用'0'来初始化内存单元
一般的变量如int、char、float、double等类型直接初始就行，用memset()反而显得更麻烦
注意：memset()的初始化并真的要把数组中所有元素都赋值为0，只是用一个给定的值在内存中占位
后面还要继续给元素逐个赋值
*/


void memset_test1()
//对一个字符数组进行初始化
{
	char str[10];
	memset(str, 0, sizeof(str)); //n一般都写成sizeof()的形式
	for(int i = 0; i < 10; i++)
	{
		printf("%d\n", str[i]);
	}
}

int main()
{
	memset_test1();
	return 0;
}