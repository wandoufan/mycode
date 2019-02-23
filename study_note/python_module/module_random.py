# random模块用于产生随机数序列，提供随机相关的功能

import random


# 1.返回两个整数之间的随机整数
# 注意：随机整数是包含范围区间的端点值的
print(random.randint(1, 5))

# 2.返回两个整数之间且固定步长的随机整数
print(random.randrange(1, 9, 2))

# 3.返回两个浮点数之间的随机浮点数
print(random.uniform(0.9, 3.14))

# 4.返回0.0和1.0之间的随机浮点数
print(random.random())

# 5.返回给定序列里的一个随机元素
string = 'hello'
print(random.choice(string))
num_list = [1, 2, 3, 4]
print(random.choice(num_list))

# 6.random.seed()方法可以使多次生成的随机数相同
count = 0
while count < 5:
    random.seed(1)
    print(random.random())
    count += 1
