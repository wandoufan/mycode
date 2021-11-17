#include <iostream>
using namespace std;

/*枚举作为类的一个成员变量*/

class Test
{
public:
	enum week
	{
		Sun, 
		Mon,
		Tue, 
		Wed, 
		Thu, 
		Fri, 
		Sat
	};
	void show()
	{
		cout << Mon << endl;
	}
};

int main()
{
	Test test;
	//访问枚举元素
	cout << test.Sun << endl;//通过对象访问枚举中的一个元素
	test.show();//通过成员函数访问枚举中的一个元素
	/*
	注意：实际测试发现，虽然没有把枚举声明为static，但仍然可以通过如下方法访问元素
	类似于静态成员变量
	*/
	cout << Test::Sun << endl;

	return 0;
}