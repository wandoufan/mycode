# windows脚本
备注：可以参考linux脚本中的相关内容  

## 注意事项
1. 要实现开机自动执行脚本，把脚本文件放到下面路径下即可
```
C:\Windows\System32\GroupPolicy\Machine\Scripts\Startup
```

## 脚本中可以使用的变量
```
@file    - 返回文件名
@fname   - 返回不带扩展名的文件名
@ext     - 只返回文件的扩展名
@path    - 返回文件的完整路径
@relpath - 返回文件的相对路径
@isdir   - 如果文件类型是目录，返回 "TRUE"
           如果是文件，返回 "FALSE"
@fsize   - 以字节为单位返回文件大小
@fdate   - 返回文件上一次修改的日期
@ftime   - 返回文件上一次修改的时间
```


## 用户和用户组相关的命令
> https://www.jb51.net/article/24733.htm
> https://www.rootop.org/pages/4246.html
备注：一般要用管理员权限去打开运行cmd，然后才能执行用户和用户组相关的命令  
1. 创建用户
```
# 设置用户名、用户密码、用户描述，设置账户永不过期
command = "net user %s %s /expires:never /FULLNAME:%s /comment:%s /add" %(user_id, user_password, user_name, user_describe)
os.system(command)
# 设置密码永不过期
command = "wmic useraccount where \"name='%s'\" set passwordexpires=false"%(user_id)
os.system(command)
```
2. 创建用户组
```
# 设置用户组名，用户组描述
command = "net localgroup %s /comment:%s /add" %(group_name, group_describe)
os.system(command)
```
3. 添加用户到用户组
```
# 向用户组内添加用户
command = "net localgroup %s %s /add" %(group_name, user_id)
os.system(command)
```


## 设置文件夹权限的icacls命令
> https://www.cnblogs.com/zhanglinfan/articles/5492964.html
**注意事项**
1. 设置之前要保证磁盘系统为NTFS格式  
2. 一般创建出的文件夹默认Users用户组都有访问权限，但无法直接删除Users组  
需要先设置'属性-安全-高级安全-禁用继承'或'/inheritance:d'，之后才能删除User组  
creator owner用户组同理，但creator owner不知道怎么用脚本去删除  
3. 不推荐使用cacls，推荐使用改进版icacls，在cmd中输入icacls可以显示所有参数  
4. 设置权限时默认只针对当前文件夹，如果要应用到子文件和子文件夹，要在权限中加上(OI)(CI)  
例如，'/grant ftp_group1:(OI)(CI)(RX,W)'  
5. 设置多个权限时，权限之间可能会有冲突，系统会以较大的权限为准  
例如，同时设置M，R，W权限时，R和W设置无效，只有M权限生效  
**perm权限掩码**
perm 是权限掩码，可以两种格式之一指定:  
1. 简单权限序列
N - 无访问权限  
F - 完全访问权限  
M - 修改权限  
RX - 读取和执行权限  
R - 只读权限  
W - 只写权限  
D - 删除权限  
2. 在括号中以逗号分隔的特定权限列表
DE - 删除  
RC - 读取控制  
WDAC - 写入DAC  
WO - 写入所有者  
S - 同步  
AS - 访问系统安全性  
MA - 允许的最大值  
GR - 一般性读取  
GW - 一般性写入  
GE - 一般性执行  
GA - 全为一般性  
RD - 读取数据/列出目录  
WD - 写入数据/添加文件  
AD - 附加数据/添加子目录  
REA - 读取扩展属性  
WEA - 写入扩展属性  
X - 执行/遍历  
DC - 删除子项  
RA - 读取属性  
WA - 写入属性  
**常用命令**
1. 查看文件夹的继承权限
备注：这里的权限和'文件属性-安全'中的权限一致  
```
icacls E:\share_test\1718-001
输出结果：
E:\share_test\1718-001 XYF-PC\XYF:(OI)(CI)(F)
                       BUILTIN\Administrators:(OI)(CI)(F)
                       NT AUTHORITY\SYSTEM:(OI)(CI)(F)
```
(OI)表示：对象继承  
(CI)表示：容器继承  
(IO)表示：仅继承  
(NP)表示：不传播继承  
(I)表示：从父容器继承的权限  
2. 设置文件夹的继承权限
备注：这里的继承关系可以在'文件属性-安全-高级'中进行查看  
备注：对于目录，继承到的权限高于自己设置的权限  
```
icacls E:\share_test\1718-001 /inheritance:e|d|r
```
e参数：启用继承(可以继承上一级的用户权限)  
d参数：禁用继承并复制ACE(复制保留当前继承的用户权限，然后断开继承关系)  
备注：对于d参数，当前继承的用户权限会被转化为不是继承的用户权限，然后保留下来  
r参数：删除所有继承的ACE(清空当前继承的用户权限，然后断开继承关系)  
备注：对于r参数，不是继承的用户权限不会被删除  
3. 设置用户或用户组对文件夹的访问权限
```
# 标准格式，其中perm代表权限掩码，权限用()括起来
icacls E:\share_test\1718-001 /grant[:r] Sid:perm
# 按照用户或用户组的名称设置权限
icacls E:\share_test\1718-001 /grant 1718-001:(D)
# 按照用户或用户组的Sid设置权限
icacls E:\share_test\1718-001 /grant *S-1-1-0:(D)
# 一次设置多个权限，多个权限间用','隔开
icacls E:\share_test\1718-001 /grant 1718-001:(R,W)
```
如果使用r参数，这些权限将替换以前授予的所有显式权限  
如果不使用r参数，这些权限将添加到以前授予的所有显式权限  
4. 删除用户或用户组对文件夹的访问权限
备注：deny也表示显示地拒绝用户有该访问权限  
```
# 标准格式，其中perm代表权限掩码，权限用()括起来
icacls E:\share_test\1718-001 /deny Sid:perm
# 删除1718-001用户组队文件夹的S权限
icacls E:\share_test\1718-001 /deny 1718-001:(S)
执行后的结果：
E:\share_test\1718-001 XYF-PC\1718-001:(DENY)(S)
                       XYF-PC\1718-001:(S,X)
                       XYF-PC\XYF:(I)(OI)(CI)(F)
                       BUILTIN\Administrators:(I)(OI)(CI)(F)
                       NT AUTHORITY\SYSTEM:(I)(OI)(CI)(F)
```
5. 删除用户或用户组对文件夹的所有访问权限
```
# 标准格式，如果不写参数，默认为g参数
icacls E:\share_test\1718-001 /remove[:[g|d]] Sid
# 删除1718-001用户组对文件夹的权限
icacls E:\share_test\1718-001 /remove 1718-001
```
如果使用g参数，将删除授予该Sid的所有权限（默认为g参数）  
如果使用d参数，将删除拒绝该Sid的所有权限（即通过deny设置的权限）  


