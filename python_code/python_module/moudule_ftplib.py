# coding:utf-8

# ftplib模块用来处理ftp登录上传下载等一系列操作

# 注意：和shell中的ftp命令一样只能传输单个文件，无法传输目录！
# 传输目录需要自己逐层遍历目录然后ftp上建立对应目录，然后再上传文件，详见下面代码实现

import ftplib

# 初始化：
ftp = ftplib.FTP()# 初始化一个ftp对象

ftp.set_debuglevel(2)# 打开调试级别2，显示详细信息

ftp.set_debuglevel(0)# 关闭调试模式

ftp.connect(hostip,port)# 要连接的服务器IP，端口

ftp.login(user,password)# 连接的用户名密码

# ftp基本命令：
ftp.cwd(pathname)#设置FTP当前操作的路径
# 特别地，用ftp.cwd(..)来返回上层目录

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
# 注意：只能传输单个文件，无法传输目录！
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

# 测试从ftp中上传下载单个文件,在linux服务器环境运行

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

---------------------------------------------------------------------------------
# 代码实现对ftp目录的上传
# 只实现了上传功能，未完待续......

import ftplib
import os

# 1.传递之前要检查目标目录是否是空的
# 2.传递结束之后要检查传输是否成功(检查文件个数？？传输反馈结果200？？)
# 3.考虑目录内容列表为空，即空目录的情况-->建一个空目录，然后回退到上一级

class MyFtp(object):
    """
    实现ftp传输复杂文件目录的功能,
    递归的判断目标数据是文件还是目录，
    然后执行不同的操作
    """
    ftp = ftplib.FTP()

    def __init__(self, host, port, username, password):
        '''
        初始化连接登录ftp
        param host:ftp主机
        param port:ftp端口
        param username:用户名
        param password:密码
        '''
        self.ftp.set_debuglevel(2)
        self.ftp.connect(host, port)
        self.ftp.login(username, password)

    def check_is_empty(self,dir):
        '''
        上传下载之前检查目标目录是否为空，不为空就报错
        '''
        pass

    def upload_file(self, localfile, remotepath):
        '''
        上传单个文件
        :param localfiel:要上传的本地文件(path1/path2/filename)
        :param remotefile:要上传到ftp上的目标路径(path1/path2)
        :return:code,msg
        '''
        if os.path.isfile(localfile) == False:
            code = -1
            msg = 'not a file'
            return code, msg
        filename = os.path.basename(localfile)
        remotefile = os.path.join(remotepath, filename)
        upload_file = open(localfile, 'rb')
        self.ftp.storbinary('STOR %s' % remotefile, upload_file)
        upload_file.close()
        return 0, 'OK'

    def upload_directory(self, localdir, remotepath):
        '''
        上传目录
        :param localdir:要上传的本地目录
        :param remotedir:要上传到ftp上的目标路径
        return:code,msg
        '''
        # 在ftp上创建对应的目录并设置为工作目录
        self.ftp.cwd(remotepath)
        dirname = os.path.basename(localdir)
        self.ftp.mkd(dirname)
        remotepath = os.path.join(remotepath,dirname)
        self.ftp.cwd(remotepath)

        file_list = os.listdir(localdir)
        if len(file_list) == 0:
            return 0, 'directory is empty'

        for file in file_list:
            if os.path.isfile(os.path.join(localdir, file)):
                localfile = os.path.join(localdir, file)
                code, msg = self.upload_file(localfile, remotepath)
                if code == -1:
                    return code, msg
                if code == 0:
                    continue
            else:
                localdir = os.path.join(localdir, file)
                code, msg = self.upload_directory(localdir, remotepath)
                # 遍历结束把路径改回上一层目录
                localdir = os.path.dirname(localdir)
                if code == -1:
                    return code, msg
                if code == 0:
                    continue
        return 0, 'OK'

    def start_upload(self, localdir, remotepath):
        '''
        开始上传，首先判断要上传的数据是文件还是目录
        :param localdir:要上传的本地目录
        :param remotedir:要上传到ftp上的目标路径
        return:code,msg
        '''
        # 如果localdir是文件直接上传，否则调用目录上传函数
        if os.path.isfile(localdir):
            code, msg = self.upload_file(localdir, remotepath)
            if code == -1:
                return code, msg
        else:
            code, msg = self.upload_directory(localdir, remotepath)
            if code == -1:
                return code, msg
        return 0, 'OK'

if __name__ == '__main__':
    host = '192.168.109.133'
    port = 21
    user = 'user'
    password = '123456'

    myftp = MyFtp(host,port,user,password)
    
    localdir = '/root/ftptest/abc'
    remotepath = '/home/user/ftptest'
    myftp.start_upload(localdir,remotepath)




















