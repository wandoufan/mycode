# 主要记录一些Linux的命令：


# 系统运行等级相关命令：
# 'ctrl+Alt+F1~F6':切换文字界面登陆tt1~tt6终端(level 3)
# 'ctrl+Alt+F7'：切换到图像界面(level 5)
# 'startx': 在文件界面切换到图形界面(前提是有X windows系统)
# 'init': 切换执行等级
# 系统运行等级(run level)总共有7级：
# run level 0:关机
# run level 3:纯命令行模式
# run level 5:图形界面模式
# run level 6:重启


# 系统关机相关命令：
# 'logoff'命令注销
# 'exit'命令表示注销，也可以用'ctrl+d'来代替实现
# 'shutdown'命令关机 '-h now'/'-h 10:30'/'-h +10'关机，'-r now'重启
# 'poweroff'命令关机
# 'init 0'命令关机
# 'reboot'命令重启


# 系统基本命令：
# 'ctrl+c'键可以停止当前运行的程序
# 'date +[%Y/%m/%d %H:%M]'命令显示时间日期
# 'cal'命令显示日历
# 'bc'命令调用计算器
# 'md5sum 文件名'查看计算和检验MD5信息签名。
# 'man 命令'查看命令的操作说明(manual)
# 'help 命令'或'命令 -help'查看Linux内置命令的帮助
# 'info 命令'查看命令的详细信息
# 'type 命令'查看命令是否为bash的内置命令(file表示外部命令，alias表示是别的命令的别名，builtin表示内置命令)
# 'nano' 文本编辑器
# 'sync' 把内存中的数据写入硬盘中保存，常用于关机前操作
# 'echo $PATH'查询环境变量路径
# 'touch 文件名'快速创建空的文件
# 'file filename'查看文件的类型，即属于ASCII文件或是data文件或是binary文件
# 'alias 命令别名='原命令''设置命令别名，例如:'alias lm='ls -l|more''
# 'alias'不加任何参数可以查看当前设置的所有命令别名
# 'unalias 命令别名'取消历史设置的命令别名
# 'history'查看bash中输入过的所有命令
#  n:n为数字，列出最近输入过的n条命令,注意没有横杠-
# -c:清除shell中所有的历史记录


# 查看系统基本信息：
# 'uname -a'显示机器名，操作系统和内核的详细信息
# 'hostname'显示或者设置当前系统的主机名
# 'cat /etc/issue'查看Linux是什么操作系统(redhat/centos/ubuntu/fedora)
# 'cat /proc/version'查看Linux的版本号
# 'free'查看系统内存使用情况
# 'stat'显示文件或文件系统的状态
# 'uptime'显示系统时间，系统运行时间，当前系统登录用户及负载情况
# 'df -h'列出文件系统的整体磁盘使用量，与当前所在的工作目录无关
# -a:列出所有文件系统，-h:以GB,MB,KB等格式显示，-i：以inode的数量来展示
# 'du filename/dirname'评估文件或目录所占用的容量，与当前的工作目录有关
# -a:列出所有的文件与目录容量(默认不包含子目录中的文件容量信息)
# -h:以GB,MB,KB等格式显示,-s:仅列出总量，不列出各个文件本身的占用容量
# 'du -sh *'列出当前目录下的所有目录大小，不包括子目录的子目录
# 'env'列出所有的环境变量及其对应的值
# 'locale -a'列出linux系统支持的所有语系
# 'top'实时显示系统资源使用情况,相当于windows进程管理器
# -d seconds:指定每两次屏幕信息刷新之间的时间间隔
# -p pid:指定监控进程ID来仅仅监控某个进程的状态。
# -s:使top命令在安全模式中运行。这将去除交互命令所带来的潜在危险。 
# -i:使top不显示任何闲置或者僵死进程。 
# -c:显示整个命令行而不只是显示命令名
# top进程列表中各个字段的含义： 
# PID — 进程id
# USER — 进程所有者
# PR — 进程优先级
# NI — nice值。负值表示高优先级，正值表示低优先级
# VIRT — 进程使用的虚拟内存总量，单位kb。VIRT=SWAP+RES
# RES — 进程使用的、未被换出的物理内存大小，单位kb。RES=CODE+DATA
# SHR — 共享内存大小，单位kb
# S — 进程状态。D=不可中断的睡眠状态 R=运行 S=睡眠 T=跟踪/停止 Z=僵尸进程
# %CPU — 上次更新到现在的CPU时间占用百分比
# %MEM — 进程使用的物理内存百分比
# TIME+ — 进程使用的CPU时间总计，单位1/100秒
# COMMAND — 进程名称（命令名/命令行）


