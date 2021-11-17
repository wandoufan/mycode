# `#`和`##`

## 构串操作符`#`
1. 基本功能
在带参数的宏定义时，把`#`右边的参数(如x)做整体的字符串替换  
注意：参数是一个变量，则替换成变量的名字，而不是变量的值  
2. 代码示例
```
#define STRING(x) #x#x
#define TEXT(x) "Name"#x"__"

int main()
{
	int num = 123;
	cout << STRING(num) << endl;//输出：numnum
	cout << TEXT(num) << endl;//输出：Namenum__
	return 0;
}
```
3. 如果不加上`#`，会报错无法识别标识符
```
#define TEST1(x) x
#define TEST2(x) x * x
#define TEST3(x) x_
#define TEST4(x) x_x
#define TEST5(x) xx

int main()
{
	int num = 123;
	cout << TEST1(num) << endl;//输出：123
	cout << TEST2(num) << endl;//输出：15129
	cout << TEST3(num) << endl;//报错：标识符没有声明，无法识别
	cout << TEST4(num) << endl;//报错：标识符没有声明，无法识别
	cout << TEST5(num) << endl;//报错：标识符没有声明，无法识别
	return 0;
}
```


## 合并操作符`##`
1. 基本功能
在带参数的宏定义时，把`##`左右两边的参数做整体的字符串拼接  
备注：这里查了很多资料，但还是没有搞明白它的功能和用法  
2. 代码示例
```
#define MERGE(a,b) a##b##a

int main()
{
	cout << MERGE(1, 2) << endl;//输出：121
	return 0;
}
```