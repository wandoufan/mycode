# coding:utf-8

# numpy(numeric python)是python科学计算的基础模块
# numpy提供以下功能：
# 快速高效且具有矢量算术运算的多维数组对象ndarray
# 用于对数组执行快速运算的数学函数(无需编写循环)
# 用于读写磁盘数据的数据集工具
# 线性代数运算，傅里叶变换，随机数生成
# 用于将C,C++,Fortran等的代码集成到python工具


import numpy as np# 惯例改名为np



# 代码中实际用到的功能：

# np.random.rand创建一个给定类型的数组，将其填充在一个均匀分布的随机样本[0, 1)中
print(np.random.rand(50))
mask = np.random.rand(50)<0.9
print(mask)

# 将DataFrame类型的数据集划分为测试集和训练集
msk = np.random.rand(len(frame_data)) < 0.9
train_data = frame_data[msk]
test_data = frame_data[~msk]