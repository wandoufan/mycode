# 主要介绍python函数中的参数

# 常见的参数包括位置参数、默认参数、关键词参数、可变参数


# 可变参数包括*args和**args，适用于函数的传入参数个数不确定的时候
# *args是若干个变量组成的元组类型
def funargs(*args):  # 可以传入任意数量个参数（包括零个）
    for i in args:
        print(i)
    print(args, type(args))
funargs(1, 2, 3, 4, 5)  # 传入5个参数

# **args是个字典类型，接收的变量必须带有变量名
def funargs(**args):  # 可以传入任意数量个参数（包括零个）
    for i in args:
        print(i)
    print(args, type(args))
funargs(a=1, b=2, c=3, d=4, e=5)  # 传入5个参数


# 关于**kwargs与位置参数、*args、默认参数混着用的问题：（注意顺序）
# 顺序必须是位置参数、*args、**kwargs，不然就会报错
# 另外位置参数必选在默认参数之前，即不能是def func(y=1, x)

# 当三者顺序是:位置参数、默认参数、*args
def foo_1(x, y=1, *args):
    print('x:', x)
    print('y:', y)
    print('*args:', *args)
foo_1(1, 2, 3, 4, 5)  # 其中的x为1，y=1的值被2替换，3,4,5都给args，即args=(3,4,5)

# 当三者顺序是:位置参数、*args、默认参数
def foo_2(x, *args, y=1):
    print('x:', x)
    print('y:', y)
    print('*args:', *args)
foo_2(1, 2, 3, 4, 5)  # 其中的x为1，2,3,4,5都给args，即args=(2,3,4,5),y始终为1
