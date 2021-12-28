#include <stdio.h>
# include <iostream>
using namespace std;

/*用指针指向结构体变量*/

/*
1.一个结构体变量的指针就是该变量所占据的内存段的起始地址
2.为了方便和直观，可以用'p -> num'来代替'(* p).num'，'->'是指向运算符
*/


void struct_pointer()
/*用指针指向结构体变量*/
{
    struct student
    {
        int num;
        char name[20];
        char sex;
        int age;
        float score;
    }student_1 = {1001, "li ming", 'M', 16, 90.0};

    struct student * p; /*定义一个struct student类型的指针变量*/
    p = & student_1; /*将指针指向结构体变量*/
    /*用成员运算符'.'来引用结构体成员*/
    /*注意：成员运算符"."优先级比指针运算符"*"优先级高，所以要用括号括起来*/
    printf("%d, %s, %c, %d, %.1f\n", (* p).num, (* p).name, (* p).sex, (* p).age, (* p).score);
    /*用指向运算符'->'来引用结构体成员*/
    printf("%d, %s, %c, %d, %.1f\n", p -> num, p -> name, p -> sex, p -> age, p -> score);
}

void struct_array_pointer()
/*用指针指向结构体数组中的成员，即结构体变量*/
{
    struct student
    {
        int num;
        char name[20];
        char sex;
        int age;
        float score;
    }student_array[] = {{1001, "li ming", 'M', 16, 90.0}, \
    {1002, "zhang", 'F', 15, 80.0}, {1003, "wang", 'M', 17, 70.0}};

    struct student * p;
    p = & student_array[0]; /*也可以写为：p = student_array;*/
    for(; p < student_array + 3; p++) /*和其他数组指针一样，可以进行指针的自加操作*/
    {
        /*用指向运算符'->'来引用结构体成员*/
        printf("%d, %s, %c, %d, %.1f\n", p -> num, p -> name, p -> sex, p -> age, p -> score);
        /*用成员运算符'.'来引用结构体成员*/
        printf("%d, %s, %c, %d, %.1f\n", (* p).num, (* p).name, (* p).sex, (* p).age, (* p).score);
    }
}

int main()
{
    struct_pointer();
    struct_array_pointer();

    /*定义一个结构体指针，然后从这个指针就可以很简便的获得一个结构体数组*/
    //结构体定义
    struct CVT
    {
        int a;
        float b;
    };
    //结构体指针
    struct CVT *cvt;
    //赋值
    for(int i = 0; i < 10; i++)
    {
        cvt[i].a = i;//用指针直接获得结构体数组
        cvt[i].b = (float)i + 0.1;
    }
    //读取显示值
    for(int j = 0; j < 10; j++)
    {
        cout << j << " : " << cvt[j].a << ", " << cvt[j].b << endl;
    }

    return 0;
}

