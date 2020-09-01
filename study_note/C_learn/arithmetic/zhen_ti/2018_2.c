# include <stdio.h>

/*
选用合适的数据结构进行矩阵A和矩阵B的运算，运算规则是矩阵A和矩阵B中对应元素如果相同，
那么矩阵C中对应元素等于A或B；如果A和B中对应元素不相同，那么矩阵C中对应元素为两元素相加之和。

算法思想：
使用二维数组来实现矩阵结构，依次遍历矩阵A和矩阵B的元素并将对应元素进行比较。
如果两个矩阵中元素值相同，在矩阵C中对应元素的值也等于A或B中的元素值。
如果两个矩阵中元素值不同，在矩阵C中对应元素的值等于A和B元素相加之和。
*/


int * matrix(int matrix_A[][3], int matrix_B[][3], int x, int y) /*x是矩阵的行数，y是矩阵的列数*/
/*矩阵运算*/
{
    int matrix_C[x][y];
    for (int i = 0; i < x; i ++)
    {
        for (int j = 0; j < y; j++)
        {
            if (matrix_A[i][j] == matrix_B[i][j])
                matrix_C[i][j] = matrix_A[i][j];
            else
                matrix_C[i][j] = matrix_A[i][j] + matrix_B[i][j];
        }
    }

    return matrix_C;
}


void main()
{
    int matrix_A[2][3] = {{1, 2, 3}, {4, 5, 6}};
    int matrix_B[2][3] = {{1, 3, 3}, {4, 5, 1}};
    int * p, * q; /*用p指针指向数组的首地址，q指针对数组进行遍历*/
    p = matrix(matrix_A, matrix_B, 2, 3);
    for (q = p; q < p + 6; q ++)
    {
        printf("%d\n", *q);
    }
}