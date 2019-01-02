# 使用关键字lambda来创建匿名函数
# lambda表达式的语法：冒号左边放函数参数，多个参数用逗号隔开，冒号右边是返回值
# 使用lambda表达式可以简化函数定义的过程，对于快速执行脚本或调用较少的函数更方便，不需要考虑函数起名问题


# 原函数
def calculate(x, y):
    return 2 * x + y

# print(calculate(2, 1))

# 使用lambda表达式来定义函数,例子中表达式返回一个函数对象，因此使用时需要进行赋值操作
g = lambda x, y: 2 * x + y
print(g(2,1))
