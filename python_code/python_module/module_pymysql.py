# coding:utf-8

# PyMySQL模块是python3中用来连接操作mysql数据库的模块，可以实现在python中直接使用sql语句
# 在Python2中则使用mysqldb模块
# 参考资料：
# http://www.runoob.com/python3/python3-mysql.html
# https://pypi.org/project/PyMySQL/

# 注意:这个模块有坑，虽然模块名本身是大写PyMySQL,但import时要用小写pymysql，否则报错找不到模块

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
	
except Exception as reason:
	print('error: select data failed\n',reason)

# 5.删除数据表中的数据
try:
	cursor.execute('delete from student where id=007;')
	
except Exception as reason:
	print('error: select data failed\n',reason)

connection.close()# 关闭连接
