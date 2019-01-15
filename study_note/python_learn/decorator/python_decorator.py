# 主要记录python中的修饰器/装饰器(decorators)的用法

# 参考资料：
# http://www.runoob.com/w3cnote/python-func-decorators.html
# https://www.jianshu.com/p/ab702e4d4ba7

# 一、装饰器的基本介绍

# 1.装饰器的定义：
# python装饰器本质上是一个函数，它可以协助其他业务函数在不修改代码的情况下增加额外的功能
# 装饰器接收业务函数作为参数，返回值也是一个函数/类对象
# 装饰器以@开头并且被放在被装饰函数的上面，相当于给被装饰函数提供了一个功能套件，可帮助代码变得更加简洁
# 有了装饰器，我们就可以抽离出大量函数中与函数功能本身无关的雷同代码并继续重用

# 2.装饰器的使用场景
# 典型的装饰器应用场景包括：记录日志、性能测试、事务处理


# 二、应用实例
import datetime
import time
import logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)


# 示例1：给业务函数增加一个装饰器，用来记录每个业务函数的运行日志

def get_run_log(func):
    """
    装饰器函数，记录包含函数名的日志信息
    """
    def wrapper(*args):
        logging.info('%s is running !' %func.__name__)
        return func(*args)
    return wrapper

def get_run_log(func):
    """
    装饰器函数，记录包含函数名的日志信息
    """
    logging.info('%s is running !' %func.__name__)
    return func

@get_run_log
def test1(name):
    """
    业务函数1
    """
    print(name)

@get_run_log
def test2(x, y, z):
    """
    业务函数2
    """
    print(x + y + z)

@get_run_log
def test3():
    """
    业务函数3
    """
    print('this is test3')

test1('Tom')
test2(1, 2, 3)
test3()



# 示例2：给函数增加一个装饰器，用来获取每个函数的运行时间
# def get_run_time():
#     start_time = datetime.datetime.now()
#     time.sleep(2)
#     end_time = datetime.datetime.now()
#     run_time = (start_time - end_time).seconds
#     print(run_time)

# get_run_time()











# def consumer(func):
#     def wrapper(*args,**kw):
#         gen = func(*args, **kw)
#         gen.next()
#         return gen
#     wrapper.__name__ = func.__name__
#     wrapper.__dict__ = func.__dict__
#     wrapper.__doc__  = func.__doc__
#     return wrapper

# word_map = {}
# def consume_data_from_file(file_name, consumer):
#     for line in file(file_name):
#         consumer.send(line)

# @consumer
# def consume_words(consumer):
#     while True:
#         line = yield
#         for word in (w for w in line.split() if w.strip()):
#             consumer.send(word)

# @consumer
# def count_words_consumer():
#     while True:
#         word  = yield
#         if word not in word_map:
#             word_map[word] = 0
#         word_map[word] += 1
#     print word_map

# if __name__ == '__main__':
#     cons = count_words_consumer()
#     cons_inner = consume_words(cons)
#     c = consume_data_from_file('test.txt', cons_inner)
#     print word_map
#     