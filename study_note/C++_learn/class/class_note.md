# C++中的类

## 结构体struct和类class的对比
1. class中既有成员变量又有成员方法，C语言中的struct只有成员变量，没有成员方法，
而C++中的struct类似于class，既有成员变量又有成员方法  

2. struct中成员变量默认是public的，而class中成员变量默认是private的

3. 当只需要描述数据结构而不需要在结构中对数据进行操作时，选择strcut
既需要描述数据结构，又需要描述对数据的处理方法时，选择class


## 类的说明
1. 在设计class时，一般将成员变量声明为private，大部分成员方法声明为public  
这样类以外的代码就不能直接访问类中变量，必须通过调用成员方法作为处理数据的接口  
从而实现了对内部数据的封装和隐藏，这就是C++中class的优点之一  

2. 类的定义包括声明部分(声明成员变量和成员方法)和实现部分(对成员方法进行定义)  
成员变量可以是任何类型数据，也可以是另一个类的实例化对象  
成员函数的实现部分既可以放在类的内部进行定义，也可以放在类的外部进行定义  
备注：对于在类外部定义的成员函数，在定义时必须使用域运算符'::'来告知编译系统函数所属的类  

3. 类名一般也都以大写字母开始，按驼峰命名法  

4. 类都要定义在最外层，一般不能定义在函数内部(作用域仅限函数内部，没有意义)  
而类的实例化对象一般都要写在函数内部，不能直接写在最外层  

5. . 关键字private、protected、public可以在类中出现多次，且先后顺序没有要求  
一般习惯上，先写public的成员，再写private的成员  
若类成员前面没有任何关键字修饰，则默认是private私有成员  
这一点和python不同，python中没有public和private，类成员默认都是公共的  

6. 按照书上的要求，不能在类中对成员变量赋默认值(只能声明，不能赋值)，这一点和python不同  
在Qt 5.15.2环境中测试，即使对变量赋值了编译器也不会报错，而且经常遇到代码直接就在类中对成员变量赋默认值  
但是，在Qt 5.2.1 + VS2010环境中测试，如果在类中直接对成员变量赋值，确实会报错  

7. 注意：类的成员方法不能用extern修饰符  
类的成员变量不能用auto、register、extern等修饰符，只能用static修饰符  


## 类对象的赋值
1. 类对象不能直接用'='来相互赋值
```
//错误语法
Student stu1, stu2;
...
stu1 = stu2;
```
2. 类对象指针可以用'='来相互赋值
```
//正确语法
Student *stu1, *stu2;
...
stu1 = stu2;
```


## 类的一般格式
```
class <类名>
{
	public:
//类成员都是公有的，外面程序可以直接访问
		[<共有型数据和函数>]
	private:
//外面程序无法访问，成员变量只能被类中函数使用，成员方法只允许在类中调用
//注意：声明为private的方法只能被类自己的函数调用，对象也不能直接调用，如果是外部函数调用会报错找不到
		[<私有型数据和函数>]
	protected:
//类成员是半公开的，类似private，但可以在类中或其子类中访问
//基类中的protected成员可以在派生类中使用，而基类中的private成员不能在派生类中使用
		[<保护型数据和函数>]
}; //注意：类定义的结尾也有分号;
<各个成员函数的实现>
```


## 类中的对象成员
1. 基本定义
成员变量可以是任何类型数据，也可以是另一个类的实例化对象  
当类的成员中有其他类的对象时，这个成员称为对象成员，这个类称为组合类  
2. 对象成员初始化的两种方法
2.1 和数据成员一样，对象成员也可以通过构造函数来完成初始化，即函数构造方式  
2.2 使用冒号':'来引导对象成员初始化，即对象成员列表方式  


## 类的作用域
1. 类名的作用范围是从类名开始的位置到文件结尾
一般来讲，文件作用域 > 类作用域 > 成员函数作用域  
2. 在类中使用成员时，成员声明的前后顺序不会影响到其使用
例如，类的方法可以先被调用(调用时不用事先声明)，再进行定义，这一点和类外部的普通函数不同  
```
class A
{
	void f1()
	{
		f2(); //调用类的方法f2，此时虽然f2还没有定义，但可以不用声明就直接调用
	}
	int f2()
	{
		return 1;
	}
};
```


