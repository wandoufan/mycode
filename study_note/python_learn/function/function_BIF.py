# 主要介绍python中的几个内建函数
# BIF即built in functions,是python的内置函数，在IDLE中输入dir(__builtins__)可以看到内置函数列表
# help(),input(),print()等常见函数都是内置函数，方便快速编程


# 1.内置函数filter(function or None,iterable)实现筛选过滤功能，返回一个filter对象(需要转化为list等类型的对象)
# 若第一个参数是函数，则将第二个参数中每一个元素作为函数的参数计算，并返回值为Ture的元素，舍弃False元素
# 若第一个参数是None，则直接将第二个参数中值为Ture的值筛选出来
# 备注：filter和map的主要区别在于返回值为False的元素是否舍弃

# 示例1：找出列表中值为True的元素
temp1 = filter(None, [1, 'a', 0, False, None])
print(list(temp1))

# 示例2：实现一个筛选奇数的过滤器
def odd(x):
    return x % 2
temp2 = filter(odd, range(10))
print(list(temp2))
# 用lambda表达式简化上述函数为一行
print(list(filter(lambda x: x % 2, range(10))))


# 2.内置函数map(function,iterable)实现映射功能，返回一个map对象(需要转化为list等类型的对象)
# 将可迭代序列的每一个元素作为函数的参数进行运算，并返回所有运算后的结果构成的新序列(包含值为False的元素)
# 第一个参数为运算函数
# 第二个参数为可迭代序列对象

# 示例1：把元素数值都变为原来2倍
def double(x):
    x *= 2
    return x
temp3 = map(double, range(10))
print(list(temp3))
# 用lambda表达式简化上述函数为一行
print(list(map(lambda x: 2 * x, range(10))))

# 示例2：把列表中所有元素都转化为字符串格式
list1 = ['a', 'b', 1, 2]
temp4 = map(str,list1)
print(list(temp4))


# 3.内置函数sorted实现排序功能，返回完成排序后列表list类型
# sorted(iterable, cmp=None, key=None, reverse=False) 返回经过排序的可迭代的类型
# iterable：用于排序的数据，一般是可迭代的对象
# cmp：用于排序的函数，函数接收的参数是key，默认为None
# key：用可迭代对象中每个元素的某个属性作为排序的依据
# reverse：设置排序规则为升序(False)或降序(True)，默认值为升序(False)

# 示例1：以列表中每个元组的第一个元素为key进行排序
list_1 = [('d',3),('b',4),('c',2),('a',1)]
list_2 = sorted(list_1, key=lambda x:x[0])
print(list_2)

# 示例2：以列表中每个元组的第二个元素为key进行排序
list_1 = [('d',3),('b',4),('c',2),('a',1)]
list_2 = sorted(list_1, key=lambda x:x[1])
print(list_2)

# 例子3：以每个列表元素的长度为key进行排序，其中key可以为函数，但函数只能有一个参数
list_1 = [[1,2,3],[1,2],[2,3,4],[1,2,3,4]]
def f(x):
	return len(x)
list_2 = sorted(list_1,key=f)
print(list_2)

# 例子4:按照字典的value的值来排序
dict1 = {'a':3, 'b':1, 'c':7, 'd':4}
result = sorted(dict1.items(), key=lambda x: x[1], reverse=True)

# 特别地，列表对象本身也带有排序方法,且方法的参数和sorted函数相同
# L.sort(cmp=None, key=None, reverse=False)，没有返回值
list_1 = ['d','b','c','a']
list_1.sort(reverse=True)
print(list_1)


