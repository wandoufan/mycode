# QDatetime

## 基本功能
QDatetime类提供日期和时间相关的函数，使用前要'#include <QDateTime>'  
另外，还有QDate类提供日期相关的功能，QTime类提供时间相关的功能  
```
字符		意义
d	天，不补零显示，1-31
dd	天，补零显示，01-31
M	月，不补零显示，1-12
MM	月，补零显示，01-12
yy	年，两位显示，00-99
yyyy	年，4位数字显示，如 2016
h	小时，不补零，0-23 或 1-12 (如果显示 AM/PM)
hh	小时，补零2位显示，00-23 或 01-12 (如果显示 AM/PM)
H	小时，不补零，0-23 (即使显示 AM/PM)
HH	小时，补零显示，00-23 (即使显示 AM/PM)
m	分钟，不补零，0-59
mm	分钟，补零显示，00-59
z	毫秒，不补零，0-999
zzz	毫秒，补零 3 位显示，000-999
AP或A	使用 AM/pm 显示
ap或a	使用 am/pm 显示
```


## 常用公共函数
1. QString toString(const QString &format) 
按照一定格式转化成字符串，返回字符串对象  
```
QDateTime current_datetime = QDateTime::currentDateTime();
ui -> Edit_time -> setText(current_datetime.toString("yyyy:MM:dd:hh:mm:ss"));
```


## 静态公共函数
1. [static] QDate QDate::currentDate()
获取当前时间日期，返回一个QDateTime对象  
```
QDateTime current_datetime = QDateTime::currentDateTime();
ui -> timeEdit -> setTime(current_datetime.time());
```

2. [static] QDate QDate::fromString(const QString &string, Qt::DateFormat format = Qt::TextDate)
把时间日期的字符串按照一定格式转化为一个QDateTime对象  
```
QDateTime user_time = QDateTime::fromString(str, "hh:mm:ss");
ui -> timeEdit -> setTime(user_time.time());
```