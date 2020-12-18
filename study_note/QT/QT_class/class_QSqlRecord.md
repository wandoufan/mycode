# QSqlRecord

## 基本功能
QSqlRecord返回包含有查询数据结果的数据库记录  


## 常用函数
1. QSqlRecord(const QSqlRecord &other)
QSqlRecord是构造函数，返回一个QSqlRecord对象  
```
myquery是一个执行查询命令后的QSqlQuery对象
QSqlRecord myrecord = myquery.record();
```
2. int indexOf(const QString &name) const
返回记录中指定字段的索引位置，如果查询的字段不存在，则返回-1  
字段名称不区分大小写，如果有多个字段匹配，则返回第一个字段的索引  
```
int index = myrecord.indexOf("user_name");
```
字段的索引位置是根据sql查询语句中的顺序而来的  
例如，'select user_id, user_name from user_info;'  
则user_id的索引位置为0，user_name的索引位置为1  
注意：不推荐使用'select * '，因为这样返回的字段索引位置是不明确的  
3. QVariant value(int index) const
QVariant value(const QString &name) const
