# include <stdio.h>
# include <iostream>
# include <string>
using namespace std;


void grammer_string()
{
	/*
	想要实现多行文本的字符串，且不用添加换行符\n
	在python中可以使用三引号'''来实现多行文本
	在C++ 11中提供了R"(...)"来实现该功能
	备注：在有的文本编辑器中可能无法识别到R"(...)"，导致无法给字符串上色
	*/
	string s1;
	s1 = R"(
	this is line1,
	this is line2,
	this is line3,
	this is line4.
	)";
	cout << s1 << endl;
}


int main()
{
	grammer_string();
	return 0;
}

