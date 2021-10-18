#include <stdio.h>

/*整理总结C语言中输出函数putchar、printf、sprintf的用法*/

/*
1.putchar函数中使用的是单引号，printf函数中使用的是双引号
*/


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
/*
格式输出函数printf(格式控制, 输出列表)向终端控制台上输出若干个任意类型的数据
注意：C语言中没有能够直接以二进制形式输出数字的格式符
*/
{
    /*d格式符输出十进制整数*/
    int a, b, c;
    a = b = c = 3;
    printf("%d, %d, %d\n", a, b, c);
    printf("%d%d%d\n", a, b, c);
    printf("a=%d, b=%d, c=%d\n", a, b, c);

    /*o格式符输出八进制整数（不输出前导符0）*/
    int number1 = 111;
    printf("八进制：%o\n", number1);

    /*x格式符输出十六进制整数（不输出前导符0x）*/
    int number2 = 111;
    printf("十六进制(小写)：%x\n", number2);
    printf("十六进制(大写)：%X\n", number2);

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
    printf("%.2f\n", e); /*输出小数点后2位*/

    /*其他格式符待补充.....*/
    
}

void test_sprintf()
/*
sprintf可以把格式化文本（字符串/字符流）打印到字符串缓冲区上
一般用来把不同类型的多个变量数据写入到同一个字符串中，类似于简便的格式转换
sprintf(字符串缓冲区, 格式控制, 输出列表)
*/
{
    char buffer[100];
    int a = 1;
    float b = 3.14;
    char c = 'c';
    char str[] = "this is a string";
    sprintf(buffer, "拼接字符串：%d + %.2f + %c, %s\n", a, b, c, str);
    printf("%s\n", buffer);

    char buffer2[100];
    sprintf(buffer2, "sprintf函数也可以只写前两个参数，忽略输出列表");
    printf("%s\n", buffer2);
}

int main()
{
    //test_putchar();
    test_printf();
    // test_sprintf();
    return 0;
}
