# coding:utf-8

# line_profiler是一个可以监控python程序运行时间消耗情况的工具
# 通过分析每行代码的时间消耗情况来对程序进行性能优化
# 注意：memory_profiler需要安装，且在windows环境下需要先安装Microsoft Visual C++ 14.0 
# 可以直接在linux下通过'pip install line_profiler'安装使用
# 注意：使用line_profiler本身就会使程序的运行时间会大大变长

# 三个常用性能分析工具的区别：
# memory_profiler:用来具体查看指定函数的内存消耗情况，可以看到每行的具体情况
# cProfile:用来具体查看程序的时间消耗情况，但是只能查看每个函数及其子函数的时间消耗情况
# line_profiler:用来具体查看指定函数的时间消耗情况，可以看到每行的具体情况

# 方法一：导入python代码中使用(使用很麻烦，不推荐)
# 需要在python代码中导入相应的库，并调用库中的方法函数

from line_profiler import LineProfiler

def do_other_stuff(numbers):
    s = sum(numbers)
    return s
def do_stuff(numbers):
    s = do_other_stuff(numbers)
    return s

if __name__ == '__main__':
    numbers = [i for i in range(9)]
    lp = LineProfiler()
    lp.add_function(do_other_stuff)
    lp_wrapper = lp(do_stuff)
    lp_wrapper(numbers)
    lp.print_stats()

# 方法二：在Linux命令中使用
# 'kernprof -l test.py'运行程序，并得到一个记录时间信息的test.py.lprof文件
# 'python -m line_profiler test.py.lprof' 获取时间信息，注意运行命令时要加上 -m line_profiler参数
# 不需要在python代码中导入库，但仍然需要在相应的函数上面加上修饰器@profile
@profile
def test1():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a
@profile
def test2():
    k = 0
    for i in range(100):
        k = i + k
    return k

if __name__ == '__main__':
    test1()
    test2()

# 输出结果：
# Total time: 0.000174 s
# File: a.py
# Function: test2 at line 7
# Line #      Hits         Time  Per Hit   % Time  Line Contents
# ==============================================================
#      7                                           @profile
#      8                                           def test2():
#      9         1          2.0      2.0      1.1      k = 0
#     10       101         85.0      0.8     48.9      for i in range(100):
#     11       100         87.0      0.9     50.0          k = i + k
#     12         1          0.0      0.0      0.0      return k

# 参数含义：
# Line:代码的行号
# Hits:代码被调用的次数
# Time:代码消耗的总时间
# Per Hit:单次代码被调用消耗的时间
# % Time:代码消耗时间所占的百分比
