# QDatetime

## 基本功能
QDatetime类提供日期和时间相关的函数  
另外，还有QDate类单独提供日期相关的功能，QTime类单独提供时间相关的功能  
父类：无  
子类：无  


## 说明
1. 时区
QDatetime支持本地时间、UTC时区、UTC偏移时区、指定时区等时区，但这些时区的区别没搞明白  
2. 没有0年
QDatetime中的year不能是0，否在QDatetime是非法的  
3. 数值合法范围
QDateTime是存储在一个qint64变量中，合法范围为+/-292百万年  
作为对比，QDate的范围为+/-20亿年  
4. QDatetime可以用来获取时间戳偏移量
时间戳表示的是从1970年1月1日00:00:00开始按秒或毫秒计算的偏移量  
注意：时间戳偏移量应该用qint64存储，如果使用int存储，会有精度不够的问题

## 代码示例
1. 把QDateTime按照一定格式转化成字符串  
只要中间的标识符能对应上就可以，格式任意写  
```
QDateTime current_datetime = QDateTime::currentDateTime();
QString string1 = current_datetime.toString("yyyy:MM:dd:hh:mm:ss"));
QString string2 = current_datetime.toString("dd.MM.yyyy"));
QString string3 = current_datetime.toString("yy:MM:dd - hh:mm"));
...
```

2. 比较两个时间点的大小
方法参考QTime  

3. 计算两个时间点的差值
方法1：使用secsTo()或msecsTo()函数
```
QDateTime now = QDateTime::currentDateTime();
QDateTime xmas(QDate(now.date().year(), 12, 25).startOfDay());
qDebug("There are %d seconds to Christmas", now.secsTo(xmas));
```
方法2：使用toSecsSinceEpoch()或toMSecsSinceEpoch()函数
```
QDateTime datetime1 = QDateTime::currentDateTime();
//程序主体
...
QDateTime datetime2 = QDateTime::currentDateTime();
int cost_time = datetime1.toSecsSinceEpoch() - datetime2.toSecsSinceEpoch();
```


## 构造函数
1. QDateTime::QDateTime(QDateTime &&other)

2. QDateTime::QDateTime(const QDateTime &other)

3. QDateTime::QDateTime(const QDate &date, const QTime &time, const QTimeZone &timeZone)
使用一个QDate对象和一个QTime对象来获得一个QDateTime对象  
如果QDate对象是合法的，而QTime对象是非法的，则QDateTime对象中的时间部分会被设置为00:00:00  
如果timeZone是非法的，则生成的QDateTime对象也是非法的  

4. QDateTime::QDateTime(const QDate &date, const QTime &time, Qt::TimeSpec spec, int offsetSeconds)
使用一个QDate对象和一个QTime对象来获得一个QDateTime对象  
如果QDate对象是合法的，而QTime对象是非法的，则QDateTime对象中的时间部分会被设置为00:00:00  

5. QDateTime::QDateTime(const QDate &date, const QTime &time, Qt::TimeSpec spec = Qt::LocalTime)
使用一个QDate对象和一个QTime对象来获得一个QDateTime对象  
如果QDate对象是合法的，而QTime对象是非法的，则QDateTime对象中的时间部分会被设置为00:00:00  

6. QDateTime::QDateTime(const QDate &date)
使用一个QDate对象来获得一个QDateTime对象，QDateTime对象中的时间部分会被设置为00:00:00  

7. QDateTime::QDateTime()
获得一个空的QDateTime对象，这个空的对象是非法的  


## 常用公共函数：设置QDateTime对象的值
1. void QDateTime::setDate(const QDate &date)
设置datetime中的date部分，如果date是非法的，则datetime也会变成非法的  

2. void QDateTime::setTime(const QTime &time)
设置datetime中的time部分，如果QTime对象是非法的，则QDateTime对象中的时间部分会被设置为00:00:00  
```
//把datetime中的time部分清零
QDateTime dt = QDateTime::currentDateTime();
dt.setTime(QTime());
```

3. void QDateTime::setMSecsSinceEpoch(qint64 msecs)
以毫秒为单位设置datetime(相对于时间戳)  

4. void QDateTime::setSecsSinceEpoch(qint64 secs)
以秒为单位设置datetime(相对于时间戳)  


## 常用公共函数：修改QDateTime对象的值(加减时间)
备注：这些参数都可以是负值  
1. QDateTime QDateTime::addYears(int nyears) const

2. QDateTime QDateTime::addMonths(int nmonths) const

3. QDateTime QDateTime::addDays(qint64 ndays) const

4. QDateTime QDateTime::addSecs(qint64 s) const

5. QDateTime QDateTime::addMSecs(qint64 msecs) const


## 常用公共函数：获取QDateTime对象的信息
1. bool QDateTime::isNull() const
当date和time都是null的时候，返回ture，否则返回false  
一个null的QDateTime对象是非法的  

2. bool QDateTime::isValid() const
当date和time在当前时区下都是合法的，返回ture，否则返回fasle  
注意：如果datetime中的date部分或time部分为空，则整个datetime也都是非法的  

