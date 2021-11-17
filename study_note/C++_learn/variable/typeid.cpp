# include <stdio.h>
# include <typeinfo>
# include <iostream>
using namespace std;

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