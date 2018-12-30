# 主要记录Linux的各个文件目录

# 注意：/data 指根目录下的data目录，./data 指当前目录下的data目录，./.data 指当前目录下的隐藏data目录

# Linux的三层目录：
# /(root,根目录)：与开机系统有关的;
# /usr(unix software resourse)：与软件安装执行有关;
# /var(variable):与系统运行过程有关;


# 1.根目录(/)：
# /bin:放置在单用户维护模式下还能被操作的命令，/bin下的命令都是基本命令，可以被root和一般账号使用
# /boot:放置开机中会使用到的文件,包括Linux内核文件、开机菜单、开机所需的配置文件
# /dev:所有的设备和接口设备都是以文件的形式存放在/dev目录中
# /etc:放置系统的配置文件，如用户的账号密码文件、各种服务的起始文件等
# /home:放置除root外的一般用户的主文件夹
# /lib:放置开机时会用到的函数库，以及在/bin中命令需要调用的函数库
# /media:放置可删除的设备，包括软盘、光盘、DVD
# /mnt:暂时挂载某些额外的设备，类似于/media
# /opt:放置第三方软件或自行安装的软件
# /root:系统管理员root的主文件夹
# /sbin:放置开机、修复、还原系统所需要的命令
# /srv:一些网络服务service启动后服务所需要的数据目录
# /tmp:一般用户或正在执行的程序放置临时文件的地方，任何人都能访问，可以定期清理
# /lost+found:仅当使用ext2/ext3文件系统格式才会产生该目录，当文件系统发生错误时存放一些丢失的片段
# /proc:放置系统内核，进程，网络状态等信息，目录属于虚拟文件系统，即数据都放置内存中，不占用硬盘空间
# /sys:放置系统内核相关的信息，类似于/proc，都是虚拟文件系统


# 2./usr目录：(放置可分享且不可变动的数据)
# /usr/X11R6/:放置X window的重要数据
# /usr/bin/:绝大部分的用户命令都放在这里，与/bin目录中命令的区别在于是否与开机过程有关
# /usr/include/：放置C/C++等程序语言的头文件，包含文件
# /usr/lib/:放置各种应用软件的函数库，目标文件
# /usr/local/bin:系统管理员在本机自行下载安装的软件，即非distribution提供的文件
# /usr/sbin/:放置非系统正常运行时需要的系统命令
# /usr/share/:放置共享文件，数据都是文本文件，不分硬件架构都可以读取
# /usr/src/:放置源码文件


# 3./var目录：
# /var/cache/:放置应用程序运行过程中产生的一些缓存文件
# /var/lib/:放置程序运行过程中需要使用到的数据文件
# /var/lock/:对于某些只能被一个程序同时调用的资源，设置锁文件
# /var/log/:放置登陆文件
# /var/mail/:放置个人电子邮箱信箱
# /var/run/:放置某些程序或服务的PID
# /var/spool/:放置一些队列数据，即排队等待其他程序使用的数据


