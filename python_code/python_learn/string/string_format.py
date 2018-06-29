
# format是用来格式化字符串的函数,类似与格式化操作符%,通过{}和:来代替%
# 函数会自动把format中的变量参数都填入{}中

# format函数的常见用法：
name = 'xyf'
action = 'good'
print('hello,{},{}!'.format(name, action))

# 通过{}中的位置参数
print('hello,{1},{0}!'.format(name, action))
print('hello,{0},{1},{0}!'.format(name, action))

# 通过{}中的关键字参数
print('{name} is {age} years old'.format(name='Tom', age=18))

# 通过映射列表
list_1 = ['Tom',18]
print('{0[0]} is {0[1]} years old'.format(list_1))

# 通过映射字典
dict_1 = {'name':'Tom','age':18}
print('{name} is {age} years old'.format(**dict_1))

# 填充与对齐
print('{:>30}'.format('右移30个位置'))
print('{:1>30}'.format('右移30个位置,并用1填充'))

# 保留小数的精度位数
print('{:.2f}'.format(3.1415))

# 用作金额的千位分隔符
print('{:,}'.format(123456789))

# 用作进制转换
print('{:b}'.format(18))# 转换为二进制
print('{:d}'.format(18))# 转换为十进制
print('{:o}'.format(18))# 转换为八进制
print('{:x}'.format(18))# 转换为十六进制