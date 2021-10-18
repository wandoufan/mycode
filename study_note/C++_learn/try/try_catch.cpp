#include "stdio.h"

/*C++中用try-catch-throw实现异常处理*/



void try_1(int a, int b)
/*标准的写法示例*/
{
	try
	{
		if(b == 0)
		{
			throw 1; //抛出一个int类型的异常
			printf("异常：被除数为0\n");
		}
		else if(a == 0)
		{
			throw 1.1; //抛出一个double类型的异常
			printf("异常：除数为0\n");
		}
		else
			printf("%d\n", a/b);
	}
	catch(double j)
	{
		printf("catch double error：%f\n", j);
	}
	catch(int i)
	{
		printf("catch int error：%d\n", i);
	}
	catch(...)
	{
		printf("匹配所有的异常，只能作为最后一个catch块\n");
	}
}

void try_2(int a, int b)
/*错误写法示例：抛出异常类型与catch()块的类型不一样*/
{
	try
	{
		if(b == 0)
		{
			throw 1; //抛出一个int类型的异常
			printf("异常：被除数为0\n");
		}
		else
			printf("%d\n", a/b);
	}
	catch(double j)
	{
		printf("catch double error：%f\n", j);
	}
}


int main()
{
	try_1(2, 0); //抛出异常
	try_1(0, 2); //抛出异常
	try_1(2, 1); //正常执行

	// try_2(2, 0);

	return 0;
}