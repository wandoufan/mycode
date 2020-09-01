#include <stdio.h>

/*整理总结C语言中函数的基本用法*/

/*
1.C程序都是从main函数开始的，在main函数中调用其他函数，之后结束整个程序的运行
一个C程序至少且仅包含一个main函数，main函数可以放在代码的开头、中间、结尾
2.函数间可以相互调用，但不能调用main函数
3.void表示无类型，函数执行后不会向main函数返回任何值
4.如果定义函数时候不指定函数类型，系统会默认函数为int型
5.C语言中实参向形参传递的是具体数值，而不是变量地址，因此单向传递，只能由实参传给形参，不能由形参传回实参
实参和形参在内存中对应不同的地址，因此数值变动后也不会相互影响
7.C语言中函数可以相互调用，但不能在一个函数中定义另一个函数，这一点和python不一样

8.数组名可以作为实参和形参，传递的数组第一个元素的地址
用数组名作为函数参数时，形参应该对应为数组名或指针变量
注意：用数组名传参时，实参和形参对应同一个地址，如果形参变化，实参会随之变化，这一点与常规的值传递方式不同
9.数组元素也可以作为函数的实参，此时传递的就是数值，而不是地址
10.用数组名作为参数时，应在调用函数和被调用函数分别定义数组，且数组类型必须一致，否则报错
11.作为形参的一维数组可以不指定大小，数组名后面跟一个空的括号即可
12.也可以用二维数组名作为实参和形参，在被调用函数中对形参定义时可以省略第一维的大小
并且在第二维大小相同的前提下，形参数组的第一维可以实参数组的第一维不同
注意：二维数组在作为函数形参时，第一维大小可以省略，但第二维大小必须指明 int matrix[][4];
*/

int main()
{
    void func_1(); /*调用函数前要先对被调用的函数进行声明*/
    func_1(); /*正式调用func_1函数*/

    int func_2(int x, int y); /*x、y是形参*/
    int a, b, c;
    a = 1;
    b = 2;
    c = func_2(a, b); /*a,b是实参*/
    printf("sum is %d \n", c);

    void func_3();
    func_3(); /*调用空函数时不会执行任何操作*/

    float func_array(int score[], int count);
    int grade[] = {92, 81, 65, 77, 42, 88, 70};
    int n = 7;
    printf("the average grade is %.2f\n", func_array(grade, n));

    return 0;
}


void func_1() /*无参函数*/
{
    printf("this is a test\n");
}


int func_2(int x, int y) /*有参函数*/
{
    int z;
    z = x + y;
    return 5; /*函数可以有多个return语句，只有最上边的执行*/
    return z;
}

void func_3() /*空函数，相当于预留函数*/
{

}


float func_array(int score[], int count) /*数组作为函数参数*/
/*求平均成绩*/
{
    int i, sum = 0;
    float average;
    for(i = 0; i < count; i++)
    {
        sum = sum + score[i];
    }
    average = sum / count;
    return average;
}