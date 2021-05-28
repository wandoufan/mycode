# QWaitCondition

## 基本功能
QWaitCondition为同步线程提供了一个条件变量  
一个线程在满足一定条件时，通知其他多个线程，使它们做出响应  
QWaitCondition一般用于'生产者/消费者'模型中，和QReadWriteLock/QMutex搭配使用  


## 代码示例
1. '生产者/消费者'模型
注意：两个线程调用的是相同的mutex和newdataAvailable  
```
//以下变量都是全局变量，两个线程都要进行访问
QMutex mutex; //互斥锁
QWaitCondition newdataAvailable; //条件变量
int seq = 0; //掷骰子的次数
int dice_value = 0; //骰子的点数

void QThreadProducer::run()
{
	//"生产者"线程，用来生产数据，即掷骰子产生点数
    m_stop = false;
    seq = 0;
    while(!m_stop)
    {
        mutex.lock();
        dice_value = QRandomGenerator::global() -> bounded(1, 7);
        seq ++;
        mutex.unlock();
        newdataAvailable.wakeAll(); //新数据已经产生，可以唤醒所有线程
        sleep(3); //假设线程任务执行一次需要3s
    }
}

void QThreadConsumer::run()
{
	//"消费者"线程，用来消费数据，把读取骰子的点数并送给主线程进行显示
    m_stop = false;
    while(!m_stop)
    {
        mutex.lock();
        newdataAvailable.wait(&mutex); //接到唤醒条件之后就往下继续执行，即发出信号
        emit newValue(seq, dice_value);
        mutex.unlock();
    }
}
```
在启动线程时，一般是先启动consumer，再启动producer，否则最早产生的数据consumer可能来不及接收  
```
thread_consumer.start();
thread_producer.start();
```
在结束线程时，也是先结束consumer，再结束producer，否则producer已经结束的时候consumer还在等着接收数据，consumer会一直处于阻塞状态  
```
thread_consumer.stopThread();
thread_consumer.wait();
thread_producer.stopThread();
thread_producer.wait();
```
如果想要先结束producer，再结束consumer，则需要用terminate()强制结束consumer，避免一直等待  
```
thread_producer.stopThread();
thread_producer.wait();
thread_consumer.terminate();
thread_consumer.wait();
```


## 构造函数
1. QWaitCondition::QWaitCondition()


## 常用公共函数
1. void QWaitCondition::wakeAll()
叫醒所有正在等待该条件的线程  
线程被唤醒的顺序取决于操作系统的策略，不能设置，也不能预测  

2. void QWaitCondition::wakeOne()
叫醒一个正在等待该条件的线程  
具体唤醒哪个线程取决于操作系统的策略，不能设置，也不能预测  
如果想唤醒某个特定线程，最好设置不同的唤醒条件，让不同的线程去等待不同的唤醒条件  

3. bool QWaitCondition::wait(QMutex \*lockedMutex, QDeadlineTimer deadline = QDeadlineTimer(QDeadlineTimer::Forever))
先解锁互斥量lockedMutex，使其他线程可以使用lockedMutex，然后阻塞当前进程一直等待唤醒条件，被唤醒后再锁定lockedMutex，然后退出函数，继续执行函数下面的代码  
注意：lockedMutex必须是被调用线程锁住，处于locked的状态，然后才能作为参数传递到函数里  
注意：当前线程和其他线程使用的是同一个lockedMutex，因此lockedMutex是一个全局变量，QWaitCondition对象也是一样的  
函数返回条件：  
3.1 如果lockedMutex是Recursive模式的，则该函数立即返回  
3.2 其他线程用wakeAll()/wakeOne()唤醒了该线程，则函数返回true  
3.3 等待时间超时后，则函数返回false(deadline默认值为Forever，即永不超时，一直等待)  


4. bool QWaitCondition::wait(QReadWriteLock \*lockedReadWriteLock, QDeadlineTimer deadline = QDeadlineTimer(QDeadlineTimer::Forever))
类似上一个函数，区别在于参数是一个lockedReadWriteLock  




