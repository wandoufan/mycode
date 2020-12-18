# QSqlError

## 基本功能
sql产生报错时返回的类型  

## 常用函数
1. QString databaseText() const
返回由数据库产生的报错内容，可能包含具体描述，也可能是空字符串
2. QString driverText() const
返回由驱动(如ODBC)产生的报错内容，可能包含具体描述，也可能是空字符串
3. QString text() const
把databaseText()和driverText()的内容合并起来返回  
可能包含具体描述，也可能是空字符串  
```
qDebug() << mydb.lastError().text();
```