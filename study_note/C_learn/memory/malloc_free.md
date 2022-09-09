# C语言中的内存空间分配

## 基本信息
1. 内存分配相关的几个函数都来自于'cstdlib.h'库
https://www.cnblogs.com/younes/archive/2010/01/23/1654961.html
https://www.zhihu.com/question/478285549/answer/2053162248


## 
动态分配
静态分配

## 
allocate()函数
deallocate()函数


## malloc函数
1. 基本格式
```
void * malloc(unsigned int size);
```
2. 函数功能
在内存的动态存储区域中分配一个长度为size的数据块，数据块是一个连续的内存空间  
注意：新分配的内存空间是没有经过初始化的，保存的是其原有的数据值  
3. 函数参数
size参数：内存空间的长度  
4. 函数返回值
如果分配成功，则返回分配内存的起始地址(空类型指针)；如果分配失败(如内存空间不足)，则返回空指针'NULL'  

## realloc函数
1. 基本格式
```
void * realloc(void * ptr, size_t size);
```
2. 函数功能
重新分配内存空间，将指针ptr指向的内存空间扩大或减少到size尺寸  
3. 函数参数

4. 函数返回值




2. void * calloc(unsigned n, unsigned size);
在内存的动态存储区域中分配n个长度为size的连续空间，函数的返回值是分配域的起始地址  
如果执行失败(如内存空间不足)则返回空指针'NULL'，calloc函数常用来为一维数组分配内存空间  

3. void free(void * p);
释放由p指针指向的动态存储区域，使这部分内存区域可以被其他变量使用，  
其中p是最近一次调用malloc或calloc函数时的返回值，free函数本身没有返回值  
```
int *p = (int*) malloc( sizeof(int) * 10 );  //分配10个int型的内存空间
free(p);  //释放内存
```