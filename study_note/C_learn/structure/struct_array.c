#include <stdio.h>

/*整理总结C语言中结构体数组的基本用法*/

/*
1.一个结构体变量可以存放一组数据，如一个学生的个人信息，但如果存放很多组数据(全班学生的信息)，就需要使用结构体数组
2.结构体数组与其他常规数组的区别：每个数组元素都是一个结构体类型的变量
*/


int main()
{
    void struct_array_define_1();
    struct_array_define_1();

    void struct_array_define_2();
    struct_array_define_2();

    void struct_array_define_3();
    struct_array_define_3();

    void struct_array_init_1();
    struct_array_init_1();

    void struct_array_init_2();
    struct_array_init_2();

    return 0;
}


void struct_array_define_1()
/*先声明结构体类型，再定义结构体数组变量*/
{
    struct student
    {
        int num;
        char name[20];
        char sex;
        int age;
        float score;
    }; /*要注意结构体的括号后边有分号*/

    struct student student_array[3];
}


void struct_array_define_2()
/*在声明结构体类型的同时定义结构体数组变量*/
{
    struct student
    {
        int num;
        char name[20];
        char sex;
        int age;
        float score;
    }student_array[3];
}


void struct_array_define_3()
/*直接定义结构体数组变量，不用写出结构体名*/
{
    struct    
    {
        int num;
        char name[20];
        char sex;
        int age;
        float score;
    }student_array[3];
}


void struct_array_init_1()
/*定义结构体数组变量时就对变量进行初始化*/
{
    struct student
    {
        int num;
        char name[20];
        char sex;
        int age;
        float score;
    /*数组的元素个数可以省略*/
    }student_array[] = {{1001, "li ming", 'M', 16, 90.0}, \
    {1002, "zhang", 'F', 15, 80.0}, {1003, "wang", 'M', 17, 70.0}};
    /*引用结构体数组中的元素*/
    printf("%d, %s, %c, %d, %.1f\n", student_array[0].num, student_array[0].name, \
        student_array[0].sex, student_array[0].age, student_array[0].score);
    printf("%d, %s, %c, %d, %.1f\n", student_array[1].num, student_array[1].name, \
        student_array[1].sex, student_array[1].age, student_array[1].score);
    printf("%d, %s, %c, %d, %.1f\n", student_array[2].num, student_array[2].name, \
        student_array[2].sex, student_array[2].age, student_array[2].score);
}


void struct_array_init_2()
/*先定义结构体数组变量，再对变量进行初始化*/
{
    struct student
    {
        int num;
        char name[20];
        char sex;
        int age;
        float score;
    };
    struct student student_array[3] = {{1001, "li ming", 'M', 16, 90.0}, \
    {1002, "zhang", 'F', 15, 80.0}, {1003, "wang", 'M', 17, 70.0}};
    /*引用结构体数组中的元素*/
    printf("%d, %s, %c, %d, %.1f\n", student_array[0].num, student_array[0].name, \
        student_array[0].sex, student_array[0].age, student_array[0].score);
    printf("%d, %s, %c, %d, %.1f\n", student_array[1].num, student_array[1].name, \
        student_array[1].sex, student_array[1].age, student_array[1].score);
    printf("%d, %s, %c, %d, %.1f\n", student_array[2].num, student_array[2].name, \
        student_array[2].sex, student_array[2].age, student_array[2].score);
    /*也可以用循环进行输出*/
    for(int i = 0; i < 3; i++)
    {
        printf("%d, %s, %c, %d, %.1f\n", student_array[i].num, student_array[i].name, \
        student_array[i].sex, student_array[i].age, student_array[i].score);
    }
}