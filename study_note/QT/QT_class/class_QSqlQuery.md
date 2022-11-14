# QSqlQuery

## 基本功能
在建立与数据库的连接之后，用QSqlQuery来执行各种sql语句  
使用时需要在.pro文件中加入：  
```
QT += sql
```
父类：无  
子类：无  


## 关于query的activate状态的说明
QSqlQuery的activate状态是指exec()执行sql指令成功了，但是还没有执行完成  
如果一个query已经执行完成，可以通过调用finish()、clear()或删除QSqlQuery对象来把状态变为inactivate  


## 关于sql语句的注意事项
备注：如果sql语句编写错误，会导致执行失败，并且返回的报错原因还可能是空字符串
备注：sql语句执行失败，都是sql语句造成的，尤其是不同数据库的sql语法还可能不一样
1. 对于Postgre SQL，插入数据时，必须要写上'into'，否则会执行失败
```
qDebug() << query.exec("insert into table1 values(123);");
```
2. SQL语句中的'VALUES'容易写成'VALUS'，在这里卡了很长时间
```
query.prepare("insert into Table1 (str1, str2) VALUES (?, ?);");
```


## 报错：数据库没有打开
1. 代码示例
```
//连接数据库
QSqlDatabase postgre = QSqlDatabase::addDatabase("QPSQL", "connection1");
postgre.setHostName("localhost");
postgre.setPort(5432);
postgre.setDatabaseName("Test");
postgre.setUserName("postgres");
postgre.setPassword("123456");
//执行sql语句
if(postgre.open())
{
    qDebug() << "数据库打开成功";
    QSqlQuery query;
    bool query_result = query.exec("SELECT * FROM Loads_All");
```
2. 报错内容
虽然数据库本身已经打开了，但执行exec()时报错：
```
QSqlQuery::exec: database not open
```
3. 报错原因
QSqlQuery对象没有指定QSqlDatabase，理论上来说，应该会使用默认的数据库连接，但实际没有，原因未知
4. 解决办法
在创建QSqlQuery对象时指定关联的数据库
```
QSqlQuery query = QSqlQuery(postgre);
```


## 构造函数
1. QSqlQuery::QSqlQuery(QSqlDatabase db)
这是最常用的QSqlQuery构建方式  
如果提供的db参数不合法，将会使用默认连接  
如果不提供任何参数，也会使用默认连接

2. QSqlQuery::QSqlQuery(const QSqlQuery &other)

3. QSqlQuery::QSqlQuery(const QString &query = QString(), QSqlDatabase db = QSqlDatabase())

4. QSqlQuery::QSqlQuery(QSqlResult \*result)


## 常用公共函数：查询状态信息
1. QString QSqlQuery::executedQuery() const
返回最新一条成功执行的sql指令  
绝大多数情况下，返回结果和QSqlQuery::lastQuery()相同  

2. QString QSqlQuery::lastQuery() const
返回正在执行的sql指令，如果当前没有sql指令，则返回空字符串  

3. const QSqlDriver \*QSqlQuery::driver() const

4. bool QSqlQuery::isActive() const
判断query的状态是否为active  

5. bool QSqlQuery::isForwardOnly() const
判断查询结果是否只能向前读取  

6. bool QSqlQuery::isNull(int field) const
在以下情况中函数返回true，否则返回false  
query为inactivate状态、query没有位于一个合法的数据记录上、没有该字段、字段为空  
备注：对于有的驱动，isNull()函数返回的信息可能不准确  

7. bool QSqlQuery::isNull(const QString &name) const
重载函数

8. bool QSqlQuery::isSelect() const
判断sql指令是否为select语句  

9. bool QSqlQuery::isValid() const
判断query当前是否位于一个合法的数据记录上  

10. QSqlError QSqlQuery::lastError() const
返回query期间发生的最新的报错  


