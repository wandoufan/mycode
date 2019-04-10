# 主要记录算法方面的基本知识点

## 算法的基本概念
* 算法是对特定问题求解步骤的一种描述，它是指令的有限序列，其中每条指令表示一个或多个操作
* 算法应具有下列5个重要的特性：
* 1.有穷性，一个算法必须在执行有限步后结束，且每一步都可以在有限时间内完成
* 2.确定性，算法中每一条指令必须有确定的含义，对于相同的输入只能得到相同的输出
* 3.可行性，一个算法是可行的，即算法中的操作都可以通过已经实现的基本运算执行有限次来实现
* 4.输入，一个算法可以有零个或多个输入
* 5.输出，一个算法可以有一个或多个输出


## 算法效率的评价指标
* 算法的效率主要通过时间复杂度和空间复杂度来度量

### 时间复杂度
* 时间复杂度描述算法运行时间与运算规模之间的关系
* 算法的时间复杂度记为:T(n) = O(f(n))
* 常见的时间复杂度有：
* O(1) < O(log2n) < O(n) < O(nlog2n) < O(n²) < O(n³) < O(2^n) < O(n!) < O(n^n)
* 关于时间复杂度的判定
> https://www.jianshu.com/p/f4cca5ce055a

### 空间复杂度
* 空间复杂度描述算法运行占用内存空间与运算规模之间的关系
* 算法的空间复杂度记为：S(n) = O(g(n))
* 如果算法需要的存储空间是常数个，即与运算规模n无关，则空间复杂度为O(1)


## 查找算法
* 1.顺序查找/线性查找
* 顺序查找主要用于在线性表中的查找，包括：
* 无序线性表的查找，从线性表一端开始逐个查找是否有满足条件的元素，直到成功或到线性表另一端
* 有序线性表的查找，也是从一端开始查找，但不一定要查完每个元素
* 2.折半查找/二分查找
* 仅适用于有序的顺序表，将给定元素的key值与线性表中间位置元素的key值进行比较，然后递归的进行下去
* 3.分块查找/索引顺序查找
* 将查找表分为若干个子块，块内元素可以无序，但块之间是有序的
* 需要建立一个索引表， 表中存放每个块中最大关键字的值和块的地址

### 散列表(hash)
* 散列函数是把查找表中关键字映射成关键字对应地址的函数
* 散列函数可能会把两个或两个以上的不同关键字映射到同一地址，称为'冲突'，发生冲突的不同关键字称为同义词
* 一方面选取散列函数时要尽可能避免这种冲突，另一方面这种冲突总是不可避免的
* 散列表中存储了关键字和对应存储地址的映射关系，即可以根据散列表直接快速访问关键字的地址，时间复杂度O(1)
* 构造散列函数时应该尽量简单易算，计算出的地址尽量均匀分布到整个地址空间


## 排序算法
* 排序就是重新排列表中的元素，使表中元素按照关键字递增或递减
* 根据排序过程中数据元素是否全部在内存中，可以将排序算法分为两类：
* 内部排序是指在排序过程中元素全部存放在内存中
* 外部排序是指在排序过程中元素无法全部同时存放在内存中，元素在内存和外存之间来回移动
* 外部排序一般都是序列很大，在内存无法一次放下，但要使用时尽量减少内外存之间的交换次数
* 外部排序主要是归并排序，其他的基本都属于内部排序

### 算法的稳定性
* 两个关键字相等的元素，排序前后的顺序不变，称为稳定的排序算法，反之是不稳定的排序算法
* 稳定的算法：冒泡排序，直接插入排序，折半插入排序，归并排序，基数排序
* 不稳定的算法：快排，希尔排序，简单选择排序，堆排序
* 注意，算法是否稳定不是评价算法优劣性的指标

### 插入排序
* 基本思想：将待排序元素按照关键字大小插入到前面已经排序好的子序列中，直到全部元素排序完成
* 1.直接插入排序
* 将待排序元素在已排序好的子序列中逐个比较后插入
* 空间复杂度O(1)，时间复杂度O(n²)
* 适用于已经基本有序的排序表和数据量不大的排序表
* 2.折半插入排序
* 先折半查找出每个待排序元素的待插入位置，再统一插入相应的位置
* 时间复杂度O(n²)
* 3.希尔排序
* 将排序表按一定步长分割为若干个子表，先对每个子表进行直接插入排序，之后再合并起来进行直接插入排序
* 空间复杂度O(1)，时间复杂度O(n²)
* 仅适用于线性表为顺序存储的情况

### 交换排序
* 基本思想：指根据序列中两个元素关键字的比较结果来对换这两个记录在序列中的位置
* 1.冒泡排序
* 从前往后/从后往前两两比较相邻元素的值，如果逆序就交换位置，称为一次冒泡
* 已经确定位置的元素就不再参与下一次冒泡，n个元素的序列至多需要n-1次冒泡
* 一次冒泡至少可以确定一个元素的最终位置
* 空间复杂度O(1)，时间复杂度O(n²)
* 2.快速排序
* 在待排序列中任选一个元素作为基准，将比其大或小的元素分别放在基准两边，称为一次快排
* 然后递归地对两个子表重复上述过程，直到每个子表中只有一个元素或为空时排序完成
* 选取基准元素时尽量选可以将队列均匀中分的元素
* 一次快排至少可以确定一个元素的最终位置
* 空间复杂度O(log2n)，时间复杂度O(nlog2n)
* 在子表规模较小时可以不再递归使用快速排序，对子表使用快速排序完成剩余排序，这样可以提高效率
* 注意，快排是所有内部排序算法中平均性能最优的排序算法

### 选择排序
* 基本思想：在第i趟排序中，从后面n-i+1个待排序元素中选取关键字最小的元素作为有序子序列的第i个元素，直到排序完成
* 1.简单选择排序
* 第i趟排序从剩下元素中选取关键字最小的元素与第i个元素交换，直到排序完成，共需要n-1次排序
* 一趟排序至少可以确定一个元素的最终位置
* 空间复杂度O(1)，时间复杂度O(n²)
* 2.堆排序
* 在排序过程中将待排序列看成一棵完全二叉树的顺序存储结构，利用完全二叉树的特性从序列中选取关键字最大/最小的元素
* 依次选取结构来构造二叉树，过程中不断调整来保证每个子树中根结点都是最大/最小的
* 选关键字最大的元素为根结点称为大根堆/大顶堆，选关键字最小的元素为根结点称为小根堆/小顶堆
* 空间复杂度O(1)，时间复杂度O(nlog2n)

### 归并排序和基数排序
* 1.归并排序
* 归并是将两个或两个以上有序表组合成一个新的有序表
* 初始设每个子表长度为1，然后两两归并，再将长度为2的子表递归地两两归并下去，称为2-路归并排序
* 空间复杂度O(n)，时间复杂度O(nlog2n)
* 注意，归并排序属于外部排序，即数据可以在内存和外村之间交换，尤其适用于对大数据量，小内存量的情况进行排序
* 2.基数排序
* 基数排序不是基于比较进行排序，而是采用多关键字排序思想，即基于关键字每一位(个十百千万)大小进行排序
* 基数排序分为最高位优先排序和最低位优先排序 

### 排序算法的选择
* 对于长度较小(n<=50)的序列，可以选择直接插入排序或简单选择排序
* 对于已经基本有序的序列，可以选择直接插入排序或冒泡排序
* 对于长度较长的序列，可以选择快速排序，堆排序或归并排序
* 当序列长度很大，关键字位数较少且可以分解时，可以选择基数排序
* 对于数据量很大，但只有少量内存的情况(内存不足以放下全部数据)，可以选择归并排序