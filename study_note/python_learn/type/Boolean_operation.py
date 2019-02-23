# 主要介绍python对象的布尔值以及逻辑运算符


# 1.bool函数用来判断对象的布尔值，返回True或False
# 所有的空对象，括号，值为零的所有数字等，它们的布尔值都是false
print(bool(0))
print(bool(0.0))
print(bool(()))  # 空元组
print(bool([]))  # 空列表
print(bool({}))  # 空字典
print(bool(''))  # 空字符串
print(bool(False))
print(bool(None))
# 所有非零的数字，非空对象等，它们的布尔值都是True
print(bool(-2))
print(bool(1))
print(bool(3.14))
print(bool('hello'))
print(bool(True))
print('\n')


# 2.id函数用来获取对象的内存地址
# 如果数据对象的id属性相同，那么它们的type和value属性也一定相同
# 如果两个变量的内存地址相同，那么它们就是同一对象
a = 1
b = 3-2
print(id(a))
print(id(b))
# 用is和is not可以判断两个变量是否指向了同一对象
print(a is b)
print(a is not b)


# 3.逻辑运算符(容易出错的知识点)
# x or y: if x is true,then x,else y   返回x或y的值
# 当x为true时返回x，当x为false时返回y
# 注意：返回的是x或y的值，不是True或False
print(0 or 0)
print(1 or 0)
print(0 or 1)
print(1 or 2)
# x and y: if x is true,then y,else x   返回x或y的值
# 注意：当x为ture时返回的是y，当x为false时返回的才是x
print(0 and 0)
print(1 and 0)
print(0 and 1)
print(1 and 2)
# not x    返回True或False
print(not 1)
print(not 0)
print('\n')

# -----------------------------------------------------------

# 例子1：判断对象是否是同一个id
seq = '12345'
print(seq is seq[:])
print('\n')

# 例子2：逻辑运算符
# 备注：比较运算符的优先级高于逻辑运算符
print('a' > 'b' or 'c')
print('a' < 'b' or 'c')
print('a' > 'b' and 'c')
print('a' < 'b' and 'c')
