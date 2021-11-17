# 函数重写override

## 基本概念
函数重写是指在子类中，对基类中定义的虚函数或纯虚函数进行重新定义  
在函数声明时，在后面加上override关键字，即表示这个函数需要被重写  


## 注意事项
1. 在派生类中对基类的纯虚函数进行重写时，以下必须和基类的纯虚函数完全一致，否则会报错  
```
函数名、函数返回类型、函数参数的个数、类型、顺序、是否为const、是否为static
```
2. 在重写函数声明时，不加上override也不会报错，但还是推荐加上override关键字  


## 函数重载overload与函数重写override
1. 这两个概念的名字比较接近，但并没有关系，即函数重载和是否有virtual修饰无关  
2. 函数重载中要求每个函数参数不一致，返回类型可以不同  
但函数重写的几个函数要求返回类型和函数参数必须完全一致  
3. 函数重载中的若干个同名函数必须都在一个作用域下
但函数重写的几个函数分别位于不同的类中，不在同一个作用域  


## 对虚函数进行重载
1. 基本说明
虚函数在基类中可能已经做过定义，但在子类中也可以根据需要重新进行定义  
2. 代码示例
```
class People
{
public:
	int m_age;
	People(int a)
	{
		m_age = a;
	}
	
	virtual void show() //在基类中，声明为虚函数
	{
		cout << "年龄是：" << m_age << endl;
	}
};

class Student:public People
{
public:
	float m_score;
	Student(int a, float s);
	void show() override;//在子类中，对虚函数进行重写，这里就不必再声明virtual
};

Student::Student(int a, float s):People(a), m_score(s){}
void Student::show()
{
	cout << "年龄是：" << m_age << ", "<< "成绩是：" << m_score << endl;
}

int main()
{
	People *p1; //p1是基类指针
	People peo1(15);
	Student stu1(18, 90.5);
	p1 = &peo1;
	p1 -> show(); //调用的是People类的show()函数
	p1 = &stu1;
	p1 -> show(); //调用的是Student类的show()函数
}
```

## 对纯虚函数进行重载
1. 基本说明
纯虚函数在基类中只有声明，没有定义，因此在子类中要使用该函数就必须自己做出具体定义  
2. override的作用
在重写函数声明时，不加上override也不会报错，但还是推荐加上override关键字  
如果加上了override，在函数定义写错参数时，甚至是忘了定义函数时，编译器会给出报错提示  
如果没有加上override，在写错函数参数时，编译器会误认为是定义了一个新函数，没有相关提示，很难发现错误  
3. 没有加上override的代码示例
父类中纯虚函数的参数是int型，而子类在重写时错写为了float型，而编译器没有给出相应的提示  
```
class Person//抽象基类
{
public:
	virtual void print(int id) = 0;//纯虚函数的声明
};

class Student:public Person
{
public:
	void print(float id);//对基类中的纯虚函数进行重写
};

void Student::print(float id)
{
	cout << "id : " << id << endl;
	cout << "this is a student" << endl;
}
```
4. 加上了override的代码示例
父类中纯虚函数的参数是int型，而子类在重写时错写为了float型，而编译器会给出相应的提示  
```
class Person//抽象基类
{
public:
	virtual void print(int id) = 0;//纯虚函数的声明
};

class Student:public Person
{
public:
	void print(float id) override;//对基类中的纯虚函数进行重写
};

void Student::print(float id)
{
	cout << "id : " << id << endl;
	cout << "this is a student" << endl;
}
```
此时，编译器会报错：
```
error: 'void Student::print(float)' marked 'override', but does not override
```