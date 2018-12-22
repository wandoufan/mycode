# coding:utf-8

# numpy(numeric python)是python科学计算的基础模块，它内部解除了Python的PIL(全局解释器锁),运算效率极好
# numpy主要提供了数组存储结构，由于内部优化后性能很好，很适合存储大量的数据，并且能保持很快的读取运算速率
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

import numpy as np  # 惯例改名为np


# 1.Ndarray对象
# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
# object参数：指定用于创建Ndarray对象的数据来源，可以是一个列表、元组或其他数据类型
# dtype参数：指定数组元素中的数据类型,如complex, float, str, list等
# copy参数：指明对象是否需要复制
# order参数：指定创建数组的样式，C为行方向，F为列方向，A为任意方向(默认)
# subok参数：默认返回一个与基类类型一致的数组
# ndmin参数：指定生成数组的最小维度
a = np.array([1, 2, 3, 4])  # 用列表创建一维数组
print(a)
a = np.array((1, 2, 3, 4))  # 用元组创建一维数组
print(a)
a = np.array([[1, 2, 3, 4], ['a', 'b', 'c', 'd'],
              ['A', 'B', 'C', 'D']])  # 用双层列表创建2维数组
print(a)
a = np.array((1, 2, 3, 4), ndmin=2)  # 指定数组最小维度为2
print(a)
a = np.array((1, 2, 3, 4), dtype=complex)  # 指定数组元素为复数
print(a)

# 2.Ndarray对象的属性
# 数组的维数称为秩(rank)，一维数组的秩为 1，二维数组的秩为 2，以此类推
# 用双层列表创建的数组即为二维数组，用三层列表创建的数组即为三维数组
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# ndarray.ndim 返回数组的维数，即数组的秩
print(a.ndim)
# ndarray.shape 返回数组的形状即n行m列，返回一个元组类型，元组的长度即为数组的维数
print(a.shape)
# ndarray.size 返回数组中元素的总个数，即n*m
print(a.size)
# ndarray.dtype 返回数组对象的元素类型
print(a.dtype)
# ndarray.itemsize 返回数组对象的每个元素大小,以字节为单位
print(a.itemsize)
# ndarray.flags 返回数组对象的内存信息,详细含义参考菜鸟教程
print(a.flags)
# ndarray.real 返回数组元素的实部
print(a.real)
# ndarray.reshape() 重新设置一维数组的形状
print(np.arange(32).reshape(4, 8))

# 3.创建Ndarray数组
# Ndarray对象除了上述numpy.array方法外，还可以用以下几种方法创建
# numpy.empty(shape, dtype = float, order = 'C')创建一个指定形状、数据类型且未初始化的数组
# order参数有'C'和'F'两个选项，分别代表行优先和列优先
# 注意：数组未初始化时，数组中元素为随机值
print(np.empty([3, 2], dtype=int))
# numpy.zeros(shape, dtype = float, order = 'C')创建一个指定大小的数组，数组元素以0来填充
# order参数有'C'和'F'两个选项，分别代表C的行数组和F的列数组
print(np.zeros([3, 2]))
# numpy.ones(shape, dtype = None, order = 'C')创建一个指定大小的数组，数组元素以1来填充
print(np.ones([3, 2]))

# 4.从已有数组中创建数组
# numpy.asarray 类似 numpy.array，但 numpy.asarray 只有三个参数
# numpy.asarray(a, dtype = None, order = None)
a = np.asarray([1, 2, 3])  # 用列表创建数组
print(a)
a = np.asarray([(1, 2, 3), (4, 5, 6)])  # 用列表元组创建数组
print(a)

# 5.从数值范围创建数组
# numpy.arange(start=0, stop, step=1, dtype)
# arange方法从指定范围内创建一维数组
# 参数分别为：起始(默认为0)、终止、步长(默认为1)、数据类型
print(np.arange(1, 15, 2))
# np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
# linspace方法创建一个由等差数列组成的一维数组
# num参数为数组元素个数，默认为50个；endpoint参数设置数列是否包含stop值
print(np.linspace(1, 22, 10, dtype=int))
# np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
# logspace方法创建一个由等比数列组成的数组
# start参数为base**start; stop参数为base**stop；base参数为对数log的底数，默认以10为底
print(np.logspace(0, 6, num=7, base=2))

