# 主要记录python中的修饰器/装饰器(decorators)的用法

# 参考资料：
# http://www.runoob.com/w3cnote/python-func-decorators.html
# https://www.jianshu.com/p/ab702e4d4ba7

# 一、装饰器的基本介绍

# 1.装饰器的定义：
# python装饰器本质上是一个函数/类，它可以协助其他业务函数在不修改代码的情况下增加额外的功能
# 装饰器接收业务函数作为参数，返回值也是一个函数/类对象
# 有了装饰器，我们就可以抽离出大量函数中与函数功能本身无关的雷同代码并继续重用
# 装饰器以@开头并且被放在被装饰函数的上面，相当于给被装饰函数提供了一个功能套件，可帮助代码变得更加简洁

# 备注：以下两种装饰器的写法，实现效果一样
# 写法一：
# @get_run_log
# def test1():
#     pass
# test1()
# 写法二：
# def test1():
#     pass
# test1 = get_run_log(test1)
# test1 = ()

# 2.装饰器的使用场景：
# 典型的装饰器应用场景包括：记录日志信息、测试函数时间性能、事务处理
# 另外在django中有内置的装饰器@login_required，可以帮助检查用户是否已登录

# 3.关于装饰器内部的wrapper函数：
# 一般会在装饰器内部定义一个封装函数wrapper，执行完装饰器的功能后将封装函数wrapper返回
# wrapper函数接收业务函数的参数，在函数内部调用运行业务函数，并根据情况确定是否需要return
# wrapper函数中使用了装饰器的func参数，装饰器返回了wrapper函数，因此wrapper属于闭包函数
# 注意：wrapper函数的参数必须和业务函数的参数一致，方便起见，可以统一写为*args

# 4.装饰器的执行顺序：
# 一个函数可以添加多个装饰器，执行顺序为由近到远，有由内到外
# 如下示例，执行顺序为：c -> b -> a
# @ a
# @ b
# @ c
# def test1():
#     pass
# 等效于func = a(b(c(test1)))


# 二、应用实例

import datetime
import time
import logging
from functools import wraps
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)


# 示例1：给业务函数增加一个装饰器，用来记录每个业务函数的运行日志

def get_run_log(func):
    """
    装饰器函数，记录包含函数名的日志信息
    备注：不一定要在内部定义封装函数wrapper
    装饰器函数接收业务函数，返回的也是业务函数，不存在函数属性改变的问题
    """
    logging.info('%s is running !' %func.__name__)
    return func

def get_run_log(func):
    """
    装饰器函数，记录包含函数名的日志信息
    由于返回的是wrapper函数，业务函数的各个属性会变成wrapper函数的属性
    方法1：可以通过属性拷贝赋值来保留业务函数的元信息
    """
    def wrapper(*args):
        logging.info('%s is running !' %func.__name__)
        func(*args)
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    wrapper.__dict__ = func.__dict__
    return wrapper

def get_run_log(func):
    """
    装饰器函数，记录包含函数名的日志信息
    由于返回的是wrapper函数，业务函数的各个属性会变成wrapper函数的属性
    方法2：给封装函数wrapper加上wraps装饰器，会自动将func函数的属性拷贝给wrapper函数
    """
    @wraps(func)
    def wrapper(*args):
        logging.info('%s is running !' %func.__name__)
        func(*args)
    return wrapper

@get_run_log
def test1(name):
    """
    业务函数1，接收单个参数
    """
    print(name)

@get_run_log
def test2(x, y, z):
    """
    业务函数2，接收多个参数
    """
    print(x + y + z)

def test3():
    """
    业务函数3，不接收参数
    """
    print('test3函数的__name__属性：', test3.__name__)
    print('test3函数的__doc__属性：', test3.__doc__.strip())

test1('Tom')
test2(1, 2, 3)
test3 = get_run_log(test3)
test3()
print('\n')


# 示例2：给业务函数增加一个装饰器，给业务函数输出的字符串两侧添加引号""

def add_quote_mark(func):
    """
    装饰器函数，给字符串两侧添加引号""
    """
    @wraps(func)
    def wrapper(*args):
        return '"' + func(*args) + '"'
    return wrapper

@add_quote_mark
def test1():
    """
    业务函数1，无参数
    """
    return 'test1函数的__name__属性：' + test1.__name__

@add_quote_mark
def test2(string):
    """
    业务函数2，有参数
    """
    return string

print(test1())
print(test2('hello world'))
print('\n')


# 示例3：给函数增加一个装饰器，用来获取每个业务函数的运行时间

def get_run_time(func):
    """
    装饰器函数，获取函数的运行时间
    """
    @wraps(func)
    def wrapper(*args):
        start_time = time.clock()
        func(*args)
        end_time = time.clock()
        run_time = end_time - start_time
        return str(func.__name__) + '运行时间：' + str(run_time)
    return wrapper

@get_run_time
def test1():
    """
    业务函数1，无参数
    """
    time.sleep(0.5)
    print('test1函数的__name__属性：', test1.__name__)

@ get_run_time
def test2(num):
    """
    业务函数2，有参数
    """
    for i in range(num):
        time.sleep(0.01)

print(test1())
print(test2(35))
print('\n')


# 示例4：记录每个业务函数的运行日志，根据情况动态设置日志级别
# 备注：装饰器可以接受参数，实现更加灵活的功能

def get_run_log(level='info'):
    """
    装饰器函数，记录不同级别的日志信息
    """
    def inner(func):
        def wrapper(*args):
            if level == 'warning':
                logging.warning('%s is running !' %func.__name__)
            else:
                logging.info('%s is running !' %func.__name__)
            return func(*args)
        return wrapper
    return inner

@get_run_log(level='warning')
def test1():
    """
    业务函数1，无参数
    """
    return 'test1函数的__name__属性：' + test1.__name__

@get_run_log()
def test2(string):
    """
    业务函数2，有参数
    """
    return string

print(test1())
print(test2('hello world'))
print('\n')


# 示例5：记录每个业务函数的运行日志，用类class来实现装饰器
# 备注：装饰不仅可以是函数，还可以定义为一个类，类装饰器具有灵活度大、高内聚、封装性等优点
# 类的装饰器主要依靠类的__call__方法来实现功能

class Log:
    """
    Log是一个用来记录函数运行日志的类装饰器
    """

    def __init__(self, func):
        self._func = func

    def __call__(self, *args):
        logging.info('%s is running !' %self._func.__name__)
        self._func()

@Log
def test1():
    """
    业务函数1，无参数
    """
    print('hello world')

test1()
print('\n')


