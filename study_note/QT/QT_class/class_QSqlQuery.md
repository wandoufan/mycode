# QSqlQuery

## 基本功能
QSqlQuery用来执行各种sql语句，使用前#include <QSqlQuery>  


## 常用函数
1. QSqlQuery(const QSqlQuery &other)
QSqlQuery类的构造函数，创建一个QSqlQuery的对象  
```
QSqlQuery myquery;
```
也可以在创建对象时直接执行sql语句
```
QSqlQuery myquery("select * from user_info;");
```
2. bool exec(const QString &query)
执行sql语句，根据是否成功返回'true'或'false'  
如果执行成功，会将query的状态设置为active  
一次只能执行一条sql语句，执行完成后才能使用next()等方法  
```
result = myquery.exec("select * from user_info;");
```
3. bool next()
检索结果中的下一条记录  
调用之前query的状态必须是active的状态和select状态  
如果当前位置在第一条记录之前，则开始检索第一条记录  
如果当前位置在第一条记录之后，则不作任何操作并返回false  
如果当前位置在中间某条记录上，则开始检索下一条记录  
```
while(myquery.next())
{
    user_id = myquery.value(0).toString().trimmed();
    qDebug() << user_id;
}
```
4. bool previous()
检索结果中的前一条记录  
调用之前query的状态必须是active的状态，且isSelect()函数必须返回true  
具体规则参考next()  
5. bool first()
检索结果中的第一条记录  
调用之前query的状态必须是active的状态，且isSelect()函数必须返回true  
6. bool last()
检索结果中的最后一条记录  
调用之前query的状态必须是active的状态，且isSelect()函数必须返回true  
7. int at() const
返回当前在query中的位置  
当位置不合法时，会返回QSql::BeforeFirstRow 或 QSql::AfterLastRow  
8. bool isActive() const
检查query的状态是否为active  
active状态是指一个QSqlQuery对象已经成功执行了exec函数，但还没有完成  
通过调用finish()函数、clear()函数或删除对象，都可以把状态设置为inactive  
9. bool isSelect() const
检查query的状态是否为select  
10. QSqlRecord record() const
查询后返回一个包含了字段信息的QSqlRecord类型  
当query的状态是inactive时，会返回一个空的记录  
```
QSqlRecord myrecord = myquery.record();
int name_index = myrecord.indexOf("user_name");
```
11. QVariant value(int index) const
QVariant value(const QString &name) const
返回当前记录中指定字段的值  
当字段索引不存在、query的状态是inactive或query位于一个非法记录上时，会返回一个非法的QVariant对象  
字段的索引位置是根据sql查询语句中的顺序而来的  
例如，'select user_id, user_name from user_info;'  
则user_id的索引位置为0，user_name的索引位置为1  
注意：不推荐使用'select * '，因为这样返回的字段索引位置是不明确的  
```
while(myquery.next())
{
    user_id = myquery.value(0).toString().trimmed();
    qDebug() << user_id;
}
```
备注：这是个重载函数，参数可以写字段索引，也可以写字段名  


