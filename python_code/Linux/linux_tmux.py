# tmux是指通过一个终端登录远程主机并运行后，在其中可以开启多个控制台的终端复用软件
# 可以使用Ports安装tmux，位置在/usr/ports/sysutils/tmux/
# tmux仅有一个依赖包libevent，位于/usr/ports/devel/libevent/
# tmux的系统级配置文件为/etc/tmux.conf,用户级配置文件为~/.tmux.conf,配置文件实际上就是tmux的命令集合


# tmux常用命令：
# 'tmux new -s session_name' 新建一个会话
# 'tmux ls' 查看现有的会话
# 'tmux a' 进入最近的会话
# 'tmux a -t session_name'或'tmux attach -t session_name' 进入指定会话
# 'tmux detach' 离开会话
# 'tmux kill-session -t session_name' 关闭指定会话
# 注意：一般不建议在新建会话中去嵌套新建/进入其他新建会话