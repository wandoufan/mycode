# QTime

## 基本功能
QTime提供时钟、计时器和时间相关的函数功能  
父类：无  
子类：无  


## 说明
1. QTime没有时间戳，如果要计算时间戳，使用QDatetime  
2. QTime使用的是24h制，不区分AM/PM  


## 代码示例
1. 获取当前时间，并转换为字符串
```
QTime time_now = QTime::currentTime();
QString string_time = time_now.toString("hh:mm:ss:zzz a");
```

2. 比较两个时间点的大小
备注：越早的时间，数值越小
方法1：直接使用>符号比较
```
QTime time1 = QTime::currentTime();
//程序主体
...
QTime time2 = QTime::currentTime();
if(time1 > time2)
    qDebug() << "time1 > time2";
else
    qDebug() << "time1 < time2";
```
方法2：判断msecsTo()或secsTo()函数返回值的正负
```
QTime time1 = QTime::currentTime();
//程序主体
...
QTime time2 = QTime::currentTime();
if(time1.msecsTo(time2) > 0)
    qDebug() << "time1 < time2";
else
    qDebug() << "time1 > time2";
```

3. 计算两个时间点的差值
方法1：使用elapsed()函数
```
QTime time;
time.start();
//程序主体
...
int cost_time = time.elapsed();
qDebug() << cost_time;
```
方法2：使用restart()函数
```
QTime time;
time.start();
//程序主体
...
int cost_time = time.restart();
qDebug() << cost_time;
```
方法3：用msecsTo()或secsTo()函数获取数值  
```
QTime time1 = QTime::currentTime();
//程序主体
...
QTime time2 = QTime::currentTime();
int cost_time = time1.secsTo(time2);
qDebug() << cost_time;
```

## 构造函数
1. QTime::QTime(int h, int m, int s = 0, int ms = 0)
用时、分、秒、毫秒构造一个QTime对象  
每个参数都要符合其合理的范围，其中毫秒的范围为0-999，否则构造出的QTime对象是非法的  

2. QTime::QTime()
创建一个空的QTime对象，注意不是零点  
对于空的QTime对象，isNull()返回true，isValid()返回false  


## 常用公共函数：设置/修改QTime对象的值
1. bool QTime::setHMS(int h, int m, int s, int ms = 0)
设置QTime对象的值，根据参数值是否合法来返回是否设置成功  

2. QTime QTime::addMSecs(int ms) const
将当前的时间对象加上ms毫秒，然后将新的时间对象返回  
ms参数也可以为负数，会得到一个当前时间对象之前的新的时间对象  

3. QTime QTime::addSecs(int s) const
将当前的时间对象加上s秒，然后将新的时间对象返回  
s参数也可以为负数，会得到一个当前时间对象之前的新的时间对象  
```
QTime n(14, 0, 0);                // n == 14:00:00
QTime t;
t = n.addSecs(70);                // t == 14:01:10
t = n.addSecs(-70);               // t == 13:58:50
t = n.addSecs(10 * 60 * 60 + 5);  // t == 00:00:05
t = n.addSecs(-15 * 60 * 60);     // t == 23:00:00
```


## 常用公共函数：获取QTime对象的信息
1. bool QTime::isNull() const
判断QTime对象是否为空，空对象一定是非法的  

2. bool QTime::isValid() const
判断QTime对象是否合法  
例如，'23:30:55.746'是合法的，但'24:12:30'是非法的  

3. int QTime::hour() const
返回QTime对象中的小时值，如果返回-1，则说明QTime对象是非法的  

4. int QTime::minute() const
返回QTime对象中的分钟值，如果返回-1，则说明QTime对象是非法的  

5. int QTime::second() const
返回QTime对象中的秒值，如果返回-1，则说明QTime对象是非法的  

6. int QTime::msec() const
返回QTime对象中的毫秒值，如果返回-1，则说明QTime对象是非法的  


## 常用公共函数：用QTime来计算时间
1. int QTime::msecsSinceStartOfDay() const
返回从今天半夜零点到当前时间点的差值，单位毫秒  

