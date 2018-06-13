# coding:utf-8

# ftplib模块用来处理ftp登录上传下载等一系列操作

import ftplib

# 初始化：
ftp = ftplib.FTP()# 初始化一个ftp对象

ftp.set_debuglevel(2)# 打开调试级别2，显示详细信息

ftp.set_debuglevel(0)# 关闭调试模式

ftp.connect(hostip,port)# 要连接的服务器IP，端口

ftp.login(user,password)# 连接的用户名密码

# ftp基本命令：
ftp.cwd(pathname)#设置FTP当前操作的路径

ftp.dir()#显示目录下所有目录信息

ftp.nlst()#获取目录下的文件

ftp.mkd(pathname)#新建远程目录

ftp.pwd()#返回当前所在位置

ftp.rmd(dirname)#删除远程目录

ftp.delete(filename)#删除远程文件

ftp.rename(fromname, toname)#将fromname改名为toname

ftp.close()#单方面断开ftp连接

ftp.quit()#发送quit命令给ftp服务器之后退出ftp

# ftp上传下载：
ftp.storbinaly(cmd,fp,blocksize=8192,callback=None,rest=None)#上传目标文件
# cmd参数是一个STOR命令，例如cmd='STOR a.txt'
# fp参数是一个以二进制方式打开的文件句柄，例如fp=open('a.txt','rb')
# blocksize参数设置缓冲区大小，例如blocksize=1024
ftp.storlines(cmd,fp,callback=None)#上传文本文件,可选的回调函数callback用于处理文件的每一行

ftp.retrbinary(cmd,callback,blocksize=8192,rest=None)#下载目标文件,回调函数callback用于处理文件的每一块（块大小默认为 8KB）
# cmd参数是一个RETR命令，例如cmd='RETR a.txt'
# callback参数是对文件句柄的函数操作，例如fp=open('a.txt','wb'),callback=fp.write
ftp.retrlines(cmd,callback=None)#下载文本文件,可选的回调函数callback用于处理文件的每一行

# STOR和RETR是ftp协议中的上传和下载命令
# 'STOR a.txt'表示告知服务器准备上传a.txt文件
# 'RETR a.txt'表示告知服务器准备下载a.txt文件

----------------------------------------------------------------------------
# 代码示例：

# coding:utf-8

# 测试从ftp中上传下载数据,在linux服务器环境运行

import ftplib

host = '192.168.109.133'
user = 'user'
password = '123456'
bufsize = 1024

ftp = ftplib.FTP()

ftp.set_debuglevel(2)

ftp.connect(host)

ftp.login(user,password)

def download():
	'''
	下载文件：
	将ftp服务器上的/home/user/ftptest/a/params.txt下载
	并写入本地的/root/ftptest路径下，文件重命名为params1.txt
	备注：params1.txt文件会在写入文件时自动创建，不需要提前创建
	'''
    serverfile = '/home/user/ftptest/a/params.txt'
    download_file = open('/root/ftptest/params1.txt','wb')
    ftp.retrbinary('RETR %s' %serverfile,download_file.write,bufsize)
    ftp.set_debuglevel(0)
    download_file.close()
    
def upload():
    '''
    上传文件：
    将本地/root/ftptest/的README文件内容读出来并上传到ftp服务器的/home/user/ftptest/a路径下
    文件名仍为README
    '''
    localfile = '/root/ftptest/README'
    upload_file = open(localfile,'rb')
    ftp.storbinary('STOR /home/user/ftptest/a/README',upload_file,bufsize)
    ftp.set_debuglevel(0)
    upload_file.close()

if __name__ == '__main__':
	download()
    upload()
    ftp.quit()























