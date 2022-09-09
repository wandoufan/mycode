#include <stdio.h>
#include <string.h>

/*
memcpy()函数的用法
1. 标准形式
void *memcpy(void *str1, const void *str2, size_t n);
从存储区 str2 复制 n 个字节到存储区 str1
注意：使用前要先'# include <string.h>'

2. 作用
一个是用来拷贝字符串，功能类似于strncpy(str1, str2, n)
另一个是用来拷贝结构体等数据类型，实现内存拷贝，这个功能更重要
*/


void memcpy_test1()//拷贝字符串
{
	char str1[50] = "http://www.baidu.com";
	char str2[50];
	memcpy(str2, str1, 4);
	printf("%s\n", str2);
}

void memcpy_test2()//拷贝结构体
{
	//定义结构体
	struct Student
	{
		char name[10];
		int age;
		float score;
	};
	struct Student student1;
	strcpy(student1.name, "zhang");
	student1.age = 10;
	student1.score = 88.88;
	//使用把memcpy()方法把结构体都拷贝到字符数组中
	char temp1[sizeof(Student)];
	memcpy(temp1, &student1, sizeof(Student));
	printf("%s\n", temp1);
}

int main()
{
	memcpy_test1();
	memcpy_test2();
	return 0;
}