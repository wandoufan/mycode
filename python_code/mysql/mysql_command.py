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
# 创建一个新的数据库，其中db_name为数据库名
# 'create {database|schema} [if not exists] db_name;' 
# 创建数据库并设置其字符集为GBK
# 'create database db_name character set=GBK;' 

# 2.2 删除
# 删除数据库
# 'drop {database|schema} [if exists] db_name;' 

# 2.3 修改
# 修改数据库的字符集
# 'alter database db_name default default character set gbk' 
# 备注：没有命令可以直接修改数据库名字，数据库改名需要通过复杂的操作才能实现

# 2.4 查看
# 查看当前数据库
# 'show databases;' 
# 查看以db开头的数据库
# "show databases like 'db_%';" 

# 2.5 选择
# 选择一个数据库作为当前的工作数据库(对数据表的所有操作都要选中指定数据库)
# 'use db_name;' 


# 3.数据表及字段操作命令:
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
# primary key 设置该列为数据表的主键，一个数据表只能有一个列为主键，主键的值要求唯一不能重复
# reference_definition 为该字段添加注释
# 示例：创建一个学生表，其中id列为非空自动编号的主键
# 'create table student_info(id int not null auto_increment primary key);' 
# 示例：创建一个教师表，包括id和name两个字段
# 'create table teacher_info(id int not null auto_increment primary key,name char not null);'
# 向数据表中添加新字段，其中create_definition部分描述字段属性
# 'alter table tb_name add create_definition;' 
# 示例：向学生表中添加name和age两个字段
# 'alter table student_info add name char not null, add age int;'
# 备注：alter table语句可以一次执行多个动作，每个动作之间用逗号隔开
# 示例：向学生表中添加sex字段，只支持'boy', 'girl'两个值
# 'alter table student_info add sex enum('boy', 'girl');'

# 3.2 删除
# 删除数据表
# 'drop table [if exists] tb_name;' 
# 删除数据表中的字段
# 'alter table tb_name drop column_name;' 

# 3.3 修改
# 修改数据表中的字段属性
# 'alter table tb_name modify column_name create_definition;' 
# 示例：把教师表中name字段改为varchar属性
# 'alter table teacher_info modify name varchar(30);'
# 修改数据表中的字段名
# 'alter table tb_name change column_name column_name2 create_definition;' 
# 示例：把教师表中的age字段改名为borntime
# 注意：字段改名时需要指定新字段的类型
# 'alter table teacher_info change age borntime char;'
# 修改数据表的名字
# 'alter table tb_name rename as tb_name2;' 
# 修改数据表的名字
# 'rename table tb_name to tb_name2;'

# 3.4 查看
# 查看当前数据库中的所有数据表
# 'show tables' 
# 查看指定数据表的所有字段及字段属性
# 'show columns from table_name;' 
# 查看指定数据库中指定数据表的所有字段及字段属性
# 'show columns from db_name.table_name;' 
# 查看指定数据表的所有字段及字段属性
# '{describe|desc} table_name;' 
# 查看数据表中具体某一个字段
# '{describe|desc} table_name column_name;' 

# 3.5 复制
# 对tb_name数据表进行复制(仅复制表结构)
# 'create table tb_name2 like tb_name;'
# 复制数据表的结构和数据
# 'create table tb_name2 as select * form tb_name;' 


# 4.数据表中数据的操作命令：
# 4.1 增加
# 向数据表中插入数据
# 'insert [into] tb_name[(column_name,...)] values(cloumn_value,...)'
# 示例：向学生表中插入一条完整数据(字符型的字段要用引号)
# 'insert student_info values(002, 'b', 10, 'girl');'
# 示例：向学生表中插入一条只包含部分字段的数据
# 备注：对于已经设置为自动编号的id字段，即使没有指定值，mysql也会自动填上相应的值
# 'insert student_info(name, age, sex) values('f', 10, 'boy');'
# 示例：向学生表中一次插入多条数据
# 'insert student_info(name, age, sex) values('g', 10, 'girl'), ('h', 10, 'girl'), ('i', 10, 'girl');'
# 向数据表中插入数据
# 'insert [into] tb_name set column_name=column_value,...;'
# 备注：insert set语句插入数据时，对于未给出值的字段将被设置为默认值
# 示例：向学生表中插入一条数据
# 'insert student_info set name='j', age=10, sex='boy';'
# 向数据表中插入查询结果
# 'insert [into] table_name[(column_name,...)] select column_name,... from tb_name2;'
# 备注：insert select语句可以将数据表的查询结果插入数据表中
# 示例：把学生表的查询结果都插入教师表中
# 'insert into teacher_info select * from student_info;'

# 4.2 删除
# 删除数据表中的字段值
# 'delete from tb_name [where 条件表达式] [limit 删除前n行]'
# 示例：把教师表中名字等于c的数据删除
# 'delete from teacher_info where name='c';'
# 示例：把教师表中前5行的数据删除
# 'delete teacher_info limit 5;'
# 删除数据表中所有的数据(相当于清空操作)
# 'truncate [table] tb_name;'

# 4.3 修改
# 修改数据表中的字段值
# 'update tb_name set column_name=column_value,... [where 条件表达式] [limit 修改前n行]'
# 示例：把教师表的age字段值都改为30
# 'update teacher_info set age=30;'
# 示例：把教师表的id=7的行sex字段值改为boy
# 'update teacher_info set sex='boy' where id=7;'
# 示例：把教师表的前5行的sex字段值改为boy
# 'update teacher_info set sex='boy' limit 5;'

# 4.4 查看
# 查看数据表中所有的字段的值
# 'select * from tb_name;'
# 查看数据表中指定字段的值
# 'select column_name,... from tb_name;'
# 示例：从学生表中查询id和age字段
# 'select id, age from student_info;'


# 5.mysql的三种数据类型：
# 5.1.数字类型,包括整型和浮点型,最常用的包括：int,float,double

# 5.2.字符串类型，包括：
# a.普通的文本字符串类型(固定长度0~255的char型和变长的varchar型)
# 如果需要快速的性能，选择char型
# 如果需要节省空间，选择varchar型
# b.可选类型(存储长文本的text型和存储声音图像等二进制数据的blob型)
# 如果搜索的内容不区分大小写，可以使用text型
# 如果搜索的内容区分大小写，可以blob型
# c.特殊类型(set型和enum型)
# enum('value1','value2',.....)只允许选择一个值或者为Null，如性别字段
# set('value1','value2',.....)允许选多个值或者为Null，如兴趣字段

# 5.3.时间日期类型，包括：
# date,格式为2018-07-09
# time,格式为08:10:30
# datetime,格式为2018-07-09 08:10:30
# year,格式为2018或18
# timestamp,时间标签


# 6.mysql的查询语句

# ----------------------------------------------------------------------

# 第七章SQL中的运算符及流程控制语句：
# ???

# SQL中的常用函数：
# ？？

# mysql导出数据：

# mysql导入数据：
