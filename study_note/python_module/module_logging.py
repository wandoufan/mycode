# coding:utf-8
# 参考资料：
# https://www.cnblogs.com/yyds/p/6901864.html
# https://docs.python.org/3/library/logging.html

# logging模块是Python内置的标准模块，主要用于输出运行日志，
# 可以设置输出日志的等级、日志保存路径、日志文件回滚等；

# 相比print，日志具备如下优点：
# 1.可以通过设置不同的日志等级，在release版本中只输出重要信息，而不必显示大量的调试信息；
# 2.print将所有信息都输出到标准输出中，logging可以由开发者决定将信息输出到什么地方，以及怎么输出；

# logging模块的日志级别：
# debug : 最详细的日志信息，常用于问题诊断，日志信息量最大，日志级别最低
# info : 详细程度仅次于debug, 一般只记录关键节点的信息, 用于确认程序是正常工作的
# warning : 用于记录程序运行时出现的一些不影响程序正常运行的问题, 如磁盘可用空间低
# error : 用于记录某个问题导致某些功能不能正常运行时的信息
# critical : 用于记录发生严重问题导致程序不能继续运行时的信息，日志信息量最小，日志级别最高

# 关于日志级别的设定：
# 开发应用程序或部署开发环境时，可以使用DEBUG或INFO级别的日志获取尽可能详细的日志信息来进行开发或部署调试；
# 应用上线或部署生产环境时，应该使用WARNING或ERROR或CRITICAL级别的日志来降低机器的I/O压力和提高获取错误日志信息的效率；
# 日志级别的指定通常都是在应用程序的配置文件中进行指定的；
# 当为某个应用程序指定一个日志级别后，应用程序会记录所有日志级别大于或等于指定日志级别的日志信息，而不是仅仅记录指定级别的日志信息；
# logging模块的默认日志记录级别是warning,即输出warning,error,critical, 而debug和info会被丢弃；

# logging模块的四大组件
# loggers : 提供程序代码直接使用的外部接口
# handlers : 用于将日志记录发送到指定的位置
# filters : 提供细粒度的日志过滤功能，用于决定哪些日志记录将会被输出
# formatters : 用于控制日志信息的最终输出格式

import logging


# logging.basicConfig()函数用于设置logging日志的配置
# filename参数：指定日志输出到目标文件，默认日志信息直接输出到控制台
# filemode参数：指定日志文件的打开模块，默认为'a'，仅当指定了filename时该参数才有效
# format参数：指定日志字符串格式，默认为'%(levelname)s:%(name)s:%(message)s'，即'日志级别:日志器名称:日志内容'，另外可以加上时间信息'%(asctime)s'
# datefmt参数：指定日志字符串中的时间格式，仅当format参数中包含时间字段'%(asctime)s'时才有效
# level参数：指定日志记录级别，默认日志记录级别是warning，指定格式为level=logging.DEBUG
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)

# logging模块提供的可选日志字段：
# %(asctime)s:日志发生的时间(可读时间)，如'2018-10-12 15:49:56'
# %(created)f:日志发生的时间(时间戳)，即调用time.time()
# %(levelname)s:日志的级别('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
# %(levelno)s:数字形式的日志级别(10, 20, 30, 40, 50)
# %(name)s: 所使用的日志器名称，默认是'root'，默认使用的是rootLogger
# %(message)s:日志记录的文本内容
# %(pathname)s:调用日志记录函数的源代码文件完整路径
# %(filename)s:源代码文件名，包含后缀
# %(module)s:源代码文件名，不含后缀
# %(lineno)d:调用日志记录函数的代码所在的行号
# %(funcName)s:调用日志记录函数的函数名
# %(process)d:对应的进程ID
# %(processName)s:对应的进程名称
# %(thread)d:对应的线程ID
# %(threadName)s:对应的线程名称

# 创建不同级别的日志
logging.debug('创建一条debug日志')
logging.info('创建一条info日志')
logging.warning('创建一条warning日志')
logging.error('创建一条error日志')
logging.critical('创建一条critical日志')
# 创建日志的另一种写法
logging.log(logging.DEBUG, '创建一条debug日志')
logging.log(logging.INFO, '创建一条info日志')
logging.log(logging.WARNING, '创建一条warning日志')
logging.log(logging.ERROR, '创建一条error日志')
logging.log(logging.CRITICAL, '创建一条critical日志')

# 记录的日志中可以包含变量参数
name = 'Tom'
age = 10
logging.info('%s is %s years old' %(name, age))
