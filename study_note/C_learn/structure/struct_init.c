#include <stdio.h>

/*整理总结C语言中结构体的基本用法*/

/*
1.结构体：将不同类型但相互联系的数据组合起来，方便整体引用(类似于python中的类class)
2."struct student"是用户自己定义的类型名，和int、float、char的作用是一样的
3.声明结构体类型时不会分配内存，在实例化出一个结构体变量后才会分配对应的内存
4.结构体成员也可以是一个结构体变量，即结构体变量可以嵌套使用，例如：
typedef struct student
{
    int num;
    float score;
    struct student * next;
}STUDENT;
注意：在结构体中声明一个结构体成员时，不能用typedef指定的新类型名STUDENT来声明
因为此时STUDENT还没有被定义出来，非法操作：STUDENT * next;

5.结构体内算作一个单独的作用域，即结构体成员的变量名可以和结构体外的变量名相同，不会产生冲突
6.通过成员运算符"."来引用结构体变量中的成员，在所有运算符中优先级最高
如果成员本身也是一个结构体变量则可以多级引用，如student_1.birthday.month
7.不能把结构体变量当做一个整体进行输入输出(也没有结构体对应的格式符)，只能逐个引用结构体变量中的成员
8.定义时没有指定长度的数组称为"flexible array"，如char name[];，
一个结构体中最多只能有一个这样的数组，并且这个数组一定要是结构体的最后一个成员
9.C语言中的结构体只有属性，没有方法，这一点和python、C++不一样，后者都是既有属性又有方法
*/


int main()
{
    void struct_define_1();
    struct_define_1();

    void struct_define_2();
    struct_define_2();

    void struct_define_3();
    struct_define_3();

    void struct_init_1();
    struct_init_1();

    void struct_init_2();
    struct_init_2();

    return 0;
}


void struct_define_1()
/*先声明结构体类型，再定义结构体变量*/
{
    struct student
    {
        int num;
        char name[20];
        char sex;
        int age;
        float score;
    }; /*要注意结构体的括号后边有分号*/

    struct student student_1, student_2;
}


void struct_define_2()
/*在声明结构体类型的同时定义结构体变量*/
{
    struct student
    {
        int num;
        char name[20];
        char sex;
        int age;
        float score;
    }student_1, student_2;
}


void struct_define_3()
/*直接定义结构体变量，不用写出结构体名*/
{
    struct
    {
        int num;
        char name[20];
        char sex;
        int age;
        float score;
    }student_1, student_2;
}


void struct_init_1()
/*在定义结构体变量时就对变量进行初始化*/
{
    struct student
    {
        int num;
        char name[20];
        char sex;
        int age;
        float score;
    }student_1 = {1001, "li ming", 'M', 16, 90.0};
    printf("%d, %s, %c, %d, %.1f\n", student_1.num, student_1.name, \
        student_1.sex, student_1.age, student_1.score);
}


void struct_init_2()
/*先定义结构体变量，再对结构体成员逐个赋值*/
{
    struct student
    {
        int num;
        char name[20];       
        char sex;
        int age;
        float score;
        
    }student_2;
    student_2.num = 1002;
    /*注意：字符数组定义后就不能直接整体赋值，非法操作：student_2.name = {"Han mei"}*/
    strcpy(student_2.name, "Han mei"); 
    student_2.sex = 'F';
    student_2.age = 18;
    student_2.score = 80.0;
    printf("%d, %s, %c, %d, %.1f\n", student_2.num, student_2.name, student_2.sex, student_2.age, student_2.score);
}