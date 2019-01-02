# abs()返回参数的绝对值
print(abs(4))
print(abs(-4))
print(abs(2 - 3j))
print('\n')

# divmod(a,b)返回的结果是包含商和余数的元组
print(divmod(10, 3))
print(divmod(3, 10))
print(divmod(10, 2.5))
print('\n')


# pow(a,b)相当于a**b,pow(a,b,c)相当于结果对c取余
print(pow(2, 3))
print(pow(2, 3, 5))
print('\n')

# round(a,b)用于对浮点型数a进行四舍五入运算，b参数可以指定精确位数
print(round(3.4))
print(round(3.5))
print(round(3.49999, 2))
print(round(3.51111111, 3))
print(round(-0.5))

print('\n')

# oct()和hex()分别将整型对象转化为八进制和十六进制的字符串，其中0x开头表示十六进制，0开头表示八进制
print(hex(255))
print(oct(255))
print(str(0xff))
a = hex(255)
b = oct(255)
print(a[2], b[1])

# bin()可以将整型数字转化为二进制字符串，0b开头表示二进制
print(bin(12))

print('\n')

# chr()将ASCII码值转化为对应的符号，ord()将符号转化为对于的ASCII码值，码值范围0~255
print(ord('a'))
print(ord('A'))
print(ord('0'))
print(ord('!'))
print(chr(97))
print(chr(65))
print(chr(48))
print(chr(33))

# -------------------------------------------------------------------------

# 例子1：用python实现依次输出a到z
for i in range(ord('a'), ord('a') + 26):
    print(chr(i))
