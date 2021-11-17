# this指针

## 基本概念
this是C++中的一个关键字，也是一个const指针，它时刻指向当前对象，通过它可以访问当前对象的所有成员  
this指针是所有成员函数的隐含参数，不用自己写这个参数，也看不见这个参数  
当调用一个对象的成员函数时，编译器先将对象地址赋给this指针，然后调用成员函数  
备注：this指针就相当于python中类的成员方法的self参数  


## 注意事项
1. this指针是一个仅能被类的非静态成员函数所访问的特殊指针，即静态成员方法不能使用this指针  
this指针只能在类的非静态成员函数的内部使用，超出这个范围编译器就搞不清this指向谁了  
2. 友元函数没有this指针，因为友元不是类的成员，只有成员函数才有this指针  


## 代码示例
实际测试，不管成员函数定义在类内部还是类外部，不管是否用this指针，都可以正常访问成员变量
```
class Test
{
public:
	Test(int number)
	{
		m_number = number;
	}
	int m_number;
	void show1()//在类内部定义，不用this指针
	{
		cout << m_number << endl;
	}
	void show2()//在类内部定义，用this指针
	{
		cout << this -> m_number << endl;
	}
	void show3();
	void show4();
};

void Test::show3()//在类外部定义，不用this指针
{
	cout << m_number << endl;
}

void Test::show4()//在类外部定义，用this指针
{
	cout << this -> m_number << endl;
}

int main()
{
	Test test1(1);
	test1.show1();
	test1.show2();
	test1.show3();
	test1.show4();
	return 0;
}
```