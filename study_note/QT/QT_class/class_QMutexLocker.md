# QMutexLocker

## 基本功能
QMutexLocker类用来简化lock和unlock一个mutex的过程  
在一些逻辑复杂的函数或可能产生异常的代码中，对mutex进行lock和unlock操作会很难去debug  
在这种情况下，可以使用QMutexLocker来确保mutex的状态总是定义明确的  
也就是说在一些复杂的代码中使用QMutexLocker可以简化代码，使代码可读性更好  
备注：这个类中的所有函数都是线程安全的  


## 工作原理
当QMutexLocker被创建出来时，mutex就是locked的状态，所以不用再写mutex.lock()  
当函数运行结束，QMutexLocker自动被析构函数销毁，mutex被解锁，所以不用再写mutex.unlock()  


## 代码示例
1. 不使用QMutexLocker时的函数
```
void QDiceThread::run()
{
    //执行线程任务
    m_stop = false;
    m_seq = 0;
    while(!m_stop)
    {
        if(!m_paused)
        {
            mutex.lock();
            m_diceValue = QRandomGenerator::global() -> bounded(1, 7);
            m_seq ++;
            mutex.unlock();
        }
        //假设线程任务执行一次需要3s
        sleep(3);
    }
    m_paused = true;
    quit();
}
```
2. 使用QMutexLocker时的函数
```
void QDiceThread::run()
{
    //执行线程任务
    m_stop = false;
    m_seq = 0;
    while(!m_stop)
    {
        if(!m_paused)
        {
            QMutexLocker locker(&mutex);
            m_diceValue = QRandomGenerator::global() -> bounded(1, 7);
            m_seq ++;
        }
        //假设线程任务执行一次需要3s
        sleep(3);
    }
    m_paused = true;
    quit();
}

```


## 构造函数
1. QMutexLocker::QMutexLocker(QRecursiveMutex \*mutex)
构建一个QMutexLocker并且锁住这个mutex，当QMutexLocker被销毁时，这个mutex会被解锁  

2. QMutexLocker::QMutexLocker(QMutex \*mutex)
构建一个QMutexLocker并且锁住这个mutex，当QMutexLocker被销毁时，这个mutex会被解锁  
```
QMutexLocker locker(&mutex);
```


## 常用公共函数
1. QMutex \*QMutexLocker::mutex() const
返回当前正在操作的mutex对象  

2. void QMutexLocker::relock()
重新锁住一个unlocked状态的mutex locker  

3. void QMutexLocker::unlock()
解锁这个mutex locker  



