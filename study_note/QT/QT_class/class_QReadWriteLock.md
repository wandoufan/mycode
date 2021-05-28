# QReadWriteLock

## 基本功能
QReadWriteLock提供了一个读-写锁，读-写锁是一个同步工具，用保护可以被读写的资源  
多个线程可以同时拥有读取权限，但一旦有一个线程要写入数据，其他所有线程都会被locked，直到写入操作完成  


## 工作原理
如果已经被一个线程lock for read，则其他线程也可以立即lock for read，但在解锁前不能lock for wirte  
如果已经被一个线程lock for write，则其他线程在解锁前不能lock for read或lock for wirte  


## 代码示例
1. QReadWriteLock的用法接近于QMutex，只是要区分是read锁还是write锁
lockForRead()/lockForWrite()一般和unlock()成对出现，而且将要保护的部分包起来  
```
QReadWriteLock locker;

void ThreadOne::run()
{
    //第一个线程读数据
    locker.lockForRead();
    readData();
    locker.unlock();
}

void ThreadTwo::run()
{
    //第二个线程也读数据
    locker.lockForRead();
    readData();
    locker.unlock();
}

void ThreadThree::run()
{
    //第三个线程写数据
    locker.lockForWrite();
    writeData();
    locker.unlock();
}
```
2. QReadWriteLock也有对应的辅助类：QReadLocker和QWriteLocker
其用法类似于QMutex和QMutexLocker的关系  
```
QReadWriteLock locker;

void ThreadOne::run()
{
    //第一个线程读数据
    QReadLocker read_locker(locker);
    readData();
}

void ThreadTwo::run()
{
    //第二个线程也读数据
    QReadLocker read_locker(locker);
    readData();
}

void ThreadThree::run()
{
    //第三个线程写数据
    QWriteLocker write_locker(locker);
    writeData();
}
```


## 构造函数
1. QReadWriteLock::QReadWriteLock(QReadWriteLock::RecursionMode recursionMode = NonRecursive)
参数默认值为'NonRecursive'，即一个线程只能lock一个QReadWriteLock一次  
也可以把参数设置为'Recursive'，即一个线程可以lock同一个QReadWriteLock多次，并且这个QReadWriteLock不会被解锁，除非调用了unlock()函数  


## 常用公共函数
1. void QReadWriteLock::lockForRead()
为当前线程设置一个读取数据锁  
如果另一个线程已经lock for write，这个函数会阻塞当前线程不再读取  
如果这个线程已经lock for write，那就不可能再去lock for read  
备注：如果已经lock，会一直等待下去，直到unlock  

2. void QReadWriteLock::lockForWrite()
为当前线程设置一个写入数据锁  
如果另一个线程(包括当前线程)已经lock for write或lock for read，这个函数会阻塞当前线程不再写入(除非QReadWriteLock是用Recursive模式创建的)  
如果这个线程已经lock for read，那就不可能再去lock for write  
备注：如果已经lock，会一直等待下去，直到unlock  

3. bool QReadWriteLock::tryLockForRead()
根据是否lock成功返回true或false  
如果另一个线程已经lock for write，那就会lock失败，立刻返回false，不再等待  

4. bool QReadWriteLock::tryLockForRead(int timeout)
重载函数，timeout参数单位为毫秒  
备注：如果timeout参数为负数，则等于调用lockForRead()函数，即一直等待下去  

5. bool QReadWriteLock::tryLockForWrite()
根据是否lock成功返回true或false  
如果另一个线程已经lock for write或lock for read，那就会lock失败，立刻返回false，不再等待  

6. bool QReadWriteLock::tryLockForWrite(int timeout)
重载函数，timeout参数单位为毫秒  
备注：如果timeout参数为负数，则等于调用lockForWrite()函数，即一直等待下去  

7. void QReadWriteLock::unlock()
如果去unlock一个没有处于locked状态的QReadWriteLock，会造成程序中断报错  





