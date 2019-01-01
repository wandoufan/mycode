# 主要记录redis的一些命令：
* 备注：命令中[]的部分表示可选项
* 备注：列表等数据类型都没有单独创建的命令，直接插入数据时就创建了一个新的数据结构


## linux环境下redis的使用：
* 启动redis服务
* 'redis-server'
* 进入到redis的命令窗口
* 'redis-cli -h host -p port -a password'或'redis'
* 进入redis的命令窗口后测试redis服务是否启动，运行则显示PONG
* 'ping'


## 键(key)命令
* 键命令用于管理redis的键，语法格式为'command key_name'
* 当key存在时删除key
* 'del key'
* 检查key是否存在
* 'exists key'
* 序列化给定key，并返回被序列化的值
* 'dump key'
* 为给定的key设置过期时间，以秒计数
* 'expire key.seconds'
* 查找符合给定模式（pattern）的key
* 'keys pattern'
* 将当前数据库的key移动到指定的数据库db中
* 'move key db'
* 去掉key的过期时间，即key永远不会过期
* 'persist key'
* 返回给定key的剩余生存时间，以秒计数
* 'ttl key'
* 从当前数据库随机返回一个key
* 'randomkey'
* 对key进行重命名
* 'rename key newkey'
* 仅当newkey不存在时，将key改名为newkey
* 'renamenx key newkey'
* 返回key所存储的值value的类型
* 'type key'


## 字符串(string)命令
* string是redis最基本的类型，string可以包含任何类型的数据，包括jpg格式的图片和序列化的对象，最大可存储512MB
* 备注：这里的字符串概念和python中的字符串概念不太一样，字符串是可以包含任何类型的数据
* 例如3，在这里不会像python一样区分是整型还是字符串类型
* 设置指定key的值
* 'set key value'
* 设置所有(一个或多个)key-value对
* 'mset key1 value1 [key2 value2,...]'
* 仅当所有给定key都不存在时，设置所有key-value对
* 'msetnx key1 value1 [key2 value2,...]'
* 仅当在key不存在的时候设定key的值
* 'setnx key value'
* 获取指定key的值
* 'get key'
* 获取key对应字符串的子串
* 'getrange key start end'
* 将给定key的值设定为value，并返回key的旧值
* 'getset key value'
* 获取所有(一个或多个)给定key的值
* 'mget key1 [key2,...]'
* 将value的值关联到key，并设定key的过期时间，以秒计数
* 'setex key seconds value'
* 返回key对应的字符串的长度
* 'strlen key'
* 将key中存储的数字值增加1
* 'incr key'
* 将key中存储的数字值增加increment
* 'incrby key increment'
* 将key中存储的数字值减少1
* 'decr key'
* 将key中的存储的数字值减少increment
* 'decr key increment'
* 仅当key存在且存储一个字符串时，在指定的value值追加到字符串末尾
* 'append key value'


## 哈希(hash)命令
* hash是一个string类型的field和value的映射表，hash特别适合用于存储对象，每个hash可以存储40多亿个键值对
* 备注：hash类似于python中的字典结构
* 设置hash表的key中的字段的值
* 'hset key field value'
* 设置多个field-value阈值对到hash表的key中
* 'hmset key field1 value1 [field2 value2,...]'
* 仅当字段field不存在时设置hash表的字段值
* 'hsetnx key field'
* 查看hash表中指定的字段是否存在
* 'hexists key field'
* 获取hash表中指定key的指定字段的值
* 'hget key field'
* 获取hash表中指定key的所有字段的值
* 'hmget key field1 [field2,...]'
* 获取hash表中指定key的所有字段和值
* 'hgetall key'
* 获取hash表中所有的字段
* 'hkeys key'
* 获取hash表中字段的数量
* 'hlen key'
* 获取hash表中所有的值
* 'havls key'
* 删除一个或多个hash表的字段
* 'hdel key field1 [field2,...]'


