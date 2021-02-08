# mysql笔记

## mysql安装
linux环境下安装：
> http://www.runoob.com/mysql/mysql-install.html
windows环境下安装：
> https://www.mysql.com/downloads/
在官网下载MySQL Community Edition版本，安装文件为mysql-installer-community-8.0.11.0.msi
安装时会有check requirements,如果有未打钩的选项表示不符合安装前环境要求；
对于不符合的选项，点击execute可以直接下载要求中需要的软件环境
安装中,mysql默认端口是3306,除非端口已被占用,否则不做修改
mysql的命令行界面：MySQL 8.0 Command Line Client - Unicode
mysql的可视化界面：MySQL Workbench 8.0 CE

## 系统数据库
系统数据库是安装mysql后系统自带的数据库，用于存放系统自身信息，一般不能删除，包括：
1. information_schema数据库
2. performance_schema数据库
3. mysql数据库
4. sys数据库

## 数据库的命名规则:
1. 不能与其他数据库同名
2. 数据库名字可以由任意数字，字母，下划线_，'$'符号组成，并用上述任意字符开头
3. 数据库名最长不超过64个字符，别名最长不超过256个字符
4. 不能使用mysql关键字作为数据库名，数据表名
5. windows下对大小写不敏感，但Linux下对大小写敏感，建议用小写