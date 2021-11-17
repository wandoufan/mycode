# 类模板

## 基本概念
有时候需要编写多个形式和功能都类似的类，编译器可以从类模板中自动生成多个类，减少了重复劳动  
template是声明类模板的关键字，表示声明一个模板  
在类模板中，以下的信息都可能不确定：  
1. 成员变量的数据类型
2. 成员函数的默认参数
3. 成员函数的返回类型


## 模板声明的注意事项
1. 模板的声明和定义必须放在一起，否则编译时可能找不到定义
2. 模板的声明和定义只能在全局范围、命名空间、类范围内进行，不能在局部范围或函数内进行
例如，不能在main函数中声明或定义一个模板  


## 使用类模板的优缺点
1. 优点
模板复用了代码，节省资源，增强了代码的灵活性，可以更快的迭代开发  
2. 缺点
让代码变得凌乱复杂，不易维护，编译代码时间变长  
当出现模板编译错误时，错误信息非常凌乱，不易定位错误  
3. 应用场景
一般在规模比较大的项目中才会频繁用到类模板，少量的脚本代码也没必要用类模板  


## 模板参数
模板参数可以是一个，也可以是多个，可以是类型参数，也可以是非类型参数  
1. 类型参数
由关键字class或typename进行声明的参数，代表模板定义中的一个变量  
备注：类型参数可以是int、float、指针等任意类型的数据  
2. 非类型参数
由普通参数构成，代表模板定义中的一个常量  
注意：非类型参数一般都是整型，不能是浮点型或类的实例化对象  
```
//Type为类型参数，width为非类型参数
template <typename Type, int width> //合法
template <typename Type, float width> //不合法
```


## 模板类和类模板的区别
```
template <typename T, int size>
class ClassTemplate
{...}

ClassTemplate<float, 10> Class1;
```
1. 类模板是用来生成其他类的类，不是一个具体的、实际的类，而是代表一类类
类模板不能直接实例化出对象，必须先确定为一个具体的模板类
从类模板生成模板类的过程称为类模板的实例化
`class ClassTemplate`
2. 模板类是根据类模板生成的类，是一个具体的、有确定值的类
`ClassTemplate<float, 10>`
3. 这是一个由类模板生成的实例化对象
`Class1`


## typename与class的区别
最开始定义模板的方法为template <typename T>，用class来声明T是一个类型参数  
后来为了避免class在两个地方使用给人带来混淆，引入了typename关键字来替代class关键字  
因此在这里，二者功能一致，但一般使用typename来做声明  


------------------------ 类模板的注意事项 ------------------------

1. 同一个模板参数名在模板参数表中只能出现一次
```
template <typename Type, typename Type> //不合法
```
2. 在不同的类模板声明中，模板参数可以被重复利用
```
template <typename Type, int width>
class ClassTemplate1
{...}
template <typename Type> //合法
class ClassTemplate2
{...}
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
也就说，一个位置使用了默认参数，其后的所有参数都必须使用默认参数
```
template <typename T, int id, int number = 1>
```
6. 对于非类型参数，赋值时只能赋值一个常量或常变量
```
template <typename T, int size>
class ClassTemplate
{...}

int a = 10;//不合法，不能直接赋值一个变量
const a = 10;//合法
ClassTemplate<float, a> Class1;
ClassTemplate<float, 10> Class2;//合法
ClassTemplate<float, 3.14> Class3;//不合法，非类型参数不能是浮点数
```


------------------------ 类模板的实例化示例 ------------------------

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

3. 同时具有类型参数和非类型参数的类模板
```
template <typename T, int size>//声明一个模板
class ClassTemplate //类模板
{
public:
	void SetArray(int index, T value)
	{
		m_array[index] = value;
	}
	void PrintArray()
	{
		for(int i = 0; i < size; i++)
		{
			cout << i << " : " << m_array[i] << endl;
		}
	}
private:
	T m_array[size];
};

int main()
{
	//模板类1
	ClassTemplate<int, 10> Class1;//可以直接赋值一个常量10
	for(int i = 0; i < 10; i++)
	{
		Class1.SetArray(i, i * 10);
	}
	Class1.PrintArray();
	//模板类2
	const int a = 5;
	ClassTemplate<float, a> Class2;//如果赋值一个变量，必须是const修饰的常变量
	for(int j = 0; j < 5; j++)
	{
		Class2.SetArray(j, j + 0.2);
	}
	Class2.PrintArray();
	return 0;
}
```

4. 类型参数带有缺省值(默认值)的类模板
```
template <typename T = int>//类型参数带有缺省值，默认为int型
class ClassTemplate1 //类模板
{
public:
	void SetValue(T value)
	{
		m_value = value;
	}
	T GetValue()
	{
		return m_value;
	}
private:
	T m_value;
};

