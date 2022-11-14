# PostgreSQL笔记

## 基本情况
PostgreSQL完全免费，而且是BSD协议，可以自己进行二次开发  
PostgreSQL的默认用户名为postgres  
PostgreSQL使用的默认端口为5432  
备注：安装PostgreSQL的分区需要是NTFS格式，如果是在FAT或FAT32分区下，可以正常安装，但数据库初始化之后可能会有问题  


## 管理工具
pgAdmin是一个针对PostgreSQL数据库的设计和管理接口  
目前实际使用的版本为pgAdmin III  
备注：不同的windows系统要下载不同版本的管理工具，详见pgAdmin官网  


## PostgreSQL远程连接配置
备注：默认情况下PostgreSQL不允许进行远程访问  
### 1. 配置数据库服务端
如果需要允许远程访问，需要修改两个配置文件：  
备注：修改前可以先把两个配置文件进行备份  
1. C:\Program Files(x86)\PostgreSQL\9.3\data\postgresql.conf
找到文件中的```listen_addresses```，将项值设定为"*"  
备注：在9.0 以上Windows版中，该项配置已经是"*"，无需修改  

2. C:\Program Files(x86)\PostgreSQL\9.3\data\pg_hba.conf
找到配置文件中的
```
host all all 127.0.0.1/32 md5
```
将这一行修改为：
```
host  all    all    0.0.0.0/0    md5
```
或者修改为：
```
host all all 127.0.0.1/32 trust
```

3. 如果不希望允许所有IP远程访问，则可以将上述配置项中的0.0.0.0设定为特定的IP值，比如：
```
host  all    all    192.168.1.0/24    md5
host  all    all    192.168.1.0/32    trust
```
表示允许网段 192.168.1.0上的所有主机使用所有合法的数据库用户名访问数据库，并提供加密的密码验证  
其中，数字24是子网掩码，表示允许192.168.1.0--192.168.1.255的计算机访问  

### 2. 配置数据库客户端
在数据库客户端，在开始菜单下点击pgAdmin III的图标打开数据库  
在'PostgreSQL 9.3 (x86)'上点击鼠标右键，选择'属性(P)'  
在弹出的'服务器localhost'界面中，'属性'--'主机'  
填入需要远程连接的数据库服务器的IP地址  


## 数采系统中PostgreSQL远程连接配置
一般直接在.cfg配置文件中写入远程数据库的主机IP，不用去pgAdmin III配置  
```
<hostname>191.30.2.16</hostname>
```


## 使用.sql文件来创建数据表
对.sql文件，选择对应的数据库，然后点击上面工具栏中的放大镜图标(里面带有'sql'字样)
在弹出的窗口中打开.sql文件，然后点击窗口的工具栏中三角形图标(带有'GPS'字样)，会显示出创建结果


## .sql文件内容示例
```
CREATE TABLE IF NOT EXISTS Loads_ALL 
(
	ProjectID VARCHAR(40) NOT NULL, 
	LoadIndex SMALLINT NOT NULL, 
	LoadID VARCHAR(40) NOT NULL, 
	GroupNumber SMALLINT NOT NULL,
	StepName TEXT NOT NULL,
	RunTime SMALLINT NOT NULL,
	LoadValue REAL NOT NULL,
	Remark TEXT
);

CREATE TABLE IF NOT EXISTS Loads_Select 
(
	ProjectID VARCHAR(40) NOT NULL, 
	LoadIndex SMALLINT NOT NULL, 
	LoadID VARCHAR(40) NOT NULL, 
	GroupNumber SMALLINT NOT NULL,
	StepName TEXT NOT NULL,
	RunTime SMALLINT NOT NULL,
	LoadValue REAL NOT NULL,
	Remark TEXT
);
```