# windows常用命令

## win+R中使用的命令
* 打开远程桌面
'mstsc'  
* 打开注册表
'regedit'  
* 打开本地组策略管理器 
'gpedit.msc'  


## cmd中使用的命令
**说明**
1. cmd中的执行过程可以输出到本地文件  
例如，'ping www.baidu.com -t > E:\ping.txt'  
2. cmd中文件的路径必须使用'\'，不能使用'/'，否则报错命令语法不正确  
* 查看ip地址
'ipconfig'  
* 查看MAC地址等详细网络信息
'ipconfig /all'  
* 查看系统信息 
'systeminfo'  
* 进入D盘
'd:'（注意切换盘符无需cd，使用'cd d:'无法进入到D盘目录下）  
* 进入某个目录
'cd 目录名'  
* 展示当前路径下所有文件
'dir'  
* 拷贝文件
'copy old_path new_path'  
* 删除文件
'del file_path'  
* 删除空目录
'rd folder_path'  
* 删除目录及其子目录和文件
'deltree folder_path'  
