#关于python中的修饰器(装饰器)，@的用法
#参见flask的学习笔记，学习笔记

# 17.关于python装饰器/修饰器：
# python装饰器本质上是一个函数，它可以协助其他函数在不修改代码的情况下增加额外的功能，装饰器的返回值也是一个函数对象。
# 装饰器是@开头且放在被装饰函数上面,例如@app.route()

# 18.关于python生成器(generator)：
# 一边循环，一边计算的机制称为生成器。例如对于很大的列表，列表元素全部创建出来会占用很大的内存空间，如果列表元素可以
# 按照某种算法推算出来，就可以在循环的过程中不断推算出后续的元素，大大节省了存储空间。
# 函数中如果出现了yield关键字，那么该函数就不再是普通函数，而是生成器函数。
# 生成器函数和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，
# 在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
# 一个函数或者子程序都只能 return 一次，但是一个生成器能暂停执行并返回一个中间的结果,即用关键字yield来代替return。
# generator对象一般用for i in fun():来迭代输出。

# pthon生成器(generator)：
# 一边循环，一边计算的机制称为生成器。例如对于很大的列表，列表元素全部创建出来会占用很大的内存空间，如果列表元素可以
# 按照某种算法推算出来，就可以在循环的过程中不断推算出后续的元素，大大节省了存储空间。
# 函数中如果出现了yield关键字，那么该函数就不再是普通函数，而是生成器函数。


# 装饰器给每个函数提供某些功能，如统计该函数的运行时间，相当于给每个函数加一个套件

def consumer(func):
    def wrapper(*args,**kw):
        gen = func(*args, **kw)
        gen.next()
        return gen
    wrapper.__name__ = func.__name__
    wrapper.__dict__ = func.__dict__
    wrapper.__doc__  = func.__doc__
    return wrapper

word_map = {}
def consume_data_from_file(file_name, consumer):
    for line in file(file_name):
        consumer.send(line)

@consumer
def consume_words(consumer):
    while True:
        line = yield
        for word in (w for w in line.split() if w.strip()):
            consumer.send(word)

@consumer
def count_words_consumer():
    while True:
        word  = yield
        if word not in word_map:
            word_map[word] = 0
        word_map[word] += 1
    print word_map

if __name__ == '__main__':
    cons = count_words_consumer()
    cons_inner = consume_words(cons)
    c = consume_data_from_file('test.txt', cons_inner)
    print word_map
    