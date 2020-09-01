# include <stdio.h>

/*
编写一个算法，判断一个无向图G是否为一棵树。若是一棵树，则算法返回true，否则返回false。

算法思想：
如果无向图是一棵树，则图是一个含有n个结点和n-1条边的无向联通图。
对于无向图来说，如果图是联通的，则从任意结点出发，仅需一次遍历就可以访问图中的所有顶点。
采用深度优先遍历算法(DFS)对无向图进行遍历，如果一次遍历就能得到n个结点和n-1条边，
则说明是一个树，否则无法构成一棵树。
深度优先遍历算法(DFS)：从图中某一起始点v开始，访问与v邻接且未被访问过的任意顶点w1，
再访问与w1邻接且未被访问过的任意顶点w2，重复上述操作直到不能继续向下访问，
再依次回退到上一级的其他未被访问过的顶点，直到图中所有顶点都被访问过为止。
*/

bool graph_is_tree(Graph * G)
{
    //判断图G是否是一棵树，如果是则返回true，否则返回false
    int i, visited[G.vertex_num];
    for(i = 0; i < G.vertex_num; i++)
    {
        visited[i] = no; //构建一个访问状态数组，且初始状态都置为未访问
    }

    int visited_vertex_num = 0; //记录访问过的结点数
    int visited_edge_num = 0; //记录访问过的边数
    int v = 0; //要访问的结点
    dfs(G, v, & visited_vertex_num, & visited_edge_num, visited[]); //对v点进行深度优先遍历

    if(visited_vertex_num == G.vertex_num && visited_edge_num == 2 * (G.vertex_num - 1))
    //如果一次访问得到了n个结点和n-1条边，则是一棵树，否则不是一棵树
        return true;
    else
        return false;
}

void dfs(Graph * G, int v, int * visited_vertex_num, int * visited_edge_num, int visited[])
{
    //对图G中的V点进行深度优先遍历
    visit(v); //对v点进行访问
    visited[v] = yes; //v点的访问状态置为yes
    visited_vertex_num ++; //访问过的结点数加1

    for (w = first_neighbor(G, v); w >= 0; w = next_neighbor(G, v, w)) //对v点往下进行递归遍历
    {
        visited_edge_num ++; //访问过的边数加1
        if (! visited[w])
        {
            dfs(G, w, & visited_vertex_num, & visited_edge_num, visited[]);
        }
    }
}