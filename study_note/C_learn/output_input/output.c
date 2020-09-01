#include <stdio.h>

/*整理总结C语言中输出函数putchar和printf的用法*/

/*
1.putchar函数中使用的是单引号，printf函数中使用的是双引号
*/


int main()
{
    void test_putchar();
    //test_putchar();
    void test_printf();
    test_printf();

    return 0;
}


void test_putchar()
/*字符输出函数putchar(c)向终端输出一个字符(只能是一个字符)*/
{
    char a, b, c;
    a = 'B';
    b = 'O';
    c = 'Y';
    putchar(a);
    putchar(b);
    putchar(c);
    /*可以通过转义符\来输出一些特殊的字符*/
    putchar('\n'); /*换行*/
    putchar('\\'); /*输出\*/
    putchar('\''); /*输出单引号*/
    putchar('\"'); /*输出双引号*/
}


void test_printf()
/*格式输出函数printf(格式控制, 输出列表)向终端输出若干个任意类型的数据*/
{
    /*d格式符输出十进制整数*/
    int a, b, c;
    a = b = c = 3;
    printf("%d, %d, %d\n", a, b, c);
    printf("%d%d%d\n", a, b, c);
    printf("a=%d, b=%d, c=%d\n", a, b, c);

    /*c格式符输出一个字符*/
    char d;
    d = 'A';
    printf("%c\n", d);

    /*s格式符用来输出一个字符串*/
    printf("%s\n", "china");
    printf("china\n");

    /*f格式符用来输出实数，以小数形式输出*/
    float e, f;
    e = 3.1415;
    f = 0.9999;
    printf("%f\n", e + f); /*%f不指定字段宽度，整数部分全部输出，并输出6位小数*/
    printf("%4.3f\n", e + f); /*指定输出数据长度为4，其中包含3位小数*/

    /*其他格式符待补充.....*/
    
}