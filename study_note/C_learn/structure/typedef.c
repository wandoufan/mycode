#include <stdio.h>

/*C语言中关键字typedef的用法*/

/*
1.除了可以直接使用C语言提供的标准类型名(int、char、float、double、long等)和自己声明的结构体
、共用体、指针、枚举类型外，还可以用typedef声明新的类型名来代替已有的类型名(相当于将类型名改名)
2.一般习惯上把typedef声明的类型名用大写字母表示，以便于和系统提供的标准类型标识符相区分
3.typedef只能用来声明类型，不能用来定义变量
4.typedef只是对已经存在的类型指定一个新的类型名，并没有创造新的类型
5.使用typedef可以提高程序的通用性和可移植性
*/


int main()
{
    typedef float REAL; /*将float类型名改名为REAL*/
    REAL a; /*用REAL来定义一个变量*/
    a = 3.14;
    printf("%.2f\n", a);

    typedef struct time
    {
        int day;
        int month;
        int year;
    }DATE; /*将typedef struct time改名为DATE，其中结构体名time可以省略*/
    DATE time_1, time_2; /*用DATE定义两个结构体变量*/
    DATE * p1; /*用DATE定义一个结构体类型的指针*/

    typedef int NUM[10]; /*声明NUM为整型数组类型*/
    NUM n; /*定义n为整型数组*/
        
    typedef char * STRING; /*声明STRING为字符指针类型*/
    STRING p2; /*定义p2为字符指针类型*/

    return 0;
}