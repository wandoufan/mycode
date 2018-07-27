# coding:utf-8

# memory_profiler是一个可以监控python程序运行时内存消耗情况的工具
# 通过分析每行代码的内存消耗情况来对程序进行性能优化
# memory_profiler使用前需要先安装
# 注意：使用memory_profiler之后程序的运行时间会大大变长

# 三个常用性能分析工具的区别：
# memory_profiler:用来具体查看指定函数的内存消耗情况，可以看到每行的具体情况
# cProfile:用来具体查看程序的时间消耗情况，但是只能查看每个函数及其子函数的时间消耗情况
# line_profiler:用来具体查看指定函数的时间消耗情况，可以看到每行的具体情况

# 方法一：导入python代码中使用
# 需要在python代码中导入相应的库，在需要监控的函数上面放置一个装饰器@profile
# 装饰器@profile可以一次写多个，可以通过指定装饰器中的precision参数来设置显示内存的精度
from memory_profiler import profile

@profile(precision=4)# 内存显示精确到小数点后4位
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a
@profile
def test():
    return 999**999

if __name__ == '__main__':
    my_func()
    test()

# 方法二：在Linux命令中使用
# 'python -m memory_profiler test.py' 运行命令时要加上 -m memory_profiler参数 
# 不需要在python代码中导入库，但仍然需要在相应的函数上面加上修饰器

# 输出结果：
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     10     24.4 MiB     24.4 MiB   @profile
#     11                             def my_func():
#     12     28.2 MiB      3.8 MiB       a = [1] * (10 ** 6)
#     13    104.5 MiB     76.3 MiB       b = [2] * (2 * 10 ** 7)
#     14     28.2 MiB    -76.3 MiB       del b
#     15     28.2 MiB      0.0 MiB       return a

# 参数含义：
# Line: 代码的行号，修饰器会把目标函数的每一行的内存情况都输出出来
# Mem usage：表示该行执行完后消耗的内存情况
# Increment： 表示当前行相对于上一行的内存变化情况