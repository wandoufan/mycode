#include <stdio.h>

/*C语言中的算术运算符*/



void test1()
{
    /*自增自减运算符*/
    //注意：只能对整型变量使用自增或自减符，不能用于常量或表达式
    //5 ++ 和(a + b) ++ 都是错误写法
    int i, j;
    i = j = 2;
    printf("%d, %d\n", i ++, j --); //先使用变量，再改变变量值
    printf("%d, %d\n", i, j);
    printf("%d, %d\n", ++ i, -- j); //先改变变量值，再使用变量
    printf("%d, %d\n", i, j);
}


int main()
{

    test1();
}