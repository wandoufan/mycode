# include<stdio.h>

/*关于const关键字*/

/*
https://www.runoob.com/w3cnote/cpp-const-keyword.html
1. const是C语言和C++的关键字，const是constant的缩写，表示不变的
const可以用来修饰内置变量类型、自定义对象、成员函数、返回值和函数参数
const可以指定一个语义约束，使被修饰对象保持不变，编译器会强制实施这个约束
2. 太麻烦了。。。晚点补充
*/


void test1()
{
	// const修饰普通类型的变量
	const int a = 1; // const把变量a定义为一个常量
	int b = a; // 可以把a赋值给其他变量
	// a = 2; // 不能再对a进行修改，否则会报错
}

void test2()
{
	// const修饰指针变量
}


int main()
{
	test1();
	test2();
	return 0;
}