# include <stdio.h>
# include <iostream>
using namespace std;

/*类中的静态成员*/

class CSum
{
public:
	CSum(int a = 0, int b = 0) //构造函数
	{
		number_private += a + b;
	}
	int getSum()
	{
		return number_private;
	}
	void setSum(int sum)
	{
		number_private = sum;
	}
	static int number_public; //用static声明公有静态成员变量
private:
	static int number_private; //用static声明私有静态成员变量
};
int CSum::number_public = 1; //对公有静态成员变量初始化赋值
int CSum::number_private = 0; //对私有静态成员变量初始化赋值

void static_variable()
{
	CSum one(10, 2), two;
	//一个对象设置了静态成员变量，另一个对象也可以访问到相同的值
	cout << one.getSum() << endl; //12
	cout << two.getSum() << endl; //12
	two.setSum(5);
	//一个对象修改了静态成员变量，另一个对象也可以访问到相同的值
	cout << one.getSum() << endl; //5
	cout << two.getSum() << endl; //5
	cout << one.number_public << endl; //通过对象来访问公有静态成员变量
	cout << CSum::number_public << endl; //通过对象来访问公有静态成员变量
}

int main()
{
	static_variable();
	return 0;
}
