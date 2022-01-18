# QT中的多线程

## 线程相关的类
1. QThread
用来实现多线程操作的核心类
2. QMutex
提供相互排斥的锁，或互斥量
3. QMutexLocker
是QMutex的辅助类，自动对QMutex加锁与解锁
4. QReadWriteLock
提供了一个可以同时读操作的锁
5. QReadLocker
是QReadWriteLock的辅助类
6. QWriteLocker
是QReadWriteLock的辅助类
7. QWaitCondition
提供了一种方法，使得线程可以在被另外线程唤醒之前一直休眠
8. QSemaphore
提供了一个整型信号量，是互斥量的泛化


## 多线程的作用
一个应用程序一般只有一个线程，一个线程内的操作时顺序执行的  
如果线程中有某个比较消耗时间的操作(如网络通信中的文件传输)，用户界面就会冻结不能及时响应  
这种情况下，就可以创建出一个子线程，专门用来处理比较耗时的操作，并与主线程之间处理好同步与数据交互  
这就是一个多线程应用程序  


## 线程之间传递数据
1. 线程同步的需求
在多线程的应用程序中，多个线程之间可能需要访问同一个变量，或者一个线程需要等待另一个线程完成某个操作后才能产生相应的动作  
2. 利用信号与槽机制来传递数据
子线程执行完某个操作后发出信号和数据，主线程接收到信号和数据后执行相应的动作  
3. 利用主线程不断循环查询来传递数据
如果不使用信号与槽机制实现线程同步，则需要在子线程中定义公共函数用来返回数据  
由于主线程不知道何时去调用子线程的公共函数，只能采用不断循环的方式(一般使用QTimer)去查询是否有新数据  
当主线程读取数据时，子线程可能正在修改该数据，这样就会造成数据错误  
因此我们希望这段代码时被保护起来的，执行过程中不被其他线程中断，以保证数据的完整性  


## 1. 基于互斥量的线程同步
1. 基本原理
增加一个互斥量QMutex，将需要保护的代码包起来，相当于原子化操作  
如果一个线程对mutex进行了lock操作，则在该线程进行unlock之前，其他线程都不能再对其进行lock操作  
主线程需要用计时器不断循环的去读取子线程中的数据，还要检查读到的数据是否是新的数据  
2. 缺点
每次只有一个线程能获得mutex的权限，如果有多个线程读取某个变量，则必须进行排队等待  


## 2. 基于QReadWriteLock的线程同步
1. 基本原理
对于互斥量的改进：如果只是读取数据，而非写入数据，则可以允许多个线程同时访问  
多个线程可以同时拥有读取权限，但一旦有一个线程要写入数据，其他所有线程都会被locked，直到写入操作完成  
备注：QReadWriteLock的用法接近于QMutex，只是要区分是read锁还是write锁  
2. 缺点
一个线程在解锁资源后，不能及时通知其他需要使用该资源的线程，造成效率低下  


## 3. 基于QWaitCondition的线程同步
1. 基本原理
对互斥量的改进：一个线程在满足一定条件时，通知其他多个线程，使它们做出响应  
QWaitCondition一般用于'生产者/消费者'模型中，和QReadWriteLock/QMutex搭配使用  
备注：在书中的demo里，还是用了信号与槽机制，而不是主线程不断循环的去读子线程  


## 4. 基于信号量的线程同步
1. 基本原理
信号量(semaphore)也是一种对共享资源进行限制访问的线程同步机制  
信号量与互斥量很相似，但也有区别：一个互斥量只能被锁定一次，但信号量可以多次使用  
互斥量相当于单个卫生间，一次只允许一个人进出，信号量相当于多人公共卫生间，允许多人进出  
信号量通常用来保护一定数量的相同的资源，如数据采集时的双缓冲区  
2. 缺点
不能传递复杂消息，只能用来同步  


## 事件相关的概念
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


## 多线程程序关闭窗口
对于多线程的程序，如果在线程正在运行时直接点击关闭窗口，会产生报错  
因此要在线程类中对closeEvent函数进行重写，定义关闭窗口时的操作  
头文件中：  
```
#include <QCloseEvent>

class Dialog : public QDialog
{
	....
protected:
    void closeEvent(QCloseEvent *event);
    ....
}
```
源文件中：  
```
void Dialog::closeEvent(QCloseEvent *event)
{
    //重载函数，在窗口关闭时确保线程被停止
    if(threadA.isRunning())
    {
        threadA.terminate();
    }
    event -> accept();
}
```