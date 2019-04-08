# 主要记录mysql的一些命令：

* 参考资料
> http://www.runoob.com/mysql/mysql-install.html
* 注意：在命令中要尽量加入'if exists'和'if not exists'来减少报错
* 注意：命令中的{}部分表示任选其一，[]部分表示可选可不选
* 注意：所有的数据库名，表名，表字段都是区分大小写的


## 1.Linux环境下mysql的使用：
* 'systemctl start mysqld' 启动mysql服务
* './mysqld_safe &' 启动mysql服务
* 'systemctl status mysqld' 查看mysql运行状态
* 'ps -ef | grep mysqld' 查看是否有mysql服务
* 'mysqladmin --version' 查看mysql版本
* 'mysqladmin -u root password 000000' 设置root用户的密码为000000
* 'mysql -u root -p' 使用root账户登录到mysql命令窗口
* 'exit' 从mysql命令窗口退出
* 如果需要给mysql添加新用户，要在系统自带的mysql库的user表中添加新用户


## 2.数据库操作命令：
### 2.1 增加
* 创建一个新的数据库，其中db_name为数据库名
* 'create {database|schema} [if not exists] db_name;' 
* 创建数据库并设置其字符集为GBK
* 'create database db_name character set=GBK;' 

### 2.2 删除
* 删除数据库
* 'drop {database|schema} [if exists] db_name;' 

### 2.3 修改
* 修改数据库的字符集
* 'alter database db_name default character set gbk' 
* 备注：没有命令可以直接修改数据库名字，数据库改名需要通过复杂的操作才能实现

### 2.4 查看
* 查看当前数据库
* 'show databases;' 
* 查看以db开头的数据库
* "show databases like 'db_%';" 

### 2.5 选择
* 选择一个数据库作为当前的工作数据库(对数据表的所有操作都要选中指定数据库)
* 'use db_name;' 


## 3.数据表及字段操作命令:
### 3.1 增加
* 创建新的数据表，其中tb_name为数据表名
* 'create [temporary] table [if not exists] tb_name {(create_definition),...} [table_options] [select_statement]' 
* temporary 表示创建一个临时表
* table_options 设置表的一些特性参数，一般不用写
* select_statement 是select语句的描述部分，用它可以快速创建表
* create_definition 是数据表中列的属性，创建新的数据表时表中至少要包含一列，具体如下：
* 'col_name type [not null | null] [default_value] [auto_increment] [primary key] [reference_definition]'
* col_name 列名或字段名(column name)
* type 字段数据类型，具体参考mysql支持的三种数据类型
* not null | null 设置该列数据是否允许为空，默认允许为空值
* default_value 设置该列数据的默认值
* auto_increment 设置自动编号，一般用于id等字段，一个数据表只能有一个自动编号的列
* primary key 设置该列为数据表的主键，主键的值要求唯一不能重复
* 注意：一个数据表只能有一个主键，一个主键可以包含多个字段，称为复合主键，但最好一个主键只包含一个字段
* reference_definition 为该字段添加注释
* 示例：创建一个学生表，其中id列为非空自动编号的主键
* 'create table student_info(id int not null auto_increment primary key);' 
* 示例：创建一个教师表，包括id和name两个字段
* 'create table teacher_info(id int not null auto_increment primary key,name char not null);'
* 向数据表中添加新字段，其中create_definition部分描述字段属性
* 'alter table tb_name add create_definition;' 
* 示例：向学生表中添加name和age两个字段
* 'alter table student_info add name char not null, add age int;'
* 备注：alter table语句可以一次执行多个动作，每个动作之间用逗号隔开
* 示例：向学生表中添加sex字段，只支持'boy', 'girl'两个值
* 'alter table student_info add sex enum('boy', 'girl');'

### 3.2 删除
* 删除数据表
* 'drop table [if exists] tb_name;' 
* 删除数据表中的字段
* 'alter table tb_name drop column_name;' 

