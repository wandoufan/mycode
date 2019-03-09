# 主要记录一些Linux的命令：

* Linux命令大全：

> http://www.runoob.com/linux/linux-command-manual.html


## 相关快捷键：
注意：在Linux中ctrl+s是锁屏的快捷键，使用xshell连接Linux时如果手误按ctrl+s会造成vim卡死的假象，ctrl+q退出锁屏即可
* 'ctrl+insert'  复制
* 'shift+insert'  粘贴
* 'ctrl+c'  停止当前运行的程序
* 'ctrl+d'  注销当前账户


## 系统运行等级相关命令：
* 'runlevel'  查看当前的运行等级
* 'ctrl+Alt+F1~F6'  切换文字界面登陆tt1~tt6终端(level 3)
* 'ctrl+Alt+F7'  切换到图像界面(level 5)
* 'startx'  在文件界面切换到图形界面(前提是有X windows系统)
* 'init'  切换执行等级  
系统运行等级(run level)总共有7级：  
* run level 0:关机
* run level 3:纯命令行模式
* run level 5:图形界面模式
* run level 6:重启


## 系统关机相关命令：
* 'logoff'  注销
* 'exit'  注销
* 'shutdown'  关机  
-h now  立即关机  
-h 10:30  指定时间点关机  
-h +10  过指定时间段之后关机  
-r now  立即重启  
* 'poweroff'  关机
* 'init 0'  关机
* 'reboot'  重启


## 系统基本命令：
* 'date +[%Y/%m/%d %H:%M]'  显示时间日期
* 'cal'  显示日历
* 'bc'  调用计算器
* 'md5sum 文件名'  查看计算和检验MD5信息签名。
* 'man 命令'  查看命令的操作说明(manual)
* 'help 命令'或'命令 -help'  查看Linux内置命令的帮助
* 'info 命令'  查看命令的详细信息
* 'type 命令'  查看命令是否为bash的内置命令(file表示外部命令，alias表示是别的命令的别名，builtin表示内置命令)
* 'sync'  把内存中的数据写入硬盘中保存，常用于关机前操作
* 'file filename'  查看文件的类型，即属于ASCII文件或是data文件或是binary文件或是directory
* 'alias'  查看当前设置的所有命令别名
* 'alias 命令别名='原命令''  设置命令别名，例如:'alias lm='ls -l|more''
* 注意：设置的别名重启后就失效了，要保持永久有效需要把命令写入~/.bashrc文件中
* 'unalias 命令别名'  取消历史设置的命令别名
* 'history'  查看bash中输入过的所有命令  
n  n为数字，列出最近输入过的n条命令，注意没有横杠-  
-c  清除shell中所有的历史记录  
* 'clear'  清除屏幕上的信息


## 环境变量相关命令：
* 'env'列出所有的环境变量及其对应的值
* 'echo $PATH'  查询环境变量路径  
注意：把一个命令(文件)放到环境变量的路径下，就可以实现在服务器任意路径下输入命令就可以执行命令  
添加新的环境变量路径方法一：  
* 'export PATH=new_path:$PATH'  但关闭窗口后下次再登录时新路径就失效了  
添加新的环境变量路径方法二：  
* 'vim /etc/profile'打开全局配置文件或'vim ~/.bash_profile'打开用户本地配置文件
* 'export PATH=new_path:$PATH'  在文档最后添加新路径
* 'source /etc/profile'或'source ~/.bash_profile'  使配置文件重新生效
注意：Linux中常有报错:command not found(实际命令已经安装)，一般都是因为命令没有添加到环境变量


## 查看系统基本信息：
* 'uname -a'  显示机器名，操作系统和内核的详细信息
* 'hostname'  显示或者设置当前系统的主机名
* 'cat /etc/issue'  查看Linux是什么操作系统(redhat/centos/ubuntu/fedora...)
* 'cat /proc/version'  查看Linux的版本号
* 'stat 文件名'  显示指定文件的详细信息，如大小，block，inode，硬链接，权限，创建时间，更改时间等
* 'uptime'  显示系统时间，系统运行时间，当前系统登录用户及负载情况
* 'locale -a'列出linux系统支持的所有语系


## 查看系统资源信息：
1.内存资源  
注意：linux中内存分为memory(物理内存)和swap(虚拟内存)，swap也称为交换区  
* 'cat /proc/meminfo'  查看系统内存使用情况，显示内存总量、已用量、剩余量

