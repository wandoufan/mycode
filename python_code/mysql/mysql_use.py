# SQL(structured query lanuguage)，即结构化查询语句

# mysql安装
# 在官网下载MySQL Community Edition版本，安装文件为mysql-installer-community-8.0.11.0.msi
# 安装时会有check requirements,如果有未打钩的选项表示不符合安装前环境要求；
# 对于不符合的选项，点击execute可以直接下载要求中需要的软件环境
# 安装中,mysql默认端口是3306,除非端口已被占用,否则不做修改

# mysql的命令行界面：MySQL 8.0 Command Line Client - Unicode
# mysql的可视化界面：MySQL Workbench 8.0 CE
# 管理员账户:root 密码：000000

# 数据模型通常由数据结构，数据操作，完整性约束3部分组成
# 数据结构：是对系统的静态描述，包括数据的内容、类型、性质
# 数据操作：是对系统动态特征的描述，包括对数据库对象示例的各种操作
# 完整性约束：是完整性规则的合集

# 常见的数据模型：
# 1.层次模型：用树状结构来表示实体类型和实体之间的联系
# 2.网状模型：用有向图结构表示实体类型和实体之间的联系
# 3.关系模型：用二维表来描述数据，是目前主流的数据库

# 关系模型的相关概念：
# 关系：一个二维表就是一个关系
# 元组：二维表中的一行，即表中的记录
# 属性：二维表中的一列，用类型和值表示
# 域：每个属性取值的变化范围

# 1.第一范式：在一个关系中消除重复字段，且各个字段都是最小的逻辑存储单位
# 即每个属性字段都要求是最小的，不可再被拆分的
# 例如：不能存在三年级二班这样可以被拆分成三年级和二班的字段
# 数据组的每个属性只可以包含一个值
# 关系中的每个数组必须包含相同数值的值
# 关系中的每个数组一定不能相同
# 2.第二范式：在第一范式的基础上要求数据库表中的每个记录行必须可以被唯一的区分
# 唯一属性列就是主关键字/主键
# 3.第三范式：在第二范式的基础上要求关系表不存在非关键字列对任意候选关键字列的传递函数依赖
# 传递函数依赖，即如果存在关键字段A决定非关键字段B，而非关键字段B又决定非关键
# 字段C，则称非关键字段C传递函数依赖于关键字段A
# 例如：工号-->(姓名,年龄,部门,部门经理)，这个关系符合第二范式
# 但是其中隐藏着关系:工号-->部门-->部门经理，因此不符合第三范式
# 注意：按照高的范式标准设计，可以消除数据冗余，增删改查时的异常

# 数据库的三级模式结构是指模式、外模式、内模式
# 1.模式
# 模式也成逻辑模式或概念模式，是数据库中全体数据的逻辑结构和特征的描述，
# 是所有用户的公共数据视图，一个数据库只有一个视图，处于中间层
# 2.外模式
# 外模式也称用户模式，是数据库用户能够看见和使用的局部数据的逻辑结构和特征
# 的描述，是数据库用户的数据视图。外模式是模式的子集，数据库可以有多个外模式
# 3.内模式
# 内模式也成存储模式，是数据物理结构和存储方式的描述，是数据在数据库内部的表示
# 方式，一个数据库只有一个内模式

# 数据库管理系统提供了两层映射
# 对每个外模式都有一个对应的外模式/模式映射，保证数据与程序的逻辑统一性
# 模式/内模式映射是唯一的，定义了数据库全局逻辑结构和存储结构之间的对应关系
# 保证数据与程序的物理独立性

# mysql通过windows的cmd窗口操作：
# 'net start mysql' 启动mysql服务器
# 'net stop mysql' 关闭mysql服务器
# 'mysql -u root -h 127.0.0.1 -p password' 登录mysql服务器
# mysql命令使用前要添加 到系统环境变量，否则无法使用

# 数据库的常用对象:
# 1.表,包含数据库中所有数据的数据库对象，由行和列组成，用于组织和存储数据
# 2.字段,表中的每一列称为一个字段，字段有自己的属性，sql支持五种基本的
# 字段类型：字符型，文本型，数值型，逻辑型，时间日期型
# 3.索引,依赖于表建立，使查找时无需对整个表进行扫描就可以找到所需的数据
# 4.视图,从一张表或多张表中导出的虚拟表，是用户查询目标数据的结果
# 5.存储过程,是一组为完成特定功能的sql语句集合

# 系统数据库,是指按照mysql后系统自带的数据库:
# 1.information_schema数据库,用于存储数据库对象相关的信息，如用户表信息，列信息等
# 2.performance_schema数据库,用于存储数据库服务器的性能参数
# 3.sakila数据库,是mysql提供的常用数据表样例
# 4.test数据库,是系统自动创建的测试数据库，但不建议用它进行测试
# 5.world数据库,3张表分别存储城市，国家和国家使用的语言等

# 数据库的命名规则:
# 1.不能与其他数据库同名
# 2.数据库名字可以由任意数字，字母，下划线_，'$'符号组成，并用上述任意字符开头
# 3.数据库名最长不超过64个字符，别名最长不超过256个字符
# 4.不能使用mysql关键字作为数据库名，数据表明
# 5.windows下对大小写不敏感，但Linux下对大小写敏感，建议用小写

# mysql的三种数据类型：
# 1.数字类型,包括整型和浮点型,最常用的包括：int,float,double
# 2.字符串类型，包括：
# a.普通的文本字符串类型(固定长度0~255的char型和变长的varchar型)
# 如果需要快速的性能，选择char型
# 如果需要节省空间，选择varchar型
# b.可选类型(存储长文本的text型和存储声音图像等二进制数据的blob型)
# 如果搜索的内容不区分大小写，可以使用text型
# 如果搜索的内容区分大小写，可以blob型
# c.特殊类型(set型和enum型)
# set('value1','value2',.....)只允许选择一个值，如性别字段
# enum('value1','value2',.....)允许选多个值，如兴趣字段
# 3.时间日期类型，包括：
# date,格式为2018-07-09
# time,格式为08:10:30
# datetime,格式为2018-07-09 08:10:30
# year,格式为2018或18
# timestamp,时间标签