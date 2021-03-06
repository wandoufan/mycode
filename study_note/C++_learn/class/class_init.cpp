# include <stdio.h>
# include <iostream>
using namespace std;

/*类的初始化*/

//定义一个类
class CMeter
{
public:
	double m_nPercent; //声明一个公有成员变量
	void StepIt(); //声明一个公有成员方法
	void SetPos(int nPos); //声明一个公有成员方法
	void get_print();
	int GetPos() //声明并定义一个公有成员方法
	{
		return m_nPos;
	}
private:
	int m_nPos; //声明一个私有成员变量
	void print(); //声明一个私有成员方法
};

void CMeter::StepIt() //在类的外部定义类的公有成员方法
{
	m_nPos++;
}

void CMeter::SetPos(int nPos) //在类的外部定义类的公有成员方法
{
	m_nPos = nPos;
}

void CMeter::get_print() //在类的外部定义类的公有成员方法
{
	print(); //通过类的公有方法来调用类的私有方法
}

void CMeter::print() //在类的外部定义类的私有成员方法
{
	cout << "this is a private test" << endl;
}

//实例化对象
void class_init()
{
	CMeter myMeter, * Meter, Meters[2]; //对象可以是普通对象、指针对象、数组对象
	myMeter.m_nPercent = 3.14; //普通对象访问成员变量
	myMeter.SetPos(2); //普通对象访问成员方法
	Meters[0].m_nPercent = 1.98; //数组对象访问成员变量
	Meter = &Meters[1]; //将指针指向数组的第二个元素
	Meter -> m_nPercent = 0.98; //通过指针访问成员时只能使用'->'
	cout << Meter -> m_nPercent << endl;
}

//私有方法测试
void private_test()
{
	CMeter myMeter;
	myMeter.get_print();
}


int main()
{
	// class_init();
	private_test();
	return 0;
}
