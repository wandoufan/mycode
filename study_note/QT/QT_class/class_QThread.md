# QThread

## 基本功能
QThread类提供了不依赖于平台的方法来管理多线程  
一个QThread对象管理着程序中的一个线程，将应用程序的线程称为主线程，将额外创建的线程称为工作线程  
父类：QObject  
子类：无  


## 使用过程
1. run()函数定义
定义一个继承于QThread的子类，在子类中对从QThread继承的虚函数run()进行重写，在run()中写明线程要实现的功能  
```
class MyThread::QThread
{
public:
    MyThread();

protected:
    void run() override;
};

void MyThread::run()
{
    //执行线程任务
}
```
2. 线程启动和执行过程
start()会在内部调用run()函数，run()函数会默认调用exec()函数来开启线程的事件循环  
备注：只需要在代码中手动调用start()，至于run()和exec()不要自己手动调用  
```
start() -> run() -> exec() -> 线程执行 -> exit()或quit()
```
3. 线程停止过程
方法1：在子线程中调用exit()或quit()来退出线程的事件循环
方法2：在主线程中调用terminate()来强制结束线程  
一般情况下，调用exit()或quit()来正常退出事件循环，也可以调用terminate()来强制结束线程(尽量避免使用)  


## 问题
1. exit()或quit()到底有什么作用？？？
run()函数的内容分为顺序执行和while循环的
但实际测试，不管怎样，只要run()执行完，即使不调用exit()或quit()，也会自动结束线程
相反，run()处在while循环中时，即使调用exit()或quit()也不会有作用
经过查看，项目的代码中除了WS8Module之外，都没有调用exit()或quit()，run()执行完成自动退出即可  

2. exit()或quit()的调用位置，是否要在run()中，还是子线程的任意位置？？？
WS8Module也不是在run()中去调用exit()或quit()，而是在修改标志位的函数中调用
```
void WS8Module::stopThread()
{
    mutex.lock();
    running = false;
    cond.wakeOne();
    mutex.unlock();

    fileThread.wait();

    if (fileThread.isRunning())
        fileThread.quit();
}
```


## run()函数的内容
1. 顺序执行
2. while循环
一般来说，会在while循环中设置一个标志位，有其他函数专门负责修改标志位，从而实现开始循环和退出循环的功能


## 启动多个线程
注意：把同一个线程对象start()多次不能启动多个线程  
1. 主线程启动一个子线程，然后子线程和主线程之间交互数据，这是最常用的一种情况
```
PrintThread *mythread1,
mythread1 = new PrintThread();
mythread1 -> start();
```
2. 定义一个线程类，并在主线程中定义多个线程对象，然后将每个线程对象都启动
```
PrintThread *mythread1, *mythread2, *mythread3;
mythread1 = new PrintThread();
mythread2 = new PrintThread();
mythread3 = new PrintThread();

mythread1 -> start();
QThread::msleep(500);
mythread2 -> start();
QThread::msleep(500);
mythread3 -> start();
```
3. 定义多个线程类，在主线程中定义多个线程对象，然后将每个线程对象都启动
```
PrintThread *mythread1, *mythread2;
ShowThread *mythread3, *mythread4;
mythread1 = new PrintThread();
mythread2 = new PrintThread();
mythread3 = new ShowThread();
mythread4 = new ShowThread();

mythread1 -> start();
QThread::msleep(500);
mythread2 -> start();
QThread::msleep(500);
mythread3 -> start();
QThread::msleep(500);
mythread4 -> start();
```


## 如何查看线程的ID
1. 通过QThread::currentThreadId()查看
可以用qDebug()把函数返回值输出出来，在每个线程的run()中调用都可以获得不同的16进制数  
注意：这里的返回值并不是线程ID本身，而是指针指向的内存地址，但是可以用来区分不同的线程  
```
0x33bc  :  0
0x33bc  :  1
0x2274  :  0
0x2274  :  1
0x33bc  :  2
0x41a8  :  0
0x2274  :  2
0x33bc  :  3
0x41a8  :  1
0x41a8  :  2
```
2. 通过QObject::thread()查看
对于所有继承自QObject的类，包括QThread，都可以调用QObject::thread()来查看当前线程  
QObject::thread()函数返回一个QThread指针，可以用qDebug()输出出来  
实际测试：不可用，在不同的位置调用这个函数，输出的值都一样  


## 构造函数
1. QThread::QThread(QObject \*parent = nullptr)
构造一个QThread对象来管理一个新的线程  
备注：在调用start()函数之前，线程不会开始执行  


