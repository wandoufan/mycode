# 主要记录redis的一些命令：

## linux环境下redis的使用：
* 启动redis服务(进入到安装目录下的src目录)
* './redis-server'
* 进入到redis的命令窗口(进入到安装目录下的src目录)
* 'redis-cli -h host -p port -a password'
* 进入redis的命令窗口后测试redis服务是否启动，运行则显示PONG
* 'ping'


## 键(key)命令
* 键命令用于管理redis的键，语法格式为'command key_name'
* 当key存在时删除key
* 'del key'
* 检查key是否存在
* 'exists key'
* 序列化给定key，并返回被序列化的值



## 字符串(string)命令
* string是redis最基本的类型，string可以包含任何类型的数据，包括jpg格式的图片和序列化的对象，最大可存储512MB


## 哈希(hash)命令



## 列表(list)命令


## 集合(set)命令


## 有序集合(sorted set)命令


## 事务命令


## 其他常用命令
* 显示redis服务器的版本等详细信息
* 'info'
* 同时执行n个请求来完成性能测试
* 'redis-benchmark -n 10000  -q'
* 查看redis是否设置了连接密码
* 'config get requirepass'
* 设置redis的连接密码
* 'AUTH password'
* redis数据备份(在 redis 安装目录中创建dump.rdb文件)
* 'save'
* redis的后台备份
* 'bgsave'
* redis恢复数据(将备份文件dump.rdb移动到 redis 安装目录并启动服务即可)
* 'config get dir'