# coding:utf-8


# pstats模块用来分析python代码，一般和cProfile搭配使用，用来分析cProfile输出的文件内容
# 参考文档：https://docs.python.org/3/library/profile.html

# Stats对象的常用方法：
# 1.strip_dirs(): 去掉无关的路径信息
# 2.sort_stats(): 排序，
#    可选参数'cumulative'代表按照函数运行时间进行排正序，
#    可选参数-1(没有引号)代表按标准名(module/line/name)排序
# 3.print_stats(n): 打印分析结果，可选参数n指定打印前n行，n还可以是小数,表示前百分之几的函数信息 
#    print_stats(10) 输出前10行
#    print_stats(.5) 输出前50%
#    print_stats('init') 只输出包含'init'的部分
#    print_stats(.5, 'init') 只输出前50%的且包含'init'的部分
# 4.print_callers('init') 输出有谁调用了'init'函数

# ----------------------------------------------------------------------------------------
# 使用示例
import cProfile
import pstats


def one():
    sum=0
    for i in range(10000):
        sum+=i
    return sum

if __name__ == '__main__':
    cProfile.run('one()', 'result') # 将cProfile的结果保存到result文件中
    p=pstats.Stats('result') # 创建Stats对象
    p.strip_dirs().sort_stats('cumulative').print_stats()