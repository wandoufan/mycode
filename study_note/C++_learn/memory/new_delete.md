# C++中的内存分配

## C++内存空间
C++程序中的内存分为两个部分：  
1. 栈
在函数内部声明的所有变量都将占用栈内存  
2. 堆
这是程序中未使用的内存，在程序运行时可用于动态分配内存  


## malloc和free
C语言中用来动态地开辟和释放内存的库函数在C++中还可以使用  
1. void * malloc(unsigned int size);
在内存的动态存储区域中分配一个长度为size的连续空间，函数的返回值是分配域的起始地址，如果执行失败(如内存空间不足)，则返回空指针'NULL'  
2. void * calloc(unsigned n, unsigned size);
在内存的动态存储区域中分配n个长度为size的连续空间，函数的返回值是分配域的起始地址  
如果执行失败(如内存空间不足)则返回空指针'NULL'，calloc函数常用来为一维数组分配内存空间  
3. void free(void * p);
释放由p指针指向的动态存储区域，使这部分内存区域可以被其他变量使用，  
其中p是最近一次调用malloc或calloc函数时的返回值，free函数本身没有返回值  
```
int *p = (int*) malloc( sizeof(int) * 10 );  //分配10个int型的内存空间
free(p);  //释放内存
```


## new和delete
**对比说明**
C++又新增了两个关键字，new和delete：new用来动态分配内存，delete用来释放内存  
和malloc()一样，new也是在堆区分配内存，必须手动释放，否则只能等到程序运行结束由操作系统回收  
new与malloc()函数相比，其主要的优点是，new不只是分配了内存，它还创建了对象  
在C++中，建议优先使用new来替代malloc()函数  
为了避免内存泄露，通常new和delete、new[]和delete[]操作符应该成对出现，并且不要和C语言中malloc()、free()一起混用  
**功能说明**
运算符new会返回指定类型的一个指针，如果分配失败(内存空间不足)则返回0  
运算符delete会释放new请求到的内存，但释放后的指针仍然有效，还可以继续使用  
**常用类型1**
1. 单个数据
new会根据数据类型来分配相应的内存空间  
```
int *p = new int;  //分配1个int型的内存空间
delete p;  //释放内存
```
2. 一组数据
用 new[] 分配的内存需要用 delete[] 释放  
```
int *p = new int[10];  //分配10个int型的内存空间
delete[] p;
```
3. new出一个类的对象
new一般和指针搭配使用，此时只需要指出类名，不需要写出对象名  
备注：在类的构造函数中，可以写上's1 = new Student(this);'
```
class Student
{
public:
	int a;
};

int main()
{
	Student *s1 = new Student;
	s1 -> a = 1;
	cout << s1 -> a << endl;
	delete s1;
}
```