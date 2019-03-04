# 主要记录linux中的隐藏bash文件

## 在Linux的普通用户目录或root用户目录下有四个隐藏文件：
* .bash_history  记录之前输入的命令
* .bash_logout  当你退出时执行的命令
* .bash_profile  当你登入shell时执行，仅在会话开始时读取一次
* .bashrc  当你登入shell时执行，每次打开新的终端时都要被读取

## 关于.bash_profile文件：
* 可以在.bash_profile文件之后添加用户局部环境变量
* 每次.bash_profile文件被修改后都要运行'source ~/.bash_profile'命令才能生效

## 关于.bashrc文件：
* 'vim ~/.bashrc' 查看bashrc文件
* 修改.bashrc可以改变环境变量PATH、别名alias和提示符
* 详细见链接：https://blog.csdn.net/eleanoryss/article/details/70207767
* 有些软件会在安装时向.bashrc文件中添加用户局部环境变量
* 每次.bashrc文件被修改后都要运行'source ~/.bashrc'命令才能生效