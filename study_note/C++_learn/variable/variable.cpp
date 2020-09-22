# include <stdio.h>
# include <typeinfo>
# include<iostream>  

/*关于c++中的变量类型*/

/*
1. 
*/


void test1()
{
	int a;
	cout << typeid(a).name() << endl;
}



int main()
{
	test1();
}