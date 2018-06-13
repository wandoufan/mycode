# coding:utf-8

# queue模块是用来提供队列、堆栈等数据结构等功能的模块
# 注意，Python 2 中是大写的Queue，Python 3 中是小写的queue
# 队列是线程之间最常用的交换数据的形式，queue就是提供队列操作的模块

import queue

# queue模块有三种数据结构及构造函数:

# 创建一个队列对象(先进先出),队列长度可以为有限或者无限
# 可选参数maxsize来设定有限队列的长度,maxsize小于1表示队列长度无限
q1 = queue.Queue(maxsize=2)

# 创建一个堆栈对象(先进后出)
q2 = queue.LifoQueue()

# 创建一个优先级队列(优先级越低越先出来)
q3 = queue.PriorityQueue()

# 将一个值放入队列中,put()有两个参数，第一个必选参数为插入的数据值，第二个可选参数block,默认为1
# 当前队列没有多余空间时，如果block为1，put()就使调用线程暂停，直到空出一个数据单元；如果block为0，则引发queue.full异常
q1.put(1)
q1.put(2)
# q1.put(3,block=0)

q2.put(1)
q2.put(2)
q2.put(3)

# 将一个值从队列中取出，可选参数block默认为True,当队列没有数据时
# 如果block为True，get()就使调用线程暂停；如果block为False,则引发queue.empty异常
print(q1.get(False))
print(q1.get(False))



# 其他queue模块的常用方法：

# 返回队列长度
print(q2.qsize())

# 如果队列为空返回True,否则返回False
print(q1.empty(), q2.empty())

# 如果队列空间满了返回True，否则返回False
print(q1.full())

# 如果放新数据时队列空间满，就不做等待，立即报错，相当于q1.put('a',False)
q1.put_nowait('a')

# 如果取出数据时队列为空，就不做等待，立即报错，相当于q1.get(False)
print(q1.get_nowait())

# 完成一项工作后q.task_done()函数向任务已经完成的队列发送一个信号
q1.task_done()

# 等到队列为空再执行再执行别的操作
q1.join()