# 查看文件目录相关的命令：
# 'ls'命令是列出目录内容(List Directory Contents)
# 'ls -l'命令以详情模式(long listing fashion)列出文件夹的内容。
# 'ls -a'命令会列出文件夹里的所有内容，包括以"."开头的隐藏文件。
# 'lsblk'就是列出块设备。除了RAM外，以标准的树状输出格式，整齐地显示块设备。
# 'lsblk -l'命令以列表格式显示块设备(而不是树状格式)。
# 'tree'以树状结构列出当前路径或指定路径的文件，使用之前可能需要安装


# 文件和目录操作相关的命令：
# 'cd'切换目录，-:刚才的目录，~:用户的主文件夹，..:代表当前目录的上层目录
# 'pwd'显示当前目录，-p:获取正确的路径，而不是连接文件的路径
# 'mkdir dirname'新建一个目录,-m 777:创建文件时顺便设置文件权限
# 'mkdir -p a/b/c'一次性新建多层目录
# 'rmdir dirname'删除一个空目录,-p:连同上层的空的目录也一起删除
# 'cp 源文件/文件夹 目标文件/文件夹'复制文件/文件夹
# -i:若目标文件已存在，询问是否要覆盖，-r:递归持续复制，用于复制目录，-u:仅当源文件更新时才覆盖
# 'rm 文件/文件夹'删除文件/文件夹-f:强制删除，-r:递归删除非空的文件夹，-i：删除前询问
# 'mv 源文件/文件夹 目标文件/文件夹'移动文件/文件夹或给文件重命名
# -f:强制覆盖，-i:若目标文件存在询问是否覆盖，-u:仅当源文件更新时才覆盖
# 'rename'用于对批量文件进行重命名
# 'basename path'获取路径中最后的文件名
# 'dirname path'获取路径中除了文件名的部分


# 查看文件内容相关的命令：
# 'cat'从第一行开始显示文件内容
# 'tac'从最后一行开始显示文件内容
# 'nl'显示内容的同时显示行号
# 'more'一页一页的显示文件内容
# 'less'可以往前翻页
# 'head'只看头几行
# 'tail'只看结尾几行
# 'od'以二进制方式读取文件


# 时间相关的命令：
# mtime(modification time)文件的内容更改时间
# ctime(status time)文件的权限属性更改时间
# atime(access time)文件上次被访问读取的时间
# 'touch filename'创建文件,-a:修改文件的访问时间,-m:修改文件的内容更改时间


# 权限相关的命令：
# 'chgrp [-R] 用户组名 dirname/filename'改变文件/文件夹所属的用户组
# 'chown [-R] 用户名 dirname/filename'改变文件/文件夹的所有者
# 'chmod 777 dirname/filename'改变文件/文件夹权限，r:4,w:2,x:1
# 'chmod a-wx dirname/filename',u:user,g:group,o:others,a:all,+:增加,-:删除,=:设置
# 'umask'查看数字形态的创建文件时的默认权限值
#  root用户默认为0022，一般用户默认为0002，777减去输出的后三位数值即为实际的权限值
# 'umask -s'查看符号形态的默认权限值
# 'umask number'修改设置默认权限值
# 'chattr +i filename/dirname'设置文件的隐藏属性，chattr命令只有在Ext2/Ext3文件系统上有效
# +:增加某个参数，其他不变;-:删除某个参数，其他不变;=:仅有后面接的参数
# a:设置a参数后文件只能增加数据，不能删除或修改原有数据，只有root才能设置这个属性
# i:设置i参数后文件不能被删除或改名，设置连接也无法写入或添加数据，只有root才能设置这个属性
# 'lsattr -a filename/dirname'显示出文件的隐藏属性


