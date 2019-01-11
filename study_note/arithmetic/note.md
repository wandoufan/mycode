# 算法笔记

* 关于排序算法的稳定性（两个相同值的数据排序前后顺序是否改变）：
稳定的：冒泡，直接插入排序，归并排序，基数排序
不稳定的：快排，希尔排序，简单选择排序，堆排序

* 删除二叉树结点或链表结点：
python中对资源的释放采用引用计数的方式，不同于C语言中可以直接free掉。
因此删除树或链表中的结点不能直接对结点本身采用del等操作。
修改结点的父结点(前后结点)的next指针，使结点本身不再被引用即可。

* 判断链表中的结点是否是尾结点：
用node.next is None来判断