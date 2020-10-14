#include <stdio.h>

/*C语言中的字符串常量*/

/*
字符串常量是一对双引号括起来的字符序列
注意：字符常量'a'和字符串常量"a"是不同的，C语言中每个字符串常量结尾都以'\0'作为结束标志
注意：在C语言中没有专门的字符串变量，即没有str类型，需要用字符型数组来存放字符串
*/

void test1()
{
    /*字符串常量*/
    printf("hello world\n");
    printf("%s\n", "hello world");
}

int main()
{
	test1();
}