# 文件查找相关的命令：
# 'which 命令'寻找执行文件(命令)的路径，-a:将PATH目录可以找到的所有命令都列出来，而不是只列第一个
# 注意：which默认是查找环境变量PATH内所规范的目录，如cd命令这种bash内置的命令就无法找到
# 'whereis filename/dirname'寻找特定文件（完整的文件名）
# 'locate keyword'给出文件的部分名称按照关键字查找，-i:忽略大小写的差异
# 注意：whereis和locate命令都是利用数据库来查询数据，并没有实际查询硬盘，所以速度很快
# 数据库默认每天执行一次更新回写，可能会有新创建的文件找不到的情况，可以用'updatedb'手动更新
# 'find [PATH] [option] [filename]'通过查找硬盘找到目标文件，find功能非常强大，参数很多，具体如下：
# 1.与时间有关的参数：-atime,-ctime,-mtime;以mtime为例：
# -mtime n:n为数字,列出在n天之前的那一天被更改过的文件
# -mtime +n:列出在n天之前(不含n天本身)被更改过的文件名
# -mtime -n:列出在n天之内(含n天本身)被更改过的文件
# <----(+n天之前)---<---(第n天)--->---(-n天之内)---->现在
# -newer filename：列出比指定文件还要新的文件
# 'find / -mtime 0'列出系统中24小时内被更改过的文件，0代表今天当前时间
# 'find /etc -newer /etc/password'列出在/etc目录下中比password文件还要新的文件
# 2.与用户或用户组相关的参数:
# -uid n:n是用户账户名对应的数字，即UID,存放在/etc/passwd
# -gid n:n是用户组名对应的数字，即GID,存放在/etc/group
# -user name:name是用户账户名
# -group name:name是用户组名
# -nouser:寻找文件的所有者不在/etc/passwd中的文件
# -nogroup:寻找文件的所有用户组不存在/etc/group中的文件
# 'find /home -user user':寻找/home下属于user用户的文件
# 'find / -nouser':寻找系统中不属于任何用户的文件(例如删除某个账户后，该账户之前创建的文件就属于无主文件)
# 3.在于文件权限及名称有关的参数：
# -name filename:查找文件名为filename的文件
# -size [+-]size:查找比指定尺寸还要大/小的文件，尺寸单位c代表byte,k代表kb
# 'find /home -size +50k'：查找/home中文件大于50kb的文件
# -type TYPE:查找指定类型的文件，类型有一般文件(f),设备文件(b,c),目录(d),连接文件(l),socket(s),FIFO(p)
# -perm mode:查找文件权限刚好等于mode的文件，mode为权限属性，如777
# -perm -mode:查找文件权限包括全部mode权限的文件
# -perm +mode:查找文件权限包含任一mode权限的文件
# 'find / -name passwd':查找系统中文件名为passwd的所有文件
# 'find /var -type s':查找/var目录中类型为socket的所有文件


# 文件传输相关的命令：
# 在xshell等客户端软件界面中可以通过直接拖动来传输文件
# 注意：使用rz/sz等传输命令前可能要先安装
# 注意：需要使用SecureCRT或者Xshell等客户端工具连接Linux,在客户端上运行rz/sz命令
# 'rz -be'弹出文件选择窗口从Windows上向linux中上传文件，常用-be参数
# -a:以文本方式传输，确定传输的文件是文本格式时可以用
# -b:以二进制方式传输
# -e:对控制字符进行转义，可以保证文件传输正确
# 'sz filename'从Linux中下载文件到windows中


# 与解压缩相关的命令：
# 'gzip filename'新建*.gz格式的压缩文件(对象只能是文件不能是文件夹)，应用最广泛，可以解开大多数格式压缩文件
# -d:解开压缩文件,-v:显示压缩比等信息,-k:压缩后保留原文件
# 默认状态下生成压缩文件后原文件会被删除，gzip生成的文件在windows中可以被rar软件解压缩
# 'zcat *.gz'不用解压缩，直接读出*.gz格式的文本文件的内容
# 'bzip2 filename'新建*.bz2格式的压缩文件(对象只能是文件不能是文件夹)，拥有更好的压缩比
# -d:解开压缩文件,-k:压缩后保留原文件,-z:新建压缩文件(可以不写),-v:显示压缩比等信息
# 'bzcat *.bz2'不用解压缩，直接读出*.bz2格式的文本文件的内容
# tar命令功能强大，可以将多个文件或目录打包成一个大文件，并使用gzip/bzip2进行压缩
# 'tar [-j|-z] [cv] [-f new_tar_filename] filename'打包与压缩
# 'tar [-j|-z] [tv] [-f new_tar_filename]'查看压缩包包含的文件名
# 'tar [-j|-z] [xv] [-f new_tar_filename] [-C 目录]'解压缩
# -j:通过bzip2方式进行解压缩，文件格式为*.tar.bz2
# -z:通过gzip方式进行解压缩，文件格式为*.tar.gz
# -c:新建打包文件
# -x:解开打包文件或者压缩文件
# -t:查看打包文件包含的文件名
# -v:在解压缩的过程中，显示正在处理的文件名
# -f 新建的文件名：f参数后面接要被处理的tar文件的完整文件名(也可以包含路径)
# -C 目录：在解开压缩时指定解压缩的路径
# 注意：-c,-t,-x三个参数不能同时出现在一个命令里
# 'zip -r new_filename.zip filename'指定文件生成*.zip格式的文件
# -r:递归的将目标目录下的所有文件和子目录都打包压缩，如果没有这个参数只会压缩一个空的目标文件夹！
# 'zip -r b.zip a test.txt'将a目录和test.txt文本文件合并压缩为一个b.zip压缩包
# 'unzip *.zip -d path'把*.zip格式的文件解压
# -d path：指定文件的解压路径，不加该参数也可以，默认会解压到压缩文件所在目录
# -v:不用解压缩，直接查看*.zip压缩包中的文件
# -t:验证压缩包中文件是否完整，是否有错
# 注意：rar命令可能需要安装才能使用，命令中的参数没有横杠-
# 'rar a new_filename.rar filename'指定文件生成*.rar格式的文件
# 'unrar e *.rar'把*.rar格式的文件解压


