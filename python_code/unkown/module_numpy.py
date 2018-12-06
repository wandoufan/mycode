# coding:utf-8

# numpy(numeric python)是python科学计算的基础模块，它内部解除了Python的PIL(全局解释器锁),运算效率极好
# numpy提供以下功能：
# 快速高效且具有矢量算术运算的多维数组对象ndarray，它是一系列同类型数据的集合
# 用于对数组执行快速运算的数学函数(无需编写循环)
# 用于读写磁盘数据的数据集工具
# 线性代数运算，傅里叶变换，随机数生成
# 用于将C,C++,Fortran等的代码集成到python工具

# 参考资料：
# https://www.jianshu.com/p/83c8ef18a1e8
# https://www.yiibai.com/numpy/numpy_ndarray_object.html
# http://www.runoob.com/numpy/numpy-tutorial.html

import numpy as np# 惯例改名为np


# 1.创建Ndarray对象
# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
# object参数：指定用于创建Ndarray对象的数据来源，可以是一个列表或其他数据类型
# dtype参数：指定数组元素中的数据类型,如complex, float, str, list等
# copy参数：指明对象是否需要复制
# order参数：指定创建数组的样式，C为行方向，F为列方向，A为任意方向(默认)
# subok参数：默认返回一个与基类类型一致的数组
# ndmin参数：指定生成数组的最小维度
a = np.array([1, 2, 3, 4])# 用列表创建一维数组
print(a)
a = np.array((1, 2, 3, 4))# 用元组创建一维数组
print(a)
a = np.array([[1, 2, 3, 4], ['a', 'b', 'c', 'd'], ['A', 'B', 'C', 'D']])# 用列表创建三维数组
print(a)
a = np.array((1, 2, 3, 4), ndmin=2)# 指定数组最小维度为2
print(a)
a = np.array((1, 2, 3, 4), dtype=complex)# 指定数组元素为复数
print(a)

# 2.Ndarray对象的属性
# 数组的维数称为秩(rank)，一维数组的秩为 1，二维数组的秩为 2，以此类推
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# ndarray.ndim 返回数组的维数，即数组的秩
print(a.ndim)# 维数一直是2？？？2维代表平面？？理解维数的概念？？？
# ndarray.shape 返回数组的形状，返回一个元组类型，元组的长度即为数组的维数
print(a.shape)
# ndarray.shape也可以用于调整数组的大小
# a.shape = (3, 3)


















# 代码中实际用到的功能：

# np.random.rand创建一个给定类型的数组，将其填充在一个均匀分布的随机样本[0, 1)中
# print(np.random.rand(50))
# mask = np.random.rand(50)<0.9
# print(mask)

# 将DataFrame类型的数据集划分为测试集和训练集
# msk = np.random.rand(len(frame_data)) < 0.9
# train_data = frame_data[msk]
# test_data = frame_data[~msk]
