# 使用信号量QSemaphore实现多线程同步

## 基本功能
模拟数据采集时的双缓冲区，一共三个线程
1. QThreadDAQ
数据采集线程：数据采集卡在进行连续数据采集时，需要一个单独的线程将采集卡采集的数据读取到缓冲区
2. QThreadShow
数据读取线程：用于读取已经存满数据的缓冲区中的数据，并传递给主线程显示，采用信号与槽机制与主线程交互  
3. Dialog
主线程：调用两个子线程，接收子线程传过来的数据并显示在窗口上