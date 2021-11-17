# 类的继承与派生

## 基本概念
继承（Inheritance）是一个类从另一个类获取成员变量和成员函数的过程  
派生（Derive）和继承是一个概念，只是站的角度不同  
继承是儿子接收父亲的产业，派生是父亲把产业传承给儿子  
被继承的类称为父类或基类，继承的类称为子类或派生类  
子类和父类通常放在一起称呼，基类和派生类通常放在一起称呼  


## 使用场景
1. 当你创建的新类与现有的类相似，只是多出若干成员变量或成员函数时，可以使用继承，这样不但会减少代码量，而且新类会拥有基类的所有功能  
2. 当你需要创建多个类，它们拥有很多相似的成员变量或成员函数时，也可以使用继承  
可以将这些类的共同成员提取出来，定义为基类，然后从基类继承，既可以节省代码，也方便后续修改成员  


## 注意事项
1. 当派生类和基类在不同的命名空间时，在基类名前要加上命名空间的名字
```
class Student:public NAMESPACE1 People
```


## 使用示例
继承的一般语法格式为：  
```
class 派生类名:［继承方式］ 基类名
{
    派生类新增加的成员
};
```
代码示例：  
```
class People//基类
{
public:
	int m_age;
	char m_name;
	void set(int age, char name)
	{
		m_age = age;
		m_name = name;
	}
	void show_people()
	{
		cout << "年龄是：" << m_age << endl;
		cout << "姓名是：" << m_name << endl;
	}
};

class Student:public People//子类
{
public:
	float m_score;
	void set(int age, char name, float score)
	{
		m_age = age;
		m_name = name;
		m_score = score;
	}
	void show_student()
	{
		cout << "年龄是：" << m_age << endl;
		cout << "姓名是：" << m_name << endl;
		cout << "成绩是：" << m_score << endl;
	}
};

int main()
{
	//初始化
	People peo1;
	peo1.set(15, 'a');
	peo1.show_people();
	Student stu1;
	stu1.set(18, 'b', 90.5);
	stu1.show_student();
	//子类调用父类的成员变量
	cout << stu1.m_age << endl;
	stu1.m_name = 'c';
	stu1.show_student();
	//子类调用父类的成员函数
	stu1.show_people();
}
```


## 继承方式
继承方式包括：public、private、protected，如果不写，则默认为private  
其中，基类中的protected成员可以在派生类中使用，而基类中的private成员不能在派生类中使用  
注意：基类的private成员在派生类只是不能使用，不是不能继承，private成员仍然占据派生类对象的内存，只是不可见了  
备注：private和protected会导致继承关系复杂，实际开发中一般只使用public方式  
1. public继承方式
基类中所有public成员在派生类中为public属性  
基类中所有protected成员在派生类中为protected属性  
基类中所有private成员在派生类中不能使用  
2. protected继承方式
基类中的所有public成员在派生类中为protected属性  
基类中的所有protected成员在派生类中为protected属性  
基类中的所有private成员在派生类中不能使用  
3. private继承方式
基类中的所有public成员在派生类中均为private属性  
基类中的所有protected成员在派生类中均为private属性  
基类中的所有private成员在派生类中不能使用  


## 改变访问权限
在派生类中使用using关键字可以改变基类成员在派生类中的访问权限  
例如将public改为private、将protected改为public  
using只能改变基类中public和protected成员的访问权限，不能改变private成员的访问权限  


## 继承时的成员名字冲突问题
如果父类和子类中有成员变量和成员方法重名，则默认以子类中的为准  
在子类中仍然可以调用父类的同名成员，但要加上类名和域解析符，例如'stu1.People::show()'  
注意：父类和子类中同名的成员方法不构成函数重载，而是子类遮蔽父类  
```
class People //基类People
{
public:
	void show()
	{
		cout << "这是基类People" << endl;
	}
};

class Student:public People //派生类Student
{
public:
	void show()
	{
		cout << "这是派生类Student" << endl;
	}
};

int main()
{
	Student stu1;
	stu1.show(); //这是派生类Student
	stu1.People::show(); //这是基类People
}
```


