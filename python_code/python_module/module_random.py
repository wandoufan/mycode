# random模块用于产生随机数序列


import random

print(random.randint(1, 5))  # 返回两个参数之间的随机整型
print(random.randrange(1, 9, 2))  # 返回1，9之间且step为2的随机整型
print(random.uniform(0.9, 3.14))  # 返回两个参数之间的随机浮点数
print(random.random())  # 返回0.0和1.0之间的随机浮点数
a = 'hello'
print(random.choice(a))  # 返回给定序列里的一个随机元素


