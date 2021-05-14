# QTime

## 基本功能
QTime提供时钟、计时器和时间相关的函数功能  
QTime可以进行时间大小的比较，越早的时间对象越小  
QTime使用的是24h制，不区分AM/PM  


## 代码示例
1. 获取当前时间，并转换为字符串
```
QTime time_now = QTime::currentTime();
QString string_time = time_now.toString("hh:mm:ss:zzz a");
```


## 构造函数
1. QTime::QTime(int h, int m, int s = 0, int ms = 0)
用时、分、秒、毫秒构造一个QTime对象  
每个参数都要符合其合理的范围，其中毫秒的范围为0-999，否则构造出的QTime对象是非法的  

2. QTime::QTime()
创建一个空的QTime对象，注意不是零点  
对于空的QTime对象，isNull()返回true，isValid()返回false  


## 常用公共函数
1. bool QTime::isNull() const
判断QTime对象是否为空，空对象一定是invalid的  

2. bool QTime::isValid() const
判断QTime对象是否合法  
例如，'23:30:55.746'是合法的，但'24:12:30'是非法的  

3. int QTime::hour() const
返回小时值，如果返回-1，则说明QTime对象是非法的  

4. int QTime::minute() const
返回分钟值，如果返回-1，则说明QTime对象是非法的  

5. int QTime::second() const
返回秒值，如果返回-1，则说明QTime对象是非法的  

6. int QTime::msec() const
返回毫秒值，如果返回-1，则说明QTime对象是非法的  

7. int QTime::msecsSinceStartOfDay() const
返回从今天半夜零点到当前时间的差值，单位毫秒  

8. QString QTime::toString(const QString &format) const
根据给定的格式，将QTime转换为一个字符串  
备注：可以不写参数，默认值为"hh:mm:ss"  
```
qDebug() << QTime::currentTime().toString("hh:mm:ss:zzz a");
```

9. QString QTime::toString(Qt::DateFormat format = Qt::TextDate) const
根据给定的格式，将QTime转换为一个字符串  

10. void QTime::start()
把该QTime对象的值设为当前时间，即currentTime()  

11. int QTime::restart()
把该QTime对象的值设为当前时间，即currentTime()，并以毫秒为单位返回中间的时间差值  


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


## 时间格式
```
字符		意义
h	小时，不补零，0-23 或 1-12 (如果显示 AM/PM)
hh	小时，补零2位显示，00-23 或 01-12 (如果显示 AM/PM)
H	小时，不补零，0-23 (即使显示 AM/PM)
HH	小时，补零显示，00-23 (即使显示 AM/PM)
m	分钟，不补零，0-59
mm	分钟，补零显示，00-59
s	秒，不补零，0-59
ss	秒，补零显示，00-59
z	毫秒，不补零，0-999
zzz	毫秒，补零 3 位显示，000-999
AP或A	使用 AM/pm 显示
ap或a	使用 am/pm 显示
```