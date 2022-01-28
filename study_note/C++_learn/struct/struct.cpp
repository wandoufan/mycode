#include <stdio.h>
# include <iostream>
using namespace std;

/*整理总结C++中结构体的基本用法*/

/*
1. C语言的结构体中只有属性，没有方法，C++的结构体中可以包含成员函数，但也极少这么做
2. C++的结构体中可以写构造函数和析构函数，用来初始化结构体和删除结构体
*/


void struct_init_1()//使用构造函数的结构体
{
    struct Student
    {
        Student(int n = 1001, float s = 90.0)
        {
            id = n;
            score = s;
        }
        int id;
        float score;
    }student_1;//使用默认参数的结构体变量
    cout << student_1.id << endl;
    cout << student_1.score << endl;
    struct Student student_2(1003, 85.5), student_3(1003, 98.5);//使用自定义参数的结构体变量
    cout << student_2.id << endl;
    cout << student_2.score << endl;
    cout << student_3.id << endl;
    cout << student_3.score << endl;
}


int main()
{
	struct_init_1();

	return 0;
}