#include<iostream>
#include<string>
using namespace std;


class Student1
{
public:
	Student1(int a, int b, float c)
	{
		id = a;
		age = b;
		score = c;
	}
	int id;
	int age;
	float score;

	void get_id() const  //用const修饰一个成员方法，const放在后面
	{
		cout << id << endl;
	}
	void get_age()
	{
		cout << age << endl;
	}
	void get_score() const; //声明时要加上const
};
void Student1::get_score() const  //定义时也要加上const
{
	cout << score << endl;
}

class Student2
{
public:
	Student2(int my_a, int my_c);
	const int a;
	int b;
private:
	const int c;
	int d;
};
Student2::Student2(int my_a, int my_c):a(my_a), c(my_c)
{
	cout << "用初始化列表来初始化const成员变量" << endl;
}

void test_init()
{
	Student2 stu(1, 3);
	cout << stu.a << endl;
}

void test_object()
{
	const Student1 zhang(1, 16, 95.5); //获取一个常对象
	cout << zhang.age << endl; //常对象的成员变量可以访问
	// zhang.age = 17; //常对象的成员变量不可以修改，否则报错
	zhang.get_id(); //常对象的const成员方法可以访问
	// zhang.get_age(); //常对象的非const成员方法不可以访问，否则报错
}

void test_pointer1()
{
	int a = 1, b = 2;
	const int *p1 = &a; //p1指针指向变量a，即a是const的
	// *p1 = 2; //不能修改p1指针指向变量的值，否则报错
	p1 = &b; //p1指针指向变量b，即指针本身的值可以改变
	// 另一种写法
	int const *p2 = &a;
	// *p2 = 2;
	p2 = &b;
}

void test_pointer2()
{
	int a = 1, b = 2;
	int * const p1 = &a; //p1指针指向变量a，即p1本身是const的
	*p1 = 2; //可以修改p1指针指向变量的值
	// p1 = &b; //不能修改指针本身的值
	// int * const p2; //注意：声明常指针时必须进行初始化，否则报错
}

void test_pointer3()
{
	int a = 1, b = 2;
	const int * const p1 = &a; //常指针p1指向常量a
	// p1 = &b; //指针本身不能修改，否则报错
	// *p1 = 2; //指向对象不能修改，否则报错
	// const int * const p2; //注意：声明常指针时必须进行初始化，否则报错
}

int main()
{
	// test_object();
	// test_pointer1();
	// test_pointer2();
	// test_pointer3();
	test_init();
}