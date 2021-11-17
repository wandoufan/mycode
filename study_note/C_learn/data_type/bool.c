#include <stdio.h>

/*整理总结C语言中逻辑运算符和逻辑表达式的基本用法*/
// 注意：C语言中没有布尔类型的变量，只有C++中有提供bool类型

/*
1.C语言中在表示逻辑运算结果时，数值'1'代表真，数值'0'代表假(逻辑运算结果只能是0或1)
cout << true << endl; //return 1
cout << false << endl; //return 0
但在判断布尔值时，0为假，任何非0数值都为真
布尔值为真：1，'a'，'-1'
布尔值为假：0，0.0，
备注：true和false不能直接拿来判断真假

2.运算优先级：非! > 算术运算符 > 关系运算符 > 与&& > 或|| > 赋值运算符

3.a && b && c中，只有a为真时，才会往下判断b和c，当a为假时，表达式b和c就不会执行
a || b || c中，只有a为假时，才会往下判断b和c，当a为真时，表达式b和c就不会执行
*/

int main()
{
    printf("%d\n", 1 && 1);
    printf("%d\n", 1 && 0);
    printf("%d\n", 0 && 1);
    printf("%d\n", 0 && 0);
    printf("\n");

    printf("%d\n", 1 || 1);
    printf("%d\n", 1 || 0);
    printf("%d\n", 0 || 1);
    printf("%d\n", 0 || 0);
    printf("\n");

    printf("%d\n", ! 0);
    printf("%d\n", ! 1);

    return 0;
}



