# coding:utf-8

# PyMySQL模块是python3中用来连接操作mysql数据库的模块，可以实现在python中直接使用sql语句
# 在Python2中则使用mysqldb模块
# 参考资料：
# http://www.runoob.com/python3/python3-mysql.html
# https://pypi.org/project/PyMySQL/

# 注意：这个模块有坑，虽然模块名本身是大写PyMySQL,但import时要用小写pymysql，否则报错找不到模块
# 注意：除了查询外，增删改等操作都需要用commit()函数来提交修改

# 关于ORM模型与pymysql的说明：
# 使用pymysql来执行sql语句实际上执行了裸的原生sql语句，可能会存在sql注入等安全问题，推荐使用ORM模型  
# ORM(Object Relational Mapping)，即对象关系映射，通过ORM我们可以通过类的方式去操作数据库，而不用再写原生的sql语句
# 通过把表映射成类，把行作实例，把字段作为属性，ORM在执行对象操作的时候最终还是会把对应的操作转换为数据库原生语句
# 使用原生sql语句的缺点：
# 1.sql语句重复利用率不高，越复杂的sql语句条件越多，代码越长，会出现很多相近的sql语句  
# 2.很多sql语句是在业务逻辑中拼出来的，如果业务逻辑生变，原生sql更改起来比较多  
# 3.写sql时容易忽略web安全问题，造成一些如sql注入之类的安全漏洞  
# 使用ORM模型操作数据库的优点：
# 1.使用ORM做数据库的开发可以有效的减少重复SQL语句的概率，写出来的模型也更加直观、清晰  
# 2.ORM语句转化成原生的sql语句需要一定开销，但实际造成的性能损耗很小  
# 3.设计更加灵活，可以写出更加复杂的查询语句  
# 4.django封装了底层的数据库实现，ORM语句可以在sqlite3、Mysql、Postgresql等多种数据库间自由切换  


import pymysql

host = '127.0.0.1'
user = 'root'
passwd = '000000'
database = 'db_test'

# 连接数据库
connection = pymysql.connect(host, user, passwd, database, port=3306)  # mysql的默认端口是3306

# 使用cursor方法创建一个游标对象cursor
cursor = connection.cursor()
cursor.execute('use db_test')# 使用execute方法执行sql语句，命令末尾不用加分号;

# 1.创建新的数据表
cursor.execute('create table if not exists teacher (id int auto_increment primary key)')

# 2.数据表中插入数据
try:
	result = cursor.execute("insert into student if not exists values(007,'丁七','1999-02-02','二班')")
	connection.commit()# 提交修改
except:
	connection.rollback()# 发生错误就回滚
# 注意: commit方法和rollback方法保证了系统的安全性
# 注意：每次增删改等操作后都要commit方法进行提交，否则操作结果无法保存

# 3.查询数据表中的数据
try:
	cursor.execute('select * from student')
	# fetchone方法获取查询的第一个结果
	# result = cursor.fetchone()
	# fetchmany方法获取查询的前n个结果
	# result = cursor.fetchmany(n)
	# fetchall方法获取查询的所有结果，返回一个元组类型
	result = cursor.fetchall()
	for student in result:
		print(student)
except Exception as reason:
	print('error: select data failed\n',reason)

# 4.修改数据表中的数据
try:
	cursor.execute("update student set grade='三年级' where id=009;")
	connection.commit()# 提交修改
except Exception as reason:
	print('error: select data failed\n',reason)

# 5.删除数据表中的数据
try:
	cursor.execute('delete from student where id=007;')
	connection.commit()# 提交修改
except Exception as reason:
	print('error: select data failed\n',reason)

connection.close()# 关闭连接