* 'free'  查看系统内存使用情况，显示内存总量、已用量、剩余量
-h  以人类易于读取的模式列出    
-m  以MB为单位显示内存(默认为KB)  
-t  显示内存总和信息  
示例：'free -ht'  

2.磁盘资源  
* 'df'  列出文件系统的整体磁盘使用量，显示磁盘总量、已用、可用、使用率、挂载点，与当前所在的工作目录无关
-h  以人类易于读取的模式列出  
-m  以MB为单位显示文件大小  
-i  以inode的数量来展示  
-a  列出所有具有0Blocks的文件系统  
注意：block(文件块)是系统读写文件的最小单位，若干个扇区组成一个block，一般为4kb大小  
注意：inode(索引节点)存储文件的元信息，如文件的创建者，创建日期，读写权限，链接数等  
示例：'df -h'  

* 'du 文件名'  列出当前工作目录下的文件和目录的大小  
-h  以人类易于读取的模式列出  
-m  以MB为单位显示文件大小  
-s  仅显示当前目录所有文件大小之和  
注意：文件名写通配符\*可以匹配当前目录下的文件和目录(不含子目录)，不写文件名先递归地显示出所有子目录的文件大小  
示例：'du -sh'  

3.进程信息  
* 'top'  实时显示出系统的内存、CPU、进程等详细信息，相当于windows进程管理器  
-d seconds  设置信息刷新周期  
-n number  设置刷新number次后自动退出(q键手动退出)  
-p pid  指定监控进程id来仅仅监控某个进程的状态  
-s  使top命令在安全模式中运行。这将去除交互命令所带来的潜在危险  
-i  使top不显示任何闲置或者僵死进程  
-c  显示整个命令行(默认只显示命令名)  
* top进程列表中各个字段的含义：  
PID  进程id号  
USER  进程所有者  
PR  进程优先级，即被CPU执行的先后顺序，值越小进程优先级越高  
NI  nice值，相当于修正优先级，范围在(-20~19)之间，负值表示高优先级，正值表示低优先级  
注意：进程真正的优先级 = PR(进程优先级) + NI(进程nice值)  
VIRT  进程使用的内存总量，单位kb，其中VIRT = SWAP + RES  
RES  进程使用的物理内存大小，单位kb  
SHR  共享内存大小，单位kb  
S  进程状态，其中D=不可中断的睡眠状态、R=运行、S=睡眠、T=跟踪/停止、Z=僵尸进程  
%CPU  上次更新到现在的CPU时间占用百分比  
注意：对于多核CPU的虚拟机，进程的CPU利用率可能超过100%  
%MEM  进程使用的物理内存百分比  
TIME+  进程累计使用的CPU时间总计  
COMMAND  进程名称，格式为(命令名/命令行)  
* top命令界面中一些常用操作：  
q  退出top命令界面  
M  按内存占用比对进程进行排序  
P  按CPU占用比对进程进行排序  
T  按时间占用比对进程进行排序  
W  将当前top的配置的文件写入./.toprc文件中  

* 'ps'  显示当前进程的状态，默认只显示部分进程信息  
-A  显示所有进程的信息  
-e  显示所有进程的信息
-aux 显示进程的详细信息  
示例：'ps -aux'  

* 'jobs'  查看后台进程
-l  列出进程的pid和进程号  
-p  只列出进程的pid  
-r  只列出正在运行的进程  
-s  只列出已经停止的进程  
注意：jobs命令只能查看当前窗口的后台进程，如果关闭了后台执行脚本的窗口，该命令就失效了  


## 进程相关的命令
* 'kill pid'  根据pid删除执行中的程序，进程的pid可以通过ps或jobs命令查看
-9  彻底杀死进程  
-KILL  强制杀死进程  
示例：'kill -9 PID'  杀掉指定PID对应的进程  

* 'nohup command &'  守护进程(no hang up)
使用了nohup后即使关闭了ssh连接(关掉xshell窗口)，进程还会继续执行(默认断开连接后进程也会停止)  注意：nohup命令守护的进程只能通过kill命令来杀死  
注意：nohup命令会在命令执行的目录下生成一个nohup.out文件用来记录进程执行的情况  
示例：'nohup python test.py &'  


