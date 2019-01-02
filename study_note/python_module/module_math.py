# coding:utf-8

# math库提供相对复杂的数学计算功能
# 参考资料：
# https://www.cnblogs.com/renpingsheng/p/7171950.html

import math

# math.pi函数返回圆周率常量
print(math.pi)

# math.degrees(x)把弧度转换为角度，360°角=2π弧度，1弧度=57°角
print(math.degrees(1))
print(math.degrees(math.pi))

# math.radians(x)把角度转换为弧度
print(math.radians(180))

# math.cos(x)返回x的余弦，x为弧度
print(math.cos(math.pi))

# math.sin(x)返回x的正弦，x为弧度
print(math.sin(math.pi))

# math.tan(x)返回x的正切，x为弧度
print(math.tan(math.pi))

# math.e函数返回自然常数常量
print(math.e)

# math.log(x[, base])函数提供求对数功能，base表示底数，默认为自然常数e(约为2.71828)
print(math.log(3))# 即ln3
print(math.log(8, 2))# 即以2为底8的对数

# math.log10(x)函数返回以10为底x的对数
print(math.log10(8))# 即以10为底8的对数

# math.log2(x)返回以2为底x的对数
print(math.log2(8))

# math.pow(x, y)函数返回x的y次方，相当于x**y
print(math.pow(2, 3))# 即2的3次方

# math.sqrt(x)函数返回x的平方根
print(math.sqrt(9))# 即9的平方根

# math.exp(x)函数返回e的x次方，e是自然常数2.718
print(math.exp(2))# 即e的平方

# math.ceil(x)函数返回大于等于x的最小整数值，如果x是整数就返回x本身
print(math.ceil(3.14))
print(math.ceil(3))

# math.trunc(x)赶回x的整数部分
print(math.trunc(3.14))

# math.modf(x)返回由x的小数部分和整数部分组成的元组
print(math.modf(3.14))

# math.fabs(x)返回x的绝对值
print(math.fabs(-1))

# math.factorial(x)返回x的阶乘
print(math.factorial(5))

# math.gcd(x, y)返回x,y的最大公约数
print(math.gcd(20, 8))

# math.isnan判断x是否为数字，当x为整数或小数则返回False，其他情况下报错
# 备注：判断对象是否为数字还可以用isinstance()函数
print(math.isnan(3))
print(math.isnan(3.14))




# ------------------------------------------------------------------------------------------
# 使用样例：
def sigmoid(x):
    """
    Sigmoid函数是单增长的S型函数，常被用作神经网络的阈值函数，可以将变量x(x范围在负无穷到正无穷之间)映射到0,1之间
    其中math.exp(-x)代表自然常数e的-x次方， 函数图像是第一二象限间的S型的单调增长函数，其中x = 0时y = 1/2
    """
    return 1.0 / (1 + math.exp(-x))

def tanh(x):
    """
    tanh函数即双曲正切函数，可以将变量x(x范围在负无穷到正无穷之间)映射到-1,1之间
    函数图像是第一三象限间的S型单调增长函数，其中x = 0 时y = 0
    """
    return (math.exp(x) - math.exp(-x))/(math.exp(x) + math.exp(-x))

def relu(x):
    """
    relu函数即线性整流函数，又称线性修正单元，具有线性、非饱和的特性
    """
    if x <= 0:
        return 0
    else:
        return x
        