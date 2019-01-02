# coding:utf-8

# python中与时间处理有关的模块包括：time，datetime，calendar
# 关于time 模块中的常用函数

import time

# 返回时间戳(时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量)
print(time.time())

# 把时间戳转化为本地时间struct_time
print(time.localtime())# struct_time对象
print(time.localtime().tm_year)# struct_time对象的年属性值
print(time.localtime().tm_mon)# struct_time对象的月属性值
print(time.localtime().tm_mday)# struct_time对象的日期属性值
print(time.localtime().tm_hour)# struct_time对象的小时属性值
print(time.localtime().tm_min)# struct_time对象的分钟属性值
print(time.localtime().tm_sec)# struct_time对象的秒属性值

# 把时间戳转化为UTC时区(0时区)
print(time.gmtime())

# 把一个本地时间转化为时间戳
print(time.mktime(time.localtime()))

# 输出简化版的本地时间
print(time.ctime())
t = time.localtime()
print(time.asctime(t))

# 推迟调用线程的运行，参数代表推迟的秒数
time.sleep(5)
time.sleep(0.01)