## 查看文件目录相关的命令：
* 'ls'  列出当前目录下的目录和文件  
-l  列出目录和文件的详细信息  
-a  列出目录里的所有内容，包括以"."开头的隐藏文件  
-R  递归地列出当前目录下子目录的文件信息  
-h  以人类易于读取的模式列出  
注意：'ll'和'ls -l'一样，是简写形式  
示例：'ls -l | grep '^-' | wc -l'  显示当前目录下所有的文件个数  
示例：'ls -l | grep '^d' | wc -l'  显示当前目录下所有的目录个数  

* 'tree'  以树状结构列出当前路径或指定路径的文件，使用之前可能需要安装
-a  显示所有文件和目录  
-s  列出文件或目录的大小  
-p  列出文件或目录的权限  
-f  列出文件或目录的完整路径  
-d  仅列出目录，不显示文件  

* 'basename path'  获取路径中最后的文件名
* 'dirname path'  获取路径中除了文件名的路径


## 查看文件内容相关的命令：
* 'nano'  打开文本编辑器
* 'touch 文件名'  快速创建空的文件
* 'cat 文件名'  从第一行开始显示文件内容
* 'tac 文件名'  从最后一行开始显示文件内容
* 'nl 文件名'  显示内容的同时显示行号
* 'more 文件名'  一页一页的显示文件内容
* 'less 文件名'  可以往前翻页
* 'head 文件名'  只看文件前几行  
-n  仅列出前n行  
* 'tail 文件名'只看文件结尾几行  
-n  仅列出后n行  
* 'od 文件名'  以二进制方式读取文件
* 'wc 文件名'  查看文件的行数,英文字符数,所有字符数  
-l  仅列出行数  
-w  仅列出英文单字数  
-m  仅列出字符数  


## 文件和目录操作相关的命令：
* 'cd path'  切换到指定目录  
-  切换到刚才访问的上一个目录  
~  切换到用户的主目录  
..  切换到当前目录的上层目录  

* 'pwd'  显示当前工作目录  
-p  获取正确的路径，而不是链接文件的路径  

* 'mkdir dirname'  新建一个目录  
-m 777  创建文件时顺便设置文件权限  
-p  如果指定目录不存在就新建该目录，而不是报错  
示例：'mkdir -p a/b/c'一次性新建多层目录  

* 'rmdir dirname'  删除一个空目录  
-p  若该目录删除子目录后也变成了空目录，则将其一并删除  
示例：'rmdir -p a/b'  

* 'cp 源文件/目录 目标路径'  复制文件或目录到指定路径  
-i  若目标文件已存在，询问是否要覆盖  
-r  递归持续复制，用于复制目录  
-u  仅当源文件更新时才覆盖  
示例：'cp -r /a/b /c'  

* 'rm 文件/目录'  删除文件或目录  
-f  强制删除，不再询问  
-r  递归删除非空的目录  
-i  删除前询问  

* 'mv 源文件/目录 目标路径'  移动文件或目录到指定路径或给文件重命名  
-f  强制覆盖  
-i  若目标文件存在询问是否覆盖  
-u  仅当源文件更新时才覆盖  

* 'rename'  对批量文件进行重命名


## 权限相关的命令：
* 'chown [用户名:用户组名] filename'  将文件的拥有者改为指定的用户或用户组
-R  递归地对目录下的子目录进行相同的设置  
示例：'chown user1:user1_group /a'  将目录下的a文件拥有者设置为user1，拥有组设置为user1_group
注意：指定用户时可以用用户名或用户id，指定用户组时也可以用用户组名或用户组id  

* 'chgrp [-R] 用户组名 dirname/filename'  改变文件或目录所属的用户组
-R  递归地对目录下的子目录进行相同的设置  
示例：'chgrp user1_group /a'  将目录下的a文件的用户组设置为user1_group

* 'chmod [ugoa] [+-=] [rwx] dirname/filename'  修改设置文件的拥有者、用户组、其他用户对应的权限
-R  递归地对目录下的子目录进行相同的权限设置  
u  user，表示文件拥有者  
g  group，表示与文件拥有者同一群组的用户  
o  others，表示非同组的其他用户  
a  all，表示user、group、others这三类用户合起来  
+  增加权限  
-  删除权限  
=  设置权限  
r  表示可以读取  
w  表示可以写入  
x  表示可以执行  
注意：修改或设置权限可以采用数字法(r:4,w:2,x:1)或字母法(rwx)  
示例：'chmod 764 /a'  设置目录下a文件的权限为user(rwx)、group(rw)、others(r)  
示例：'chmod a+x /a'  给目录下a文件的user、group、others都增加x权限

