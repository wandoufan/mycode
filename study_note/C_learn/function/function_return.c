# include <stdio.h>

/*函数的常用返回值*/

/*
1.C语言中的return只能返回一个值，这一点和python不一样，
如果需要返回多个数值，需要将多个数值组合成数组或结构体等复合结构后按一个参数返回
如果函数类型和return的类型不一致，以函数类型为准
2.一个函数可以返回整型值、字符值、实型值等，也可以返回一个指针类型的数据，即地址
返回指针型的函数：类型名 * 函数名(参数列表); 
其中函数的类型名应与返回指针所指向的数据类型一致
3.返回指针的函数定义为'int func()'，即不写'*'，实际也可以运行
但会有警告：'return makes integer from pointer without a cast'
*/


int main()
{
    int * function_return_pointer(int matrix[][3], int x, int y); /*x是矩阵的行数，y是矩阵的列数*/
    int matrix_1[2][3] = {{1, 2, 3}, {4, 5, 6}};

    int * p, * q, i = 0; /*用p指针指向数组的首地址，q指针对数组进行遍历*/
    p = function_return_pointer(matrix_1, 2, 3);

    for (q = p; q < p + 2 * 3; q++)
    {
        printf("%d, ", *q);
        if (i == 2) /*每3个元素换一行*/
        {
            printf("\n");
            i = 0;
        }
        else
            i ++;
    }

    return 0;
}


int * function_return_pointer(int matrix[][3], int x, int y) /*返回指针的函数*/
/*函数功能：将矩阵的数值加1，之后返回矩阵的地址*/
{
    for (int i = 0; i < x; i ++)
    {
        for (int j = 0; j < y; j++)
        {
            matrix[i][j] += 1;
        }
    }

    return matrix;
}