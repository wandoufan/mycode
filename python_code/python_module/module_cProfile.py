# coding:utf-8

# cProfile是一个可以监控python程序运行消耗时间的工具
# 通过分析每个函数及其子函数的时间消耗情况来对程序进行性能优化
# cProfile是python内置库，不需要安装
# 注意：使用cProfile本身就会使程序的运行时间会大大变长

# 三个常用性能分析工具的区别：
# memory_profiler:用来具体查看指定函数的内存消耗情况，可以看到每行的具体情况
# cProfile:用来具体查看程序的时间消耗情况，但是只能查看每个函数及其子函数的时间消耗情况
# line_profiler:用来具体查看指定函数的时间消耗情况，可以看到每行的具体情况

# 方法一：导入python代码中使用(使用很麻烦，不推荐)
# cProfile.run(cmd)方法中只能针对命令
import cProfile
import re
cProfile.run('re.compile("foo|bar")')


# 方法二：在Linux命令中使用
# 'python -m cProfile test.py' 运行命令时要加上 -m cProfile参数 
# 不需要在python代码中导入库或添加修饰器，就可以直接使用

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