* 'umask'  查看数字形态的创建文件时的默认权限值  
number  修改设置默认权限值  
注意：root用户默认为0022，一般用户默认为0002，777减去输出的后三位数值即为实际的权限值  

* 'chattr filename/dirname'  设置文件的隐藏属性，chattr命令只有在Ext2/Ext3文件系统上有效
+  增加某个参数，其他不变  
-  删除某个参数，其他不变  
=  仅设置后面接的参数  
a  设置a参数后文件只能增加数据，不能删除或修改原有数据，只有root才能设置这个属性，适用于日志类文件  
i  设置i参数后文件不能被删除或改名，设置连接也无法写入或添加数据，只有root才能设置这个属性  
示例：'chattr +i /a'  给目录下的a文件增加i属性  

* 'lsattr filename/dirname'  查看文件的隐藏属性  
-a  显示所有文件和目录的隐藏属性，包括隐藏文件  
-R  递归地将目录下的子目录文件的隐藏属性也显示出来  


## 基础网络操作相关的命令：
* 'ifconfig'  查看、配置、启用或禁用网络接口，注意不是ipconfig
示例：'ifconfig eth0 up'  启动网卡eth0  
示例：'ifconfig eth0 down'  关闭网卡eth0  
示例：'ifconfig eth0 192.168.0.5'  给网卡eht0设置ip  

* 'ping host_name/host_ip'  测试主机之间网络的连通性
-i seconds  设置发送数据包的时间间隔  
-s data  设置发送数据包的大小  
-c number 设置发送数据包的个数(默认一直发送)
示例：'ping www.baidu.com'

* 'netstat'  查看整个Linux系统的网络状态
-a  显示所有连线中的端口  
-p  显示正在使用端口的程序pid和程序名称  
-n  将域名信息转换为ip信息显示出来  
-c  持续的列出网络的状态  
-t  显示tcp协议的连线状况  
-u  显示udp协议的连线状况  
-l  仅显示处在监听状态的端口  
示例：'netstat -apn | grep port'  查看占用指定端口的进程以及进程的PID  
示例：'netstat -at'  查看所有的tcp端口  

* 'traceroute host_name/host_ip'  追踪路由
* 'route'  显示和设置linux系统的路由表
* 'nc'  设置路由器，扫描端口

* 'telnet host_name/host_ip'  使用TELNET协议远程登录到指定主机
示例：'telnet 192.168.0.5'  
注意：telnet因为采用明文传送报文，安全性不好，很多Linux服务器都不开放telnet服务  
* 'ssh username@host_ip'  使用SSH加密协议远程登录到指定主机


## 文本内容处理相关命令：
* 'grep 目标字符串 filename' 以行为单位分析信息，如果有符合条件的字符串，就将该行取出来
-c  计算找到目标字符串的次数  
-i  忽略大小写  
-n  输出行号  
-v  反向选择，即显示没有目标字符串的行  
示例：'grep hello \*.txt'  显示所有以txt为后缀的文件中所有包含'hello'字符串的行  
示例：'grep -i [a-z] test1.txt'  选取test1.txt中所有包含英文字母的行(正则匹配)  

* 'sed'  利用脚本来自动化编辑处理一个或多个文件

* "awk '{script}' filename"  用脚本(脚本要用引号括起来)来按行处理文本文件中的数据，具有复杂而强大的功能，常用来分割字符 
-F '分割符'  指定分割符(分割符要用引号括起来)，默认分割符为空格和制表符  
* awk中常见变量的含义：
$0  指脚本正在处理的当前行 
$1  指每行文本被分割后的第1个字段列   
$2  指每行文本被分割后的第2个字段列   
$n  指每行文本被分割后的第n个字段列   
NR  表示当前的行号，即是文本的第几行  
NF  表示当前行被分割后的列数  
示例："awk '{print $0}' b"  按行输出b文件中的内容，相当于cat  
示例："awk -F '3' '{print $2}' b"  将b文件中每行以3为分割符进行分割，并打印出每行被分割后的第2个字段列  
示例："awk -F '[(:)]' '{print $2}' b"  设置'('、 ':'、 ')'三个分割符  


