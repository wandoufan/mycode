#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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

int main()
{
    printf("111111111\n");
    void test_init();
    // test_init();

    void test_output();
    test_output();

    void test_function();
    // test_function();

    return 0;
}


void test_init()
{
    /*定义字符数组时对所有元素进行初始化*/
    char a[10] = {'I', ' ', 'a', 'm', ' ', 'h', 'a', 'p', 'p', 'y'};
    /*初始化时，未指定的元素默认值为空字符，即'\0'*/
    //char b[10] = {'I', ' ', 'a', 'm', ' ', 'h'};
    /*如果初始化时指定了全部的元素值，定义时可以省略数组长度*/
    //char c[] = {'I', ' ', 'a', 'm', ' ', 'h', 'a', 'p', 'p', 'y'};
    /*可以直接使用一个字符串常量来对字符数组进行初始化*/
    //char d[] = {"I am happy"};
    /*用字符串常量初始化是可以省略括号*/
    //char e[] = "I am happy";

    int i, j;
    for(i=0; i<11; i++)
        printf("%c", a[i]);
    printf("\n");

    /*字符数组也可以定义二维的，详见二维数组部分*/
}


void test_output()
{
    char a[10] = {'I', ' ', 'a', 'm', ' ', 'h', 'a', 'p', 'p', 'y'};
    /*c格式符输出一个字符*/
    printf("%c\n", a[0]);
    /*s格式符用来输出一个字符串*/
    printf("%s\n", a);

    /*输出中文字符*/
    char b[100] = "这是一段中文字符串";
    //不能像英文字符一样逐个输出，否则会显示乱码
    for(int i = 0; i < 10; i++)
    {
        printf("%c\n", b[i]);
    }
    //按字符串整个输出，会正常显示为中文
    printf("%s\n", b);
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


void test_function()
/*C库函数提供了很多用来处理字符串的函数*/
//注意：这些函数是由string.h库提供的
{
    char str1[] = "I am happy";
    char str2[] = "Hello World";

    //strcat(str1, str2)函数将str2拼接到str1的后面，返回str1的地址
    //备注：没有找到preappend方式添加的函数，如果想要在字符串前面添加另一个字符串，把两个参数位置对调
    printf("%s\n", strcat(str1, str2));

    //strncat(str1, str2, n)函数将str2的前n个字符拼接到str1的后面，返回str1的地址

    // strcpy(str1, str2)函数将str2复制到str1中去，str1的原数据被抹去，返回str1的地址
    // char* strcpy(char* strDestination, const char* strSource);
    // strcpy函数常用来对字符数组进行整体赋值
    printf("%s\n", strcpy(str1, "test"));

    // strncpy(str1, str2, n)函数将str2的前n个字符复制到str1中去，str1的原数据被抹去，返回str1的地址
    printf("%s\n", strncpy(str1, "good", 2));

    // strcmp(str1, str2)函数比较str1和str2，对字符串自左至右按ASCII码值大小比较，以第一个不同的字符为准
    // 若str1=str2，函数值为0；若str1>str2，函数值为正整数1；若str1<str2，函数值为负整数-1
    // 注意：1和-1的布尔值都是True，因此函数返回值不能直接用来判断真假
    printf("%d\n", strcmp("china", "chima"));
    if(strcmp("china", "chima") > 0)
        printf("yes\n");
    
    // strlen(str1)函数返回str1的长度，注意：长度是指字符串的实际长度，不包括'\0'在内
    printf("%d\n", strlen("this is a length test"));

    // strlwr(str1)函数将字符串中所有字母小写，返回str1的地址
    printf("%s\n", strlwr(str2));

    // strupr(str1)函数将字符串中所有字母大写，返回str1的地址
    printf("%s\n", strupr(str2));

    /*其他函数待补充.....
}