### 3.3 修改
* 修改数据表中的字段属性
* 'alter table tb_name modify column_name create_definition;' 
* 示例：把教师表中name字段改为varchar属性
* 'alter table teacher_info modify name varchar(30);'
* 修改数据表中的字段名
* 'alter table tb_name change column_name column_name2 create_definition;' 
* 示例：把教师表中的age字段改名为borntime
* 注意：字段改名时需要指定新字段的类型
* 'alter table teacher_info change age borntime char;'
* 修改数据表的名字
* 'alter table tb_name rename as tb_name2;' 
* 修改数据表的名字
* 'rename table tb_name to tb_name2;'

### 3.4 查看
* 查看当前数据库中的所有数据表
* 'show tables' 
* 查看指定数据表的所有字段及字段属性
* 'show columns from table_name;' 
* 查看指定数据库中指定数据表的所有字段及字段属性
* 'show columns from db_name.table_name;' 
* 查看指定数据表的所有字段及字段属性
* '{describe|desc} table_name;' 
* 查看数据表中具体某一个字段
* '{describe|desc} table_name column_name;' 

### 3.5 复制
* 对tb_name数据表进行复制(仅复制表结构)
* 'create table tb_name2 like tb_name;'
* 复制数据表的结构和数据
* 'create table tb_name2 as select * form tb_name;' 


## 4.数据表中数据的操作命令：
### 4.1 增加
* 向数据表中插入数据
* 'insert [into] tb_name[(column_name,...)] values(cloumn_value,...)'
* 示例：向学生表中插入一条完整数据(字符型的字段要用引号)
* 'insert student_info values(002, 'b', 10, 'girl');'
* 示例：向学生表中插入一条只包含部分字段的数据
* 备注：对于已经设置为自动编号的id字段，即使没有指定值，mysql也会自动填上相应的值
* 'insert student_info(name, age, sex) values('f', 10, 'boy');'
* 示例：向学生表中一次插入多条数据
* 'insert student_info(name, age, sex) values('g', 10, 'girl'), ('h', 10, 'girl'), ('i', 10, 'girl');'
* 向数据表中插入数据
* 'insert [into] tb_name set column_name=column_value,...;'
* 备注：insert set语句插入数据时，对于未给出值的字段将被设置为默认值
* 示例：向学生表中插入一条数据
* 'insert student_info set name='j', age=10, sex='boy';'
* 向数据表中插入查询结果
* 'insert [into] table_name[(column_name,...)] select column_name,... from tb_name2;'
* 备注：insert select语句可以将数据表的查询结果插入数据表中
* 示例：把学生表的查询结果都插入教师表中
* 'insert into teacher_info select * from student_info;'

### 4.2 删除
* 删除数据表中的字段值
* 'delete from tb_name [where 条件表达式] [limit 删除前n行]'
* 示例：把教师表中名字等于c的数据删除
* 'delete from teacher_info where name='c';'
* 示例：把教师表中前5行的数据删除
* 'delete from teacher_info limit 5;'
* 删除数据表中所有的数据(相当于清空操作)
* 'truncate [table] tb_name;'

### 4.3 修改
* 修改数据表中的字段值
* 'update tb_name set column_name=column_value,... [where 条件表达式] [limit 修改前n行]'
* 示例：把教师表的age字段值都改为30
* 'update teacher_info set age=30;'
* 示例：把教师表的id=7的行sex字段值改为boy
* 'update teacher_info set sex='boy' where id=7;'
* 示例：把教师表的前5行的sex字段值改为boy
* 'update teacher_info set sex='boy' limit 5;'

### 4.4 查看
* 查看数据表中所有的字段的值
* 'select * from tb_name;'
* 查看数据表中指定字段的值
* 'select column_name,... from tb_name;'
* 示例：从学生表中查询id和age字段
* 'select id, age from student_info;'


## 5.mysql的三种数据类型：
### 5.1.数字类型
* 包括整型和浮点型,最常用的包括：int,float,double

### 5.2.字符串类型：
* a.普通的文本字符串类型(固定长度0~255的char型和变长的varchar型)
* 注意：在定义char和varchar时都要声明长度，否则默认长度只有1
* 如果需要快速的性能，选择char型
* 如果需要节省空间，选择varchar型
* b.可选类型(存储长文本的text型和存储声音图像等二进制数据的blob型)
* 如果搜索的内容不区分大小写，可以使用text型
* 如果搜索的内容区分大小写，可以blob型
* c.特殊类型(set型和enum型)
* enum('value1','value2',.....)只允许选择一个值或者为Null，如性别字段
* set('value1','value2',.....)允许选多个值或者为Null，如兴趣字段