## 文件查找相关的命令：
* 'which 命令'寻找执行文件(命令)的路径，-a:将PATH目录可以找到的所有命令都列出来，而不是只列第一个
* 注意：which默认是查找环境变量PATH内所规范的目录，如cd命令这种bash内置的命令就无法找到
* 'whereis filename/dirname'寻找特定文件（完整的文件名）
* 'locate keyword'给出文件的部分名称按照关键字查找，-i:忽略大小写的差异
* 注意：whereis和locate命令都是利用数据库来查询数据，并没有实际查询硬盘，所以速度很快
* 数据库默认每天执行一次更新回写，可能会有新创建的文件找不到的情况，可以用'updatedb'手动更新
* 'find [PATH] [option] [filename]'通过查找硬盘找到目标文件，find功能非常强大，参数很多，具体如下：
* 1.与时间有关的参数：-atime,-ctime,-mtime;以mtime为例：
* -mtime n:n为数字,列出在n天之前的那一天被更改过的文件
* -mtime +n:列出在n天之前(不含n天本身)被更改过的文件名
* -mtime -n:列出在n天之内(含n天本身)被更改过的文件
* <----(+n天之前)---<---(第n天)--->---(-n天之内)---->现在
* -newer filename：列出比指定文件还要新的文件
* 'find / -mtime 0'列出系统中24小时内被更改过的文件，0代表今天当前时间
* 'find /etc -newer /etc/password'列出在/etc目录下中比password文件还要新的文件
* 2.与用户或用户组相关的参数:
* -uid n:n是用户账户名对应的数字，即UID,存放在/etc/passwd
* -gid n:n是用户组名对应的数字，即GID,存放在/etc/group
* -user name:name是用户账户名
* -group name:name是用户组名
* -nouser:寻找文件的所有者不在/etc/passwd中的文件
* -nogroup:寻找文件的所有用户组不存在/etc/group中的文件
* 'find /home -user user':寻找/home下属于user用户的文件
* 'find / -nouser':寻找系统中不属于任何用户的文件(例如删除某个账户后，该账户之前创建的文件就属于无主文件)
* 3.在于文件权限及名称有关的参数：
* -name filename:查找文件名为filename的文件
* -size [+-]size:查找比指定尺寸还要大/小的文件，尺寸单位c代表byte,k代表kb
* 'find /home -size +50k'：查找/home中文件大于50kb的文件
* -type TYPE:查找指定类型的文件，类型有一般文件(f),设备文件(b,c),目录(d),连接文件(l),socket(s),FIFO(p)
* -perm mode:查找文件权限刚好等于mode的文件，mode为权限属性，如777
* -perm -mode:查找文件权限包括全部mode权限的文件
* -perm +mode:查找文件权限包含任一mode权限的文件
* 'find / -name passwd':查找系统中文件名为passwd的所有文件
* 'find /var -type s':查找/var目录中类型为socket的所有文件


## 文件传输相关的命令：
* wget命令可以通过URL地址下载数据，详见linux_wget文档
* ftp命令可以实现本地和ftp服务器之间的文件传输，详见linux_ftp文档
* 在xshell中安装Xftp软件后可以通过直接拖动来传输文件
* 注意：使用rz/sz等传输命令前可能要先安装
* 注意：需要使用SecureCRT或者Xshell等客户端工具连接Linux,在客户端上运行rz/sz命令
* 'rz -be'弹出文件选择窗口从Windows上向linux中上传文件，常用-be参数
* -a:以文本方式传输，确定传输的文件是文本格式时可以用
* -b:以二进制方式传输
* -e:对控制字符进行转义，可以保证文件传输正确
* 'sz filename'从Linux中下载文件到windows中
* 'scp'即secure copy，用于不同主机之间复制文件
* 'scp [参数] [原路径] [目标路径]'scp是secure copy的缩写, scp是linux系统下基于ssh登陆进行安全的远程文件拷贝命令
* -r:递归的复制整个目录
* -v:详细方式显示输出
* -B:使用批处理模式，传输过程中不询问
* -P:指定传输数据用到的端口号，注意是大写
* 1.从本地拷贝文件到远程
* 'scp local_file/local_dir username@remote_ip:remote_file/remote_dir'后边只需要输入密码
* 'scp local_file/local_dir remote_ip:remote_file/remote_dir'后边需要输入用户名和密码
* 2.从远程拷贝文件到本地
* 'scp username@remote_ip:remote_file/remote_dir local_file/local_dir'后边只需要输入密码
* 'scp remote_ip:remote_file/remote_dir local_file/local_dir'后边需要输入用户名和密码
* 示例：'scp -r -P 8080 /root/ftptest/abc user@192.168.109.133:/home/user/ftptest'


