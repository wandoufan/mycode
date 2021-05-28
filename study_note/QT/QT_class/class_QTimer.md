# QTimer

## 基本功能
QTimer类提供了单次触发的定时器和循环重复的定时器  
使用前要'#include <QTimer>'  
注意：QTimer并不是一个可见的组件，在UI设计器里找不到它  


## 使用示例
1. 循环重复定时器
```
//每秒钟执行一次监听函数  
QTimer *timer;
timer = new QTimer(this);
connect(timer, SIGNAL(timeout()), this , SLOT(listen()));
timer -> start(1000);
```
2. 单次触发定时器
```
//一分钟之后再去执行test函数，相当于sleep了一分钟
QTimer::singleShot(60000, this, SLOT(test()));
```


## 构造函数
1. QTimer::QTimer(QObject \*parent = nullptr)


## 常用公共函数
1. int interval() const
查询当前的interval值，即每个循环周期的长度，单位毫秒，默认为0  

2. void setInterval(int msec)
设置的interval值，单位毫秒，一般可以直接在调用start函数时设置  
interval函数和start函数的参数值都是用来设置每个循环周期的长度  
注意：如果interval函数和start函数都进行了设置，则以后面设置的参数为准  

3. bool isActive() const
查询当前计时器是否在运行  

4. bool isSingleShot() const
查询当前定时器是否是单次定时器  


## 公共槽函数
1. [slot] void QTimer::start(int msec)
用来启动或重启一个循环计时器，其中函数参数表示每个循环周期的长度  
例如，start(2000)相当于每隔2秒钟去执行一次槽函数  
如果之前已经用setInterval函数进行过设置，则start函数的参数可以为空  
如果计时器已经在运行，则计时器停止并重新开始计时  
如果计时器是单次的，则计时器只会运行一次  
interval函数和start函数的参数值都是用来设置每个循环周期的长度  
注意：如果interval函数和start函数都进行了设置，则以后面设置的参数为准  

2. [slot] void QTimer::start()
这是一个重载函数，不需要填写时间参数  

3. [slot] void QTimer::stop()
stop函数是一个槽函数，用来停止计时器  


## 信号函数
1. [signal] void QTimer::timeout()
timeout函数是QTimer最主要的信号函数，一般用在connect函数的信号参数中  
当时间用完时就会触发timeout函数  
注意：这是一个私有的信号函数，可以用在connect中，但不能被用户去触发  


## 公共静态函数
1. [static] void QTimer::singleShot(int msec, const QObject \*receiver, const char \*member)
singleShot函数用来启动单次触发定时器，相当于sleep函数  
第一个参数是定时时间  
第二个参数是接收对象  
第三个参数是时间到了之后被触发的槽函数  
备注：singleShot是一个静态公共函数，即可以不经实例化就直接调用，使用很方便  