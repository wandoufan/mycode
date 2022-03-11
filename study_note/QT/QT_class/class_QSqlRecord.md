# QSqlRecord

## 基本功能
QSqlRecord是包含有查询结果的数据记录  
使用时需要在.pro文件中加入：  
```
QT += sql
```
父类：无  
子类：QSqlIndex  


## 关于QSqlRecord的应用场景
QSqlRecord中存放的是对数据库进行查询后获得的结果  
对QSqlRecord中的字段以及字段的值进行修改也不会影响数据库中真正的数据  
目前发现的唯一的作用就是，通过QSqlQuery查询获取一个QSqlRecord  
然后把QSqlRecord中的数据修改为自己想要设置的，最后再用QSqlQuery把数据写回到数据库中  


## 构造函数
备注：QSqlRecord对象一般通过QSqlQuery::record()来获取
1. QSqlRecord::QSqlRecord(const QSqlRecord &other)

2. QSqlRecord::QSqlRecord()


## 常用公共函数：对数据记录中的字段进行增删改查
1. void QSqlRecord::append(const QSqlField &field)
向数据记录的最后位置添加字段  

2. void QSqlRecord::insert(int pos, const QSqlField &field)
向数据记录中的pos位置插入字段  

3. void QSqlRecord::clear()
删除数据记录中的所有字段  

4. void QSqlRecord::clearValues()
清空数据记录中所有字段的值，然后把每个字段都设置为null  

5. void QSqlRecord::remove(int pos)
删除数据记录中pos位置的字段  
如果pos超出索引范围，则不做任何操作  

6. void QSqlRecord::replace(int pos, const QSqlField &field)
对数据记录中pos位置的字段用filed进行替换  
如果pos超出索引范围，则不做任何操作  


## 常用公共函数：查询数据记录中的各种信息
1. int QSqlRecord::count() const
返回数据记录中包含的字段的个数  

2. bool QSqlRecord::contains(const QString &name) const
判断数据记录中是否包含name字段  

3. QString QSqlRecord::fieldName(int index) const

4. int indexOf(const QString &name) const
返回记录中指定字段的索引位置，如果查询的字段不存在，则返回-1  
字段名称不区分大小写，如果有多个字段匹配，则返回第一个字段的索引  
```
int index = myrecord.indexOf("user_name");
```
字段的索引位置是根据sql查询语句中的顺序而来的  
例如，'select user_id, user_name from user_info;'  
则user_id的索引位置为0，user_name的索引位置为1  
注意：不推荐使用'select * '，因为这样返回的字段索引位置是不明确的  

5. bool QSqlRecord::isEmpty() const
判断数据记录中是否包含任何字段  

6. bool QSqlRecord::isGenerated(const QString &name) const
没搞明白什么功能  

7. bool QSqlRecord::isGenerated(int index) const
没搞明白什么功能  

8. bool QSqlRecord::isNull(const QString &name) const
如果name字段为null，或者没有name字段，则返回true，否则返回false  

9. bool QSqlRecord::isNull(int index) const


## 常用公共函数：获取数据记录中的字段
1. QSqlField QSqlRecord::field(int index) const

2. QSqlField QSqlRecord::field(const QString &name) const


## 常用公共函数：获取数据记录中的字段的值
1. QVariant QSqlRecord::value(int index) const

2. QVariant QSqlRecord::value(const QString &name) const


## 常用公共函数：设置数据记录中的字段的值
1. void QSqlRecord::setNull(int index)

2. void QSqlRecord::setNull(const QString &name)

3. void QSqlRecord::setValue(int index, const QVariant &val)

4. void QSqlRecord::setValue(const QString &name, const QVariant &val)



