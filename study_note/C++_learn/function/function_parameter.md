# 函数参数

## 默认参数
C语言函数不支持默认参数，而C++函数支持默认参数
注意：默认参数必须在位置参数之后，不能写成"void func_1(int a = 1, int b)"
```
void func_1(int a, int b = 1)
{
	printf("默认参数函数：%d\n", a + b);
}

int main()
{
	func_1(1); //只传递一个参数
	func_1(1, 2); //传递多个参数
}
```