## 继承时的构造函数问题
1. 基本说明
因为父类和子类的名字都不一样，因此子类无法继承父类的构造函数  
子类从父类继承的成员变量也需要由子类的构造函数来进行初始化，因此在子类的构造函数中调用父类的构造函数，来对父类中的成员变量进行初始化  
注意：派生类构造函数中只能调用直接基类的构造函数，不能调用间接基类的  
2. 多层继承时的构造函数
继承关系为：'A --> B --> C'，C是最终派生类，此时，B称为C的直接基类，A称为C的间接基类  
如果C中调用了B的构造函数，B会自动调用A的构造函数，相当于C间接地（或者说隐式地）调用了A的构造函数  
执行顺序为：A类构造函数 --> B类构造函数 --> C类构造函数  
因此不能在C中显示地调用A的构造函数，否则就相当于A中构造函数调用了两次  
3. 示例1：基类中没有构造函数
```
class People//基类
{
public:
	int m_age;
	char m_name;
	void set(int age, char name)
	{
		m_age = age;
		m_name = name;
	}
	virtual void show() //在基类中声明为虚函数
	{
		cout << "年龄是：" << m_age << endl;
		cout << "姓名是：" << m_name << endl;
	}
};

class Student:public People//子类
{
public:
	float m_score;
	Student(int age, char name, float score)//子类构造函数
	{
		m_age = age;//对父类中的成员变量进行初始化
		m_name = name;//对父类中的成员变量进行初始化
		m_score = score;
	}
	void show() override;//在子类中对虚函数进行重写
};

void Student::show()
{
	cout << "年龄是：" << m_age << endl;
	cout << "姓名是：" << m_name << endl;
	cout << "成绩是：" << m_score << endl;
}

int main()
{
	People peo1;
	peo1.set(15, 'a');
	peo1.show();
	Student stu1(18, 'b', 90.5);
	stu1.show();
}
```
4. 示例2：基类中有构造函数，但构造函数没有参数
效果和上面一样，相当于基类没有构造函数
```
class People//基类
{
public:
	int m_age;
	char m_name;
	People()//基类构造函数
	{
		cout << "调用了基类的构造函数" << endl;
	}
	void set(int age, char name)
	{
		m_age = age;
		m_name = name;
	}
	virtual void show() //在基类中声明为虚函数
	{
		cout << "年龄是：" << m_age << endl;
		cout << "姓名是：" << m_name << endl;
	}
};

class Student:public People//子类
{
public:
	float m_score;
	Student(int age, char name, float score)//子类构造函数
	{
		m_age = age;//对父类中的成员变量进行初始化
		m_name = name;//对父类中的成员变量进行初始化
		m_score = score;
	}
	void show() override;//在子类中对虚函数进行重写
};

void Student::show()
{
	cout << "年龄是：" << m_age << endl;
	cout << "姓名是：" << m_name << endl;
	cout << "成绩是：" << m_score << endl;
}

int main()
{
	People peo1;
	peo1.set(15, 'a');
	peo1.show();
	Student stu1(18, 'b', 90.5);
	stu1.show();
}
```
5. 示例3：基类中有构造函数，且构造函数有参数
注意：这种情况下，子类必须显式的调用基类的构造函数，否则会报错  
也就是说，这种情况下，只有这一种方法可以对从父类中继承的成员变量进行初始化  
```
class People//基类
{
public:
	int m_age;
	char m_name;
	People(int age, char name)//基类构造函数
	{
		m_age = age;
		m_name = name;
		cout << "调用了基类的构造函数" << endl;
	}
	
	virtual void show() //在基类中声明为虚函数
	{
		cout << "年龄是：" << m_age << endl;
		cout << "姓名是：" << m_name << endl;
	}
};

class Student:public People//子类
{
public:
	float m_score;
	Student(int age, char name, float score);//子类构造函数
	void show() override;//在子类中对虚函数进行重写
};

//People(age, name)是显式调用基类的构造函数，m_score(score)是子类自己的初始化列表
Student::Student(int age, char name, float score):People(age, name), m_score(score)
{
	cout << "调用了子类的构造函数" << endl;
}

void Student::show()
{
	cout << "年龄是：" << m_age << endl;
	cout << "姓名是：" << m_name << endl;
	cout << "成绩是：" << m_score << endl;
}

int main()
{
	People peo1(15, 'a');
	peo1.show();
	Student stu1(18, 'b', 90.5);
	stu1.show();
}
```
实际测试，如果不调用父类的构造函数，像示例2那样直接对父类中成员变量进行初始化，会产生报错：  
```
error: no matching function for call to 'People::People()'
candidate expects 2 arguments, 0 provided
```


