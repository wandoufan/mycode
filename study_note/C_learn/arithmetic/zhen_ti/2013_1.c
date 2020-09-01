# include <stdio.h>

/*
已知顺序表有n个记录，表中记录不依关键字有序排列，编写一算法为该顺序表建立一个有序的索引表（依关键字递增排列），
索引表中的每一项应含有记录的关键字和该记录在顺序表中的序号。要求算法的时间复杂度在最好的情况下能够达到O(n)。

算法思想：
要求算法的时间复杂度在最好情况下能够达到O(n)，因此可以次用直接插入排序。
假设顺序表中的前i-1个元素为有序子序列，对于第i个元素找出其在有序子表中要插入的位置k，
将位置K后的元素都向后移动1个位置，然后将第i个元素复制到位置k上。
反复执行以上操作，直到整个顺序表有序，共需要执行n-1次。
*/


int main()
{
    int a[] = {5, 8, 3, 1, 9, 6, 4, 2, 7, 10};
    int *p, n = 10;
    int * Insert_Sort(int array[], int n);
    p = Insert_Sort(a, n);

    for (int i = 0; i < n; i ++)
    {
        printf("%d\n", * (p + i));
    }
}


int * Insert_Sort(int array[], int n) /*n代表记录的个数*/
/*直接插入排序*/
{
    int i, j, temp;
    for (i = 1; i <= n; i++)
    {
        if (array[i] < array[i - 1])
        {
            temp = array[i];
            for (j = i - 1; temp < array[j] && j >= 0; j--)
            {
                array[j + 1] = array[j]; /*将元素都向后挪一位*/
            }
            array[j + 1] = temp;
        }
        for (int k = 0; k < 10; k++)
        {
            printf("%d,", array[k]);
        }
        printf("\n");
    }

    return array;
}