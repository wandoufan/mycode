# 命名空间namespace

## 基本概念
代码的工程越大，各种标识符产生名称冲突的概率越大，为了避免名称冲突，C++中引入了命名空间  
命名空间将代码组成逻辑组，同名变量调用时要声明所在的namespace，从而避免了名称冲突(collision)  
备注：C不使用名称空间，C语言中所有符号名称都定义在一个全局命名空间中  
当C代码包含多个库，尤其库是不同人编写时就很可能发生名称冲突  


## 命名空间的声明
备注：一般声明和引用的代码不在一个文件中，声明通常在头文件中，引用通常在源代码文件中  
namespace是C++中的关键字，用来定义一个命名空间
命名空间的名字一般全部小写，有时候也用驼峰命名法，语法格式为：  
```
namespace space_name{
	// 各种代码声明
	variables;
	functions;
	classes;
}
```
1. 命名空间中的成员随时可以添加，不必一次性写完
```
namespace zhang{
	int a = 1;
}

namespace zhang{
	void func()
	{
		cout << "zhang" << endl;
	}
}
```
2. 命名空间中函数的声明和定义可以分离
```
namespace li{
	int a = 2;
	void func();
}

void li::func()
{
	cout << "li" << endl;
}
```
3. 命名空间可以多层嵌套定义，内外层的同名变量互不影响
```
namespace wang{
	int a = 3;
	namespace liu{
		int a = 4;
	}
	void func()  //这个func是属于空间wang，不属于空间liu，即liu无法调用func()
	{
		cout << "wang" << endl;
	}
}
```
4. 用namespace声明时可以不写空间名，这个空间的标识符只能在本文件内使用，相当于用static进行了声明
```
namespace {  //可以不写空间名
	int a = 1;
	void func()
	{
		cout << "no name" << endl;
	}
}

int main()
{
	cout << a << endl;
	func();
}
```
5. 命名空间只能定义在最外层的全局范围内定义，不能在函数内部定义命名空间
```
下面是错误的写法
void test_namespace()
{
	namespace zhang{
		int a = 1;
	}
	cout << zhang::a << endl;
}

```
6. 命名空间可以直接把类名写进去，相当于把类里的所有成员都加入了命名空间  
备注：QT程序中是这样写的，其他地方不知道是否能这样操作  
```
QT_BEGIN_NAMESPACE
namespace Ui { class Widget_database; }
QT_END_NAMESPACE

class Widget_database : public QWidget
{
    Q_OBJECT

public:
    Widget_database(QWidget *parent = nullptr);
    ~Widget_database();

private:
    Ui::Widget_database *ui;
};
```


## 命名空间中标识符的引用
备注：一般声明和引用的代码不在一个文件中，声明通常在头文件中，引用通常在源代码文件中  
1. 使用'using namespace'来声明引入某个命名空间的所有标识符
引入整个命名空间的声明会增加命名冲突的可能性，因为多个命名空间中可能会有相同的标识符  
备注：如果两个命名空间有冲突，只是单纯的using声明不会报错，只有引用到那个冲突的标识符时才报错  
```
using namespace wang;
cout << a << endl;  //此时编译器已经知道a是wang空间的了，不需要再单独声明
```
2. 使用'::'运算符来声明引入某个命名空间的某个标识符
```
cout << zhang::a << endl;
cout << wang::liu::a << endl;  //当命名空间有多层嵌套时，引用也要多层声明
```
3. 同样的，在命名空间有嵌套时，也使用'::'运算符来引入某个内层的命名空间
```
using namespace wang::liu;
```
4. using遇到函数重载
如果某个命名空间中有多个同名重名函数，使用using就相当于声明了这个空间中所有的重载函数  