## 常用公共函数：设置sql指令中的数据值
备注：实际测试，使用下面语法，在insert语句后面可以不加分号;，也能执行成功
1. void QSqlQuery::addBindValue(const QVariant &val, QSql::ParamType paramType = QSql::In)
向一个值列表中添加要绑定的数值  
如果想要绑定一个空值，使用一个null QVariant，例如QVariant(QVariant::String)代表一个空字符串  
示例1：向数据表中插入4组数据(1, "one")、(2, "two")、(3, "three")、(4, "")  
```
QSqlQuery q;
q.prepare("insert into myTable values (?, ?)");

QVariantList ints;
ints << 1 << 2 << 3 << 4;
q.addBindValue(ints);

QVariantList names;
names << "one" << "two" << "three" << QVariant(QVariant::String);
q.addBindValue(names);

if(q.execBatch())
{...}
```
示例2：通过字段位置来设置字段值  
```
QSqlQuery query;
query.prepare("INSERT INTO person (id, forename, surname) "
           "VALUES (?, ?, ?)");
query.addBindValue(1001);
query.addBindValue("Bart");
query.addBindValue("Simpson");
query.exec();
```

2. void QSqlQuery::bindValue(const QString &placeholder, const QVariant &val, QSql::ParamType paramType = QSql::In)
绑定sql指令中的一个字段及其对应的值  
placeholder参数为placeholder标识符: + 字段名  
示例1：通过字段名来设置字段值  
```
QSqlQuery query;
query.prepare("INSERT INTO person (id, forename, surname) "
           "VALUES (:id, :forename, :surname)");
query.bindValue(":id", 1001);
query.bindValue(":forename", "Bart");
query.bindValue(":surname", "Simpson");
query.exec();
```
示例2：通过字段位置来设置字段值  
```
QSqlQuery query;
query.prepare("INSERT INTO person (id, forename, surname) "
              "VALUES (:id, :forename, :surname)");
query.bindValue(0, 1001);
query.bindValue(1, "Bart");
query.bindValue(2, "Simpson");
query.exec();
```
示例3：通过字段位置来设置字段值  
```
QSqlQuery query;
query.prepare("INSERT INTO person (id, forename, surname) "
           "VALUES (?, ?, ?)");
query.bindValue(0, 1001);
query.bindValue(1, "Bart");
query.bindValue(2, "Simpson");
query.exec();
```

3. void QSqlQuery::bindValue(int pos, const QVariant &val, QSql::ParamType paramType = QSql::In)
重载函数  

4. QVariant QSqlQuery::boundValue(const QString &placeholder) const
返回字段绑定的数值  
placeholder参数为placeholder标识符: + 字段名  

5. QVariant QSqlQuery::boundValue(int pos) const
重载函数  

6. QMap<QString, QVariant> QSqlQuery::boundValues() const
返回字段绑定的数值  


## 常用公共函数：执行sql指令
1. bool QSqlQuery::exec(const QString &query)
执行sql语句，根据是否成功返回'true'或'false'  
如果执行成功，会将query的状态设置为active  
一次只能执行一条sql语句，执行完成后才能使用next()等方法  
```
result = myquery.exec("select * from user_info;");
```
备注：调用exec()会重置查询的last error  
注意：不管查询结果是否为空，只要sql语句执行成功，就返回ture  
注意：执行插入数据时，如果表中已经有该条数据，则执行插入失败，返回false  

2. bool QSqlQuery::prepare(const QString &query)
提前设置要执行执行的sql指令，返回是否设置成功  

3. bool QSqlQuery::exec()
执行一个以前已经准备好了的sql语句  
备注：通过QSqlQuery::prepare()来提前设置sql指令  

4. bool QSqlQuery::execBatch(QSqlQuery::BatchExecutionMode mode = ValuesAsRows)
批量执行以前已经准备好了的sql语句，返回是否执行成功  
其中，所有的绑定参数都必须是QVariantList的形式，每个QVariantList的元素个数必须相同  
如果数据库不支持batch模式，驱动将会通过调用exec()函数来模拟执行  
备注：batch是指一次操作中执行多条SQL语句，相比于一次一次执行效率会提高很多  


