# 主要记录在Linux下ftp的搭建和使用

* 注意：ftp命令只能每次只能上传简单的单个文件，不能传输目录！
* 如果想要在ftp上传输复杂目录，要么用代码自己逐层遍历然后在ftp上建立对应目录然后再上传文件
* 要么就打包后用压缩包传输，要么就使用scp命令直接复制。


## ftp的搭建过程(以ubuntu操作系统为例)：
```
一般在各种linux的发行版中，最常用的ftp软件是vsftpd，另外还有tftp
'apt-get update'更新一下软件源
'apt-get install vsftpd'安装vsftpd软件
'service vsftpd restart'重启一下vsftpd的服务
'service vsftpd status'查看服务状态是否开启
新建一个用户ftpuser
'vim /etc/vsftpd.conf'编辑配置文件，向文件中添加：
"userlist_deny=NO ，userlist_enable=YES ，userlist_file=/etc/allowed_users，seccomp_sandbox=NO"，另外设置文件中的"local_enable=YES"
'vim /etc/allowed_users'新建文件并向其中写入刚才的用户名ftpuser
'vim /etc/ftpusers'查看文件中是否有ftpuser,如果有就删除
```


## ftp配置文件相关:
```
ftp的配置文件主要有三个，位于/etc目录下，分别是：
1.ftpusers文件用来指定哪些用户不能访问ftp服务器，相当于黑名单
2.user_list文件用来作为白名单或黑名单，具体取决于userlist_enable和userlist_deny的值
其中设置userlist_file=/etc/allowed_users
3.vsftpd.conf是vsftpd的主配置文件，其中：
anonymous_enable=NO             关闭匿名登录
local_enable=YES        允许本地用户登录
write_enable=YES        启用后可以允许用户向ftp中上传文件
local_umask=022             本地用户创建文件的 umask 值
dirmessage_enable=YES           当用户第一次进入新目录时显示提示消息
xferlog_enable=YES      一个存有详细的上传和下载信息的日志文件
connect_from_port_20=YES        在服务器上针对 PORT 类型的连接使用端口 20（FTP 数据）
xferlog_std_format=YES          保持标准日志文件格式
listen=NO               阻止 vsftpd 在独立模式下运行
listen_ipv6=YES             vsftpd 将监听 ipv6 而不是 IPv4，你可以根据你的网络情况设置
pam_service_name=vsftpd         vsftpd 将使用的 PAM 验证设备的名字
userlist_enable=YES             允许 vsftpd 加载用户名字列表
tcp_wrappers=YES        打开 tcp 包装器
userlist_enable=YES       启用userlist列表
userlist_deny=YES         userlist列表成为黑名单（反之是白名单）
```


## ftp的登录上传下载相关命令：
```
'ftp hostip/hostname'或'ftp username@hostip/hostname' 登录ftp
注意：大部分地方登陆都是'ftp ip:port',但也碰到过'ftp ip port',即中间是空格的情况！
之后需要输入登陆账户的用户名和密码，登陆成功后会返回‘230 Login successful.’
登入ftp后，就会进入以'ftp>'开头的ftp命令行界面
在ftp命令行内部也可以直接使用'ls'/'mkdir'等linux命令
'close'或'disconnect'断开与远程服务器的ftp连接，但是还停留在ftp命令行内部，可以用open命令再进入
'open hostip在ftp命令行内部再次连接指定远程服务器，需要输入用户名密码
'lcd dirpath'在从ftp上下载文件之前要先用lcd命令指定本地接收文件的目录位置
'get filename'从ftp上下载指定的文件
注意：使用get命令下载时，当前的工作目录要是文件所在的目录，即不能用get path1/path2/file这种方式，否则会报错找不到文件
'mget *.txt'下载多个文件，可以配合通配符使用
'put filename'向ftp中上传文件，文件不在当前目录下时要使用绝对路径
'mput *.txt'上传多个文件，可以配合通配符使用
'delete filename'删除ftp上的文件
'quit'或'exit'或'bye'或'!'退出ftp命令行
备注：使用mput/mget可以传输当前目录中的所有文件(不包含目录)，但每个文件都会提示确认，使用'prompt off'可以关掉确认交互
'rpm -qa | grep ftp'查看服务器上是否安装了ftp服务
```


## 关于ftp方式上传和wget方式下载时的覆盖问题：
```
如果要下载/上传的文件在目标路径已经存在，则会进行自动覆盖；
即多次重复执行上传下载操作，也不会产生任何报错，新的数据会自动覆盖旧的数据；
注意：如果要传输的不是文件而是目录，那么ftp上新增和修改的文件会增加到本地，
但ftp上删除的文件在覆盖后本地的对应文件依然会存在；
```