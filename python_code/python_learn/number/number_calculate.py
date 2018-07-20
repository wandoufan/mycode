a = -0X12  # 0x表示十六进制
print(a, '\n')
b = 3**2
print(b, '\n')
aComplex = 2.3 - 4.5j
print(aComplex.real, '\n')  # 该复数的实部
print(aComplex.imag, '\n')  # 该复数的虚部
print(aComplex.conjugate(), '\n')  # 返回该复数的共轭复数

# //表示地板除
a = 1 // 2
print(a)
b = 1.0 // 2.0
print(b)

# /表示真正的除法
c = 1 / 2
print(c)
d = 1.0 / 2.0
print(d)
print('\n')

# %表示取余
a = 12
a %= 8
print(a)
b = 12.0
b %= 8.0
print(b)

# **表示幂运算
a = 3**2
b = -3**2  # **优先级比-高
c = (-3)**2
d = 4**-1  # **优先级比-低
print(a, b, c, d)

# 位操作符（只适用于整型）
print(~12)  # ~为取反，结果为-（num+1)
print(12 << 3)  # 左移3位
print(12 >> 3)  # 右移3位
print(12 & 3)  # 按位与运算
print(12 ^ 3)  # 按位异或运算
print(12 | 3)  # 按位或运算

# 赋值运算符:
a += b  # 加法赋值运算符
a = a + b
a -= b  # 减法赋值运算符
a = a - b
a *= b  # 乘法赋值运算符
a = a * b
a /= b  # 除法赋值运算符
a = a / b
a **= b  # 幂赋值运算符
a = a**b
a %= b  # 取余运算符
a = a % b
a //= b # 地板除运算符
a = a // b
