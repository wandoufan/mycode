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


## 使用方法
继承的一般语法格式为：  
```
class 派生类名:［继承方式］ 基类名
{
    派生类新增加的成员
};
```
例如：  
```
class People //基类People
{
public:
	void set_age(int a)
	{
		age = a;
	}
	void get_age()
	{
		cout << age << endl;
	}
private:
	int age;
};

class Student:public People //派生类Student
{
public:
	void set_score(float a)
	{
		score = a;
	}
	float score;
};
```

## 继承方式
继承方式包括：public、private、protected，如果不写，则默认为private  
其中，基类中的protected成员可以在派生类中使用，而基类中的private成员不能在派生类中使用  
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
注意：基类的private成员在派生类只是不能使用，不是不能继承，private成员仍然占据派生类对象的内存，只是不可见了  
备注：private和protected会导致继承关系复杂，实际开发中一般只使用public方式  


## 改变访问权限
在派生类中使用using关键字可以改变基类成员在派生类中的访问权限  
例如将public改为private、将protected改为public  
using只能改变基类中public和protected成员的访问权限，不能改变private成员的访问权限  


## 继承时的名字遮蔽问题
如果父类和子类中有成员重名，则以子类中的为准  