3. QTime QDateTime::time() const

4. QDate QDateTime::date() const


## 常用公共函数：用QDateTime来计算时间
1. qint64 QDateTime::toSecsSinceEpoch() const
以秒为单位返回从时间戳到本时间对象之间的差值，一般返回值都是正值  

2. qint64 QDateTime::toMSecsSinceEpoch() const
以毫秒为单位返回从时间戳到本时间对象之间的差值，一般返回值都是正值  

3. qint64 QDateTime::msecsTo(const QDateTime &other) const
以毫秒为单位返回本时间对象到other时间对象之间的差值  
如果other时间对象比本时间对象更早，则返回值为负值  
如果返回0，则说明其中有一个时间对象是非法的  

4. qint64 QDateTime::secsTo(const QDateTime &other) const
以秒为单位返回本时间对象到other时间对象之间的差值  
如果other时间对象比本时间对象更早，则返回值为负值  
如果返回0，则说明其中有一个时间对象是非法的  


## 常用公共函数：QDateTime转字符串
1. QString toString(const QString &format) 

2. QString QDateTime::toString(QStringView format) const

3. QString QDateTime::toString(QStringView format, QCalendar cal) const

4. QString QDateTime::toString(const QString &format, QCalendar cal) const

5. QString QDateTime::toString(Qt::DateFormat format = Qt::TextDate) const


## 常用公共函数：时区相关的函数
1. void QDateTime::setTimeSpec(Qt::TimeSpec spec)

2. void QDateTime::setTimeZone(const QTimeZone &toZone)

3. Qt::TimeSpec QDateTime::timeSpec() const

4. QTimeZone QDateTime::timeZone() const

5. QString QDateTime::timeZoneAbbreviation() const

6. QDateTime QDateTime::toLocalTime() const

7. QDateTime QDateTime::toOffsetFromUtc(int offsetSeconds) const

8. QDateTime QDateTime::toUTC() const

9. QDateTime QDateTime::toTimeSpec(Qt::TimeSpec spec) const

10. QDateTime QDateTime::toTimeZone(const QTimeZone &timeZone) const


## 静态公共函数
1. [static] QDate QDate::currentDate()
获取当前时间日期，返回一个QDateTime对象  

2. [static] QDateTime QDateTime::currentDateTimeUtc()

3. [static] QDate QDate::fromString(const QString &string, Qt::DateFormat format = Qt::TextDate)
把时间日期的字符串按照一定格式转化为一个QDate对象  

4. [static] QDateTime QDateTime::fromString(const QString &string, const QString &format, QCalendar cal)
把时间日期的字符串按照一定格式转化为一个QDateTime对象  


## 静态公共函数：QDateTime对象与时间戳偏移量之间的相互转换
1. [static] qint64 QDateTime::currentMSecsSinceEpoch()
以毫秒为单位返回时间戳到当前时间的偏移量  

2. [static] qint64 QDateTime::currentSecsSinceEpoch()
以秒为单位返回时间戳到当前时间的偏移量  

3. [static] QDateTime QDateTime::fromMSecsSinceEpoch(qint64 msecs)
以毫秒为单位的时间戳偏移量转换为QDateTime对象  

4. [static] QDateTime QDateTime::fromMSecsSinceEpoch(qint64 msecs, Qt::TimeSpec spec, int offsetSeconds = 0)
以毫秒为单位的时间戳偏移量转换为QDateTime对象  

5. [static] QDateTime QDateTime::fromMSecsSinceEpoch(qint64 msecs, const QTimeZone &timeZone)
以毫秒为单位的时间戳偏移量转换为QDateTime对象  

6. [static] QDateTime QDateTime::fromSecsSinceEpoch(qint64 secs, Qt::TimeSpec spec = Qt::LocalTime, int offsetSeconds = 0)
以秒为单位的时间戳偏移量转换为QDateTime对象  

7. [static] QDateTime QDateTime::fromSecsSinceEpoch(qint64 secs, const QTimeZone &timeZone)
以秒为单位的时间戳偏移量转换为QDateTime对象  


## 日期时间格式format
```
字符		意义
d		天，不补零显示，1-31
dd		天，补零显示，01-31
M		月，不补零显示，1-12
MM		月，补零显示，01-12
yy		年，两位显示，00-99
yyyy	年，4位数字显示，如 2016
h		小时，不补零，0-23 或 1-12 (如果显示 AM/PM)
hh		小时，补零2位显示，00-23 或 01-12 (如果显示 AM/PM)
H		小时，不补零，0-23 (即使显示 AM/PM)
HH		小时，补零显示，00-23 (即使显示 AM/PM)
m		分钟，不补零，0-59
mm		分钟，补零显示，00-59
s 		秒，不补零，0-59
ss 		秒，补零，00-59
z		毫秒，不补零，0-999
zzz		毫秒，补零 3 位显示，000-999
AP或A	使用 AM/pm 显示
ap或a	使用 am/pm 显示
```