## 构造函数
1. 基本定义
构造函数是为了在创建对象时，将对象初始化为给定值(相当于设置默认值)  
类中规定，不能在类中对成员变量赋默认值，为了能够实现设置初始值的功能，就出现了构造函数  
2. 构造函数的特点
构造函数的最大特点是创建对象时它会被自动执行，这一点类似于python类中的__init__()函数  
一般规定，构造函数名必须与其类名相同，可以带参数，也可以不带参数  
构造函数没有返回值，定义时也不用声明函数类型  
构造函数可以有多个，初始化时根据不同的参数去匹配不同的构造函数，本质是函数重载  
如果类要用于实例化对象，则构造函数必须是public，否则无法实例化  
如果类只用于派生其他类，则构造函数可以是private  
3. 默认构造函数
如果在定义类时没有定义任何构造函数，则编译器会自动为类生成一个构造函数，称为默认构造函数  
默认构造函数是隐式的，不带任何参数，也没有任何功能，主要目的是为了符合类的语法结构标准  
如果用户自己定义了构造函数，则默认构造函数就不存在了  
```
默认构造函数形式(实际上看不见，仅供了解)
CMeter ()
{}
```
4. explicit关键字和implicit关键字
这两个关键字都是专门用来修饰类的构造函数的，一般放在构造函数名称前面  
explicit表示显式的，implicit表示隐式的，在没有特别声明的情况下，类的构造函数默认为隐式的  
在C++中，构造函数实际上可以实现数据类型的自动转换，即隐式转换  
有时候隐式转换可能会出现问题，因此会使用explicit关键字来禁止隐式转换，只能进行显示转换  
备注：这两个关键字都很少用到，大致了解即可  


## 构造函数的代码示例
1. 没有参数的构造函数  
```
class Test
{
public:
	Test() //构造函数必须与类同名，没有返回类型
	{
		cout << "test" << endl;
	}
	int m_number;
};

int main()
{
	Test test1;
	/*
	注意：构造函数没有参数的类，在实例化时不要加括号
	如果加了括号也不会报错，但实际上并没有实例化出一个对象
	编译器可能误认为是调用了一个函数
	*/
	Test test2();//错误示例
}
```
2. 带有参数的构造函数  
```
class Test
{
public:
	Test(int number)
	{
		m_number = number;
	}
	int m_number;
};

int main()
{
	Test test(10);//实例化时必须传参，否则报错
	cout << test.m_number << endl;
}
```
3. 构造函数的参数允许设置默认值，但要谨慎使用  
```
class Test
{
public:
	Test(int number, float score = 3.14)
	{
		m_number = number;
		m_score = score;
	}
	int m_number;
	float m_score;
};

int main()
{
	Test test1(10);
	cout << test1.m_number << endl;
	cout << test1.m_score << endl;
	Test test2(5, 2.7);
	cout << test2.m_number << endl;
	cout << test2.m_score << endl;
}
```
4. 有多个构造函数，即实现构造函数的重载
```
class Test
{
public:
	Test()
	{
		cout << "匹配了第一个构造函数" << endl;
	}
	Test(int i)
	{
		cout << "匹配了第二个构造函数" << endl;
	}
	Test(float f)
	{
		cout << "匹配了第三个构造函数" << endl;
	}
	Test(int i, float f)
	{
		cout << "匹配了第四个构造函数" << endl;
	}
};

int main()
{
	int i = 1;
	float f = 3.14;
	Test test1;
	Test test2(i);
	Test test3(f);
	Test test4(i, f);
}
```


## 采用初始化列表的构造函数
1. 基本概念
构造函数的主要功能是对类中成员变量设置初始值，为此可以使用更简洁的初始化列表方法  
此时构造函数体内可以空着，也可以写一些其他语句  
初始化列表可以用于全部成员变量，也可以只用于部分成员变量  
使用构造函数初始化列表并没有效率上的优势，仅仅是书写方便  
初始化列表方法的另一个重要作用是初始化const成员变量  
注意：初始化列表的后面没有分号';'，而且即使函数体为空，也必须在最后加上'{}'  
2. 示例1：在类的外部定义初始化列表形式的构造函数
```
class Student
{
public:
	Student(int age, char name, float score);//构造函数声明
	void show()
	{
		cout << "年龄：" << m_age << endl;
		cout << "姓名：" << m_name << endl;
		cout << "成绩：" << m_score << endl;
	}
private:
	int m_age;
	char m_name;
	float m_score;
};

//采用初始化列表的构造函数
Student::Student(int age, char name, float score): m_name(name), m_age(age), m_score(score)
{
	/*
	相当于在函数体内部写如下语句：
	m_age = age;
	m_name = name;
	m_score = score;
	*/
	cout << "初始化列表方法测试" << endl;
}

int main()
{
	Student stu1(15, 'a', 92.5);
	stu1.show();
	return 0;
}
```
3. 示例2：在类的内部定义初始化列表形式的构造函数
```
class Student
{
public:
	Student(int age, char name, float score): m_name(name), m_age(age), m_score(score)
	{
		cout << "初始化列表方法测试" << endl;
	}
	void show()
	{
		cout << "年龄：" << m_age << endl;
		cout << "姓名：" << m_name << endl;
		cout << "成绩：" << m_score << endl;
	}
private:
	int m_age;
	char m_name;
	float m_score;
};

int main()
{
	Student stu1(15, 'a', 92.5);
	stu1.show();
	return 0;
}
```
4. 示例3：没有函数参数的构造函数使用初始化列表方法
```
class Student
{
public:
	//将成员变量都初始化为空指针
	Student(): m_name(nullptr), m_age(nullptr), m_score(nullptr)
	{
		cout << "初始化列表方法测试" << endl;
	}
	int * m_age;
	char * m_name;
	float * m_score;
};

int main()
{
	Student stu1;
	//注意：不能通过构造函数将其他指针赋值给成员变量，以下是错误写法
	int age = 1;
	int *p1 = &age;
	char name = 'a';
	char *p2 = &name;
	float score = 90.5;
	float *p3 = &score;
	Student stu2(p1, p2, p3)//会报错
	return 0;
}
```
5. 示例4：成员变量不一定都要通过外部传参来实现初始化
```
class Student
{
public:
	//相当于把m_score的默认值设置为3.14
	Student(int age, char name): m_name(name), m_age(age), m_score(3.14)
	{
		cout << "初始化列表方法测试" << endl;
	}
	void show()
	{
		cout << "年龄：" << m_age << endl;
		cout << "姓名：" << m_name << endl;
		cout << "成绩：" << m_score << endl;
	}
private:
	int m_age;
	char m_name;
	float m_score;
};

int main()
{
	Student stu1(15, 'a');
	stu1.show();
	return 0;
}
```
6. 示例5：在有继承关系时，子类的初始化列表
```
class People//基类
{
public:
	People(int age, char name):m_age(age), m_name(name)
	{
		cout << "调用了基类的构造函数" << endl;
	}
	int m_age;
	char m_name;
};

class Student:public People//子类
{
public:
	//基类构造函数有参数的情况下，子类必须显式的调用基类的构造函数，否则会报错
	Student(int age, char name, float score): People(age, name), m_score(score)
	{
		cout << "调用了子类的构造函数" << endl;
	}
	float m_score;
};

int main()
{
	People peo1(15, 'a');
	Student stu1(18, 'b', 90.5);
	return 0;
}
```