## 常用公共函数
1. void QThread::exit(int returnCode = 0)
用给定的returnCode退出线程的事件循环  
调用exit()函数之后，线程会离开事件循环并调用QEventLoop::exec()，由QEventLoop::exec()来返回returnCode  
执行exit()函数之后，线程中不会有启动的事件循环，除非再次调用QThread::exec()  
备注：不要把QEventLoop::exec()和QThread::exec()混淆  
备注：returnCode为0代表成功，任何非0值代表错误  
备注：和C语言中的exit()函数不同，虽然返回类型是void，但确实可以把returnCode返回给调用者  
备注：这个函数是线程安全的  

2. bool QThread::isFinished() const
返回线程是否运行结束  
备注：这个函数是线程安全的  

3. bool QThread::isRunning() const
返回线程是否正在运行  
备注：这个函数是线程安全的  

4. int QThread::loopLevel() const
返回当前事件循环对于线程的等级  
注意：这个线程只能在线程本身的内部进行调用  

5. QThread::Priority QThread::priority() const
返回线程的优先级，如果线程此时没有在运行，则返回'InheritPriority'  

6. void QThread::setPriority(QThread::Priority priority)
为一个正在运行的线程设置优先级，如果线程此时没有在运行，则函数不做任何操作并立即返回  
优先级参数可以是集合中的任何值，除了'InheritPriority'  

7. bool QThread::wait(QDeadlineTimer deadline = QDeadlineTimer(QDeadlineTimer::Forever))
wait()函数用来阻塞直到该线程执行完成后，再执行wait()函数下面的代码，即等待当前进程执行完成  
当满足下面两个条件之一时执行阻塞：  
a. 当线程已经运行完成(从run()函数中返回)或者还没有开始运行时，则返回true  
b. 如果到达了deadline的时间，则返回false  
deadline参数的默认值为QDeadlineTimer::Forever，即永远不会超时  
这种情况下，只有在线程已经运行完成(从run()函数中返回)或者还没有开始运行时，wait()函数才返回  
备注：这个函数是在Qt 5.15版本中才被引入进来的  
```
//一般在线程退出时，都要调用wait()函数，因为事件循环队列中可能还有事件没有处理完
mythread -> quit();
mythread -> wait();
```

8. bool QThread::wait(unsigned long time)
这是一个重载函数，设置线程阻塞的时间  


## 公共槽函数
1. [slot] void QThread::quit()
退出线程的事件循环并返回code 0(成功)，效果等于调用了QThread::exit(0)  
如果该线程中没有事件循环，则quit()函数不做任何操作  
备注：这个函数是线程安全的  

2. [slot] void QThread::start(QThread::Priority priority = InheritPriority)
调用run()函数来开始执行线程  
如果线程已经在运行了，则该函数不做任何操作  
priority参数表示操作系统安排新线程的方式，详见下面enum QThread::Priority  

3. [slot] void QThread::terminate()
强制结束线程的执行  
线程是否会被立即结束取决于操作系统的线程策略，可以在terminate()函数之后再调用QThread::wait()函数来进行确保  
备注：当一个线程被强制结束后，所有等待该线程完成的其他线程都会被立即唤醒  
注意：这个函数比较危险，例如进程可能会在修改数据时被强制结束，因此尽量避免使用  
备注：这个函数是线程安全的  


## 信号函数
1. [signal] void QThread::finished()
在关联的线程即将执行完成之前，这个信号发出(一般在调用quit()等函数之后发出该信号)  
当这个信号发出时，事件循环就已经停止运行了，除了延期删除事件外，线程中不会再执行任何事件  
这个信号可以被关联到槽函数QObject::deleteLater()上，来释放线程中的对象  
注意：如果关联的线程被terminate()函数终结了，发出信号的线程就变成未定义的了  
注意：这是一个私有的信号，可以用在信号connection中，但不能被用户发出  

2. [signal] void QThread::started()
在关联的线程开始执行前，这个信号发出(一般在调用start()函数之后发出该信号)  
注意：这是一个私有的信号，可以用在信号connection中，但不能被用户发出  


## 静态公共函数
1. [static] template <typename Function, typename Args> QThread \*QThread::create(Function &&f, Args &&... args)
创建并返回一个新的QThread对象，这个新线程会用给定的arg参数执行函数f  
可以连接信号函数、把QObject添加到线程里、选择新线程的优先级等等  
注意：对返回的实例对象不要调用start()函数超过一次，否则可能会造成未知的错误  
备注：类似与构造函数，在调用start()函数之前，创建的线程对象不会执行  
备注：这个函数只有在使用C++17时才支持  

