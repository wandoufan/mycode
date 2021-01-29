#include <stdio.h>
#include <iostream>
using namespace std;

/*整理总结C语言中指针的基本用法*/

/*基本概念*/
/*
直接访问：按照变量地址存放变量值
间接访问：将变量的地址存放在另一变量中
指针：一个变量的内存地址称为该变量的指针
指针变量：如果一个变量专门用来存放另一个变量的地址，则称它为指针变量
*/

/*
1.指针运算符*根据地址找到对应的变量，取地址符&取出变量的地址，二者可以看做是互逆操作
2.指针变量只能通过取地址符&来存放地址，不能直接把一个整数或其他任何非地址类型的数据赋值给一个指针变量
3.*和&优先级相同，但按照自右向左的方向结合，即&*p1 = &(*p1)
4.函数参数不仅可以是int,float,char等类型，还可以是指针类型，即传递一个变量的地址到另一个函数
这样可以改变"函数只能进行单向的值传递"的特性，在被调用函数中可以实现对实参进行修改
5.注意：指针一般不能指向一个常量，例如'int * p1 = & 1;'，整型指针指向一个整型常量是错误的
但字符串类型的指针可以指向一个字符串常量
*/


void pointer_init()
{
    /*指针的定义与引用*/
    int i = 1;
    // 定义指针变量：基类型 * 指针变量名;
    int * p1, * p2, * p3;
    //1. 通过取地址符&将变量i的地址存放入指针变量p1中
    p1 = & i;
    cout << *p1 << endl;
    //2. p2等于p1所指向变量的地址对应的变量，即i
    p2 = & * p1; 
    cout << *p2 << endl;
    //3. 先取i的地址，再获取地址对应的变量，最后还是i变量本身
    cout << * & i << endl;
    //4. 把一个指针赋值给另一个指针
    p3 = p2;
    cout << *p3 << endl;
    
    //以下是错误写法：
    //1. 把指针指向一个数值常量
    //*p1 = 100;
    //2. 指针指向变量时不能再带*号
    //*p1 = &i;
    
}

void pointer_change(int * pointer_1, int * pointer_2)
{
    //对指针指向变量进行修改
    (* pointer_1)++;
    * pointer_2 += 3;
}

void pointer_change_test()
{
    /*以指针作为函数参数，并通过指针改变原函数中变量的值(不需要return回传参数)*/
    int a = 1, b = 1;
    int * p1, * p2;
    p1 = & a;
    p2 = & b;
    //可以定义指向变量的指针，把指针作为函数参数
    pointer_change(p1, p2); 
    //也可以不定义指针，直接把变量的地址作为函数参数
    // pointer_change(&a, &b);
    cout << "a : " << a << endl;
    cout << "b : " << b << endl;
    cout << "*p1 : " << *p1 << endl;
    cout << "*p2 : " << *p2 << endl;
}

int main()
{
    pointer_init();
    // pointer_change_test();
    return 0;
}