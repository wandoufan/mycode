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

ftp.dir()#显示目录下所有目录信息，测试发现一般返回是None

ftp.nlst()#获取目录下的文件，返回结果是一个包含目录中所有文件的列表
# 相当于os.listdir(path)

ftp.mkd(pathname)#新建远程目录,一次只能建一层目录

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

----------------------------------------------------------------------------------------
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

--------------------------------------------------------------------------------------------
# 代码实现对ftp目录的上传
# 只实现了上传功能，下载功能可以用wget实现,不需要像上传一样进行逐层遍历

import ftplib
import os

# 1.传递之前要检查目标目录是否是空的
# 2.传递结束之后要检查传输是否成功(检查文件个数？/*resp* '226 Transfer complete.'？)
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

    def check_file_number(self,dir):
        '''
        上传之后检查ftp的每个目录下文件数量与本地文件数量是否一致，
        不一致就报错
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
        # 先检查要创建的目录是否已经存在
        if dirname in self.ftp.nlst():
            return -1, 'directory already exist!'
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

-------------------------------------------------------------------------------------------
# 代码功能：wget方式从ftp下载目录，对指定路径下的所有文件打包并上传压缩包到ftp

import ftplib
import os


class MyFtp(object):
    """
    实现训练数据目录下载
    和训练结果/评估结果上传的功能
    """
    ftp = ftplib.FTP()

    def __init__(self, host, port, username, password):
        '''
        初始化连接登录ftp
        :param host:ftp主机
        :param port:ftp端口
        :param username:用户名
        :param password:密码
        '''
        # 连接或登录失败时返回信息？
        self.ftp.set_debuglevel(2)
        self.ftp.connect(host, port)
        self.ftp.login(username, password)

    def create_zipfile(self, zip_file_path):
        '''
        创建zip格式的压缩包 
        :param zip_file_path：要进行压缩的数据的路径
        :return:code,msg
        '''
        os.chdir(zip_file_path)
        cmd = 'zip -r release.zip *'
        os.system(cmd)
        if os.path.isfile(os.path.join(zip_file_path, 'release.zip')):
            return 0, 'OK'
        else:
            code = -1
            msg = 'create zip file failed'
            return code, msg

    def download(self, user, password, localpath, remotepath):
        '''
        wget方式从ftp下载train-data数据
        ftp训练数据路径：train-data/V0.1
        :param user:用户名
        :param password:密码
        :param localpath:要下载数据到本地的路径
        :param download_remotepath:要从ftp上下载数据的路径
        return code,msg
        '''
        # 下载前检查ftp服务器上对应的数据是否存在
        version = os.path.basename(remotepath)
        self.ftp.cwd('train-data')
        data_list = self.ftp.nlst()
        if version not in data_list:
            code = -1
            msg = 'ftp data %s not found' %version
            return code, msg

        # 下载前检查本地目标路径中是否已经存在数据
        local_train_data = os.path.join(localpath,version)
        if os.path.isdir(local_train_data):
            code = -1
            msg = 'local data %s already exist' %version
            return code, msg

        cmd1 = 'wget -nH -r -l inf -P %s --ftp-user=%s --ftp-password=%s ftp://192.168.109.133/%s' %(localpath, user, password, remotepath)
        os.system(cmd1)
        # 下载到本地后要把目标数据从上层目录中挪出来，之后再删除上层目录
        cmd2 = 'mv %s/train-data/%s %s/%s' %(localpath, version, localpath, version)
        os.system(cmd2)
        cmd3 = 'rmdir %s/train-data' %localpath
        os.system(cmd3)

        # 检查数据是否下载成功
        if os.path.isdir(local_train_data):
            return 0, 'OK'
        else:
            code = -1
            msg = 'download file failed'
            return code, msg

    def upload_train_data(self, localpath, remotepath):
        '''
        向ftp上传压缩包格式的训练结果
        本地训练结果:/home/work/workdir/model-data/V0.1/output/release/release.zip 
        ftp训练结果路径: model-data/V0.1/output
        :param localpath：要上传的训练结果的路径
        :param remotepath: 要上传到ftp上的路径
        :return:code,msg
        '''
        # 上传之前先检查要上传的数据是否存在
        if not os.path.isdir(localpath):
            code = -1
            msg = 'local data not exist'
            return code, msg

        # 上传前检查ftp上对应路径是否存在，如果不存在，需要先逐层建立目录
        self.ftp.cwd('/home/user')# 正式服务器上登入ftp后的默认路径为'/',需要修改？
        if 'model-data' not in self.ftp.nlst():
            self.ftp.mkd('model-data')
        self.ftp.cwd('model-data')
        if 'V0.1' not in self.ftp.nlst():
            self.ftp.mkd('V0.1')
        self.ftp.cwd('V0.1')
        if 'output' not in self.ftp.nlst():
            self.ftp.mkd('output')
        self.ftp.cwd('output')

        code, msg = self.create_zipfile(localpath)
        if code == -1:
            return code, msg
        zipfile = os.path.join(localpath, 'release.zip')
        upload_file = open(zipfile,'rb')
        self.ftp.storbinary('STOR %s/release.zip' %remotepath, upload_file)
        upload_file.close()

        # 检查文件是否上传成功
        self.ftp.cwd('/home/user/model-data/V0.1/output')# 需要具体修改？
        if 'release.zip' not in self.ftp.nlst():
            code = -1
            msg = 'upload data failed'
            return code, msg
        else:
            return 0, 'OK'

    def upload_evaluation_data(self, localpath, remotepath):
        '''
        向ftp上传压缩包格式的评估结果
        本地评估结果:/home/work/workdir/assessment-data/V0.1/2/output/release/release.zip
        ftp评估结果路径：assessment-data/V0.1/2/output 
        :param localpath：要上传的评估结果的路径
        :param remotepath: 要上传到ftp上的路径
        :return:code,msg
        '''
        # 上传之前先检查要上传的数据是否存在
        if not os.path.isdir(localpath):
            code = -1
            msg = 'local data not exist'
            return code, msg

        # 上传前检查ftp上对应路径是否存在，如果不存在，需要先逐层建立目录
        self.ftp.cwd('/home/user')# 正式服务器上登入ftp后的默认路径为'/',需要修改？
        if 'assessment-data' not in self.ftp.nlst():
            self.ftp.mkd('assessment-data')
        self.ftp.cwd('assessment-data')
        if 'V0.1' not in self.ftp.nlst():
            self.ftp.mkd('V0.1')
        self.ftp.cwd('V0.1')
        if '2' not in self.ftp.nlst():
            self.ftp.mkd('2')
        self.ftp.cwd('2')
        if 'output' not in self.ftp.nlst():
            self.ftp.mkd('output')
        self.ftp.cwd('output')

        code, msg = self.create_zipfile(localpath)
        if code == -1:
            return code, msg
        zipfile = os.path.join(localpath, 'release.zip')
        upload_file = open(zipfile,'rb')
        self.ftp.storbinary('STOR %s/release.zip' %remotepath, upload_file)
        upload_file.close()

        # 检查文件是否上传成功
        self.ftp.cwd('/home/user/assessment-data/V0.1/2/output')# 需要具体修改？
        if 'release.zip' not in self.ftp.nlst():
            code = -1
            msg = 'upload data failed'
            return code, msg
        else:
            return 0, 'OK'


if __name__ == '__main__':
    host = '192.168.109.133'
    port = 21
    user = 'user'
    password = '123456'

    myftp = MyFtp(host, port, user, password)

    download_localpath = '/root/download'
    download_remotepath = 'train-data/V0.1'
    code, msg = myftp.download(user, password, download_localpath, download_remotepath)
    print('!!!!!',code,msg)
    
    upload_train_localpath = '/root/workdir/model-data/V0.2/output/release'
    upload_train_remotepath = '/home/user/model-data/V0.2/output/'

    upload_evaluation_localpath = '/root/workdir/assessment-data/V0.2/2/output/release'
    upload_evaluation_remotepath = '/home/user/assessment-data/V0.2/2/output/'

    code, msg = myftp.upload_train_data(upload_train_localpath, upload_train_remotepath)
    print('!!!!!',code,msg)
    code, msg = myftp.upload_evaluation_data(upload_evaluation_localpath, upload_evaluation_remotepath)
    print('!!!!!',code,msg)












