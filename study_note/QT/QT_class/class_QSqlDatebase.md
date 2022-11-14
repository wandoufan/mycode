# QSqlDatabase

## 基本功能
QSqlDatabase类用于建立与数据库的连接  
对于sql server数据库，连接之前要先在ODBC进行相应的配置  
对于单机型数据库，如sqlite，只需要设置数据库文件即可  
使用时需要在.pro文件中加入：  
```
QT += sql
```
父类：无  
子类：无  


## 关于connectionName属性的说明
connectionName是与数据库的连接的名字，不是连接的数据库的名字，没有规范，可以任意起名  
QSqlDatabase中没有setConnectionName()函数，只有使用静态公共函数创建连接时可以设置该属性值  
数据库的连接可以同时有多个，connectionName就相当于区分各个连接的id  
connectionName属性不一定要设置，但如果设置了就不能有重名，否则已有的同名连接会被从list中删除掉  


## 关于数据库连接个数的说明
有一个列表list用来管理数据库的连接，每次新建一个连接会自动把新连接添加到列表中  
数据库的连接可以同时有多个，每个连接的connectionName不能有重复  
数据库连接可以不设置connectionName，这样就是默认的数据库连接  
```
QSqlDatabase mydb1 = QSqlDatabase::addDatabase("QODBC", "firstConnection");
QSqlDatabase mydb2 = QSqlDatabase::addDatabase("QODBC", "secondConnection");
QSqlDatabase mydb3 = QSqlDatabase::addDatabase("QODBC", "thirdConnection");
QSqlDatabase defaultdb = QSqlDatabase::addDatabase("QODBC");//default connection
```


## 报错：数据库驱动没有加载
执行下面的代码时
```
postgre = QSqlDatabase::addDatabase("QPSQL");
```
遇到报错
```
QSqlDatabase: QPSQL driver not loaded
QSqlDatabase: available drivers: QSQLITE QMYSQL QMYSQL3 QODBC QODBC3 QPSQL QPSQL7
```
代码本身是正常没有错误的，解决方法：
1. 临时解决方法
原来使用的MSVC 2015 64位编译器，更换为MSVC 2015 32位或MinGW 32位编译器之后报错解决
2. 网上方法一
添加PostgreSQL的路径到系统环境变量中，实际测试，这个方法没有作用
```
C:\Program Files (x86)\PostgreSQL\9.3\bin
C:\Program Files (x86)\PostgreSQL\9.3\lib
```
3. 网上方法二
从PostgreSQL安装路径中复制libpq.dll文件到下面目录中，实际测试，这个方法没有作用
```
C:\Program Files (x86)\PostgreSQL\9.3\lib
```
4. 网上方法三
有可能安装的postgresql-9.3.4-1-windows.exe本身是32位的，而使用的Qt5.11是64位的，二者无法兼容
有可能是这个原因，但是没有去验证


## 代码示例：连接sqlite数据库
使用sqlite数据库无需配置账户密码等，只需要指明数据库文件  
注意：数据库文件要写出完整的路径  
```
QSqlDatabase mydb = QSqlDatabase::addDatabase("QSQLITE", "myconnection1");
mydb.setDatabaseName(QString::fromLocal8Bit("E:\\xingyifan\\project\\db_file\\card_reader.db"));
if(mydb.open())
......
```


## 代码示例：连接PostgreSQL
```
QSqlDatabase postgre = QSqlDatabase::addDatabase("QPSQL", "first connection");
postgre.setHostName("localhost");
postgre.setPort(5432);
postgre.setDatabaseName("Test");
postgre.setUserName("postgres");
postgre.setPassword("123456");
if(postgre.open())
...
```


## 建立连接函数中的type参数
不同数据库在QT中使用不同的驱动类型，具体对应关系如下
```
Driver Type			Description
QDB2				IBM DB2
QIBASE				Borland InterBase Driver
QMYSQL				MySQL Driver
QOCI				Oracle Call Interface Driver
QODBC				ODBC Driver (includes Microsoft SQL Server)
QPSQL				PostgreSQL Driver
QSQLITE				SQLite version 3 or above
QSQLITE2			SQLite version 2
QTDS				Sybase Adaptive Server
```


## 构造函数
备注：一般都使用静态公共函数直接建立连接，不需要构造出QSqlDatabase对象
1. QSqlDatabase::QSqlDatabase(const QSqlDatabase &other)

