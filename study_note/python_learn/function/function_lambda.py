# 主要介绍lambda表达式

# lambda表达式实际是一种匿名函数，通过lambda关键字来创建
# result = lambda param1, param2,...: function
# lambda表达式的语法：冒号左边放函数参数，多个参数用逗号隔开，冒号右边是返回值
# 使用lambda表达式可以使代码更简洁，对于快速执行脚本或调用较少的函数更方便，不需要考虑函数起名问题


# 示例1：把元素数值都变为原来2倍(冒号右边可以调用一个函数)
def double(x):
    return 2*x
func = lambda x: double(x)
print(func(2))

# 示例2：计算2*x+y的值(冒号右边可以直接是函数中的计算过程)
func = lambda x, y: 2 * x + y
print(func(2, 1))
