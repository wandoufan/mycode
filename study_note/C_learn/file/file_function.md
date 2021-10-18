# 文件读写函数

## 注意事项
1. 执行读写函数之后，文件指针会自动移动到下一个位置
2. 读取二进制文件之前，必须知道文件中的数据格式(类型，长度)，也就是说，读的格式必须和写的格式一致


## 以字符形式读写文件
1. int fgetc(FILE \*fp);
从指定文件读取一个字符
如果读取到了文件末尾，则函数会返回一个文件结束标志EOF(即-1)
对于文本文件，字符的ASCII码值不可能是-1，因此读到-1时就代表文件已经结束
对于二进制文件，某个字节的二进制数据可能刚好是-1，因此不能再用EOF判断，改用feof函数判断
```
char ch;
ch = fgetc(fp);
//判断文本文件
while(ch != EOF)
{
	printf("%c", ch);
	ch = fgetc(fp);
}
//判断二进制文件
while(!feof(fp))
{
	ch = fgetc(fp);
}
```

2. int fputc(int ch, FILE \*fp);
向指定文件中写入一个字符
写入成功，则返回写入的字符；写入失败，则返回EOF
```
char ch = 'a';
fputc(ch, fp);
```


## 以字符串形式读写文件
1. char \*fgets(char \*str, int n, FILE \*fp);
从指定的文件中读取一个字符串，并保存到字符数组中
读取成功，则返回字符数组首地址str；读取失败，则返回NULL；读取到了文件末尾，也返回NULL
str参数代表字符数组
n参数代表要读取的字符数目
注意：读到的字符串会在末尾自动添加'\0'，n个字符中也包括'\0'，即实际只有n-1个字符，如果希望读100个字符，n值应该是101
```
char str[10];
fgets(str, 5, fp);
printf("%s\n", str);
```
注意：在读取过程中如果遇到了换行，则读取会提前结束，也就是说，不管n多大，一次最多只能读一行数据
备注：C语言中没有按行读取文件的函数，只要把n设的足够大，fgets函数就能实现按行读取的效果
```
char str[100];
while(fgets(str, 100, fp) != NULL)
{
	printf("%s\n", str);
}
```

2. int fputs(char \*str, FILE \*fp);
向指定文件中写入一个字符串
写入成功，则返回一个非负值(一般是0)；写入失败，则返回一个EOF
备注：如果需要写入多行数据，每行数据末尾用\n进行换行
```
char str[100] = "this is a test\n";
if(fputs(str, fp) != EOF)
{
	printf("write successed!\n");
}
```


## 以数据块形式读写文件(常用)
注意：fread()和fwrite()函数都应该以二进制的形式打开文件
备注：数据块可以是一个字符，可以是一个字符串，也可以是多行数据，没有具体的限制
1. size_t fread(void \*ptr, size_t size, size_t count, FILE \*fp);
从指定文件中读取数据块，数据量为size * count
读取成功，则返回数据块的个数count；如果返回值小于count，则可能发生了错误，也可能读到了文件末尾
ptr参数代表内存区块中的指针(如数组、变量、结构体等)，用来存放读取到的数据
size参数代表每个数据块的字节数，一般用sizeof(type)，type要和数组中元素类型一致
例如：sizeof(struct student)、sizeof(int)、sizeof(char)
count参数代表要读写的数据块的个数，一般跟数组中元素的个数对应
count参数代表要读写的数据块的个数
```
//读取结构体数组(要定义一个和写入时完全相同的结构体)
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

//读取整型数组
int a[10];
int count = fread(a, sizeof(int), 10, fp);
printf("%d\n", count);
for(int i = 0; i < 10; i++)
{
	printf("%d, ", a[i]);
}

//读取字符数组
char a[100];
int count = fread(a, sizeof(char), 30, fp);
printf("%d\n", count);
printf("%s\n", a);
```

