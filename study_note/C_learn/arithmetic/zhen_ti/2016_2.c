# include <stdio.h>

/*
试编写一个算法，给有向无环图G中每个顶点赋以一个整数序号，并满足以下条件：
若从顶点i到顶点j有一条弧，则应使i < j。

算法思想：
拓扑排序中每个顶点出现且仅出现一次，如果顶点j排在顶点i后面，则图中不存在从顶点j到顶点i的路径。
对有向无环图中所有顶点进行拓扑排序，然后按拓扑顺序对第一个顶点赋值为1，之后依次加1，最后一个顶点赋值n。
拓扑排序算法：
1.有向无环图(DAG)中选择一个没有前驱(即入度为0)的顶点输出；
2.从图中删除该顶点和所有以该顶点为弧尾的弧；
3.重复以上操作，直到有向无环图为空，所有顶点已被输出；
*/

void topological_sort(Graph * G)
{
    InitStack(S); //初始化一个栈S，用来存储当前所有入度为0的顶点
    for (int i = 0; i < G.vertex_num; i++)
    {
        if (indegree(i) == 0) //如果顶点i入度为0，则将其存入栈中
            Push(S, i);
    }
    int count = 0; //记录当前已经输出的顶点数
    struct Node sort_list[G.vertex_num] //存储输出的顶点

    while(! StackEmpty(S))
    {
        Pop(S, i); //输出顶点i
        sort_list[count] = i; //将顶点i存入输出列表中
        count ++; //输出个数加1
        for (int j = 0; j < G.vertex_num; j++)
        {
            if (i -> next == j) //如果存在顶点i到顶点j的弧，则将顶点j的入度减1
            {
                j.indegree -= 1;
            }
            if (indegree(j) == 0) //如果顶点j的入度为0，则将顶点j也存入栈中
            {
                Push(S, j);
            }
        }
    }

    for (int k = 0; k < G.vertex_num; k++)
    {
        sort_list[k].value = k + 1; //按输出的拓扑顺序依次对顶点赋一个序号，编号为从1到n
    }
}