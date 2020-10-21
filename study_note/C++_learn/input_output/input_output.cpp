# include <stdio.h>
# include <iostream>
using namespace std;

/*关于C++中的输入输出*/

/*
1. C++中使用cin为标准输入流，使用cout为标准输出流，C语言中没有这两项
C语言中常用的scanf和printf在C++中仍然可以使用，C++中cout和cin的更好用
2. cin和cout是C++中预先定义好的流对象，分别代表标准输入设备(键盘)和标准输出设备(显示器)
使用cout进行输出时要紧跟'<<'运算符，使用cin进行输入时要紧跟'>>'运算符
'<<'和'>>'可以自动分析处理数据类型，无需再像printf中那样给出格式控制符
3. 'endl'表示end of line，作用是换行，和C语言中的'\n'完全相同
4. 在C++程序中如果要使用cin和cout等，必须要包含头文件<iostream>
iostream是Input Output Stream的缩写，意思是输入输出流
另外，还要进行命名空间的声明:'using namespace std;'
如果不声明命名空间，则需要使用时'std::cout'或'std::endl'
5. 注意：cout和cin不是C++的关键字，而是ostream和istream类的对象
6. 在命令窗口输入完一个参数后按回车再输入下一个参数
7. 注意：cout方法也不能直接去输出list等复合类型的数据，这一点和python不同
*/


void test1()
{
	printf("test1\n");
	int num1, num2, num3;
	cin >> num1 >> num2 >> num3;
	printf("%d, %d, %d", num3, num2, num1);
}

void test2()
{
	printf("test2\n");
	int num1 = 1, num2 = 2, num3 = 3;
	cout << num1 << endl << num2 << endl << num3 << endl;
}

int main()
{
	// test1();
	test2();
	return 0;
}
