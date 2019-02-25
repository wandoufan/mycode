# 主要记录python中字符串类型的相关操作
# 字符串是不可变的序列类型
# python不支持单字符类型char，即单字符在python属于长度为1的字符串 


# 判断是否成员符，并返回ture或false
A = 'hello,world!'
print('hello'in A)
print('hello' not in A)

# 正向索引
print(A[0])  # 0表示第一位
print(A[-1])  # -1表示最后一位
print(A[1:4])
print(A[::-1])
print(A[5:], '\n')

# 反向索引
final_index = -len(A)  # 定义反向索引
print(A[-1])  # -1表示最后一个
print(A[-12])  # -len(A)表示第一个

# 改变字符串的内容,字符串属于不可变数据类型，不能直接用A[2]='b'的形式改变内容
print(A[:6] + 'python')
print('\n')

# 删除字符串中的字符
print('删除字符o', A[:4] + A[5:])

# 清空字符串
A = ''
print(A)

# 字符串的加法和乘法
B = 'hello'
C = ','
D = 'world'
print(B + C + D)
print(B * 3 + C + D * 2)
print('\n')

# 字符串按照ASCII码值的大小进行比较
str1 = 'abcd'
str2 = 'xyz'
print(str1 < str2)

# 字符串按照ASCII码值的大小返回最大/最小的字符
print(max(str1))
print(min('abc123'))

print('\n')
