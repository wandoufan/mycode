# 主要记录进程、线程、协程方面的基本知识


## 进程(process)
### 基本概念
进程是计算机上程序的一次执行过程，是一个动态的产生消亡的过程  
进程是一个实体，有自己独立的地址空间和各种资源，是系统进行资源分配和调度的基本单位  
进程由程序、数据和进程控制块(PCB)三部分组成  
进程可以创建一个新的进程，二者为父子关系，且任何进程只能有一个父进程  
注意：同一个程序执行两次得到的属于两个不同的进程  

### 并发与并行
并发执行是指多个进程轮流使用CPU等资源，看起来像是在同时运行，单CPU的环境下采用多路复用就可以实现  
并行执行是指多个进程真正在同时运行，必须要在多核CPU的环境下才能运行  

### 进程的三个状态
1. 运行态
进程占有CPU资源正在运行中，可以转换为就绪态或阻塞态  
2. 就绪态
进程具备运行条件，唯一需要的就是等待分配CPU资源，可以转换为运行态  
3. 阻塞态
不具备运行条件，正在等待某个事件的完成，可以转换为就绪态  

### 进程的创建时机
1. 系统初始化时，系统的调度进程创建init进程
2. 进程运行过程中根据需要创建了一个子进程
3. 用户与系统交互过程中创建了新的进程，如用户双击程序图标
4. 一个批处理作业的初始化（只在大型机的批处理系统中应用）
备注：UNIX系统用fork()系统调用来创建新进程，而windows系统用CreatProcess()来创建新进程  

### 进程间通信
进程间通信(IPC，Inter-Process Communication)，指至少两个进程或线程间传送数据或信号的一些技术或方法
1. 管道(pipe)/无名管道
管道是一种半双工的通信方式，数据只能单向流动，而且只能在父子进程或兄弟进程之间使用
管道可以看做特殊文件，能够用read、write函数读写，但它不属于任何文件系统，只存在于内存中
缺点：速度慢，容量有限，只能在父子进程或兄弟进程之间使用

2. 命名管道(FIFO)
命名管道是半双工的通信方式，但可以在任意的进程之间交换数据，实现通信
命名管道是一种文件类型，它以一种特殊设备文件形式存在于文件系统中
缺点：速度慢，容量有限

3. 消息队列(Message Queue)
消息队列是消息的链表，存放在内核中，一个消息队列由一个标识符(队列ID)来唯一标识
消息队列是面向记录的，其中的消息具有特定的格式和特定的优先级
消息队列独立于进程，即进程终止时，消息队列中对应的进程消息内容不会被删除
消息队列可以实现消息的随机查询，消息可以按照先进先出或消息类型进行读取
消息队列克服了信号传递信息少、管道只能承载无格式字节流以及缓冲区大小受限等缺点
缺点：容量受到系统限制，且要注意第一次读的时候，要考虑上一次没有读完数据的问题

4. 信号量(semaphore)
信号量是一个计数器，用于实现进程间的互斥与同步，而不是用于存储进程间通信数据
信号量相当于一个锁机制，用来控制多个进程对共享资源的访问，防止发生冲突
信号量基于操作系统的 PV 操作，程序对信号量的操作都是原子操作
缺点：不能传递复杂消息，只能用来同步

5. 共享内存(Shared Memory)
共享内存是多个进程共享一个给定的区域，这段共享内存由一个进程创建，但多个进程都可以访问
共享内存方式的通信数据都是进程直接在内存中读写，因此速度是最快的
多个进程共同访问共享内存时可能会发生冲突，需要用信号量实现锁机制，常用共享内存+信号量模式
缺点：进程之间需要保持同步


## 线程(thread)
### 基本概念
进程创建、撤消与切换等操作时开销过大，为了降低开销成本，因此引入了线程
线程可以看做轻量级的进程，是CPU调度的最小单位，它被包含在进程之中，是进程中的实际运作单位
线程是由进程分出来的，本身不独立拥有系统资源，只有一点运行必不可少的寄存器等资源
同一进程中的各个线程共享该进程的资源，即这些线程拥有相同的地址空间，共享进程的文件、内存、信号量等
同一进程中的多个线程可以并发执行，不同进程之间的多个线程也可以并发执行
线程由程序、数据和线程控制块(TCB)三部分组成
注意：由于同一个进程内的线程共享内存和文件，所以线程之间互相通信不必调用内核

### 多线程的作用
一个应用程序一般只有一个线程，一个线程内的操作时顺序执行的  
如果线程中有某个比较消耗时间的操作(如网络通信中的文件传输)，用户界面就会冻结不能及时响应  
这种情况下，就可以创建出一个子线程，专门用来处理比较耗时的操作，并与主线程之间处理好同步与数据交互  
这就是一个多线程应用程序  

### 线程相关的概念
主线程：程序的入口，相当于main函数,是创建其他子线程的线程，主线程消亡时，其他线程也会跟着消亡
守护线程：随主线程一块结束的线程是守护线程
非守护线程：主线程结束时还可以继续运行的是非守护线程
父线程：能够创建子线程的就是父线程，父线程消亡时，子线程可以继续执行
子线程：被父线程创建出来的就是子线程
注意：在python中当没有存活的非守护进程时，整个python程序才会退出
也就是说，如果主线程运行完后如果还有其他非守护线程运行,主线程是不会退出的，会被无限挂起


## 进程和线程的比较
### 进程和线程的区别
1. 一个程序至少有一个进程，一个进程至少有一个线程，线程是包含在进程之中的
2. 进程是系统资源分配的基本单位，有自己独立的地址空间；线程是CPU调用的基本单位，没有独立的系统资源
3. 线程可以看做一个轻量级的进程，线程创建、撤消与切换的系统开销更小
4. 线程的划分尺度小于进程，使得多线程程序的并发性高，对CPU的使用效率更高
5. 线程适合于在SMP机器(双CPU系统)上运行，而进程则可以跨机器迁移
6. 一个进程崩溃后，在保护模式下不会对其他进程产生影响，但是一个线程崩溃整个进程都死掉，所以多进程要比多线程健壮

### 多进程和多线程的选择
对资源的管理和保护要求高，不限制开销和效率时，使用多进程
要求效率高，频繁切换时，资源的保护管理要求不是很高时，使用多线程


## 协程(Coroutine)/微线程/纤程
协程是一种比线程更加轻量级的存在，正如一个进程可以拥有多个线程一样，一个线程也可以拥有多个协程
协程不是被操作系统内核所管理，而完全是由程序所控制，因此协程的资源开销远远小于线程
协程与子例程一样，也是一种程序组件，但相对子例程而言，协程更为一般和灵活，但在实践中使用没有子例程那样广泛
协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行