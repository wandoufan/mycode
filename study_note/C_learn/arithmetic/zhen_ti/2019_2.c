# include <stdio.h>

/*
输入一串数字字符串，写程序对字符串进行翻转。

算法思想：
用头指针指向字符串的第一个元素，尾指针指向字符串的最后一个元素。
将头指针和尾指针指向的元素进行交换，之后将头指针加1，尾指针减1。
重复以上操作直到头指针和尾指针相遇，此时的字符串就是翻转后的字符串。
*/  
 
char * reverse_string(char *string)
/*对字符串进行翻转，返回翻转后的字符串*/
{
    char temp;
    char *head = string;
    char *tail = string;
    while (*tail != '\0') /*将尾指针指向最后一个元素*/
    {
        tail++;
    }
    tail--;
 
    while (head < tail) /*依次交换头尾指针指向的元素*/
    {
        temp = *head;
        *head = *tail;
        *tail = temp;
        head ++;
        tail --;
    }

    return string; /*返回翻转后的字符串*/
}

int main()
{
    char a[] = "123456";
    printf("%s\n", reverse_string(a));
    return 0;
}