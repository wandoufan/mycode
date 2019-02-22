# 主要记录python中的生成器(generator)

# 使用了yield关键字的函数称为生成器(generator)
# 生成器是一个返回迭代器的函数，只能用于迭代操作，生成器可以看做特殊的迭代器
# 调用一个生成器函数，返回的是一个迭代器对象
# 生成器函数和普通函数的执行流程不一样，普通函数是顺序执行，遇到return语句或者最后一行函数语句就返回
# 而在调用生成器运行的过程中，每次遇到yield时函数会暂停并保存当前所有运行信息，返回yield的值
# 并在下一次执行next()方法时从当前位置继续运行
# yield关键字的功能类似于return关键字，但是在生成器函数中可以多次返回

# 生成器可以实现一边循环，一边计算的机制，方便处理大规模的数据对象，节约内存空间
# 例如对于一个规模很大的列表，如果列表元素全部创建出来会占用很大的内存空间，
# 如果列表元素可以按照某种算法推算出来，就可以在循环的过程中不断推算出后续的元素，大大节省了存储空间。

# 生成器和迭代器的区别：
# 生成器可以看做特殊的迭代器，生成器函数的返回结果是一个迭代器对象
# 生成器函数中使用了yield关键字


def test():
    list1 = [0, 1, 2, 3, 4]
    for i in list1:
        yield i

print(test())
print(type(test()))
for info in test():
    print(info) 

# -----------------------------------------------------

# 示例1：实现斐波那契数列
# n=1时f(n)=1；n=2时f(n)=1;n>2时f(n)=f(n-1)+f(n-2)

# 常规的递归法：
def fab1(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a1 = 1
        a2 = 1
        a3 = 1
        for i in range(n - 2):
            a3 = a2 + a1
            a1 = a2
            a2 = a3
        return a3

print(fab1(1), fab1(2), fab1(8))

# 使用yield的生成器法：
def fab2(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a = 1
        b = 1
        c = 1
        for i in range(n - 2):
            a = b
            b = c
            c = a + b
        yield c

print(fab2(8))
print(type(fab2(8)))
for i in fab2(8):
    print(i)
