# QSqlDatabase

## 基本功能
QSqlDatabase类用于建立与数据库的连接，#include <QSqlDatabase>  
连接之前要先在ODBC进行相应的配置  
不同数据库在QT中使用不同的驱动类型，具体对应关系如下：  
```
Driver Type - Description
QDB2 - IBM DB2
QIBASE - Borland InterBase Driver
QMYSQL - MySQL Driver
QOCI - Oracle Call Interface Driver
QODBC - ODBC Driver (includes Microsoft SQL Server)
QPSQL - PostgreSQL Driver
QSQLITE - SQLite version 3 or above
QSQLITE2 - SQLite version 2
QTDS - Sybase Adaptive Server
```


## 常用函数
1. [static] QSqlDatabase QSqlDatabase addDatabase(const QString &type, const QString &connectionName = QLatin1String(defaultConnection))
addDatabase函数用来创建出一个数据库对象，具体参数详见上面对应表  
一次只能建立一个连接，新连接建立时旧连接会被自动删去  
备注：这是一个公共静态成员方法，可以不需要实例化就直接使用  
```
QSqlDatabase mydb = QSqlDatabase::addDatabase("QODBC");
```
2. void setHostName(const QString &host)
setHostName函数用来设置要建立连接的主机名，该函数没有默认参数  
```
mydb.setHostName("localhost"); //表示本地主机 127.0.0.1
```
3. void setPort(int port)
设置连接端口
```
mydb.setPort(1433); //sql server默认端口为1433
```
4. void setDatabaseName(const QString &name)
设置要连接的数据库的名称，这里的名称要ODBC中的设置保持一致
```
mydb.setDatabaseName(QString::fromLocal8Bit("UserInfo_Test"));//连接的数据库名称
```
5. void setUserName(const QString &name)
设置数据库账户名
```
mydb.setUserName("sa");
```
6. void setPassword(const QString &password)
设置数据库密码
```
mydb.setPassword("123456");
```
7. bool open()
bool open(const QString &user, const QString &password)
检查数据库是否连接成功
```
if(mydb.open())
```
8. QSqlError lastError() const
返回数据库连接或执行过程中的报错，返回类型为QSqlError
```
qDebug() << mydb.lastError().text();
```