2. [static] template <typename Function> QThread \*QThread::create(Function &&f)
功能同上，只是函数不带参数  

3. [static] QThread \*QThread::currentThread()
返回一个指针指向QThread对象，这个QThread对象管理着当前正在执行的线程  

4. [static] Qt::HANDLE QThread::currentThreadId()
返回当前正在执行的线程的句柄，相当于线程ID  
注意：返回的句柄只能用作Qt内部调用，不能自己用在任何程序代码中  
备注：Qt::HANDLE在所有平台上的定义都是空类型指针`void *`  
备注：在Windows平台上，这个函数返回一个DWORD(Windows-Thread ID)，这个DWORD是由Win32函数GetCurrentThreadId()返回的  
关于将currentThreadId()输出出来的方法：  
备注：根据网上的资料，Qt::HANDLE设计时就不是用来直接输出的，也不建议这么操作  
4.1 用qDebug()可以直接输出出来，结果为一个16进制数  
注意：这个数并不是线程ID本身，而是指针指向的内存地址  
```
qDebug() << "id: " << mythread -> currentThreadId();//输出：0x44f8
```
4.2 将Qt::HANDLE转换为QString或int，尝试多次都失败了，会内存报错  

5. [static] int QThread::idealThreadCount()
返回系统中最多可以同时运行的线程的数量，实际就是电脑CPU的核数  
这个数量是通过查询处理器的个数得到的，如果处理器的个数探测不到，则函数返回1  

6. [static] void QThread::msleep(unsigned long msecs)
强制当前线程休眠一段时间，单位为毫秒  
注意：这个函数不保证准确度，在系统负载较大的情况下，实际休眠时间可能比指定时间更长  

7. [static] void QThread::sleep(unsigned long secs)
强制当前线程休眠一段时间，单位为秒  
注意：这个函数不保证准确度，在系统负载较大的情况下，实际休眠时间可能比指定时间更长  

8. [static] void QThread::usleep(unsigned long usecs)
强制当前线程休眠一段时间，单位为微秒  
注意：这个函数不保证准确度，在系统负载较大的情况下，实际休眠时间可能比指定时间更长  


## 保护函数
1. [protected] int QThread::exec()
启动并进入到一个事件循环中，然后开始执行循环队列中的事件，如果调用了exit()或quit()就会退出事件循环，并返回returnCode  
如果exit()函数是经由quit()函数调用的，则返回值为0  
这个函数是设计用来在run()函数内部进行调用的，而且也只能在当前线程内部自己调用  
备注：从Qt4.4开始，run()函数就会默认调用exec()函数，因此一般不需要自己在run()函数中手动调用  
注意：exec()没有退出事件循环或停止线程的功能，不要和exit()混淆  

2. [virtual protected] void QThread::run()
在调用start()函数之后，新创建的线程自动会调用这个run()函数，run()函数会再进一步调用exec()函数  
注意：一般要在子类中对这个方法进行重写，在函数里实现线程需要完成的任务  
注意：当run()函数执行完成并返回时，会自动结束线程的执行，不管是否调用了exit()或quit()  
备注：run()不能直接调用，而是要通过调用start()函数来间接调用run()函数
```
//头文件中
protected:
    void run() override;

//源文件中
void QDiceThread::run()
{
    //执行线程任务
    m_stop = false;
    m_seq = 0;
    while(!m_stop)
    {
        if(!m_paused)
        {
            m_diceValue = QRandomGenerator::global() -> bounded(1, 7);
            m_seq ++;
            emit newValue(m_seq, m_diceValue);
        }
        msleep(500);
    }
    quit();
}
```


## enum QThread::Priority
这个集合中的值表示操作系统应该如何安排新创造的线程，即新线程的优先级  
优先级参数的效果取决与操作系统的优先级策略  
如果操作系统本身不支持线程优先级(如Linux)，则优先级参数会被忽略掉  
```
Constant   Value   Description
QThread::IdlePriority   0   只有在没有其他线程运行时才安排新线程(默认)
QThread::LowestPriority   1   scheduled less often than LowPriority.
QThread::LowPriority   2   scheduled less often than NormalPriority.
QThread::NormalPriority   3   the default priority of the operating system.
QThread::HighPriority   4   scheduled more often than NormalPriority.
QThread::HighestPriority   5   scheduled more often than HighPriority.
QThread::TimeCriticalPriority   6   scheduled as often as possible.
QThread::InheritPriority   7   使用和创造线程相同的优先级(默认)
```