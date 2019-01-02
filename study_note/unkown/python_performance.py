# 关于python代码性能优化的总结：

# 参考资料(关于log和熵的计算)：
# https://blog.csdn.net/u010786109/article/details/43374227
# https://stackoverflow.com/questions/3650194/are-numpys-math-functions-faster-than-pythons
# https://stackoverflow.com/questions/15450192/fastest-way-to-compute-entropy-in-python
# https://blog.biolab.si/2012/06/15/computing-joint-entropy-in-python/

# https://flystarhe.github.io/docs-2014/python/notes/profiler/

# 优化案例：
# https://rare-technologies.com/parallelizing-word2vec-in-python/
# https://rare-technologies.com/word2vec-in-python-part-two-optimizing/

# 常见优化的方向：
# 用cython替换耗时较多的核心部分
# 用多进程进行处理，例如十万行的文件用十个进程从十个对应位置同时开始读取处理，最后再合并结果
# ......

# 性能分析的工具(都属于既是python的库，又是Linux命令，可以单写一个文件出来)：
# 时间消耗：cProfile
# python -m cProfile test.py
# 内存消耗：memory_profiler
# 安装：pip install -U memory_profiler
# python -m memory_profiler test.py



