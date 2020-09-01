#include <stdio.h>

/*整理总结while语句和do while语句的基本用法*/


/*
1.while后边有多个语句时要用{}括起来，括号外不加分号;
2.一般用while(1)来表示无限循环
3.当while后面的表达式第一次为"真"时，while和do while结果相同
当while后面的表达式第一次为"假"时，while一次也不执行，do while会执行一次循环体
4.注意：while语句的循环条件可以设置为'i--'，当变量减到0时，布尔值为假，会自动跳出循环
*/


int main()
{
    void while_test_1();
    while_test_1();

    void while_test_2();
    while_test_2();

    void do_while_test();
    do_while_test();

    return 0;
}


void while_test_1()
{
    int i = 1, sum = 0;
    while(i <= 100)
    {
        sum += i;
        i ++;
    }
    printf("%d\n", sum);

}


void while_test_2()
{
    /*使用i--作为循环语句可以自动结束循环，不需要另外设置跳出循环的条件*/
    int i = 5;
    while(i--)
    {
        printf("%d\n", i);
    }
}


void do_while_test()
{
    int i = 1, sum = 0;
    do
    {
        sum += i;
        i++;
    }
    while(i <= 100);
    printf("%d\n", sum);
}