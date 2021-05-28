# QSemaphore

## 基本功能
QSemaphore提供了一个一般性的计数信号量（计数器）  
信号量是对互斥量的一般性泛化，一个互斥量只能被锁定一次，但信号量可以多次使用  
互斥量相当于单个卫生间，一次只允许一个人进出，信号量相当于多人公共卫生间，允许多人进出  


## 代码示例
1. 数据采集时的双缓冲区，分为两个线程
数据采集线程：例如数据采集卡在进行连续数据采集时，需要一个单独的线程将采集卡采集的数据读取到缓冲区  
数据读取线程：用于读取已经存满数据的缓冲区中的数据，并传递给主线程显示，采用信号与槽机制与主线程交互  
```
const int buffer_size = 8;
int buffer1[buffer_size]; //1号缓冲区，存储采集到的数据
int buffer2[buffer_size]; //2号缓冲区，存储采集到的数据

int current_buffer = 1; //当前正在写入的buffer，值为1或2
int buffer_number = 0; //缓冲区序号（已经写入数据的缓冲区个数）
int counter = 0; //数据生成器(模拟采集卡采集到的数据)

QSemaphore empty_buffers(2); //信号量：空的缓冲区个数，初始资源为2个
QSemaphore full_buffers; //信号量：满的缓冲区个数，初始资源为0个

void QThreadDAQ::run()
{
    m_stop = false;
    current_buffer = 1;
    buffer_number = 0;
    counter = 0;
    if(empty_buffers.available() < 2) //保证线程启动时，空的缓冲区可用资源为2个
    {
        empty_buffers.release(2 - empty_buffers.available());
    }
    while(!m_stop)
    {
        empty_buffers.acquire(1); //申请一个空的缓冲区资源
        for(int i = 0; i < buffer_size; i++)//向缓冲区中写入数据
        {
            if(current_buffer == 1)
                buffer1[i] = counter;
            else
                buffer2[i] = counter;
            counter ++; //模拟数据采集卡采集到的数据
            msleep(50); //假设每50ms采集到一个数据
        }
        buffer_number ++; //已经写入数据的缓冲区个数+1
        if(current_buffer == 1) //切换到另一个buffer继续写入
            current_buffer = 2;
        else
            current_buffer = 1;
        full_buffers.release(1); //释放(创建)一个满的缓冲区资源，即可用满的缓冲区资源+1
    }
    quit();
}

void QThreadShow::run()
{
    m_stop = false;
    if(full_buffers.available() > 0) //将full_buffers信号量的可用资源初始化为0
    {
        full_buffers.acquire(full_buffers.available());
    }
    while(!m_stop)
    {
        full_buffers.acquire(1); //申请一个满的缓冲区资源(如果没有就阻塞等待数采线程释放资源)
        int buffer_data[buffer_size]; //存储从缓冲区读到数据
        int seq = buffer_number;
        if(current_buffer == 1) //如果当前正在写入的缓冲区是1，则说明2号缓冲区已经满了
        {
            for(int i = 0; i < buffer_size; i++)
            {
                buffer_data[i] = buffer2[i]; //从2号缓冲区中拷贝数据
            }
        }
        else
        {
            for(int i = 0; i < buffer_size; i++)
            {
                buffer_data[i] = buffer1[i]; //从1号缓冲区中拷贝数据
            }
        }
        empty_buffers.release(1); //释放(创建)一个空的缓冲区资源，即可用空的缓冲区资源+1
        emit newValue(buffer_data, buffer_size, seq);
    }
    quit();
}
```


## 构造函数
1. QSemaphore::QSemaphore(int n = 0)
创建一信号量，并初始化n个由该信号量守护的资源，默认值为0  
```
QSemaphore sem(5);
```


## 常用公共函数
1. void QSemaphore::release(int n = 1)
释放n个由该信号量守护的资源  
备注：释放n个可用资源之后，可用资源就会加n  
注意：如果当前可释放资源为0个，这个函数也可以被用来创建新资源  
```
QSemaphore sem(5);
sem.acquire(5);         // 申请5个资源
sem.release(5);         // 释放5个资源
sem.release(10);        // 创建10个新的资源（当前可释放资源已经为0）
```

2. int QSemaphore::available() const
返回信号量当前可用资源的数量，返回值一定不是负数  

3. void QSemaphore::acquire(int n = 1)
试图申请n个由该信号量来守护的资源，如果n > available()，这个调用会被阻塞直到有足够的资源可用  
备注：申请n个资源之后，可用资源就会减n  

4. bool QSemaphore::tryAcquire(int n = 1)
如申请成功，则返回true，如果n > available()，则申请任何资源，立刻返回false  

5. bool QSemaphore::tryAcquire(int n, int timeout)
如申请成功，则返回true，如果n > available()，则等待timeout时间(单位毫秒)，立刻返回false  
如果timeout参数为负数，则一直等待下去，等效于调用了acquire()函数  