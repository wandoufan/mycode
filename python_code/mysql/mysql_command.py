# 主要记录mysql的一些命令：
# 参考资料：http://www.runoob.com/mysql/mysql-install.html
# 注意：在命令中要尽量加入'if exists'和'if not exists'来减少报错
# 注意：命令中的{}部分表示任选其一，[]部分表示可选可不选
# 注意：所有的数据库名，表名，表字段都是区分大小写的


# 1.Linux环境下mysql的使用：
# 'systemctl start mysqld' 启动mysql服务
# './mysqld_safe &' 启动mysql服务
# 'systemctl status mysqld' 查看mysql运行状态
# 'ps -ef | grep mysqld' 查看是否有mysql服务
# 'mysqladmin --version' 查看mysql版本
# 'mysqladmin -u root password 000000' 设置root用户的密码为000000
# 'mysql -u root -p' 使用root账户登录到mysql命令窗口
# 'exit' 从mysql命令窗口退出
# 如果需要给mysql添加新用户，要在系统自带的mysql库的user表中添加新用户


# 2.数据库操作命令：
# 2.1 增加
# 'create {database|schema} [if not exists] db_name;' 创建一个新的数据库，其中db_name为数据库名
# 'create database db_name character set=GBK;' 创建数据库并设置其字符集为GBK

# 2.2 删除
# 'drop {database|schema} [if exists] db_name;' 删除数据库

# 2.3 修改
# 'alter database db_name default default character set gbk' 修改数据库的字符集
# 备注：没有命令可以直接修改数据库名字，数据库改名需要通过复杂的操作才能实现

# 2.4 查看
# 'show databases;' 查看当前数据库
# "show databases like 'db_%';" 查看以db开头的数据库

# 2.5 选择
# 'use db_name;' 选择一个数据库作为当前的工作数据库(对数据表的所有操作都要选中指定数据库)


# 3.数据表操作命令:
# 3.1 增加
# 创建新的数据表，其中tb_name为数据表名
# 'create [temporary] table [if not exists] tb_name {(create_definition),...} [table_options] [select_statement]' 
# temporary 表示创建一个临时表
# table_options 设置表的一些特性参数，一般不用写
# select_statement 是select语句的描述部分，用它可以快速创建表
# create_definition 是数据表中列的属性，创建新的数据表时表中至少要包含一列，具体如下：
# 'col_name type [not null | null] [default_value] [auto_increment] [primary key] [reference_definition]'
# col_name 列名或字段名(column name)
# type 字段数据类型，具体参考mysql支持的三种数据类型
# not null | null 设置该列数据是否允许为空，默认允许为空值
# default_value 设置该列数据的默认值
# auto_increment 设置自动编号，一般用于id等字段，一个数据表只能有一个自动编号的列
# primary key 设置该列为数据表的主键，一个数据表只能有一个列为主键
# reference_definition 为该字段添加注释
# 示例：创建一个学生表，其中id列为非空自动编号的主键
# 'create table student_info(id int not null auto_increment primary key);' 

# 3.2 删除
# 'drop table tb_name2;' 删除数据表
# 'alter table tb_name change drop borntime;' 删除数据表中的字段

# 3.3 修改
# 'alter table tb_name modify name varchar(40);' 修改数据表中的字段定义
# 'alter table tb_name change column born borntime;' 修改数据表中的字段名
# 'alter table tb_name rename as tb_name2;' 修改数据表的名字
# 'rename table tb_name to tb_name2;' 对数据表重命名，可以一次修改多个表的名字，逗号隔开

# 3.4 查看
# 'show tables' 查看当前数据库中的所有数据表
# 'show columns from db_name.table_name;' 查看指定数据库中的指定数据表的所有列
# 'show columns from table_name;' 查看指定数据表的所有列
# '{describe|desc} table_name;' 查看当前数据库中是数据表
# '{describe|desc} table_name column_name;' 查看数据表中具体某一列
# 'alter table tb_name add name varchar(50) not null;' 向数据表中添加新字段

# 3.5 复制
# 'create table tb_name2 like tb_name;' 对tb_name数据表进行复制(仅复制表结构)
# 'create table tb_name2 as select * form tb_name;' 复制数据表的结构和内容


# 4.数据表中数据的操作命令：
# 4.1 增加

# 4.2 删除

# 4.3 修改

# 4.4 查看





# ----------------------------------------------------------------------

# 第七章SQL中的运算符及流程控制语句：
# ???


# 表中数据的增删改命令：
# 'insert into tb_name values(001,'张三','1999-01-01','一班');' 向数据表中插入完整数据
# 'insert into tb_name (id,name,class) values(003,'王五','三班');' 向数据表中插入部分字段
# 'insert into tb_name (id,name,class) values(004,'刘六','四班'),(005,'赵七','一班');' 一次插入多条数据
# 'insert into tb_name set id=006,name='周八',class='二班';' set指定值来插入数据
# 'insert into tb_name (id,name,class) select id,name,class from tb_name2;' 将查询结果插入数据表
# 'update tb_name2 set id=007 where id=001;' 修改数据表中的字段值
# 'delete from tb_name2 where id=007;' 删除数据表中指定的字段值
# 'truncate table tb_name2;' 删除整个数据表中的字段值


# 表中数据的查询命令：
# 'select * from tb_name;' 查看数据表中所有的字段值
# 'select name,class from tb_name;' 查看数据表中一个或多个字段
# ？？？


# SQL中的常用函数：
# ？？