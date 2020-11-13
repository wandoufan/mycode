# 变量存储类型

## 基本概念
变量的存储类型定义了变量在哪里开辟内存空间，以及占用内存空间的有效期限  
C/C++中每个变量或函数都有两个属性：数据类型和存储类型  
一般格式为：'<存储类型> <数据类型> <变量名>;'  


## 存储方式
1. 静态存储方式是指在程序运行期间由系统分配固定的存储空间，即内存一直不释放  
静态存储区主要存放：  
1.1 全局变量  
1.2 用static声明的局部变量  
2. 动态存储方式是指在程序运行期间根据需要动态的分配存储空间，即调用完成就释放内存  
动态存储区主要存放：  
2.1 函数的形参(在调用函数时才给形参分配内存空间)  
2.2 auto类型的局部变量，即自动变量  
2.3 函数调用时的现场保护和返回地址  
3. 关于定义了局部变量但未赋初始值的说明：
如果是静态局部变量，则编译时自动赋值为0(对于数值变量)或空字符(对字符变量)  
如果是自动变量，则其初始值不确定，可能是任意一块内存空间的值  

### 1. 自动类型(auto)
函数中的局部变量除非专门声明为static，否则默认为auto类型，即auto可以省略不写  
C/C++中的大部分变量都是auto类型，称为自动变量  

### 2. 寄存器类型(register)
如果某个变量频繁被调用，可以在定义时用register声明，该变量就会被直接存入CPU的寄存器中，加快读写速度  
例如，在一个上万次的for循环中每次都要调用某个局部变量，则这个变量可以被声明为register  
如果系统的寄存器已满，没有多余空间时，寄存器变量会自动转成auto变量  
注意：只有自动变量和函数形参可以作为寄存器变量，静态局部变量和全局变量不能声明为register  
备注：如今的编译系统已经可以自动识别频繁使用的变量，一般不需要用户自己去使用register声明  

### 3. 外部类型(extern)
如果需要扩展外部变量的作用域，可以用extern来声明引入一个已经定义好的外部变量  
extern后可以跟多个变量，一个变量也可以在多个地方被extern  
编译器遇到extern先在本文件找，找不到就去项目的其他文件找，还找不到就报错  
注意：extern是这四个关键字中唯一不在定义时使用的，使用时同样要声明类型  
1. 在本源文件内使用extern
如果一个变量定义在后，使用在前，调用该变量时就需要用extern进行声明  
```
int main()
{
	extern int a, b;  //对后面定义的a,b进行声明，注意要写明变量类型
	cout << a << endl;
	cout << b << endl;
	return 0;
}

int a = 1, b = 2;
```
2. 在多个文件间使用extern
如果程序由多个源文件组成，想在一个文件中引用另一个文件的变量也用extern声明  
变量只需要在一个文件中定义，其他文件想使用直接用extern，不需要再定义  
注意：跨文件使用全局变量更需要谨慎，出bug时很难找到问题来源  

### 4. 静态类型(static)
如果需要某个变量在函数本次调用结束后继续保留变量值，则可以在定义时用static进行声明  
局部变量用static声明之后会存放在静态存储区，称为静态局部变量  
静态类型的变量会长期占用内存，且使用过多会造成代码混乱，非必要则不使用静态局部变量  
注意：虽然函数调用结束后，静态局部变量仍然存在，但其他函数也不能去调用它  
```
# include <stdio.h>
# include <iostream>
using namespace std;

void static_test()
{
	int i = 0;
	static int j = 0;  //j为static类型，函数结束后变量值不会清空
	i ++;
	j ++;
	cout << "i = " << i << endl;
	cout << "j = " << j << endl;
}

int main()
{
	static_test();  //1 1
	static_test();  //1 2
	static_test();  //1 3
}
```

