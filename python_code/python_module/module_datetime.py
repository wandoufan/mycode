# coding:utf-8

# datetime也是时间相关的模块
# python中与时间处理有关的模块包括：time，datetime，calendar
# 参考资料：
# https://docs.python.org/3/library/datetime.html

import datetime
import time


# 最常用的功能是用来计算程序运行的时间
start_time = datetime.datetime.now()
for i in range(10):
	i+=1
end_time = datetime.datetime.now()
run_time = (end_time-start_time).seconds# seconds方法把时间换算为秒


# datetime模块中提供的常量：
print(datetime.MINYEAR)
print(datetime.MAXYEAR)


# datetime模块中提供的类：

# 1.datetime.date(year, month, day)类
datetime_date = datetime.date
# today()返回当前日期，相当于 datetime.date.fromtimestamp(time.time())
print(datetime_date.today())
print(datetime_date.today().year)
print(datetime_date.today().month)
print(datetime_date.today().day)
# fromtimestamp(timestamp)返回与POSIX时间戳对应的本地时间
print(datetime_date.fromtimestamp(time.time()))
# date类初始化时可以传入年月日作为参数
my_birthday = datetime.date(1994, 3, 18)
# 时间对象可以按时间先后比较大小
print(my_birthday < datetime_date.today())
print('1994-03-18' < '2018-10-01')
# 时间对象可以灵活设置年月日的值
print(my_birthday.replace(year=2011, month=9, day=1))
# 时间对象可以计算出差值
time_to_birthday = abs(my_birthday - datetime_date.today())
print(time_to_birthday.days)

# 2.datetime.time类
datetime_time = datetime.time

# 3.datetime.datetime类
datetime_datetim = datetime.datetime

# 4.datetime.timedelta类
datetime_timedelata = datetime.timedelta

# 5.datetime.tzinfo类
datetime_tzinfo = datetime.tzinfo

# 6.datetime.timezone类
datetime_timezone = datetime.timezone
