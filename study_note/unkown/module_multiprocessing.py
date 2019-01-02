# coding:utf-8


# multiprocessing模块用来提供多进程相关的功能，与threading模块相似
# 注意：multiprocessing模块是多进程，threading模块是多线程！
# multiprocessing模块提供本地和远程并发的功能

# 进程和线程的区别：


import multiprocessing
import time
import os

def hello(a,b):
	print(a+b,time.ctime())

# 注意：在windows中使用进程模块就必须把相关进程代码写在if __name__ == '__main__'语句下面
# 在Linux/unix系统下则不需要
# if __name__ == '__main__'语句来代表主进程，需要在主进程中创建启动子进程
if __name__ == '__main__':

# Process 类用来描述一个进程对象。创建子进程的时候，只需要传入一个执行函数和函数的参数即可完成 Process 示例的创建。
# Process 类使用的是threading.Thread类的API接口
# multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
# group参数是预留暂时不用的，target参数是调用的函数程序，name参数是进程名字
# 参数args和kwargs分别表示调用target时的参数列表和关键字参数。
	p1 = multiprocessing.Process(target=hello,args=(1,2))
	print(type(p1))
# 进程对象通过.start()方法来启动
	p1.start()
# join()方法阻塞主线程来等待当前线程运行
	p1.join()
# https://docs.python.org/2/library/multiprocessing.html#the-process-class

# Pool 类????

# terminate()结束进程
# is_alive()方法？？？
# run()
# start()
# join()