# 类中的静态成员

## 基本概念
1. 静态成员的定义
在类中用static声明的成员变量和成员方法都称为静态成员  
静态成员既有public，也有private  

2. 静态成员的好处
以往实现数据共享的方式是设置全局变量或全局对象，但代码量大时可能会造成程序的混乱  
静态成员可以解决这个问题，既实现数据封装隐藏，也能实现数据共享和外部访问  
静态成员变量可以看做类的多个对象之间的全局变量  

3. 静态成员的坏处
和全局变量一样，类的对象过多时会造成代码混乱，很难查出是哪个对象修改了静态成员  


## 静态成员变量
1. 注意事项
静态成员变量可以被类的多个对象共享，但只用存储一处，节省了内存空间  
注意：静态成员变量只有一个，并不是每个对象各自调用一个静态成员变量  
当有一个对象修改了静态成员变量的值，其他对象的这个变量都会改变值  
注意：静态成员变量的值是在代码初始化编译时就已经生成的，并不是在调用时才去生成  
静态成员变量具有静态生存期，在程序中初始化时开始，到程序结束时消失  
即静态成员变量的内存空间不能用构造函数创建，也不能用析构函数释放  
注意：静态成员变量的内存空间不会随着对象的产生而分配，也不会随着对象的消失而释放  

2. 声明和初始化
必须在类的内部进行声明：  
```
static int number;
```
必须在类的外部进行初始化：  
```
<数据类型><类名>::<静态成员变量> = <值>;
```
注意：静态成员变量的内存空间不能通过定义类对象的方式来分配，必须在类的外部进行初始化  
注意：静态成员变量使用前必须初始化，且不能是通过一个对象进行初始化

3. 引用格式
当静态成员变量为public时，可以有两种方式访问，通过对象引用和直接引用  
对象引用的格式: '<对象名>.<静态成员变量>'  
直接引用的格式: '<类名>::<静态成员变量>'  


## 静态成员方法
1. 注意事项
如果把函数成员声明为静态的，就可以把函数与类的任何特定对象独立开来  
静态成员函数一般都是公有的public，可以让外部不需要实例化对象就能任意调用  
静态成员函数即使在类对象不存在的情况下也能通过'类名::函数名'被调用  
静态成员函数没有this指针，只能访问类中的静态成员变量和其他静态成员函数  

2. 定义
静态成员函数的定义可以写类内部，也可以写类外部，没有影响  

3. 引用格式
当静态成员方法为public时，可以有两种方式访问，通过对象引用和直接引用  
对象引用的格式: '<对象名>.<静态成员方法>'  
直接引用的格式: '<类名>::<静态成员方法>'  

4. 直接写函数名
如果是在类或子类中引用该类的静态成员方法，可以只写函数名，前面不需要加类名或对象名  
```
sleep(5); //不需要写成 QThread::sleep(5);
```


## 代码示例：静态成员变量和静态成员方法的定义与使用
```
class Test
{
public:
	static int m_public; //静态成员变量
	static void func_static();//静态成员方法，在内部声明，在外部定义
	static void func_static2()//静态成员方法，在内部声明和定义
	{
		cout << "调用了静态成员方法" << endl;
		cout << m_private << endl;//静态成员方法中只能引用静态成员变量
	}
private:
	static int m_private; //静态成员变量
};

//注意：要声明变量为int型
int Test::m_public = 1;//对静态成员变量初始化必须在类外部进行
int Test::m_private = 2;//对静态成员变量初始化必须在类外部进行

void Test::func_static()
{
	cout << "调用了静态成员方法" << endl;
	cout << m_private << endl;//静态成员方法中只能引用静态成员变量
}

int main()
{
	Test test1, test2, *p;
	p = new Test;
	//引用静态成员变量
	cout << Test::m_public << endl;//通过类名直接引用静态成员变量
	cout << test1.m_public << endl;//通过对象引用静态成员变量
	cout << p -> m_public << endl;//通过对象指针引用静态成员变量
	//多个对象共享一个静态成员变量，有一个对象修改了静态成员变量之后，其他对象也会随之改变
	test1.m_public = 10;
	cout << test2.m_public << endl;//输出10
	//引用静态成员方法
	Test::func_static();//通过类名直接引用静态成员方法
	test1.func_static();//通过对象引用静态成员方法
	p -> func_static();//通过对象指针引用静态成员方法

	return 0;
}
```


## 关于在静态公共函数中调用非静态成员变量的方法
1. 问题说明
静态成员函数没有this指针，只能访问类中的静态成员变量和其他静态成员函数
因此，一般来说，静态成员函数中不能调用非静态的成员变量
但在有些场景下，静态函数需要对非静态的成员变量进行读取或写入操作
2. 实现方法
在类中声明一个类本身的指针，作为类的成员变量，并将其声明为static类型的
在静态公共函数中，可以调用到静态的类指针，再通过类指针去访问其他非静态的成员变量
备注：这里的用法有点类似于单例类，但又不完全一样
3. 代码示例1
头文件
```
class StaticTest
{
public:
    StaticTest();
    static int get_non_static();

private:
    static StaticTest *m_instance;
    int m_non_static;
};
```
源文件
```
//静态的类指针在初始化时直接指向一个新的类对象
StaticTest *StaticTest::m_instance = new StaticTest;

StaticTest::StaticTest()
{
    m_non_static = 10;
}

int StaticTest::get_non_static()
{
    m_instance -> m_non_static += 1;
    return m_instance -> m_non_static;
}
```
调用代码
```
//静态的类指针只有一个，所以三次调用静态函数实际是调用了同一个对象
qDebug() << StaticTest::get_non_static();//输出：11
qDebug() << StaticTest::get_non_static();//输出：12
qDebug() << StaticTest::get_non_static();//输出：13
```
4. 代码示例2
头文件
```
class StaticTest
{
public:
    StaticTest();
    static int get_non_static();

private:
    static StaticTest *m_instance;
    int m_non_static;
};
```
源文件
```
//类指针初始化时赋值为空指针，在构造函数中再指向类对象
StaticTest *StaticTest::m_instance = nullptr;

StaticTest::StaticTest()
{
    m_instance = this;
    m_non_static = 10;
}

int StaticTest::get_non_static()
{
    m_instance -> m_non_static += 1;
    return m_instance -> m_non_static;
}
```
调用代码1
```
//自己手动实例化一个类对象，从而调用到构造函数，三次调用静态函数也是调用了同一个对象
StaticTest mytest;
qDebug() << StaticTest::get_non_static();//输出：11
qDebug() << StaticTest::get_non_static();//输出：12
qDebug() << StaticTest::get_non_static();//输出：13
```
调用代码2
```
//每次调用前都手动实例化一个类对象，因此三次调用静态函数是调用了三个对象
StaticTest mytest1;
qDebug() << StaticTest::get_non_static();//输出：11
StaticTest mytest2;
qDebug() << StaticTest::get_non_static();//输出：11
StaticTest mytest3;
qDebug() << StaticTest::get_non_static();//输出：11
```