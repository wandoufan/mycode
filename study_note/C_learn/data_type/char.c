#include <stdio.h>

/*C语言中的字符变量*/

/*
字符型变量用来存放字符常量，用关键字char定义，只能存放一个字符
编译系统一般都是用一个字节存放一个字符，即一个字符变量在内存中占一个字节
字符型数据在存储时实际是将其ASC码放入存储中，相当于存储整数，因此可以进行算数运算
注意：小写字母比其大写字母的ASC码值大32
*/

void test1()
{
    /*字符型变量*/
    char c1, c2;
    c1 = 'a'; //注意: c1 = "a"; 是错误的，不能把一个字符串常量赋给一个字符变量
    c2 = 'B';
    printf("%c\n", c1);
    printf("%d\n", c2);
    c2 = c2 + 32; //小写字母比其大写字母的ASC码值大32
    printf("%c\n", c2);
    printf("%d\n", c2);
}

int main()
{
	test1();
}