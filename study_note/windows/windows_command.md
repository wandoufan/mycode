# windows常用命令

## win+R中使用的命令
* 打开远程桌面
'mstsc'  
* 打开注册表
'regedit'  
* 打开本地组策略管理器 
'gpedit.msc'  


## 在cmd中使用命令
1. cmd中的执行过程可以输出到本地文件  
例如，'ping www.baidu.com -t > E:\ping.txt'  
2. cmd中文件的路径必须使用'\'，不能使用'/'，否则报错命令语法不正确  
3. 可以把命令直接写入一个txt文本中，然后后缀改为.bat，就可以直接执行


## 常用命令
### ping
1. ping www.baidu.com -t
一直发送数据包  
2. ping www.baidu.com -l 1000
发送大小为1000字节的数据包  
备注：ping发送数据包默认为32字节，最大可以指定为65500字节  

### tracert
1. tracert ip或网址
查询从本机到目标IP所经过的路由器及其IP地址  
从左到右的5条信息分别代表了生存时间（每途经一个路由器结点自增1）、三次发送的ICMP包返回时间（共计3个，单位为毫秒ms）和途经路由器的IP地址（如果有主机名，还会包含主机名）  
其中带有星号的信息表示该次ICMP包返回时间超时  

### telnet
备注：使用telnet命令前要先安装和开启telnet服务  
1. telnet ip port
查看某个IP的某个端口是否可以访问  

### netstat
1. netstat
查看本机各个端口的网络连接情况  

### ipconfig
1. ipconfig
查看ip地址  
2. ipconfig /all
查看MAC地址等详细网络信息  

### systeminfo
1. systeminfo
查看系统信息，包括系统安装时间、开机时间、补丁包安装情况等  

### cd
1. cd 目录名
进入某个目录作为工作目录  
2. d:
进入D盘  
注意：切换盘符无需cd，使用'cd d:'无法进入到D盘目录下  

### dir
1. dir
展示当前路径下所有文件

### tree
1. tree
* 以树状展示当前目录所有文件夹  
2. tree 目录名
以树状展示指定目录所有文件夹（不包含文件）  
3. tree /f 目录名
以树状展示指定目录所有文件夹和文件  

### copy
1. copy old_path new_path
拷贝文件  

### del
1. del file_path
删除文件  

### rd
1. rd folder_path
删除空目录  

### deltree
1. deltree folder_path
删除目录及其子目录和文件  

### regsvr32
1. regsvr32 file_path
注册dll或ocx  
2. regsvr32 /u file_path
取消注册dll或ocx  