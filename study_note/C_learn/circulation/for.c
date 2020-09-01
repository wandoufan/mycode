#include <stdio.h>

/*整理总结for语句的基本用法*/

/*
1.for语句非常灵活，不仅可以用于循环次数已经确定的情况，
还可以用于循环次数不确定但知道循环结束条件的情况，完全可以替代while语句
2.for语句标准格式:for(循环变量赋初值; 循环条件; 循环变量增值)
3.for语句中的三个表达式都可以省略：for(; ;)，此时相当于while(1)
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

    void test_6();
    test_6();

    return 0;
}


void test_1()
{
    /*对循环变量i的定义也可以直接写到for语句中：for(int i = 1; i <= 5; i++)*/
    int i;
    for(i = 1; i <= 5; i++)
        printf("%d\n", i);
    printf("\n");
}


void test_2()
{
    /*for后面如果有多个语句，要用{}括起来，否则只会循环执行第一句，循环结束后才会执行其他语句*/
    int i;
    for(i = 1; i <= 5; i++)
    {
        printf("%d\n", i);
        printf("this is test_2\n");
    }
    printf("\n");
}


void test_3()
{
    /*若循环变量在for语句之前已经赋初值，则for的第一个表达式可以省略，注意表达式后面的分号不能省略*/
    int i = 1;
    for(; i <= 5; i++)
        printf("%d\n", i);
    printf("\n");
}


void test_4()
{
    /*for语句的第二个表达式可以省略，即不判断循环条件，循环会无限进行下去*/
    int i;
    for(i = 1; ; i++)
    {
        printf("%d\n", i);
        if(i > 4)
            break;
    }
    printf("\n");
}


void test_5()
{
    /*for语句的第三个表达式也可以省略，但要在循环体中给出循环变量的增值语句，否则循环会无限制进行下去*/
    int i;
    for(i = 1; i <= 5;)
    {
        printf("%d\n", i);
        i++;
    }
    printf("\n");
}


void test_6()
{
    /*for语句的第一个表达式也可以是与循环变量无关的其他表达式*/
    int i, sum;
    i = 1;
    for(sum = 0; i <= 10; i++)
    {
        sum = sum + i;
        printf("%d\n", sum);
    }
}