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
	void setSum(int num)
	{
		number_private = num;
	}
	static void change_public(int num); //用static声明公有静态成员方法
	static void change_private(int num); //用static声明私有静态成员方法
	static int number_public; //用static声明公有静态成员变量
private:
	static int number_private; //用static声明私有静态成员变量
};
int CSum::number_public = 1; //对公有静态成员变量初始化赋值
int CSum::number_private = 0; //对私有静态成员变量初始化赋值

void CSum::change_public(int num) //在类外部对公有静态方法进行定义
{
	number_public = num;
}

void CSum::change_private(int num) //在类外部对公有静态方法进行定义
{
	number_private = num;
}

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
	cout << one.number_public << endl; //通过对象名来访问公有静态成员变量
	cout << CSum::number_public << endl; //通过类名来访问公有静态成员变量
}

void static_func()
{
	CSum::change_public(3); //通过类名访问公有静态成员方法
	cout << CSum::number_public << endl; //3
	CSum three;
	three.change_public(4); //通过对象名来访问公有静态成员方法
	cout << CSum::number_public << endl; //4
	three.change_private(7);
	cout << three.getSum() << endl;
}

int main()
{
	static_variable();
	static_func();
	return 0;
}
