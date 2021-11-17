# 函数重载override

## 基本概念
函数重载是指在满足一定条件的前提下，C++允许同一个作用域内多个函数同名，包括：  
1. 函数形参的个数不同（注意有默认参数的情况）  
2. 函数形参的个数相同，但类型不同或顺序不同  
当调用了重载函数时，编译器会根据函数参数情况自动去匹配到正确的函数  
备注：函数重载是一种静态多态  
备注：C++支持函数重载，但C语言不支持函数重载  


## 注意事项
1. 重载函数的返回类型可以相同也可以不同，但函数之间只有返回类型不同，不能成为合法的重载函数  
2. overload不是关键字，进行函数重载时不需要用overload进行任何声明  
3. 进行重载的若干个同名函数必须都在一个作用域下  


## 函数重载的作用
重载函数常用在同一个作用域内，用同一个函数名来命名一组功能相近的函数  
使用重载函数可以减少函数名数量，避免了命名空间污染，一定程度上解决命名冲突的问题  


## 函数重载overload与函数重写override
1. 这两个概念的名字比较接近，但并没有关系，即函数重载和是否有virtual修饰无关  
2. 函数重载中要求每个函数参数不一致，返回类型可以不同  
但函数重写的几个函数要求返回类型和函数参数必须完全一致  
3. 函数重载中的若干个同名函数必须都在一个作用域下
但函数重写的几个函数分别位于不同的类中，不在同一个作用域  


## 代码示例
1. 正确示例：编译器根据传递参数的类型和个数去自动匹配对应的函数
```
void sum(int a, int b)
{
	cout << "调用了重载函数void sum(int a, int b)" << endl;
	cout << a + b << endl;
}

void sum(int a, int b, int c)
{
	cout << "调用了重载函数void sum(int a, int b, int c)" << endl;
	cout << a + b + c << endl;
}

void sum(char a, char b)
{
	cout << "调用了重载函数void sum(char a, char b)" << endl;
	cout << (int)a + (int)b << endl;
}

void sum(int a, char b)
{
	cout << "调用了重载函数void sum(int a, char b)" << endl;
	cout << a + (int)b << endl;
}

int sum(char a, int b)
{
	cout << "调用了重载函数int sum(char a, int b)" << endl;
	return (int)a + b;
}

int main()
{
	sum(1, 2);
	sum(1, 2, 3);
	sum('a', 'b');
	sum(1, 'a');
	cout << sum('a', 1) << endl;
	return 0;
}
```
2. 错误示例：当函数参数带有默认值时，编译器可能会匹配到多个函数
```
int sum(int x, int y = 1)
{
	return x + y;
}

int sum(int x)
{
	return x + 10;
}

int main()
{
	sum(1);//报错，编译器不知道该去调用哪个函数
	return 0;
}
```