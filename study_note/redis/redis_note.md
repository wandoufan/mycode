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