#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
读写二进制文件和文本文件
*/


void read1()
{
	FILE *fp;
	fp = fopen("D:\\share\\test.txt", "rb");
	if(fp == NULL)
	{
		printf("open failed!\n");
	}
	else
	{
		printf("open successd!\n");
		int a[10];
		int count = fread(a, sizeof(int), 10, fp);
		printf("%d\n", count);
		for(int i = 0; i < 10; i++)
		{
			printf("%d, ", a[i]);
		}
		fclose(fp);
	}
}

void write1()
{
	FILE *fp;
	fp = fopen("D:\\share\\test.txt", "wb");
		if(fp == NULL)
	{
		printf("open failed!\n");
	}
	else
	{
		printf("open successed!\n");
		int a[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
		int count = fwrite(a, sizeof(int), 10, fp);
		printf("%d\n", count);
		fclose(fp);
	}
}

void read2()
{
	FILE *fp;
	fp = fopen("D:\\share\\test2.txt", "rb");
		if(fp == NULL)
	{
		printf("open failed!\n");
	}
	else
	{
		printf("open successed!\n");
		struct student
		{
			int num;
			char name[20];
			char sex;
			int age;
			float score;
		};
		struct student student_array[3];
		int count = fread(student_array, sizeof(struct student), 3, fp);
		printf("%d\n", count);
		for(int i = 0; i < 3; i++)
		{
			printf("num: %d, name: %s, sex: %c, age: %d, score: .1%f\n", student_array[i].num, \
				student_array[i].name, student_array[i].sex, student_array[i].age, student_array[i].score);
		}
		fclose(fp);
	}
}

void write2()
{
	FILE *fp;
	fp = fopen("D:\\share\\test2.txt", "wb");
		if(fp == NULL)
	{
		printf("open failed!\n");
	}
	else
	{
		printf("open successed!\n");

		struct student
		{
			int num;
			char name[20];
			char sex;
			int age;
			float score;
		};
		struct student student_array[3] = {{1001, "li ming", 'M', 16, 90.0}, \
		{1002, "zhang", 'F', 15, 80.0}, {1003, "wang", 'M', 17, 70.0}};
		int count = fwrite(student_array, sizeof(struct student), 3, fp);
		printf("%d\n", count);
		fclose(fp);
	}
}


void read3()
{
	FILE *fp;
	fp = fopen("D:\\share\\test3.txt", "rb");
	if(fp == NULL)
	{
		printf("open failed!\n");
	}
	else
	{
		printf("open successd!\n");
		// char a[100];
		// int count = fread(a, sizeof(char), 30, fp);
		// printf("%d\n", count);
		char a[100] = "abcdsf124fa3";
		for(int i = 0; i < 10; i++)
		{
			printf("%c\n", a[i]);
		}
		printf("%s\n", a);
		fclose(fp);
	}
}

void write3()
{
	FILE *fp;
	fp = fopen("D:\\share\\test3.txt", "wb");
		if(fp == NULL)
	{
		printf("open failed!\n");
	}
	else
	{
		printf("open successed!\n");
		char a[100] = "这是一段中文";
		// char a[100] = "abcdsf124fa3";
		int count = fwrite(a, sizeof(char), 30, fp);
		printf("%d\n", count);
		fclose(fp);
	}
}

void read4()
{
	FILE *fp;
	fp = fopen("D:\\share\\test4.txt", "rb");
	if(fp == NULL)
	{
		printf("open failed!\n");
	}
	else
	{
		printf("open successd!\n");
		int a;
		char b;
		char str[100];
		int count = fscanf(fp, "%d\n%c\n%s\n", &a, &b, str);
		printf("%d\n", count);
		printf("%d %c %s\n", a, b, str);
		fclose(fp);
	}
}

void write4()
{
	FILE *fp;
	fp = fopen("D:\\share\\test4.txt", "wb");
		if(fp == NULL)
	{
		printf("open failed!\n");
	}
	else
	{
		printf("open successed!\n");
		int a = 1;
		char b = 'a';
		char str[] = "this is a string!";
		int count = fprintf(fp, "%d\n%c\n%s\n", a, b, str);
		printf("%d\n", count);
		fclose(fp);
	}
}

void read5()
{
	FILE *fp;
	fp = fopen("D:\\share\\test2.txt", "rb");
		if(fp == NULL)
	{
		printf("open failed!\n");
	}
	else
	{
		printf("open successed!\n");
		struct student
		{
			int num;
			char name[20];
			char sex;
			int age;
			float score;
		};
		struct student student_array[3];

		fseek(fp, sizeof(struct student), 1);
		printf("%d\n", ftell(fp));
		int count = fread(student_array, sizeof(struct student), 1, fp);
		printf("%d\n", count);
		printf("%d\n", sizeof(student_array)/sizeof(struct student));
		printf("num: %d, name: %s, sex: %c, age: %d, score: .1%f\n", student_array[0].num, \
			student_array[0].name, student_array[0].sex, student_array[0].age, student_array[0].score);
		fclose(fp);
	}
}

int main()
{
	// read1();
	// write1();
	// read2();
	// write2();
	// read3();
	// write3();
	// read4();
	// write4();
	read5();
}