# 用户账户管理相关的命令：
# 'useradd username'添加新用户
# -m:自动创建用户的登录目录，注意必须加上该参数，否则创建的新用户在/home下没有用户目录
# -d path:指定用户目录的路径，默认为/home/username
# -u uid:指定UID，0~499默认是保留给系统用户账号使用的，所以该值必须大于499
# -g groups:指定用户所属的群组，值为GID，默认为100，即users
# -e:指定账号的失效日期，日期格式为MM/DD/YY，例如06/30/12,默认为永久有效
# -f:指定密码过期多少天后禁用账户，如果为0账号立即被停用，如果为-1则账号一直可用，默认值为-1
# -s:指定用户登入后所使用的shell,默认值为/bin/bash
# 'usermod username'修改系统已经存在的用户的属性
# 'userdel username'删除用户
# 'groupadd'新创建建用户组
# -g gid:指定新建工作组的GID
# -r:创建系统工作组，系统工作组的组ID小于500
# 'passwd username'修改或初次设置用户密码，注意不是password
# 'chage'修改用户密码有效期限等属性
# 'id'查看用户的uid,gid及归属的用户组
# 'su - username' 切换当前用户
# 'sudo'以root身份执行事先在sudoers文件允许过的命令，如果没有提前允许，需要手动输入密码
# 'who'显示当前登录用户的信息
# 'users'显示当前所有登录用户的用户列表


# 基础网络操作相关的命令：
# 'ssh username@host_ip'使用SSH加密协议远程登录
# 'telnet'使用TELNET协议远程登录(telnet因为采用明文传送报文，安全性不好，很多Linux服务器都不开放telnet服务)
# 'ifconfig'查看、配置、启用或禁用网络接口的命令,注意不是ipconfig
# 'scp'即secure copy，用于不同主机之间复制文件
# 'ping'测试主机之间网络的连通性
# 'wget'命令行下载文件
# 'route'显示和设置linux系统的路由表
# 'ifup'启动网卡
# 'ifdown'关闭网卡
# 'netstat'查看网络状态
# 'ss'查看网络状态


