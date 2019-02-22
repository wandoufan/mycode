# 常见面试问题：
## TCP协议的三次握手和四次挥手？
## OSI/ISO七层协议？TCP/IP的四层协议？



* -----------------------------------

# 实际面试中遇到的问题：
## 一行代码实现99乘法表

## 字符串的常用方法
## 字典按值排序
## 装饰器功能及示例
## 字符串翻转的多种方法
* string[::-1];result = sorted(string);

## filter函数
## map函数
## 写一个有打印功能的装饰器
## vim三种状态
* 一般模式(查、删、复制)，编辑模式(增、改)，命令行模式

## python提高效率的方法

## list和tuple的区别
* 相同点：都是序列，都可以根据索引访问，都可以存放任何类型数据
* 不同点：list用[]创建，tuple用()创建;list可变，tuple不可变;
* python一般分配较大内存块给tuple，因为它不可变，较小内存块给list，因此大量元素时tuple比list快

## hash函数将字符串格式的数据映射到5个数据库
```
def hash_func(data):
    num = id(data)
    return num%5
```

## yield的用法
## 迭代器和生成器的区别
## cookie和session的区别，http是无连接的，如何识别不同的用户？
## python中的静态方法，全局方法，XX方法的区别？
## 如何判断单链表是否有环？

## python读取大文件
* 用句柄的readlines方法会把数据都加入内存，读取大文件时会内存溢出
* 直接用迭代的方法读取，每次只往内存中加入一部分数据
```
with open('test.text', 'r') as f:
    for each_line in f:
        print(each_line)
```

## 双重列表乘5的结果
```
[[]]*5
```

## 类中的属性，及初始化问题
```
a = test()
print(a.__dict__)
```

## id(seq[:])==id(seq)
```
True
```


## 有一个无重复数字的整数数组，求最大升序子序列，时间复杂度限定在O(nlogn)