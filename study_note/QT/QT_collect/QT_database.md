# QT中使用数据库

## 基本情况
Qt支持的数据库包括：mysql、oracle、sql server、sqlite等  
QT通过Qt SQL模块来实现对数据库的各种操作  
Qt SQL模块包括多个类，可以实现数据库连接、SQL语句执行、数据获取与界面显示功能  
数据与界面之间采用Model/View架构，可以方便的实现数据显示与操作  
备注：QT自带了sqllite数据库，无需再进行安装  


## Qt SQL模块
注意：要在项目中使用Qt SQL模块，需要先在.pro文件中加入'QT += sql'  
在头文件或源文件中使用模块中的类时，要声明'#include<类名>'  
也可以直接用'#include<Qtsql>'把模块中所有类都包含进去，但会造成冗余  


## Qt SQL模块中常用类
1. QSqlDatabase（常用）
用于建立与数据库的连接  
2. QSqlDriver
用于访问具体的SQL数据库的底层抽象类  
3. QSqlDriverCreator
为某个具体的数据库驱动提供SQL驱动的模板类  
4. QSqlDriverCreatorBase
所有SQL驱动器的基类  
5. QSqlDriverPlugin
用于定制QSqlDriver插件的抽象基类  
6. QSqlError（常用）
SQL数据库错误信息，即sql产生报错时返回的类型  
7. QSqlField
操作数据表或视图的字段的类  
8. QSqlIndex
操作数据库的索引的类  
9. QSqlQuery（常用）
执行各种sql语句的类  
10. QSqlQueryModel
sql查询结果数据的只读数据模型，用于select查询结果的只读显示  
11. QSqlRecord（常用）
返回的包含有查询数据结果的类  
12. QSqlRelation
用于存储SQL外键信息的类  
13. QSqlResult
访问sql数据库的抽象接口  
14. QSqlTableModel
用来编辑一个单一数据表的类  
15. QDataWidgetMapper
用于界面组件与字段之间实现映射，实现字段内容的自动显示  
16. QSqlRelationTableModel
用于一个数据表的可编辑数据模型  

其中继承关系为：
```
父类 -> 子类
QAbstractTableModel -> QSqlQueryModel -> QSqlTableModel -> QSqlRelationTableModel
```


## 连接sql server步骤
> https://blog.csdn.net/xianchao0127/article/details/111084495
> https://www.cnblogs.com/JackyPeng/articles/7612037.html
1. 登录到数据库中，手动在数据库中新建一个目标数据库
2. 配置ODBC（配置方法详见参考资料）
3. 使用QSqlDatabase连接数据库，然后使用QSqlQuery执行各种sql语句


## ODBC
ODBC（Open Database Connectivity），即开放数据库连接  
它是由微软公司提供的一组对数据库访问的标准API（应用程序编程接口）  
sql server等微软公司的数据库都可以通过这个接口去进行访问  
Qt数据库驱动并不能直接连接到sql server中的数据库，而是要通过配置ODBC数据源来进行连接  
ODBC打开方式：在cmd中输入'odbcad32'或在开始中搜索ODBC  