# sqlite笔记

## 基本情况
sqlite是一个微型数据库，所有的数据表、索引等数据库元素全部都存在一个文件里  
sqlite expert是sqlite数据库的可视化管理工具，包含了sqlite数据库驱动  
即安装了sqlite expert之后就无需再安装sqlite数据库驱动  

## 优点缺点
1. 优点
sqlite是开源免费的  
体积很小，sqlite的驱动库文件只有500KB  
性能很高，对数据访问速度甚至超过了mysql  
无需服务器，无需进行任何的配置或安装，使用简单方便  
sqlite可以跨平台使用，在不同平台之间可以随意复制数据库  
sqlite是一个单机型数据库，不需要任何外部依赖  
2. 缺点
不能支持大量的数据和高并发用户量  
sqlite是一个单机型数据库，不能设置C/S架构  
sqlite中，视图是只读的，不可以在视图上执行DELETE、INSERT或UPDATE语句  

## sqlite中的数据类型、
1. 每个存储在sqlite数据库中的值都具有以下存储类之一：
NULL	值是一个 NULL 值  
INTEGER	值是一个带符号的整数，根据值的大小存储在 1、2、3、4、6 或 8 字节中  
REAL	值是一个浮点值，存储为 8 字节的 IEEE 浮点数字  
TEXT	值是一个文本字符串，使用数据库编码（UTF-8、UTF-16BE 或 UTF-16LE）存储  
BLOB	值是一个 blob 数据，完全根据它的输入存储  
2. Boolean 数据类型
sqlite没有单独的Boolean存储类，布尔值被存储为整数 0（false）和 1（true）  
3. Date 与 Time 数据类型
sqlite没有一个单独的用于存储日期和/或时间的存储类  
但 sqlite能够把日期和时间存储为 TEXT、REAL 或 INTEGER 值  
TEXT	格式为 "YYYY-MM-DD HH:MM:SS.SSS" 的日期  
REAL	从公元前 4714 年 11 月 24 日格林尼治时间的正午开始算起的天数  
INTEGER	从 1970-01-01 00:00:00 UTC 算起的秒数  
4. sqlite提供了很多种细分的数据类型

## sqlite的特性
1. sqlite是不区分大小写的，但也有一些命令是大小写敏感的，比如 GLOB 和 glob 在 sqlite的语句中有不同的含义  
2. sqlite没有用户帐户概念，而是根据文件系统确定所有数据库的权限  

## sqlite expert中使用sqlite
备注：QT里自带了sqlite，但不知道怎么打开，还是需要官网上下载安装  
安装了sqlite expert之后，并没有sqlite3.exe，即无法在cmd里直接运行sqlite命令  
1. 新建数据库
file - New DataBase，选择中对应的数据库文件  
注意：在expert的界面中无法直接新建数据库，必须在文件夹中新建一个txt然后改名  
数据库文件的后缀名包括：.db、.db3、.sqlite，使用任意一个都可以  
2. 在expert中有一个DDL窗口，对数据库做的操作会自动转换为sql语句  
3. 在expert中有一个SQL窗口，可以输入执行sql语句  

