#include <stdio.h>

/*整理总结C语言中的基础语法*/

/*
1.C语言中用双斜杠//注释掉一行或用来写注释，python中用#注释掉一行
2.代码开头的#include <stdio.h>语句用来将库函数都加入程序中，之后可以直接调用库函数，即standard input & output
3.C程序没有行号，许多编译器支持一行内写多个语句，或一个语句写在多行上，每个语句后必须用分号做结尾
4.C代码太长时可以直接用 \ 进行换行，和python中一样
*/


int main()
{
   printf("Hello, World!!!! \n");
   /* 这是C语言中注释的格式 */
   // printf("C语言中用双斜杠注释掉一行，python中用#注释掉一行");
   printf("代码太长时可以用\
   	进行换行，\
   	写在每行的最后");
   return 0;
}