## 列表(list)命令
* list是简单的字符串列表，按照插入的顺序进行排序，可以在列表的首/尾添加元素，每个列表最多可以包含40多亿个元素
* 备注：这里的列表和python中的列表概念不太一样，更接近于数据结构中的栈/队列
* 在列表首部添加一个或多个元素
* 'lpush key value1 [value2,...]'
* 在列表尾部添加一个或多个元素
* 'rpush key value1 [value2,...]'
* 通过索引获取列表中的元素
* 'lindex key index'
* 获取列表指定范围内的元素
* 'lrange key start stop'
* 获取列表长度
* 'llen key'
* 通过索引更改列表元素的值
* 'lset key index value'
* 通过索引删除列表元素的值
* 'lrem key index value'
* 只保留指定索引范围内的列表元素，索引范围外的都删除
* 'ltrim key start end'
* 移除并获取列表的第一个元素
* 'lpop key'
* 移除并获取列表的最后一个元素
* 'rpop key'
* 移除并获取列表的第一个元素，如果列表中没有元素会阻塞列表直到超时或发现可弹出元素
* 'blpop key1 [key2,...] timeout'
* 移除并获取列表的最后一个元素，如果列表中没有元素会阻塞列表直到超时或发现可弹出元素
* 'brpop key1 [key2,...] timeout'


## 集合(set)命令
* set是string类型的无序集合，集合成员是唯一的，即集合中不能有重复的元素，每个集合最多可以包含40多亿个元素
* 集合是通过hash表进行实现的，因此增删查等操作的复杂度都是O(1)
* 向集合中添加一个或多个元素
* 'sadd key member1 [member2,...]'
* 获取集合中成员的个数
* 'scard key'
* 获取所有集合的差集
* 'sdiff key1 [key2,...]'
* 获取所有集合的差集并存储在destination中
* 'sdiffstore destination key1 [key2,...]'
* 获取所有集合的交集
* 'sinter key1 [key2,...]'
* 获取所有集合的交集并存储在destination中
* 'sinterstore destination key1 [key2,...]'
* 获取所有集合的并集
* 'sunion key1 [key2,...]'
* 获取所有集合的并集并存储在destination中
* 'sunion destination key1 [key2,...]'
* 判断member元素是否是集合key的成员
* 'sismember key member'
* 返回集合中的所有成员
* 'smembers key'
* 随机返回集合中的一个或count个成员
* 'srandmember key [count]'
* 将member元素从当前集合移动到另一集合
* 'smove set1 set2 member'
* 移除集合中的一个或多个元素
* 'srem key member1 [member2,...]'
* 随机移除并返回集合中的一个元素
* 'spop key'


## 有序集合(sorted set)命令
* 有序集合和集合一样也是string类型元素的集合,且不允许重复的成员，每个集合最多可以包含40多亿个元素
* 不同的在于，有序集合中的每个元素都对应一个double类型的分数(分数可以重复)，集合中元素按照分数进行由小到大的排序
* 备注：元素对应的分数在元素加入有序集合时进行设置
* 向有序集合中添加一个或多个成员，或者更新已存在成员的分数
* 'zadd key score1 member1 [score2 member2,...]'
* 获取有序集合中成员的个数
* 'zcard key'
* 获取有序集合中在指定分数区间的成员的个数
* 'zcount key min_socre max_score'
* 获取有序集合中在指定分数区间的成员
* 'zrangebyscore key min_score max_score'
* 获取有序集合中指定成员的分数值
* 'zscore key member'
* 获取有序集合中指定成员的索引
* 'zrank key member'
* 获取有序集合的指定的索引区间的成员
* 'zrange key start stop'
* 对有序集合中指定成员的分数增加increment
* 'zincrby key incremnt member'
* 从有序集合中移除一个或多个成员
* 'zrem key member1 [member2,...]'
* 从有序集合中移除指定索引区间的成员
* 'zremrangebyrank key start stop'
* 从有序集合中移除指定分数区间的成员
* 'zremrangebyscore key min_socre max_score'


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