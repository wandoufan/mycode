# 常类型const


## 基本概念
常类型是指使用const修饰符进行说明的类型，C语言中也有const  
常类型的变量或对象的值是不能被更新的，因此定义常类型时必须初始化  
如果试图修改被const修饰的对象，则会报错'assignment of read-only variable'  


## const关键字
const是C语言和C++的关键字，const是constant的缩写，表示不变的  
const可以用来修饰内置变量类型、自定义对象、成员函数、返回值和函数参数  
const可以指定一个语义约束，使被修饰对象保持不变，编译器会强制实施这个约束  


## 常对象
常对象是指由类实例化出来的对象常量，定义格式为：  
'const class object(params);'或'class const object(params);'  
常对象只能访问被const修饰的成员方法，因为非const成员可能会修改对象的数据  
```
const Student1 zhang(1, 16); //获取一个常对象
cout << zhang.age << endl; //常对象的非const成员变量可以访问
// zhang.age = 17; //常对象的非const成员变量不可以修改，否则报错
zhang.get_id(); //常对象的const成员方法可以访问
// zhang.get_age(); //常对象的非const成员方法不可以访问，否则报错
```


## 常成员变量
const成员变量的用法和普通const变量的用法相似，只需要在声明时加上const关键字  
初始化const成员变量只有一种方法，就是通过构造函数的初始化列表  
注意：不可以直接在类的构造函数的函数体中初始化const的成员  
```
class Student2
{
public:
	Student2(int my_a, int my_c);
	const int a; //只声明一个const成员变量，但不赋值
	int b;
private:
	const int c;
	int d;
};
Student2::Student2(int my_a, int my_c):a(my_a), c(my_c) //初始化列表
{
	cout << "用初始化列表来初始化const成员变量" << endl;
}

Student2 stu(1, 3); //const成员变量赋值
```


## 常成员方法
常成员方法需要在声明和定义的时候在函数头部的结尾加上const关键字  
const成员函数可以使用类中的所有成员变量，但是不能修改它们的值  
我们经常将读取成员变量的get函数设置为const的，表示只能读取，不能修改  
注意：如果声明和定义是分开的，必须在成员函数的声明和定义处同时加上const关键字  
```
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
	void get_score() const; //类内部声明时要加上const
};
void Student1::get_score() const  //类外部定义时也要加上const
{
	cout << score << endl;
}
```

-------------------------------------------------------------------

## 常量
用const修饰变量后，变量的值就不能再被修改，称为常变量  
const变量必须在定义时初始化，不能先定义再初始化  
常变量也完全可以用'#define'来代替  
```
const int a = 1; // const把变量a定义为一个常量
int b = a; // 可以把a赋值给其他变量
// a = 2; // 不能再对a进行修改，否则会报错
```


## 常指针
常指针是用const修饰的指针，有三种形式：  
1. const放在指针变量的类型之前，表示声明一个指向常量的指针  
'const int \*p1 = &a;'和'int const \*p1 = &a;'的效果一样  
这种情况下，不能通过指针改变它所指向的变量值，但可以修改指针本身的值  
```
int a = 1, b = 2;
const int *p1 = &a; //p1指针指向变量a，即a是const的
// *p1 = 2; //不能修改p1指针指向变量的值，否则报错
p1 = &b; //p1指针指向变量b，即指针本身的值可以改变
// 另一种写法
int const *p2 = &a;
// *p2 = 2;
p2 = &b;
```
2. const放在定义指针变量的名之前，表示指针本身是一个常量，称为指针常量或常指针  
例如：'int * const p1 = &a;'  
这种情况下，不能改变指针本身的值，但可以通过指针改变它所指向的变量值  
```
int a = 1, b = 2;
int * const p1 = &a; //p1指针指向变量a，即p1本身是const的
*p1 = 2; //可以修改p1指针指向变量的值
// p1 = &b; //不能修改指针本身的值
// int * const p2; //注意：声明常指针时必须进行初始化，否则报错
```
3. 将const在上述两个地方都写上，表示一个指向常量的常指针  
'const int * const p1 = &a;'和'int const * const p1 = &a;'效果一样  
这种情况下，指针指向的变量值和指针本身都不可变  
```
int a = 1, b = 2;
const int * const p1 = &a; //常指针p1指向常量a
// p1 = &b; //指针本身不能修改，否则报错
// *p1 = 2; //指向对象不能修改，否则报错
// const int * const p2; //注意：声明常指针时必须进行初始化，否则报错
```


## 常函数
函数开头的const用来修饰普通函数的返回值，表示返回值是const类型，也就是不能被修改  
例如：'const char * getname()'  
函数头部的结尾加上const表示类中的常成员函数，这种函数只能读取不能修改成员变量的值  
例如：'char * getname() const'  


## 常函数形参
常用const来修饰函数的指针形参，防止在函数内部修改指针指向的数据  
```
void test(const char *p)
```


## const和非const类型转换
'const char \*'和'char \*'是不同的类型  
可以把非const类型赋值为const类型，但不能把const类型赋值给非const类型  



## 常引用