### 5.3.时间日期类型：
* date,格式为2018-07-09
* time,格式为08:10:30
* datetime,格式为2018-07-09 08:10:30
* year,格式为2018或18
* timestamp,时间标签


## 6.mysql的查询语句：
### 6.1 单表查询
* select语句语法
* 'select column_name,... from tb_name [where 条件表达式] [group by 分组字段名] [order by 排序字段名] [having 条件表达式] [limit 输出个数]'
* 查看数据表中所有的字段的值
* 'select * from tb_name;'
* 查看数据表中指定字段的值
* 'select column_name,... from tb_name;'
* 使用关键字as给查询结果字段起别名，返回的结果字段名就变成了新起的别名
* 'select name as student_name from student'
* 使用比较运算符查询
* 'select * from student_info where age > 10;'
* 'select * from student_info where age <= 10;'
* 'select * from student_info where age != 10;'
* 使用关键字in的集合查询
* 'select * from student_info where age in (7, 12);'
* 'select * from student_info where age not in (7, 12);'
* 使用关键字between and的范围查询
* 'select * from student_info where age between 10 and 13;'
* 使用关键字like的字符匹配查询
* 备注：通配符%可以匹配任意个字符(零个，一个或多个)，通配符_只能匹配一个字符
* 'select * from student_info where name like '%a%';'
* 'select * from student_info where name not like '%a%';'
* 'select * from student_info where name like '_a_';'
* 'select * from student_info where name not like '_a_';'
* 使用关键字is null的空值查询
* 'select * from student_info where sex is null;'
* 'select * from student_info where sex is not null;'
* 使用关键字and的多条件查询
* 'select * from student_info where name like '%a%' and age=8;'
* 使用关键字or的多条件查询
* 'select * from student_info where name like '%a%' or age=8;'
* 使用关键字distinct去除结果中的重复行
* 'select distinct name from student_info;'
* 使用关键字order by对查询结果排序
* 备注：ASC参数表示升序排序，DESC参数表示降序排序，默认为升序排序
* 'select * from student_info order by age desc;'
* 'select * from student_info order by age;'
* 使用关键字group by的分组查询，group by经常和聚合函数一起使用
* 注意：sql_mode变量中有ONLY_FULL_GROUP_BY的限制，需要去掉，否则会有报错
* 备注：默认情况下每组只显示一条记录，通过group_concat函数把指定字段的所有记录都显示出来
* 'select * from student_info group by age;'
* 'select id, name, group_concat(age), sex from student_info group by age;'
* 'select * from student_info group by age, sex;'
* 使用关键字limit的限制查询结果数量
* 备注：只有一个参数时表示返回结果的个数，有两个参数时第一个参数表示返回的起始行数，第二个参数表示返回结果的个数
* 'select * from student_info limit 30;'
* 'select * from student_info limit 20, 30;'
* 使用关键字having进行查询，having通常和group by一起使用(group by不一定需要having)，用来过滤group by返回的数据集
* 备注：having和where的区别在于where无法与聚合函数一起使用，having可以弥补where不能与聚合函数一起使用的不足
* 示例：将学生表按name字段进行分组，然后输出name字段有两个以上重复的数据行
* 'select group_concat(id), name from student_info group by name having count(name) >= 2'
* 在单表查询中给表临时起名，不需要用关键字，原表名和临时表名用空格隔开
* 注意：同一个查询语句中可以给数据表起多个临时名，多个临时名指的都是同一个数据表
* 示例：数据表为Scores，将数据表临时命名为a和b
* 'select a.Score, (select count(distinct b.score) from Scores b where b.score >= a.score) as Rank from Scores a order by a.Score desc'


### 6.2 聚合函数查询
* 聚合函数根据一组数据求出一个值，聚合函数的结果只能根据选定行中非空的值进行计算，null值会被忽略
* count()函数返回指定字段的非null值的结果个数，当参数为*时返回包含null值的结果个数
* 'select count(sex) from student_info;'
* 'select count(*) from student_info;'
* sum()函数返回某个字段值的总和
* 'select sum(age) from student_info;'
* avg()函数返回某个字段的平均值
* 'select avg(age) from student_info;'
* max()函数返回某个字段中的最大值
* 'select max(age) from student_info;'
* min()函数返回某个字段中的最小值
* 'select min(age) from student_info;'

