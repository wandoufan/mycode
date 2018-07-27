# coding:utf-8

# python中与时间处理有关的模块包括：time，datetime，calendar
# datetime也是时间相关的模块，最常用的功能是用来计算程序运行的时间
# 其他功能？与time模块的区别？

from datetime import datetime

start_time = datetime.now()
for i in range(10):
	i+=1
end_time = datetime.now()
run_time = (end_time-start_time).seconds# seconds方法把时间换算为秒

print(start_time,'\n',end_time,'\n',run_time)