## 析构函数
1. 析构函数定义
析构函数是在对象删除之前，完成一些内存释放等清理工作  
析构函数用来释放一个对象，和构造函数的功能刚好相反  
析构函数名必须与其类名相同，函数前面加一个逻辑非符号'\~'来作为析构函数的标识  
每个类只有一个析构函数，没有任何参数，没有返回值，定义时也不用声明函数类型  
备注：类中不一定都有析构函数，也可以不写析构函数  
```
class CMeter
{
public:
	CMeter(int nPos) 
	{
		m_nPos = nPos;
	}
	~CMeter()  //析构函数
	{}
private:
	int m_nPos;
};
```
2. 析构函数的特点
析构函数只有在以下两种情况才会被自动调用：  
2.1 实例化对象定义在一个函数体中，当函数调用结束后，析构函数被自动调用  
2.2 用new为对象分配动态内存，当使用delete释放对象时，析构函数被自动调用  
3. 默认析构函数
和默认构造函数类似，如果在定义类时没有定义任何构造函数，则会自动生成一个默认构造函数  


## 浅拷贝与深拷贝
1. C++中的深浅拷贝和python中的概念一致
浅拷贝和深拷贝的区别主要针对类中有的成员是指针类型情况的  
2. 每一个C++类都有一个隐式的默认构造函数，这个函数就是浅拷贝函数  


## 局部类
在一个函数体内定义的类称为局部类(local class)  
局部类定义的类型只在定义它的作用域内可见，而且局部类不能使用函数作用域中的变量  
局部类不能被外部所继承，不能定义静态成员函数，且所有成员函数都必须定义在类的内部  
备注：实际实践中，局部类是很少使用的，了解即可  
```
void fun()
{
　　class A
　　{
		...
	};
	...
}
```


## 嵌套类
1. 基本概念
在一个类中定义的类称为嵌套类，定义嵌套类的类称为外部类(外围类)  
嵌套类的声明必须写在外部类的内部，但具体定义可以写在外部类的内部或外部  
注意：嵌套类没有对外部类的访问权限，因此无法在嵌套类中使用外部类的成员  
备注：在项目代码中，嵌套类属于比较常用的用法，如XXXModuleData类里面会定义XXXThread类  
2. 作用
实现访问控制，限定嵌套类只能由外部类访问  
隐藏类名，减少全局的标识符，并避免名称冲突  
对类进行嵌套通常是为了帮助实现外部类，即嵌套类和外部类之间有主从关系  
例如：外部类为MyModule，嵌套类为MyModouleData  
3. 作用域
如果嵌套类定义在外部类的private部分，则只有外部类可以使用嵌套类  
如果嵌套类定义在外部类的protect部分，则外部类及其子类可以使用嵌套类  
如果嵌套类定义在外部类的public部分，则所有类都可以使用嵌套类  
备注：对于public的嵌套类，在外部类以外使用时必须加上外部类作用域限制符  
4. 代码示例
```
class A//外部类
{
public:
	void testa();
public:
	class B//嵌套类
	{
	public:
		void testa();//嵌套类的成员函数可以和外部类的成员函数同名
		void testb();
		int m_b;
	};
	B *b;//嵌套类对象可以作为外部类的一个成员变量
	...
private:
	class C//嵌套类
	{...};
};

//在外部类以外定义嵌套类的成员
void A::B::testa()
{...}
void A::B::testb()
{...}

//在外部类以外调用嵌套类的成员
A *a;
a -> b -> testa();
a -> b -> testb();
cout << a -> b -> m_b << endl;
```