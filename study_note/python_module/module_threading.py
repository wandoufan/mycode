# coding:utf-8

# threading模块用来提供多线程相关的功能，是实现并发的的主要途径

# 注意：multiprocessing模块是多进程，threading模块是多线程！
# thread模块是python初级的版本，现在已经废除
# python当前版本的多线程库没有实现优先级、线程组，线程也不能被停止、暂停、恢复、中断。


import threading
import time


def hello():
    print('hello,world', time.ctime())

# 有两种方法来创建线程：一种通过继承threading.Thread类，重写它的run()方法；
# 派生类中重写了父类threading.Thread的run()方法，其他方法（除了构造函数)都不应在子类中被重写，
# 换句话说，在子类中只有_init_()和run()方法被重写。


class MyThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        hello()

t1 = MyThread()
print(type(t1))

# 另一种是创建一个threading.Thread的对象，在它的初始化函数(__init__)将可调用的对象作为参数传入
# 初始化函数为：__init__(self, group=None, target=None, name=None, args=(), kwargs={})
# group参数是预留暂时不用的，target参数是调用对象，name参数是线程名字，默认值为“Thread-N“，N是一个数字
# 参数args和kwargs分别表示调用target时的参数列表和关键字参数。
t2 = threading.Thread(target=hello)
print(type(t2))

# 线程对象通过.start()方法来启动，start方法再调用threading.Thread类中的run()方法
t1.start()
t2.start()

# jion([timeout])：等待被join方法调用的线程结束后再往下运行，其中timeout参数为等待时间；
# 例如:在父线程A中创建了子线程B，并在A中调用了B.join()，那么A线程会在调用的地方等待，
# 一直到B线程运行完成之后才会继续往下执行。
# timeout为父线程最多等待子线程运行的时间，时间一到不管是否运行完成都立即结束线程任务；
# 当timeout参数没有被指定或者是None时，其主线程将被阻塞一直到当前线程运行终止；
# 线程能被join()多次，但不能在线程启动之前调用join()
# 线程不能调用自身的join()，否则会引起死锁错误
t1.join(5)

# setDaemon(bool)：设置守护线程，即设置子线程是否随主线程一起结束
# 例如:在父线程A中创建了子线程B，并在A中调用了B.setDaemon(True),即为把B设置为了守护线程
# 在A线程消亡时，不管B线程的是否运行完成，都要随A线程一起消亡。
# 根据特性可以看出一般都是把不重要的线程设置为守护线程
# 相反，非守护线程一般很重要，主线程运行完后不会立即退出，而是等所有非守护线程完成才退出
# setDaemon(bool)必须在start()之前调用,默认参数值为False。
t3 = MyThread()
t3.setDaemon(True)
t3.start()
print(t3.isAlive())

# 例子：
t1 = threading.Thread(target=hello)
t2 = threading.Thread(target=hello)
t3 = threading.Thread(target=hello)
t4 = threading.Thread(target=hello)
list1=[t1,t2,t3,t4]
# 将列表中的线程对象都逐一启动
for t in list1:
	t.start()
# 将列表中的已经启动的线程对象再逐一jion()
# 可以保证所有线程对象都运行完了之后整个程序再往下走
for t in list1:
	t.join()

# 推迟调用线程的运行，参数代表推迟的秒数
time.sleep(5)

# setName(name) 方法，设置线程名字
t1.setName('my_thread')

# getName()方法，返回线程名字
print(t1.getName())
print(t2.getName())

# isAlive()方法判断线程是否活动的，返回True或False
print(t1.isAlive())
print(t2.isAlive())

# isDaemon()方法，判断线程是否随主线程一起结束。
print(t1.isDaemon())



# threading.Lock()用来创建互斥锁保护临界资源，保证线程之间不会因为争夺资源陷入死锁中
# Lock类返回一个锁对象，一旦某个线程获得这个锁，其他线程要想获得锁就必须阻塞至锁被释放
lock = threading.Lock()
# 锁对象的acquire()方法和release()方法分别放在任务的开始和结束位置
# acquire([blocking=1])方法代表获得一个锁
# 当没有参数或参数为True时以阻塞方式获得锁，即要等到锁释放后才能加锁，而后返回True
# 当有参数且参数为False时以非阻塞方式获得锁，即如果被锁定，则不等待直接返回False,如果未锁定则返回True
# release()方法用来释放资源，把锁的locked状态改为unlocked


def lock_test():
    lock.acquire()
    print('this is a lock test')
    lock.release()
t1 = threading.Thread(target=lock_test)
t2 = threading.Thread(target=lock_test)

t1.start()
t2.start()

# thread.event() ???????


---------------------------------------------------------------------------------
# 代码示例：
import threading
import os
import time

# 调用线程Train和Readlog,两个线程交替执行

class Train(threading.Thread):
    # 负责生成日志文件，不断向日志中写入数据
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.train()

    def train(self):
        count = 1
        while True:
            with open('C:/b.log','w') as file:
                if count<10:
                    count +=1
                    print('count is %d' %count)
                    file.write(str(count)+'\n')
                    file.close()
                    time.sleep(1)
                else:
                    file.write('x'+'\n')
                    file.write('abc')
                    file.close()
                    print('train finish!')
                    break

class Readlog(threading.Thread):
    # 负责读日志文件中的数据
    def __init__(self):
        threading.Thread.__init__(self)
        self.continue_ = True

    def run(self):
        self.readlog()


# 备注：readlog中的while循环是双层循环，所以只能在循环过程中不断去判断标志位的值
# 如果是单层循环，可以直接写成 ‘while self.continue_:’
    def readlog(self):
        while True:
            if not os.path.isfile('C:/b.log'):
                print('waiting for log file.......')
                time.sleep(2)
            else:
                with open('C:/b.log','r') as log:
                    for eachline in log:
                        if self.continue_ == False:
                            break
                        else:
                            #time.sleep(1)
                            print('this is log file:',eachline)
                            if eachline == 'x'+'\n':
                                print('readlog finish!')
                                break
                    break

    def terminate(self):
        #方法一：修改标志位退出线程
        self.continue_ = False
        print('stop readlog')
        #方法二：强制退出线程任务
        #os._exit(0)
        

#文件不能同时读写？？t1,t2不能同时运行？？
#尝试修改写一个数据就关闭文件,也不行？？
class Start():

    def begin(self):
        t1 = Train()
        t2 = Readlog()

        t1.start()
        t2.start()
        t1.join()
        time.sleep(6)

        if t2.isAlive():
            t2.terminate()


if __name__ == '__main__':
    task = Start()
    task.begin()