### 6.3 多表查询
* 多表查询又称为连接查询，包括内连接(等同连接)，外连接(左连接、右连接、全连接)
* 数据库在通过连接两张或多张表来返回记录时，都会生成一张中间的临时表，然后再将这张临时表返回给用户
* 内连接是最普遍连接类型，要求构成连接的每一部分的每个表都匹配
* 其中最常用的是等同连接/相等连接，连接后的表中某个字段与每个表中的都相同
* 注意：内连接可以使用关键字join或inner join或省略关键字直接用逗号隔开，以下三个命令效果相同
* 'select * from student_info, teacher_info where teacher_info.name = student_info.name;'
* 'select * from student_info join teacher_info where teacher_info.name = student_info.name;'
* 'select * from student_info inner join teacher_info where teacher_info.name = student_info.name;'
* 1.外连接是指用outer join关键字将两个表连接起来进行查询
* 左连接(left join)是用左表中所有数据分别与右表中每条数据进行连接组合
* 左连接相当于以左表为准，返回左表右表都有的数据(相当于内连接的数据)，以及左表有右表没有的数据(右表部分填充为null)
* 'select * from teacher_info left join student_info on teacher_info.name = student_info.name;'
* 2.右连接(right join)是将右表中所有数据分别于左表中每条数据进行连接组合
* 右连接相当于以右表为准，返回左表右表都有的数据(相当于内连接的数据)，以及右表有左表没有的数据(左表部分填充为null)
* 'select * from teacher_info right join student_info on teacher_info.name = student_info.name;'
* 3.全连接是不加连接条件，得到结果个数会是一个笛卡尔乘积
* 'select * from student_info, teacher_info;'
* 注意：在使用left jion时，on和where条件的区别如下
* on条件是在生成临时表时使用的条件，它不管on中的条件是否为真，都会返回左边表中的记录
* where条件是在临时表生成好后，再对临时表进行过滤的条件，这时已经没有left join的含义了，条件不为真的就全部过滤掉
* 一般在内连接中用where，左连接和右连接中用on

### 6.4 子查询
* 子查询就是一个查询的结果是另一个查询的条件，mysql支持多层查询，并且从查询最内层开始
* 使用关键字in的子查询
* 注意：一般使用in关键字只能支持一个值的判断，而在多层查询中使用in可以支持多个值
* 'select * from student_info where name in (select name from teacher_info);'
* 使用比较运算符的子查询
* 'select * from student_info where age < (select age from teacher_info where id=10);'
* 使用关键字exists的子查询
* 备注：使用exists时内层查询语句不返回查询的结果，当内层查询查到满足要求的记录时返回true，否则返回false；仅当内层返回true时外层才进行查询
* 'select * from student_info where exists (select * from teacher_info where age < 50);'
* 使用关键字any的子查询
* 备注：使用any表示只要满足内层查询返回结果的任何一条，就可以来执行外层查询语句
* 'select * from student_info where age < any(select age from teacher_info);'
* 使用关键字all的子查询
* 备注：使用all表示需要满足内层查询返回结果的每一条，才可以执行外层查询语句
* 'select * from student_info where age < all(select age from teacher_info);'

### 6.5 合并查询结果
* 合并查询结果就是将多个查询结果合并到一起显示
* 使用关键字union的合并查询(结果合并后去重)
* 'select name from student_info union select name from teacher_info;'
* 使用关键字union all的合并查询(结果简单合并，允许有重复值)
* 'select name from student_info union all select name from teacher_info;'

### 6.6 正则表达式查询
* 使用关键字regexp进行正则匹配
* 'select * from student_info where name regexp '^a';'


## 7.编码格式：
### 7.1 查看编码格式
* 查看数据库编码格式
* 'show create datebase db_name;'
* 查看数据表编码格式
* 'show create table tb_name'

