# QT中的多线程

## 基本情况


## 线程相关的类
QThread
用来实现多线程操作的核心类
QMutex
QMutexLocker
QReadWriteLock
QWaitCondition
QSemaphore

继承关系：


## 线程中的事件循环
1. 事件
Qt是事件驱动的，事件由一个普通对象表示(QEvent或其子类)，事件可以由程序产生，也可以由程序外部产生  
事件和信号的区别：事件并不是一产生就被分发  
2. 事件队列
事件产生之后就会被加入到一个队列中(先进先出)，即事件队列  
3. 事件循环
事件分发器会不断遍历事件队列，如果发现事件队列中有事件，那么就把这个事件发送给它的目标对象，这个循环被称作事件循环  
每个Qt应用程序中至少有一个事件循环  
4. 主事件循环(主循环)
将处于调用main()函数的那个线程中，并且由QCoreApplication::exec()创建开启的事件循环称为主事件循环  
QCoreApplication::exec()只能在调用main()函数的线程中调用，因此主循环所在的线程就是主线程，也被称为GUI线程  
5. 局部事件循环
QThread也可以通过在QThread::run()中调用QThread::exec()来开启一个局部事件循环  


## 线程安全(thread-safety)和可重入(reentrant)
详见Qt帮助文档中的"Reentrancy and Thread-Safety"  
1. 一个线程安全的函数可以同时的被多个线程调用，包括所有的调用使用了共享的数据，因为对共享数据的引用都是序列化连续的
2. 一个可重入的函数也可以同时的被多个线程调用，但前提是，每个调用使用它自己的数据
3. 因此一个线程安全的函数一定是可重入的，一个可重入的函数不一定是线程安全的
4. 如果一个类是线程安全的，则说明类的成员函数可以被多个线程安全的调用，即使每个线程都使用了类的同一个实例
5. 如果一个类是可重入的，则说明类的成员函数可以被多个线程安全的调用，但前提是，每个线程使用了类的不同实例
备注：只有在Qt文档中对类或函数进行了thread-safety或reentrant的标记，才可以在多个线程中去使用  
备注：大多数Qt类都是可重入的，但不是线程安全的，因为线程安全需要很多额外的QMutex方面的开销  
例1：这个类不是线程安全的，因为对成员变量n的加减操作不是原子化的，多个线程同时读写n时可能会出现错误  
```
class Counter
{
public:
	Counter() { n = 0; }

	void increment() { ++n; }
	void decrement() { --n; }
	int value() const { return n; }

private:
	int n;
};
```
例2：使用QMutex来保护成员变量，从而使类变成线性安全的  
```
class Counter
{
public:
	Counter() { n = 0; }

	void increment() { QMutexLocker locker(&mutex); ++n; }
	void decrement() { QMutexLocker locker(&mutex); --n; }
	int value() const { QMutexLocker locker(&mutex); return n; }

private:
	mutable QMutex mutex;
	int n;
};
```


## 信号与槽和多线程
详见QT帮助文档"Threads and QObjects"  

## Qt多线程的原则
https://www.cnblogs.com/icmzn/p/7348264.html
待补充。。。


## 多窗口与多线程
多个窗口之间的通信
> https://blog.csdn.net/qq_34719188/article/details/79945717
