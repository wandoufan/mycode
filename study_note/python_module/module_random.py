# random模块用于产生随机数序列，提供随机相关的功能

# 随机数分为伪随机数和真随机数
# 1.真随机数
# 真正的随机数是使用物理现象产生的：比如掷钱币、骰子、转轮等，其结果是不可预测的、不可见的、完全没有规律的
# 2.伪随机数
# 伪随机数是按照一定算法模拟产生出来的，其结果是确定的、可见的
# 因此伪随机是有周期的，经过足够多次的运行，其结果会出现重复
# 计算机不能生产绝对随机的随机数，只能产生伪随机数
# 计算机中的随机函数都是伪随机的，经常会使用时间作为随机因子，通过算法不停迭代产生随机数
# 对于一个随机函数，如果初始的种子seed是相同的，那么后续迭代出的随机数序列也是相同的


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

# 5.返回给定序列对象里的一个随机元素
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
