# IDLE是一个python shell，即可以利用IDLE这个shell与python交互，windows的cmd窗口和Linux的命令窗口都是shell
# BIF即built in functions,是python的内置函数，在IDLE中输入dir(__builtins__)可以看到内置函数列表
# help(),input(),print()等常见函数都是内置函数，方便快速编程

# filter和map的主要区别在于返回值为False的元素是否舍弃

# 内置函数filter(function or None,iterable)实现筛选过滤功能
# 若第一个参数是函数，则将第二个参数中每一个元素作为函数的参数计算，并返回值为Ture的元素，舍弃False元素
# 若第一个参数是None，则直接将第二个参数中值为Ture的值筛选出来

temp1 = filter(None, [1, 'a', 0, False, None])
print(list(temp1))

# 用filter()函数写出一个筛选奇数的过滤器


def odd(x):
    return x % 2
temp2 = filter(odd, range(10))
print(list(temp2))

# 用lambda表达式简化上述函数为一行
print(list(filter(lambda x: x % 2, range(10))))

# 内置函数map(function,iterable)实现映射功能
# 将可迭代序列的每一个元素作为函数的参数进行运算，并返回所有运算后的结果构成的新序列


def double(x):
    x *= 2
    return x
temp3 = map(double, range(10))
print(list(temp3))

list1 = ['a', 'b', 1, 2]
# 把列表中所有元素都转化为字符串格式
temp4 = map(str,list1)
# 把列表各个元素按行排列
temp5 = '\n'.join(map(str,list1))
print(temp5)

# 用lambda表达式简化上述函数为一行
print(list(map(lambda x: 2 * x, range(10))))
