# include <stdio.h>

/*
给定两个单链表，编写算法找出两个链表的公共结点，并给出算法的时间复杂度。

算法思想：
两个链表有公共结点即说明两个链表在某个结点处相交，拓扑结构是'Y'型的。
1.求出两个单链表的长度len_1和len_2，长度之差为n；
2.用两个指针分别指向两个单链表，让较长链表的指针先移动n步，此时两个链表剩余的长度相同；
3.之后同步遍历两个链表，如果遇到两个指针指向同一个结点，则该结点即为公共结点；
4.如果遍历到链表结束都没有遇到相同结点，则说明两个链表没有公共结点；
算法复杂度为O(len_1 + len_2)。
*/


LNode * search_common_node(LinkList * L1, LinkList * L2)
{
    /*找出两个单链表L1和L2的公共结点*/
    int len_1 = length(L1), len_2 = length(L2); //两个链表的长度分别为len_1和len_2
    LNode * p_long, * p_short;
    if (len_1 < len_2)
    {
        p_long = L2 -> next;
        p_short = L1 -> next;
        n = len_2 -len_1; //两个链表长度之差为n
    }
    else
    {
        p_long = L1-> next;
        p_short = L2 -> next;
        n = len_1 -len_2;
    }

    while(n--) //让较长链表的指针先遍历n个结点，之后再开始同步
    {
        p_long = p_long -> next;
    }

    while(p_long != NULL)
    {
        if (p_long == p_short)
        {
            return p_long; //如果遇到两个指针指向同一个结点，则该结点即为公共结点
        }
        else
        {
            p_long = p_long -> next;
            p_short = p_short -> next;
        }
    }

    return NULL; //如果遍历到链表结束都没有遇到相同结点，则说明两个链表没有公共结点
}