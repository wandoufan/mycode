# include <stdio.h>
# include <typeinfo>
# include <iostream>
using namespace std;

/*关于c++中的变量类型*/

/*
1. C++中的数据类型包括基本数据类型、派生类型、复合类型三大类
2. C++的数据类型和C语言大致相同，最主要是多了一个class类
*/


void test1()
{
// 查看变量的类型用typeid函数
// 如果用gcc编译器，输出的是变量类型的首字母
// 如果用VC++编译器，输出的是变量类型的全拼
	int a = 1;
	double b = 3.14;
	cout << typeid(a).name() << endl;
	cout << typeid(b).name() << endl;
}


int main()
{
	test1();
}