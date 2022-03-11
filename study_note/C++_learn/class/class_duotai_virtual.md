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


## 虚函数(virtual)
1. 基本概念
为了解决上面的问题，让基类指针能够访问派生类的成员函数，C++增加了虚函数  
在函数声明前面增加virtual关键字，函数定义处可以加也可以不加  
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
	void show() override;//在子类中，用override声明要重写，这里就不必再声明virtual
};

Student::Student(int a, float s):People(a), m_score(s){}
void Student::show()//对虚函数进行重新定义
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


## 纯虚函数(pure virtual)
1. 基本概念
纯虚函数是在基类中声明的虚函数，一般用于抽象类中  
纯虚函数在基类中没有定义，但要求任何派生类都要定义自己的实现方法  
纯虚函数只有函数的名字而不具备函数的功能，不能被调用  
使用纯虚函数是为了标识一个规范的函数名字，确保每个派生类中接口的名字相同  
2. 基本格式
纯虚函数没有函数体，只做声明，不做具体定义  
纯虚函数名后面要加上'= 0'，不代表函数返回值为0，只是告诉编译系统这是一个纯虚函数  
备注：纯虚函数前面也是用'virtual'来进行标识  
3. 注意事项
在派生类中对基类的纯虚函数进行重写时，以下必须和基类的纯虚函数完全一致，否则会报错  
```
函数名、函数返回类型、函数参数的个数、类型、顺序、是否为const、是否为static
```
4. 细节说明
如果在一个抽象基类中声明了纯虚函数，但派生类中没有对其进行定义，则该纯虚函数在派生类中仍然为纯虚函数  
也就是说，如果抽象基类中声明了多个纯虚函数，则在派生类中需要对所有的纯虚函数都进行定义  
否则，派生类中也会包含未定义的纯虚函数，此时的派生类也是一个抽象类  
5. 代码示例
```
class Person//抽象基类
{
public:
	virtual void print(int id) = 0;//纯虚函数的声明
};

class Teacher:public Person
{
public:
	void print(int id)//在派生类中对纯虚函数做出具体定义
	{
		cout << "id : " << id << endl;
		cout << "this is a teacher" << endl;
	}
};

class Student:public Person
{
public:
	void print(int id)//在派生类中对纯虚函数做出具体定义
	{
		cout << "id : " << id << endl;
		cout << "this is a student" << endl;
	}
};

int main()
{
	Teacher teacher;
	teacher.print(10);
	Student student;
	student.print(20);
	return 0;
}
```

## 抽象类
1. 基本概念
如果类中至少有一个函数被声明为纯虚函数，则这个类就是抽象类  
抽象类一般用作基类，用于被其派生类继承  
抽象类不能用作参数类型、函数返回类型或显式转换的类型  
2. 引入原因
很多情况下，基类本身生成对象是不合理的  
例如，动物作为一个基类可以派生出老虎、孔雀等子类，但动物本身不能生成对象  
3. 使用方式
抽象类只能作为基类，不能去定义一个抽象类的实例化对象  
但可以定义一个抽象类的指针，让该指针可以指向它的派生类对象，进而实现多态性  
4. 代码示例
通过抽象类指针可以访问派生类中定义的纯虚函数，但无法访问派生类中新定义的函数  
```
class Person//抽象基类
{
public:
	virtual void print(int id) = 0;//纯虚函数的声明
};

class Teacher:public Person
{
public:
	void print(int id)//在派生类中对纯虚函数做出具体定义
	{
		cout << "id : " << id << endl;
		cout << "this is a teacher" << endl;
	}
	void teach()//派生类中新定义的函数
	{
		cout << "teaching" << endl;
	}
};

class Student:public Person
{
public:
	void print(int id)//在派生类中对纯虚函数做出具体定义
	{
		cout << "id : " << id << endl;
		cout << "this is a student" << endl;
	}
	void study()//派生类中新定义的函数
	{
		cout << "studying" << endl;
	}
};

int main()
{
	Teacher teacher;
	teacher.print(10);
	teacher.teach();
	Student student;
	student.print(20);
	student.study();

	Person *person;//抽象基类的对象指针
	//错误写法：直接用基类指针去调用纯虚函数
	// person -> print(0);
	//正确写法：把基类指针指向子类对象，然后再调用子类对象中定义的纯虚函数
	person = &teacher;
	person -> print(1);
	person = &student;
	person -> print(2);
	//错误写法：用基类指针去调用派生类中新定义的函数
	// person -> study();

	return 0;
}
```


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