## 常用公共函数：获取sql指令执行结果
1. QSqlRecord QSqlQuery::record() const
获取当前查询得到的QSqlRecord对象，这个对象中包含了字段信息  
当query的状态是inactive时，会返回一个空的记录  
```
QSqlRecord myrecord = myquery.record();
int name_index = myrecord.indexOf("user_name");
```

2. QVariant QSqlQuery::value(int index) const
返回当前记录中指定字段的值  
当字段索引不存在、query的状态是inactive或query位于一个非法记录上时，会返回一个非法的QVariant对象  
字段的索引位置是根据sql查询语句中的顺序而来的  
例如，'select user_id, user_name from user_info;'，则user_id的索引位置为0，user_name的索引位置为1  
注意：不推荐使用'select * '，因为这样返回的字段索引位置是不明确的  
```
QString user_id, user_name;
while(myquery.next())
{
    user_id = myquery.value(0).toString().trimmed();
    user_name = myquery.value(1).toString().trimmed();
    qDebug() << user_id;
    qDebug() << user_name;
}
```

3. QVariant QSqlQuery::value(const QString &name) const  
重载函数，根据数据表中的字段名来获取字段值  
```
while(query.next())
{
    QString id     = query.value(QLatin1String("VariableID")).toString();
    QString name   = query.value(QLatin1String("VariableName")).toString();
}
```

4. int QSqlQuery::numRowsAffected() const
返回查询结果中的数据条数  
查询结果为空时返回0，无法获得条数时返回-1，query是inactivate状态时返回-1  
备注：如果使用的是SELECT语句，则数值是不确定的，这时使用size()函数  

5. int QSqlQuery::size() const
返回查询结果中的数据条数  
查询结果为空时返回0，无法获得条数时返回-1，query是inactivate状态时返回-1  
备注：size()函数只支持SELECT语句，如果是非SELECT语句，则返回-1  


## 常用公共函数：在执行结果中进行定位
1. bool QSqlQuery::next()
定位到执行结果中的下一条记录，返回是否执行成功  
调用next()函数之前，query必须是active的状态，而且执行的必须是SELECT语句  
如果当前位置在第一条记录之前，则开始检索第一条记录并返回true  
如果当前位置在最后一条记录之后，则不作任何操作并返回false  
如果当前位置在中间某条记录上，则开始检索下一条记录并返回true  
示例：检索所有查询结果，跳出while循环时，当前位在最后一条记录之后  
```
while(myquery.next())
{
    user_id = myquery.value(0).toString().trimmed();
    qDebug() << user_id;
}
```

2. bool QSqlQuery::nextResult()
忽略当前记录，并跳转到下一条记录上  

3. bool QSqlQuery::previous()
检索结果中的前一条记录  
调用previous()函数之前，query必须是active的状态，而且执行的必须是SELECT语句  
具体规则参考next()  

4. bool QSqlQuery::first()
检索结果中的第一条记录  
调用first()函数之前，query必须是active的状态，而且执行的必须是SELECT语句  

5. bool QSqlQuery::last()
检索结果中的最后一条记录  
调用last()函数之前，query必须是active的状态，而且执行的必须是SELECT语句  

6. int QSqlQuery::at() const
返回当前在query中的位置  
当位置不合法时，会返回QSql::BeforeFirstRow 或 QSql::AfterLastRow  


## 常用公共函数：其他
1. void QSqlQuery::clear()
清除查询结果，释放QSqlQuery对象的所有资源，把query状态设置为inactivate  
备注：一般情况下不会用到这个函数  

2. void QSqlQuery::finish()
把query状态设置为inactivate  
备注：一般情况下不会用到这个函数  