## 与解压缩相关的命令：
* 'gzip filename'新建*.gz格式的压缩文件(对象只能是文件不能是目录)，应用最广泛，可以解开大多数格式压缩文件
* -d:解开压缩文件,-v:显示压缩比等信息,-k:压缩后保留原文件
* 默认状态下生成压缩文件后原文件会被删除，gzip生成的文件在windows中可以被rar软件解压缩
* 'zcat *.gz'不用解压缩，直接读出*.gz格式的文本文件的内容
* 'bzip2 filename'新建*.bz2格式的压缩文件(对象只能是文件不能是目录)，拥有更好的压缩比
* -d:解开压缩文件,-k:压缩后保留原文件,-z:新建压缩文件(可以不写),-v:显示压缩比等信息
* 'bzcat *.bz2'不用解压缩，直接读出*.bz2格式的文本文件的内容
* tar命令功能强大，可以将多个文件或目录打包成一个大文件，并使用gzip/bzip2进行压缩
* 'tar [-j|-z] [cv] [-f new_tar_filename] filename'打包与压缩,其中filename是要被压缩的文件
* 'tar [-j|-z] [tv] [-f new_tar_filename]'查看压缩包包含的文件名
* 'tar [-j|-z] [xv] [-f new_tar_filename] [-C 目录]'解压缩
* -j:通过bzip2方式进行解压缩，文件格式为*.tar.bz2
* -z:通过gzip方式进行解压缩，文件格式为*.tar.gz(更常用)
* -c:新建打包文件
* -x:解开打包文件或者压缩文件
* -t:查看打包文件包含的文件名
* -v:在解压缩的过程中，显示正在处理的文件名
* -f new_tar_filename：f参数指定生成的压缩包文件的名字，如test.tar.gz
* -C 目录：在解开压缩时指定解压缩的路径
* 注意：-c,-t,-x三个参数不能同时出现在一个命令里
* 'zip -r new_filename.zip filename'指定文件/目录生成*.zip格式的文件
* -r:递归的将目标目录下的所有文件和子目录都打包压缩，如果没有这个参数只会压缩一个空的目标目录！
* 'zip -r new_filename.zip *'将当前工作目录下的所有文件打包(解压开就是目录下的所有东西而不是目录)
* 'zip -r b.zip a test.txt'将a目录和test.txt文本文件合并压缩为一个b.zip压缩包
* 'unzip *.zip -d path'把*.zip格式的文件解压
* -d path：指定文件的解压路径，不加该参数也可以，默认会解压到当前工作目录
* -v:不用解压缩，直接查看*.zip压缩包中的文件
* -t:验证压缩包中文件是否完整，是否有错
* 注意：rar命令可能需要安装才能使用，命令中的参数没有横杠-
* 'rar a new_filename.rar filename'指定文件生成*.rar格式的文件
* 'unrar e *.rar'把*.rar格式的文件解压


## 用户账户管理相关的命令：
* 'useradd username'添加新用户
* -m:自动创建用户的登录目录，注意必须加上该参数，否则创建的新用户在/home下没有用户目录
* -d path:指定用户目录的路径，默认为/home/username
* -u uid:指定UID，0~499默认是保留给系统用户账号使用的，所以该值必须大于499
* -g groups:指定用户所属的群组，值为GID，默认为100，即users
* -e:指定账号的失效日期，日期格式为MM/DD/YY，例如06/30/12,默认为永久有效
* -f:指定密码过期多少天后禁用账户，如果为0账号立即被停用，如果为-1则账号一直可用，默认值为-1
* -s:指定用户登入后所使用的shell,默认值为/bin/bash
* 'usermod username'修改系统已经存在的用户的属性
* 'userdel username'删除用户
* 'groupadd'新创建建用户组
* -g gid:指定新建工作组的GID
* -r:创建系统工作组，系统工作组的组ID小于500
* 'passwd username'修改或初次设置用户密码，注意不是password
* 'chage'修改用户密码有效期限等属性
* 'id'查看用户的uid,gid及归属的用户组
* 'su - username' 切换当前用户
* 'sudo'以root身份执行事先在sudoers文件允许过的命令，如果没有提前允许，需要手动输入密码
* 'who'显示当前登录用户的信息
* 'users'显示当前所有登录用户的用户列表
* 用root账户登录系统后命令提示符是#
* 用普通账户登录系统后命令提示符是$




