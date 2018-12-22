# 主要介绍python对象的布尔值以及逻辑运算符

# 判断一个对象的布尔值，其中not为'非'

# 8.关于逻辑运算符：
# x or y: if x is true,then x,else y   返回x或y的值
# x and y: if x is true,then y,else x   返回x或y的值
# not x    返回True或False


# 所有的空对象，括号，值为零的所有数字等，它们的布尔值都是false
# 以下类型的数据布尔值都是false
print(not None)
print(not False)
print(not 0)
print(not 0.0)
print(not {})
print(not [])
print(not ())
print(not '')
print('\n')

# bool函数用来判断对象的布尔值
print(bool(0))
print(bool([]))
print(bool(-2))
print(bool(1))
print(bool(3))
print(bool('hello'))

# 判断两个对象的布尔值是否相等
print('abcde' < 'abbde')

print([3, 'abc'] == ['abc', 3])

print(2 + 4 - 3)

print(3 * 4 / 6)

print(3 * 4 // 6)

print(2 < 4)

print(2 >= 4)

print(2 != 4)

print(2 < 4 and 2 > 4)  # 与

print(2 < 4 or 2 > 4)  # 或

print(2 < 3 < 4)

print(not 2 < 4)  # 非

print(2 == 4)

print('\n')
# 用'is'和'is not'判断两个变量是否指向了相同的对象
a = b = 3.14
# id()是python的内建函数，可以用来查看对象的id
print(id(a))
print(id(b))
print(a is b)
print(a is not b)

print('\n')

x = 'hat'
y = 'hat'
print(id(x))
print(id(y))
print(x is y)
print(x is not y)


