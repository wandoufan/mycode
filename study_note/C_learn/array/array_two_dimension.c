#include <stdio.h>
#include <string.h>

/*整理总结C语言中二维数组的基本用法*/

/*
1.C语言中二维数组在内存中是按行存放的，即先存放第一行元素，再存放第二行元素
2.C语言中允许使用多维数组，如三维数组：int a[3][4][5]
3.和一维数组一样，二维数组的下标都是从0开始计算，定义int a[3][4]数组不存在a[3][4]元素
*/


void test_number()
/*元素是数字的二维数组*/
{
    int i, j;
    int a[3][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}}; /*定义一个三行四列的整型二维数组*/
    //int b[3][4] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}; /*可以将所有数值写在一个括号内，但要按顺序排列好*/
    //int c[3][4] = {{1}, {5}, {9}}; /*对每行第一个元素赋值，其他未指定元素默认值为0*/
    //int d[3][4] = {{1, 2}, {5, 6}, {0, 0, 11}}; /*可以对部分元素赋值，其他未指定元素默认值为0*/
    //int e[3][4] = {{1, 2}, {5, 6}}; /*可以只对几行元素赋值，其他未指定元素默认值为0*/
    //int f[][4] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}; /*如果指定了全部值，定义时可以省略行数，但不能省略列数*/

    for(i = 0; i <= 2; i++)
    {
        for(j = 0; j <= 3; j++)
            printf("%d,", a[i][j]);
        printf("\n");
    }
}

void test_char()
/*元素是字符的二维数组*/
{
    int i, j;
    //二维数组可以逐个元素输出
    char z[3][5] = {{' ', ' ', '*', ' ', ' '}, {' ', '*', ' ', '*', ' '}, {'*', ' ', ' ', ' ', '*'}};
    for(i = 0; i <= 2; i++)
    {
        for(j = 0; j <= 4; j++)
            printf("%c,", z[i][j]);
        printf("\n");
    }
    printf("\n");

    //二维数组也可以每行都按一个字符串进行输出
    char string_list [5][100] = {"this is string 1", "this is string 2", "this is string 3",
    "this is string 4", "this is string 5"};
    for(i = 0; i < 5; i++)
    {
        printf("%s\n", string_list[i]);
    }
}

void test_char2()
/*给二维字符数组赋值*/
{
    char info[10][100];
    char string[100];
    for(int i = 0; i < 5; i++)
    {
        sprintf(string, "this is %d string\n", i);
        strcpy(info[i], string);//使用strcpy函数
        // info[i] = string; //错误写法
    }
    for(int i = 0; i < 5; i++)
    {
        printf("%s\n", info[i]);
    }
}

int main()
{
    // test_number();
    test_char();

    return 0;
}