2. size_t fwrite(void \*ptr, size_t size, size_t count, FILE \*fp);
向指定文件中写入数据块，数据量为size * count
写入成功，则返回数据块的个数count；如果返回值小于count，则一定发生了写入错误
ptr参数代表内存区块中的指针(如数组、变量、结构体等)，用来存放要写入的数据
size参数代表每个数据块的字节数，一般用sizeof(type)，type要和数组中元素类型一致
例如：sizeof(struct student)、sizeof(int)、sizeof(char)
count参数代表要读写的数据块的个数，一般跟数组中元素的个数对应
```
//写入结构体数组(记事本打开为乱码)
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

//写入整型数组(记事本打开为乱码)
int a[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
int count = fwrite(a, sizeof(int), 10, fp);
printf("%d\n", count);

//写入英文和数字字符数组(记事本打开显示正常)
char a[100] = "this is a fwrite() test12345";
int count = fwrite(a, sizeof(char), 30, fp);
printf("%d\n", count);

//写入中文字符数组(记事本打开显示正常)
char a[100] = "这是一段中文";
int count = fwrite(a, sizeof(char), 30, fp);
printf("%d\n", count);

//写入单个整型变量(记事本打开为乱码)
int a = 1;
int *p;
p = &a;
int count = fwrite(p, sizeof(int), 1, fp);
printf("%d\n", count);

//写入单个字符(记事本打开显示正常)
char a = 'd';
char *p;
p = &a;
int count = fwrite(p, sizeof(int), 1, fp);
printf("%d\n", count);
```


## 格式化读写文件
备注：fscanf()和fprintf()函数与scanf()和printf()功能相似，都是格式化读写函数，区别在于fscanf()和fprintf()的读写对象不是键盘和显示器，而是磁盘文件
备注：fscanf()和fprintf()在输入输出时要进行字符和二进制之间的转换，效率不如fread()和fwrite()函数
1. int fscanf(FILE \*fp, char * format, ...);
从指定文件中读入参数数据，并赋值给参数列表中的参数
读取成功，则返回被成功赋值的参数个数；读取失败，则返回EOF(即-1)
format参数代表格式控制字符串
...参数代表参数列表
注意：和fgetc()函数不同，fscanf()函数在读取字符串的时候，遇到字符串中的空格和换行就会提前结束
```
int a;
char b;
char str[100];
int count = fscanf(fp, "%d\n%c\n%s\n", &a, &b, str); //读取格式要和写入格式完全一致
printf("%d\n", count);
printf("%d %c %s\n", a, b, str);
```

2. int fprintf(FILE \*fp, char * format, ...);
向指定文件中写入参数数据
写入成功，则返回写入字符的个数(注意不是参数个数)；写入失败，则返回一个负数
format参数代表格式控制字符串
...参数代表参数列表
```
int a = 1;
char b = 'a';
char str[] = "this is a string!";
int count = fprintf(fp, "%d\n%c\n%s\n", a, b, str);
printf("%d\n", count);
```


## 移动文件指针实现随机读写
1. int fseek(FILE \*fp, long offset, int origin);
改变文件指针的当前位置
执行成功，则返回0；执行失败，则返回-1
offset参数代表位移量，是相对于起始点向前移动的字节数，数字的后面要加上L
origin参数代表起始点，其中，0代表文件开头，1代表当前位置，2代表文件末尾
备注：fseek()函数一般用于二进制文本，在文本文件中由于要进行转换，计算的位置有时候会出错
```
fseek(fp, 100L, 0); //文件指针移动到文件开头后面100个字节处
fseek(fp, 50L, 1); //文件指针移动到当前位置后面50个字节处
fseek(fp, -10L, 2); //文件指针移动到文件末尾前面10个字节处
```
```
//结构体数组中有三条记录，移动指针，只读取文件中的第二条记录
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
```

2. void rewind (FILE \*fp);
使文件指针重新返回文件的开头，函数没有返回值

3. long ftell(FILE \*fp);
返回文件指针的当前位置，位置用相对于文件开头的位移量来表示
如果出错，则返回-1L
```
if(ftell(fp) == -1L)
{
	printf("error\n");
}
```


## 检测文件读写状态
1. int feof(FILE \*fp);
如果文件指针到了文件末尾，则函数返回一个非零值；如果文件指针没有到文件末尾，则函数返回0；

2. int ferror(FILE \*fp);
在调用各种输入输出函数时，如果出现错误，除了输入输出函数本身的返回值，还可以用ferror函数进行检查
如果返回值为0，表示未出错；如果返回值为非零值，则表示出错；
备注：对同一个文件，每次调用输入输出函数，都会产生一个新的ferror函数值，因此调用后要立刻获取ferror函数值，否则信息会丢失
备注：对同一个文件，如果没有再次调用输入输出函数，则之前产生的ferror函数值就会一直保留
```
if(ferror(fp))
{
	printf("读取出错");
}
else
{
	printf("读取成功");
}
```

3. void clearerr(FILE \*fp);
使feof()和ferror()的返回值都重置为0