2. QSqlDatabase::QSqlDatabase()


## 常用公共函数：查询连接属性
1. QString QSqlDatabase::connectOptions() const

2. QString QSqlDatabase::connectionName() const

3. QString QSqlDatabase::databaseName() const

4. QSqlDriver \*QSqlDatabase::driver() const

5. QString QSqlDatabase::driverName() const

6. int QSqlDatabase::port() const

7. QString QSqlDatabase::password() const

8. QString QSqlDatabase::userName() const


## 常用公共函数：查询连接状态
1. bool QSqlDatabase::isOpen() const

2. bool QSqlDatabase::isOpenError() const

3. bool QSqlDatabase::isValid() const
判断QSqlDatabase对象中是否具有合法的驱动  

4. QSqlError QSqlDatabase::lastError() const
返回数据库连接或执行过程中的报错，返回类型为QSqlError  
```
qDebug() << mydb.lastError().text();
```


## 常用公共函数：设置连接信息
备注：这些属性必须要在打开连接之前就设置好，否则无法生效  
1. void QSqlDatabase::setHostName(const QString &host)
setHostName函数用来设置要建立连接的主机名，该函数没有默认参数  
```
mydb.setHostName("localhost"); //表示本地主机 127.0.0.1
```

2. void QSqlDatabase::setPort(int port)
设置连接端口  
```
mydb.setPort(1433); //sql server默认端口为1433
```

3. void QSqlDatabase::setDatabaseName(const QString &name)
设置要连接的数据库的名称，这里的名称要ODBC中的设置保持一致  
```
mydb.setDatabaseName(QString::fromLocal8Bit("UserInfo_Test"));//连接的数据库名称
```

4. void QSqlDatabase::setUserName(const QString &name)
设置数据库账户名  
```
mydb.setUserName("sa");
```

5. void QSqlDatabase::setPassword(const QString &password)
设置数据库密码  
```
mydb.setPassword("123456");
```

6. void QSqlDatabase::setConnectOptions(const QString &options = QString())
设置连接选项，对于不同类型的数据库具有不同的连接选项  
options参数取值详见帮助手册  


## 常用公共函数：建立/断开连接
1. bool QSqlDatabase::open()
连接数据库，并返回是否连接成功  
```
if(mydb.open())
{...}
```

2. bool QSqlDatabase::open(const QString &user, const QString &password)
重载函数  

3. void QSqlDatabase::close()
关闭数据库连接，释放资源，所有与此相关的QSqlQuery对象都会失效  


## 常用公共函数：执行sql指令
备注：虽然有接口函数，但一般不在这里执行sql指令，而是在QSqlQuery中写sql语句
1. QSqlQuery QSqlDatabase::exec(const QString &query = QString()) const

2. QSqlRecord QSqlDatabase::record(const QString &tablename) const


## 常用公共函数：transaction
备注：通过调用QSqlDriver::hasFeature(QSqlDriver::Transactions)函数可以判断数据库是否支持transaction
1. bool QSqlDatabase::commit()
向数据库提交了一个transaction(如果驱动支持transaction)，然后调用QSqlDatabase::transaction()函数

2. bool QSqlDatabase::transaction()
开始在数据库上执行transaction(如果驱动支持transaction)，返回是否执行成功


## 静态公共函数
1. [static] QSqlDatabase QSqlDatabase addDatabase(const QString &type, const QString &connectionName = QLatin1String(defaultConnection))
新建一个数据库连接，添加到数据连接列表中，并返回该连接对象  
type参数取值详见上面对应表  
connectionName参数详见上面的详细说明  

2. [static] QSqlDatabase QSqlDatabase::addDatabase(QSqlDriver \*driver, const QString &connectionName = QLatin1String(defaultConnection))

3. [static] QSqlDatabase QSqlDatabase::cloneDatabase(const QSqlDatabase &other, const QString &connectionName)

4. [static] QSqlDatabase QSqlDatabase::cloneDatabase(const QString &other, const QString &connectionName)

5. [static] bool QSqlDatabase::contains(const QString &connectionName = QLatin1String(defaultConnection))

6. [static] QSqlDatabase QSqlDatabase::database(const QString &connectionName = QLatin1String(defaultConnection), bool open = true)

7. [static] QStringList QSqlDatabase::drivers()
输出支持的所有数据库驱动  

