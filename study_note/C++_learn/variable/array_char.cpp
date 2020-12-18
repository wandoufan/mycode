#include <stdio.h>
#include <cstring>
#include <iostream>
using namespace std;

/*整理总结C语言中字符数组的基本用法*/

/*
1.C语言中字符串只能用字符数组来存放，字符数组中的一个元素存放一个字符
2.由于C语言中字符型和整型是相互通用的，也可以用整型数组来存放字符数据，这样操作合法但是浪费存储空间
3.注意：字符数组只能在定义时用一个字符串常量来整体赋值，不能先定义再整体赋值一个字符串
非法操作：char a[10]; a[10] = "happy";
也不能两个字符数组相互赋值，非法操作：str1 = str2;
也可以通过strcpy函数来实现先定义数组再整体赋值的操作：strcpy(str1, "test");
4.注意：用字符串常量整体赋值后系统会在最后自动加上一个'\0'，所以这样得到的字符数组长度+1
5.不能用s格式符输出单个字符，非法操作：printf("%s", c[0]);
6.对于一个字符类型的数组，可通过引用数组名或字符指针变量来一次输出一个字符串(不是逐个输出字符)
而对于一个数值类型的数组，不能通过数组名整体输出，只能逐个引用数组元素
*/


void test_init()
{
    //定义字符数组时直接整体赋值
    //注意：要在最后加上'\0'表示结束，否则输出结果中会有乱码，'\0'也占据一个数组长度
    //1. 初始化时对所有元素进行赋值
    char a[11] = {'I', ' ', 'a', 'm', ' ', 'h', 'a', 'p', 'p', 'y', '\0'};
    //2. 初始化时，未指定的元素默认值为空字符，即'\0'
    char b[10] = {'I', ' ', 'a', 'm', ' ', 'h'};
    //3. 如果初始化时指定了全部的元素值，定义时可以省略数组长度
    char c[] = {'I', ' ', 'a', 'm', ' ', 'h', 'a', 'p', 'p', 'y', '\0'};
    //4. 可以直接使用一个字符串常量来对字符数组进行初始化
    char d[] = {"I am happy"};
    //5. 用字符串常量初始化是可以省略括号
    char e[] = "I am happy";

    //先定义数组，然后再逐个进行赋值
    char f[5];
    f[0] = 'g';
    f[1] = 'o';
    f[2] = 'o';
    f[3] = 'd';
    f[4] = '\0';

    //注意：以下是错误写法
    //1. 必须在定义时整体赋值，不能先定义一个字符数组，然后再整体赋值
    //char a[10];
    // a = "I am happy";
    //2. 字符数组之间不能相互赋值，只能用strcpy函数
    // char a[10] = {'I', ' ', 'a', 'm', ' ', 'h', 'a', 'p', 'p', 'y'};
    // char b[10];
    // b = a;

    /*字符数组也可以定义二维的*/
    char z[3][5] = {{' ', ' ', '*', ' ', ' '}, {' ', '*', ' ', '*', ' '}, {'*', ' ', ' ', ' ', '*'}};
    for(int i = 0; i <= 2; i++)
    {
        for(int j = 0; j <= 4; j++)
            printf("%c,", z[i][j]);
        printf("\n");
    }
    printf("\n");
}


void test_output()
{
    char a[10] = {'I', ' ', 'a', 'm', ' ', 'h', 'a', 'p', 'p', 'y'};
    /*c格式符输出一个字符*/
    printf("%c\n", a[0]);
    /*s格式符用来输出一个字符串*/
    printf("%s\n", a);
}

void test_output_cpp()
{
    char a[11] = {'I', ' ', 'a', 'm', ' ', 'h', 'a', 'p', 'p', 'y', '\0'};
    //对于一个字符类型的数组，可通过引用数组名来整体输出
    cout << a << endl;
    //可以通过索引下标来逐个输出数组元素
    cout << a[0] << endl;
    //注意：当引用数组下标超出合法范围时，程序并不报错，而是返回一个随机值
    cout << a[-1] << endl;
    cout << a[20] << endl;
}

void test_function()
{
    /*C库函数提供了很多用来处理字符串的函数*/
    //注意：要在C++环境下使用这些函数，必须先#include <cstring>
    char str1[] = "I am happy";
    char str2[] = "Hello World";

    /*1.strcat(str1, str2)函数将str2拼接到str1的后面，返回str1的地址*/
    printf("%s\n", strcat(str1, str2));

    /*2.strcpy(str1, str2)函数将str2复制到str1中去，str1的原数据被抹去，返回str1的地址*/
    /*strcpy函数常用来对字符数组进行整体赋值*/
    printf("%s\n", strcpy(str1, "test"));

    /*3.strncpy(str1, str2, n)函数将str2的前n个字符复制到str1中去，str1的原数据被抹去，返回str1的地址*/
    printf("%s\n", strncpy(str1, "good", 2));

    /*4.strcmp(str1, str2)函数比较str1和str2，对字符串自左至右按ASCII码值大小比较，以第一个不同的字符为准
    若str1=str2，函数值为0；若str1>str2，函数值为正整数1；若str1<str2，函数值为负整数-1
    注意：1和-1的布尔值都是True，因此函数返回值不能直接用来判断真假*/
    printf("%d\n", strcmp("china", "chima"));
    if(strcmp("china", "chima") > 0)
        printf("yes\n");
    
    /*5.strlen(str1)函数返回str1的长度，注意：长度是指字符串的实际长度，不包括'\0'在内*/
    printf("%d\n", strlen("this is a length test"));

    /*6.strlwr(str1)函数将字符串中所有字母小写，返回str1的地址*/
    printf("%s\n", strlwr(str2));

    /*7.strupr(str1)函数将字符串中所有字母大写，返回str1的地址*/
    printf("%s\n", strupr(str2));

    /*其他函数待补充.....*/
}

int main()
{
    // test_init();
    //test_output();
    test_output_cpp();
    //test_function();

    return 0;
}