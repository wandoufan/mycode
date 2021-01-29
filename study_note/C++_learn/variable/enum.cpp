# include <stdio.h>
# include <typeinfo>
# include <iostream>
using namespace std;

/*枚举类型enum的用法*/

/*
1. 枚举常量只能是标识符，不能是整型、字符、字符串等常量
错误写法：'enum week {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};'
2. 枚举常量表中要列出所有的取值，取值之间要以','隔开，且取值必须各不相同
枚举类型名和常量名一般都要首字母大写
3. 编译系统为每个枚举常量指定一个整数值，即所列举元素的序号，默认从0开始，依次加1
枚举变量占用内存的大小与整型数相同
4. 可以在定义枚举类型时为部分或全部枚举常量指定整数值，在指定值之前的枚举常量仍按默认方式取值，
而指定值之后的枚举常量按依次加1的原则取值， 各枚举常量的整数值可以重复
5. 枚举变量只能参与赋值和关系运算以及输出操作，参与运算时用其本身的整数值
6. 枚举类型在实际应用中常与switch-case结构搭配使用
*/

void enum_init1()
{
	/*
	使用方式1
	先定义枚举类型：'enum <类型名> {<枚举常量表>};'
	在定义枚举变量：'<类型名> <变量名>;'
	*/
	enum week {Sun, Mon , Tue, Wed, Thu, Fri, Sat};
	// 注意：两个枚举类型中的常量名不能有重复的，否则会产生冲突
	enum Day {Sun, Mon, Day1, Day2};
	// 注意：枚举类型名和常量名也不能有重复，否则也会报错
	enum Sun {Sun1, Sun2, Sun3};
	week today;
}

void enum_init2()
{
	/*
	使用方式2
	类型和变量同时定义，此时类型名可以省略不写
	'enum [类型名] {<枚举常量表>} <变量名>;'
	*/
	enum {Sun, Mon , Tue, Wed, Thu, Fri, Sat} day1, day2;
}

void enum_index()
{
	/*
	改变枚举常量的序号
	在指定值之前的枚举常量仍按默认方式取值，
	而指定值之后的枚举常量按依次加1的原则取值， 各枚举常量的整数值可以重复
	*/
	// enum week {Sun, Mon, Tue, Wed, Thu, Fri, Sat};
	// enum week {Sun, Mon = 3, Tue, Wed, Thu, Fri, Sat};
	// enum week {Sun, Mon = 3, Tue, Wed, Thu = 3, Fri, Sat};
	enum week {Sun, Mon = 3, Tue, Wed, Thu = 1, Fri, Sat};
	cout << Sun << endl;
	cout << Mon << endl;
	cout << Tue << endl;
	cout << Wed << endl;
	cout << Thu << endl;
	cout << Fri << endl;
	cout << Sat << endl;
}

void enum_calculate()
{
	/*枚举类型的运算*/
	enum week {Sun, Mon , Tue, Wed, Thu, Fri, Sat};
	week day1, day2, day3;
	day1 = Mon;//将枚举常量赋值给枚举变量
	cout << day1 << endl;//输出值为整型序号值
	int i = day1;//枚举变量可以赋值给整型变量
	cout << i << endl;
	day2 = day1;//枚举变量可以赋值给另一个同类型的枚举变量
	cout << day2 << endl;
	int j = Thu;//枚举常量可以赋值给整型变量
	cout << j << endl;
	day3 = (week) 5;//可以通过枚举类型加序号，来给枚举变量赋值
	cout << day3 << endl;
	//错误写法：直接把整型赋值给枚举变量
	// day1 = 1;
}

void enum_compare()
{
	/*枚举类型的比较，结果为0或1*/
	enum week {Sun, Mon , Tue, Wed, Thu, Fri, Sat};
	week day1, day2;
	day1 = Mon;
	day2 = Thu;
	cout << (day1 > day2) << endl;
	cout << (day1 == Mon) << endl;
	cout << (day2 < Sat) << endl;
}

/*
关于枚举变量取值时用按位或符号'|'的问题
在QT程序中遇到了一种很少见的用法，枚举变量在取值时可以一次取多个值，值之间用'|'隔开
应用场景：休息日rest_day可以同时具有sunday和saturday两种取值
其中，枚举常量的取值必须都是2的幂数
备注：资料很少，没有完全搞明白具体用法
*/
void enum_example1()
{
    /*取值用按位或符号示例*/
    enum Week {Sunday=1, Monday=2, Tuesday=4, Wensday=8, \
    	Thursday=16, Friday=32, Saturday=64};
    // Week rest_day = Week::Sunday | Week::Saturday;
}

int main()
{
	enum_init1();
	// enum_init2();
	// enum_calculate();
	// enum_compare();
	// enum_index();
	// enum_example1();
	return 0;
}