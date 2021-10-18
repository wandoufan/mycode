#include <stdio.h>

/*整理总结C语言中一维数组的基本用法*/

/*
1.数组是有序数据的集合，且数组中每一个元素都属于同一类型
2.数组定义时要声明类型，且定义类型与数组中元素类型一致
3.数组定义时要声明数组大小，且不允许对大小进行动态定义
4.对于一个字符类型的数组，可通过引用数组名或字符指针变量来一次输出一个字符串(不是逐个输出字符)
而对于一个数值类型的数组，不能通过数组名整体输出，只能逐个引用数组元素
5.如果在定义数组时就初始化，且对数组中每一个元素都指定了值，则数组长度可省略
6.数组下标都是从0开始计算，定义的int a[10]数组不存在a[10]元素
7.C语言中不能直接输出数组元素：printf(array[1])，必须用格式符来引用：printf("%d", array[1])
8.注意：当引用数组的下标为负数时(如array[-3])也会指向一个未定义的内存区域，不会有报错，一般会输出一个随机数值
在循环中要注意对数组下标的下限限定为0，否则会向负数无限循环下去
*/

/*
关于数组的长度
C语言中没有直接读取数组长度的函数，必须借助sizeof()
读取数组的字节数，再除以数组元素的字节数
int length = sizeof(a)/sizeof(int);
另外，如果是结构体数组，要写成:
struct student {...};
struct student student_array[3];
int length = sizeof(student_array)/sizeof(struct student)
*/

int main()
{
    void test_init();
    test_init();

    return 0;
}

void test_init()
{
    /*数组元素逐个初始化*/
    int a[10]; /*定义一个长度为10的整型数组*/
    int i;
    for(i = 0; i <= 9; i++)
        a[i] = i;
    for(i = 0; i <= 9; i++)
        printf("%d\n", a[i]);
    printf("\n");

    /*在定义数组时对所有数组元素初始化*/
    int b[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}; /*数组长度可省略*/
    for(i = 0; i <= 9; i++)
        printf("%d\n", b[i]);
    printf("\n");

    int c[10] = {0}; /*对所有数组元素赋一个值，不能写成{0 * 10}*/
    for(i = 0; i <= 9; i++)
        printf("%d\n", c[i]);
    printf("\n");    

    /*在定义数组时对部分数组元素初始化*/
    int d[10] = {0, 1, 2, 3, 4}; /*对前5个元素赋值，其他未指定的元素默认值为0*/
    for(i = 0; i <= 9; i++)
        printf("%d\n", d[i]);
    printf("\n");
}