# 可以作为管道命令的一些命令:
# 管道命令"|"中仅能处理前一个命令传递过来的正确信息(stdout)，不能直接处理错误信息(stderr)
# 每个管道后边接的第一个数据必须是能接受标准输入(stdin)的命令，例如：cat ,less等，另外例如：ls,cp,mv就不是管道命令
# 在管道命令中stdin和stdout可以用减号'-'来代替
# 'cut file/stdin' 以行为单位选取信息，将同一行的数据进行分解后取出需要的部分，常用于log日志文件分析提取等地方
# -d:后面接上分割字符，与-f一起使用
# -f:依靠-d的分割字符将信息切割成数段，-f表示取出其中的第几段
# -c:以字符的单位取出固定的字符区间
# 'echo $PATH | cut -d ':' -f 3,5' 以':'为分隔符分割环境变量，并取出其中的第三和第五段
# 'cat test1.txt | cut -d ' ' -f 3' 以空格为分隔符分割test1.txt，并取出其中的第三段
# 'cat test1.txt | cut -c 5-12' 选取出test1.txt中的第五个到第十二个字符
# 'cat test1.txt | cut -c 5-' 选取出test1.txt中的第五个到最后一个字符
# 'grep 目标字符串 file/stdin' 以行为单位分析信息，若当中有我们需要的信息，就将该行取出来
# -c:计算找到目标字符串的次数
# -i:忽略大小写
# -n:输出行号
# -v:反向选择，即显示没有目标字符串的行
# --color=auto:在行中给目标字符串加上颜色
# 'cat test1.txt | grep -i 'hello'' 选取test1.txt中所有包含'hello'字符串的行
# 'sort file/stdin' 给目标文件或接收到的标准输入排序
# -f:忽略大小写
# -b:忽略最前面的空格
# -n:以纯数字为标准排序(默认以文字类型排序)
# -r:反向排序
# -u:相同的数据仅出现一行代表，相当于去重
# -t:后边接分割符
# -k:后边接数字，表示分割后的第几个区间
# 'cat test1.txt | sort -f' 把test1.txt中的每一行按首字母进行排序后显示，注意原文件的数据顺序不会改变
# 'uniq file/stdin' 给目标文件或接收到的标准输入显示时去除重复
# -i:忽略大小写
# -c:给每行的重复数计数
# 'cat test1.txt | uniq -c' 把test1.txt中的重复行去除后显示
# 'wc file/stdin' 给目标文件或接收到的标准输入显示行数，字数等详细信息
# -l:仅列出行数
# -w:仅列出英文单字数
# -m:仅列出字符数
# 'cat test1.txt | wc' 列出test1.txt中的字符数等信息
# 'tee filename'表示双向重定向，既把数据都输入filename文件中，又在屏幕上显示出结果来
# -a:以追加的方式把数据加入filename中
# 'ls -l | tee filename' 把ls -l命令的结果显示出来并写入filename中
# 'tr' 用来删除或替换字符串
# -d:后边接目标字符串，删除目标字符串
# -s:后边接旧字符串和新字符串，替换指定字符串
# 'cat test1.txt | tr '[a-z]' '[A-Z]'' 把输出的test1.txt中的小写都替换为大写，注意原文件的大小写不会变
# 'join file1 file2' 把两个文件当中有相同数据的那一行加在一起，注意文件被join使用前要先sort排序处理
# 'paste file1 file2' 把两个文件中每行的内容直接加起来，中间用[tab]键隔开
# 'expand filename' 把文件中的[tab]键转换成空格
# 'split filename prefix' 把大的file文件切割成小的文件，其中prefix代表切割文件的前导文字
# -b:后边接要切割成的大小，单位为b,k,m
# -l:按行数来切割


# 变量操作相关的命令：
# 'read 变量名'读取来自键盘输入的变量，可以实现与用户的交互
# -p:后边接给用户的提示符，例如'read -p 'input your name:' username'
# -t:后边接等待用户输入的秒数
# 'declare 变量名'/'typeset 变量名'声明变量的类型
# -a:设置变量为数组类型(array),数组设置方式为'array[index]=content',显示为'echo "${array[1]},${array[2]}"'
# -i:设置变量为整数类型(integer)
# -x:设置变量为环境变量/全局变量，等同export
# +x:把环境变量变为自定义变量，等同export的逆操作
# -r:设置变量为readonly,该类型不可以被更改内容，也不能被重设
# -p:查看变量当前的数据类型和数值
# 'export 变量名'来把变量变成全局变量/环境变量,用于变量需要在其他子进程执行的情况
# 'unset 变量名' 取消变量 


# 在ubuntu下防火墙相关的命令：
# sudo ufw disable #关闭防火墙
# sudo ufw enable #开启防火墙
# sudo ufw status #查看防火墙状态


# 待整理命令：
# '/etc/init.d/ssh restart'重启ssh服务
# 'service vsftpd restart'重启vsftpd服务 
# 'service vsftpd start'启动vsftpd服务 
# 'service vsftpd stop'关闭vsftpd服务 
# 上面几个操作执行完后都没有反应，没有任何返回信息？
# 'service vsftpd status'查看vsftpd服务状态
# 服务相关的命令？
# 'netstat -apn | grep port'查看占用指定端口的进程以及进程的PID
# 'kill -9 PID'杀掉指定PID对应的进程
# 'nohup python a.test &'？？？守护进程，关掉xshell之后进程还会继续运行
# 'open host_ip port'打开ftp命令,
# 'apt-get update'ubuntu下更新软件源，一般在下载新软件之前可能需要更新一下
# 'apt-get install software_name'安装软件
# 'apt-get purge software_name'卸载软件
# 'wget'从指定URL上下载数据？？
# 'mget'从ftp上下载数据
# 'rpm -qa | grep ftp'查看服务器上是否安装了ftp服务？？