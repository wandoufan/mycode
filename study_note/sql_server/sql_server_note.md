# sql server笔记

## 基本情况
sql server是微软开发的产品，属于中小型数据库，采用C/S架构  
常见版本为sql server 2008R2
1. 优点
在多用户时具有较好的性能表现  
在windows平台下与相关软件集成度高  
2. 缺点
sql server只能在windows平台上运行  
3. 默认信息
sql server默认用户名是sa，密码是安装的时候设置的密码  
默认端口号为1433  
SQL Server服务使用两个端口：TCP-1433、UDP-1434  
其中1433用于供SQL Server对外提供服务，1434用于向请求者返回SQL Server使用了哪个TCP/IP端口  


## sql server和mysql的对比
使用的sql语句语法基本都一致，但有的内置函数并不一样  
例如获取时间、处理字符串、获取uuid等函数  


## sql语句的不同
1. 修改字段属性
```
mysql语法：
alter table tb_name modify column_name create_definition;
alter table teacher_info modify user_name varchar(30);
sqlserver语法：
alter table [表名] alter column [列名] [列属性]
alter table user_info alter column user_id char(30);
```


