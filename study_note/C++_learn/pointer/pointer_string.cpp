#include <stdio.h>
#include <iostream>
using namespace std;

/*C语言中用指针指向字符串*/


/*
1.在C语言中可以通过字符数组来存放一个字符串，也可以通过字符指针来指向一个字符串(不需要定义字符数组)
2.对于一个字符类型的数组，可通过引用数组名或字符指针变量来一次输出一个字符串(不是逐个输出字符)
而对于一个数值类型的数组，不能通过数组名整体输出，只能逐个引用数组元素
3.关于字符串数组和字符串指针的区别：C程序设计P257页
4.注意：指针一般不能指向一个常量，例如'int * p1 = & 1;'，整型指针指向一个整型常量是错误的
但字符串类型的指针可以指向一个字符串常量
*/


int main()
{
    void pointer_char_init();
    pointer_char_init();

    void pointer_string_init();
    pointer_string_init();

    return 0;
}


void pointer_char_init()
/*用指针指向单个字符*/
{
    char c = 'A';
    char * p;
    p = & c;
    printf("%c\n", * p);
}


void pointer_string_init()
/*用指针指向字符串*/
{
    char * string; /*注意：指向字符串的指针也是用char来进行定义*/
    string = &"I am happy";
    /*也可以直接定义为一行：char * string = "I am happy";*/
    /*注意：输出%s字符串类型时不需要有指针运算符*，输出%d整型和%c字符型时需要有指针运算符*/
    printf("%s\n", string); /*错误写法：printf("%s\n", * string);*/
}