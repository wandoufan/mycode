#include <stdio.h>

/*用结构体变量(或结构体数组)的指针作为函数参数*/

/*
将一个结构体变量的值传递给另一个函数，有3个方法：
1.直接把结构体变量的成员作为实参进行传递，如student_1.num或student_array[0].num，属于值传递
2.将整个结构体变量作为实参进行传递，对应的形参也要是相同类型的结构体变量，也属于值传递
这种传递方式内存开销很大，一般很少使用
3.将结构体变量(或结构体数组)的指针作为实参进行传递，属于地址传递，在被调用函数中可以实现对实参进行修改
*/


struct student /*作为全局变量时要定义在最上面*/
{
    int num;
    char name[20];
    char sex;
    int age;
    float score;
}student_1 = {1001, "li ming", 'M', 16, 90.0};


int main()
{
    printf("%d, %s, %c, %d, %.1f\n", student_1.num, student_1.name, \
        student_1.sex, student_1.age, student_1.score);

    void struct_change(struct student * p); /*结构体变量类型的指针作为形参*/
    struct_change(& student_1); /*结构体变量的起始地址作为实参*/

    printf("%d, %s, %c, %d, %.1f\n", student_1.num, student_1.name, \
        student_1.sex, student_1.age, student_1.score);

    return 0;
}


void struct_change(struct student * p)
/*对结构体变量的数值进行修改(不需要通过return回传参数)*/
{
    p -> num = 1002;
    strcpy(p -> name, "zhang");
}

