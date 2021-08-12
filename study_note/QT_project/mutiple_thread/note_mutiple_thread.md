# Qt实现多线程样例

## 基本功能
模拟投掷骰子，在这个程序里只有主线程和子线程两个线程，主要演示一下多线程代码的基本写法  
QDiceThread类继承于QThread类，用来实现子线程任务(掷骰子)  
Dialog类继承于QDialog类，用来实现UI界面等主线程任务以及调用子线程  

使用了信号与槽机制来实现线程之间的通信和同步  
注意：并不是掷一次骰子就是一个子线程，而是整个掷骰子的过程都是子线程  