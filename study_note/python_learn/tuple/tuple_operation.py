# 主要记录python中的元组类型

# 元组属于不可变数据类型，包含任意数目的各种python对象，使用圆括号()来定义,可以用做字典的key

# 元组和列表的比较：
# 相同点：都是序列，都可以根据索引访问，都可以存放任何类型数据
# 不同点：list用[]创建，tuple用()创建;list可变，tuple不可变;
# python一般分配较大内存块给tuple，因为它不可变，较小内存块给list，因此大量元素时tuple比list快


# 声明一个元祖
tuple_1 = ()
print(type(tuple_1))

# 元组创建赋值
atuple = (123, 'abc', 3.14, ['alist', 456], 3 - 4j)
# 注意：当元组只有一个元素时需要加一个逗号，否则会被当作是其他数据类型
btuple = (123,) # 不能写为btuple = (123)
print(type(btuple))
print(type(123))
ctuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tuple('abc'))
print(type(btuple).__name__)

# 访问元组的值
print('输出第一个元素', atuple[0])
print('输出最后一个元素', atuple[-1])
print('输出子列表的子元素', atuple[3][1])
print('输出相反的序列', atuple[::-1])

# 更新元组，元组是不可变类型，只能像字符串一样构造一个新的
atuple[3][1] = 789  # 元组本身不可变，但元组中的可变部分如列表元素可以改变
print(atuple)
ctuple = ctuple[0], ctuple[4], ctuple[-1]
print(ctuple)
dtuple = btuple + ctuple
print(dtuple)
btuple *= 2
print(btuple)

# 判断对象是否成员列表
print(123 in atuple)
print(123 not in atuple)

x, y = 1, 2
print(x, y)
