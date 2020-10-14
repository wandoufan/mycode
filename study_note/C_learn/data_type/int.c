#include <stdio.h>

/*C语言中的整型变量*/

/*
整型变量包括：基本整型int、短整型short int(或short)、长整型long int(或long)
以上3类都可以加上unsigned 表示为无符号数，加上signed 表示为有符号数，如果不写，默认为有符号数
在一个整常量后面加上字母u(或U)则认为是unsigned int型，如12345u
在一个整常量后面加上字母l(或L)则认为是long int型，123l
*/

void test1()
{
    int a;
    a = 1; //可以先声明变量，再赋值
    int b= 2; //可以在声明变量时直接赋值
    int a1 = 1, b1 = 2, c1 = 3; //声明可以给所有变量赋值
    int a2, b2, c2 = 3; //声明时可以给部分变量赋值
    int a3, b3, c3;
    a3 = b3 = c3 = 1; //可以同时给多个变量赋值
    //注意：int a = b = c = 3; 是错误的写法
}

int main()
{
	test1();
}