## 基类和派生类的析构函数
1. 基本用法
和构造函数类似，子类无法直接继承父类的析构函数  
不同的是，在派生类的析构函数中不用显式地调用基类的析构函数  
因为每个类只有一个析构函数，编译器知道如何选择，无需程序员干涉  
2. 多层继承时的析构函数
析构函数用来销毁派生类对象，因此执行顺序和构造函数刚好相反  
执行顺序为：C类析构函数 --> B类析构函数 --> A类析构函数  


## 多重继承
1. 基本概念
当派生类只有一个基类时称为单继承，派生类有多个基类时称为多继承  
使用多重继承会造成代码逻辑复杂，思路混乱，Java、C#、PHP等直接取消了多继承  
多继承一般用在大型项目中，中小型项目很少使用  
C++中虽然还支持多继承，但一般也尽量避免使用  
2. 使用方法
继承关系为：'A、 B、 C --> D'  
```
class A //基类A
{
public:
	int a;
};
class B //基类B
{
public:
	int b;
};
class C //基类C
{
public:
	int c;
};
class D : public A, private B, protected C //派生类D
{
public:
	int d;
};

```
3. 多重继承时的构造函数
多重继承形式下的构造函数要在派生类的构造函数中调用多个基类的构造函数  
调用基类构造函数的顺序和和它们在派生类构造函数中出现的顺序无关，而是和声明派生类时基类出现的顺序相同  
```
D(形参列表): A(实参列表), B(实参列表), C(实参列表){}
```
4. 多重继承时的析构函数
多继承形式下析构函数的执行顺序和构造函数的执行顺序相反  
5. 多重继承时的命名冲突
当两个或多个基类中有同名的成员时，如果直接访问该成员，就会产生命名冲突  
这个时候需要在成员名字前面加上类名和域解析符::，以显式地指明到底使用哪个类的成员  
```
D my_d;
my_d.a = 1; //D类中的a成员变量
my_d.A::a = 2; //A类中的a成员变量
```


## 虚继承和虚基类
1. 菱形继承
菱形继承关系是：'A --> B、 C --> D'，类A派生出类B和类C，类D继承自类B和类C  
菱形继承是一种典型的多重继承结构，很容易发生命名冲突  
如果类A有一个成员变量a，那么在类D中直接访问a就会产生歧义  
编译器不知道它究竟来自A-->B-->D这条路径，还是来自A-->C-->D这条路径  
需要在成员名字前面加上类名和域解析符::，以显式地指明到底使用哪个类的成员  
2. 虚继承（Virtual Inheritance）
为了解决多继承时的命名冲突和冗余数据问题，C++提出了虚继承，使得在派生类中只保留一份间接基类的成员  
在继承方式前面加上virtual关键字就是虚继承  
3. 虚基类（Virtual Base Class）
虚继承的目的是让某个类做出声明，承诺愿意共享它的基类  其中，这个被共享的基类就称为虚基类（Virtual Base Class）  
不论虚基类在继承体系中出现了多少次，在派生类中都只包含一份虚基类的成员  
4. 例子
```
class A //A是虚基类
{
protected:
	int m_a;
};
class B: virtual public A //用virtual声明虚继承
{
protected:
	int m_b;
};
class C: virtual public A //用virtual声明虚继承
{
protected:
	int m_c;
};
class D: public B, public C //派生类D
{
public:
	//通过虚继承可以直接在D中访问m_a成员变量，不用担心产生歧义
	void seta(int a){ m_a = a; }
private:
	int m_d;
};
```
5. 虚继承时的构造函数
略...  