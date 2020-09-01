# include <stdio.h>

/*
改进有向图的邻接表存储方法，不用遍历整个有向图就可获得某个顶点的出度和入度。编写算法实现改进的有向图邻接表存储。

算法思想：
邻接表法可以直接获得某个顶点的出度，但求顶点的入度时需要遍历整个邻接表。
不遍历整个有向图就获得某个顶点的出度和入度，可以采用十字链表法。
在十字链表中每条弧对应一个弧结点，每个顶点对应一个顶点结点。
弧结点包含5个域：
1.尾域(tailvex)指向弧尾结点；2.头域(headvex)指向弧头结点；3.链域(hlink)指向弧头相同的下一条弧；
4.链域(tlink)指向弧尾相同的下一条弧；5信息域(info)存储弧相关的信息(可省略)。
顶点结点包含3个域：
1.data域存放结点相关的信息；2.firstin域指向以该结点为弧头的弧(不唯一)；
3.firstout域指向以该结点为弧尾的弧(不唯一)。
对于十字链表法，遍历一个顶点就可以获得所有以该顶点为弧头和弧尾的弧，从而获得该顶点的出度和入度。
*/


# def MaxVertexNum 100 //图中顶点的最大数目

typedef struct edge_node //弧结点
{
    int tailvex, headvex; //该弧的尾结点和头结点
    struct edge_node * hlink, * tlink; //该弧的链域
    // info_type info; //该弧的信息域
}EDGE;

typedef struct vertex_node //顶点结点
{
    int data; //顶点结点的相关信息
    EDGE * firstin, * firstout; //该顶点的第一条入弧和出弧   
}VERTEX;

typedef struct graph //十字链表
{
    VERTEX node_list[MaxVertexNum]; //顶点结点数组
    int vertex_num, edge_num; //图的顶点个数和边数   
}GRAPH;