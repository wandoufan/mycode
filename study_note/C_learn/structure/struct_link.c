#include <stdio.h>

/*用结构体来构建链表*/

/*
1.结构体变量适合作为链表的结点
2.静态链表：链表中所有的结点都是在程序中预先定义好的，不是临时开辟的
3.一般最后一个结点的next指向'NULL'作为判断的链表结束的条件
4.动态链表：动态的分配链表的存储空间，当有新结点时才去开辟新的存储空间
*/


int main()
{
    void link_static();
    link_static();

    void link_dynamic();
    link_dynamic();

    return 0;
}


void link_static()
/*建立一个静态的单链表*/
{
    struct student
    {
        int num;
        float score;
        struct student * next; /*在结构体中定义一个结构体类型的指针*/
    }student_1, student_2, student_3;

    student_1.num = 1001;
    student_1.score = 90.0;
    student_2.num = 1002;
    student_2.score = 80.0;
    student_3.num = 1003;
    student_3.score = 70.0;

    struct student * head, * p; /*指向链表结点的指针要和链表结点的类型一致*/
    head = & student_1; /*头指针指向第一个结点*/
    student_1.next = & student_2;
    student_2.next = & student_3;
    student_3.next = NULL; /*最后一个结点的next指向'NULL'*/
    p = head; /*p是用来进行遍历的指针*/

    while(p != NULL)
    {
        printf("%d, %.1f\n", p -> num, p -> score);
        p = p -> next;
    }
}


void link_dynamic()
/*构建一个动态函数*/
{

}