### 7.2 创建时指定编码格式
* 创建数据库
* 'create database db_name character set=GBK;' 
* 创建数据表
* 'create table tb_test (id int) character set=utf8;'
* 注意：如果创建时不指定编码格式，则默认编码格式是latin1，不支持中文

### 7.3 修改编码格式
* 修改数据库的编码格式
* 'alter database db_name default character set gbk' 
* 修改数据表的编码格式
* 'alter table tb_name convert to character set utf8;'


## 8.数据导入导出：
### 8.1 sql语句导出
* sql语句导出数据表(可以导出为文本、XML、HTML等格式)
* 'select * from tb_name into outfile file_path [option,...]'
* 常用option如下
* fields terminated by '字符'  将字段按指定字符分隔，默认为制表符\t
* fields [optionally] enclosed by '字符'  将每个字段两边加上指定的字符，一般用于添加引号""，默认不添加字符
* lines starting by '字符'  给每一行数据开头添加字符，默认不添加字符
* lines terminated by '字符'  给每一行数据结尾添加字符，默认为换行符\n
* 示例：导出为txt文本格式，每一行以>开头
* "select * from tb_word into outfile '/var/lib/mysql-files/topic_word.txt' lines starting by '>';"
* 示例：导出为CSV格式，数据之间用逗号隔开
* "select * from tb_word into outfile '/var/lib/mysql-files/topic_word.csv' fields terminated by ',';"
* 注意：使用sql语句默认只允许导出到指定路径(Linux命令导出没有路径限制)，导出其他路径会有关于'secure-file-priv'的安全报错
* 查看数据导出路径设置
* "show global variables like '%secure%';"
* 备注：sql中没有找到直接导出数据库的语句

### 8.2 linux命令导出
* linux命令导出数据库(包含所有表结构和表中数据)
* 'mysqldump -u user_name -p db_name > file_path'
* 示例：导出db_test数据库到指定路径
* 'mysqldump -u root -p db_test > /root/data/db_test.sql'
* linux命令导出数据库(只导出表结构不含表中数据)
* 'mysqldump -u user_name -p -d db_name > file_path'
* linux命令导出数据表(包含表结构和表中数据)
* 'mysqldump -u user_name -p db_name tb_name > file_path'
* 示例：导出db_test数据库中的tb_word数据表到指定路径
* 'mysqldump -u root -p db_test tb_word > /root/data/tb_test.sql'
* linux命苦导出数据表(只导出表结构不含表中数据)
* 'mysqldump -u user_name -p -d db_name table_name > file_path' 

### 8.3 sql语句导入数据
* sql语句导入数据表(导入前数据表必须已经存在且字段格式与要导入的数据文件一致)
* 'load data infile file_path into table tb_name'
* 示例：将指定文件中的数据导入tb_word数据表中
* 'load data infile '/var/lib/mysql-files/test' into table tb_word;'
* 注意：使用sql语句导入数据时同样只能从mysql指定的路径下导入数据文件

### 8.4 linux命令导入数据库
* linux命令导入数据库(导入前数据库必须已经存在)
* 'mysql -u user_name -p db_name < database_file_path'
* linux命令导入数据表(不需要指定导入的数据表)
* 'mysql -u user_name -p db_name < table_file_path'
* 备注：导入的sql文件都应该是.sql格式的


## 9.mysql提供的函数：
### 9.1 数学函数
* abs(x)函数求x的绝对值
* floor(x)函数求小于等于x的最大整数
* rand()函数返回0~1之间的随机数
* pi()函数返回圆周率
* truncate(x, y)返回x保留到小数点后y位的值
* round(x)函数对x四舍五入取整
* round(x, y)函数对x四舍五入保留到小数点后y位
* sort(x)函数返回x的平方根

### 9.2 字符串函数
* char_length(s)函数返回字符串的字符数
* length(s)函数返回字符串的长度
* left(s, n)函数返回字符串的前n个字符
* upper(s)函数将字符串所有字母都变大写
* reverse(s)函数将字符串反转

### 9.3 日期和时间函数
* curdate()/current_date() 获取当前的日期
* curtime()/current_time() 获取当前的时间
* now()/localtime()/sysdate() 获取当前的日期和函数
* datediff(d1, d2) 计算日期d1和日期d2之间相隔的天数
* adddate(d1, n) 计算日期d1之后的n天对应的日期
* subdate(d1, n) 计算日期d1之前的n天对应的日期

