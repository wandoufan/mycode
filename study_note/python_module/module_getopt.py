# coding:utf-8

# getopt模块是专门用来处理命令行参数的，可以接收到运行脚本时加入的相关参数
# 有时候需要些脚本处理一些任务，根据输入的不同的命令行参数进行不同的处理，这时就用到getopt模块

import getopt
import sys

# getopt模块的两个函数：getopt.getopt和getopt.gnu_getopt

# getopt.getopt(args, shortopts, longopts=[])
# getopt语句一般写在if __name__ == '__main__'语句下面，并根据接收的不同参数进行不同的操作
# 在cmd等shell环境中用命令加对应参数去执行脚本程序
# args指的是当前脚本接收的参数，它是一个列表，可以通过sys.argv获得
# shortopts 是短参数，它是一个字符串，类似于：'hr'
# longopts 是长参数，它是一个列表，类似于：['help','run']
opts, arg = getopt.getopt(sys.argv[1:], 'hr', ['help', 'run'])
# 执行脚本命令：python test.py -h 或 python test.py --help(注意对于长参数要使用双横杠)

# 如果短参数后面有冒号： ，或长参数后面有等号=  则表示选项后边必须有对应的值
opts, arg = getopt.getopt(sys.argv[1:], 'h:', ['help='])
# 执行脚本命令：python test.py -h test 或 python test.py --help test

# getopt.getopt()函数返回值分别是两个列表：opts和args
# opts列表中存放了若干元组，每个元组为(选项, 选项对应的值)
# args 为不属于格式信息的剩余的命令行参数，去除有用的输入以后剩余的部分.
for option, value in opts:
    print(option, value)
    if option in ['-h', '-r']:
        print('success!')

# gnu_getopt函数是getopt函数的改进型，在某些方面可以弥补getopt函数的缺陷
# getopt函数一旦遇到第一个不符合配置选项格式的参数就放弃解析了，剩下的部分不检查。
# 所以使用getopt时，为了保证程序的运行，一般的参数一定要放在最后面。
# gnu_getopt函数则可以轻松面对这个问题，允许用户随便放置一般参数的位置

# getopt模块的两个属性：getopt.error和getopt.GetoptError，主要用来获取错误信息
