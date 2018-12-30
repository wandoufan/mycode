# 主要记录redis的一些基本知识点：

## redis基本介绍：
* redis（remote dictionary server）是用C语言开发的一个开源的高性能键值对（key-value）数据库
* redis属于no-sql的非关系型数据库，通常被称为数据结构服务器
* redis属于内存数据库，数据都缓存在内存中进行处理，因此具有很高的性能
* redis的value支持的数据类型包括：
  * 字符串string
  * 哈希散列hash 
  * 列表list
  * 集合set
  * 有序集合sorted set
* redis相比其他key-value数据库具有以下优点：
  * redis支持数据的持久化，可以将内存中的数据永久保存到磁盘上，重启的时候可以再次从磁盘中加载使用
  * redis不仅支持key-value类型的数据，同时还提供list、set、hash等存储结构
  * redis支持master-slave模式的数据备份
  * redis的操作都具有原子性，即操作要么成功执行要么失败完全不执行
* redis的默认端口为6379

## redis参考资料：
* redis官网
> https://redis.io/
* redis参考资料
> http://www.runoob.com/redis/redis-intro.html
* redis在线测试
> http://try.redis.io/

## redis安装：
* Linux环境下安装：
> https://www.jianshu.com/p/bc84b2b71c1c
* windows环境下安装：
> http://www.runoob.com/redis/redis-install.html

## 关系型数据库和非关系型数据库：
* 常见的关系型数据库主要包括：oracle、mysql、DB2、Microsoft sql server、Microsoft Access、SQLLite
* 常见的非关系型数据库主要包括：redis、mongo DB、Neo4j  

### 非关系型数据库
* 关系型数据库最主要的数据结构是二维表，通过二维表及表之间的联系来组成一个数据组织
* 优点
  * 易于维护，都是使用格式一致的表结构存储
  * 使用方便，都支持使用SQL语言进行操作
  * 可以进行多表之间的复杂查询
  * 事务操作可以保证数据的一致性和完整性
* 缺点
  * 只能从磁盘中读取数据，读写性能一般
  * 对海量数据的增删改查性能一般
  * 只能支持基础类型的数据，
  * 数据之间复杂的关系不利于后期的扩展
* 应用场景
  * 一般量级的、对数据安全性要求很高的场景

### 非关系型数据库
* 非关系型数据库最主要的数据结构是key-value，数据以对象的形式存储在数据库中，而对象之间的的关系通过每个对象自身的属性来决定
* 优点
  * 可以直接从内存中读取数据，无需经过sql层解析，读写性能很高
  * key-value的结构支持多种value类型，包括文档形式和图片形式
  * 数据和数据之间没有关系，也不存在耦合性，易于扩展
* 缺点
  * 数据结构较为复杂，不合适复杂查询
  * 不支持sql语言，每种no-sql数据库都要单独学习
  * 没有事务关系，无法保证数据的一致性和完整性
* 应用场景
  * 海量级数据、对数据安全性要求不敏感的场景