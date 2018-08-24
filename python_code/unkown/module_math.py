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