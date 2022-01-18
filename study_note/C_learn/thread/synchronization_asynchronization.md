# C语言中的同步和异步

## 基本概念
1. 同步阻塞执行(串行)
在代码中调用一个函数，必须等该函数执行完并返回后，代码才能继续往下执行
在被调用函数执行期间，代码会被阻塞，直到函数执行完成
备注：默认情况下，C代码会按同步执行，更加节约系统资源
2. 异步非阻塞执行(并行)
在代码中调用一个函数，函数会自己开始执行，代码不必等待就继续往下执行
当调用多个函数时，哪个函数执行速度更快就会更早完成执行，与调用函数的先后顺序无关
备注：异步执行需要开启多线程的方式，速度更快，但需要耗费更多的系统资源



## 线程相关的概念
1. 主线程
程序的入口，相当于main函数，是创建其他子线程的线程，主线程消亡时，其他线程也会跟着消亡
2. 守护线程
随主线程一块结束的线程是守护线程
3. 非守护线程
主线程结束时还可以继续运行的是非守护线程
4. 父线程
能够创建子线程的就是父线程，父线程消亡时，子线程也可以继续执行
5. 子线程
被父线程创建出来的就是子线程