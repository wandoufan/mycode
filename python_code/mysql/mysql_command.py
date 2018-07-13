# 主要记录mysql的一些命令：
# 注意：在命令中要尽量加入'if exists'和'if not exists'来减少报错


# 数据库操作命令：
# 'show databases;' 查看当前数据库
# 'show databases like 'db_%'' 查看以db开头的数据库
# 'create {database|schema} db_name;' 创建一个新的数据库，db_name为数据库名
# 'create database db_name character set=GBK;' 创建数据库并设置其字符集为GBK
# 'create database if not exists db_name' 创建前检查数据库不存在时才进行创建 
# 'use db_name;' 选择一个数据库成功当前工作数据库
# 'alter database db_name default default character set gbk' 修改数据库的字符集
# 'drop {database|schema} [if exists] db_name;' 删除数据库


# 数据表操作命令:
# 'show tables' 查看当前数据库中的所有数据表
# 'create table student (id int auto_increment primary key);' 创建student数据表
# 'show columns from table_name.db_name;' 查看指定数据库中的指定数据表
# 'show columns from table_name;' 查看当前数据库中的student数据表
# '{describe|desc} table_name;' 查看当前数据库中是数据表
# '{describe|desc} table_name column_name;' 查看数据表中具体某一列
# 'alter table student add name varchar(50) not null;' 向数据表中添加新字段
# 'alter table student modify name varchar(40);' 修改数据表中的字段定义
# 'alter table student change column born borntime;' 修改数据表中的字段名
# 'alter table student change drop borntime;' 删除数据表中的字段
# 'alter table student rename as xuesheng;' 修改数据表的名字
# 'rename table student to xuesheng;' 对数据表重命名，可以一次修改多个表的名字，逗号隔开
# 'create table xuesheng like student;' 对student数据表进行复制(仅复制表结构)
# 'create table xuesheng as select * form student;' 复制数据表的结构和内容
# 'drop table xuesheng;' 删除数据表


# 数据表操作命令中相关参数的含义：
# auto_increment，实现自动编号，即使没有写入值也会自动填上相应的编号，常用于id等字段
# primary key, 设置该字段为主键
# default default_value, 设置字段的默认值
# null | not null, 设置字段是否允许为空，一般不指定则默认允许为空


# 第七章SQL中的运算符及流程控制语句：
# ???


# 表中数据的增删改命令：
# 'insert into student values(001,'张三','1999-01-01','一班');' 向数据表中插入完整数据
# 'insert into student (id,name,class) values(003,'王五','三班');' 向数据表中插入部分字段
# 'insert into student (id,name,class) values(004,'刘六','四班'),(005,'赵七','一班');' 一次插入多条数据
# 'insert into student set id=006,name='周八',class='二班';' set指定值来插入数据
# 'insert into student (id,name,class) select id,name,class from xuesheng;' 将查询结果插入数据表
# 'update xuesheng set id=007 where id=001;' 修改数据表中的字段值
# 'delete from xuesheng where id=007;' 删除数据表中指定的字段值
# 'truncate table xuesheng;' 删除整个数据表中的字段值


# 表中数据的查询命令：
# 'select * from student;' 查看数据表中所有的字段值
# 'select name,class from student;' 查看数据表中一个或多个字段
# ？？？


# SQL中的常用函数：
# ？？？