#include <stdio.h>

/*整理总结if语句的基本用法*/

/*
1.if语句后面没有冒号，这一点与python不同
2.else不是一个单独的语句，必须是if语句的一部分，与if配对使用
*/


int main()
{
    void test_1();
    test_1();

    void test_2();
    test_2();

    void test_3();
    test_3();

    void test_4();
    test_4();

    void test_5();
    test_5();

    return 0;
}


void test_1()
{
    /*if(表达式)语句*/
    int a, b;
    a = 1;
    b = 2;
    if(a < b)printf("yes\n"); /*可以分成两行写，但是是一个语句，只能最后加一个分号*/
}


void test_2()
{
    /*if(表达式)语句1 else 语句2*/
    int a, b;
    a = 1;
    b = 2;
    if(a > b)
        printf("yes\n"); /*每个语句后面都有一个分号*/
    else
        printf("no\n");
}


void test_3()
{
    /*else if 语句*/
    int x, y;
    x = 10;
    if(x < 0)
        y = 1; /*每个语句后面都有一个分号*/
    else if(x < 5)
        y = 2;
    else if(x < 10)
        y = 3;
    else y = 4;
    printf("%d\n", y);
}


void test_4()
{
    /*if后面有多个语句时要用{}括起来，注意括号外边不需要再加分号;*/
    if(1 < 2)
    {
        printf("this is 1\n");
        printf("this is 2\n");
        printf("this is 3\n");
    }
}


void test_5()
{
    /*if语句可以嵌套使用*/
    int x, y;
    x = 1;
    if(x < 10)
        if(x < 0)
            y = 1;
        else
            y = 2;
    else
        if(x > 20)
            y = 3;
        else
            y = 4;
    printf("%d\n", y);
}