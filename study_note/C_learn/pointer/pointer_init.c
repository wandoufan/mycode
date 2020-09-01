#include <stdio.h>

/*整理总结C语言中指针的基本用法*/

/*基本概念*/
/*
直接访问：按照变量地址存放变量值
间接访问：将变量的地址存放在另一变量中
指针：一个变量的地址称为该变量的指针
指针变量：如果一个变量专门用来存放另一个变量的地址，则称它为指针变量
*/

/*
1.指针运算符*根据地址找到对应的变量，取地址符&取出变量的地址，二者可以看做是互逆操作
2.指针变量只能通过取地址符&来存放地址，不能直接把一个整数或其他任何非地址类型的数据赋值给一个指针变量
3.*和&优先级相同，但按照自右向左的方向结合，即&*p1 = &(*p1)

4.函数参数不仅可以是int,float,char等类型，还可以是指针类型，即传递一个变量的地址到另一个函数
这样可以改变"函数只能进行单向的值传递"的特性，在被调用函数中可以实现对实参进行修改
*/


int main()
{
    void pointer_init();
    pointer_init();

    void pointer_change(int * pointer_1, int * pointer_2); /*pointer_1，pointer_2是形参*/
    int a = 1, b = 2;
    int * p1, * p2;
    p1 = & a;
    p2 = & b;
    pointer_change(p1, p2); /*p1,p2是实参*/
    // pointer_change(&a, &b);
    printf("%d, %d\n", a, b);
    printf("%d, %d\n", * p1, * p2);

    return 0;
}


void pointer_init()
/*指针的定义与引用*/
{
    int i = 1;
    /*定义指针变量：基类型 * 指针变量名;*/
    int * p1, * p2; /*定义指针变量时需要指定指针变量可以指向的变量类型*/
    p1 = & i; /*通过取地址符&将变量i的地址存放入指针变量p1中*/
    printf("%d\n", * p1);
    p2 = & * p1; /*p2等于p1所指向变量的地址对应的变量，即i*/
    printf("%d\n", * p2);
    printf("%d\n", * & i); /*代表变量i的地址对应的变量，即i本身*/
}


void pointer_change(int * pointer_1, int * pointer_2)
/*以指针作为函数参数，并通过指针改变原函数中变量的值(不需要return回传参数)*/
{
    (* pointer_1)++;
    * pointer_2 += 3;
}


