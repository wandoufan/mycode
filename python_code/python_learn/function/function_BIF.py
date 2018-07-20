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

# --------------------------------------------------------

# 关于排序函数sorted的具体用法：
# https://www.cnblogs.com/sysu-blackbear/p/3283993.html
# sorted(iterable, cmp=None, key=None, reverse=False) 返回经过排序的可迭代的类型
# iterable：是可迭代类型;
# cmp：用于比较的函数，比较什么由key决定;
# key：用列表元素的某个属性或函数进行作为关键字，有默认值，迭代集合中的一项;
# reverse：排序规则. reverse = True  降序 或者 reverse = False 升序，默认值False。
list_1 = [('d',3),('b',4),('c',2),('a',1)]
list_2 = sorted(list_1, key=lambda x:x[0])# 以每个元组的第一个元素为key进行排序
# 其中'x'变量代表list_1中的每个元组元素
print(list_2)
list_2 = sorted(list_1, key=lambda x:x[1])# 以每个元组的第二个元素为key进行排序
print(list_2)
list_1 = [[1,2,3],[1,2],[2,3,4],[1,2,3,4]]
def f(x):
	return len(x)
# 以每个列表元素的长度为key进行排序，其中key可以为函数，但函数只能有一个参数
list_2 = sorted(list_1,key=f)
print(list_2)

# 另外，列表对象本身也带有排序方法,且方法的参数和sorted函数相同
# L.sort(cmp=None, key=None, reverse=False) 不返回值
list_1 = ['d','b','c','a']
list_1.sort(reverse=True)
print(list_1)


