#include <stdio.h>

/*整理总结C语言中输入函数getchar()和scanf()的用法*/


void test_scanf()
/*
scanf("格式控制字符串", 地址表列);
注意：后面参数不是变量，而是变量地址
*/
{
	int a;
	char b;
	scanf("%d%c", &a, &b);
}


int main()
{
	test_scanf();
	return 0;
}
