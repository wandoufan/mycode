# 共用体union

## 基本概念
我们有时候需要把几种不同类型的变量都存放到同一段内存单元中  
这几种变量在内存中占有的字节数不同，但都从同一内存地址开始存放  
几种不同的变量共占同一段内存的结构，就称为共用体，也称为联合体  
共用体的基本格式为：  
```
union 共用体名
{
	成员列表
};
```
注意：在使用时不能直接引用共用体变量，只能引用共用体变量中的某个成员  


## 共用体的应用场景
共用体在一般的编程中应用较少，在单片机中应用较多  
共用体的主要作用是节省内存空间，其实没有太大必要，用结构体代替就可以了  


## union和struct的对比
共用体和结构体的定义形式相似，但它们的具体含义是不同的  
共同体变量所占的内存长度等于最长的成员的长度  
结构体变量所占内存长度是各成员占用的内存长度之和  


## 共用体数据的特点
1. 同一个内存单元可以存放几种不同类型的成员，但每次只能存放其中一种，而不是同时存放好几种
2. 共用体变量中起作用的成员是最后一次存放的成员，放入一个新成员之后，原有的成员就失去了作用
因此使用共用体变量时必须注意变量中当前存放的是哪个成员
3. 共用体变量的地址和它各个成员的地址都是同一个地址
例如，&data、&data.i、&data.c、&data.f都是对应同一个内存地址
4. 共用体变量不能作为函数参数，也不能作为函数的返回值，但可以使用指向共用体变量的指针
5. 共用体可以作为结构体的一个成员，结构体也可以作为共用体的一个成员
6. 可以定义共用体数组，数组也可以作为共用体的成员


## 共用体的定义和声明
1. 声明union数据类型，同时定义union变量
```
int main()
{
	union data
	{
		int i;
		char c;
		float f;
	}a, b, c;

	a.i = 1;
	a.c = 'a';
	a.f = 3.14;

	printf("%d\n", a.i);//无效
	printf("%c\n", a.c);//无效
	printf("%f\n", a.f);//有效
	return 0;
}
```
2. 先声明union数据类型，再定义union变量
```
int main()
{
	union data
	{
		int i;
		char c;
		float f;
	};

	union data a, b, c;

	a.i = 1;
	a.c = 'a';
	a.f = 3.14;

	printf("%d\n", a.i);//无效
	printf("%c\n", a.c);//无效
	printf("%f\n", a.f);//有效
	return 0;
}
```


## 共用体语法示例
1. 不能在定义共用体变量时就对它进行初始化
```
int main()
{
	union data
	{
		int i;
		char c;
		float f;
	}a = (1, 'a', 3.14);//不合法
	
	return 0;
}
```
2. 不能直接对共用体变量赋值
```
int main()
{
	union data
	{
		int i;
		char c;
		float f;
	}a;
	a = 1;

	return 0;
}
```
3. 同一类型的共用体变量之间可以相互赋值
```
int main()
{
	union data
	{
		int i;
		char c;
		float f;
	}a, b;

	a.i = 1;
	a.c = 'a';
	a.f = 3.14;
	b = a;
	printf("%f\n", b.f);

	return 0;
}
```