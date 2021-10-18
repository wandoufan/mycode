# 类模板

## 基本概念
有时候需要编写多个形式和功能都类似的类，编译器可以从类模板中自动生成多个类，减少了重复劳动  
template是声明类模板的关键字，表示声明一个模板  
类模板中以下的信息都可能不确定：  
1. 成员变量的数据类型
2. 成员函数的默认参数
3. 成员函数的返回类型


## 使用类模板的优缺点
1. 优点
模板复用了代码，节省资源，增强了代码的灵活性，可以更快的迭代开发  
2. 缺点
让代码变得凌乱复杂，不易维护，编译代码时间变长  
当出现模板编译错误时，错误信息非常凌乱，不易定位错误  


## 模板参数
模板参数可以是一个，也可以是多个，可以是类型参数，也可以是非类型参数  
1. 类型参数
由关键字class或typename进行声明的参数，代表模板定义中的一个变量  
备注：类型参数可以是int或float等任意类型的数据  
2. 非类型参数
由普通参数构成，代表模板定义中的一个常量  
注意：非类型参数一般都是整型，不能是浮点型或类的实例化对象  
```
//Type为类型参数，width为非类型参数
template <typename Type, int width> //合法
template <typename Type, float width> //不合法
```


## 注意事项
1. 同一个模板参数名在模板参数表中只能出现一次
```
template <typename Type, typename Type> //不合法
```
2. 在不同的类模板声明中，模板参数可以被重复利用
```
template <typename Type, int width>
template <typename Type> //合法
```
3. 类模板中的成员变量名不能和模板参数表中的变量名重复
类模板中的成员函数的参数名不能和模板参数表中的变量名重复
```
template <typename Type, int width>
class TemplateClass
{
public:
	void test(int width);//不合法
	void test(int width_);//合法
private:
	int width; //不合法
	int m_width; //合法
}
```
否则会产生如下报错
```
error: declaration of 'int width' shadows template parameter
```
4. 有多个类模板声明时，最下面的类模板声明生效
```
template <typename T>
class Image;

template <typename U>
class Image;

// 模板的真正定义
template <typename Type>
class Image
{
	//模板定义中只能引用名字Type,不能引用名字T和U
};
```
5. 类模板参数中可以有缺省实参，有缺省实参的参数放在最右边
```
template <typename T, int id, int number = 1>
```
6. 对于非类型参数，赋值时只能赋值一个const常量


## 模板类和类模板的区别
类模板是用来生成其他类的类，不是一个具体的、实际的类，而是代表一类类  
模板类是根据类模板生成的类，是一个具体的、有确定值的类  
从类模板生成模板类的过程称为类模板的实例化  


## typename与class的区别
最开始定义模板的方法为template <typename T>，用class来声明T是一个类型参数  
后来为了避免class在两个地方使用给人带来混淆，引入了typename关键字来替代class关键字  
因此在这里，二者功能一致，但一般使用typename来做声明  


## 示例
1. 只有一个类型参数的类模板
类模板中成员变量的数据类型不确定，成员函数的返回类型不确定
生成了多个模板类，每个模板类的数据类型都不相同
```
template <typename T>//声明一个模板
class ClassTemplate //类模板
{
public:
	ClassTemplate(T value) //构造函数
	{
		m_value = value;
	}

	void GetValue();

	T ReturnValue() //成员函数的返回类型为T
	{
		return m_value;
	}

private:
	T m_value; //成员变量的数据类型为T
};

template <typename T>
void ClassTemplate<T>::GetValue()//在类模板外面定义成员函数
{
	cout << "GetValue : " << m_value << endl;
}

int main()
{
	//模板类1
	ClassTemplate<int> ClassInt(10);//模板实例化
	ClassInt.GetValue();
	cout << "ReturnValue : " << ClassInt.ReturnValue() << endl;
	//模板类2
	ClassTemplate<float> ClassFloat(3.14);//模板实例化
	ClassFloat.GetValue();
	cout << "ReturnValue : " << ClassFloat.ReturnValue() << endl;
	//模板类3
	ClassTemplate<char> ClassChar('a');//模板实例化
	ClassChar.GetValue();
	cout << "ReturnValue : " << ClassChar.ReturnValue() << endl;
	return 0;
}
```

2. 有多个类型参数的类模板
类模板中成员变量的数据类型不确定，成员函数的返回类型不确定
生成了多个模板类，每个模板类的数据类型都不相同
```
template <typename T1, typename T2>//声明一个模板
class ClassTemplate //类模板
{
public:
	ClassTemplate(T1 key, T2 value):m_key(key), m_value(value)//使用初始化列表的构造函数
	{
	}

	void GetValue();

	T1 ReturnKey()
	{
		return m_key;
	}

	T2 ReturnValue()
	{
		return m_value;
	}

private:
	T1 m_key;
	T2 m_value;
};

template <typename T1, typename T2>
void ClassTemplate<T1, T2>::GetValue()//在类模板外面定义成员函数
{
	cout << "GetValue : " << m_key << "-" << m_value << endl;
}

int main()
{
	//模板类1
	ClassTemplate<int, string> ClassIntString(100, "Tom");//模板实例化
	ClassIntString.GetValue();
	cout << "Return : " << ClassIntString.ReturnKey() << '-' << ClassIntString.ReturnValue() << endl;
	//模板类2
	ClassTemplate<int, float> ClassIntFloat(100, 3.14);//模板实例化
	ClassIntFloat.GetValue();
	cout << "Return : " << ClassIntFloat.ReturnKey() << '-' << ClassIntFloat.ReturnValue() << endl;
	return 0;
}
```

3. 有类型参数和非类型参数(不带默认值)的类模板
```

```

4. 有类型参数和非类型参数(带默认值)的类模板

5. 只有非类型参数的类模板
目前没有见过这种类型的  


------------------------待总结-----------------------------

## 函数模板作为类模板成员
类模板中的成员函数还可以是一个函数模板。成员函数模板只有在被调用时才会被实例化。例如下面的程序：
```
#include <iostream>
using namespace std;
template <class T>
class A
{
public:
    template <class T2>
    void Func(T2 t) { cout << t; }  //成员函数模板
};

int main()
{
    A<int> a;
    a.Func('K');  //成员函数模板Func被实例化
    a.Func("hello");
    return 0;
}
```


## 类模板的继承问题
1. 写模板类模板函数时一般都要声明与定义放在一起
模板类与模板函数若是没有实例化是不产生实际代码的，所以在代码链接过程中，实例化是在main.cpp中，会找不到函数的定义
。。。。。。。。。。