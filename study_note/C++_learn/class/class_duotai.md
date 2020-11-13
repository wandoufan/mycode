# C++中的多态和虚函数

## 用指针访问对象的问题
在C++中，用基类指针访问其派生类的成员时，会存在一个问题：  
通过基类指针只能访问派生类的成员变量，但是不能访问派生类的成员函数  
```
class People
{
public:
	People(int a)
	{
		age = a;
	}
	int age;
	void show()
	{
		cout << "年龄是：" << age << endl;
	}
};

class Student:public People
{
public:
	Student(int a, float s);
	float score;
	void show()
	{
		cout << "成绩是：" << score << endl;
	}
};
Student::Student(int a, float s):People(a), score(s){}

int main()
{
	People *p1; //p1是基类指针
	People peo1(15);
	Student stu1(18, 90.5);
	p1 = &peo1;
	p1 -> show(); //调用的是People类的show()函数
	p1 = &stu1;
	p1 -> show(); //调用的还是People类的show()函数
}
```


## 虚函数
1. 基本概念
为了解决上面的问题，让基类指针能够访问派生类的成员函数，C++增加了虚函数（Virtual Function）  
在函数声明前面增加virtual关键字，函数定义处可以加也可以不加  
```
class People
{
public:
	People(int a)
	{
		age = a;
	}
	int age;
	virtual void show() //声明为虚函数
	{
		cout << "年龄是：" << age << endl;
	}
};

class Student:public People
{
public:
	Student(int a, float s);
	float score;
	virtual void show() //声明为虚函数，子类中也可以不写virtual关键字
	{
		cout << "成绩是：" << score << endl;
	}
};
Student::Student(int a, float s):People(a), score(s){}

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
2. 虚函数的原理
通过指针调用普通的成员函数时会根据指针的类型（通过哪个类定义的指针）来判断调用哪个类的成员函数  
但虚函数与此不同，虚函数是根据指针的指向来调用的，指针指向哪个类的对象就调用哪个类的虚函数  
3. 虚函数的作用
有了虚函数，基类指针指向基类对象时就使用基类的成员，指向派生类对象时就使用派生类的成员  
多态是面向对象编程的主要特征之一，C++中虚函数的唯一用处就是构成多态  


## 虚函数的注意事项
1. 可以只将基类中的函数声明为虚函数，这样所有派生类中具有遮蔽关系的同名函数都将自动成为虚函数  
2. 构造函数不能是虚函数，派生类不继承基类的构造函数，将构造函数声明为虚函数没有什么意义  
3. 析构函数可以声明为虚函数，而且有时候必须要声明为虚函数  


## 多态
1. 基本概念
同一条语句可以执行不同的操作，看起来有不同表现方式，这就是多态（Polymorphism）  
例如，在上述过程中'p1 -> show()'，基类指针p1指向对象不同时，调用的成员函数也不同  
2. 多态的作用
可以通过基类指针对所有派生类（包括直接派生和间接派生）的成员变量和成员函数进行全方位的访问，尤其是成员函数  
如果没有多态，我们只能访问到派生类成员变量  
对于具有复杂继承关系的大中型程序，多态可以增加其灵活性，让代码更具有表现力  
如果类的继承关系很简单，那么多态的作用就很小  
3. 通过引用来实现多态
引用和指针功能类似，不仅指针可以实现多态，引用也能实现多态  
但引用不像指针灵活，指针可以随时改变指向，而引用只能指代固定的对象  
```
int main()
{
	People peo1(15);
	Student stu1(18, 90.5);
	People &refer_peo1 = peo1;
	Student &refer_stu1 = stu1;
	refer_peo1.show(); //调用的是People类的show()函数
	refer_stu1.show(); //调用的是Student类的show()函数
}
```


## 构成多态的条件
1. 必须存在继承关系  
2. 继承关系中必须有同名的虚函数，并且它们是覆盖关系（函数原型相同）  
3. 存在基类的指针，且通过该指针调用虚函数  