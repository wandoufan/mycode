# coding:utf-8

# math库提供相对复杂的数学计算功能
# 参考资料：
# https://www.cnblogs.com/renpingsheng/p/7171950.html

import math

# math.log(x[, base])函数提供求对数功能，base表示底数，默认为自然常数e(约为2.71828)
print(math.log(3))# 即ln3
print(math.log(8, 2))# 即以2为底8的对数

# math.log10(x)函数返回以10为底x的对数
print(math.log10(8))# 即以10为底8的对数

# math.pow(x, y)函数返回x的y次方
print(math.pow(2, 3))# 即2的3次方

# math.sqrt(x)函数返回x的平方根
print(math.sqrt(9))# 即9的平方根

# math.exp(x)函数返回e的x次方，e是自然常数2.718
print(math.exp(2))# 即e的平方


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
        