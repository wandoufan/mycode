# 主要介绍类型判断函数type()及相关的类型转换函数

# 1.type()以一个对象作为参数，并返回该对象的类型
print(type(4.0))
print(type('$*!'))
print(type(type(4)))
# 其中type对象的__name__属性可以返回简短的类型属性
print(type(4).__name__)
print('\n')

# 2.isinstance()用来判断对象是否是某种指定的数据类型，如果是返回True,如果不是返回False
# 第一个参数是要判断的对象，第二个参数是指定的数据类型(可以有多个类型)
num = 3.14
print(isinstance(num, (int, float, complex)))  # 判断对象是否是个数字
print('\n')

# 3.转换对象类型的函数
# 转换为整型数，对象必须是整数或浮点数或整数数字组成的字符串
print(int('4'))
print(int(3.6))
# 转换为浮点数，对象必须是整数或浮点数或数字组成的字符串
print(float('3.14'))
print(float(4)) 
# 转换为复数，对象必须是数字 
print(complex(3)) 
# 转换为列表，对象必须是可迭代对象 
print(list('abcd')) 
# 转换为元组，对象必须是可迭代对象  
print(tuple('abcd'))
# 转换为字符串，相当于对对象直接加引号'' 
print(str([1, 2, 'b', 3, 'c', 4]))
# 转换为字符串，相当于对对象直接加引号'' 
print(repr(3.1415))
print('\n')