# 6.Ndarray数组的切片和索引
# ndarray数组对象可以通过下标进行索引(索引值也是从0开始)，并通过内置的slice函数从原数组中切割出一个新的数组
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# slice(start, stop, step), start/stop为起始/终止索引值
print(a[slice(1, 3, 1)])
# ndarray数组也可以通过类似列表的方式来直接切片
print(a[1][2])  # 返回2行3列的元素
print(a[1:3])  # 返回第二行第三行的元素
print(a[1:])  # 返回第二行以后的元素
# 切片中还可以通过省略号...来表示所有元素
print(a[..., 1])  # 返回第二列元素
print(a[1, ...])  # 返回第二行元素
print(a[..., 1:])  # 返回第二列以后的元素
print(a[1, 2])  # 返回2行3列的元素

# 7.Ndarray数组的高级索引
# ndarray数组对象除了用上述的整数或切片作为索引外，还可以采用整数数组索引、布尔索引及花式索引
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
# 整数数组索引，第一个数组中是目标元素的行号，第二个数组中的是目标元素的列号，两个数组组合为目标元素的坐标
print(a[[0, 0, 2, 2], [0, 3, 0, 3, ]])  # 返回数组的四个角的元素
print(a[1:3, 1:3])  # 返回数组中间四个元素
print(a[1:3, [1, 2]])  # 返回数组中间四个元素
# 布尔索引可以通过布尔运算来获取符合指定条件的元素的数组
print(a[a > 5])  # 返回数组中值大于5的元素
# 花式索引指的是利用一个一维整数数组作为索引
# 如果索引目标是一维数组，那么返回就是索引值作为下标的元素；如果索引目标是二维数组，那么返回就是索引值对应的行
a = np.array([1, 2, 3, 4])
print(a[1])  # 一维数组的单个元素可以直接写索引值
print(a[[1, 2, 3]])  # 即使是一维数组也不能写成print(a[1, 2, 3])
a = np.arange(32).reshape(8, 4)
print(a)
print(a[[4, 2, 1, 7]])  # 返回第5、3、2、8行的元素
print(a[[1]])  # 返回第2行的元素
print(a[[-1, -3, -4]])  # 返回倒数第2、4、5行的元素
# 用np.ix_方法传入多个数组，第一个数组为行号，第二个数组为列号
print(a[np.ix_([0, 1, 2, 3], [1, 2])])

# 8.Numpy的广播
# 当两个数组形状相同时(a.shape==b.shape)，a*b的结果就是数组相应位置元素相乘
a = np.arange(16).reshape(4, 4)
b = np.arange(16, 32, 1).reshape(4, 4)
print(a * b)
# 当两个数组形状不同时numpy会自动触发广播机制
a = np.arange(16).reshape(4, 4)
b = np.array([1, 2, 3, 4])
print(a * b)
print(a + b)

# 9.Numpy迭代数组
a = np.arange(16).reshape(4, 4)
# np.nditer方法可以把数组变成一个可以迭代对象，遍历数组中的每个元素
# nditer对象的可选参数order可以设置遍历元素的顺序
for x in np.nditer(a):# 迭代时默认是行优先
    print(x)
for x in np.nditer(a, order='F'):# Fortan order表示列序优先
    print(x)
for x in np.nditer(a, order='C'):# C order表示行序优先
    print(x)
# 在迭代中修改数组元素数值
# nditer对象的可选参数op_flags可以设置数组的读写状态
# 默认情况下为只读对象(read-only)，如果要在遍历时修改元素，要设定为read-write或者write-only
for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2*x # 把元素数值都变为2倍
print(a)
# 数组对象可以直接进行迭代，遍历数组中的每一行
for row in a:
    print(row)
# np.flat方法也可以把数组变成一个可迭代对象，遍历数组中的每个元素
for x in a.flat:
    print(x)

# 10.Numpy数组操作
# ndarray.T返回数组的转置数组
a = np.arange(16).reshape(4, 4)
print(a.T)
# numpy.transpose方法交换数组的维度，相当于转置
print(np.transpose(a))

print('\n', '------------------------------', '\n')

# 代码中实际用到的功能：

# np.random.rand创建一个给定类型的数组，将其填充在一个均匀分布的随机样本[0, 1)中
# print(np.random.rand(50))
# mask = np.random.rand(50)<0.9
# print(mask)

# 将DataFrame类型的数据集划分为测试集和训练集
# msk = np.random.rand(len(frame_data)) < 0.9
# train_data = frame_data[msk]
# test_data = frame_data[~msk]