## 可以作为管道命令的一些命令:
* 管道命令"|"中仅能处理前一个命令传递过来的正确信息(stdout)，不能直接处理错误信息(stderr)
* 每个管道后边接的第一个数据必须是能接受标准输入(stdin)的命令，例如：cat ,less等，另外例如：ls,cp,mv就不是管道命令
* 在管道命令中stdin和stdout可以用减号'-'来代替
* 'cut file/stdin' 以行为单位选取信息，将同一行的数据进行分解后取出需要的部分，常用于log日志文件分析提取等地方
* -d:后面接上分割字符，与-f一起使用
* -f:依靠-d的分割字符将信息切割成数段，-f表示取出其中的第几段
* -c:以字符的单位取出固定的字符区间
* 'echo $PATH | cut -d ':' -f 3,5' 以':'为分隔符分割环境变量，并取出其中的第三和第五段
* 'cat test1.txt | cut -d ' ' -f 3' 以空格为分隔符分割test1.txt，并取出其中的第三段
* 'cat test1.txt | cut -c 5-12' 选取出test1.txt中的第五个到第十二个字符
* 'cat test1.txt | cut -c 5-' 选取出test1.txt中的第五个到最后一个字符
* 'sort file/stdin' 给目标文件或接收到的标准输入排序
* -f:忽略大小写
* -b:忽略最前面的空格
* -n:以纯数字为标准排序(默认以文字类型排序)
* -r:反向排序
* -u:相同的数据仅出现一行代表，相当于去重
* -t:后边接分割符
* -k:后边接数字，表示分割后的第几个区间
* 'cat test1.txt | sort -f' 把test1.txt中的每一行按首字母进行排序后显示，注意原文件的数据顺序不会改变
* 'uniq file/stdin' 给目标文件或接收到的标准输入显示时去除重复
* -i:忽略大小写
* -c:给每行的重复数计数
* 'cat test1.txt | uniq -c' 把test1.txt中的重复行去除后显示
* 'wc file/stdin' 给目标文件或接收到的标准输入显示行数，字数等详细信息
* -l:仅列出行数
* -w:仅列出英文单字数
* -m:仅列出字符数
* 'cat test1.txt | wc' 列出test1.txt中的字符数等信息
* 'tee filename'表示双向重定向，既把数据都输入filename文件中，又在屏幕上显示出结果来
* -a:以追加的方式把数据加入filename中
* 'ls -l | tee filename' 把ls -l命令的结果显示出来并写入filename中
* 'tr' 用来删除或替换字符串
* -d:后边接目标字符串，删除目标字符串
* -s:后边接旧字符串和新字符串，替换指定字符串
* 'cat test1.txt | tr '[a-z]' '[A-Z]'' 把输出的test1.txt中的小写都替换为大写，注意原文件的大小写不会变
* 'join file1 file2' 把两个文件当中有相同数据的那一行加在一起，注意文件被join使用前要先sort排序处理
* 'paste file1 file2' 把两个文件中每行的内容直接加起来，中间用[tab]键隔开
* 'expand filename' 把文件中的[tab]键转换成空格
* 'split filename prefix' 把大的file文件切割成小的文件，其中prefix代表切割文件的前导文字
* -b:后边接要切割成的大小，单位为b,k,m
* -l:按行数来切割