## 文件夹共享的net share命令
**注意事项**
1. 一般先设置文件夹权限，再设置文件夹共享
2. 一般要用管理员权限去打开运行cmd，然后才能执行文件夹共享相关的命令
3. 可以用'net share /?'来查看命令的所有参数
4. 在共享文件夹中删除文件时，文件会不经过回收站而直接彻底删除
保险起见，要么禁止其他用户的删除权限，要么对共享文件夹设置备份  
如果数据已经被删除，只能通过数据恢复软件来尝试恢复了  
5. 在"网络共享中心-更改高级共享设置-密码保护的共享"中可以设置访问共享文件夹是否需要输入密码
备注：默认设置是需要输入密码的，所以需要先给计算机账户设置密码  
**常用命令**
1. 查看当前电脑的所有共享文件夹及其共享名
```
net share
```
备注：也可以通过'计算机管理-系统工具-共享文件夹-共享'进行查看和关闭共享  
2. 设置指定文件夹为共享文件夹
```
将E:\share_test文件夹共享为myshare
net share myshare=E:\share_test /remark:"this is remark"
```
sharename参数：表示共享的名字  
drive:path参数：共享文件夹的绝对路径  
/users:number参数：同时访问共享目录的最大用户数  
/unlimited参数：同时访问共享目录的用户数不受限制  
/remark:"text"参数：为共享文件夹设置注释(没找到在哪看注释)  
3. 将文件夹共享给指定的用户或用户组，并设置其权限
注意：如果在共享时不指定用户权限，则默认Everyone用户组有可读权限  
```
标准格式，设置用户权限
net share myshare=E:\share_test /grant:user,[read|change|full]
将文件夹共享，并且设置group1组的用户对共享文件夹有更改和读取权限
net share myshare=E:\share_test /grant:group1,change
```
user参数：指定授权用户或用户组的名称  
read参数：表示只读权限  
change参数：表示更改和读取权限  
full参数：表示完全控制权限  
4. 设置指定文件夹取消共享  
可以根据共享名或共享路径来取消共享  
```
net share sharename /delete
net share E:\share_test /delete
```


## windows数据备份的wbadmin命令
使用windows server backup进行备份时无法设置备份副本的个数  
可以用wbadmin命令来删除多余的备份副本  
**常用命令**
1. 查看当前电脑中所有的备份
```
可以查看所有备份的时间和版本号
wbadmin get versions
```
2. 删除电脑中的备份
windows server backup的备份文件不是按每次备份单独存为一个文件  
而是把所有备份都叠加为一个文件，文件名显示为最新备份的版本号  
因此无法通过删除文件夹来删除多余备份，只能用wbadmin命令去删除  
```
指定保留最新的3个备份，多余备份都删除
wbadmin delete backup -keepversions:3
删除所有备份
wbadmin delete backup -keepversions:0
删除最早的备份
wbadmin delete backup -deleteOldest
删除指定版本的备份
wbadmin delete backup -version:版本号
```


## 遍历文件并执行操作的forfiles命令
**用法解析**
```
forfiles [/P pathname] [/M searchmask] [/S]
         [/C command] [/D [+ | -] {yyyy/MM/dd | dd}]
```
可以根据文件名、文件日期等属性对文件进行更精准的操作  
1. /p 指定了搜索的路径，默认是当前工作目录  
2. /m 指定搜索的正则表达式，默认为通配符*  
例如\*.log可以删除所有后缀为.log的文件  
3. /s 递归到子目录
4. /c 对每个找到的文件执行的命令，如果是cmd命令，则命令体必须以'cmd /c'开头  
命令体部分要用双引号""括起来，默认为"cmd /c echo @file"  
5. /d 指定一个日期或天数，用于比较文件的最后修改日期是否符合条件  
'+'表示大于等于，即n天以前的文件，默认为'+'  
'-'表示小于等于，即n天以内的文件  
文件日期可以直接用'yyyy/MM/dd'指定到某一天，也可以用'dd'表示距离现在dd天  
**使用示例**
1. 删除在C盘backup目录下最后修改日期在10天前的文件
```
forfiles /p "c:\backup" /d -10 /c "cmd /c echo deleting @file ... && del /f @path"
```
