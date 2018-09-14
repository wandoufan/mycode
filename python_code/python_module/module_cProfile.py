# coding:utf-8

# cProfile是一个可以监控python程序运行消耗时间的工具
# 通过分析每个函数及其子函数的时间消耗情况来对程序进行性能优化
# cProfile是python内置库，不需要安装，属于C扩展，开销较小，适合剖析长时间运行的Python程序
# 注意：使用cProfile本身就会使程序的运行时间会变长

# 三个常用性能分析工具的区别：
# memory_profiler:用来具体查看指定函数的内存消耗情况，可以看到每行的具体情况
# cProfile:用来具体查看程序的时间消耗情况，但是只能查看每个函数及其子函数的时间消耗情况
# line_profiler:用来具体查看指定函数的时间消耗情况，可以看到每行的具体情况

# 备注：cProfile本身结果输出到文件后，文件内容是以二进制的方式保存的，用文本编辑器打开时会乱码
# 一般配合使用pstats库对结果文件进行具体分析

# 方法一：导入python代码中使用
# cProfile.run()方法查看指定函数的时间消耗情况
# cProfile.run('test()', filename='result.out', sort='cumulative')
# 第一个必选参数指定要运行的函数，另外也可以运行命令，如cProfile.run('re.compile("foo|bar")')
# 第二个可选参数指定将结果输出到文件
# 第三个可选参数指定排序方式，其中cumulative代表按照函数运行时间进行排序

import cProfile
import re
def one():
    sum=0
    for i in range(10000):
        sum+=i
    return sum
cProfile.run('one()')
# cProfile.run('one()', 'result') # 把one函数的运行结果保存到result文件中

# 方法二：在Linux命令中使用
# 'python -m cProfile test.py' 通过命令直接运行python代码
# 不需要在python代码中导入库或添加修饰器，就可以直接使用
# python -m cProfile -o result.out -s cumulative test.py
# 第一个必选参数-m指定使用cProfile分析工具
# 第二个可选参数-o指定输出文件
# 第三个可选参数-s指定排序方式，其中cumulative代表按照函数运行时间进行排序

# 输出结果：
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.095    0.095    0.095    0.095 <stdin>:1(my_func)
#      1    0.003    0.003    0.099    0.099 <string>:1(<module>)
#      1    0.000    0.000    0.099    0.099 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 参数含义：
# ncalls：表示函数调用的次数
# tottime：表示指定函数本身总的运行时间，不包括函数中调用子函数的运行时间
# percall：（第一个percall）等于tottime/ncalls
# cumtime：表示该函数及其所有子函数的调用运行的时间，即函数开始调用到返回的时间
# percall：（第二个percall）即函数运行一次的平均时间，等于cumtime/ncalls
# filename:lineno(function)：每个函数调用的具体信息
