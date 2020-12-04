# QT中使用数据库

## 基本情况
Qt支持的数据库包括：mysql、oracle、sql server、sqlite等  
QT通过Qt SQL模块来实现对数据库的各种操作  
Qt SQL模块包括多个类，可以实现数据库连接、SQL语句执行、数据获取与界面显示功能  
数据与界面之间采用Model/View架构，可以方便的实现数据显示与操作  


## Qt SQL模块
要在项目中使用Qt SQL模块，需要先在.pro文件中加入'QT += sql'  
在头文件或源文件中使用模块中的类时，要声明'#include<类名>'  
也可以直接用'#include<Qtsql>'把模块中所有类都包含进去，但会造成冗余  


## Qt SQL模块中常用类
1. QSqlDatebase
用于建立与数据库的连接  
2. QSqlDriver
用于访问具体的SQL数据库的底层抽象类  
3. QSqlDriverCreator
为某个具体的数据库驱动提供SQL驱动的模板类  
4. QSqlDriverCreatorBase
所有SQL驱动器的基类  
5. QSqlDriverPlugin
用于定制QSqlDriver插件的抽象基类  
6. QSqlError
SQL数据库错误信息，可以用于访问上一次出错的信息  
7. QSqlField
操作数据表或视图的字段的类  
8. QSqlIndex
操作数据库的索引的类  
9. QSqlQuery
执行各种sql语句的类  
10. QSqlQueryModel
sql查询结果数据的只读数据模型，用于select查询结果的只读显示  
