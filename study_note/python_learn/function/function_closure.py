# 主要介绍python函数中的闭包closure概念

# 如果一个函数引用了其外层函数中的变量(不是全局变量)，且外层函数的返回值是该函数的引用，则该函数就是闭包的


# 示例1：test2是一个闭包函数
# 注意：test1中的变量x也是局部变量，但是在test1的内部函数test2中也只能对x进行访问，不能修改
def test1(x):
    print('x:', x)
    def test2(y):
        print('y:', y)
        return x * y
    return test2

print(test1(5))  # x为5，y没有赋值
print('\n')
print(test1(5)(8))  # x为5，y为8


# 示例2：装饰器中的wrapper函数是经典的闭包函数
import logging

def get_run_log(func):
    """
    装饰器函数，记录包含函数名的日志信息
    """
    def wrapper(*args):
        logging.info('%s is running !' %func.__name__)
        func(*args)
    return wrapper

@get_run_log
def test1():
    pass

test1()