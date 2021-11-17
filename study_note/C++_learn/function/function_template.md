# 函数模板

## 基本概念
有时候需要编写多个形式和功能都类似的函数，编译器可以从类模板中自动生成多个函数，减少了重复劳动  
template是声明函数模板的关键字，表示声明一个模板  
在函数模板中，函数的参数类型都是不确定的  


## 模板声明的注意事项
1. 模板的声明和定义必须放在一起，否则编译时可能找不到定义
2. 模板的声明和定义只能在全局范围、命名空间、类范围内进行，不能在局部范围或函数内进行
例如，不能在main函数中声明或定义一个模板  


--------------------- 代码示例 ------------------------

1. 只有一个模板参数的函数模板
```
template <typename T>
void function_template(T value)
{
	cout << value << endl;
	cout << typeid(value).name() << endl;
}

int main()
{
	function_template(3.14);
	function_template('a');
	function_template(1);//可以不指明模板参数的类型，系统会根据实参类型自动匹配
	function_template<>(1);//可以写一个空参数列表，效果和上面一样
	function_template<int>(1);//可以指明模板参数的具体类型
	function_template<int>(3.14);//指明的模板参数类型和实参类型不一致时，会将实参进行类型转换
	return 0;
}
```

2. 有多个模板参数的函数模板
```
template <typename T1, typename T2, typename T3>
void function_template(T1 value1, T2 value2, T3 value3)
{
	cout << value1 << endl;
	cout << typeid(value1).name() << endl;
	cout << value2 << endl;
	cout << typeid(value2).name() << endl;
	cout << value3 << endl;
	cout << typeid(value3).name() << endl;
}

int main()
{
	function_template(1, 3.14, 'a');
	return 0;
}
```

3. 模板参数可以作为函数模板的返回类型
```
template <typename T>
T function_template(T value)
{
	return value;
}

int main()
{
	cout << function_template(3.14) << endl;
	cout << typeid(function_template(1)).name() << endl;
	return 0;
}
```
