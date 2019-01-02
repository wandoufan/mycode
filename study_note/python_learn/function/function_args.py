# 主要介绍python函数中的参数
# 常见的参数包括位置参数、默认参数、关键字参数、可变参数

# 1.位置参数
# 位置参数就是在调用函数时根据参数的位置来传递参数
# 注意：传递参数时参数的位置顺序和个数都必须一一对应
def func(x, y, z):
    print(x, y, z)

# 2.默认参数
# 在定义函数时就为参数指定了默认值，调用函数时默认参数的值可以传也可以不传
# 注意：默认参数必须在位置参数之后，即不能是def func(y=1, x)的形式
def func(x, y=1):
    print(x, y)

# 3.关键字参数
# 在调用参数时用键-值的形式传递，使用时更加清晰，而且不再有参数的位置顺序要求
# 注意：关键字参数之间不要求顺序，但有位置参数时，关键字参数必须在位置参数之后
def func(name, age):
    print(name, age)
func(name='jack', age=10)
func(age=10, name='jack')
func('jack', age=10)
# func(age=10, 'jack')  # 错误的写法
print('\n')

# 4.可变参数
# 可变参数包括*args和**kwargs，适用于函数的传入参数个数不确定的时候
# 注意：可变参数必须在位置参数之后，其中**kwargs参数必须在*args参数之后
# *args是若干个变量组成的元组类型
def funargs(*args):  # 可以传入任意数量个参数（包括零个）
    print(args, type(args))
funargs(1, 2, 3, 4, 5)  # 传入5个参数
# **args是若干个变量组成的字典类型，接收的变量必须带有变量名
def funargs(**kwargs):  # 可以传入任意数量个参数（包括零个）
    print(kwargs, type(kwargs))
funargs(a=1, b=2, c=3, d=4, e=5)  # 传入5个参数
print('\n')


# 5.参数之间的混合使用问题：
# 当三者顺序是:位置参数、默认参数、*args
def foo_1(x, y=1, *args):
    print('x:', x)
    print('y:', y)
    print('*args:', *args)
foo_1(1, 2, 3, 4, 5)  # 其中的x为1，y=1的值被2替换，3,4,5都给args，即args=(3,4,5)
print('\n')

# 当三者顺序是:位置参数、*args、默认参数
def foo_2(x, *args, y=1):
    print('x:', x)
    print('y:', y)
    print('*args:', *args)
foo_2(1, 2, 3, 4, 5)  # 其中的x为1，2,3,4,5都给args，即args=(2,3,4,5),y始终为1
print('\n')

# 当*args和**kwargs参数混合使用时
def foo_3(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)
    print('\n')
foo_3(1, 2, 3, 4)
foo_3(a=1, b=2, c=3)
foo_3(1, 2, 3, 4, a=1, b=2, c=3)
foo_3('a', 1, None, a=1, b='2', c=3)
# foo_3(a=1, b=2, c=3, 1, 2, 3, 4)  # 错误写法