### 9.4 条件判断函数
* if(expr, v1, v2) 如果表达式expr成立，则执行v1，否则执行v2
* ifnull(v1, v2) 如果v1不为空，则显示v1的值，否则显示v2的值


## 10.索引
### 基本概念
* 索引是一种将数据库中单列或多列的值进行排序的结构
* 索引的优点：
* 索引是由数据表中一列或多列组成，指向数据库中具体数据所在位置，可以优化数据库的查询效率
* 当用户通过索引查询时不需要再遍历数据库中所有的数据，大幅提高查询效率
* 索引的缺点：
* 创建和维护索引需要耗费时间，且时间与数据规模成正比，不利于数据更新
* 存储索引需要另外占用物理存储空间
* 索引的存储类型包括b树索引和hash索引，其中默认为b树索引
* 创建索引时要设置索引名，索引名不一定要和数据表名一致

### 索引的分类
* 1.普通索引
* 不应用任何限制条件的索引，可以在任何数据类中创建，字段本身的约束条件可以判断其值是否为空或唯一
* 2.唯一性索引
* 使用unique参数可以设置唯一索引，索引值必须对应唯一字段，例如主键就是一种特殊的唯一索引
* 3.全文索引
* 使用fulltext参数可以设置全文索引，只能创建在char、varchar或text等字符串类型的数据字段中
* 4.单列索引
* 只对应一个字段的索引就可以称为单列索引，包括以上3种索引都属于单列索引
* 5.多列索引
* 对应表中的多个字段，可以通过多个字段查询，但应用索引时必须用到其中的第一个字段
* 6.空间索引
* 使用spatial参数可以设置空间索引，只能建立在空间数据类型(geometry)上，但mysql中只有myisam存储引擎支持空间检索

### 创建新数据表时建立索引
* 1.普通索引
* 'create table student(id int not null auto_increment primary key, index student_info(id));'
* 2.唯一索引
* 'create table student(id int not null auto_increment primary key, unique index student_info(id));'
* 3.全文索引
* 'create table student(name char not null, fulltext index student_info(name))engine=MyISAM;'
* 4.单列索引
* 'create table student(id int not null auto_increment primary key, index student_info(id));'
* 5.多列索引
* 'create table student(id int not null, name char not null, index student_info(id, name));'
* 6.空间索引
* 'create table list(id int not null, goods geometry not null, spatial index list_info(goods))engine=MyISAM;'

### 在已创建的数据表中建立索引
* 1.普通索引
* 'create index student_info on student(id)'
* 2.唯一索引
* 'create unique index student_info on student(id)'
* 3.全文索引
* 'create fulltext index student_info on student(name)'
* 4.单列索引
* 'create index student_info on student(id)'
* 5.多列索引
* 'create index student_info on student(id, name)'
* 6.空间索引
* 'create spatial index list_info on list(goods)'

### 在已有索引的数据表上添加新索引
* 1.普通索引
* 'alter table student add index student_info(id)'
* 2.唯一索引
* 'alter table student add unique index student_info(id)'
* 3.全文索引
* 'alter table student add fulltext index student_info(name)'
* 4.单列索引
* 'alter table student add index student_info(id)'
* 5.多列索引
* 'alter table student add index student_info(id, name)'
* 6.空间索引
* 'alter table list add spatial index list_info(goods)'

### 删除索引
* 'drop index index_name on tb_name'




## 其他常用命令：
* 1.查看mysql的系统参数
* 'show global variables'
* 2.查看mysql端口(默认端口是3306)
* "show global variables like 'port'"
* 3.获取数据版本号
* 'select version();'
* 4.获取当前数据库名
* 'select database();'或'select schema();'
* 5.获取当前用户名
* 'select user();'或'select system_user();'或'select current_user();'
* 6.获取mysql服务器的连接状况
* 'select connection_id();'
* 7.查看sql_mode的值
* 'show variables like "sql_mode";'
* 8.修改sql_mode的值
* 'set sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';'


---

### 待完善：
* 1.数据完整性约束
* 2.数据库触发器
* 3.数据库视图


