# QMutex

## 基本功能
QMutex是基于互斥量的线程同步类，用来在多个线程之间实现访问数据  
QMutex类的实例mutex是一个互斥量/互斥锁，用来保护一个对象/数据结构/一段代码一次只有一个线程能访问  
如果一个线程对mutex进行了lock操作，则在该线程进行unlock之前，其他线程都不能再对其进行lock操作  
在一些逻辑复杂的函数或可能发生异常的代码中，经常把QMutex和QMutexLocker搭配使用  
备注：这个类中的所有函数都是线程安全的  


## 代码示例
1. lock()/tryLock()一般和unlock()成对出现，而且将要保护的部分包起来  
备注：不一定是函数中的所有代码，一般包住数据读写部分的代码即可  
```
QMutex mutex;
int number = 1;

void method1()
{
	mutex.lock();
	number += 1;
	mutex.unlock();
}

void method2()
{
	mutex.lock();
	number -= 1;
	mutex.unlock();
}
```


## 构造函数
1. QMutex::QMutex(QMutex::RecursionMode mode)
参数默认值为'QMutex::NonRecursive'，即一个线程只能lock一个mutex一次  
也可以把参数设置为'QMutex::Recursive'，即一个线程可以lock同一个mutex多次，并且这个mutex不会被解锁，除非调用了unlock()函数  
备注：创建的实例对象默认是unlocked状态  

2. QMutex::QMutex()
备注：创建的实例对象默认是unlocked状态  


## 常用公共函数
1. bool QMutex::isRecursive() const
判断这个mutex是否是递归的  
如果一个mutex是递归的，则允许同一个线程对同一个mutex多次进行lock()/trylock()操作  
如果一个mutex是非递归的，同一个线程对同一个mutex多次进行lock()操作会造成lock()函数进入死锁状态，trylock()操作则会返回false  

2. void QMutex::lock()
lock这个mutex  
如果另一个线程已经lock了这个mutex，那么这次lock()调用会被一直阻塞，直到另一个线程unlock了这个mutex  
也就是说如果这个mutex已经是locked，那么这次lock()调用会一直等待  

3. bool QMutex::tryLock(int timeout = 0)
尝试lock这个mutex，根据是否lock成功返回true或false，其中timeout的单位为毫秒  
如果另一线程已经lock了这个mutex，则会等待timeout时间  
备注：如果timeout参数为负数，则等于调用lock()函数，即一直等待下去  

4. void QMutex::unlock()
unlock这个mutex  
在多个线程中对一个mutex进行unlock()操作会造成错误  
对一个没有处于locked状态的mutex进行unlock()操作会造成未知的后果  