int main()
{
	//模板类1
	ClassTemplate1<> Class1;//可以不指定类型参数，注意<>不能省略
	Class1.SetValue(3.14);//输入的float类型会被强制转换为int类型
	cout << Class1.GetValue() << endl;//3
	//模板类2
	ClassTemplate1<float> Class2;//也可以指定为其他的类型参数
	Class2.SetValue(3.14);
	cout << Class2.GetValue() << endl;//3.14
	return 0;
}
```

5. 类型参数和非类型参数都带有缺省值(默认值)的类模板
```
template <typename T = int, int size = 10>//类型参数和非类型参数都带有缺省值
class ClassTemplate2 //类模板
{
public:
	void SetValue(int index, T value)
	{
		m_array[index] = value;
	}
	void PrintValue()
	{
		for(int i = 0; i < size; i++)
		{
			cout << i << " : " << m_array[i]<< endl;
		}
	}
private:
	T m_array[size];
};

int main()
{
	//模板类1
	ClassTemplate2<> Class1;//可以不指定任何参数
	for(int i = 0; i < 10; i ++)
	{
		Class1.SetValue(i, 3);
	}
	Class1.PrintValue();
	//模板类2
	ClassTemplate2<float> Class2;//可以只指定第一个参数
	for(int i = 0; i < 10; i ++)
	{
		Class2.SetValue(i, 3.14);
	}
	Class2.PrintValue();
	//模板类3
	ClassTemplate2<float, 5> Class3;//可以指定两个参数
	for(int i = 0; i < 5; i++)
	{
		Class3.SetValue(i, 3.14);
	}
	Class3.PrintValue();
	// ClassTemplate2<5> Class3;//不合法，不能只指定第二个参数
	return 0;
}
```

6. 只有非类型参数带有缺省值(默认值)的类模板
```
template <typename T, int size = 5>//只有非类型参数带有缺省值
class ClassTemplate3 //类模板
{
public:
	void SetValue(int index, T value)
	{
		m_array[index] = value;
	}
	void PrintValue()
	{
		for(int i = 0; i < size; i++)
		{
			cout << i << " : " << m_array[i]<< endl;
		}
	}
private:
	T m_array[size];
};

int main()
{
	//模板类1
	ClassTemplate3<int> Class1;//可以只指定第一个参数
	for(int i = 0; i < 5; i ++)
	{
		Class1.SetValue(i, 3);
	}
	Class1.PrintValue();
	//模板类2
	ClassTemplate3<float, 10> Class2;//可以指定两个参数
	for(int i = 0; i < 10; i ++)
	{
		Class2.SetValue(i, 3.14);
	}
	Class2.PrintValue();
	return 0;
}
```

7. 只有非类型参数的类模板
目前没有见过这种类型的，类模板中至少都有一个类型参数


------------------------ 类模板的继承示例 ------------------------

1. 如果父类是类模板，而子类不是类模板，则继承时需要指明父类的具体类型
```
template <typename T>//声明一个模板
class ClassFather //类模板
{
public:
	void SetValue(T value)
	{
		m_value = value;
	}
	T GetValue()
	{
		return m_value;
	}
public:
	T m_value;
};

class ClassSon1:public ClassFather<int> //父类是一个类模板，必须指明父类的具体类型
{
public:
	void PrintType()
	{
		cout << m_value << endl;
		cout << "成员变量的类型为：" << typeid(m_value).name() << endl;
	}
};

class ClassSon2:public ClassFather<float> //父类是一个类模板，必须指明父类的具体类型
{
public:
	void PrintType()
	{
		cout << m_value << endl;
		cout << "成员变量的类型为：" << typeid(m_value).name() << endl;
	}
};

int main()
{
	//子类1的对象
	ClassSon1 son1;
	son1.SetValue(3);
	son1.PrintType();
	//子类2的对象
	ClassSon2 son2;
	son2.SetValue(3.14);
	son2.PrintType();
	return 0;
}
```

2. 如果一定要灵活指定父类中的T的类型，那子类也必须变成类模板
```
template <typename T>//声明一个模板
class ClassFather //类模板
{
public:
	void PrintType()
	{
		cout << "成员变量的类型为：" << typeid(m_value1).name() << endl;
	}
public:
	T m_value1;
};

template <typename T1, typename T2>
class ClassSon:public ClassFather<T1> //子类的父类是一个类模板
{
public:
	void PrintType()
	{
		cout << "成员变量的类型为：" << typeid(m_value2).name() << endl;
	}
public:
	T2 m_value2;
};

int main()
{
	//子类的对象
	ClassSon<int, float> son;
	son.PrintType();
	son.ClassFather::PrintType();
	return 0;
}
```

3. 类模板也可以作为子类
```
class Person//父类
{
public:
	virtual void print(int id) = 0;//纯虚函数的声明
};

template <typename T>
class Teacher:public Person//子类是一个类模板
{
public:
	void print(int id)//在子类中对纯虚函数做出具体定义
	{
		cout << "id : " << id << endl;
		cout << "this is a teacher" << endl;
	}
	void getType(T value)
	{
		cout << typeid(value).name() << endl;
	}
};

int main()
{
	Teacher<int> teacher;
	teacher.print(10);
	teacher.getType(3.14);
	return 0;
}
```