2. int QTime::msecsTo(const QTime &t) const
返回从本时间对象到t时间对象的差值，单位毫秒  
如果t时间对象比本时间对象更早，则返回值为负数  
如果返回0，则说明其中有一个时间对象是非法的  
备注：QTime是用一天来度量时间，一天有86400秒，因此函数返回值在(-86400000, 86400000)之间  

3. int QTime::secsTo(const QTime &t) const
返回从本时间对象到t时间对象的差值，单位秒，不统计毫秒的部分  
如果t时间对象比本时间对象更早，则返回值为负数  
如果返回0，则说明其中有一个时间对象是非法的  
备注：QTime是用一天来度量时间，一天有86400秒，因此函数返回值在(-86400, 86400)之间  

3. void QTime::start()
把该QTime对象的值设为当前时间，这个函数一般在计时的时候使用  
备注：实际测试，调用该函数时，编译器提示函数为'deprecated'(强烈反对)，原因未知  

4. int QTime::restart()
把该QTime对象的值设为当前时间，并以毫秒为单位返回上次调用start()或restart()的时间点到当前时间的差值  
start()和restart()常结合起来用作计时器  
如果计时时间超过24小时，则计时器结果清零  
如果在计时过程中，系统的时钟发生了改变，则计时结果不确定  
备注：实际测试，调用该函数时，编译器提示函数为'deprecated'(强烈反对)，原因未知  

5. int QTime::elapsed() const
以毫秒为单位返回上次调用start()或restart()的时间点到当前时间的差值  
如果计时时间超过24小时，则计时器结果清零  
如果在计时过程中，系统的时钟发生了改变，则计时结果不确定  
注意：这个时间的准确度依赖于操作系统，并非所有的操作系统都能提供毫秒级的准确度  
备注：实际测试，调用该函数时，编译器提示函数为'deprecated'(强烈反对)，原因未知  


## 常用公共函数：QTime转字符串
1. QString QTime::toString(const QString &format) const
根据给定的格式，将QTime转换为一个字符串  
备注：可以不写参数，默认值为"hh:mm:ss"  
```
qDebug() << QTime::currentTime().toString("hh:mm:ss:zzz a");
```

2. QString QTime::toString(Qt::DateFormat format = Qt::TextDate) const
根据给定的格式，将QTime转换为一个字符串  

3. QString QTime::toString(QStringView format) const


## 静态公共函数
1. [static] QTime QTime::currentTime()
根据系统时钟返回当前的时间  
注意：这个时间的准确度依赖于操作系统，并非所有的操作系统都能提供毫秒级的准确度  

2. [static] QTime QTime::fromMSecsSinceStartOfDay(int msecs)
返回一个时间，这个时间等于半夜零点 + 给定的毫秒数  
```
//结果为08:20:00
QTime time1 = QTime::fromMSecsSinceStartOfDay(30000000);
```

3. [static] QTime QTime::fromString(const QString &string, Qt::DateFormat format = Qt::TextDate)
根据给定格式的时间字符串，返回一个QTime对象  

4. [static] QTime QTime::fromString(const QString &string, const QString &format)
根据给定格式的时间字符串，返回一个QTime对象  

5. [static] bool QTime::isValid(int h, int m, int s, int ms = 0)
判断QTime对象是否合法  


## 时间格式format
```
字符		意义
h		小时，不补零，0-23 或 1-12 (如果显示 AM/PM)
hh		小时，补零2位显示，00-23 或 01-12 (如果显示 AM/PM)
H		小时，不补零，0-23 (即使显示 AM/PM)
HH		小时，补零显示，00-23 (即使显示 AM/PM)
m		分钟，不补零，0-59
mm		分钟，补零显示，00-59
s		秒，不补零，0-59
ss		秒，补零显示，00-59
z		毫秒，不补零，0-999
zzz		毫秒，补零 3 位显示，000-999
AP或A	使用 AM/pm 显示
ap或a	使用 am/pm 显示
```