## 变量操作相关的命令：
* 'read 变量名'读取来自键盘输入的变量，可以实现与用户的交互
* -p:后边接给用户的提示符，例如'read -p 'input your name:' username'
* -t:后边接等待用户输入的秒数
* 'declare 变量名'/'typeset 变量名'声明变量的类型
* -a:设置变量为数组类型(array),数组设置方式为'array[index]=content',显示为'echo "${array[1]},${array[2]}"'
* -i:设置变量为整数类型(integer)
* -x:设置变量为环境变量/全局变量，等同export
* +x:把环境变量变为自定义变量，等同export的逆操作
* -r:设置变量为readonly,该类型不可以被更改内容，也不能被重设
* -p:查看变量当前的数据类型和数值
* 'export 变量名'来把变量变成全局变量/环境变量,用于变量需要在其他子进程执行的情况
* 'unset 变量名' 取消变量 


## 在ubuntu下防火墙相关的命令：
* sudo ufw disable #关闭防火墙
* sudo ufw enable #开启防火墙
* sudo ufw status #查看防火墙状态
* sudo ufw allow 22 #开通22端口

* ---------------------------------------------------------------------------
* 待整理命令：


## 时间相关的命令：
* mtime(modification time)文件的内容更改时间
* ctime(status time)文件的权限属性更改时间
* atime(access time)文件上次被访问读取的时间
* 'touch filename'创建文件,-a:修改文件的访问时间,-m:修改文件的内容更改时间


* 软件安装卸载相关的命令？？？：
* yum和apt-get(apt??)是Linux中两个常用软件安装命令，绝大部分软件都可以用这两个命令进行安装，相当于应用商店
* 'yum search python'搜索yum支持的python版本
* 'yum install python'安装python
* 'yum groupinstall package_name' 安装新包 
* 'apt-get'只能用于ubuntu还是也需要安装才能使用
* 'apt-get update'ubuntu下更新软件源，一般在下载新软件之前可能需要更新一下
* 'apt-get install software_name'安装软件
* 'apt-get remove --purge software_name'卸载软件
* 'pip'安装python库
* yum和apt注意可能需要把镜像资源配置为国内的，否则国外的镜像源可能被墙，造成安装软件时连接失败
* 'apt update'  配置新的镜像资源后需要重新更新下载
* 'curl http:...' web请求？？？



* 'make'命令？？
* 经常会下载一些安装包到本地，解压后进入目录直接输入'make'命令就可以安装
* 完成安装后会在安装目录下编译产生一个src目录，里面有很多命令，进入到该目录下，然后./file_name就会执行相应的命令
* 如果把这个文件拷贝到环境变量路径下，就可以实现在任意位置执行命令
* wget http://download.redis.io/releases/redis-2.8.17.tar.gz
* tar xzf redis-2.8.17.tar.gz
* cd redis-2.8.17
* make

* source命令？？？：
* source命令也称为点命令，也就是一个点符号. ,是bash的内部命令
* 可以使使Shell读入指定的Shell程序文件并依次执行文件中的所有语句
* source命令通常用于重新执行刚修改的初始化文件，使之立即生效，而不必注销并重新登录
* 'source filename'或'. filename' 执行filename文件
* 'source ~/.bashrc'使刚修改过的.bashrc文件立即生效
* 'source /etc/profile'使刚修改过的配置文件立即生效
* 'source file'和'sh file' 执行脚本时的区别：？？？
* https://www.cnblogs.com/ThatsMyTiger/p/6865817.html

* 服务相关的命令？？？：
* '/etc/init.d/ssh restart'重启ssh服务
* 'service vsftpd restart'重启vsftpd服务 
* 'service vsftpd start'启动vsftpd服务 
* 'service vsftpd stop'关闭vsftpd服务 
* 上面几个操作执行完后都没有反应，没有任何返回信息？
* 'service vsftpd status'查看vsftpd服务状态


* 'open host_ip port'打开ftp命令,
* 'rpm -qa | grep ftp'查看服务器上是否安装了ftp服务？？
* 'rpm'的功能？？




* 'diff a b' 比较两个文件的不同

* 替代top的htop，和替代grep的ag命令（https://github.com/ggreer/the_silver_searcher）



* 文件相关的命令？？？：
* ln -s  <源文件或目录>  <软链接地址>
* 软链接可以是针对文件，也可以是针对目录
* 当 我们需要在不同的目录，用到相同的文件时，我们不需要在每一个需要的目录下都放一个必须相同的文件，\
* 我们只要在某个固定的目录，放上该文件，然后在其它的 目录下用ln命令链接（link）它就可以，不必重复的占用磁盘空间
* 相当于windows系统中的快捷方式
* 软链接的删除、修改？？软连接与硬链接的区别？？

