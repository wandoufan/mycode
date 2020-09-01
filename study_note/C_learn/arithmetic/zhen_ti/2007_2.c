# include <stdio.h>

/*
给定一棵用二叉链表表示的二叉树，编写算法计算指定的某一层k(k > 1)上的叶结点数目。

算法思想：
对二叉树进行层序遍历，采用一个队列结构存储遍历到的结点，用一个指针指向当前遍历层的最后一个结点。
当第k-1层的最后一个结点出队时，队列剩余的结点都是第k层的结点。
对第k层的结点进行遍历，若结点既没有左孩子也没有右孩子，则该结点为叶子结点。
层序遍历算法：
先将二叉树的根结点入队，然后出队，判断其是否有左孩子，如果有，将其左孩子入队。
判断其是否有右孩子，如果有，将其右孩子入队，重复以上操作直到队列为空。
*/


int get_node_num(BiTree * T, int k)
{
    //计算第k层上的叶结点数目
    int leaf_count = 0; //定义leaf_num来存储叶结点的数目
    int level = 1; //定义level来表示当前遍历到的层数
    InitQueue(Q); //初始化一个队列Q用来存储结点
    EnQueue(Q, T); //将第一个结点入队
    BiTNode * tail; //定义一个尾结点指针指向每层的最后一个结点
    tail = Q -> rear; //尾指针指向队列最后一个元素

    while(level < k)
    {
        DeQueue(Q, x);
        if (x -> lchild != NULL)
        {
            EnQueue(Q, x -> lchild); //如果结点x有左孩子，将左孩子入队
        }
        if (x -> rchild != NULL)
        {
            EnQueue(Q, x -> rchild); //如果结点x有右孩子，将右孩子入队
        }
        if (tail == x); //如果当前的出队元素就是该层的最后一个元素，则让尾指针重新指向队列
        {
            tail = Q -> rear;
            level += 1; //将当前遍历层数加1
        }
    }

    while(! QueueEmpty(Q)) //对第k层的结点逐个遍历，如果既没有左孩子也没有右孩子，则说明是叶子结点
    {
        DeQueue(Q, y);
        if (y -> lchild == NULL && x -> rchild == NULL)
        {
            leaf_count += 1;
        }
    }

    return leaf_count; //返回第k层叶子结点的个数
}