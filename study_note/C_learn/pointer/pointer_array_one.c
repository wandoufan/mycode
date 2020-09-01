#include <stdio.h>

/*C语言中用指针指向一维数组*/


/*
1.引用数组元素可以通过下标法(a[1])，也可以通过指针法(指针指向数组的某一个元素)
2.在C语言中数组名代表数组中首个元素的地址，因此 p = &a[0]; 等价于 p = a;
3.C语言中规定:如果指针p指向了数组中的某个元素，则p+1指向数组中的下一个元素(而不是p指向的地址+1)
p+1实际是p+1*d，d是数组中一个元素所占的字节数
4.p+i就是a[i]的地址，同理a+i也是a[i]的地址，*(p+i)或*(a+i)对应的都是a[i]
5.指向数组的指针也可以带下标，如p[i]和*(p+i)等价
6.各种类型数组的指针都可以进行自加操作(p++)，但不能对数组名进行自加操作(a++)
*/


int main()
{
    void pointer_array();
    pointer_array();

    return 0;
}


void pointer_array()
/*用指针指向数组元素*/
{
    int a[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int * p; /*指针的基类型应与要指向的数组的类型一致*/
    p = & a[0]; /*也可以直接写为p = a;*/
    for(int i = 0; i < 10; i++)
    {
        printf("%d\n", *(p + i)); /*输出a[i]的值*/
        printf("%d\n", *(a + i)); /*输出a[i]的值*/
    }
    for(int j = 0; j < 10; j++)
    {
        printf("%d\n", *p++); /*也可以通过指针的自加操作输出a[i]的值*/
        /*注意：数组名a是一个常量，因此不能进行自加操作(a++)*/
    }
}