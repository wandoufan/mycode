# coding:utf-8

# 测试从ftp中读取数据,在linux服务器环境运行

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
